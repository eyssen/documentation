#!/usr/bin/env python3
"""Generate sitemap.xml from a Sphinx HTML build tree.

This project's Makefile builds languages in separate passes:

    make html                     # English  -> _build/html/
    make html CURRENT_LANG=hu     # Hungarian -> _build/html/hu/

sphinx-sitemap is a poor fit here: each sphinx-build only sees one language,
the default URL scheme would emit /en/ and /18.0/ prefixes that this site does
not use, and locale_dirs still contains unpublished languages. Walking the
published HTML after each pass produces a single sitemap at the site root
covering whatever pages actually exist (EN, HU, or both).

Usage:
    python3 scripts/generate_sitemap.py _build/html
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import escape

DEFAULT_BASE_URL = "https://doc.eyssen.com/"

# Sphinx copies these next to the pages; they are not published content.
SKIP_DIRS = frozenset({
    "_static",
    "_sources",
    "_images",
    "_downloads",
    "_modules",
})

# Sphinx utility pages and the sitemap itself.
SKIP_FILENAMES = frozenset({
    "search.html",
    "genindex.html",
    "py-modindex.html",
    "404.html",
    "sitemap.xml",
})

# redirects extension writes a one-line meta-refresh stub (see extensions/redirects).
REDIRECT_MARKER = 'http-equiv="refresh"'
REDIRECT_MAX_BYTES = 400


def iter_html_pages(html_root: Path):
    """Yield published HTML pages under html_root, skipping artifacts."""
    for path in html_root.rglob("*.html"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(html_root).parts):
            continue
        if path.name in SKIP_FILENAMES:
            continue
        if _is_redirect_page(path):
            continue
        yield path


def _is_redirect_page(path: Path) -> bool:
    try:
        size = path.stat().st_size
    except OSError:
        return False
    if size > REDIRECT_MAX_BYTES:
        return False
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False
    return REDIRECT_MARKER in text


def page_to_loc(html_root: Path, page: Path, base_url: str) -> str:
    """Map a built HTML file to its public absolute URL.

    index.html is published as the directory URL (trailing slash), matching
    conf.py's canonical URL builder. Other pages keep their .html suffix.
    """
    relative = page.relative_to(html_root).as_posix()
    if relative.endswith("/index.html"):
        relative = relative[: -len("index.html")]
    elif relative == "index.html":
        relative = ""
    # quote() keeps slashes; UTF-8 pages stay valid sitemap loc values.
    return base_url.rstrip("/") + "/" + quote(relative, safe="/")


def collect_locs(html_root: Path, base_url: str) -> list[str]:
    locs = {page_to_loc(html_root, page, base_url) for page in iter_html_pages(html_root)}
    return sorted(locs)


def render_sitemap(locs: list[str]) -> str:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for loc in locs:
        lines.append("  <url>")
        lines.append(f"    <loc>{escape(loc)}</loc>")
        lines.append("  </url>")
    lines.append("</urlset>")
    lines.append("")
    return "\n".join(lines)


def generate_sitemap(html_root: Path, base_url: str = DEFAULT_BASE_URL) -> tuple[Path, int]:
    """Write sitemap.xml at the HTML root. Return (path, url_count)."""
    if not html_root.is_dir():
        raise FileNotFoundError(f"HTML build directory does not exist: {html_root}")
    locs = collect_locs(html_root, base_url)
    dest = html_root / "sitemap.xml"
    dest.write_text(render_sitemap(locs), encoding="utf-8")
    return dest, len(locs)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "html_root",
        type=Path,
        help="Sphinx HTML output root (typically _build/html)",
    )
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"Public site origin (default: {DEFAULT_BASE_URL})",
    )
    args = parser.parse_args(argv)

    html_root = args.html_root.resolve()
    try:
        dest, count = generate_sitemap(html_root, args.base_url)
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote {count} URLs to {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

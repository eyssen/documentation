"""Unit tests for scripts/generate_sitemap.py (no Sphinx build required)."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from generate_sitemap import DEFAULT_BASE_URL, generate_sitemap  # noqa: E402


REDIRECT_HTML = '<html><head><meta http-equiv="refresh" content="0; url=../applications.html"/></head></html>'
PAGE_HTML = "<html><head><title>Doc</title></head><body><p>content</p></body></html>"


class GenerateSitemapTest(unittest.TestCase):
    def test_combined_en_and_hu_tree(self):
        with tempfile.TemporaryDirectory() as tmp:
            html_root = Path(tmp)
            (html_root / "index.html").write_text(PAGE_HTML, encoding="utf-8")
            (html_root / "applications.html").write_text(PAGE_HTML, encoding="utf-8")
            (html_root / "search.html").write_text(PAGE_HTML, encoding="utf-8")
            (html_root / "genindex.html").write_text(PAGE_HTML, encoding="utf-8")
            (html_root / "_static").mkdir()
            (html_root / "_static" / "dummy.html").write_text(PAGE_HTML, encoding="utf-8")
            (html_root / "applications" / "general").mkdir(parents=True)
            (html_root / "applications" / "general" / "old_page.html").write_text(
                REDIRECT_HTML, encoding="utf-8"
            )

            hu = html_root / "hu"
            hu.mkdir()
            (hu / "index.html").write_text(PAGE_HTML, encoding="utf-8")
            (hu / "applications.html").write_text(PAGE_HTML, encoding="utf-8")
            (hu / "search.html").write_text(PAGE_HTML, encoding="utf-8")

            dest, count = generate_sitemap(html_root)
            self.assertEqual(dest, html_root / "sitemap.xml")
            self.assertEqual(count, 4)
            xml = dest.read_text(encoding="utf-8")

            self.assertIn(f"<loc>{DEFAULT_BASE_URL}</loc>", xml)
            self.assertIn(f"<loc>{DEFAULT_BASE_URL}hu/</loc>", xml)
            self.assertIn(f"<loc>{DEFAULT_BASE_URL}applications.html</loc>", xml)
            self.assertIn(f"<loc>{DEFAULT_BASE_URL}hu/applications.html</loc>", xml)

            self.assertNotIn("search.html", xml)
            self.assertNotIn("genindex.html", xml)
            self.assertNotIn("_static", xml)
            self.assertNotIn("old_page.html", xml)
            self.assertTrue(xml.startswith("<?xml version="))
            self.assertIn('xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"', xml)

    def test_missing_html_root(self):
        with self.assertRaises(FileNotFoundError):
            generate_sitemap(Path("/tmp/does-not-exist-eyssen-sitemap"))


if __name__ == "__main__":
    unittest.main()

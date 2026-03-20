#!/usr/bin/env python3
"""
Sync Hungarian PO files with POT source templates.

- Creates new .po files from .pot templates (msginit)
- Updates existing .po files: adds new strings, marks obsolete (msgmerge)
- Preserves all existing valid translations
- Reports statistics on new/obsolete entries

Requires: brew install gettext

Usage:
    python3 scripts/sync_po.py           # sync all
    python3 scripts/sync_po.py --dry-run # show what would change
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import polib
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "polib"], check=True)
    import polib

ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / "locale" / "sources"
HU_DIR = ROOT / "locale" / "hu" / "LC_MESSAGES"

# POT files that don't need translation (build artifacts, not content)
SKIP_POTS = {"last_build", "sphinx"}


def find_tool(name: str) -> str | None:
    """Find gettext tool in PATH or common brew locations."""
    path = shutil.which(name)
    if path:
        return path
    for prefix in ("/opt/homebrew/bin", "/usr/local/bin"):
        candidate = Path(prefix) / name
        if candidate.exists():
            return str(candidate)
    return None


def count_entries(po_path: Path) -> dict:
    """Count translated/untranslated/fuzzy/obsolete entries in a PO file."""
    po = polib.pofile(str(po_path))
    return {
        "translated": len(po.translated_entries()),
        "untranslated": len(po.untranslated_entries()),
        "fuzzy": len(po.fuzzy_entries()),
        "obsolete": len(po.obsolete_entries()),
        "total": len(po),
    }


def main():
    parser = argparse.ArgumentParser(description="Sync HU PO files with POT templates")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change")
    args = parser.parse_args()

    msgmerge = find_tool("msgmerge")
    msginit = find_tool("msginit")

    if not msgmerge:
        print("ERROR: msgmerge not found. Install with: brew install gettext")
        sys.exit(1)

    HU_DIR.mkdir(parents=True, exist_ok=True)

    pot_files = sorted(SOURCES_DIR.glob("*.pot"))
    pot_names = {p.stem for p in pot_files} - SKIP_POTS
    po_names = {p.stem for p in HU_DIR.glob("*.po")}

    # Report orphaned PO files (no matching POT)
    orphans = po_names - pot_names
    if orphans:
        print(f"⚠ Orphaned PO files (no matching POT): {', '.join(sorted(orphans))}")
        print()

    stats_rows = []

    for pot in pot_files:
        if pot.stem in SKIP_POTS:
            continue

        po = HU_DIR / f"{pot.stem}.po"

        if not po.exists():
            # --- Create new PO ---
            if args.dry_run:
                print(f"  CREATE   {po.name}")
                stats_rows.append({"file": po.name, "action": "create"})
                continue

            if msginit:
                subprocess.run(
                    [msginit, "--no-translator", "-l", "hu",
                     "-i", str(pot), "-o", str(po)],
                    check=True, capture_output=True,
                )
            else:
                # Fallback: copy POT with header fixup
                content = pot.read_text(encoding="utf-8")
                content = content.replace(
                    '"Language: \\n"', '"Language: hu\\n"'
                ).replace(
                    '"Language-Team: LANGUAGE <LL@li.org>\\n"',
                    '"Language-Team: Hungarian <hu@li.org>\\n"',
                )
                po.write_text(content, encoding="utf-8")

            counts = count_entries(po)
            print(f"  CREATE   {po.name}  ({counts['total']} strings)")
            stats_rows.append({"file": po.name, "action": "create", **counts})
        else:
            # --- Update existing PO ---
            before = count_entries(po) if not args.dry_run else None

            if args.dry_run:
                print(f"  UPDATE   {po.name}")
                stats_rows.append({"file": po.name, "action": "update"})
                continue

            result = subprocess.run(
                [msgmerge, "--update", "--backup=none", str(po), str(pot)],
                capture_output=True, text=True,
            )

            if result.returncode != 0:
                print(f"  ERROR    {po.name}: {result.stderr.strip()}")
                continue

            after = count_entries(po)
            new_strings = max(0, after["untranslated"] - before["untranslated"])
            new_fuzzy = max(0, after["fuzzy"] - before["fuzzy"])

            status = "OK"
            details = []
            if new_strings > 0:
                details.append(f"+{new_strings} new")
                status = "UPDATED"
            if new_fuzzy > 0:
                details.append(f"+{new_fuzzy} fuzzy")
                status = "UPDATED"
            if after["obsolete"] > before["obsolete"]:
                details.append(f"+{after['obsolete'] - before['obsolete']} obsolete")
                status = "UPDATED"

            detail_str = f"  ({', '.join(details)})" if details else ""
            print(f"  {status:8s} {po.name}{detail_str}")
            stats_rows.append({"file": po.name, "action": status.lower(), **after})

    # Summary
    print(f"\n{'═' * 60}")
    if not args.dry_run:
        total_untranslated = sum(r.get("untranslated", 0) for r in stats_rows)
        total_fuzzy = sum(r.get("fuzzy", 0) for r in stats_rows)
        total_translated = sum(r.get("translated", 0) for r in stats_rows)
        total_all = sum(r.get("total", 0) for r in stats_rows)
        print(f"  Translated:   {total_translated:6d}")
        print(f"  Untranslated: {total_untranslated:6d}")
        print(f"  Fuzzy:        {total_fuzzy:6d}")
        print(f"  Total:        {total_all:6d}")
        if total_all > 0:
            pct = total_translated / total_all * 100
            print(f"  Coverage:     {pct:.1f}%")
    print()


if __name__ == "__main__":
    main()

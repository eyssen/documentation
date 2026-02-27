#!/usr/bin/env python3
"""
Initialize Hungarian (hu) locale from POT files.
Creates locale/hu/LC_MESSAGES/*.po from locale/sources/*.pot
"""
from pathlib import Path

LOCALE_DIR = Path(__file__).resolve().parent.parent / "locale"
SOURCES_DIR = LOCALE_DIR / "sources"
HU_LC_MESSAGES = LOCALE_DIR / "hu" / "LC_MESSAGES"


def init_hu_locale():
    HU_LC_MESSAGES.mkdir(parents=True, exist_ok=True)

    for pot_file in SOURCES_DIR.glob("*.pot"):
        po_file = HU_LC_MESSAGES / pot_file.with_suffix(".po").name
        content = pot_file.read_text(encoding="utf-8")

        # Update header for Hungarian: Language-Team + add Language: hu
        # Note: In .pot/.po files, \n in quoted strings is stored as backslash-n
        content = content.replace(
            '"Language-Team: LANGUAGE <LL@li.org>\\n"',
            '"Language-Team: Hungarian <hu@li.org>\\n"\n'
            '"Language: hu\\n"',
        )
        # Add Plural-Forms for Hungarian
        content = content.replace(
            '"Content-Transfer-Encoding: 8bit\\n"',
            '"Content-Transfer-Encoding: 8bit\\n"\n'
            '"Plural-Forms: nplurals=2; plural=(n != 1);\\n"',
        )
        # Add Language: hu line (POT doesn't have it, PO needs it)
        content = content.replace(
            '"Language-Team: LANGUAGE <LL@li.org>\n"',
            '"Language-Team: Hungarian <hu@li.org>\n"'
            '"Language: hu\n"',
        )

        po_file.write_text(content, encoding="utf-8")
        print(f"Created {po_file.relative_to(LOCALE_DIR)}")


if __name__ == "__main__":
    init_hu_locale()
    print("Hungarian locale initialized. Edit .po files in locale/hu/LC_MESSAGES/ to add translations.")

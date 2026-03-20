#!/usr/bin/env python3
"""
Translate PO files to Hungarian using Claude CLI (Sonnet).

Uses the claude CLI with -p (pipe mode) — works with Claude subscription,
no API key needed.

Usage:
    python3 scripts/translate_po.py                        # all files, missing only
    python3 scripts/translate_po.py --file finance.po      # single file
    python3 scripts/translate_po.py --force                # retranslate everything
    python3 scripts/translate_po.py --dry-run              # preview without translating
    python3 scripts/translate_po.py --model claude-sonnet-4-6  # specific model
    python3 scripts/translate_po.py --batch-size 30        # larger batches

Requires: pip install polib, claude CLI (npm install -g @anthropic-ai/claude-code)
"""
import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

try:
    import polib
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "polib"], check=True)
    import polib

HU_DIR = Path(__file__).resolve().parent.parent / "locale" / "hu" / "LC_MESSAGES"

DEFAULT_MODEL = "claude-sonnet-4-6"
DEFAULT_BATCH_SIZE = 20

SYSTEM_PROMPT = """\
You are a professional translator for Odoo ERP documentation (English → Hungarian).

RULES:
- Use formal Hungarian ("Ön" form, not "te")
- Use standard Hungarian IT/ERP terminology consistently
- DO NOT translate these RST constructs (keep them exactly as-is):
  :doc:, :ref:, :guilabel:, :menuselection:, :command:, :file:, :icon:,
  :class:, :attr:, :meth:, :func:, :data:, :option:, :abbr:, :dfn:,
  ``code literals``, **bold markers**, *italic markers*
- DO NOT translate: URLs, file paths, Python/JS code, variable names
- DO NOT translate proper nouns: Odoo, PostgreSQL, Python, JavaScript, XML, CSV, etc.
- PRESERVE exactly as-is: all whitespace, \\n newlines, RST formatting
- PRESERVE placeholders: %(name)s, %s, %d, {variable}
- For :menuselection:`A --> B --> C`, translate A, B, C but keep ` --> ` separators
- For :guilabel:`Label`, translate only the visible Label text inside backticks

OUTPUT FORMAT:
Return ONLY a valid JSON object: {"translations": ["fordítás1", "fordítás2", ...]}
The "translations" array MUST have EXACTLY the same number of items as the input "strings" array.
Do not include any other text, explanation, or markdown formatting."""


def translate_batch(texts: list[str], model: str) -> list[str]:
    """Send a batch of strings to Claude CLI for translation."""
    payload = json.dumps({"strings": texts}, ensure_ascii=False)
    prompt = (
        f"Translate these {len(texts)} English strings to Hungarian.\n"
        f"Return JSON with key \"translations\" containing exactly {len(texts)} items.\n\n"
        f"{payload}"
    )

    full_prompt = f"{SYSTEM_PROMPT}\n\n---\n\n{prompt}"

    try:
        result = subprocess.run(
            ["claude", "-p", "--model", model, "--output-format", "text"],
            input=full_prompt,
            capture_output=True,
            text=True,
            timeout=180,
        )

        if result.returncode != 0:
            print(f"\n    ERROR: claude exit code {result.returncode}: {result.stderr[:200]}")
            return texts

        output = result.stdout.strip()

        # Extract JSON — Claude might wrap it in ```json ... ```
        json_match = re.search(r'\{[^{}]*"translations"\s*:\s*\[[\s\S]*?\]\s*\}', output)
        if json_match:
            parsed = json.loads(json_match.group())
        else:
            parsed = json.loads(output)

        translations = parsed.get("translations", [])

        if len(translations) != len(texts):
            print(f" ⚠ {len(translations)}/{len(texts)}", end="")
            if len(translations) < len(texts):
                translations += texts[len(translations):]
            else:
                translations = translations[:len(texts)]

        return translations

    except subprocess.TimeoutExpired:
        print(" TIMEOUT", end="")
        return texts
    except json.JSONDecodeError as e:
        print(f" JSON error: {e}", end="")
        return texts
    except Exception as e:
        print(f" ERROR: {e}", end="")
        return texts


def get_entries_to_translate(po: polib.POFile, force: bool) -> list[polib.POEntry]:
    """Get entries that need translation."""
    if force:
        entries = list(po)
    else:
        entries = po.untranslated_entries() + po.fuzzy_entries()

    # Filter: skip empty msgid (header) and pure URLs
    return [
        e for e in entries
        if e.msgid.strip() and not re.match(r"^https?://\S+$", e.msgid.strip())
    ]


def translate_file(
    po_path: Path, model: str, batch_size: int,
    force: bool = False, dry_run: bool = False
) -> dict:
    """Translate a single PO file. Returns stats."""
    po = polib.pofile(str(po_path))
    entries = get_entries_to_translate(po, force)

    total_in_file = len([e for e in po if e.msgid.strip()])
    already = total_in_file - len(po.untranslated_entries()) - len(po.fuzzy_entries())

    print(f"\n{'─' * 60}")
    print(f"  {po_path.name}: {len(entries)} to translate"
          f" (already done: {already}/{total_in_file})")

    if not entries:
        return {"file": po_path.name, "translated": 0, "total": 0, "skipped": 0}

    if dry_run:
        for e in entries[:5]:
            preview = e.msgid[:80].replace("\n", "\\n")
            print(f"    → {preview}...")
        if len(entries) > 5:
            print(f"    ... +{len(entries) - 5} more")
        return {"file": po_path.name, "translated": 0, "total": len(entries), "skipped": 0}

    translated_count = 0
    skipped_count = 0
    total_batches = (len(entries) + batch_size - 1) // batch_size

    for i in range(0, len(entries), batch_size):
        batch = entries[i : i + batch_size]
        batch_num = i // batch_size + 1
        texts = [e.msgid for e in batch]

        print(f"  [{batch_num}/{total_batches}] {len(texts)} strings...", end="", flush=True)
        translations = translate_batch(texts, model)

        for entry, translation in zip(batch, translations):
            if translation and translation != entry.msgid:
                entry.msgstr = translation
                if "fuzzy" in entry.flags:
                    entry.flags.remove("fuzzy")
                translated_count += 1
            else:
                skipped_count += 1

        # Save after each batch — safe to interrupt and resume
        po.save(str(po_path))
        print(f" ✓ {translated_count}", flush=True)

        # Small delay between batches
        if batch_num < total_batches:
            time.sleep(0.5)

    print(f"  Saved: {translated_count} translated, {skipped_count} skipped")
    return {
        "file": po_path.name,
        "translated": translated_count,
        "total": len(entries),
        "skipped": skipped_count,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Translate Odoo docs PO files to Hungarian using Claude CLI"
    )
    parser.add_argument("--file", action="append", dest="files",
                        help="PO file name(s) to translate (repeatable, e.g. --file finance.po --file hr.po)")
    parser.add_argument("--exclude", action="append", default=[],
                        help="PO file name(s) to skip (repeatable, e.g. --exclude developer.po)")
    parser.add_argument("--force", action="store_true",
                        help="Retranslate ALL entries (including already translated)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be translated, no API calls")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"Claude model (default: {DEFAULT_MODEL})")
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE,
                        help=f"Strings per API call (default: {DEFAULT_BATCH_SIZE})")
    args = parser.parse_args()

    # Verify claude CLI is available
    try:
        ver = subprocess.run(
            ["claude", "--version"], capture_output=True, text=True, check=True
        )
        print(f"Claude CLI: {ver.stdout.strip()}")
    except FileNotFoundError:
        print("ERROR: 'claude' CLI not found.")
        print("Install: npm install -g @anthropic-ai/claude-code")
        sys.exit(1)

    # Collect files
    exclude_names = {e.replace(".po", "") for e in args.exclude}
    if args.files:
        files = []
        for f in args.files:
            po_path = HU_DIR / f if not Path(f).is_absolute() else Path(f)
            if not po_path.exists():
                print(f"File not found: {f}")
                sys.exit(1)
            files.append(po_path)
    else:
        files = sorted(HU_DIR.glob("*.po"))

    # Apply exclusions
    if exclude_names:
        files = [f for f in files if f.stem not in exclude_names]

    if not files:
        print("No PO files found. Run sync_po.py first.")
        sys.exit(1)

    mode = "FORCE (retranslate all)" if args.force else "missing + fuzzy only"
    print(f"Mode:       {mode}")
    print(f"Model:      {args.model}")
    print(f"Batch size: {args.batch_size}")
    print(f"Files:      {len(files)}")

    stats = []
    start_time = time.time()

    for f in files:
        result = translate_file(f, args.model, args.batch_size, args.force, args.dry_run)
        stats.append(result)

    elapsed = time.time() - start_time

    # Summary
    print(f"\n{'═' * 60}")
    print("SUMMARY")
    total_translated = sum(s["translated"] for s in stats)
    total_entries = sum(s["total"] for s in stats)
    for s in stats:
        if s["total"] > 0:
            print(f"  {s['file']:30s}  {s['translated']:5d} / {s['total']:5d}")
    print(f"\n  Total: {total_translated} / {total_entries} strings translated")
    print(f"  Time:  {elapsed:.0f}s")


if __name__ == "__main__":
    main()

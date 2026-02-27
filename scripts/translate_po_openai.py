#!/usr/bin/env python3
"""
Translate Odoo documentation PO files to Hungarian using OpenAI API.

Usage:
    python3 scripts/translate_po_openai.py --api-key sk-...
    python3 scripts/translate_po_openai.py --api-key sk-... --file locale/hu/LC_MESSAGES/index.po
    python3 scripts/translate_po_openai.py --api-key sk-... --all
    python3 scripts/translate_po_openai.py --api-key sk-... --all --model gpt-4o-mini

Notes:
- Skips already translated strings (non-empty msgstr)
- Preserves RST markup, :doc:, :ref:, guilabel etc.
- Saves progress after each batch; safe to interrupt and resume
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

try:
    from openai import OpenAI
except ImportError:
    print("Installing openai package...")
    os.system(f"{sys.executable} -m pip install openai")
    from openai import OpenAI

LOCALE_DIR = Path(__file__).resolve().parent.parent / "locale" / "hu" / "LC_MESSAGES"

SYSTEM_PROMPT = """You are a professional technical translator specializing in ERP software documentation.
Translate English texts to Hungarian.

STRICT RULES:
- Use professional/formal Hungarian tone
- DO NOT translate: RST roles (:doc:, :ref:, :guilabel:, :menuselection:, :icon:, :class:, :attr:, :meth:, etc.)
- DO NOT translate: code, variable names, URLs, file paths, module names
- DO NOT translate: Odoo, eYssen, Python, JavaScript, PostgreSQL and other proper nouns
- PRESERVE all whitespace, newlines (\\n), and RST formatting exactly
- PRESERVE placeholders: %(name)s, {variable}, %s, %d
- You will receive a JSON object: {"strings": ["text1", "text2", ...]}
- You MUST return a JSON object: {"translations": ["fordítás1", "fordítás2", ...]}
- The "translations" array MUST have EXACTLY the same number of items as "strings"
- Translate each string independently, in order"""

BATCH_SIZE = 10  # smaller = more reliable


# ── PO file parsing ──────────────────────────────────────────────────────────

def decode_po_string(raw: str) -> str:
    """Convert PO quoted string block to plain text."""
    parts = re.findall(r'"((?:[^"\\]|\\.)*)"', raw)
    result = ''.join(parts)
    return (result
            .replace('\\n', '\n')
            .replace('\\t', '\t')
            .replace('\\"', '"')
            .replace('\\\\', '\\'))


def encode_po_string(text: str) -> str:
    """Encode plain text as PO quoted string (single or multiline)."""
    escaped = (text
               .replace('\\', '\\\\')
               .replace('"', '\\"')
               .replace('\t', '\\t'))
    if '\n' not in escaped:
        return f'"{escaped}"'
    # multiline
    lines = escaped.split('\n')
    parts = ['""']
    for i, line in enumerate(lines):
        suffix = '\\n' if i < len(lines) - 1 else ''
        if line or suffix:
            parts.append(f'"{line}{suffix}"')
    return '\n'.join(parts)


def find_translatable_entries(content: str) -> list[dict]:
    """
    Find all msgid/msgstr pairs where msgstr is empty.
    Returns list of dicts: {msgid_text, msgid_raw, entry_start, msgstr_empty_start}
    """
    entries = []

    # Match full msgid block + msgstr block
    pattern = re.compile(
        r'(?<!#\n)(msgid\s+(?:"[^"]*"\s*\n)*"[^"]*")\s*\n'
        r'(msgstr\s+"")\s*\n',
        re.MULTILINE
    )

    for m in pattern.finditer(content):
        msgid_raw = m.group(1)
        msgid_text = decode_po_string(msgid_raw.replace('msgid ', '', 1).strip())

        # Skip empty msgid (header)
        if not msgid_text.strip():
            continue
        # Skip pure URLs
        if re.match(r'^https?://', msgid_text):
            continue

        entries.append({
            'msgid_text': msgid_text,
            'msgid_raw': msgid_raw,
            'msgstr_pos': m.start(2),    # position of `msgstr ""`
            'msgstr_len': len(m.group(2)),
        })

    return entries


# ── Translation ───────────────────────────────────────────────────────────────

def extract_translations_from_response(parsed, expected_count: int, originals: list[str]) -> list[str]:
    """Robustly extract a list of strings from OpenAI JSON response."""
    result = None

    if isinstance(parsed, list):
        result = parsed
    elif isinstance(parsed, dict):
        # Try known keys first
        for key in ('translations', 'translated', 'results', 'output', 'strings'):
            val = parsed.get(key)
            if isinstance(val, list):
                result = val
                break
        if result is None:
            # Take first list value
            for val in parsed.values():
                if isinstance(val, list):
                    result = val
                    break
        if result is None:
            raise ValueError(f"No list found in response dict: {list(parsed.keys())}")
    else:
        raise ValueError(f"Unexpected response type: {type(parsed)}")

    # Flatten if nested (model sometimes wraps each item in a list)
    flat = []
    for item in result:
        if isinstance(item, list):
            flat.extend(str(x) for x in item)
        else:
            flat.append(str(item) if not isinstance(item, str) else item)
    result = flat

    # Fix count
    if len(result) < expected_count:
        print(f"  WARNING: got {len(result)}/{expected_count}, padding with originals")
        result += originals[len(result):]
    elif len(result) > expected_count:
        print(f"  WARNING: got {len(result)}/{expected_count}, truncating")
        result = result[:expected_count]

    return result


def translate_batch(client: OpenAI, texts: list[str], model: str) -> list[str]:
    """Translate a batch of strings via OpenAI. Returns originals on error."""
    payload = json.dumps({"strings": texts}, ensure_ascii=False)
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": (
                        f'Translate the following {len(texts)} strings to Hungarian. '
                        f'Return a JSON object with key "translations" containing exactly {len(texts)} items.\n'
                        f'{payload}'
                    )
                }
            ],
            temperature=0.1,
            response_format={"type": "json_object"},
        )
        raw = response.choices[0].message.content
        if raw is None:
            raise ValueError("Empty response from API")
        parsed = json.loads(raw)
        return extract_translations_from_response(parsed, len(texts), texts)

    except Exception as e:
        print(f"  API error: {e}")
        time.sleep(3)
        return texts  # Fall back to originals


# ── PO file update ────────────────────────────────────────────────────────────

def apply_translations_to_content(content: str, entries: list[dict], translations: dict[str, str]) -> str:
    """
    Apply translations to PO file content using byte-offset replacement.
    Works backwards so offsets stay valid.
    """
    # Sort by position descending so replacements don't shift later offsets
    to_replace = []
    for entry in entries:
        msgid_text = entry['msgid_text']
        if msgid_text in translations:
            msgstr_new = f'msgstr {encode_po_string(translations[msgid_text])}'
            to_replace.append((
                entry['msgstr_pos'],
                entry['msgstr_len'],
                msgstr_new
            ))

    to_replace.sort(key=lambda x: x[0], reverse=True)

    for pos, length, replacement in to_replace:
        content = content[:pos] + replacement + content[pos + length:]

    return content


# ── Main translation loop ─────────────────────────────────────────────────────

def translate_po_file(po_file: Path, client: OpenAI, model: str) -> dict:
    """Translate a single PO file. Returns stats dict."""
    print(f"\nTranslating: {po_file.name}")
    content = po_file.read_text(encoding='utf-8')

    entries = find_translatable_entries(content)
    print(f"  {len(entries)} strings need translation")

    if not entries:
        return {'file': po_file.name, 'translated': 0, 'total': 0}

    translations: dict[str, str] = {}
    total_batches = (len(entries) + BATCH_SIZE - 1) // BATCH_SIZE

    for batch_num, batch_start in enumerate(range(0, len(entries), BATCH_SIZE), 1):
        batch = entries[batch_start:batch_start + BATCH_SIZE]
        texts = [e['msgid_text'] for e in batch]

        print(f"  Batch {batch_num}/{total_batches} ({len(texts)} strings)...", end=' ', flush=True)
        results = translate_batch(client, texts, model)

        for entry, translation in zip(batch, results):
            if translation and translation != entry['msgid_text']:
                translations[entry['msgid_text']] = translation

        print("done")
        time.sleep(0.3)

    # Apply all translations at once
    new_content = apply_translations_to_content(content, entries, translations)
    po_file.write_text(new_content, encoding='utf-8')

    print(f"  Saved {po_file.name} ({len(translations)} strings translated)")
    return {'file': po_file.name, 'translated': len(translations), 'total': len(entries)}


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Translate Odoo docs PO files to Hungarian')
    parser.add_argument('--api-key', required=True, help='OpenAI API key')
    parser.add_argument('--model', default='gpt-4o-mini',
                        help='Model (default: gpt-4o-mini)')
    parser.add_argument('--file', help='Translate a single PO file')
    parser.add_argument('--all', action='store_true', help='Translate all PO files')
    args = parser.parse_args()

    client = OpenAI(api_key=args.api_key)

    # Test connection
    try:
        client.chat.completions.create(
            model=args.model,
            messages=[{"role": "user", "content": "Say OK"}],
            max_tokens=5
        )
        print(f"API connection OK (model: {args.model})")
    except Exception as e:
        print(f"API connection failed: {e}")
        sys.exit(1)

    po_files = []
    if args.file:
        po_files = [Path(args.file)]
    elif args.all:
        po_files = sorted(LOCALE_DIR.glob('*.po'))
    else:
        parser.print_help()
        sys.exit(0)

    stats = []
    for po_file in po_files:
        if not po_file.exists():
            print(f"File not found: {po_file}")
            continue
        result = translate_po_file(po_file, client, args.model)
        stats.append(result)

    print("\n=== Summary ===")
    total = sum(s['translated'] for s in stats)
    for s in stats:
        print(f"  {s['file']:30s}: {s['translated']:5d} / {s['total']:5d}")
    print(f"\nTotal translated: {total} strings")


if __name__ == '__main__':
    main()

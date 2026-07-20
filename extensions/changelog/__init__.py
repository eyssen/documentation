"""
Changelog extension for Sphinx.

Generates a "What's New" section on the homepage by reading git log entries.
Extracts recent commits and categorizes them as 'new', 'updated', or 'fix'
based on commit message prefixes.

When a commit message is too short or generic (e.g. "new docs"), the extension
derives one or more human-readable entries from the changed paths under
``content/`` so bulk documentation drops still appear on the homepage.
"""

import re
import subprocess

from sphinx.util import logging

_logger = logging.getLogger(__name__)

# Maximum number of changelog entries to display
MAX_ENTRIES = 10

# Number of days to look back in git history
LOOKBACK_DAYS = 180

# Commit subjects that are noise or too vague to show as-is
_GENERIC_SUBJECTS = re.compile(
    r'^(new docs?|docs?|update(s)?|wip|misc|changes?)$',
    re.I,
)

# Map content/ path segments to short topic labels (first match wins by specificity)
_TOPIC_RULES = [
    (re.compile(r'content/applications/productivity/ai'), 'AI platform documentation'),
    (re.compile(r'content/applications/sales/withdrawal'), 'EU right of withdrawal documentation'),
    (re.compile(r'content/applications/finance/accounting/bank/cash_register'),
     'Cash register documentation'),
    (re.compile(r'content/applications/finance/accounting/payments/follow_up'),
     'Payment follow-up documentation'),
    (re.compile(r'content/applications/inventory_and_mrp/inventory/shipping_receiving'),
     'Inventory shipping & receiving documentation'),
    (re.compile(r'content/applications/inventory_and_mrp/inventory/warehouses_storage'),
     'Warehouse & storage documentation'),
    (re.compile(r'content/applications/inventory_and_mrp/inventory/product_management'),
     'Product management documentation'),
    (re.compile(r'content/applications/hr/employees/equipment'), 'Equipment management documentation'),
    (re.compile(r'content/applications/productivity/sign'), 'Sign documentation'),
    (re.compile(r'content/applications/finance/'), 'Finance documentation'),
    (re.compile(r'content/applications/sales/'), 'Sales documentation'),
    (re.compile(r'content/applications/inventory_and_mrp/'), 'Inventory & MRP documentation'),
    (re.compile(r'content/applications/productivity/'), 'Productivity documentation'),
    (re.compile(r'content/applications/hr/'), 'HR documentation'),
    (re.compile(r'content/applications/websites/'), 'Website documentation'),
    (re.compile(r'content/applications/services/'), 'Services documentation'),
    (re.compile(r'content/applications/marketing/'), 'Marketing documentation'),
    (re.compile(r'content/applications/general/'), 'General settings documentation'),
    (re.compile(r'content/applications/essentials/'), 'Essentials documentation'),
    (re.compile(r'content/developer/'), 'Developer documentation'),
    (re.compile(r'content/administration/'), 'Administration documentation'),
]


def _get_git_changelog(source_dir, max_entries=MAX_ENTRIES, lookback_days=LOOKBACK_DAYS):
    """Extract recent meaningful commits from git log.

    Returns a list of dicts with keys: date, type, message.
    """
    entries = []
    try:
        result = subprocess.run(
            [
                'git', 'log',
                f'--since={lookback_days} days ago',
                '--pretty=format:%H|%ad|%s',
                '--date=format:%b %d',
                '--no-merges',
                '--diff-filter=ACDMR',
                '--',
                'content/',
            ],
            cwd=source_dir,
            capture_output=True,
            text=True,
            timeout=15,
        )

        if result.returncode != 0:
            _logger.warning('Changelog: git log failed: %s', result.stderr)
            return entries

        seen_messages = set()

        for line in result.stdout.strip().split('\n'):
            if not line or line.count('|') < 2:
                continue

            commit_hash, date_str, message = line.split('|', 2)
            message = message.strip()
            date_str = date_str.strip()

            # Skip noise commits
            msg_lower = message.lower()
            if any(skip in msg_lower for skip in [
                'merge', 'fix typo', 'minor', 'wip', 'temp', 'todo',
                'readme', 'gitignore', '.po', '.pot', 'locale/',
                'translate', 'i18n', 'rebrand', 'copyright',
            ]):
                continue

            expanded = _entries_for_commit(
                source_dir, commit_hash, date_str, message,
            )
            for entry in expanded:
                msg_key = entry['message'].lower()[:60]
                if msg_key in seen_messages:
                    continue
                seen_messages.add(msg_key)
                entries.append(entry)
                if len(entries) >= max_entries:
                    return entries

    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        _logger.warning('Changelog: could not run git: %s', e)

    return entries


def _entries_for_commit(source_dir, commit_hash, date_str, message):
    """Build one or more changelog entries for a single commit."""
    cleaned = _clean_message(message)
    generic = (
        len(message.strip('- ')) < 15
        or bool(_GENERIC_SUBJECTS.match(message.strip()))
    )

    if not generic:
        return [{
            'date': date_str,
            'type': _categorize_commit(message),
            'message': cleaned,
        }]

    # Generic / too-short subject → derive topics from changed content paths
    topics = _topics_from_commit(source_dir, commit_hash)
    if not topics:
        # Still nothing useful
        if len(cleaned) >= 10:
            return [{
                'date': date_str,
                'type': _categorize_commit(message),
                'message': cleaned,
            }]
        return []

    entry_type = _categorize_commit(message)
    # Prefer "new" when the subject itself said new/docs dump
    if entry_type == 'updated' and 'new' in message.lower():
        entry_type = 'new'

    # One entry per major topic (cap so one bulk commit cannot fill the list)
    out = []
    for topic in topics[:6]:
        out.append({
            'date': date_str,
            'type': entry_type,
            'message': f'Add {topic}' if entry_type == 'new' else topic[0].upper() + topic[1:],
        })
    return out


def _topics_from_commit(source_dir, commit_hash):
    """Return ordered unique topic labels for files changed in ``commit_hash``."""
    try:
        result = subprocess.run(
            ['git', 'show', '--name-only', '--pretty=format:', commit_hash, '--', 'content/'],
            cwd=source_dir,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return []

    if result.returncode != 0:
        return []

    topics = []
    seen = set()
    for path in result.stdout.splitlines():
        path = path.strip()
        if not path.startswith('content/'):
            continue
        for pattern, label in _TOPIC_RULES:
            if pattern.search(path):
                if label not in seen:
                    seen.add(label)
                    topics.append(label)
                break

    # Drop broad "X documentation" parents when a more specific topic under the
    # same area is already listed (e.g. keep Cash register, drop Finance).
    broad = {t for t in topics if t.endswith(' documentation') and t.count(' ') <= 2}
    # Specific labels we treat as children of broad app buckets
    children_of = {
        'Finance documentation': (
            'Cash register documentation', 'Payment follow-up documentation',
        ),
        'Inventory & MRP documentation': (
            'Inventory shipping & receiving documentation',
            'Warehouse & storage documentation',
            'Product management documentation',
        ),
        'Sales documentation': ('EU right of withdrawal documentation',),
        'Productivity documentation': ('AI platform documentation', 'Sign documentation'),
        'HR documentation': ('Equipment management documentation',),
    }
    drop = set()
    for parent, kids in children_of.items():
        if parent in seen and any(k in seen for k in kids):
            drop.add(parent)
    return [t for t in topics if t not in drop]


def _categorize_commit(message):
    """Categorize a commit message into new/updated/fix."""
    msg_lower = message.lower()

    if any(word in msg_lower for word in ['add', 'new', 'create', 'initial']):
        return 'new'
    elif any(word in msg_lower for word in ['fix', 'bug', 'correct', 'repair']):
        return 'fix'
    else:
        return 'updated'


def _clean_message(message):
    """Clean up a commit message for display."""
    # Remove bracketed prefixes: [FIX], [IMP], [ADD], etc.
    message = re.sub(r'^\[[\w/]+\]\s*', '', message)

    # Remove conventional commit prefixes: docs(scope):, fix:, feat(x):, etc.
    message = re.sub(r'^[\w]+(?:\([^)]*\))?:\s*', '', message)

    # Capitalize first letter
    if message:
        message = message[0].upper() + message[1:]

    # Truncate very long messages
    if len(message) > 120:
        message = message[:117] + '...'

    return message


def _inject_changelog(app, pagename, templatename, context, doctree):
    """Inject changelog entries into the homepage template context."""
    if pagename != app.config.master_doc:
        return

    # Use confdir (repo root with conf.py) not srcdir (content/ subdir),
    # so that the 'content/' path filter in git log resolves correctly.
    repo_dir = app.confdir
    entries = _get_git_changelog(repo_dir)
    context['changelog_entries'] = entries


def setup(app):
    """Sphinx extension setup."""
    app.connect('html-page-context', _inject_changelog)

    return {
        'version': '1.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

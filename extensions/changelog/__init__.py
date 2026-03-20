"""
Changelog extension for Sphinx.

Generates a "What's New" section on the homepage by reading git log entries.
Extracts recent commits and categorizes them as 'new', 'updated', or 'fix'
based on commit message prefixes.
"""

import subprocess
from datetime import datetime

from docutils import nodes
from sphinx.util import logging

_logger = logging.getLogger(__name__)

# Maximum number of changelog entries to display
MAX_ENTRIES = 10

# Number of days to look back in git history
LOOKBACK_DAYS = 90


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
                '--pretty=format:%ad|%s',
                '--date=format:%b %d',
                '--no-merges',
                '--diff-filter=ACDMR',
                '--',
                'content/',
            ],
            cwd=source_dir,
            capture_output=True,
            text=True,
            timeout=10,
        )

        if result.returncode != 0:
            _logger.warning('Changelog: git log failed: %s', result.stderr)
            return entries

        seen_messages = set()

        for line in result.stdout.strip().split('\n'):
            if not line or '|' not in line:
                continue

            date_str, message = line.split('|', 1)
            message = message.strip()

            # Skip noise commits
            if any(skip in message.lower() for skip in [
                'merge', 'fix typo', 'minor', 'wip', 'temp', 'todo',
                'readme', 'gitignore', '.po', '.pot', 'locale/',
            ]):
                continue

            # Deduplicate similar messages
            msg_key = message.lower()[:50]
            if msg_key in seen_messages:
                continue
            seen_messages.add(msg_key)

            # Categorize
            entry_type = _categorize_commit(message)

            entries.append({
                'date': date_str.strip(),
                'type': entry_type,
                'message': _clean_message(message),
            })

            if len(entries) >= max_entries:
                break

    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        _logger.warning('Changelog: could not run git: %s', e)

    return entries


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
    # Remove common prefixes
    for prefix in ['[FIX]', '[IMP]', '[ADD]', '[REF]', '[DOC]']:
        if message.upper().startswith(prefix):
            message = message[len(prefix):].strip()

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

    source_dir = app.srcdir
    entries = _get_git_changelog(source_dir)
    context['changelog_entries'] = entries


def setup(app):
    """Sphinx extension setup."""
    app.connect('html-page-context', _inject_changelog)

    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

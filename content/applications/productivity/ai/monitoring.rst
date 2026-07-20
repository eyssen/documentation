==========
Monitoring
==========

Administrators audit AI usage under :menuselection:`AI --> Monitoring`.

Logs
====

:menuselection:`AI --> Monitoring --> Logs` (``ai.log``)

Each significant chat/tool event can produce a log row: user, company, tool,
model, success/failure, whether sudo was used (should be false for business
ops), timing and optional payload.

- Prefer **Metadata only** log level in production.
- Full payload logs may contain personal data and secrets pasted by users —
  restrict access and retention accordingly.
- Logs are kept for audit; run **steps** have a separate retention setting.

Violations
==========

:menuselection:`AI --> Monitoring --> Violations`

Security-relevant events (blocked patterns, channel denials, policy abuses,
etc.) create violation records. Accumulated strikes in the configured window
lead to a temporary ban.

Review violations to:

- spot prompt-injection attempts;
- find misconfigured channel audiences (noise of denials);
- detect users probing delete/write without capability.

User bans
=========

:menuselection:`AI --> Monitoring --> User Bans`

Temporarily suspends AI use for a user. The gate checks bans **first**, before
expensive LLM or triage work — this breaks adaptive attack iteration.

- Duration comes from Settings (:guilabel:`Ban minutes`) when auto-issued.
- Admins may manage bans manually.
- AI Administrators / Settings are treated as ban-exempt in design (they
  administer the rails themselves) — another reason agent users must never be
  AI admins.

Agent tasks and runs
====================

For autonomous work, also monitor:

- :menuselection:`AI --> Agents --> Tasks`
- :menuselection:`AI --> Agents --> Runs`

Inspect failed steps, tool errors and pending write linkage. Step journals can
be purged after :guilabel:`Run step retention` days; keep enough history to
investigate incidents.

Write proposals queue
=====================

:menuselection:`AI --> Write Proposals` is both a user tool and a control
surface: a backlog of pending agent proposals means supervisors need capacity,
or the agent is too aggressive.

Operational rhythms
===================

**Daily (early production)**

- Open violations and bans.
- Count pending agent proposals older than one business day.

**Weekly**

- Sample full conversations for quality and data-handling mistakes.
- Review new access rules and capability changes (change control).

**After any incident**

- Switch log level only as long as needed.
- Export relevant logs; then return to metadata-only.
- Rotate provider API keys if leakage is suspected.
- Re-read :doc:`security` checklist with the owning team.

Related configuration
=====================

Rate limits, strike thresholds and retention: :doc:`configuration`.  
Policy and capabilities: :doc:`access_policy`, :doc:`capabilities_and_tools`.

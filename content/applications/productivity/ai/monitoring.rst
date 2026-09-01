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

.. important::
   Not every refusal appears here. The field-level structural rails — a field that
   also writes into another model, a non-writable or non-stored field — record no
   violation and cost no strike, so an empty :guilabel:`Violations` list is not
   evidence that nothing was refused. A disabled **capability** is a different
   case: that one *is* a strikeable boundary and does appear here. See principle 9
   on :doc:`../ai` for which boundaries strike, and :ref:`ai/policy/cross-model`
   for the field rails.

   Look for the evidence of such a refusal in three other places:

   - the acting user's conversation, where the assistant reports the refusal and
     names the model and the fields it was not allowed to write;
   - the :guilabel:`Steps` tab of the run, for an agent: the tool call is
     recorded with :guilabel:`Gate Verdict` *denied* and the refusal message;
   - the Odoo server log, for a refusal inside a one2many or many2many payload:
     the nested model and field are recorded there and nowhere in the interface,
     so ask whoever operates your server to look them up — they name the
     field-level rule that would open it.

   :menuselection:`AI --> Monitoring --> Logs` will not show it: ``ai.log``
   records provider calls and writes that were actually applied.

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

Failure types
-------------

There is no *Cancelled* state and no *Reaped* state. Every run below is simply
**Failed** in the list, and :guilabel:`Failure Type` on the run form is what
tells them apart. It is not a column and no filter ships for it, so add a custom
filter or a custom group-by on :guilabel:`Failure Type` in
:menuselection:`AI --> Agents --> Runs` before trying to watch a population. Each
of the three below also leaves a note on the task's chatter.

- ``reaped_stuck`` — no worker ever finalised the run (restart, out-of-memory
  kill, pod eviction) and the reaper closed it. A recurring population points at
  server restarts, or at a task that exceeds its time limit. A reaped run
  deliberately does **not** count towards the task's automatic deactivation,
  because the reaper runs outside the dispatcher — nothing will archive a task
  whose worker keeps dying, so this population is the only signal there is, and
  it needs acting on.
- ``cancelled`` — a run that was actually executing when it was stopped on
  request via :guilabel:`Request Cancellation`. The
  steps the run did execute stay on its :guilabel:`Steps` tab, but its answer
  records the cancellation rather than a partial reply, and any write proposals
  it had already opened are cancelled with it, so nothing is left approvable. A
  cancellation is neutral for the task's failure streak: neither counted nor
  reset.
- ``triage_denied`` — the pre-run instruction check refused the task's standing
  instruction, so the agent never started. Unlike the other two this one **does**
  count towards automatic deactivation: five consecutive failures, the first of
  them more than a week old, archive the task. A burst normally means either a
  badly worded standing instruction or a triage provider outage, which fails
  closed.

Two further values belong to runs that were parked for approval:
``waiting_approval_expired`` (nobody answered in time) and
``waiting_approval_empty`` (the run was freed because no proposal was left to
wait for, and none of them had been applied — this is also what you see when a
supervisor cancels a run that was parked for approval rather than executing). An
ordinary crash inside a run records the exception's class name instead.

See :ref:`ai/agents/reaper` and :ref:`ai/agents/cancel` for the mechanisms
behind these, and :doc:`configuration` for the parameters and scheduled actions
that drive them.

Write proposals queue
=====================

:menuselection:`AI --> Write Proposals` is both a user tool and a control
surface: a backlog of pending agent proposals means supervisors need capacity,
or the agent is too aggressive.

.. important::
   The :guilabel:`Agent write-proposal lifetime` only applies while the proposing
   run is still open. Once that run has ended — most often a run that overran its
   time limit and closed as :guilabel:`Timed out` — its pending proposals are
   expired by the next pass of the **AI: Expire pending writes** scheduled action,
   every 15 minutes, because nobody is left to carry the result back. That sweep
   runs whatever the lifetime is set to, ``0`` included.

   So review the proposals of failed and timed-out runs promptly; do not plan to
   come back to them tomorrow.

Operational rhythms
===================

**Daily (early production)**

- Open violations and bans.
- Count pending agent proposals whose run is still open, and clear them the same
  day; once a run has ended, its proposals are swept rather than waiting.

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

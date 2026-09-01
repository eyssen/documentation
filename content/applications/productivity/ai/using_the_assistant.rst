=====================
Using the assistant
=====================

Interactive chat
================

Backend users in **AI: User** can open the assistant from the **systray bubble**
(persistent chat UI) or from :menuselection:`AI --> Conversations`.

Typical turn flow:

1. You send a message (optionally with attachments).
2. The orchestrator assembles layered system prompts (core safety, global
   behaviour, agent prompt, skills, environment facts, optional record
   snapshot, history).
3. The model may call tools (search, read, skills, memory, …).
4. Each tool call is authorized by the **access gate** (ban → capability → AI
   policy → Odoo ACL → sanitise → audit).
5. The assistant replies in the conversation language when possible.

Chatting from a business form may attach a **record snapshot** (L4) so the model
sees the current record context. Snapshots are data-fenced; treat them as
sensitive if the form is sensitive.

Conversations
=============

:menuselection:`AI --> Conversations` lists chat threads for the current user
(administrators may see more depending on record rules).

Use conversations to:

- continue multi-turn work with full history;
- review what was asked and answered;
- relate write proposals and logs back to a thread.

.. note::
   Agent channels (Discuss, chatter, assignment) also use conversation-style
   ledgers so every channel has an auditable communication history.

Attachments and files
=====================

Users can attach images and documents to a chat turn (subject to configured
MIME types and max size under AI Settings → Web Access / file limits).

- Images may be re-encoded before they reach the model.
- HTML/SVG and other renderable active content is refused for document download
  tools.
- Fetching a file from a URL into a binary field requires **both** Web and Write
  capabilities (``fetch_file_to_field``).

Write proposals
===============

When a tool wants to create, update, delete, attach a file, or run certain
actions and confirmation is required, the gate creates an
``ai.pending.write`` row instead of applying immediately.

Open :menuselection:`AI --> Write Proposals` to:

- read the human-readable :guilabel:`Summary`;
- inspect model, operation, target id and values;
- **Apply** or **Cancel** while the proposal is still *Pending*;
- use :guilabel:`Open record` to jump to the existing target document (write /
  delete / action on a live id — not available for pure creates).

For **agent** proposals the supervisor also receives a **To-Do** on the target
business record when possible (e.g. the vendor bill), with a chatter note and a
fallback activity on the agent task for creates without an id yet. That
activity is a pointer into the proposal workflow; applying or cancelling the
proposal closes it. See :ref:`ai/agents/task-write-mode`.

An agent proposal can be refused at apply time even while it still reads
*Pending*. If the run that proposed it was stopped on request, or closed by the
stuck-run reaper because its worker died, :guilabel:`Apply` answers *The agent
run that proposed this write was stopped before it finished, so this proposal
can no longer be approved.* A run that somebody else declared over may no longer
authorise a change, so the work has to be re-requested rather than approved —
see :ref:`ai/agents/cancel`. Usually such a proposal has already been cancelled
or expired with its run; where the row survives, this is what you meet.
Proposals from a run that ended on its own stay approvable
until they expire, and :guilabel:`Cancel` is never refused for this reason.

.. note::
   Even with Write enabled, the gate refuses fields that also write into a
   different model — a lead's email address, or a product on an invoice line.
   The refusal names the model and the field it would not write; for a line
   inside :guilabel:`Invoice lines` it names that parent field rather than the
   line's own. It does not say why, so ask an administrator to check
   :ref:`ai/policy/cross-model`. Such a refusal is a configuration boundary: it
   records no violation and costs you no strike.

Chat vs agent proposals
-----------------------

+---------------------+----------------------------------+----------------------------------+
|                     | Interactive chat                 | Autonomous agent run             |
+=====================+==================================+==================================+
| Controlled by       | Global :guilabel:`Ai Write Mode` | The **task's**                   |
|                     | in Settings                      | :guilabel:`Write Mode`           |
|                     |                                  | (default *confirm*; see          |
|                     |                                  | :ref:`ai/agents/task-write-mode`)|
+---------------------+----------------------------------+----------------------------------+
| Approver            | Usually the chatting user        | Agent **supervisor** (when the   |
|                     |                                  | task mode still proposes)        |
+---------------------+----------------------------------+----------------------------------+
| Default TTL         | 60 minutes (configurable)        | 1440 minutes (configurable),     |
|                     |                                  | only while its run is open       |
+---------------------+----------------------------------+----------------------------------+
| Acting identity on  | The chat user                    | The **agent user** (from the     |
| apply               |                                  | run), not the supervisor         |
+---------------------+----------------------------------+----------------------------------+
| Systray nudge       | Chat card / own proposals list   | To-Do on the **business record** |
|                     |                                  | when possible, else on the task  |
+---------------------+----------------------------------+----------------------------------+

.. note::
   The agent lifetime applies only while the proposing run is still open. Once
   that run has ended — :guilabel:`Done`, :guilabel:`Failed` or
   :guilabel:`Timed out` — the **AI: Expire pending writes** scheduled action
   expires its remaining proposals on its next pass, at most 15 minutes later,
   whatever the lifetime says. The case that catches supervisors out is a run
   that overran its own time limit: it closes as :guilabel:`Timed out` while
   still holding open proposals. Review proposals from failed and timed-out runs
   promptly. If you open a :guilabel:`To-Do` for a proposal that no longer
   exists, mark the activity done: the proposal expired with its run.

.. important::
   Approving an agent proposal means: "I authorise this agent to perform this
   change with *its* rights." The supervisor does not need (and should not use)
   broader rights than necessary to review the summary — execution rights come
   from the agent user + policy at apply time.

Write modes
-----------

**Interactive chat** — under :menuselection:`AI --> Configuration --> Settings`:

- **Apply automatically** — every create/write/delete/file tool runs immediately.
  Highest risk.
- **Always require confirmation** — everything becomes a proposal.
- **Create automatically, confirm updates** (*hybrid*, default) — only *new*
  records auto-apply; updates, deletes and file attaches wait for confirmation.

**Agent runs** — same three values, but on the **task** form
(:guilabel:`Write Mode`), defaulting to *Always require confirmation*. The
Settings value does not apply to agent runs. Use *auto* or *hybrid* only when
the standing instruction and skills keep risk bounded (draft-only fills, no
posting, no payments). Details: :ref:`ai/agents/task-write-mode`.

A TTL of 0 disables expiry **by age** for that class of proposals. It does not
disable the sweep described above: a proposal whose agent run has already ended
is expired however long you are prepared to wait for an approval.

Navigating the UI
=================

With the **Navigate** capability, the assistant can help open menus / actions
the user is allowed to reach. It does not bypass menu ACLs.

Presenting choices
==================

The assistant may use a structured **present choices** tool so the UI can show
selectable options instead of free text only (when supported by the chat
frontend).

What the assistant should not do
================================

- Claim a model, field, stage or module exists without tool or environment
  evidence on *this* database.
- Write ``state`` directly to skip business buttons.
- Promise that an email was sent to a customer unless a real mail tool/action
  did so under policy (shipped support prompts forbid fake send claims).
- Treat ticket text as a privilege upgrade.

For agent-driven work (assignment, @mention), see :doc:`agents`.

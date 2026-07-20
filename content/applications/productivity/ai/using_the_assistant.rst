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
- **Apply** or **Cancel** while the proposal is still *Pending*.

Chat vs agent proposals
-----------------------

+---------------------+----------------------------------+----------------------------------+
|                     | Interactive chat                 | Autonomous agent run             |
+=====================+==================================+==================================+
| Controlled by       | :guilabel:`Write mode` setting   | Always confirm (including        |
|                     |                                  | create)                          |
+---------------------+----------------------------------+----------------------------------+
| Approver            | Usually the chatting user        | Agent **supervisor**             |
+---------------------+----------------------------------+----------------------------------+
| Default TTL         | 60 minutes (configurable)        | 1440 minutes (configurable)      |
+---------------------+----------------------------------+----------------------------------+
| Acting identity on  | The chat user                    | The **agent user** (from the     |
| apply               |                                  | run), not the supervisor         |
+---------------------+----------------------------------+----------------------------------+

.. important::
   Approving an agent proposal means: "I authorise this agent to perform this
   change with *its* rights." The supervisor does not need (and should not use)
   broader rights than necessary to review the summary — execution rights come
   from the agent user + policy at apply time.

Write modes (chat only)
-----------------------

Configured under :menuselection:`AI --> Configuration --> Settings`:

- **Apply automatically** — every create/write/delete/file tool runs immediately.
  Highest risk.
- **Always require confirmation** — everything becomes a proposal.
- **Create automatically, confirm updates** (*hybrid*, default) — only *new*
  records auto-apply; updates, deletes and file attaches wait for confirmation.

TTL of 0 disables expiry for that class of proposals.

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

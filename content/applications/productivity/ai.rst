===
AI
===

The **AI** application is eYssen's security-first LLM assistant for Odoo. It
connects your database to language-model providers (OpenAI, Anthropic, xAI,
Google Gemini, OpenRouter and compatible APIs), lets users chat with a grounded
assistant about *this* Odoo instance, and can run **autonomous agents** that act
as narrow-privilege colleagues on Discuss, chatter, activities and project
tasks.

Every data operation the model requests goes through a single access gate: the
assistant never receives more privilege than the user (or the agent user) already
holds in Odoo, and an admin can narrow that further with AI access policies,
capabilities, channel rules and write confirmation.

.. danger::
   **Misconfigured AI is dangerous.** An AI agent with broad Odoo groups, open
   write capabilities, or ``agent_full`` channel scope can read, change or delete
   business data, send content to an external LLM provider, and act unattended.
   Read :doc:`ai/security` **before** enabling write capabilities, linking agent
   users, or exposing AI to untrusted requesters. Default install is read-oriented
   and write-denied; every privilege you add is a deliberate decision.

.. note::
   The technical module name is ``ai`` (Productivity / AI). It depends on
   **Mail**, **Web**, **Project**, and eYssen's project template/category helpers
   used for the AI Ops work queue.

What you can do
===============

- **Interactive assistant** — systray chat bubble and :menuselection:`AI -->
  Conversations` for grounded Q&A, schema search, optional web fetch, file
  ingest, skills and memory.
- **Human-confirmed writes** — create/update/delete proposals in :menuselection:`AI
  --> Write Proposals` instead of silent mutations (configurable).
- **Autonomous agents** — optional linked ``res.users`` identities with a
  supervisor, channel allow-lists, capability ceilings, per-task write mode
  (confirm by default; hybrid/auto only as an explicit opt-in), pending-write
  approval with a systray nudge on the **business record**, and
  supervisor-requested cancellation (see :doc:`ai/agents`).
- **Access policy framework** — per-group / per-model / per-field allow·deny on
  top of Odoo ACLs (never grants beyond the acting user's own rights).
- **Skills** — reusable instruction packs (factory + custom) activated always or
  on demand.
- **Memory** — durable user/agent/company memories with graph and search tools.
- **Monitoring** — audit logs, violation strikes, temporary bans, and an agent
  run ledger in which a run whose worker died is closed automatically.
- **Optional MCP / web / UI customization** — external tools, web search, and
  admin-only schema/view customization, all capability-gated and off by default
  where risky.

Who this documentation is for
=============================

+---------------------------+---------------------------------------------------+
| Role                      | Typical tasks                                     |
+===========================+===================================================+
| System / AI administrator | Providers, settings, policies, agents, monitoring |
+---------------------------+---------------------------------------------------+
| Supervisor of an agent    | Approve write proposals, review tasks and runs    |
+---------------------------+---------------------------------------------------+
| Everyday AI user          | Chat, confirm own write proposals, use memory     |
+---------------------------+---------------------------------------------------+
| Security / compliance     | Threat model, least privilege, audit trail        |
+---------------------------+---------------------------------------------------+

Document map
============

.. toctree::
   :titlesonly:

   ai/security
   ai/getting_started
   ai/using_the_assistant
   ai/configuration
   ai/capabilities_and_tools
   ai/access_policy
   ai/agents
   ai/agent_recipes
   ai/skills_and_memory
   ai/monitoring

Key design principles
=====================

1. **Run as the user (or as the agent user)** — no ``sudo`` on business data.
   Odoo ACLs and record rules always apply.
2. **AI policy narrows, with one named exception** — ``ai.access.rule`` can never
   grant a right the underlying user does not already hold in Odoo. Within that
   ceiling, a rule naming a specific **field** is the one place a rule *opens*
   something the gate otherwise refuses: a field that also writes into another
   model. A model-level Allow deliberately never lifts that — see
   :ref:`ai/policy/cross-model`.
3. **Capabilities are master switches** — e.g. Write / Delete / Web / MCP /
   Customize ship disabled until an admin turns them on.
4. **Default-deny channels for agents** — an agent without a matching channel
   rule refuses inbound address (Discuss DM, @mention, activity, assignment).
5. **Supervisor four-eyes by default on agent writes** — each agent **task**
   has its own :guilabel:`Write Mode` (default **Always require confirmation**).
   Unattended runs therefore propose for the supervisor unless that task
   explicitly opts into *hybrid* or *auto* for trusted, low-risk work (for
   example filling **draft** vendor bills that the playbook never posts). The
   global chat write mode does **not** control agent runs — see
   :ref:`ai/agents/task-write-mode`.
6. **Customer / email text is work material, not authority** — instructions in
   a ticket body cannot raise the agent's privileges; triage and capability
   ceilings subtract only.
7. **Grounding** — the assistant must not invent models, fields or stages; it
   uses tools and live environment facts for *this* database.
8. **Runs are accounted for** — cancellation is cooperative and recorded, never a
   silent kill: the run stops at its next step boundary and closes as failed with
   a cancellation reason. A run whose worker died is closed by a scheduled
   housekeeping job, which rebuilds its ledger row from the dispatch record where
   one survives.
9. **A structural refusal is not abuse** — the gate refuses plenty the model
   merely guessed at (a non-writable field, a field that also writes another
   model) without recording a violation or spending a strike, so an empty
   Violations list is not proof that nothing was refused. Strikes are for real
   boundaries: a secret or privileged field, an explicit policy Deny, a disabled
   capability.

See also
========

- :doc:`../general/users/access_rights` — Odoo groups and record rules (the floor
  under every AI action)
- :doc:`../general/developer_mode` — needed for the Technical menus where the AI
  system parameters and scheduled actions live
- :doc:`discuss` — Discuss DMs used by agent channels
- :doc:`../services/project` — project tasks and assignment channel (if Project
  docs are available in your build)

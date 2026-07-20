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
  supervisor, channel allow-lists, capability ceilings and pending-write
  approval.
- **Access policy framework** — per-group / per-model / per-field allow·deny on
  top of Odoo ACLs (policy can only *narrow*, never grant beyond the user).
- **Skills** — reusable instruction packs (factory + custom) activated always or
  on demand.
- **Memory** — durable user/agent/company memories with graph and search tools.
- **Monitoring** — audit logs, violation strikes, temporary bans.
- **Optional MCP / web / UI customization** — external tools, web search, and
  admin-only schema/view customization, all capability-gated and off by default
  where risky.

Who this documentation is for
=============================

| Role | Typical tasks |
| --- | --- |
| System / AI administrator | Providers, settings, policies, agents, monitoring |
| Supervisor of an agent | Approve write proposals, review tasks and runs |
| Everyday AI user | Chat, confirm own write proposals, use memory |
| Security / compliance | Threat model, least privilege, audit trail |

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
2. **AI policy only narrows** — ``ai.access.rule`` cannot grant rights the
   underlying user does not have.
3. **Capabilities are master switches** — e.g. Write / Delete / Web / MCP /
   Customize ship disabled until an admin turns them on.
4. **Default-deny channels for agents** — an agent without a matching channel
   rule refuses inbound address (Discuss DM, @mention, activity, assignment).
5. **Supervisor four-eyes on agent writes** — agent runs always propose writes
   for the supervisor; they never auto-apply unattended creates either.
6. **Customer / email text is work material, not authority** — instructions in
   a ticket body cannot raise the agent's privileges; triage and capability
   ceilings subtract only.
7. **Grounding** — the assistant must not invent models, fields or stages; it
   uses tools and live environment facts for *this* database.

See also
========

- :doc:`../general/users/access_rights` — Odoo groups and record rules (the floor
  under every AI action)
- :doc:`discuss` — Discuss DMs used by agent channels
- :doc:`../services/project` — project tasks and assignment channel (if Project
  docs are available in your build)

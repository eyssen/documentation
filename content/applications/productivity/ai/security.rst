========
Security
========

.. danger::
   **This module can be dangerous if it is not configured carefully.**

   An LLM connected to Odoo can, depending on what you enable:

   - **Exfiltrate data** to an external model provider (prompts, tool results,
     attachments and conversation history leave your server).
   - **Read any business data** the acting user (or agent user) can already read
     under Odoo ACLs — and, by default, the AI access policy allows *read*
     unless you tighten it.
   - **Create, change or delete records** once Write / Delete capabilities and
     access-policy rules allow it — including through unattended agent runs if
     a supervisor later approves a proposal, or instantly in chat write mode
     *Apply automatically*.
   - **Call business actions** (lifecycle methods) if the Action capability and
     allow-list permit them.
   - **Reach the public web or MCP tools**, which can import untrusted content
     into the model context (prompt injection) or send data outbound.
   - **Modify UI and schema** if Customize is enabled for an administrator.

   Treat every AI privilege like production root access for that scope: start
   narrow, measure, then open only what a concrete use case needs.

Threat model (what can go wrong)
================================

Data leaving the company
------------------------

Every chat turn and tool result that is sent to the provider is processed under
that provider's terms and jurisdiction. Sensitive personal data, salaries,
passwords (if ever present in free text), contract terms and customer secrets
can appear in:

- the user message and conversation history;
- L4 record snapshots when chatting from a form;
- tool outputs (``search`` / ``read`` / ``read_group`` results);
- uploaded files and fetched web pages;
- agent run steps and full-payload logs (if logging is set to full payload).

**Mitigations:** choose a provider and region you accept contractually; keep
:guilabel:`Log level` on *Metadata only* in production unless investigating an
incident; deny sensitive models/fields in AI access rules; do not enable Web or
MCP for agents that handle confidential tickets; train users not to paste
secrets into chat.

Over-privileged interactive chat
--------------------------------

If a highly privileged employee uses the assistant with Write / Delete / Action
enabled and write mode *Apply automatically*, a single mistaken model turn (or a
prompt-injection in a pasted email) can mutate production data immediately.

**Mitigations:** keep write mode on *hybrid* or *confirm*; leave Delete off;
restrict Write to trusted groups via capability :guilabel:`Restricted to
groups`; field/model deny rules for payroll, banks, tax and system models.

Over-privileged autonomous agent
--------------------------------

An agent linked to a ``res.users`` runs with **that user's** Odoo groups. If
you copy "Internal User" defaults without stripping groups, the agent is a
full employee. Combined with ``agent_full`` channel scope and a wide audience,
any allow-listed requester can trigger work at the agent's full capability
classes.

**Mitigations:** create a dedicated user with only the groups needed; never link
Settings / AI Administrator; set a human supervisor; use ``intersect`` scope by
default; empty channel audiences mean *nobody*; keep Write capability off on
public-facing agents; always re-check proposals as supervisor.

Prompt injection and social engineering
---------------------------------------

Text from customers, email, chatter and uploaded PDFs is **work material**, not
a grant of rights. Attackers still try to:

- override system instructions ("ignore previous rules…");
- coerce the model into calling tools it should not;
- iterate after refusals (adaptive attacks).

**Mitigations (built-in):** blocked input patterns; capability ceilings enforced
at the gate; AI policy + Odoo ACLs; strikes → temporary ban on violations so
attackers cannot freely iterate; triage layer that may only *subtract*
authority. None of these make injection "solved" — they reduce impact. Design
agents so the worst successful injection still cannot read or write more than
the agent was meant to.

Lifecycle / state bypass
------------------------

Writing the ``state`` field raw can skip buttons like Confirm / Post. The gate
**rejects direct writes to lifecycle ``state``**. Use allow-listed business
actions (``call_action``) instead when Action capability is enabled.

Hard-deny floor (self-protection)
---------------------------------

A fixed set of technical models (AI config tables, security-sensitive system
models, sequences, menus, settings, reports, and similar) is always denied to
AI tools regardless of access rules. Admins cannot "open" these via
``ai.access.rule``. This is a floor, not a complete data classification
policy — business models like ``hr.employee``, ``account.move`` or
``mail.message`` are **not** all hard-denied by default; you must configure
them if needed.

Sensitive field stripping
-------------------------

Fields whose names look like secrets (password, token, api_key, …), magic
fields, and certain complex types are stripped or refused on write. This is
defense-in-depth, not a substitute for denying whole models (e.g. HR).

Confirmation and re-check
-------------------------

Pending writes are re-validated at **apply** time under the correct acting
identity and current policy. Approving an old proposal after rights were
revoked should fail closed. Agent proposals rebuild authority from the **run**,
not from the confirmer's privilege (the confirmer authorises; the agent
executes).

Security roles and groups
=========================

+----------------------------------+------------------------------------------+
| Group                            | Purpose                                  |
+==================================+==========================================+
| **AI: User**                     | Use chat, own conversations, own write   |
|                                  | proposals, memory; supervisors need this |
|                                  | to approve agent proposals.              |
+----------------------------------+------------------------------------------+
| **AI: Administrator**            | Configure agents, capabilities,          |
|                                  | policies, skills, MCP, monitoring.       |
|                                  | Implies AI: User.                        |
+----------------------------------+------------------------------------------+
| **Settings**                     | AI Settings app page, guided setup,      |
| (system administration)          | setup plans.                             |
+----------------------------------+------------------------------------------+

.. important::
   An **agent user** must never hold Settings or AI Administrator. The module
   blocks linking such users on the agent form (at write time). Do not grant
   those groups later on the user form either — that bypasses the agent
   constraint and removes the ban kill-switch for AI admins.

Layered controls (checklist)
============================

Use all layers; none replaces the others:

1. **Odoo groups on the user / agent user** — what they can do without AI.
2. **AI capabilities** — which tool classes exist (ask, read, write, delete,
   web, mcp, action, customize, setup, navigate).
3. **AI access groups + rules** — model/field allow·deny for AI tools.
4. **Agent ``capability_ids``** — further ceiling for that agent only.
5. **Channel rules + audience + scope_mode** — who may trigger the agent and
   whether capability classes are intersected with the requester.
6. **Write mode / pending writes / supervisor** — human in the loop.
7. **Rate limits, strikes, bans, blocked patterns** — abuse and iteration.
8. **Logging and retention** — evidence and least retention for step journals.

Recommended production baseline
===============================

- Leave **Write**, **Delete**, **Web**, **MCP**, **Customize**, **Action**
  disabled until a named use case needs each one.
- Keep access-policy defaults: read allow (or deny if you prefer deny-by-default
  and open only needed models), create/write/delete **deny**.
- Prefer write mode **hybrid** or **confirm** for chat; never *auto* on shared
  production databases without a change-management process.
- One **supervisor** human per agent; supervisors in AI: User.
- No shared "god" agent for all departments — split by domain and data.
- Review :menuselection:`AI --> Monitoring --> Violations` weekly at first.
- Document every agent in your internal runbook (purpose, user groups, rules,
  data classes allowed).

What security does *not* guarantee
==================================

- Perfect resistance to prompt injection.
- Classification of every sensitive business field out of the box.
- That training-data guesses cannot appear in free-text answers (grounding
  rules reduce but do not eliminate hallucinations — critical actions must go
  through tools and confirmation).
- GDPR/legal compliance by itself — you still need lawful basis, DPAs with
  providers, and retention policy for conversations you keep.

Continue with :doc:`getting_started` only after this page is understood by the
people who will administer the module.

=================
Skills and memory
=================

Skills
======

A **skill** (``ai.skill``) is a reusable instruction pack the assistant can
load mid-task — similar to progressive disclosure in modern coding agents.

Menu: :menuselection:`AI --> Configuration --> Behavior --> Skills`

Fields
------

+-----------------------------+------------------------------------------------+
| Field                       | Purpose                                        |
+=============================+================================================+
| :guilabel:`Name`            | Short UI / catalogue label                     |
+-----------------------------+------------------------------------------------+
| :guilabel:`Code`            | Technical id for ``use_skill``                 |
|                             | (``^[a-z][a-z0-9_]*$``)                        |
+-----------------------------+------------------------------------------------+
| :guilabel:`Description`     | When to use (English; shown to the model)      |
+-----------------------------+------------------------------------------------+
| :guilabel:`Body`            | Full instructions when active (English)        |
+-----------------------------+------------------------------------------------+
| :guilabel:`Activation mode` | **On demand** (catalogue + ``use_skill`` /     |
|                             | keywords) or **Always** (every turn — use      |
|                             | sparingly)                                     |
+-----------------------------+------------------------------------------------+
| :guilabel:`Trigger          | Comma-separated keywords on the latest user    |
| keywords`                   | message for auto load                          |
+-----------------------------+------------------------------------------------+
| :guilabel:`Active` /        | Visibility and ordering                        |
| sequence                    |                                                |
+-----------------------------+------------------------------------------------+
| Provenance                  | Factory / custom (and factory-modified)        |
+-----------------------------+------------------------------------------------+

Runtime behaviour
-----------------

- CRUD is **AI Administrator** only.
- At runtime every AI user sees the same active skills (no per-user skill
  toggle).
- Tools ``list_skills`` / ``use_skill`` require capability **ask**.
- Bounds limit catalogue size, always-on count and body length so one skill
  cannot dominate the prompt.

Factory skills
--------------

The module ships factory skills (XML data, ``noupdate``). Examples include
operational playbooks for vendor bills, bank reconciliation patterns, follow-ups
and localisation-aware product fields — grounded to eYssen stacks where
applicable.

- **Sync factory skills** admin action refreshes **pristine** factory rows from
  code on upgrade.
- If you edit a factory skill, it becomes factory-modified and is **not**
  auto-overwritten; you can reset to factory when desired.

.. _ai/skills/vendor-bill:

Vendor bill from documents (``vendor_bill_from_documents``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Full AP playbook for Odoo 18: chat PDFs or draft supplier invoices
(``in_invoice``) that have attachments but empty lines. It is **not** an AR /
customer-invoice skill.

What it is designed to do:

- Resolve partner flags, reuse product / account / tax / analytic patterns from
  prior bills for the same vendor.
- Fill invoice lines on **draft** moves only.
- Schedule a human **review** To-Do on every bill it actually changed.
- **Hungarian NAV twin path (before filling lines):** many HU suppliers already
  exist as NAV-imported bills. If exactly one clear match is found (often already
  posted), the skill **reattaches** the image/PDF from the empty draft to that
  existing bill, notes the merge, and **unlinks the empty draft** only when it
  still has no meaningful lines — it must **not** double-book the same invoice.
  Non-HU / foreign suppliers skip this path.

Hard stops in the playbook:

- Do **not** post, pay, or write NAV transmission fields.
- Do **not** invent partners, taxes or accounts when prior-bill reuse fails —
  leave for the human.
- Prefer reporting an existing bill over creating a second one with the same
  partner + reference.

Pair with Recipe D in :doc:`agent_recipes` (chat helper or scheduled agent). For
unattended runs, task :guilabel:`Write mode` *auto* is only appropriate because
this skill keeps bills draft; if you customise the skill to post, switch the
task back to *confirm*.

Writing a good skill
--------------------

- State triggers clearly in the description.
- Give ordered steps and which tools to call first.
- Say what **not** to invent (accounts, taxes, partners).
- Keep always-on skills short; put long playbooks on demand.

Memory
======

**Memory** (``ai.memory``) stores durable facts the assistant may recall across
conversations.

Menu: :menuselection:`AI --> Memory --> Memories` and :guilabel:`Memory Graph`.

Types
-----

- **Working** — short-lived task context  
- **Episodic** — what happened in a session  
- **Semantic** — durable facts / preferences  
- **Archive** — cold storage  

Scopes
------

- **User** (default private)
- **Company** / **System** — admin (or approved promotion)
- **Agent** / **Run** — agent-centric context

Users may create/write user, agent and run scopes; company/system need admin or
promotion approval.

Tools
-----

Under capability **ask**: ``memory_search``, ``memory_save``, ``memory_forget``,
``memory_link``. Prompt injection of memories is size-bounded.

Good practice
-------------

- Save stable preferences ("user wants HU date format") as semantic/user.
- Do not store passwords, API keys or full personal ID documents in memory.
- Review company-scope memories periodically; treat them as shared
  configuration.
- Use forget when a fact is wrong — do not pile contradictions.

Skills vs memory
================

+------------------+----------------------------------+
| Skills           | Memory                           |
+==================+==================================+
| How to do a job  | What is true for this user/org   |
| (playbooks)      | (facts, preferences)             |
+------------------+----------------------------------+
| Admin-authored   | User/agent/runtime authored      |
| configuration    |                                  |
+------------------+----------------------------------+
| Versioned factory| Operational data                 |
| possible         |                                  |
+------------------+----------------------------------+

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

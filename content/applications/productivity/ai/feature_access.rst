================
Who can use what
================

This page is an overview for administrators: which group, capability and rule
each AI feature depends on, and where to change it. The principle is always the
same: AI works with your rights and can only be narrowed, never widened.

The three layers
================

1. Groups. :guilabel:`AI: User` lets a person use the assistant and the
   one-click features. :guilabel:`AI: Administrator` lets a person configure
   providers, policies, agents and sources. Both are set on the user form under
   the AI category.
2. Capabilities. Master switches under :menuselection:`AI --> Configuration -->
   Behavior --> Capabilities` decide which classes of tools exist at all:
   :guilabel:`Ask (Q&A)`, :guilabel:`Read data`, :guilabel:`Navigate UI`,
   :guilabel:`Write data`, :guilabel:`Delete data`, :guilabel:`Web access`,
   :guilabel:`MCP tools`, :guilabel:`Business actions`, :guilabel:`Customize UI
   & schema` and :guilabel:`Guided system setup`. Write, delete, web, MCP,
   actions and customization are off after installation. A capability can be
   limited to groups.
3. Access rules. Under :menuselection:`AI --> Configuration --> Security -->
   Access Rules`, per-model and per-field allow and deny rules sit on top of
   Odoo's own rights. By default reading is allowed and creating, writing and
   deleting are denied. See :doc:`access_policy`.

What each feature needs
=======================

- AI panel, writing assistant, AI search, command palette, dictation:
  :guilabel:`AI: User`, a chat model, the :guilabel:`Ask (Q&A)` capability. The
  assistant sees record data only if :guilabel:`Read data` and the access rules
  allow reading that model for you.
- Changes made by the assistant in chat: :guilabel:`Write data` or
  :guilabel:`Delete data`, plus an allow rule for the model and fields, plus the
  write mode. Keep confirmation on.
- One-click buttons in apps (assign a lead, describe a product, draft
  timesheets, file a document): the click is your decision, so they do not need
  the write capability, but they read data through the same access rules. If the
  AI is not allowed to read the model, you get a clear message instead of a
  result.
- AI fields and AI server actions: the user chosen in :guilabel:`Acts as` (or
  the agent task's agent user). See :doc:`fields_and_automation`.
- Knowledge sources: sources are managed by AI administrators; each person only
  gets excerpts from sources and records they may read themselves
  (:doc:`knowledge_sources`).
- MCP server: internal users in :guilabel:`AI: User`; only an allow-list of
  tools; changes always wait for your confirmation (:doc:`mcp_server`).
- Live chat agent: a dedicated service user that can only ask, read the data
  sources you list and hand over; it gets no write rights beyond creating a
  lead, if you turn that on (:doc:`livechat`).
- Website builder tools: :guilabel:`Customize UI & schema` and the website
  designer group; every change is a confirmation card (:doc:`website`).
- AI triage of project tasks: reviewer in :guilabel:`AI: User`, the
  :guilabel:`Write data` capability and an allow rule for writing the task
  fields it changes (:doc:`project_sla`).

Limits and traces
=================

- Rate and cost limits per person and per day are under :menuselection:`AI -->
  Configuration --> Settings` (see :doc:`configuration`). Repeated policy
  violations earn strikes and a temporary ban.
- Every model call is written to the AI log and every applied change to the
  change log, both under :menuselection:`AI --> Monitoring --> Logs` and
  :menuselection:`AI --> Monitoring --> Mutation Logs` (see :doc:`monitoring`).

.. tip::
   Roll out in steps: start with the assistant and the writing features for a
   pilot group, add knowledge sources, then enable one write path at a time and
   read the logs for a couple of weeks before widening it.

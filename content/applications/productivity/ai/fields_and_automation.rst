=========================================
AI fields, server actions and automations
=========================================

AI can fill in data for you without anybody opening the assistant: a field that
is written by the model, a server action that asks the model for a value, or a
server action that hands a record to an agent. This page is for administrators.

AI fields
=========

An AI field is an existing, stored and editable field of any model that the
model fills from an instruction. Typical examples: a one-sentence summary of a
request, the category that fits a product best, a priority class. Supported
field types are text, rich text, integer, decimal, monetary, checkbox,
selection, date, date and time, many2one and many2many.

Create one under :menuselection:`AI --> Configuration --> Behavior --> AI
Fields`:

- Choose the model and the field. A field can have only one AI rule.
- Write the instruction, for example "A one-sentence summary of what the
  customer asks for."
- :guilabel:`Acts as` is the user whose access rights are used to read the
  record and to write the value. Choose a user who may read and change that
  model, never a more powerful one than needed.
- Restrict the records with the domain, and use :guilabel:`Also show these
  fields` to give the model related fields to look at. For a relational field,
  the choice domain limits which records the model may pick.

When values are filled
======================

- :guilabel:`Auto Fill`: a scheduled action runs every 15 minutes and fills only
  empty values, newest records first, in batches (20 records by default, system
  parameter ``ai.fields.batch_size``).
- :guilabel:`Fill empty values now` on the rule runs it at once.
- Numbers and checkboxes have no "empty" state, so they are only filled from the
  :guilabel:`Fill AI fields` entry of the Actions menu, which appears
  automatically on the model while a rule exists, or from an automation. Tick
  :guilabel:`Overwrite` if that action should also replace values that are
  already set.

The model must answer with a value that is valid for the field: selection keys,
related records among the offered choices and dates are checked before anything
is written, and an answer of "nothing" leaves the field empty. The record is
shown to the model without the fields the assistant may never read. Every write
is made as the :guilabel:`Acts as` user, so Odoo access rights and record rules
apply, and it appears in the AI change log under :menuselection:`AI -->
Monitoring --> Mutation Logs`. Problems are kept in the rule (:guilabel:`Last
run` and the last error).

AI in server actions
====================

Two kinds of server action use AI. They need :doc:`developer mode
<../../general/developer_mode>` to edit under :menuselection:`Settings -->
Technical --> Server Actions`, and they can also be used as actions of an
automation rule.

- :guilabel:`Ask AI`: on an "Update Record" action, set the value type to
  :guilabel:`Ask AI` and describe in :guilabel:`AI instruction` what the model
  should put in the field ("Describe what the AI should put in the field...").
  For each record the field is set from the model's answer, using the same
  engine and the same checks as AI fields. It works on saved records only.
- :guilabel:`Hand to an AI agent`: choose an :guilabel:`Agent task` and the
  records are queued as work items of that standing task. A background job then
  runs one isolated agent run per record with the task's agent, capabilities,
  instruction and write mode. Only agents with their own user and a supervisor
  can be used, because unattended work must never run in the name of whoever
  triggered it. See :doc:`agents` and the work-item sections there.

Automations
===========

Combine a trigger with one of those actions in :menuselection:`Settings -->
Technical --> Automation --> Automation Rules`: for example "when a task is
created, hand it to the triage agent" or "when a lead is created, fill its
category with AI". Time-based work ("every Monday, summarise last week's
tickets") is better modelled as a standing agent task with a schedule under
:menuselection:`AI --> Agents --> Tasks`.

Administrators with the :guilabel:`Customize UI & schema` capability can also
ask the assistant in chat to list, create, change or run automations. Creating
or changing one is always a proposal that needs confirmation.

.. warning::
   Unattended AI acts without anyone clicking. Keep the model and field lists
   narrow, choose a low-privilege :guilabel:`Acts as` user, keep agent tasks on
   confirmation write mode unless the work is low risk, and review the AI change
   log regularly.

======================
Capabilities and tools
======================

**Capabilities** are master switches that decide which *classes* of tools the
model may be offered and which the access gate will execute. They are
configured under :menuselection:`AI --> Configuration --> Behavior -->
Capabilities`.

Capability record fields
========================

- :guilabel:`Code` — stable technical code (``ask``, ``read``, ``write``, …).
- :guilabel:`Name` — UI label.
- :guilabel:`Is enabled` — global off switch.
- :guilabel:`Restricted to groups` — empty = all AI users (who pass other
  checks); otherwise only those Odoo groups.
- Optional company scoping.

.. important::
   Disabling a capability hides its tools **and** makes the gate reject them if
   the model invents a call. Offering a tool without the capability is not
   possible through the normal menu; the gate remains authoritative.

Shipped capabilities
====================

+-----------------+---------------------------+------------------------------------+
| Code            | Default enabled           | Role                               |
+=================+===========================+====================================+
| ``ask``         | Yes                       | Q&A helpers: schema search,        |
|                 |                           | environment, skills, memory, list  |
|                 |                           | actions, present choices           |
+-----------------+---------------------------+------------------------------------+
| ``read``        | Yes                       | ``search``, ``read``,              |
|                 |                           | ``read_group``, ``get_fields``     |
+-----------------+---------------------------+------------------------------------+
| ``navigate``    | Yes                       | Open UI the user may access        |
+-----------------+---------------------------+------------------------------------+
| ``write``       | **No**                    | ``create_record``,                 |
|                 |                           | ``update_record``, file attach     |
|                 |                           | (with web)                         |
+-----------------+---------------------------+------------------------------------+
| ``delete``      | **No**                    | ``delete_record``                  |
+-----------------+---------------------------+------------------------------------+
| ``web``         | **No**                    | ``web_search``, ``web_fetch``      |
+-----------------+---------------------------+------------------------------------+
| ``mcp``         | **No**                    | Dynamic tools from MCP servers     |
+-----------------+---------------------------+------------------------------------+
| ``action``      | **No**                    | ``call_action`` on allow-listed    |
|                 |                           | methods                            |
+-----------------+---------------------------+------------------------------------+
| ``customize``   | **No**; AI Administrator  | View/field/model customization     |
|                 | group by default          | tools                              |
+-----------------+---------------------------+------------------------------------+
| ``setup``       | Yes, **Settings** group   | Guided module install tools        |
|                 | only                      |                                    |
+-----------------+---------------------------+------------------------------------+

Tool catalogue (built-in)
=========================

Ask
---

- ``search_docs`` — keyword search over models/fields the user may use.
- ``get_environment`` — live version, edition, company, user, optional modules.
- ``list_skills`` / ``use_skill`` — skill catalogue and body load.
- ``list_allowed_actions`` — which business actions are allow-listed.
- ``memory_search`` / ``memory_save`` / ``memory_forget`` / ``memory_link``.
- ``present_choices`` — structured options for the UI.

Read
----

- ``search`` — domain search + field read (capped limit).
- ``read`` — by explicit ids (fails if too many ids; does not silently trim).
- ``read_group`` — aggregates (measures validated; domains policy-checked).
- ``get_fields`` — schema (required flags; not raw callable domains).

Write / delete
--------------

- ``create_record`` / ``update_record`` / ``delete_record`` — always via gate;
  may become pending writes.
- ``fetch_file_to_field`` — requires **web** *and* **write**.

Web
---

- ``web_search`` / ``web_fetch`` — subject to domain allow-list and daily caps.

Action
------

- ``call_action`` — only methods present on :guilabel:`Allowed Actions`.

Navigate / customize / setup
----------------------------

- ``navigate`` — UI navigation helpers.
- Customize tools — inspect/apply view chain, custom fields/models, undo,
  import/export customizations (admin).
- Setup tools — preview/install modules through guided setup controls.

Agent capability ceiling
========================

On ``ai.agent``, :guilabel:`Capabilities` further **intersects** what that agent
may use. An agent with only ``ask`` + ``read`` cannot execute write tools even
if Write is globally enabled for humans.

For ad-hoc channel runs with scope **intersect**, the effective capability
classes are:

.. code-block:: text

   effective = agent.capability_ids ∩ requester.allowed_capabilities
               (and global enabled flags / group restrictions)

Scope **agent_full** uses the agent's capabilities without intersecting the
requester's capability classes. Data access still uses the **agent user's**
Odoo ACL + AI policy — not the requester's record rules. See :doc:`agents`.

Enabling write safely (pilot pattern)
=====================================

1. Keep global Write disabled.
2. Create an Odoo group e.g. *AI Writers*.
3. Enable Write capability with :guilabel:`Restricted to groups` = AI Writers.
4. Add model-level ``perm_create`` / ``perm_write`` **allow** rules only for the
   models in the pilot (:doc:`access_policy`).
5. Try the writes the pilot actually needs. Model-level rules are not enough on
   their own: many everyday fields also write into a second model, and the gate
   refuses those even under a model-level Allow. Each one needs a rule naming
   the **field**, with :guilabel:`perm_write` = Allow — see
   :ref:`ai/policy/cross-model`. Discovering them by trying is safe, because
   this refusal records no violation and costs no strike.
6. Keep write mode **confirm** or **hybrid**.
7. Monitor logs and violations for two weeks before widening.

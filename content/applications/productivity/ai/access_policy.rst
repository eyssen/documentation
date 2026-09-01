==============
Access policy
==============

The AI **access policy** decides what the access gate may do *in addition to*
normal Odoo ACLs. It can only **narrow** rights: if the user cannot read a
record in Odoo, AI cannot either — even if a rule says Allow.

Menus:

- :menuselection:`AI --> Configuration --> Security --> Access Groups`
- :menuselection:`AI --> Configuration --> Security --> Access Rules`

Concepts
========

AI access group
---------------

An ``ai.access.group`` is a set of people the rules apply to:

- :guilabel:`Members` — explicit users (including agent users).
- :guilabel:`Mapped Odoo groups` — everyone in those groups is also a member.
- :guilabel:`Rules` — the allow/deny matrix for this group.

Use groups such as *AI – Sales readers*, *AI – Support agent bot*, *AI – No HR*.

AI access rule
--------------

An ``ai.access.rule`` targets:

- optional :guilabel:`Access group` (empty = **global** rule for all AI users);
- :guilabel:`Model` (required);
- optional :guilabel:`Field` (empty = model-level rule);
- :guilabel:`perm_read` / :guilabel:`perm_write` / :guilabel:`perm_create` /
  :guilabel:`perm_delete` each as **Inherit**, **Allow** or **Deny**.

Create and delete are model-level only (ignored on field rules). Setting field
values on create still needs write allow on those fields where the policy
checks them.

Resolution order
================

For a given user, model, operation and optional field, ``ai_can`` resolves
roughly as:

1. **Hard-deny floor** — technical / self-protection models always deny,
   including every ``ai.*`` platform model and raw ``mail.message`` /
   ``mail.activity`` / ``discuss.channel`` (see :doc:`security`).
2. **Any explicit Deny**, field-level or model-level. A Deny at either tier is
   absolute and nothing below overrides it.
3. **Field-level Allow** (read/write only) — decides the field tier and outranks
   the global default for that field. This is the mechanism the shipped rules and
   the whole cross-model opt-in rely on: with write defaulting to Deny, a
   field-scoped Allow is what makes a field writable. It does not replace the
   model tier, though: a **direct** write to a model must still pass step 4 or 5
   for that model. Only a payload nested inside a parent one2many or many2many
   field skips the model check on the child model.
4. **Model-level Allow** — most specific Allow wins among groups.
5. **Global defaults** from Settings (default_read / create / write / delete).

Unknown models or operations fail closed. Results are cached and invalidated
when rules, groups or parameters change.

Universal sanitiser rails (before/alongside policy)
===================================================

Independently of allow rules, the gate refuses or strips the following — with one
exception, noted in the list:

- magic fields;
- sensitive-looking field names (password, token, api_key, …);
- fields that write into another model — the only rail an Allow rule can lift,
  and only per field; see :ref:`ai/policy/cross-model`;
- lifecycle ``state`` writes;
- non-writable / complex types that must not be LLM-driven;
- hard-deny models in relational paths / domains.

.. _ai/policy/cross-model:

Cross-model write protection
============================

Some Odoo fields do not only store a value: writing them also writes into a
**different** model. ``crm.lead.email_from``, for example, updates the linked
partner's email address. Left unguarded, an assistant allowed to "edit leads"
could change contact data outside the models you opened, and the audit log would
only name the lead.

Odoo has two kinds of such field, and only one of them can be opened.

A **related** field re-routes the write to the other model by definition. The
gate refuses it outright, on create and on write, and no access rule of any shape
opens it — allow the assistant to write the *target* model instead.

A field carrying an **inverse** runs arbitrary code that may touch anything:
``crm.lead.email_from`` is compute-plus-inverse, and its inverse writes
``res.partner.email``. The gate refuses such a field **unless a field-level rule
explicitly allows writing that exact field**. A model-level Allow is deliberately
*not* enough: granting write on ``crm.lead`` must not silently open
``res.partner`` as well.

The surface is wider than it looks. Core Odoo carries inverses on everyday
fields — a vendor bill's partner, journal, currency and payment term, an invoice
line's product and account, a lead's email — so expect to meet this rail on the
first real write you enable.

Either refusal is a configuration boundary, not abuse: it records no violation
and costs the user no strike.

Opening one of these fields
---------------------------

1. Go to :menuselection:`AI --> Configuration --> Security --> Access Rules`.
2. Create a rule with :guilabel:`Model` **and** :guilabel:`Field` set — the field
   is what makes it count.
3. Set :guilabel:`perm_write` = **Allow**.

.. important::
   A rule with :guilabel:`Field` left empty is a model-level rule and will not
   lift this rail, however permissive it looks. :guilabel:`perm_write` is the
   permission that counts, and it is also what opens the field inside a *create*
   payload: :guilabel:`perm_create` is model-level and is ignored on field rules.

   The rule lifts the inverse rail and nothing else. A field that is not stored in
   the database — ``product.template.standard_price`` is computed with an inverse
   but has no column — and a related field both stay refused however permissive
   the rule is. So if the refusal survives a correct field-level rule, the field
   is related or not stored, not an inverse field.

.. tip::
   When the refusal happens inside a one2many or many2many payload — an invoice
   line inside :guilabel:`Invoice lines`, for example — the assistant reports only
   the **parent** field, ``invoice_line_ids``, because that is the field it tried
   to write. The nested model and field that were actually refused go to the Odoo
   **server** log at INFO level; search it for ``AI x2many write refused``. They do
   not appear under :menuselection:`AI --> Monitoring --> Logs`, and a refusal for
   a missing field opt-in records no violation either — it is a configuration
   boundary, not abuse.

Defaults and recommended postures
=================================

Fresh install
-------------

- Read: **allow** (minus floor and strips) so the assistant is useful for Q&A.
- Create / write / delete: **deny** until you open specific models.
- Nine field-level write allows ship enabled, so the vendor-bill and
  invoice-line flows keep working under the cross-model rail above:
  ``account.move`` (partner, journal, currency, payment term, delivery date,
  payment reference) and ``account.move.line`` (product, account, partner).
  Nothing is opened on ``crm.lead``.

  These rows carry **no access group and no company**, so they are global rules:
  they apply to every AI user and every agent, not only to the invoicing flow.
  They arrive on install **and** on every upgrade of the AI app. If you edit or
  deactivate one, an upgrade will not overwrite your change; if you delete one, it
  comes back.

  They exist only where **Accounting** is installed, and each install or upgrade of
  the AI app seeds only the apps present at that moment. Install Accounting
  *after* the AI app and the rows appear only at the next upgrade of the AI app —
  until then the vendor-bill flow refuses invoice-line writes with no other
  symptom, so upgrade the AI app after adding Accounting.

.. warning::
   On the nested-line path the three ``account.move.line`` rows are real write
   permission, not only a lifted rail. A field-level Allow is resolved before the
   model tier and before the global default, so once write is allowed on
   ``account.move``, the assistant can set product, account and partner on invoice
   lines through :guilabel:`Invoice lines` even though write on
   ``account.move.line`` itself was never allowed — the create/write default of
   Deny does not hold that line. A *direct* write to ``account.move.line`` is
   still refused; only a payload nested inside a parent field skips the
   model-level check.

   Header fields on ``account.move`` are unaffected: writing the document still
   needs your own model-level Allow. To close the three line fields, add an
   explicit **Deny** — model-level on ``account.move.line``, or on the field — or
   deactivate the shipped rules. A Deny at either tier beats the Allow, and either
   edit survives every upgrade; deleting a shipped rule only brings it back.

Deny-by-default read (stricter)
-------------------------------

Set default read to **Deny**, then add Allow rules only for models the assistant
should see (e.g. ``product.product``, ``res.partner`` with field denies on
internal notes, etc.). Safer for regulated databases; requires more setup.

Examples
========

Deny all AI read on employees
-----------------------------

1. Create global rule on model ``hr.employee``.
2. Set :guilabel:`perm_read` = **Deny** (other perms inherit/deny as you like).

Allow support agent to create helpdesk tickets only
---------------------------------------------------

1. Create AI access group *Support bot* with the agent user as member.
2. Global defaults already deny create.
3. Rule on ``helpdesk.ticket`` (or ``project.task``) for that group:

   - ``perm_create`` = Allow  
   - ``perm_read`` = Deny (or Allow only safe fields via field rules)  
   - ``perm_write`` = Deny  
   - ``perm_delete`` = Deny  

4. Field-level: allow write on the few fields set at create time (name,
   description, partner email, team) if your policy requires write-allow to set
   values on create.
5. Ensure the agent **user** has matching Odoo ACLs to create those tickets —
   policy alone cannot grant create if the user group cannot.

Calendar free/busy without event details
----------------------------------------

Goal: agent may create a meeting in free slots but must not dump other people's
event subjects and attendees to the LLM.

1. Model ``calendar.event``:

   - ``perm_read`` = Deny at model level for the bot group, **or**
   - ``perm_read`` = Allow with field-level **Deny** on ``name``, ``description``,
     ``partner_ids``, ``videocall_location``, and similar.
2. Prefer a dedicated free-busy API/action if you add one later; raw event read
   is a common over-share.
3. ``perm_create`` = Allow with write-allow only on start, stop, name (generic),
   user_id.

See :doc:`agent_recipes` for end-to-end agent recipes that combine policy,
capabilities and channels.

Relation to Odoo record rules
=============================

AI policy does **not** replace record rules. Multi-company, follower-only
documents, and portal isolation remain enforced by Odoo when the gate runs as
the user. When designing "create but not read", verify both layers: a create
that returns a read snapshot may still fail or strip if read is denied — the
assistant should treat tool errors as authoritative.

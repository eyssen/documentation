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

1. **Hard-deny floor** — technical / self-protection models always deny.
2. **Field-level rules** (for read/write) — any explicit Deny wins.
3. **Model-level rules** — Deny overrides; most specific Allow wins among
   groups.
4. **Global defaults** from Settings (default_read / create / write / delete).

Unknown models or operations fail closed. Results are cached and invalidated
when rules, groups or parameters change.

Universal sanitiser rails (before/alongside policy)
===================================================

Independently of allow rules, the gate refuses or strips:

- magic fields;
- sensitive-looking field names (password, token, api_key, …);
- inverse-related hazards;
- lifecycle ``state`` writes;
- non-writable / complex types that must not be LLM-driven;
- hard-deny models in relational paths / domains.

Defaults and recommended postures
=================================

Fresh install
-------------

- Read: **allow** (minus floor and strips) so the assistant is useful for Q&A.
- Create / write / delete: **deny** until you open specific models.

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

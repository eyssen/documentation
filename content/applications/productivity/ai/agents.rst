======
Agents
======

An **agent** (``ai.agent``) describes *how* an AI colleague behaves. It is
**not** the same thing as the Odoo user account it may run as.

Two shapes
==========

Chat persona (no linked user)
-----------------------------

Example: shipped default **Jarvis**.

- Used when a human opens the AI chat.
- Runs **as the chatting user** (their ACLs, their AI policy membership).
- :guilabel:`System prompt`, model overrides and capabilities shape the
  session.
- No supervisor required.
- :guilabel:`Allowed groups` can restrict who may invoke this persona.

Autonomous colleague (linked user)
----------------------------------

- :guilabel:`User` points at a dedicated ``res.users``.
- Runs with **that user's** rights (like a human employee).
- :guilabel:`Supervisor` is mandatory — authorises work and approves write
  proposals.
- Channel rules decide who may address the agent and with what capability
  scope.
- Appears as ``is_ai_agent`` on the user (read-only indicator).

.. danger::
   Linking a wide-privilege user to an agent is equivalent to giving that
   privilege to a prompt-injectable worker. Always create a **narrow** user for
   the agent. Never use the superuser, portal users, Settings, or AI
   Administrator accounts.

Agent form fields
=================

:menuselection:`AI --> Configuration --> Behavior --> Agents`

+---------------------------+--------------------------------------------------+
| Field                     | Purpose                                          |
+===========================+==================================================+
| :guilabel:`Name`          | Display name (e.g. Support Assistant).           |
+---------------------------+--------------------------------------------------+
| :guilabel:`Active`        | Inactive agents do not run.                      |
+---------------------------+--------------------------------------------------+
| :guilabel:`Model`         | Optional model override; else main / defaults.   |
+---------------------------+--------------------------------------------------+
| :guilabel:`Temperature` / | Sampling overrides for this agent's turns.       |
| :guilabel:`Max tokens`    |                                                  |
+---------------------------+--------------------------------------------------+
| :guilabel:`System prompt` | Appended after global prompt layers.             |
+---------------------------+--------------------------------------------------+
| :guilabel:`Capabilities`  | Ceiling of tool classes for this agent.          |
+---------------------------+--------------------------------------------------+
| :guilabel:`Restricted to  | Who may invoke as chat persona.                  |
| groups`                   |                                                  |
+---------------------------+--------------------------------------------------+
| :guilabel:`User`          | Optional linked internal user (unique).          |
+---------------------------+--------------------------------------------------+
| :guilabel:`Supervisor`    | Required if User is set; must be AI: User.       |
+---------------------------+--------------------------------------------------+
| :guilabel:`Channel rules` | Default-deny allow-lists per channel.            |
+---------------------------+--------------------------------------------------+
| :guilabel:`Default agent` | Marks the persona used by default in chat.       |
+---------------------------+--------------------------------------------------+

Channel rules
=============

:menuselection:`AI --> Configuration --> Behavior --> Agents` → channel rules
(or dedicated channel rule views).

Channels:

- **Discuss direct message**
- **Chatter @mention**
- **Activity** (assigned activity)
- **Assignment** (e.g. project task assignee) — critical: without this, anyone
  who can assign a task could not be distinguished from a Discuss gate
- **Email** / **AI chat panel** — reserved / progressive wiring; default-deny
  still applies

Rule fields:

- :guilabel:`Allowed groups` / :guilabel:`Allowed users` — audience. **Empty
  audience matches nobody** (not everyone).
- :guilabel:`May request` — audience may trigger an ad-hoc run.
- :guilabel:`Scope mode`:

  - **Agent rights ∩ requester rights** (``intersect``, default) — capability
    *classes* both hold. Data is still read/written as the **agent**.
  - **The agent's full rights** (``agent_full``) — trusted audience only.

.. important::
   ``intersect`` is **not** "run as the requester". It only narrows tool
   classes (read/write/web/…). Record visibility remains the agent's. Only
   allow-list people you trust with whatever the agent can see.

Inbound flow (simplified)
=========================

1. Message / assignment / activity targets the agent.
2. If requester is **banned** → refuse (no LLM).
3. Resolve channel rule (default deny) → else refuse + violation / strike.
4. Enqueue inbound request; drain cron wakes.
5. Optional triage may subtract authority only.
6. Create task / run under supervisor scope; execute as agent user with
   committed capability ceiling.
7. Writes become pending proposals for the supervisor.
8. Agent posts notes / drafts on the thread as itself — customer text never
   becomes a silent privilege grant.

Tasks and runs
==============

Operational menus (AI: User, supervisor-scoped):

- :menuselection:`AI --> Agents --> Tasks` — work items (registry).
- :menuselection:`AI --> Agents --> Runs` — execution ledger and steps.

Supervisors use these to see what the agent attempted, which tools ran, and
which proposals are waiting.

AI Ops project stages
=====================

The module ships an **AI** project category, an **AI Agent** project template,
and a shared stage pack:

**Inbox → Review → Ready → Doing → Waiting → Done / Cancelled**

Suggested use:

- automated audit findings land in **Inbox** without assignee;
- managers refine in **Review**;
- assign the agent user only from **Ready**;
- **Waiting** for human input or approval;
- never auto-apply skills/policies from an audit without a human.

Support Assistant pack
======================

Shipped inactive **Support Assistant** agent with ask+read capabilities and
channel rules whose audiences are empty until you configure them. Activate by:

1. Creating a narrow internal user (helpdesk/project read as needed).
2. Linking it on the agent; set supervisor.
3. Filling channel audiences (groups/users who may DM / assign / @mention).
4. Setting :guilabel:`Active`.
5. Tuning AI access rules for ticket models.

Identity constraints (summary)
==============================

At link time the module rejects agent users that are:

- superuser (uid 1);
- share/portal;
- Settings / system administrator;
- AI Administrator;
- holding API keys (non-interactive login risk).

These checks are point-in-time on the agent form — do not "upgrade" the user
later from the Users menu.

Next: practical recipes in :doc:`agent_recipes`.

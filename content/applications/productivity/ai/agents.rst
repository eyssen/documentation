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
- :guilabel:`System Prompt`, model overrides and capabilities shape the
  session.
- No supervisor required.
- :guilabel:`Restricted to groups` can restrict who may invoke this persona.

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
| :guilabel:`Temperature`   | Sampling override for this agent's own turns,    |
|                           | withheld from models that do not accept one.     |
+---------------------------+--------------------------------------------------+
| :guilabel:`Max Tokens     | ``0``, the default, sends no cap at all: the     |
| (0 = no override)`        | model's own output limit applies. A positive     |
|                           | value caps this agent's completions instead —    |
|                           | see the note below.                              |
+---------------------------+--------------------------------------------------+
| :guilabel:`System Prompt` | Appended after global prompt layers.             |
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
| :guilabel:`Channel Rules` | Default-deny allow-lists per channel.            |
+---------------------------+--------------------------------------------------+
| :guilabel:`Default agent` | Marks the persona used by default in chat.       |
+---------------------------+--------------------------------------------------+

.. note::
   A cap only takes effect where the model record publishes an output limit of
   its own, and it behaves differently per provider. Both rules, and what an
   update does to agents that already carry a value, are described once under
   :ref:`ai/config/completion-caps`.

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
- :guilabel:`May Request` — audience may trigger an ad-hoc run.
- :guilabel:`Scope Mode`:

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
7. Writes follow that **task's** :guilabel:`Write Mode` (default: pending
   proposals for the supervisor; see :ref:`ai/agents/task-write-mode`).
8. Agent posts notes / drafts on the thread as itself — customer text never
   becomes a silent privilege grant.

Tasks and runs
==============

Operational menus (AI: User, supervisor-scoped):

- :menuselection:`AI --> Agents --> Tasks` — work items (registry).
- :menuselection:`AI --> Agents --> Runs` — execution ledger and steps.

Supervisors use these to see what the agent attempted, which tools ran, and
which proposals are waiting.

.. _ai/agents/task-write-mode:

Task write mode (agent runs only)
---------------------------------

Each task carries :guilabel:`Write Mode`. It applies **only** to agent runs
dispatched for that task — not to interactive chat (chat uses the global
setting under :menuselection:`AI --> Configuration --> Settings`).

+------------------------------------------+-----------------------------------+
| Value                                    | Effect on that task's runs        |
+==========================================+===================================+
| **Always require confirmation**          | Every create / write / delete /   |
| (``confirm``, default)                   | file attach becomes an            |
|                                          | ``ai.pending.write`` for the      |
|                                          | supervisor.                       |
+------------------------------------------+-----------------------------------+
| **Create automatically, confirm updates**| Creates apply immediately;        |
| (``hybrid``)                             | updates, deletes and file         |
|                                          | attaches still need approval.     |
+------------------------------------------+-----------------------------------+
| **Apply immediately** (``auto``)         | Allowed mutations apply at once   |
|                                          | under the agent user's rights and |
|                                          | the run's capability ceiling.     |
+------------------------------------------+-----------------------------------+

The global ``ai.write_mode`` parameter never overrides a task: an
administrator cannot flip every unattended agent to auto with one setting.
``hybrid`` / ``auto`` are deliberate per-task opt-ins for **trusted, low-risk**
work — for example an accounts-payable standing task that fills **draft**
vendor bills and whose skill **never posts** invoices. Prefer ``confirm``
whenever a run could post, pay, delete, or touch customer-facing data.

When a proposal is created, the platform also places a **To-Do activity** (and
usually a chatter note) on the **target business record** when one exists
(e.g. the vendor bill being updated), falling back to the agent task for
creates that have no id yet. Confirm and Cancel still live on
:menuselection:`AI --> Write Proposals`; the activity is only a systray nudge
so the supervisor lands on the invoice or partner, not only on the abstract
proposal list. The Write Proposals form has :guilabel:`Open record` for the
same jump. The activity is closed when the proposal is applied, cancelled or
expired.

.. tip::
   The hard-deny floor blocks raw AI tools on every ``ai.*`` platform model.
   Agents therefore cannot “manage” their own approval queue or AI config via
   tools — and should not try. Platform nudges and skill-driven review
   activities on business documents use controlled paths; instruct agents not
   to invent AI-config tool calls, or they will burn refusals and strikes.

A run's ledger row becomes visible to other users only once the attempt has
**ended** or **parked for approval**: the row is written and finalised inside the
worker's own transaction, so nothing is committed while the agent is still
working. The runs list therefore shows completed work, not a live view of what is
executing right now.

Failed runs carry a :guilabel:`Failure Type` on the run form that says which kind
of failure it was — see :doc:`monitoring` for the values worth watching.

.. _ai/agents/cancel:

Stopping a run
--------------

Open the run and use :guilabel:`Request Cancellation`. The button appears while
the run is :guilabel:`Running` or :guilabel:`Waiting for approval`, and only the
agent's supervisor or an AI administrator may request it.

.. important::
   This button is not a general "stop the agent now" control, because of the
   ledger behaviour above: a run that is executing normally has no row yet, so
   there is nothing to open. In practice you use it on a run parked in
   :guilabel:`Waiting for approval`, or on one left in :guilabel:`Running` by an
   earlier server incident. To stop unwanted work in advance instead, keep the
   task's :guilabel:`Deadline Seconds` short enough that a run ends on its own,
   and clear :guilabel:`Active` on the task so it is not dispatched again.

Cancelling a run parked in :guilabel:`Waiting for approval` withdraws its open
write proposals, then closes the run: as :guilabel:`Done` if a proposal of that
run had already been applied, otherwise as :guilabel:`Failed` with
:guilabel:`Failure Type` ``waiting_approval_empty``, since nothing it proposed
was approved.

Cancelling a run that is genuinely still executing is **cooperative, never
immediate**. The request is read at the start of each provider round and again
before each tool call, so it takes effect only after the round-trip already in
flight has finished — allow up to about two minutes at the shipped defaults, and
never in the middle of a provider call. Such a run then closes as
:guilabel:`Failed` with :guilabel:`Failure Type` ``cancelled``; there is no
separate *Cancelled* state. The steps it did execute stay on the
:guilabel:`Steps` tab, the run's answer records the cancellation rather than a
partial reply, and any write proposals it had already opened are cancelled with
it, so nothing is left approvable. A cancellation is neutral for the task's
automatic deactivation: it neither counts as a failure nor clears an existing
streak.

.. note::
   If no worker is left to hear the request, the button answers
   :guilabel:`Nothing in flight to cancel` instead of confirming. Nothing is
   broken — the run has most likely already finished, or its worker died — but no
   worker will see the request and the run will not stop on its account. Reload
   the record to see where it really stands; a dead worker's run is closed by the
   stuck-run reaper below.

.. _ai/agents/reaper:

Runs whose worker died
----------------------

If the server process handling a run is killed (restart, out-of-memory, hard
kill), nobody is left to finish the run. A scheduled action, **AI: reap stuck
agent runs**, runs every 15 minutes and closes them: the run is recorded as
:guilabel:`Failed` with :guilabel:`Failure Type` ``reaped_stuck``, a note is
posted on the task, and any write proposals still waiting on it are expired so
nothing can be approved on behalf of a dead run. If the crash took the ledger row
with it, the housekeeping job rebuilds one from the record the dispatch left
behind — provided that record was written; a kill early enough to prevent even
that leaves nothing to rebuild from.

Do not expect that closure within 15 minutes. The run has to age past its own
time limit plus a grace period (10 minutes by default — see
:doc:`configuration`) before a pass will touch it, and passes are 15 minutes
apart, so worst case is around half an hour. One pass closes at most 200 runs,
oldest first; a large backlog after a restart storm drains over the following
passes.

The same scheduled action also frees runs parked in :guilabel:`Waiting for approval`
that have no open proposal left — for example when the last proposal expired
while the supervisor was still confirming it — so such a run is not left holding
an activity reminder for a proposal that no longer exists.

.. tip::
   Every dispatch attempt carries a :guilabel:`Dispatch Token`, shown on the run
   form. It is the key that joins a run to the short-lived record written when
   the run started, which is what both the reaper and
   :guilabel:`Request Cancellation` look for — so it is also the value to quote
   when correlating a run with the server log.

.. _ai/agents/dispatch-triage:

Pre-run instruction check
-------------------------

Scheduled and :guilabel:`Run Now` runs execute the task's standing instruction
directly. Tick :guilabel:`Triage On Dispatch` on a task to run the same stage-1
check that an agent addressed from chat receives. The check can only **narrow**
what the task already grants — it never widens anything.

Consider before enabling it:

- it costs one extra model call per run (time and tokens), and the scheduler
  reserves about 30 seconds of its own tick budget for that call. A task whose
  :guilabel:`Deadline Seconds` already sits close to the worker's time limit may
  therefore be skipped rather than dispatched;
- the check has its own short deadline of 15 seconds and is fail-closed: a triage
  model that is slow, unreachable, or answers off-schema counts as a refusal;
- a refusal means the agent never starts. The run is recorded as
  :guilabel:`Failed` with :guilabel:`Failure Type` ``triage_denied``, a note is
  posted on the task, and a :guilabel:`To-Do` activity is created for the
  supervisor — so no refusal is silent;
- refusals count towards the task's automatic deactivation. The task is archived
  once five consecutive runs have failed **and** the streak is more than seven
  days old, and its supervisor is notified. Because a triage failure is a
  refusal, a long provider outage can archive a task that was never
  misconfigured; that is why the option is per task and off by default;
- what the check decided is recorded on the run as :guilabel:`Triage Verdict`, on
  the :guilabel:`Snapshot` tab, and is empty on every run of a task that did not
  opt in. It is telemetry, not a boundary: the narrowing it describes is already
  committed in the run's :guilabel:`Allowed Caps`, which is what the access gate
  reads.

The global kill switch for stage-1 triage — inbound addressing and this pre-run
check alike — is the ``ai.triage_enabled`` system parameter, under
:menuselection:`Settings --> Technical --> Parameters --> System Parameters`
(which needs :doc:`developer mode <../../general/developer_mode>`).

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

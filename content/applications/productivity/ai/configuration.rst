=============
Configuration
=============

Most day-to-day platform options live under
:menuselection:`AI --> Configuration`. Global defaults that map to system
parameters are on the **Settings** page (Settings users only).

Settings
========

Open :menuselection:`AI --> Configuration --> Settings` (or the AI section on
the main Settings app).

Guided system setup
-------------------

- :guilabel:`Start setup assistant` — opens chat with the guided setup skill for
  system administrators. Module install is never free-form: when setup plans are
  used, install goes through a confirmable plan (MVP may propose only).

Abuse guardrails
----------------

+----------------------------+--------------------------------------------------+
| Setting                    | Meaning                                          |
+============================+==================================================+
| :guilabel:`Ai Max Strikes` | Violations in the window before a temporary ban  |
|                            | (default 3).                                     |
+----------------------------+--------------------------------------------------+
| :guilabel:`Ai Strike       | Hours over which strikes accumulate (default 24).|
| Window Hours`              |                                                  |
+----------------------------+--------------------------------------------------+
| :guilabel:`Ai Ban Minutes` | How long a ban lasts (default 60).               |
+----------------------------+--------------------------------------------------+

Rate and usage limits
---------------------

+------------------------------------------+------------------------------------------+
| Setting                                  | Meaning                                  |
+==========================================+==========================================+
| :guilabel:`Ai Rate Limit Rpm`            | Max requests per minute per user         |
|                                          | (default 20).                            |
+------------------------------------------+------------------------------------------+
| :guilabel:`Ai Max Daily Calls`           | 0 = unlimited.                           |
+------------------------------------------+------------------------------------------+
| :guilabel:`Ai Max Daily Cost Usd`        | Soft cost cap using model unit prices; 0 |
|                                          | = unlimited. Unpriced models may not     |
|                                          | enforce cost well.                       |
+------------------------------------------+------------------------------------------+
| :guilabel:`Ai Max Conversations Per Day` | 0 = unlimited.                           |
+------------------------------------------+------------------------------------------+
| :guilabel:`Ai Max Successive Calls`      | Bound on chained model turns (default    |
|                                          | 10).                                     |
+------------------------------------------+------------------------------------------+
| :guilabel:`Ai Max Tool Calls`            | Bound on tool invocations per turn loop  |
|                                          | (default 10).                            |
+------------------------------------------+------------------------------------------+
| :guilabel:`Ai Write Mode`                | **Interactive chat only** — auto /       |
|                                          | confirm / hybrid. Agent runs use each    |
|                                          | task's own :guilabel:`Write Mode`        |
|                                          | instead (default confirm). See           |
|                                          | :doc:`using_the_assistant` and           |
|                                          | :ref:`ai/agents/task-write-mode`.        |
+------------------------------------------+------------------------------------------+
| :guilabel:`Chat write-proposal           | Minutes until a chat proposal expires; 0 |
| lifetime (minutes)`                      | = never.                                 |
+------------------------------------------+------------------------------------------+
| :guilabel:`Agent write-proposal          | Minutes until an agent proposal expires  |
| lifetime (minutes)`                      | (default 1440); 0 = never.               |
+------------------------------------------+------------------------------------------+

Logging
-------

- :guilabel:`Ai Log Level` — *Metadata only* (default, recommended) or *Full
  payload* (stores message/tool content; high sensitivity).
- :guilabel:`Run Step Retention (Days)` — purge horizon for
  ``ai.agent.run.step`` journal rows (default 90; 0 disables). Does **not**
  auto-purge ``ai.log`` or run headers.

Model
-----

- :guilabel:`AI Model` — the model used by the interactive assistant. Its
  provider is used automatically.

This setting covers the interactive assistant only. A per-agent completion cap
is set on the agent itself (:doc:`agents`) and depends on the model record — see
:ref:`ai/config/completion-caps`.

Access policy defaults
----------------------

Applied when no more specific ``ai.access.rule`` decides:

- Default **read**: Allow  
- Default **create** / **write** / **delete**: Deny  

See :doc:`access_policy` for rules and groups.

Runtime introspection
---------------------

- :guilabel:`Publish Installed Modules` — whether environment facts may include
  the installed module list (still subject to the user's
  ``ir.module.module`` ACL). Denying makes the assistant more cautious, not
  magically more accurate. Version, edition, company and user facts remain.

Web access and files
--------------------

Requires the **Web access** capability to be enabled for tools to be offered.

+----------------------------------+-------------------------------------------+
| Setting                          | Meaning                                   |
+==================================+===========================================+
| :guilabel:`Search Backend`       | ``ai.web.provider`` used by               |
|                                  | ``web_search``. Empty = search off.       |
+----------------------------------+-------------------------------------------+
| :guilabel:`Fetch Backend`        | Provider for ``web_fetch``; empty falls   |
|                                  | back to built-in Direct fetch.            |
+----------------------------------+-------------------------------------------+
| :guilabel:`Allowed Domains`      | Comma-separated allow-list; empty = any   |
|                                  | public host (SSRF protections still       |
|                                  | apply to private ranges).                 |
+----------------------------------+-------------------------------------------+
| :guilabel:`Daily Limit`          | Max web calls per user per company; 0 =   |
|                                  | unlimited.                                |
+----------------------------------+-------------------------------------------+
| :guilabel:`Max Page Text`        | Characters retained from a fetched page.  |
+----------------------------------+-------------------------------------------+
| :guilabel:`Max Query Length`     | Cap on search query size.                 |
+----------------------------------+-------------------------------------------+
| :guilabel:`Allowed Image Types`, | MIME allow-lists for ingest.              |
| :guilabel:`Allowed Document      |                                           |
| Types`                           |                                           |
+----------------------------------+-------------------------------------------+
| :guilabel:`Max File Size`        | Bytes (default 10 MiB).                   |
+----------------------------------+-------------------------------------------+

System parameters and scheduled actions
=======================================

A few platform switches have no field on the Settings page. They live in the
Technical menus, which require
:doc:`developer mode <../../general/developer_mode>`.

System parameters
-----------------

:menuselection:`Settings --> Technical --> Parameters --> System Parameters`

- ``ai.triage_enabled`` — global off switch for stage-1 triage, covering both
  the inbound check and a task's :guilabel:`Triage On Dispatch` (default
  ``True``). Set it to ``False`` and every instruction is executed unassessed.
- ``ai.waiting_approval_ttl_minutes`` — how long a run may sit waiting for a
  supervisor's answer before it is failed (default ``1440``; ``0`` means never
  expire by age).
- ``ai.run_reaper_grace_seconds`` — how long past a task's own time limit the
  stuck-run reaper waits before it declares a run abandoned (default ``600``,
  i.e. 10 minutes). This is not a kill switch: to stop reaping altogether,
  deactivate the scheduled action instead.

Scheduled actions
-----------------

:menuselection:`Settings --> Technical --> Automation --> Scheduled Actions`

The module ships seven scheduled actions, all active after install:

- **AI: Expire user bans** (hourly) — lifts the temporary bans whose end time
  has passed.
- **AI: Expire pending writes** (every 15 minutes) — expires write proposals
  older than their configured lifetime. It first releases the proposals left
  behind by a run that has already finished, so a lifetime of ``0`` does not
  also disable that sweep.
- **AI: dispatch scheduled agent tasks** (every 5 minutes) — starts the agent
  tasks that are due. This is only how often the dispatcher itself wakes; each
  task's own interval decides its cadence, so the cron has to wake at least as
  often as the shortest interval configured on a task.
- **AI: drain inbound addressing requests** (every minute) — starts the runs
  queued when somebody addresses an agent through a Discuss message, a chatter
  mention, an activity or an assignment. It is deliberately more frequent than
  the dispatcher, because somebody is waiting for the reply.
- **AI: expire waiting-approval agent runs** (every 15 minutes) — fails the runs
  that have waited for a supervisor's answer longer than
  ``ai.waiting_approval_ttl_minutes``, and expires the proposals they were
  waiting on.
- **AI: reap stuck agent runs** (every 15 minutes) — closes runs whose worker
  died, and also frees runs parked for approval with nothing left to approve.
  Both jobs, their cadence and their batch limit are described in
  :ref:`ai/agents/reaper`.
- **AI: memory maintenance** (every 6 hours) — archives working memories past
  their expiry date, lets the salience of untouched entries decay, and flags
  high-salience personal entries as promotion candidates for an administrator.

LLM providers and models
========================

:menuselection:`AI --> Configuration --> Providers --> LLM Providers`

Fields of interest:

- Provider type and API key (system parameter storage).
- :guilabel:`Base Url` — only override when you understand the trust boundary
  (a writable base URL can be an SSRF risk if pointed at internal services).
- :guilabel:`Timeout`, :guilabel:`Max Retries`, :guilabel:`Call Deadline` —
  wall-clock budget for one provider call including retries.

:menuselection:`AI --> Configuration --> Providers --> Models`

- :guilabel:`Model` — exact vendor id.
- :guilabel:`Context Window`, :guilabel:`Max Output Tokens`, tool and
  temperature support flags.
- Prompt / completion unit prices and price source (provider API, curated
  catalog, or manual — manual is not overwritten by refresh).

.. _ai/config/completion-caps:

Completion caps
---------------

:guilabel:`Max Output Tokens` on the model is what the assistant caps its
completions at, and it is also the precondition for a per-agent cap. Only
providers that publish a completion limit fill it in; ``0`` means *unknown*.

An agent's own :guilabel:`Max Tokens (0 = no override)` (:doc:`agents`) reaches
every provider — OpenAI, OpenRouter, xAI, Google Gemini and Anthropic — each
under the parameter name its API expects. It is put on the wire **only** for a
model that publishes a :guilabel:`Max Output Tokens` of its own. Point an agent
at a model that still reads ``0`` and the agent's value is dropped: the model
writes to its own limit, and nothing on the agent form says why. Fill in
:guilabel:`Max Output Tokens` on the model if you want the per-agent cap to bite.

``0`` on the agent — the default — means *no override*: the model's own output
cap applies, exactly as for a turn with no agent at all. Set a positive value
only where you deliberately want that agent to be terser or cheaper, and
remember that on reasoning models the cap counts thinking tokens too, so a low
value truncates answers.

.. note::
   Anthropic is the exception, in the other direction: its API always requires
   the parameter. An Anthropic model whose :guilabel:`Max Output Tokens` is still
   ``0`` therefore falls back to a conservative built-in value of 1024 tokens,
   not to the model's real limit.

.. warning::
   Upgrading from an earlier version changes how agents that are already
   configured behave.

   - A cap an administrator had already typed on an agent used to reach Anthropic
     only. It now applies on every provider, so a low value that was inert on
     OpenAI, OpenRouter, xAI or Gemini starts truncating answers there.
   - The upgrade resets the old shipped default of ``2048`` to ``0`` on every
     agent still carrying it, so that no database keeps a cap nobody chose. On
     an Anthropic model that publishes a cap of its own, that 2048 was genuinely
     in force: those agents may now write up to the model's full
     :guilabel:`Max Output Tokens` — more tokens, more cost and more time, and an
     answer long enough to exhaust the provider's :guilabel:`Call Deadline` fails
     with an error instead of stopping at 2048 tokens.

   Any other value you typed is kept. Re-enter a cap on every agent you meant to
   limit, including one you had deliberately set to 2048.

Web providers
=============

:menuselection:`AI --> Configuration --> Providers --> Web Providers`

Configure search/fetch backends (factory rows may ship for common engines).
Assign them in Settings as search/fetch backends.

MCP servers
===========

:menuselection:`AI --> Configuration --> Providers --> MCP Servers`

Model Context Protocol servers expose **external** tools to the assistant when
the **MCP tools** capability is enabled. Factory MCP definitions may ship
inactive or empty of secrets.

Per server, typically configure:

- endpoint / transport;
- authentication secrets (never commit them to docs or git);
- which users/groups may use the server's tools;
- enable/disable.

Every MCP call still re-checks capability and server audience. Treat MCP like
installing untrusted plugins: least privilege, no production secrets in tool
responses you do not need.

Prompt layers
=============

:menuselection:`AI --> Configuration --> Behavior --> Prompt Layers`

Layered system prompts (core, global, module, …) shape behaviour. Core safety
layers are not meant for casual editing. Global operational layers may be
adjusted by AI administrators; migrations may refresh factory content only when
still pristine.

.. important::
   A layer's :guilabel:`Body` is **English only** and not translatable. These are
   the rails the model is steered by, not user-facing text: rails that switched
   language with the interface would leave the instructions in one language and
   the tool names in another. The assistant still answers in the language of the
   conversation — that is decided by the user's messages, never by this text.

   On a database upgraded from an earlier version, each layer keeps its English
   body and any translated bodies are discarded. Re-check every global and
   per-module layer whose body you had edited in a translated interface.

Blocked patterns
================

:menuselection:`AI --> Configuration --> Security --> Blocked Patterns`

Regex (or pattern) rules on input/output that raise violations when matched
(e.g. classic "ignore previous instructions" probes). Extend carefully —
over-broad patterns create false positives and strike noise.

Allowed actions
===============

:menuselection:`AI --> Configuration --> Security --> Allowed Actions`

Allow-list of business methods the **Action** capability may invoke via
``call_action`` (e.g. mark activity done). Methods not listed cannot be called
through AI even if Write is on. Prefer allow-listed actions over raw field
writes for lifecycle transitions.

Customizations ledger
=====================

:menuselection:`AI --> Configuration --> Customizations`

When **Customize UI & schema** is used, changes are tracked in a ledger with
import/export for recovery. Primary UX is still chat tools for admins; the
ledger is the admin recovery path.

Setup plans
===========

:menuselection:`AI --> Configuration --> Setup Plans` (Settings users)

Plans proposed by the guided setup flow for module installation / configuration
steps that require explicit confirmation.

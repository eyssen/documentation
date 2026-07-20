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
| :guilabel:`Max strikes`    | Violations in the window before a temporary ban  |
|                            | (default 3).                                     |
+----------------------------+--------------------------------------------------+
| :guilabel:`Strike window   | Hours over which strikes accumulate (default 24).|
| (hours)`                   |                                                  |
+----------------------------+--------------------------------------------------+
| :guilabel:`Ban (minutes)`  | How long a ban lasts (default 60).               |
+----------------------------+--------------------------------------------------+

Rate and usage limits
---------------------

+------------------------------------+------------------------------------------+
| Setting                            | Meaning                                  |
+====================================+==========================================+
| :guilabel:`Rate limit (RPM)`       | Max requests per minute per user         |
|                                    | (default 20).                            |
+------------------------------------+------------------------------------------+
| :guilabel:`Max daily calls`        | 0 = unlimited.                           |
+------------------------------------+------------------------------------------+
| :guilabel:`Max daily cost (USD)`   | Soft cost cap using model unit prices; 0 |
|                                    | = unlimited. Unpriced models may not     |
|                                    | enforce cost well.                       |
+------------------------------------+------------------------------------------+
| :guilabel:`Max conversations / day`| 0 = unlimited.                           |
+------------------------------------+------------------------------------------+
| :guilabel:`Max successive calls`   | Bound on chained model turns (default    |
|                                    | 10).                                     |
+------------------------------------+------------------------------------------+
| :guilabel:`Max tool calls`         | Bound on tool invocations per turn loop  |
|                                    | (default 10).                            |
+------------------------------------+------------------------------------------+
| :guilabel:`Write mode`             | Chat only — auto / confirm / hybrid.     |
|                                    | See :doc:`using_the_assistant`.          |
+------------------------------------+------------------------------------------+
| :guilabel:`Chat write-proposal     | Minutes until a chat proposal expires; 0 |
| lifetime`                          | = never.                                 |
+------------------------------------+------------------------------------------+
| :guilabel:`Agent write-proposal    | Minutes until an agent proposal expires  |
| lifetime`                          | (default 1440); 0 = never.               |
+------------------------------------+------------------------------------------+

Logging
-------

- :guilabel:`Log level` — *Metadata only* (default, recommended) or *Full
  payload* (stores message/tool content; high sensitivity).
- :guilabel:`Run step retention (days)` — purge horizon for
  ``ai.agent.run.step`` journal rows (default 90; 0 disables). Does **not**
  auto-purge ``ai.log`` or run headers.

Model
-----

- :guilabel:`AI Model` — the model used by the interactive assistant. Its
  provider is used automatically.

Access policy defaults
----------------------

Applied when no more specific ``ai.access.rule`` decides:

- Default **read**: Allow  
- Default **create** / **write** / **delete**: Deny  

See :doc:`access_policy` for rules and groups.

Runtime introspection
---------------------

- :guilabel:`Publish installed modules` — whether environment facts may include
  the installed module list (still subject to the user's
  ``ir.module.module`` ACL). Denying makes the assistant more cautious, not
  magically more accurate. Version, edition, company and user facts remain.

Web access and files
--------------------

Requires the **Web access** capability to be enabled for tools to be offered.

+----------------------------------+-------------------------------------------+
| Setting                          | Meaning                                   |
+==================================+===========================================+
| :guilabel:`Search backend`       | ``ai.web.provider`` used by               |
|                                  | ``web_search``. Empty = search off.       |
+----------------------------------+-------------------------------------------+
| :guilabel:`Fetch backend`        | Provider for ``web_fetch``; empty falls   |
|                                  | back to built-in Direct fetch.            |
+----------------------------------+-------------------------------------------+
| :guilabel:`Allowed domains`      | Comma-separated allow-list; empty = any   |
|                                  | public host (SSRF protections still       |
|                                  | apply to private ranges).                 |
+----------------------------------+-------------------------------------------+
| :guilabel:`Daily limit`          | Max web calls per user per company; 0 =   |
|                                  | unlimited.                                |
+----------------------------------+-------------------------------------------+
| :guilabel:`Max page text`        | Characters retained from a fetched page.  |
+----------------------------------+-------------------------------------------+
| :guilabel:`Max query length`     | Cap on search query size.                 |
+----------------------------------+-------------------------------------------+
| :guilabel:`Allowed image / doc   | MIME allow-lists for ingest.              |
| types`                           |                                           |
+----------------------------------+-------------------------------------------+
| :guilabel:`Max file size`        | Bytes (default 10 MiB).                   |
+----------------------------------+-------------------------------------------+

LLM providers and models
========================

:menuselection:`AI --> Configuration --> Providers --> LLM Providers`

Fields of interest:

- Provider type and API key (system parameter storage).
- :guilabel:`Base URL` — only override when you understand the trust boundary
  (a writable base URL can be an SSRF risk if pointed at internal services).
- :guilabel:`Timeout`, :guilabel:`Max retries`, :guilabel:`Call deadline` —
  wall-clock budget for one provider call including retries.

:menuselection:`AI --> Configuration --> Providers --> Models`

- :guilabel:`Model id` — exact vendor id.
- Context window, max output tokens, tool and temperature support flags.
- Prompt / completion unit prices and price source (provider API, curated
  catalog, or manual — manual is not overwritten by refresh).

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

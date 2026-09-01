===============
Getting started
===============

Install the app
===============

1. Activate :doc:`developer mode <../../general/developer_mode>` if you need
   technical menus later; ordinary setup does not require it.
2. Go to :menuselection:`Apps`, remove the *Apps* filter if needed, search for
   **AI**.
3. Install **AI (Experimental)** (module technical name ``ai``).

After install, the **AI** root menu appears for users in the **AI: User** group.

Assign access rights
====================

1. Open :menuselection:`Settings --> Users & Companies --> Users`.
2. For each person who may use the assistant, enable **AI: User** under the
   **AI** category.
3. For administrators who configure providers, policies and agents, enable
   **AI: Administrator**.
4. System settings (API keys, global defaults, guided setup) still require
   **Settings** / Administration rights.

.. tip::
   Supervisors of autonomous agents must be **AI: User** (so they can open
   write proposals). They do not need AI Administrator unless they also
   configure the platform.

Connect a provider
==================

1. Open :menuselection:`AI --> Configuration --> Providers --> LLM Providers`.
2. Create or open a provider and set:

   - :guilabel:`Provider type` — OpenRouter, OpenAI, Anthropic, xAI or Google
     Gemini.
   - :guilabel:`API key` — write-only; stored in system parameters, never shown
     again in clear text.
   - Optional :guilabel:`Base URL` override for compatible gateways.
   - Timeouts / retries / call deadline as needed for your workers.

3. Use the provider's **Refresh models** (or equivalent) action to import the
   model catalogue and prices where available.
4. Open :menuselection:`AI --> Configuration --> Settings` and set
   :guilabel:`AI Model` to the model the interactive assistant should use.

.. important::
   The assistant is a **tool-calling** loop. Choose a model with tool / function
   support enabled on the :guilabel:`Models` form (``supports_tools``).

Safe defaults after install
===========================

Out of the box the platform is intentionally cautious:

+---------------------------+-----------------------------------------------+
| Area                      | Default                                       |
+===========================+===============================================+
| Capabilities **ask**,     | Enabled for AI users                          |
| **read**, **navigate**,   |                                               |
| **setup** (admins only)   |                                               |
+---------------------------+-----------------------------------------------+
| **write**, **delete**,    | **Disabled**                                  |
| **web**, **mcp**,         |                                               |
| **customize**, **action** |                                               |
+---------------------------+-----------------------------------------------+
| Access policy defaults    | read **allow**; create / write / delete       |
|                           | **deny** at model level                       |
+---------------------------+-----------------------------------------------+
| Field-level write allows  | Nine field-scoped write rules on              |
|                           | ``account.move`` / ``account.move.line``      |
|                           | (:doc:`access_policy`)                        |
+---------------------------+-----------------------------------------------+
| Chat write mode           | **hybrid** (auto-create; confirm update /     |
|                           | delete / file attach)                         |
+---------------------------+-----------------------------------------------+
| Default agent             | **Jarvis** (chat persona, no linked user)     |
+---------------------------+-----------------------------------------------+
| Support Assistant agent   | Present but **inactive** until you link a     |
|                           | user and open channel audiences               |
+---------------------------+-----------------------------------------------+

Those nine field-level rules exist so the invoice / vendor-bill flow keeps
working, and they are seeded only where **Accounting** is installed. Nothing
writes while the Write capability is off, so they take effect only once you
enable it.

.. tip::
   Once Write is on, expect some ordinary fields to be refused anyway, because
   writing them also writes a second model. The refusal names the model and the
   fields it would not write, but not the reason — read
   :ref:`ai/policy/cross-model` before you conclude that policy is broken.

First conversation
==================

1. Ensure your user has **AI: User** and a main model is set.
2. Click the AI bubble in the systray (backend), or open
   :menuselection:`AI --> Conversations` and start a chat.
3. Ask something that needs this database, for example: "Which modules are
   installed?" or "Search partners named Acme".
4. The assistant should call tools (``get_environment``, ``search``, …) rather
   than inventing schema.

If nothing answers, check: provider active, API key set, main model set, user
not banned, rate limits not exhausted
(:doc:`monitoring`).

Optional next steps
===================

- Tighten read policy for HR / accounting models — :doc:`access_policy`.
- Enable Write only for a pilot group — :doc:`capabilities_and_tools`.
- Activate **Support Assistant** or design domain agents —
  :doc:`agents` and :doc:`agent_recipes`.
- Review the full security checklist — :doc:`security`.

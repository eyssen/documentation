==========
MCP server
==========

With the MCP server enabled, your Odoo database can be connected to external AI
apps that speak the Model Context Protocol, such as Claude, ChatGPT or an
AI-enabled code editor. The app can then search and read the data its user can
see in Odoo and, with confirmation, propose changes, from inside the app the
person already uses.

.. note::
   This is the opposite direction of :menuselection:`AI --> Configuration -->
   Providers --> MCP Servers`, where Odoo calls tools of other servers (see
   :doc:`configuration`). Here Odoo is the server.

Enable the server
=================

1. Install the modules AI MCP Gateway (and, for portal users, AI MCP Gateway -
   Portal).
2. Open :menuselection:`AI --> Configuration --> Settings`, find the block
   :guilabel:`MCP server` and turn it on. The setting is off by default.
3. Copy the address from :guilabel:`MCP server URL`. It is your Odoo address
   followed by ``/mcp``, and it is what you paste into the AI app.

.. important::
   AI apps call the server without a login cookie, so Odoo must select this
   database from the host name alone. If the server serves several databases,
   set its ``dbfilter`` option so that this host name selects only this database
   (for example ``^%d$`` with one database per subdomain), or serve a single
   database. If that is not the case, the settings page shows a warning and the
   apps get "404 Not Found".

Connect an AI app
=================

1. In the AI app, add a custom connector or MCP server and paste the server URL.
2. The app opens an Odoo sign-in page. Sign in with your own account. Only
   internal users in the :guilabel:`AI: User` group can connect, and the group
   is checked again on every request.
3. A consent page says which app wants to connect, what it will be able to do
   (:guilabel:`Read only` or :guilabel:`Read and propose changes`) and which
   tools it can use. Click :guilabel:`Allow` or :guilabel:`Deny`. Consent is
   asked every time an app connects.

Behind the scenes the connection uses OAuth 2.1 with PKCE. Access tokens are
short-lived and refresh tokens rotate on every use; only hashes are stored.
Scripted clients can alternatively use an Odoo API key as the bearer token, if
:guilabel:`Accept Odoo API keys` is on.

Connected apps and disconnecting
================================

Every user sees their own connections in their preferences, on the tab
:guilabel:`Connected AI apps`, with the date connected and last use.
:guilabel:`Disconnect` takes effect immediately.

Administrators see all connections under :menuselection:`AI --> Configuration
--> MCP Server --> Connected AI apps` (with :guilabel:`Revoke`) and the
registered apps under :menuselection:`AI --> Configuration --> MCP Server --> AI
Apps`. Revoking a refresh token revokes the whole connection.

Which tools are exposed
=======================

The server does not hand out everything the assistant can do. It offers an
allow-list of tools that are known to respect confirmation, filtered by the
user's own capabilities:

- Reading and looking up: search, read, group and aggregate records, describe
  fields, search the documentation of models, read the environment, list allowed
  actions and skills and use a skill, compute dates, read attachments, list
  menus, search memory, search and fetch web pages (if the Web access capability
  is on).
- Changing (only if the Write, Delete or Business actions capability is on):
  create, update and delete records, call an allowed business action, fetch a
  file into a field.

Not exposed, whatever the capabilities: saving or forgetting memories, creating
or running automations, changing views, fields or models, generating images and
the website builder tools. A token with only read access sees only the read
tools. Every tool call runs as the user, through the same access rules, policy
checks and audit as the assistant in Odoo.

Changes made by AI apps
=======================

By default :guilabel:`Always ask for confirmation` applies: each connection has
its own conversation ("MCP: app name"), and every create, update, delete or
action becomes a proposal that you approve in the AI panel (see :doc:`panel`).
The alternative :guilabel:`Follow the AI write settings` uses the global write
mode instead. Each tool call is written to the AI log as an MCP call and counts
towards the rate limits.

Choose the behaviour in the setting :guilabel:`Changes made by AI apps`.

Registering apps
================

There are two ways to let an app in.

- You register it yourself under :menuselection:`AI --> Configuration --> MCP
  Server --> AI Apps`: the :guilabel:`App name` shown on the consent page and
  the allowed :guilabel:`Redirect URIs`. Use :guilabel:`Generate secret` for a
  confidential app (the secret is shown only once) or :guilabel:`Make public
  (PKCE only)` for apps that cannot keep a secret.
- Or you turn on :guilabel:`Allow dynamic client registration` and apps register
  themselves. This is off by default. When on, registration is limited per
  network address (:guilabel:`Registrations per address and hour`, 10 by
  default), the registered addresses must match :guilabel:`Allowed redirect URI
  patterns`, and apps that never get used are deleted after 72 hours. An
  authorization error of an app that is not yet reviewed is shown on an error
  page instead of redirecting back to the app.

More settings in the block :guilabel:`MCP server`: :guilabel:`Token lifetimes`
(access token minutes and refresh token days) and :guilabel:`Allowed browser
origins` for browser-based apps. The default redirect patterns accept
``https://`` addresses and the local loopback addresses used by desktop tools.

Portal users
============

With the portal module and the setting :guilabel:`Portal users may connect AI
apps` (off by default), portal users can connect AI apps too, from the page "My
AI apps" of the portal. They get only the search, read and group tools,
read-only, and only for models that have an explicit read allow rule in an AI
access group they belong to. A shipped, empty group :guilabel:`Portal users
(MCP)` is mapped to all portal users for that purpose. Odoo's own portal rights
still apply underneath.

Limits
======

- The server is stateless and answers single requests: no streaming, no
  server-initiated messages, no resources or prompts.
- Apps are identified by registration (yours or dynamic), not by a URL-based
  client identity document.
- A user who is archived, removed from the AI group or banned loses access on
  the next request.

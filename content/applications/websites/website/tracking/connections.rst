===========
Connections
===========

The browser tags (Google tag, Google Tag Manager, Meta Pixel) only need the identifiers of your
accounts. The features that talk to the **platform APIs** need a **connection** to a Google or
Meta account:

- Google: Merchant Center synchronization, offline conversions, Customer Match, Search Console,
  Business Profile reviews.
- Meta: Conversions API (unless you enter an access token), catalog, Lead Ads, pages, Instagram,
  and WhatsApp (unless you enter a system user token).

A connection is made once by an administrator and can be shared by all the websites of a company.

.. _tracking/connections/modes:

Two ways to connect
===================

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Mode
     - Description
   * - :guilabel:`Own app credentials`
     - You create your own Google Cloud OAuth client or your own Meta app and enter its identifier
       and secret in Odoo. You control the app, its verification, and its quotas.
   * - :guilabel:`Broker service`
     - Your database connects through a **broker**: a central Odoo database that owns one verified
       Google OAuth client and one Meta app and serves many databases. You do not create any app;
       you only enter the broker URL, your instance ID, and the instance secret that the broker's
       administrator gave you. See :doc:`/applications/general/tracking_broker`.

Broker mode is the easiest if your provider offers it. Own credentials are the choice if you want
to depend on nobody, or if you are the provider.

.. note::
   If a broker is configured in the :guilabel:`Connection Broker` setting (see below), new
   connections are created in broker mode by default.

Create a connection
===================

Go to :menuselection:`Website --> Configuration --> Tracking & Consent --> Connections` (or
:menuselection:`Google --> Configuration --> Connections` / :menuselection:`Meta --> Configuration
--> Connections`). This menu is only available to administrators. Click :guilabel:`New` and fill in:

- :guilabel:`Name`: for example `Google - Main account`.
- :guilabel:`Provider`: :guilabel:`Google` or :guilabel:`Meta`.
- :guilabel:`Company`: with several companies.
- :guilabel:`Mode`: :guilabel:`Own app credentials` or :guilabel:`Broker service`.

In :guilabel:`Own app credentials` mode, enter the :guilabel:`Client ID / App ID` and the
:guilabel:`Client Secret / App Secret` of your app, and register the **redirect URI** displayed in
the :guilabel:`Redirect Uri` field in the app (it ends with `/website_tracking/oauth/callback`). In
:guilabel:`Broker service` mode, enter the :guilabel:`Broker URL`, the :guilabel:`Broker Instance ID`,
and the :guilabel:`Broker Instance Secret`.

Click :guilabel:`Connect`. You are sent to Google or Meta to sign in with the account that manages
your assets and to accept the permissions, then you come back to Odoo. The status changes to
:guilabel:`Connected`, and the :guilabel:`Connected Account`, the :guilabel:`Scopes`, and the
:guilabel:`Token Expiry` are displayed.

.. screenshot:: tracking-connection-form
   :menu: Website ‣ Configuration ‣ Tracking & Consent ‣ Connections ‣ (a connection)
   :shows: A connection form in Connected status: the Connect/Reconnect, Test, and Disconnect
      buttons, the status bar, the provider, the mode, the connected account name, the scopes, and
      the token expiry.
   :highlight: The status bar and the buttons (red frame).
   :data: Connection "Google - Main account", mode "Broker service".
   :notes: English UI, light theme, 1440px width. Use a throw-away account.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Button
     - Action
   * - :guilabel:`Connect` / :guilabel:`Reconnect`
     - Starts the authorization. Use :guilabel:`Reconnect` when the permissions changed or the
       connection is in error.
   * - :guilabel:`Test`
     - Gets a fresh access token and displays :guilabel:`Connection works` with the account name.
   * - :guilabel:`Disconnect`
     - Revokes the authorization at Google or Meta (or at the broker) and erases the tokens. The
       connection stays in the list as :guilabel:`Not connected`.

The status is :guilabel:`Error` when Odoo cannot get a token anymore (revoked access, expired
token, wrong secret). The reason is displayed in :guilabel:`Last Error`; fix it and click
:guilabel:`Reconnect`.

.. important::
   Google refreshes its access automatically. A Meta user token lasts about 60 days: with your own app,
   reconnect when the status turns to :guilabel:`Error`; with a broker, the token is extended
   automatically when it is used during its last seven days, and you reconnect if it expired. Without
   a valid token, the Meta features that use the connection stop.

Select the connection of a website
==================================

Each website uses one connection per provider: select it in the :guilabel:`Google Connection` field
of the Google settings (:guilabel:`Google Account` setting), or in the :guilabel:`Meta Connection`
field of the Meta settings (:guilabel:`Meta Connection` setting). You can create the connection
directly from these fields.

Create your own Google app
==========================

#. In the `Google Cloud console <https://console.cloud.google.com>`_, create a project (or select
   an existing one) and enable the APIs of the features you use: **Search Console API**,
   **Business Profile APIs**, **Merchant API** and **Content API for Shopping**, **Google Ads API**,
   and **Data Manager API**.
#. Configure the **OAuth consent screen** with the scopes below. Google verifies applications that
   ask for sensitive scopes before external users can accept them; until then the app stays in
   *testing* mode, and its authorizations expire after a few days.
#. Create an **OAuth client ID** of type *Web application*, and add the redirect URI of the
   connection in :guilabel:`Authorized redirect URIs`.
#. Copy the client ID and the client secret into the connection.

One Google connection serves every Google feature, so it asks for all the scopes at once: Merchant
Center (`content`), Data Manager API (`datamanager`), Google Ads API (`adwords`), Search Console
(`webmasters`), and Business Profile (`business.manage`).

Create your own Meta app
========================

#. In `Meta for Developers <https://developers.facebook.com>`_, create an app of type **Business**
   and add the **Facebook Login for Business** product.
#. In its settings, add the redirect URI of the connection in :guilabel:`Valid OAuth Redirect
   URIs`.
#. Request the permissions you need (see below). For a use limited to your own business assets, the
   *standard access* of an app in development mode is enough for the people who have a role in the
   app; other users need *advanced access* after Meta's app review.
#. Copy the app ID and the app secret into the connection.

The Meta connection asks for these permissions: `ads_management`, `business_management`,
`catalog_management`, `leads_retrieval`, `pages_show_list`, `pages_read_engagement`,
`pages_manage_metadata`, `pages_manage_posts`, `pages_messaging`, `instagram_basic`,
`instagram_content_publish`, `instagram_manage_messages`, `whatsapp_business_management`, and
`whatsapp_business_messaging`.

The same app can be used for :doc:`webhooks </applications/websites/meta/connection>`.

.. _tracking/connections/broker-setting:

Connection Broker setting
=========================

If your provider operates a broker, go to :menuselection:`Website --> Configuration --> Settings`,
and, in the :guilabel:`Tracking` block, fill in the :guilabel:`Connection Broker` setting:

- :guilabel:`Broker URL`: the address of the broker (for example `https://connect.example.com`).
- :guilabel:`Broker Instance ID`: the identifier of your database at the broker.
- :guilabel:`Broker Instance Secret`: the secret that the broker's administrator showed you once.

Leave the fields empty to use your own app credentials. The new connections are then created in
broker mode and need no further data: click :guilabel:`Connect`.

.. tip::
   The broker only accepts return addresses that its administrator registered for your instance:
   if you use a new domain name for the website, ask the administrator of the broker to add it.

.. seealso::
   - :doc:`/applications/general/tracking_broker`
   - :doc:`/applications/websites/google/connection`
   - :doc:`/applications/websites/meta/connection`

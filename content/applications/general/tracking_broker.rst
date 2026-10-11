=====================================
Connection broker for Google and Meta
=====================================

A **connection broker** is a central Odoo database that owns **one** verified Google OAuth client and
**one** Meta app, and lets many other Odoo databases (the *instances*) connect to Google and Meta
accounts through it. The instances do not create any app at Google or Meta: their administrators just
click :guilabel:`Connect`.

This page is for the administrators of a company that **offers** the connection as a service to several
databases, for example an integrator who manages the databases of its customers. If you only use the
Google or Meta app in your own database, read :doc:`/applications/websites/website/tracking/connections`
instead.

.. important::
   The broker is a separate database, installed only once. Do not install it on the databases that
   use the Google and Meta apps. Install *Website Tracking Connection Broker* from :menuselection:`Apps`
   in the central database.

How it works
============

#. The administrator of an instance clicks :guilabel:`Connect` on a connection in :guilabel:`Broker
   service` mode.
#. The instance sends the administrator to the broker with a **signed request**. The broker checks
   the instance, the signature, the return address, and the requested permissions, then redirects the
   administrator to the consent screen of Google or Meta.
#. After the consent, the broker keeps the long-lived secret of the account (the Google refresh token or
   the Meta long-lived token) **encrypted**, and sends the administrator back to the instance with a
   one-time code that is valid for ten minutes.
#. The instance redeems the code. From then on, it asks the broker for **short-lived access tokens** when
   it needs to call Google or Meta. The long-lived secrets never leave the broker.

The broker never reads the data of the instances: it only holds the authorizations.

Set up the broker
=================

Go to :menuselection:`Settings --> Tracking Broker --> Settings`. All the settings below are available
to administrators only.

Encryption key
--------------

The tokens are stored encrypted with a key. Generate a key and add it to the server configuration file:

.. code-block:: text

   website_tracking_broker_key = <key>

You can list several keys separated by commas: the first one encrypts, all of them decrypt. This lets you
rotate the key. The :guilabel:`Token Encryption` setting shows the :guilabel:`Encryption Key Status`.

.. warning::
   Without the option in the configuration file, Odoo generates a key and keeps it in the database. A
   warning is displayed in the settings. A key stored in the database is lost with it: use the
   configuration file in production, and keep a copy of the key in a safe place. If the key is lost, all
   the connections must be made again.

Public URL
----------

In the :guilabel:`Public URL` setting, enter the public HTTPS address of the broker (for example
`https://connect.example.com`). It is given to the instances. The **redirect URIs** to register at
Google and Meta are displayed in the settings: the address followed by `/broker/google/callback` and
`/broker/meta/callback`.

.. screenshot:: general-tracking-broker-settings
   :menu: Settings ‣ Tracking Broker ‣ Settings
   :shows: The Tracking Broker settings: the Public URL, the Token Encryption status, the Google
      OAuth Client with the redirect URI, the Allowed Scopes, the Meta App with the app ID, the
      secret (hidden), the Graph API version and the redirect URI, and the Allowed Permissions.
   :highlight: The Public URL and the redirect URIs (red frame).
   :data: Public URL "https://connect.example.com", secrets hidden.
   :notes: English UI, light theme, 1440px width. Use a test database.

Google
------

#. In the Google Cloud console, create a project and enable the APIs that your customers use (Content
   API for Shopping and Merchant API, Google Ads API, Data Manager API, Search Console API, Business
   Profile APIs, Analytics Admin API).
#. Configure the **OAuth consent screen** with the scopes that you allow, and create an OAuth client
   ID of type *Web application* with the Google redirect URI displayed in the settings.
#. Enter the :guilabel:`Broker Google Client ID` and the :guilabel:`Broker Google Client Secret` in
   the :guilabel:`OAuth Client` setting.
#. Check the :guilabel:`Allowed Google Scopes`: the scopes that the instances may request, separated by spaces.
   Any other request is refused.

.. important::
   Google must **verify** your application before people outside your organization can grant it
   sensitive scopes (Google Ads, Search Console, Business Profile, Merchant Center). Until it is
   verified, the application stays in *testing* mode and the authorizations expire after a few days.

Meta
----

#. In Meta for Developers, create an app of type **Business** and add the *Facebook Login for Business*
   product.
#. Add the Meta redirect URI displayed in the settings to the valid OAuth redirect URIs.
#. Request the *advanced access* of the permissions that you allow (app review).
#. Enter the :guilabel:`Broker Meta App ID`, the :guilabel:`Broker Meta App Secret`, and the
   :guilabel:`Broker Graph API Version` in the :guilabel:`Meta App` setting, and check the
   :guilabel:`Allowed Meta Permissions`.

Register the instances
======================

Go to :menuselection:`Settings --> Tracking Broker --> Broker Instances`, and create **one record per
customer database**:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Name` and :guilabel:`Customer`
     - To recognize the instance.
   * - :guilabel:`Instance ID`
     - The identifier of the instance, generated by Odoo. Copy it.
   * - :guilabel:`Broker URL`
     - The address of the broker to give to the instance.
   * - :guilabel:`Google` and :guilabel:`Meta`
     - The providers that the instance may use.
   * - :guilabel:`Allowed Hosts`
     - The host names of the websites of the instance, one per line (`www.example.com`, or
       `host:port`). The broker only redirects the administrators back to these hosts, which must use
       HTTPS (plain HTTP is accepted for `localhost`).

Click :guilabel:`Show Secret`. A window displays the :guilabel:`Broker URL`, the :guilabel:`Instance
ID`, and the **secret**. **The secret is displayed only once**: copy the three values and send them
securely to the administrator of the instance. If the secret is lost, click :guilabel:`Generate New
Secret`; the instance must then be updated.

The administrator of the instance enters the three values in :menuselection:`Website --> Configuration
--> Settings --> Tracking --> Connection Broker`. See
:ref:`tracking/connections/broker-setting`.

.. screenshot:: general-tracking-broker-instance
   :menu: Settings ‣ Tracking Broker ‣ Instances ‣ (an instance)
   :shows: An instance form with the Show Secret and Generate New Secret buttons, the Instance group
      (customer, instance ID, broker URL), the Providers group, the Allowed Hosts, and the Grants
      tab.
   :highlight: The Show Secret button and the Allowed Hosts (red frame).
   :data: Instance "Customer website" with host "www.example.com".
   :notes: English UI, light theme, 1440px width.

Follow and revoke the connections
=================================

:menuselection:`Settings --> Tracking Broker --> Broker Grants` lists the connections made through the
broker: the instance, the provider, the connected account, the last use, and the status.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Status
     - Meaning
   * - :guilabel:`Pending`
     - The administrator came back from the consent screen, but the instance did not redeem the code
       yet. The grants that are not redeemed in ten minutes are deleted.
   * - :guilabel:`Active`
     - The instance uses the grant.
   * - :guilabel:`Error`
     - The broker cannot get a token anymore (access revoked by the user, expired Meta token). The
       administrator of the instance has to reconnect. The reason is displayed in :guilabel:`Last
       Error`.
   * - :guilabel:`Revoked`
     - Disconnected by the instance or by you.

Click :guilabel:`Revoke` on a grant to disconnect it. The authorization is also revoked at Google or
Meta, unless another grant uses the same account.

.. tip::
   A Meta token lasts about 60 days. The broker extends it automatically when it is used during the
   last seven days and Meta allows it. If the token expired before, or if Meta refuses, the status
   turns to :guilabel:`Error` and the administrator of the instance has to click
   :guilabel:`Reconnect`.

Security
========

- Each request of an instance is **signed** with its secret. A request with a wrong signature, an
  unknown instance, or a provider that is not allowed is refused, and the number of requests is
  limited.
- The broker only redirects to the allowed hosts of the instance, and only the allowed scopes are
  requested.
- The instances receive access tokens that last a few minutes (Google) or the long-lived token
  needed for the call (Meta); the refresh tokens stay encrypted in the broker.
- Treat the broker as a sensitive system: restrict the access to its database, use HTTPS only, and
  back up the encryption key.

.. seealso::
   - :doc:`/applications/websites/website/tracking/connections`
   - :doc:`/applications/websites/google/connection`
   - :doc:`/applications/websites/meta/connection`

=======================
Connection and webhooks
=======================

The Conversions API (without an access token), the product catalog, Lead Ads, the Facebook and
Instagram pages, and WhatsApp use the Meta API. They need a **Meta connection** to the account that
manages your business assets, and, to receive notifications in real time, a **webhook**.

Connect Meta
============

#. As an administrator, go to :menuselection:`Meta --> Configuration --> Connections` and create a
   connection with the :guilabel:`Meta` provider. Choose the mode:

   - :guilabel:`Broker service`: nothing to create at Meta. Your provider's broker owns the Meta
     app. See :doc:`/applications/general/tracking_broker`.
   - :guilabel:`Own app credentials`: create a Meta app and enter its ID and secret, as explained in
     :ref:`tracking/connections/modes`.

#. Click :guilabel:`Connect`, sign in with the Facebook account that manages your business assets,
   and accept the permissions. Select all the assets (pages, catalogs, ad accounts, WhatsApp
   accounts) that Odoo may use.
#. In :menuselection:`Meta --> Configuration --> Settings`, in the :guilabel:`Meta API` block, select
   the connection in the :guilabel:`Meta Connection` field.

.. screenshot:: meta-settings-connection
   :menu: Meta ‣ Configuration ‣ Settings
   :shows: The Meta API block of the Meta settings with the Meta Connection setting (Meta Connection
      and Graph API Version fields, Connections link) and the Webhooks setting enabled with the
      callback URL, the app ID, the app secret (hidden), the verify token, and the Generate Verify
      Token and Webhook Notifications links.
   :highlight: The Meta Connection field (red frame).
   :data: Connection "Meta - Main account".
   :notes: English UI, light theme, 1440px width, crop to the block.

One connection serves every Meta feature: Odoo asks for all the permissions at once. The
:guilabel:`Graph API Version` field (administrators only) is the version of the Meta API that Odoo
calls; keep the default value unless a Meta announcement tells you to change it.

.. important::
   A Meta access token lasts about **60 days**. When it expires, the connection turns to
   :guilabel:`Error` and the Meta features stop (the events stay in the queue and are retried). Open
   the connection and click :guilabel:`Reconnect`.

.. _meta/webhooks:

Webhooks
========

Meta calls your database when something happens: a person fills in a lead form, a customer writes
on Messenger, Instagram, or WhatsApp, or a message is delivered. Odoo stores the notification and
processes it a few minutes later.

#. In the :guilabel:`Meta API` block, enable :guilabel:`Webhooks`. This setting applies to the whole
   company and is visible to administrators only.
#. Copy the :guilabel:`Webhook Callback URL`.
#. Enter the :guilabel:`Meta App ID` and the :guilabel:`Meta App Secret` of your Meta app. The secret
   is used to check that the notifications really come from Meta.
#. Click :guilabel:`Generate Verify Token` (or type any secret string) and save.
#. In your Meta app, open the *Webhooks* product, and for each object that you use (*Page*,
   *Instagram*, *WhatsApp Business Account*), enter the callback URL and the verify token, then
   subscribe to the fields you need (for example `leadgen` for Lead Ads, `messages` for WhatsApp).

A Meta app has a single callback URL for each object. The notifications therefore reach the database
whose address is registered in the app. If you :doc:`connect through a broker
</applications/general/tracking_broker>`, the Meta app belongs to the broker: the features that need
webhooks (Lead Ads, Facebook and Instagram messages, WhatsApp) require **your own Meta app**, unless the
administrator of the broker tells you that the notifications are forwarded to your database.

.. note::
   Odoo refuses a notification whose signature does not match the app secret. If you have several
   companies with webhooks enabled, each company must use its own Meta app, or the same app and
   secret.

The :guilabel:`Webhook Notifications` link opens the list of the notifications received
(:menuselection:`Meta --> Webhook Notifications`):

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Status
     - Meaning
   * - :guilabel:`Pending`
     - Waiting for the next processing.
   * - :guilabel:`Processed`
     - Handled. Processed and ignored notifications are deleted after 30 days.
   * - :guilabel:`Ignored`
     - A kind of notification that no feature of your database uses.
   * - :guilabel:`Error`
     - Still failing after five attempts. Read the error, fix the cause, and click :guilabel:`Process
       Again`.

.. _meta/webhooks/troubleshooting:

Webhook troubleshooting
-----------------------

- **Meta refuses the callback URL.** The database must be reachable from the Internet over HTTPS, the
  verify token in Meta must be identical to the one in Odoo, and :guilabel:`Webhooks` must be
  enabled.
- **Nothing arrives.** Check that your Meta app is in *Live* mode, and that the page or the
  WhatsApp account is subscribed to the app.
- **Notifications in error.** Open one: the :guilabel:`Payload` tab shows the data, and the error
  shows why it failed. A missing contact or a missing permission are the usual causes.
- **Notifications stay pending.** They are processed by a scheduled action. Ask your administrator
  whether it is active.

.. seealso::
   - :doc:`/applications/websites/website/tracking/connections`
   - :doc:`lead_ads`
   - :doc:`whatsapp`

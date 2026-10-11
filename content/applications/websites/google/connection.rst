==========
Connection
==========

Search Console, Business Profile, Merchant Center, offline conversions, and Customer Match use the
Google APIs. They need a Google account that manages the assets (the website property, the business
location, the Merchant Center account, the Google Ads account) and a :doc:`connection
</applications/websites/website/tracking/connections>` between Odoo and that account.

Connect
=======

#. As an administrator, go to :menuselection:`Google --> Configuration --> Connections` and create a
   connection with the :guilabel:`Google` provider. Choose the mode:

   - :guilabel:`Broker service`: nothing to create at Google. Your provider's broker holds the OAuth
     client. See :doc:`/applications/general/tracking_broker`.
   - :guilabel:`Own app credentials`: create an OAuth client in the Google Cloud console and enter
     its ID and secret, as explained in :ref:`tracking/connections/modes`.

#. Click :guilabel:`Connect`, sign in with the Google account that has access to your assets, and
   accept the permissions.
#. In :menuselection:`Google --> Configuration --> Settings`, in the :guilabel:`Google APIs` block,
   select the connection in the :guilabel:`Connection` field of the :guilabel:`Google Account`
   setting. This setting is visible to administrators only.

.. screenshot:: google-settings-connection
   :menu: Google ‣ Configuration ‣ Settings
   :shows: The Google APIs block of the Google settings with the Google Account setting and its
      Connection field set to a connected connection, then the Search Console and Business Profile
      Reviews settings.
   :highlight: The Connection field (red frame).
   :data: Connection "Google - Main account".
   :notes: English UI, light theme, 1440px width, crop to the block.

The Google account must have enough rights in each product: at least *Full user* on the Search
Console property, *Manager* of the Business Profile location, *Standard access* on the Merchant
Center account, and access to the Google Ads account (directly or through a manager account, see
:doc:`offline_conversions`).

.. note::
   The browser features (Google tag, Tag Manager, conversions, consent mode, Measurement Protocol)
   do not use the connection: you can use them without it.

.. seealso::
   - :doc:`/applications/websites/website/tracking/connections`
   - :doc:`search_console_reviews`
   - :doc:`merchant_center`

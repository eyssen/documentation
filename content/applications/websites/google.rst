:show-content:
:hide-page-toc:

======
Google
======

The **Google** app connects your website to Google Analytics 4, Google Tag Manager, Google Ads,
Search Console, Business Profile, and Merchant Center. All its settings are in one place:
:menuselection:`Google --> Configuration --> Settings`.

.. cards::

   .. card:: Tags and Analytics
      :target: google/tags

      Google tag (Google Analytics 4), Google Tag Manager, GA4 user ID and debug mode.

   .. card:: Consent mode
      :target: google/consent_mode

      Advanced and basic Consent Mode v2, regional defaults, ads data redaction, URL passthrough.

   .. card:: Google Ads
      :target: google/ads

      Conversion actions, enhanced conversions, dynamic remarketing, cart data, new customers.

   .. card:: Measurement Protocol
      :target: google/measurement_protocol

      Send refunds, lead stages, store sales, and confirmed purchases to GA4 from the server.

   .. card:: Connection
      :target: google/connection

      Connect a Google account with your own OAuth client or through a broker.

   .. card:: Search Console and reviews
      :target: google/search_console_reviews

      Search statistics and Business Profile reviews in Odoo.

   .. card:: Merchant Center
      :target: google/merchant_center

      Product feed, Merchant API synchronization, product statuses, promotions, Customer Reviews.

   .. card:: Offline conversions and audiences
      :target: google/offline_conversions

      Upload orders to Google Ads and feed Customer Match audiences.

   .. card:: Google Ads lead forms
      :target: google/lead_forms

      Create CRM leads from lead form assets and report the lead stages.

The Google app is based on the :doc:`shared tracking base </applications/websites/website/tracking/overview>`: read
the pages about :doc:`consent </applications/websites/website/tracking/cookie_consent>`, :doc:`privacy
</applications/websites/website/tracking/privacy>`, and :doc:`testing </applications/websites/website/tracking/troubleshooting>`.

.. toctree::
   :titlesonly:
   :hidden:

   google/tags
   google/consent_mode
   google/ads
   google/measurement_protocol
   google/connection
   google/search_console_reviews
   google/merchant_center
   google/offline_conversions
   google/lead_forms

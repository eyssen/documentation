=================================
Testing and troubleshooting
=================================

Test every integration before you start a campaign, and again after each change to the website, the
cookies bar, or the checkout. Use the tools below, from the simplest to the most detailed.

.. _tracking/troubleshooting/prepare:

Before you test
===============

#. Test in a **private window** that is not logged in as an administrator. No event is sent while
   you edit the website or translate it.
#. Accept the cookies: open the :ref:`Customize panel <tracking/consent/customize>` and accept the
   analytics and marketing cookies. Check the line that appeared in the :ref:`consent log
   <tracking/consent/log>`.
#. Disable the ad blockers of your browser.
#. Enable the :guilabel:`Tracking Debug Mode` in :menuselection:`Website --> Configuration -->
   Settings` to see every event and its data in the browser console (open the developer tools of
   your browser). Disable it afterwards.

Tools
=====

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Tool
     - Use
   * - Google Tag Assistant
     - Open `tagassistant.google.com <https://tagassistant.google.com>`_ and connect your website.
       It shows which Google tags and Google Tag Manager containers load on each page, the consent
       signals, and the events.
   * - GA4 DebugView
     - Enable :guilabel:`GA4 Debug Mode` in the Google settings, then open *Admin ► DebugView* in
       Google Analytics: the events of your browser appear in real time. For the events of the
       server, enable :guilabel:`MP Validation Mode` (see below).
   * - Meta Test Events
     - In Meta Events Manager, open the dataset and the *Test events* tab, copy the test code,
       paste it in :guilabel:`Test Event Code` (Meta settings, after enabling :guilabel:`Test
       Events`), and click :guilabel:`Send Test Event`. See :ref:`meta/capi/test`.
   * - Server Events list
     - Check that the server events are :guilabel:`Sent`, and read the answer of the provider when
       they are in :guilabel:`Error`. See :doc:`server_events`.
   * - Lead Ads testing tool
     - Meta's tool to create a test lead on one of your pages. See :ref:`meta/lead-ads/test`.
   * - WhatsApp test number
     - Meta gives a free test number in the *API Setup* of your app. See :ref:`meta/whatsapp/test`.
   * - Merchant Center diagnostics
     - Check the feed status and the product issues. See :doc:`/applications/websites/google/merchant_center`.

Validation modes
================

Some APIs can check a request without recording it. Use these modes before the first real
campaign:

- :guilabel:`MP Validation Mode` (Google, GA4 Measurement Protocol): the server events go to
  Google's validation server. Nothing reaches the reports, and Google's validation messages are
  displayed on the server events.
- :guilabel:`Validation Mode` (Google, Google Ads account): the offline conversions and the Customer
  Match members are sent with the "validate only" option: Google checks them and records nothing.
- :guilabel:`Test Events` (Meta, Conversions API): the events are sent with the test code and
  appear only in the *Test events* tab.

The server events sent in these modes are marked and can be filtered with the :guilabel:`Test
Events` filter. **Disable the modes before going live**, otherwise nothing is recorded.

Common problems
===============

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Symptom
     - Check
   * - No event at all
     - Is the cookies bar enabled and are the marketing/analytics cookies accepted? Is the
       :guilabel:`Cookie Policy Version` the one of the cookie you have? Did you select the right
       website in :guilabel:`Settings of Website`? Is the Google tag or the pixel enabled with a
       valid ID? Are you logged in as a designer, or in edit mode?
   * - The pixel or the Google tag loads only on the second page
     - Basic consent mode, or the pixel is not loaded before the consent. Enable the Google
       *Advanced* consent mode and, if your legal basis allows it, :guilabel:`Load Before Consent`.
   * - The purchase is counted twice
     - A purchase is sent by the browser and by the server with the same event ID: the platform
       deduplicates them. A count that is higher than expected usually means that two tags send the
       purchase (for example a Google Tag Manager tag and the Google tag): disable one of them.
       See :ref:`ecommerce/tracking/purchase`.
   * - The purchase is not reported
     - Look at the :guilabel:`Report Purchases` setting: with :guilabel:`When the order is
       confirmed`, a purchase paid by wire transfer is reported only once it is confirmed. Check the
       :guilabel:`Purchase Reported` field of the order.
   * - Dynamic remarketing or catalog ads do not match the products
     - The :guilabel:`Product Identifier` of the website must be the same in the events and in the
       product feeds. Check the warnings of the feed.
   * - A server event is in error
     - Open it and read the :guilabel:`Response` tab. Typical causes: a missing access token or API
       secret, a connection in error, a missing consent, or an expired event.
   * - The connection is in error
     - Click :guilabel:`Reconnect`. See :doc:`connections`.
   * - The webhook is not verified, or no notification arrives
     - See :ref:`meta/webhooks/troubleshooting`.

.. seealso::
   - :doc:`server_events`
   - :doc:`privacy`

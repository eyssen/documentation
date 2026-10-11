====================
Measurement Protocol
====================

The **GA4 Measurement Protocol** lets the server send events to Google Analytics 4 when no browser
is involved: a refund posted by the accountant, a lead that moves in the CRM pipeline, a sale at the
point of sale, or a purchase confirmed days after the visit. The server events are queued, sent every
few minutes, and visible in the :doc:`server events list
</applications/websites/website/tracking/server_events>`.

Set it up
=========

#. In Google Analytics, open *Admin > Data streams*, select your web stream, and under *Measurement
   Protocol API secrets* create a secret.
#. In Odoo, go to :menuselection:`Google --> Configuration --> Settings`. In the :guilabel:`Google
   Analytics` block, enable :guilabel:`Measurement Protocol` and fill in:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Measurement ID`
     - The GA4 measurement ID receiving the events. Leave it empty to use the measurement ID of
       the :ref:`Google tag <google/tags/google-tag>`.
   * - :guilabel:`API Secret`
     - The secret created in Google Analytics. Only administrators can see it.

Then choose what the server sends. All the events require the **analytics** consent of the
visitor (or of the customer), except store purchases:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Option
     - Events sent
   * - :guilabel:`Refunds`
     - A `refund` event when a credit note of a website order is posted. Enabled by default.
   * - :guilabel:`Lead Events`
     - The lead stage events of the CRM (qualified, working, won, lost…) defined by the :doc:`lead
       stage rules </applications/sales/crm/optimize/lead_tracking>`, and leads that do not come
       from a website form. Enabled by default.
   * - :guilabel:`Store Purchases`
     - A `purchase` event for each paid point of sale order of an identified customer. See
       :doc:`/applications/sales/point_of_sale/store_sales_tracking`.
   * - :guilabel:`Purchases from the Server`
     - See :ref:`google/mp/purchases`.

.. screenshot:: google-settings-measurement-protocol
   :menu: Google ‣ Configuration ‣ Settings
   :shows: The Google Analytics block of the Google settings: the GA4 User ID and GA4 Debug Mode
      options, then the Measurement Protocol setting enabled with the measurement ID, the API secret
      (hidden), the five options, and the Server Events link.
   :highlight: The Measurement Protocol setting (red frame).
   :data: Measurement ID "G-ABCDE12345", secret hidden (throw-away).
   :notes: English UI, light theme, 1440px width, crop to the block.

.. _google/mp/purchases:

Purchases from the server
=========================

By default, the purchase of a website order is sent by the **browser** of the customer when the
confirmation page is displayed (see :ref:`ecommerce/tracking/purchase`). That fails for an order paid
later by a bank transfer, or that you confirm by hand.

If :guilabel:`Report Purchases` is set to :guilabel:`When the order is confirmed` in the eCommerce
tracking settings, enable :guilabel:`Purchases from the Server`: the purchase is then sent by the
server when the order is confirmed, wherever the customer is, and the browser does **not** send it a
second time. If you use Google Tag Manager, the `purchase` event of the data layer is flagged so that
you can exclude it from your GA4 tag.

.. important::
   The events are rejected by Google if they are older than 72 hours: an event that cannot be sent
   within three days is marked :guilabel:`Discarded`.

Validation mode
===============

Enable :guilabel:`MP Validation Mode` while you test: the events are sent to Google's validation
server instead of the reports. Nothing is recorded, and the validation messages are displayed on the
server events. Disable it to go live. See :doc:`/applications/websites/website/tracking/troubleshooting`.

.. seealso::
   - :doc:`tags`
   - :doc:`/applications/websites/website/tracking/privacy`

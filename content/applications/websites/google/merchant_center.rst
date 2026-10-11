=================
Merchant Center
=================

Google Merchant Center displays your products in Google Shopping, Free listings, Performance Max,
and YouTube. The app offers two ways to give your products to Merchant Center, which can be used
together:

- a :doc:`product feed </applications/websites/ecommerce/product_feeds>` that Merchant Center
  **fetches** on a schedule;
- the **Merchant API synchronization**, which **sends** each change of a product at once and
  imports the status of the products every day.

It also publishes your discount codes as promotions, and offers the Google Customer Reviews survey
to your customers.

Go to :menuselection:`Google --> Configuration --> Settings`: the :guilabel:`Merchant Center` block
contains the settings of this page. They require eCommerce.

.. note::
   The synchronization and the promotions use the :doc:`Google connection <connection>`, and the
   scope of the connection must include Merchant Center. The fetched feed needs no connection.

.. _google/merchant/feed:

Product feeds
=============

In the :guilabel:`Product Feeds` setting:

- :guilabel:`Merchant Center ID`: the number of your Merchant Center account (digits only).
- :guilabel:`Product Feed`: the feed of the :guilabel:`Google Merchant Center` channel of the
  website. Click the :guilabel:`Product Feed` button to open or create it.
- :guilabel:`Reviews Feed`: a feed of the :guilabel:`Google product reviews` channel, to publish the
  product reviews of your customers. Click :guilabel:`Product Reviews Feed` to open or create it.

Create the feeds as described in :doc:`/applications/websites/ecommerce/product_feeds`.

.. screenshot:: google-settings-merchant-feeds
   :menu: Google ‣ Configuration ‣ Settings
   :shows: The Merchant Center block of the Google settings: the Product Feeds setting with the
      Merchant Center ID, Product Feed, and Reviews Feed fields and the two buttons, then the
      Merchant API Product Sync, Promotions, and Google Customer Reviews settings.
   :highlight: The Product Feeds setting (red frame).
   :data: Merchant Center ID "123456789" (throw-away), feed "Google Shopping ES".
   :notes: English UI, light theme, 1440px width, crop to the block.

To let Merchant Center fetch the feed, open the feed in Odoo, copy its **Feed URL** (the secret
address, see :ref:`ecommerce/feeds/url`), and in Merchant Center add a **scheduled fetch** of this
URL under *Products > Feeds*.

.. _google/merchant/sync:

Merchant API product sync
=========================

The sync keeps Merchant Center up to date in near real time: changes of the price, the stock, the
content, or the publication of a product are sent as soon as they happen, without waiting for the next
fetch. It sends the items of the :guilabel:`Product Feed` selected above, with the same columns.

#. In Merchant Center, create (or reuse) a **primary API data source** for your products.
#. In the Odoo settings, enable :guilabel:`Merchant API Product Sync`. A reminder is displayed if no
   :guilabel:`Product Feed` is selected.
#. Fill in the data source:

   .. list-table::
      :header-rows: 1
      :widths: 30 70

      * - Field
        - Description
      * - :guilabel:`Data Source`
        - The data source in the form `accounts/123/dataSources/456`. Click :guilabel:`Create Data
          Source` to let Odoo create it (or find the one with the same name).
      * - :guilabel:`Content Language`
        - The two-letter language of the products, for example `es`. Defaults to the language of
          the feed.
      * - :guilabel:`Feed Label`
        - The feed label of the products, for example `ES`. Defaults to the tax country of the
          feed, otherwise the country of the company.

#. Click :guilabel:`Send All Products` for the first synchronization. It also removes from Merchant
   Center the products that were sent earlier and that left the feed (unpublished, archived, or
   excluded by the filter).

The changes are queued as :doc:`server events </applications/websites/website/tracking/server_events>`
(one request per product, merged if the product changes several times in a row) and can be followed
there.

Product statuses
----------------

Every day, Odoo imports the status of the products from Merchant Center. Click :guilabel:`Import
Statuses` to do it immediately; the date is displayed in :guilabel:`Statuses`. The status appears:

- in the :guilabel:`Google Merchant Center` group of the :guilabel:`Marketing` tab of the product
  (with the :guilabel:`Merchant Center Offer ID` and the :guilabel:`Merchant Center Issues`);
- as an optional column :guilabel:`Merchant Center Status` of the product lists.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Status
     - Meaning
   * - :guilabel:`Eligible`
     - The product can be shown.
   * - :guilabel:`Eligible (limited)`
     - The product can be shown with limits.
   * - :guilabel:`Pending`
     - Merchant Center did not finish processing it.
   * - :guilabel:`Not eligible or disapproved`
     - The product cannot be shown: read the issues.

For a product with several variants, the worst status is displayed. Use the filters
:guilabel:`Disapproved in Merchant Center` and :guilabel:`Merchant Center Issues` in the product
list to find the products to fix.

.. screenshot:: google-merchant-product-status
   :menu: Website ‣ eCommerce ‣ Products ‣ (a product) ‣ Marketing
   :shows: The Marketing tab of a product with the Google Merchant Center group at the top: the
      status badge Not eligible or disapproved, the offer ID, and the issues text.
   :highlight: The Google Merchant Center group (red frame).
   :data: A demo product with one issue "Missing value [gtin]".
   :notes: English UI, light theme, 1440px width.

.. _google/merchant/promotions:

Promotions
==========

If *Discount & Loyalty* is installed, the :guilabel:`Promotions` setting appears. It publishes the
**discount codes** of the website as Merchant Center promotions, so that Google shows the offer on your
products.

#. Create a data source for promotions in Merchant Center, enter it in :guilabel:`Data Source`, or
   click :guilabel:`Create Data Source`.
#. Click :guilabel:`Send Promotions`.

Odoo sends the discount code programs that are valid today and give a **percentage** or a **fixed
amount on the whole order**. Programs without an end date are published for 180 days. The other
programs are skipped, and the reason is displayed (for example: no discount code, or a discount that is
not on the whole order).

.. _google/merchant/reviews:

Google Customer Reviews
=======================

*Google Customer Reviews* invites your customers to rate their experience after they received the
order, and displays your seller rating. Enable it in the :guilabel:`Google Customer Reviews` setting
(the :guilabel:`Merchant Center ID` is required) and fill in:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Estimated Delivery (days)`
     - Days between the order and the delivery (`5` by default); Google sends the survey after this
       delay.
   * - :guilabel:`Opt-in Position`
     - Where the survey opt-in is displayed on the order confirmation page: dialog in the center,
       at the bottom right, bottom left, top right, or top left, or a tray at the bottom.
   * - :guilabel:`Store Widget`
     - Displays the seller rating widget on every page.
   * - :guilabel:`Widget Position`
     - :guilabel:`Bottom right` or :guilabel:`Bottom left`.

The opt-in is loaded only when the customer accepted the **marketing** cookies. The valid barcodes
(GTIN) of the ordered products are passed to Google so that it can also collect product reviews.

.. seealso::
   - :doc:`/applications/websites/ecommerce/product_feeds`
   - :doc:`/applications/websites/ecommerce/tracking`
   - :doc:`/applications/websites/website/tracking/troubleshooting`

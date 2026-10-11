============
Meta catalog
============

A **Meta catalog** holds the products that Meta can show in dynamic ads, in the Facebook and Instagram
shops, and in product tags. Odoo fills it from the products of your eCommerce in two ways that work
together:

- a **product feed** that Meta downloads every day;
- **real-time updates** that push the changes of price, stock, content, and publication to the catalog
  in the hours that follow, without waiting for the next download.

The product IDs of the catalog are the same as the ones of the :doc:`pixel events <pixel>`, so Meta can
link what a visitor viewed to the catalog item that it shows in the ad.

Prerequisites
=============

- A catalog in Meta Commerce Manager. Note its **catalog ID**.
- A :doc:`Meta connection <connection>` with the catalog management permission.
- The products are published on the website. Fill in their :doc:`marketing data
  </applications/websites/ecommerce/product_feeds>` (brand, GTIN, and so on).

Set up the catalog
==================

Go to :menuselection:`Meta --> Configuration --> Settings`. In the :guilabel:`Meta Catalog` block,
enable :guilabel:`Catalog Feed`:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Catalog ID`
     - The ID of the catalog in Commerce Manager (digits only).
   * - :guilabel:`Meta Feed`
     - The :doc:`product feed </applications/websites/ecommerce/product_feeds>` of the *Meta catalog*
       channel. Click :guilabel:`Configure Feed`: Odoo creates it for the website if it does not
       exist, and opens it so that you can adjust the columns, the language, the currency, and the
       prices.
   * - :guilabel:`Commerce Manager Feed ID`
     - Filled in by Odoo when the feed is registered. Clear it to register the feed again.

Then click :guilabel:`Register the Feed in Commerce Manager`. Odoo creates the data feed in the
catalog, with a **daily** download of the address of the feed. The first download can take a few
minutes. You can also register the address of the feed by hand in Commerce Manager (*Data sources >
Data feed > Scheduled feed*) and skip this button.

.. screenshot:: meta-settings-catalog
   :menu: Meta ‣ Configuration ‣ Settings
   :shows: The Meta Catalog block of the Meta settings: the Catalog Feed setting enabled with the
      Catalog ID, Meta Feed and Commerce Manager Feed ID fields and the Configure Feed and Register
      the Feed in Commerce Manager buttons, then the Real-time Catalog Updates setting with the Send
      All Products and Catalog Items buttons.
   :highlight: The Catalog ID field and the two buttons (red frame).
   :data: Catalog ID "1234567890123456", feed "Meta catalog - My Website".
   :notes: English UI, light theme, 1440px width, crop to the block.

Real-time updates
=================

The daily download is too slow for a price that changes or a product that sells out. Enable
:guilabel:`Real-time Catalog Updates` to send the changes as soon as they are detected:

- When a product is changed (price, name, description, images, marketing data, publication, and so
  on), the change is queued and sent to the catalog in batches.
- Stock and pricelist changes do not modify the product itself, so Odoo checks them **every hour**:
  it recomputes the data of the items and sends those that changed, including the scheduled price
  rules and the stock movements.
- A product that is unpublished, archived, or deleted is **removed** from the catalog.
- Meta processes the batches asynchronously. Odoo checks the result every hour and flags the items
  that Meta rejected, with the reason.

The data sent is the one of the Meta feed, with the same columns and IDs, so the file and the updates
never contradict each other.

Click :guilabel:`Send All Products` to send the whole feed again (for example after changing the
columns), and :guilabel:`Catalog Items` to open the list of the items:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Status
     - Meaning
   * - :guilabel:`Processing`
     - Sent, waiting for the answer of Meta.
   * - :guilabel:`Up to date`
     - Accepted by Meta.
   * - :guilabel:`Rejected`
     - Refused by Meta. The error tells why (for example a missing image or an invalid price). Fix the
       product, and it is sent again at the next check, or click :guilabel:`Send Again` on the item.
   * - :guilabel:`Removed`
     - Deleted from the catalog.

These requests also appear in the :menuselection:`Meta --> Server Events` list (see
:doc:`/applications/websites/website/tracking/server_events`), where a failed request is retried
automatically.

.. note::
   The catalog updates do not depend on the cookies of the visitors: they contain no personal data.

.. tip::
   Check in Commerce Manager, under *Catalog > Items* and *Diagnostics*, that the products arrive and
   that Meta does not report issues. The events of the pixel should show a high *match rate* of the
   content IDs with the catalog in Events Manager.

.. seealso::
   - :doc:`/applications/websites/ecommerce/product_feeds`
   - :doc:`/applications/websites/ecommerce/tracking`
   - :doc:`connection`

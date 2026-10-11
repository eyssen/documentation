=============
Product feeds
=============

A **product feed** is a file that lists your eCommerce products with their prices, availability,
images, and identifiers. Google Merchant Center, Meta catalogs, and price comparison sites download it
regularly to publish your products in their shopping ads, free listings, and shops.

Odoo generates the feeds from the products of your website, keeps them up to date, and serves them at
a secret address. You can create as many feeds as you need: one per website, language, currency,
pricelist, or sales channel.

.. note::
   The product feeds are installed automatically with the :doc:`Google
   </applications/websites/google/merchant_center>` or :doc:`Meta
   </applications/websites/meta/catalog>` integration of the eCommerce. If the *Stock* management of
   the eCommerce is installed, the stock quantities are added to the feeds as well.

Create a feed
=============

Go to :menuselection:`Website --> eCommerce --> Product Feeds` and click :guilabel:`New`.

#. Enter a :guilabel:`Name` (for example `Google Shopping HU`) and select the :guilabel:`Channel`:

   .. list-table::
      :header-rows: 1
      :widths: 30 70

      * - Channel
        - Use
      * - :guilabel:`Google Merchant Center`
        - The product feed of Google, with all the attributes of Merchant Center.
      * - :guilabel:`Meta catalog`
        - The feed of the Meta (Facebook and Instagram) catalogs.
      * - :guilabel:`Google product reviews`
        - The reviews of your customers, for Google product ratings.
      * - :guilabel:`Custom`
        - A minimal feed for a comparison site or any other destination. You choose the columns.

#. Select the :guilabel:`Website`, and the other fields described below.
#. Click :guilabel:`Load Default Columns` to fill the columns of the channel. This replaces the
   existing columns.
#. Click :guilabel:`Preview` to check the first items, then :guilabel:`Generate Now`.

.. screenshot:: product-feed-form
   :menu: Website ‣ eCommerce ‣ Product Feeds ‣ (a feed)
   :shows: A Google Merchant Center product feed form with the Generate Now, Preview, and Load
      Default Columns buttons, the Products and Output groups (with the Feed URL and its refresh
      button), the Prices group, the Last Generation group, and the Columns tab with the default
      columns.
   :highlight: The Feed URL field and the Generate Now button (red frame).
   :data: Feed "Google Shopping HU", 120 items, 3 warnings.
   :notes: English UI, light theme, 1440px width.

Products
--------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Item Level`
     - :guilabel:`Product variants`: one item per variant, grouped by product. :guilabel:`Products`:
       one item per product.
   * - :guilabel:`Only Published Products`
     - Enabled by default. Only the products published on the website are listed.
   * - Filter (domain)
     - Restricts the products of the feed, for example to one category or brand.
   * - :guilabel:`Out of Stock Products`
     - :guilabel:`List as out of stock` or :guilabel:`Leave out of the feed`.
   * - :guilabel:`Stock Quantity`, :guilabel:`Stock Locations`
     - With the *Stock* management of the eCommerce: the quantity sent in the feed (on hand,
       forecasted, or free to use, which is the default) and the locations that are counted
       (by default the warehouse of the website).

Output and prices
-----------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Language`
     - The language of the texts and links. Defaults to the language of the website.
   * - :guilabel:`Format`
     - :guilabel:`CSV`, :guilabel:`TSV (tab separated)`, :guilabel:`XML (RSS 2.0)` (default), or
       :guilabel:`XML (Atom 1.0)`. Use the format that the destination accepts. For a CSV, choose the
       :guilabel:`CSV Separator`.
   * - :guilabel:`Gzip Compression`
     - Compresses the file.
   * - :guilabel:`Image Size`
     - :guilabel:`1920 px`, :guilabel:`1024 px` (default) or :guilabel:`512 px`.
   * - :guilabel:`Refresh Every (hours)`
     - The file is regenerated when it is older than this. 6 hours by default. `0`: only when you
       click :guilabel:`Generate Now`.
   * - :guilabel:`Pricelist`
     - The prices of the feed. Defaults to the pricelist of the website, with its discounts.
   * - :guilabel:`Prices`
     - :guilabel:`Tax included` (default) or :guilabel:`Tax excluded`. Most countries expect prices
       with taxes; use tax excluded in the US and Canada.
   * - :guilabel:`Tax Country`
     - The taxes are mapped with the fiscal position applied to the customers of this country.

.. _ecommerce/feeds/url:

Feed URL
--------

The :guilabel:`Feed URL` is the address that the destination downloads. It contains a **secret key**:
whoever knows the address can read the feed, but nobody can guess it. Click the refresh button next to
it to generate a new secret address if it leaked: the old address stops working immediately, and you
have to give the new one to the destinations.

The file is cached. It is regenerated by a scheduled action (every hour for the feeds that are due), and
when the destination fetches a file that is too old. The last generation date, the number of items,
the generation time, and the number of warnings are displayed in the :guilabel:`Last Generation` group.

Columns
=======

The :guilabel:`Columns` tab lists the attributes written in the file, and where their value comes
from. The default columns of each channel contain all the main attributes of Merchant Center and of the
Meta catalog: identifier, title, description, link, images, availability, price and sale price, brand,
GTIN, MPN, condition, Google product category, product type, color, size, gender, age group, material,
pattern, shipping, custom labels, and so on.

You can add, remove, or reorder the columns, and change for each one:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Name`
     - The name of the attribute in the file.
   * - :guilabel:`Value`
     - :guilabel:`Standard value` (computed by Odoo), :guilabel:`Product field` (any field of the
       product, for example `categ_id.name`), :guilabel:`Fixed text`, :guilabel:`Product attribute`
       (a variant attribute), or :guilabel:`Mapped value` (a value replaced according to a table).
   * - :guilabel:`Prefix`, :guilabel:`Suffix`
     - Text added before or after the value.
   * - :guilabel:`Max. Length`, :guilabel:`Strip HTML`
     - Truncates the value and removes the HTML markup of the descriptions.
   * - :guilabel:`Default Value`
     - Used when the product has no value.
   * - :guilabel:`Required`
     - The items without a value are **left out** of the feed and reported as warnings.

.. important::
   Do not change the standard value of the item identifier column. It uses the :ref:`product
   identifier <ecommerce/tracking/identifier>` of the eCommerce tracking, so that the items of the
   feed and the events of the website have the same ID.

Shipping
--------

In the :guilabel:`Shipping` tab, add one line per destination (country, region or postal code), with
the service, the price, and the handling and transit times. They are added to the items.

Attribute mapping
-----------------

In the :guilabel:`Attribute Mapping` tab, select the variant attributes of your products that provide
the color, size, material, pattern, gender, and age group, when the product has no value of its own in
its :guilabel:`Marketing` tab.

Warnings
--------

After each generation, the feed lists the problems in the :guilabel:`Warnings` tab: a barcode that is
not a valid GTIN (it is left out), a required value that is missing (the product is left out), and so
on. Fix them on the products and generate the feed again. The number of warnings is displayed in the
list of feeds. Merchant Center and the Meta catalog report their own checks as well.

Marketing data of the products
==============================

Open a product and go to the :guilabel:`Marketing` tab. These fields enrich the items; fill in at least
the brand and the identifiers.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Group
     - Fields
   * - :guilabel:`Identifiers`
     - :guilabel:`Brand`, :guilabel:`MPN`, :guilabel:`Has Unique Identifiers` (uncheck it for custom-made
       or vintage products without GTIN or MPN), :guilabel:`Condition`. The GTIN is the
       :guilabel:`Barcode` of the product; its check digit is verified.
   * - :guilabel:`Category`
     - :guilabel:`Google Product Category`, :guilabel:`Facebook Product Category`,
       :guilabel:`Adult`, :guilabel:`Multipack`, :guilabel:`Bundle`.
   * - :guilabel:`Apparel`
     - :guilabel:`Gender`, :guilabel:`Age Group`, :guilabel:`Color`, :guilabel:`Size`, size type and
       system, :guilabel:`Material`, :guilabel:`Pattern`.
   * - :guilabel:`Energy and Unit Price`
     - Energy efficiency classes, :guilabel:`Unit Pricing Measure` (for example `750 ml`) and
       :guilabel:`Unit Pricing Base Measure` (for example `100 ml`).
   * - :guilabel:`Availability`
     - :guilabel:`Feed Availability`: :guilabel:`Automatic` (default), :guilabel:`In stock`,
       :guilabel:`Out of stock`, :guilabel:`Preorder`, or :guilabel:`Backorder`, with the
       availability date, and the :guilabel:`Feed Expiration Date`.
   * - :guilabel:`Shipping`
     - Shipping label, package dimensions, country the product ships from, handling days, and transit
       time label.
   * - :guilabel:`Ads`
     - Five custom labels, the included and excluded destinations, :guilabel:`Pause Ads`, and the
       :guilabel:`Ads Redirect URL`.
   * - :guilabel:`Highlights`, :guilabel:`Product Details`
     - One highlight per line (ten at most), and the detail lines (section, attribute, value).

The :guilabel:`Marketing` section of a product variant overrides the MPN, color, size, material, and
pattern of the product for this variant.

With the *Stock* management, :guilabel:`Automatic` availability means *in stock* if the product is
available, and *out of stock* if a stored product has no stock and cannot be ordered when out of
stock.

Reference data
==============

The following lists are in :menuselection:`Website --> eCommerce --> Configuration`:

- :guilabel:`Brands`: the brands that you select on the products.
- :guilabel:`Google Product Categories`: the Google taxonomy. Click :guilabel:`Import` to download it
  from Google (in English, and in Hungarian, Spanish, and Romanian when these languages are installed)
  or to import a file. You can set a Google product category on an eCommerce category: the products of
  the category inherit it.
- :guilabel:`Feed Destinations`: the Google destinations (shopping ads, display ads, free listings,
  local inventory ads, and so on) that you can include or exclude on a product.

.. screenshot:: product-marketing-tab
   :menu: Website ‣ eCommerce ‣ Products ‣ (a product) ‣ Marketing
   :shows: The Marketing tab of a product with the groups Identifiers, Category, Apparel, Energy
      and Unit Price, Availability, Shipping, Ads, and Highlights, and the Product Details lines.
   :highlight: The Brand, MPN, and Google Product Category fields (red frame).
   :data: A clothing product with a brand, a GTIN barcode, and a Google category.
   :notes: English UI, light theme, 1440px width.

Connect a feed to a platform
============================

- **Google Merchant Center**: see :doc:`/applications/websites/google/merchant_center`.
- **Meta catalog**: see :doc:`/applications/websites/meta/catalog`.
- **A comparison site**: create a :guilabel:`Custom` feed, choose the format that the site expects,
  and give it the :guilabel:`Feed URL`.

.. seealso::
   - :doc:`tracking`
   - :doc:`/applications/websites/google/merchant_center`
   - :doc:`/applications/websites/meta/catalog`

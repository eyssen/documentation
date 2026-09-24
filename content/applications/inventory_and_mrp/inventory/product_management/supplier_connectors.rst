===========================
Supplier catalog connectors
===========================

The supplier catalog connectors import the product catalog, the purchase prices, and the stock
levels of a wholesaler into Odoo, and keep them up to date automatically. They are plug-ins of the
:doc:`Supplier Product Management (SPM) <supplier_products>` module: every connector feeds the same
supplier stock, vendor lines, and order warnings described on that page.

.. list-table::
   :header-rows: 1
   :widths: 22 28 50

   * - Connector
     - Module
     - Source
   * - :guilabel:`Hurtel`
     - `spm_hurtel_api`
     - Two XML feeds (IdoSell IOF format): a *full* feed with the master data, and a *light* feed
       with the stock levels
   * - :guilabel:`Partner Telekom`
     - `spm_partner_telekom_api`
     - One XML feed, downloaded from a URL or read from a local file
   * - :guilabel:`DRO`
     - `spm_dro_api`
     - One combined XML feed (master data, prices, and stock), fetched from an FTP/FTPS server or read
       from a local file
   * - :guilabel:`Thomax`
     - `spm_thomax_api`
     - Two CSV feeds: a master/price feed and a stock feed
   * - :guilabel:`Vision Software`
     - `spm_vision_software_api`
     - The SOAP web service of the supplier's *Vision Software (Octopus)* ERP

.. note::
   - Install the connectors from the :doc:`Apps <../../../general/apps_modules>` dashboard. They
     require the *Purchase*, *Inventory*, and *eCommerce* apps.
   - Each connector adds its own menu under :menuselection:`Purchase --> SPM`. Purchase users can
     consult the data; only users with the :guilabel:`Purchase: Administrator` access right can
     configure the connectors and launch synchronizations.
   - A feed or an API access is granted by the supplier. Ask the supplier for the address of the
     feed and the credentials before configuring a connector.

.. _supplier-connectors/principle:

How a synchronization works
===========================

All connectors work in the same way, in up to three stages:

#. **Stage 1 – staging.** The feed is downloaded and copied, as is, into staging tables
   (:menuselection:`Purchase --> SPM --> (connector) --> Products (Staging)`). Nothing is changed on
   the products at this point. A staging product is :guilabel:`Present`, :guilabel:`Vanished` (it
   disappeared from the feed), or in :guilabel:`Error`.
#. **Stage 2 – products.** The staging products are turned into Odoo products:

   - a staging product that was imported before is matched with its product through the supplier's
     identifier, and the product is **updated**;
   - otherwise, if the feed contains a valid :ref:`GTIN barcode <supplier-connectors/barcode>` that
     already exists on a product imported by **another** connector, that product is reused: the
     connector only adds its own vendor line and supplier stock to it, without changing its name,
     price, or category. The same article sold by several wholesalers is therefore a single product
     with several vendors;
   - otherwise, a new storable product is **created**, available for sales and purchases.

#. **Stage 3 – images.** The pictures referenced by the feed are downloaded in the background, by
   small batches, into the main image and the extra images of the product.

The following data is maintained on the products by stage 2:

- the :guilabel:`Internal Reference`, the :guilabel:`Barcode` or the :guilabel:`Manufacturer Part
  Number`, the weight (when provided), the eCommerce description, the :guilabel:`Sales Price`, and
  the :guilabel:`Cost`;
- the eCommerce category, according to the :ref:`category mapping
  <supplier-connectors/categories>`;
- the brand and the other attributes provided by the feed, as attributes that do not create
  variants;
- the **vendor line** of the supplier (:guilabel:`Purchase` tab), with the supplier's product code
  and the :guilabel:`Supplier Lead Time (days)` of the connector;
- the **supplier stock** at the :guilabel:`Default Supplier Location` of the connector.

.. important::
   Only the fields listed above are overwritten at each synchronization. Any other field of the
   product, including its **name** after the creation, its product category, and its sales
   description, can be modified manually without being reverted. A price of zero coming from the
   feed never overwrites an existing price.

Products that vanish from the feed are **not** archived automatically: their supplier stock is
removed at the next full synchronization, and the product itself is left to the user. They can be
archived in bulk with the :ref:`Full Upgrade Wizard <supplier-connectors/full-upgrade>`.

.. _supplier-connectors/settings:

Configure a connector
=====================

Go to :menuselection:`Purchase --> SPM --> (connector) --> Settings`, and click :guilabel:`New`.
Several settings records can exist for one connector, e.g., one per company.

Base settings
-------------

- :guilabel:`Supplier`: the contact of the wholesaler. It is used on the vendor lines.
- :guilabel:`Default Supplier Location`: the :doc:`supplier location <supplier_products>` that
  receives the supplier stock. It is required: without it, no supplier stock is recorded.
- :guilabel:`Company`.
- :guilabel:`Category Review User`: the user who gets an activity each time the synchronization
  discovers a new category in the feed. Leave empty to disable these activities.
- :guilabel:`Sync Lock Timeout (hours)`: a running synchronization locks the connector, so that two
  runs never overlap. After this delay, a lock left behind by an interrupted run is released
  automatically.

Pricing
-------

The :guilabel:`Pricing` tab defines how the sales price is derived from the supplier's price:

- :guilabel:`Cost Currency`: the currency of the prices of the feed;
- :guilabel:`List Currency`: the currency of the sales prices, usually the company currency. The
  supplier's price is converted with the exchange rate of the day of the synchronization;
- :guilabel:`Pricing Tiers`: the markup rules, by price band. Each tier has an :guilabel:`Up To`
  limit (exclusive, in list currency), a :guilabel:`Markup Type` (:guilabel:`Fixed amount` or
  :guilabel:`Percent`), and a :guilabel:`Markup Value` (e.g., `45` for +45%). The tiers are evaluated
  in ascending order of their limit, and the first tier whose limit is higher than the converted
  price applies. Use `0` as limit on exactly one tier to mark the open-ended top band. No tier is
  delivered with the modules;
- :guilabel:`Price Rounding Strategy`: :guilabel:`No rounding`, or :guilabel:`Ceil to next X90`,
  which rounds the marked-up price up to the next amount ending in 90 (e.g., 1,181 → 1,190;
  1,191 → 1,290);
- :guilabel:`Require Pricing Tier`: when enabled, a product whose price matches no tier is reported
  as an error instead of being sold at its cost;
- :guilabel:`Supplier Lead Time (days)`: written on the vendor line of every product of the
  connector. Changing it here updates all the vendor lines at the next synchronization;
- *Készlettel rendelkező termékek létrehozása* (create products that are in stock only): when
  enabled, new products are only created for articles that the supplier has in stock. The stock of
  the existing products is always updated, including when it drops to zero.

The :guilabel:`Cost` of the product is the converted supplier price, without markup or rounding.

.. example::
   With the tiers *up to 5,000: fixed 1,500*, *up to 50,000: 35%*, and *0 (open-ended): 20%*, and
   the :guilabel:`Ceil to next X90` rounding, a product bought for the equivalent of 12,000 gets
   a sales price of 12,000 × 1.35 = 16,200 → **16,290**.

.. screenshot:: inventory-supplier-connectors-pricing
   :menu: Purchase ‣ SPM ‣ Hurtel ‣ Settings ‣ (a settings record) ‣ Pricing tab
   :shows: The Pricing tab of a connector with the currencies (EUR → HUF), the rounding strategy "Ceil to next X90", the procurement options, and three pricing tiers.
   :highlight: The "Pricing Tiers" list (red frame).
   :data: Tiers: up to 5,000 fixed 1,500; up to 50,000 percent 35; 0 percent 20.
   :module: spm_hurtel_api
   :notes: English UI, light theme, 1440px width.

Source and schedule
-------------------

The source of the data, and the frequency of the automatic synchronization, are set in the tab(s)
specific to each connector (see :ref:`supplier-connectors/specifics`). In all connectors:

- a **source** is a URL, a file on the server, or an API address, with its credentials. For the feeds
  downloaded over HTTP, the :guilabel:`Authentication` tab supports :guilabel:`No Auth`,
  :guilabel:`HTTP Basic`, :guilabel:`URL Query Parameter`, and :guilabel:`Custom HTTP Header`, plus
  optional :guilabel:`Extra Headers (JSON)`;
- the automatic synchronization is **disabled by default**. Tick the *Cron Active* checkbox of the
  feed, and set the interval (and, where available, the hour and minute of the day). The
  :guilabel:`Open Cron Record` button opens the corresponding scheduled action;
- the download of the images has its own switch in the :guilabel:`Image Download` tab:
  :guilabel:`Image Download Cron Active`, with the :guilabel:`Image Download Batch Size` (number of
  products per run, every 15 minutes). The :guilabel:`Pending Images` and :guilabel:`Failed Images`
  counters show the progress. An image is tried up to five times.

.. _supplier-connectors/run:

Run a synchronization manually
==============================

The header of the settings form contains the manual actions:

- :guilabel:`Sync Now` (or :guilabel:`Sync Full Now` / :guilabel:`Sync Light Now` for Hurtel,
  :guilabel:`Sync Master` / :guilabel:`Sync Stock` for Thomax): queues a complete run, which starts
  within about a minute in the background;
- :guilabel:`Sync to Products`: runs stage 2 only, on the data already in staging, e.g., after
  correcting the pricing tiers or the category mapping;
- :guilabel:`Stock Only` (Hurtel): refreshes the supplier stock only;
- :guilabel:`Full Upgrade Wizard`: see :ref:`below <supplier-connectors/full-upgrade>`;
- :guilabel:`Force Unlock`: releases the lock of a synchronization that was interrupted. It is
  reserved for users with the :guilabel:`Administration: Settings` access right; use it only when
  no synchronization is actually running.

While a run is in progress, the :guilabel:`Sync in Progress` toggle is on, and the form shows which
feed is being processed and until when the lock is held.

.. _supplier-connectors/log:

Import log
----------

Every run, manual or scheduled, creates an entry in :menuselection:`Purchase --> SPM --> (connector)
--> Import Log`, with its feed, its trigger (:guilabel:`Cron` or :guilabel:`Manual`), its status,
its duration, and detailed counters: staging products created, updated, skipped because unchanged,
and failed; products created, updated, and failed in stage 2; supplier stock lines created, updated,
and archived; etc. The errors of individual products are listed in the lines of the log.

.. screenshot:: inventory-supplier-connectors-import-log
   :menu: Purchase ‣ SPM ‣ Hurtel ‣ Import Log ‣ (a finished full run)
   :shows: An import log form of a full synchronization with its status, start and end time, duration, and the counters of stage 1 and stage 2.
   :highlight: The status and the stage 2 counters (red frames).
   :data: A successful full run with a few thousand products, 12 created, 340 updated, 2 failed.
   :module: spm_hurtel_api
   :notes: English UI, light theme, 1440px width.

.. _supplier-connectors/categories:

Category mapping
================

The categories of the feed are listed in :menuselection:`Purchase --> SPM --> (connector) -->
Categories`. The first time a category is met, an eCommerce category with the same name (and, for
hierarchical feeds, the same parents) is created automatically, and the products of the category
are published in it.

To place the products of a feed category in an eCommerce category of your own instead, open the
feed category and select it in :guilabel:`Manual Mapping`. The :guilabel:`Webshop Category` field
shows the category actually in use, and the :guilabel:`Mapping Status` whether it is a
:guilabel:`Manual override`, :guilabel:`Auto-created`, or missing (:guilabel:`No webshop category`).
The new mapping is applied to the products at the next stage 2. The eCommerce categories added
manually to a product are left untouched.

Use the :guilabel:`Awaiting Review`, :guilabel:`Auto-mapped`, :guilabel:`Manual Override`, and
:guilabel:`No Webshop Category` filters to work through the new categories. If a
:guilabel:`Category Review User` is set on the connector, this user gets an activity for every
new category.

.. note::
   The Vision Software connector maps the supplier's product groups through the :guilabel:`VS API
   Name` field of the eCommerce categories and of the attribute values, and assigns the
   :guilabel:`Product Category` and the :guilabel:`Brand Attribute` selected in its settings.

.. _supplier-connectors/full-upgrade:

Full Upgrade Wizard
===================

A normal synchronization protects what was changed manually, and skips the articles that did not
change in the feed. The :guilabel:`Full Upgrade Wizard` (Hurtel, Partner Telekom, DRO, and Vision
Software) forces the refresh of selected components on the existing products, e.g., after a change
of the pricing tiers, or to reset the names to those of the supplier.

Click :guilabel:`Full Upgrade Wizard` on the settings form, and tick the components to refresh:

- :guilabel:`Identity`: :guilabel:`Name`, :guilabel:`Description`, :guilabel:`Default Code (SKU)`,
  :guilabel:`Barcode (EAN)`;
- :guilabel:`Classification`: :guilabel:`Webshop Categories`, and, for Hurtel, :guilabel:`Brand
  Attribute` and :guilabel:`Other Attributes (Parameters)`;
- :guilabel:`Commerce`: :guilabel:`List Price`, :guilabel:`Standard Price (Cost)`;
- :guilabel:`Stock`: :guilabel:`Supplier Quants (Stock)`, :guilabel:`Supplier Info`;
- :guilabel:`Media`: :guilabel:`Images`;
- :guilabel:`Lifecycle`: :guilabel:`Create New Products`, :guilabel:`Archive Vanished Products`.

The :guilabel:`Full Refresh`, :guilabel:`Stock + Price`, and :guilabel:`Names + Descriptions`
buttons tick a predefined set, and :guilabel:`Reset` clears the selection. Then, choose the
:guilabel:`Scope`: all the products of the connector, only the articles changed in the feed since
the :guilabel:`Changed Since` date, or, for Hurtel, a :guilabel:`Specific Brand only`. Click
:guilabel:`Run Upgrade`: the upgrade runs in the background, and its import log opens to follow the
progress.

.. warning::
   Refreshing the :guilabel:`Name`, the :guilabel:`Description`, or the prices overwrites the manual
   corrections made on the products of the chosen scope. :guilabel:`Archive Vanished Products`
   archives every product that is no longer in the feed.

.. screenshot:: inventory-supplier-connectors-full-upgrade
   :menu: Purchase ‣ SPM ‣ Hurtel ‣ Settings ‣ (a settings record) ‣ Full Upgrade Wizard
   :shows: The Full Upgrade Wizard with the four preset buttons, the six groups of component checkboxes ("Stock + Price" preset ticked), the Scope radio buttons and the Run Upgrade button.
   :highlight: The preset buttons and the "Scope" field (red frames).
   :module: spm_hurtel_api
   :notes: English UI, light theme, crop to the dialog.

.. _supplier-connectors/barcode:

Barcodes
========

A code of the feed is only written in the :guilabel:`Barcode` field of the product, and only used
to recognize a product already imported from another wholesaler, when it is a valid GTIN. Any other
code is stored as :guilabel:`Manufacturer Part Number`. See :doc:`supplier_products`.

.. _supplier-connectors/specifics:

Connector specifics
===================

Hurtel
------

- :guilabel:`Full Feed` tab: the source of the full XML feed, synchronized weekly by default. The
  full run updates the master data, the prices, and the stock, and flags the vanished articles.
- :guilabel:`Light Feed` tab: the source of the light feed, synchronized daily by default. The light
  run only refreshes the supplier stock of the existing products; new articles wait for the next
  full run.
- :guilabel:`Warehouse Stock ID`: which stock of the feed is imported: `0` for the aggregated total,
  `1` (default) for the supplier's main warehouse, `2` and above for secondary warehouses.
- :guilabel:`Default Language` and :guilabel:`Translation Languages`: the language of the feed used
  for the name and the description of the products, and the additional languages for which the
  translations are imported. The languages must be installed in the database and present in the
  feed.
- :guilabel:`Auto-run Stage 2 after Stage 1`: untick it to stop after the staging, review the new
  categories and attributes, and then click :guilabel:`Sync to Products (Full)` manually.

Partner Telekom
---------------

- :guilabel:`Feed` tab: :guilabel:`Source Type` (:guilabel:`URL` or :guilabel:`Local File`),
  :guilabel:`Source Path`, and the schedule, daily by default.

DRO
---

- :guilabel:`Feed` tab: :guilabel:`Source Type` :guilabel:`FTP` (default) or :guilabel:`Local
  File`, the :guilabel:`Source Path` of the file, and the :guilabel:`FTP Connection`:
  :guilabel:`FTP Host`, :guilabel:`FTP Port`, :guilabel:`FTP User`, :guilabel:`FTP Password`, and
  :guilabel:`Use FTPS (TLS)`, enabled by default.
- The feed does not detail the stock per warehouse: all the supplier stock goes to the
  :guilabel:`Default Supplier Location`.

Thomax
------

- :guilabel:`Feeds` tab: the :guilabel:`Master / Price Feed` (:guilabel:`Master Source Path`,
  :guilabel:`Master Encoding`, UTF-8 by default; daily by default) and the :guilabel:`Stock Feed`
  (:guilabel:`Stock Source Path`, :guilabel:`Stock Encoding`, `cp1250` by default; every two hours
  by default), with a common :guilabel:`CSV Delimiter` (`;`). Each feed has its own :guilabel:`Sync
  Master` / :guilabel:`Sync Stock` button and schedule.
- :guilabel:`Verify SSL Certificate`: keep it enabled, unless the supplier's server presents an
  incomplete certificate chain that makes the download fail, and you accept the reduced security.
- The technical attributes of the master feed are imported as product attributes.
- This connector has no Full Upgrade Wizard.

Vision Software
---------------

- :guilabel:`Authentication` tab: the :guilabel:`API URL` of the supplier's web service, and the
  :guilabel:`API Key (authcode)`.
- :guilabel:`Sync & Endpoints` tab: the schedule (every 12 hours by default), and one switch per
  service of the API. Only the product list (:guilabel:`Enable Cikklista (GetCikkekAuth)`) and
  stage 2 (:guilabel:`Enable Stage 2 (staging -> products)`) are enabled by default; the product groups, barcodes, price list,
  price changes, stock, stock changes, invoices, attribute values, images, and sales prices per
  payment class can be enabled one by one. The supplier limits the number of calls per day of each
  service; the limit is indicated in the tooltip of each switch, and the time of the last call is
  displayed in :guilabel:`Last Call Per Endpoint`.
- :guilabel:`Vision Partner ID (PID)` or :guilabel:`Vision Partner Code`: your customer identifier
  at the supplier, required by the price services.
- The product list is requested incrementally: only the articles changed since the last successful
  call, minus a safety margin of :guilabel:`GetCikkek Changed-Since Margin (days)`.
- The raw answers of the optional services can be consulted under :menuselection:`Purchase --> SPM
  --> Vision Software --> Cache` (prices, stock, barcodes, images, invoices, product groups, and
  attribute values). Some of these menus and field labels are displayed in Hungarian, the language
  of the supplier's API.
- The serial number management of the supplier's articles is taken over as the tracking of the
  product (no tracking, by lots, or by unique serial number).

.. seealso::
   - :doc:`supplier_products`
   - :doc:`../../../websites/ecommerce/products`

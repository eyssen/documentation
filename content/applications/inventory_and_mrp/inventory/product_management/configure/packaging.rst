=========
Packaging
=========

.. |adjust| replace:: :icon:`oi-settings-adjust` :guilabel:`(additional options)`

In Odoo *Inventory*, *packaging* refers to disposable containers holding multiple units of a
specific product.

For example, different packages for cans of soda, such as a 6-pack, a 12-pack, or a case of 36,
**must** be configured on the individual product form. This is because packagings are product
specific, not generic.

.. note::
   A barcode can be stored on each packaging line, but scanning that barcode does **not** add the
   contained number of units to the product count automatically. Barcode-driven receipts record
   quantities in the product's own unit of measure; see :doc:`../../../barcode`.

Configuration
=============

To use packagings, navigate to :menuselection:`Inventory app --> Configuration --> Settings`. Then,
under the :guilabel:`Products` heading, enable the :guilabel:`Product Packagings` feature, and click
:guilabel:`Save`.

.. screenshot:: inventory-packaging-enable
   :menu: Inventory ‣ Configuration ‣ Settings
   :shows: The Inventory settings page scrolled to the "Products" section with the "Product Packagings"
      checkbox enabled.
   :highlight: The "Product Packagings" checkbox (red frame).
   :data: Demo company "YourCompany".
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the "Products" settings block.

.. _inventory/product_management/packaging-setup:

Create packaging
================

Packagings can be created directly on the product form, or from the :guilabel:`Product Packagings`
page.

From product form
-----------------

Create packagings on a product form by going to :menuselection:`Inventory app --> Products -->
Products`, and select the desired product.

Under the :guilabel:`Inventory` tab, scroll down to the :guilabel:`Packaging` section, and click
:guilabel:`Add a line`. In the table, fill out the following fields:

- :guilabel:`Packaging` (required): name of packaging that appears on sales/purchase orders as a
  packaging option for the product.
- :guilabel:`Contained quantity` (required): amount of product in the packaging.
- :guilabel:`Unit of Measure` (required): measurement unit for quantifying the product.
- :guilabel:`Sales`: check this option for packagings intended for use on sales orders.
- :guilabel:`Purchase`: check this option for packagings intended for use on purchase orders.

.. note::
   Access additional fields in the :guilabel:`Packaging` table below by clicking the |adjust| icon
   to the far-right of the column titles in the :guilabel:`Packaging` section, and selecting the
   desired options from the drop-down menu that appears.

- :guilabel:`Barcode`: identifier used to trace the packaging in stock moves and pickings. Leave
  blank if not in use.
- :guilabel:`Company`: indicates the packaging is only available at the selected company. Leave
  blank to make the packaging available across all companies.

.. example::
   To create a packaging type for six units of the product, `Grape Soda`, begin by clicking
   :guilabel:`Add a line`. In the line, name the :guilabel:`Packaging` `6-pack`, and set the
   :guilabel:`Contained quantity` to `6`. Repeat this process for additional packagings.

   .. screenshot:: inventory-packaging-create-on-product
      :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ Inventory tab
      :shows: The "Packaging" section of a product form with one line: Packaging "6-pack", Contained
         quantity 6, Unit of Measure "Units", with the Sales and Purchase checkboxes visible.
      :highlight: The new "6-pack" line (red frame).
      :data: Product "Grape Soda", unit of measure "Units".
      :module: stock, product
      :notes: English UI, light theme, 1440px width, crop to the Packaging table.

From product packagings page
----------------------------

To view all packagings that have been created, go to :menuselection:`Inventory app --> Configuration
--> Product Packagings`. Doing so reveals the :guilabel:`Product Packagings` page with a complete
list of all packagings that have been created for all products. Create new packagings by clicking
:guilabel:`New`.

.. example::
   Two soda products, `Grape Soda` and `Diet Coke`, have three types of packagings configured. On
   the :guilabel:`Product Packagings` page, each product can be sold as a `6-Pack` that contains 6
   products, as a `12-Pack` of 12 products, or as a `Case` of 32 products.

   .. screenshot:: inventory-packaging-list
      :menu: Inventory ‣ Configuration ‣ Product Packagings
      :shows: The "Product Packagings" list with several packagings across products — for two soda products,
         a "6-Pack" of 6, a "12-Pack" of 12 and a "Case" of 32.
      :highlight: None.
      :data: Products "Grape Soda" and "Diet Coke", three packagings each.
      :module: stock, product
      :notes: English UI, light theme, 1440px width, full list view.

Partial reservation
-------------------

After :ref:`completing the packaging setup <inventory/product_management/packaging-setup>`,
packagings can be reserved in full or partial quantities for outgoing shipments. Partial packaging
flexibility expedites order fulfillment by allowing the immediate shipment of available items, while
awaiting the rest.

To configure packaging reservation methods, go to :menuselection:`Inventory app --> Configuration
--> Product Categories`. Then, click :guilabel:`New`, or select the desired product category.

On the product category's form, in the :guilabel:`Logistics` section, :guilabel:`Reserve Packagings`
can be set to :guilabel:`Reserve Only Full Packagings` or :guilabel:`Reserve Partial Packagings`.

.. important::
   To see the :guilabel:`Reserve Packaging` field, the :guilabel:`Product Packaging` feature
   **must** be enabled. To enable this feature, go to :menuselection:`Inventory app -->
   Configuration --> Settings`, scroll to the :guilabel:`Products` section, tick the
   :guilabel:`Product Packagings` checkbox, and click :guilabel:`Save`.

.. screenshot:: inventory-packaging-reserve
   :menu: Inventory ‣ Configuration ‣ Product Categories ‣ (a category)
   :shows: A product category form, "Logistics" section, with the "Reserve Packagings" field and its two
      options "Reserve Only Full Packagings" and "Reserve Partial Packagings".
   :highlight: The "Reserve Packagings" field (red frame).
   :data: Product category "All / Saleable".
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the Logistics section. The field only appears when
      "Product Packagings" is enabled.

.. example::
   To better evaluate the options based on business needs, consider the following example:

   - a product is sold in twelve units per packaging.
   - an order demands two packagings.
   - there are only twenty-two units in stock.

   When :guilabel:`Reserve Only Full Packagings` is selected, only twelve units are reserved for the
   order.

   Conversely, when :guilabel:`Reserve Partial Packagings` is selected, twenty-two units are
   reserved for the order.

Apply packagings
================

When creating a sales order in the :menuselection:`Sales` app, specify the packagings that should be
used for the product. The chosen packaging is displayed on the :abbr:`SO (Sales Order)` under the
:guilabel:`Packaging` field.

.. example::
   18 cans of the product, `Grape Soda`, is packed using three 6-pack packagings.

   .. screenshot:: inventory-packaging-on-sales-order
      :menu: Sales ‣ Orders ‣ Orders ‣ (a quotation)
      :shows: A sales order line with Quantity 18 and the "Packaging" field set to "6-pack", i.e. three
         packagings of six.
      :highlight: The "Packaging" cell on the order line (red frame).
      :data: Customer "Deco Addict"; one line for 18 units of "Grape Soda".
      :module: sale, stock
      :notes: English UI, light theme, 1440px width, crop to the order lines.

.. _inventory/product_management/packaging-route:

Routes for packaging
====================

When receiving packagings, by default, they follow the warehouse's :doc:`configured reception route
<../../shipping_receiving/daily_operations>`. To **optionally** set up a packaging-specific route,
go to :menuselection:`Inventory app --> Configuration --> Routes`.

.. important::
   The *Product Packagings*, *Storage Locations*, and *Multi-Step Routes* features (found by going
   to :menuselection:`Inventory app --> Configuration --> Settings`) **must** be activated, and
   saved.

.. seealso::
   :doc:`../../shipping_receiving/daily_operations/use_routes`

Create route
------------

On the :guilabel:`Routes` page, click :guilabel:`New`, or select a route that is **not** for a
warehouse. Next, in the :guilabel:`Applicable on` section, tick the :guilabel:`Packagings` checkbox.

.. screenshot:: inventory-packaging-route-form
   :menu: Inventory ‣ Configuration ‣ Routes ‣ New
   :shows: A route form with the "Applicable on" section showing the "Packagings" checkbox ticked while
      "Products" and "Warehouses" are not ticked.
   :highlight: The "Packagings" checkbox (red frame).
   :data: A new route named "Packaging reception".
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the "Applicable on" section. Caption to convey:
      route with Packagings selected, Products and Warehouses not selected.

.. _inventory/product_management/route-on-packaging:

Apply route on packaging
------------------------

Then, to apply the route, go to :menuselection:`Inventory app --> Products --> Products`, and select
the product that uses packaging.

In the product form, switch to the :guilabel:`Inventory` tab. In the :guilabel:`Packaging` section
that contains :ref:`configured packagings <inventory/product_management/packaging-setup>`, click the
|adjust| icon. Tick the :guilabel:`Routes` checkbox to make the column visible in the
:guilabel:`Packaging` table.

In the :guilabel:`Routes` field, select the packaging-specific route. Repeat these steps for all
packaging intended to use the route.

.. screenshot:: inventory-packaging-apply-route
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ Inventory tab
   :shows: The "Packaging" table on a product form with the optional "Routes" column made visible and a
      packaging-specific route selected on the packaging line.
   :highlight: The "Routes" cell on the packaging line (red frame).
   :data: Product "Grape Soda", packaging "6-pack", route "Packaging reception".
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the Packaging table. Requires Product Packagings,
      Storage Locations and Multi-Step Routes to be enabled.


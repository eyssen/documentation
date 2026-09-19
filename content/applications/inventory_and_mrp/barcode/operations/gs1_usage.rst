=================
GS1 barcode usage
=================

.. _barcode/operations/gs1_usage:

.. |AI| replace:: :abbr:`A.I. (Application Identifier)`
.. |GTIN| replace:: :abbr:`GTIN (Global Trade Item Number)`

GS1 barcodes provide a standardized format that barcode scanners can interpret. They encode
information in a :ref:`specific structure recognized globally <barcode/operations/gs1>`, allowing
scanners to understand and process supply chain data consistently.

The following sections contain examples of how GS1 barcodes provided by the business identify
common warehouse items.

.. important::
   Odoo **does not** create GS1 barcodes. Businesses must purchase a unique Global Trade Item Number
   (GTIN) from GS1. Then, they can combine their existing GS1 barcodes with product and supply chain
   information (also provided by GS1) to create barcodes in Odoo.

.. important::
   In this database, the barcode-scan fields used on receipts, deliveries, transfers, and orders
   (see :doc:`receipts_deliveries`, :doc:`inventory_adjustment`, and :doc:`scan_on_orders`) only
   match a scanned code against a single product's :guilabel:`Barcode` field. They do **not** split
   a composite GS1-128 barcode that packs several application identifiers into one scan (for
   example a product |GTIN| followed by a quantity and a lot number in a single code). Use a plain
   |GTIN| as the product's barcode as described below, and enter quantities and lot numbers
   separately on the transfer.

.. seealso::
   - `Purchase GTINs <https://www.gs1.org/standards/get-barcodes>`_
   - :ref:`GS1 nomenclature <barcode/operations/gs1>`

.. _barcode/operations/gs1-lots:

Configure barcodes for product, quantity, and lots
==================================================

To build a GS1 barcode that contains information about a product, its quantities, and the lot
number, the following barcode patterns and Application Identifiers (A.I.) are used:

+------------+--------------------------+------+----------------------------------+------------------------------------------+
|    Name    |        Rule Name         | A.I. |       Barcode Pattern            |              Field in Odoo               |
+============+==========================+======+==================================+==========================================+
| Product    | Global Trade Item Number | 01   | (01)(\\d{14})                    | :guilabel:`Barcode` field on product form|
|            | (GTIN)                   |      |                                  |                                          |
+------------+--------------------------+------+----------------------------------+------------------------------------------+
| Quantity   | Variable count of items  | 30   | (30)(\\d{0,8})                   | Quantity on transfer form                |
+------------+--------------------------+------+----------------------------------+------------------------------------------+
| Lot Number | Batch or lot number      | 10   | (10)([!"%-/0-9:-?A-Z_a-z]{0,20}) | Lot/serial number on transfer form       |
+------------+--------------------------+------+----------------------------------+------------------------------------------+

.. _barcode/operations/lot-setup:

Configuration
-------------

First, enable product tracking using lots by navigating to :menuselection:`Inventory app -->
Configuration --> Settings`, and checking the box for :guilabel:`Lots & Serial Numbers` under the
:guilabel:`Traceability` heading.

Then, set up the product barcode by navigating to the intended product form in
:menuselection:`Inventory app --> Products --> Products` and selecting the product. On the product
form, in the :guilabel:`General Information` tab, fill in the :guilabel:`Barcode` field with the
unique 14-digit `Global Trade Item Number (GTIN) <https://www.gs1.org/standards/get-barcodes>`_,
which is a universally recognized identifying number that is provided by GS1.

.. important::
   On the product form, omit the |AI| `01` for |GTIN| product barcode pattern, as it is only used to
   encode multiple barcodes into a single barcode that contains detailed information about the
   package contents.

.. example::

   To record the GS1 barcode for the product, `Fuji Apple`, enter the 14-digit |GTIN|
   `20611628936004` in the :guilabel:`Barcode` field on the product form.

   .. screenshot:: barcode-gs1-usage-barcode-field
      :menu: Inventory ‣ Products ‣ Products ‣ (Fuji Apple) ‣ General Information
      :shows: The "Barcode" field on the product form filled in with "20611628936004".
      :highlight: The "Barcode" field (red frame).
      :data: Product "Fuji Apple".
      :module: product
      :notes: English UI, light theme, 1440px width.

.. tip::
   To view or set the |GTIN| for several products at once, use the products list's :guilabel:`Barcode`
   column as described in :doc:`../setup/software`.

   .. screenshot:: barcode-gs1-usage-product-barcodes-page
      :menu: Inventory ‣ Products ‣ Products ‣ (list view)
      :shows: The products list with the "Barcode" column enabled, filled with 14-digit GTINs.
      :highlight: n/a
      :data: A handful of demo products with GTIN barcodes.
      :module: product
      :notes: English UI, light theme, 1440px width.

.. _barcode/operations/lot-setup-on-product:

After activating tracking by lots and serial numbers from the settings page, specify that this
feature is to be applied on each product by navigating to the :guilabel:`Inventory` tab on the
product form. Under :guilabel:`Tracking`, choose the :guilabel:`By Lots` radio button.

.. screenshot:: barcode-gs1-usage-track-by-lots
   :menu: Inventory ‣ Products ‣ Products ‣ (Fuji Apple) ‣ Inventory
   :shows: The "Tracking" field set to "By Lots" in the product form's Inventory tab.
   :highlight: The "By Lots" option (red frame).
   :data: Product "Fuji Apple".
   :module: stock
   :notes: English UI, light theme, 1440px width.

With the product barcode and lot tracking configured this way, scanning the plain product |GTIN|
resolves to the right product on any barcode-enabled screen (see :doc:`receipts_deliveries` and
:doc:`inventory_adjustment`); the lot or serial number itself is still entered or scanned into its
own field on the transfer, separately from the product barcode.

.. _barcode/operations/quantity-ex:

Configure barcode for product and non-unit quantity
===================================================

To build a GS1 barcode that contains products measured in a non-unit quantity, like kilograms, for
example, the following barcode patterns are used:

+-------------+--------------------------+----------+--------------------+----------------------------+
|    Name     |        Rule Name         |   A.I.   |  Barcode Pattern   |       Field in Odoo        |
+=============+==========================+==========+====================+============================+
| Product     | Global Trade Item Number | 01       | (01)(\\d{14})      | :guilabel:`Barcode` field  |
|             | (GTIN)                   |          |                    | on product form            |
+-------------+--------------------------+----------+--------------------+----------------------------+
| Quantity in | Variable count of items  | 310[0-5] | (310[0-5])(\\d{6}) | Quantity on transfer form  |
| kilograms   |                          |          |                    |                            |
+-------------+--------------------------+----------+--------------------+----------------------------+

As with the lot example above, the |GTIN| (application identifier `01`) is what gets set as the
product's plain :guilabel:`Barcode` field; the weight/quantity segment of a composite GS1 barcode is
not read automatically by the scan-enabled screens in this database, so the quantity is entered
manually once the product line has been added.

.. seealso::
   :ref:`Simplify vendor unit conversions with UoMs
   <inventory/product_replenishment/unit-conversion>`

Verify product moves
====================

After processing a scanned transfer, the resulting quantities are recorded on the
:guilabel:`Product Moves` report, accessible by navigating to :menuselection:`Inventory app -->
Reporting --> Product Moves`.

The items on the :guilabel:`Product Moves` report are grouped by product by default. To confirm the
received or delivered quantities, click on a product line to open its collapsible drop-down menu,
which displays a list of *stock move lines* for the product, each one tied to the transfer reference
(e.g. `WH/IN/00013`) it came from.

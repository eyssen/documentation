=========================
Supplier stock and data
=========================

Odoo tracks what *your own* warehouses hold. When a large part of the catalog is drop-shipped or
bought to order, the decisive question is a different one: **how much does the supplier have?** The
eYssen *Supplier Product Management* module (``supplier_product_management``, usually shortened to
*SPM*) records the supplier's own stock next to each vendor line of a product, and uses it to warn
on purchase and sales orders.

.. note::
   An earlier module, ``eyssen_supplier_product_management``, implements the same supplier-location
   and supplier-stock model without the minimum-order policy, the order warnings, the GTIN
   validation and the supplier dashboard. ``supplier_product_management`` supersedes it; only one
   of the two should be installed.

Supplier locations
==================

A **supplier location** is a warehouse or depot of a vendor, from which that vendor can ship.
Locations are maintained under :menuselection:`Purchase --> Configuration --> Supplier Locations`,
and each one has:

- a :guilabel:`Name` and a :guilabel:`Description`;
- the :guilabel:`Supplier` it belongs to;
- a :guilabel:`Location Address` — the contact holding the physical address; and
- an :guilabel:`Active` flag, plus a counter of the stock lines recorded for it.

A vendor's own contact form lists its :guilabel:`Locations` and its :guilabel:`Supplier Stocks`, and
shows a :guilabel:`Warehouse Stocks` summary of what that vendor currently holds.

.. screenshot:: inventory-supplier-products-location
   :menu: Purchase ‣ Configuration ‣ Supplier Locations ‣ (a location)
   :shows: A supplier location form with the Name, Supplier, Location Address and Description, and the
      counter of its stock lines.
   :highlight: The "Supplier" and "Location Address" fields (red frame).
   :data: Supplier "Azure Interior", location "Central depot".
   :module: supplier_product_management
   :notes: English UI, light theme, 1440px width, full form.

Supplier stock
==============

Supplier stock is recorded per **vendor line** of a product (the lines on a product's
:guilabel:`Purchase` tab), per supplier location, and per kind:

- :guilabel:`Free` — what the supplier can ship right now;
- :guilabel:`On-hand` — what the supplier physically holds; and
- :guilabel:`Expected` — what the supplier expects to receive, with an
  :guilabel:`Expected Date` and an :guilabel:`Expected Note`.

Every line carries its :guilabel:`Quantity` in the supplier's own unit of measure. The full list is
available under :menuselection:`Purchase --> SPM --> Supplier Stocks`.

.. screenshot:: inventory-supplier-products-stocks
   :menu: Purchase ‣ SPM ‣ Supplier Stocks
   :shows: The supplier stock list with the Supplier, Product, Supplier Location, Type (Free / On-hand /
      Expected), Quantity, unit of measure and Expected Date columns.
   :highlight: The "Type" column (red frame).
   :data: Three suppliers with free and expected quantities for several products.
   :module: supplier_product_management
   :notes: English UI, light theme, 1440px width, full list view.

Where supplier stock is shown
-----------------------------

- On a **vendor line** of a product: a :guilabel:`Supplier Quantity` total and a
  :guilabel:`Supplier Quantities` breakdown per location and kind.
- On a **product** (and product variant): a :guilabel:`Supplier Quantity` total across every
  vendor, and a :guilabel:`Supplier Stocks` action that opens the underlying lines.
- On a **sales order line**: the stock available at the supplier for that product, so a
  salesperson can promise a date for something that is not in the company's own stock.

.. screenshot:: inventory-supplier-products-on-product
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ Purchase tab
   :shows: The vendor lines of a product with the "Supplier Quantity" column, and the per-location
      "Supplier Quantities" breakdown next to a line.
   :highlight: The "Supplier Quantity" column (red frame).
   :data: Two vendors, one with 40 free and 100 expected units.
   :module: supplier_product_management
   :notes: English UI, light theme, 1440px width, crop to the Purchase tab.

Purchase order warnings
=======================

Minimum order amount
--------------------

On a vendor's contact form, a minimum order value can be agreed:

- :guilabel:`Minimum Order Amount` with its :guilabel:`Minimum Order Currency`; and
- :guilabel:`Minimum Order Policy` — :guilabel:`No Minimum`, :guilabel:`Warn Below Minimum` or
  :guilabel:`Block Below Minimum`.

A purchase order whose total falls under the agreed minimum shows a warning naming the missing
amount. With :guilabel:`Block Below Minimum` the order cannot be confirmed until the total reaches
the minimum; with :guilabel:`Warn Below Minimum` it is only a warning. The order total is converted
into the minimum-order currency with the rate of the order date.

.. screenshot:: inventory-supplier-products-min-order
   :menu: Purchase ‣ Orders ‣ Purchase Orders ‣ (a draft order)
   :shows: A draft purchase order with the "Below Minimum Order" warning above the order lines, naming the
      minimum amount agreed with the supplier and how much is missing.
   :highlight: The warning (red frame).
   :data: Supplier with a minimum order amount of 500.00 EUR and policy "Block Below Minimum"; order total
      320.00 EUR.
   :module: supplier_product_management
   :notes: English UI, light theme, 1440px width, crop to the warning and the totals.

Supplier stock shortage
-----------------------

While a purchase order is a :guilabel:`Draft` or :guilabel:`Sent`, each line compares its quantity
against the supplier's :guilabel:`Free` stock for that product, converted into the line's purchase
unit of measure, and flags a shortage when the order asks for more than the supplier has. A
:guilabel:`Supplier Stock Warning` on the order summarises the shortages.

.. note::
   When the supplier has **no** stock line at all for a product, its stock is treated as *unknown*
   rather than zero, so no shortage is reported.

A vendor's contact form can name a :guilabel:`Supplier Stock Manager`. When a draft order for that
vendor exceeds the available supplier stock, an activity is scheduled for that user. The activity is
not recreated while the same shortage persists, and a new shortage notifies again once the previous
one has cleared.

.. screenshot:: inventory-supplier-products-shortage
   :menu: Purchase ‣ Orders ‣ Purchase Orders ‣ (a draft order)
   :shows: A draft purchase order with the supplier stock warning listing the lines that ask for more than
      the supplier's free stock, and the "Supplier Available" quantity shown on those lines.
   :highlight: The warning and the "Supplier Available" column (red frames).
   :data: One line for 50 units where the supplier has 40 free.
   :module: supplier_product_management
   :notes: English UI, light theme, 1440px width, crop to the warning and the order lines.

Barcodes and manufacturer part numbers from supplier feeds
==========================================================

Supplier catalogs mix real barcodes with supplier SKUs and manufacturer codes in the same column.
SPM therefore validates every incoming code before it is written to a product:

- a value that is a valid **GTIN** — EAN-8, UPC-A (12 digits), EAN-13 or GTIN-14, with a correct
  check digit — is stored as the product's :guilabel:`Barcode`; and
- anything else is stored as the product's :guilabel:`Manufacturer Part Number` instead.

Only a valid GTIN is used to match a supplier's product to an existing product, so a
non-barcode code can neither end up in the barcode field nor merge two unrelated products onto one
product record.

.. screenshot:: inventory-supplier-products-mpn
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ General Information tab
   :shows: A product form showing both the "Barcode" field with a valid EAN-13 and the "Manufacturer Part
      Number" field with the supplier's own code.
   :highlight: The "Manufacturer Part Number" field (red frame).
   :data: A product imported from a supplier feed.
   :module: supplier_product_management
   :notes: English UI, light theme, 1440px width, crop to the two fields.

.. note::
   The individual supplier connectors that fetch these catalogs are separate modules, each with its
   own settings and import log; they all feed the same supplier stock and the shared **SPM
   Statisztika** dashboard under :menuselection:`Purchase --> SPM`.

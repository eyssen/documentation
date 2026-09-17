=========================
Bulk editing products
=========================

Maintaining a large catalog one record at a time is slow. The eYssen modules on this page change
many products at once, and fill an order or a transfer from a pasted list or a spreadsheet instead
of line by line.

.. seealso::
   - :doc:`Import and export data </applications/essentials/export_import_data>`
   - :doc:`Stock productivity helpers <stock_helpers>` — the same bulk-add wizard on transfers

Bulk update products
====================

``eyssen_product_bulk_update`` adds a :guilabel:`Bulk Update` action to the products list. Select
the products in :menuselection:`Inventory app --> Products --> Products`, then open
:menuselection:`Actions --> Bulk Update`.

The wizard's :guilabel:`General Information` tab changes:

- :guilabel:`Product Type` — set the type of every selected product;
- :guilabel:`Product Category` — move every selected product to one category; and
- :guilabel:`Pricelist Tags` with a :guilabel:`Pricelist Tag Operation` choosing how to apply them:
  :guilabel:`Update` replaces the tags, :guilabel:`Increase` adds the listed tags to the existing
  ones, :guilabel:`Decrease` removes them, and :guilabel:`Clean` clears every tag.

Fields left empty are not touched, so one wizard run can change only the category, only the tags,
or several things at once. The selected products are listed on the wizard's :guilabel:`Products`
tab, where a product can still be removed before clicking :guilabel:`Update`.

.. screenshot:: inventory-bulk-editing-product-update
   :menu: Inventory ‣ Products ‣ Products ‣ (select products) ‣ Actions ‣ Bulk Update
   :shows: The "Bulk Update" wizard, "General Information" tab, with the Product Type, Product Category and
      the "Pricelist Tag Operation" / "Pricelist Tags" fields, and the "Products" tab next to it.
   :highlight: The "Pricelist Tag Operation" field (red frame).
   :data: Eight selected products; operation "Increase" adding the tag "Winter sale".
   :module: eyssen_product_bulk_update
   :notes: English UI, light theme, 1440px width, crop to the wizard.

.. note::
   Other modules add their own fields to this wizard — for example the
   :doc:`out-of-stock status <out_of_stock_ordering>`, and the webshop fields below.

Bulk update variants' attributes
--------------------------------

A second :guilabel:`Bulk Update` action is available on the **product variants** list. It changes
the attribute values of the selected variants: an :guilabel:`Attributes Operation`
(:guilabel:`Update`, :guilabel:`Increase`, :guilabel:`Decrease` or :guilabel:`Clean`) decides how
the listed attribute values are applied, and :guilabel:`Update only selected Attributes`
(enabled by default) keeps the attributes that are not listed untouched.

.. screenshot:: inventory-bulk-editing-variant-attributes
   :menu: Inventory ‣ Products ‣ Product Variants ‣ (select variants) ‣ Actions ‣ Bulk Update
   :shows: The variant bulk-update wizard with the "Attributes Operation" field, the "Update only selected
      Attributes" checkbox and one line per attribute with its "Values" field.
   :highlight: The "Attributes Operation" field (red frame).
   :data: Six selected variants; operation "Increase" adding the value "Width: Wide".
   :module: eyssen_product_bulk_update
   :notes: English UI, light theme, 1440px width, crop to the wizard.

Webshop fields in bulk
----------------------

``eyssen_product_bulk_update_ws`` adds an :guilabel:`eCommerce` tab to the product bulk-update
wizard, with the same four operations (:guilabel:`Update`, :guilabel:`Increase`,
:guilabel:`Decrease`, :guilabel:`Clean`) for:

- :guilabel:`Websites` — which websites the selected products are published on; and
- :guilabel:`Website Categories` — the webshop categories the products belong to.

.. screenshot:: inventory-bulk-editing-ecommerce-tab
   :menu: Inventory ‣ Products ‣ Products ‣ (select products) ‣ Actions ‣ Bulk Update ‣ eCommerce
   :shows: The "eCommerce" tab of the bulk-update wizard with the "Website Operation" / "Websites" and
      "Website Categories Operation" / "Website Categories" field pairs.
   :highlight: The two operation fields (red frame).
   :data: Operation "Increase" adding the website "eYssen Shop" and the category "Winter".
   :module: eyssen_product_bulk_update_ws
   :notes: English UI, light theme, 1440px width, crop to the tab.

.. _inventory/bulk-editing/bulk-add:

Bulk-add products to an order
=============================

``eyssen_product_bulk_add_sale`` and ``eyssen_product_bulk_add_purchase`` add an
:guilabel:`Add Bulk Products` button to the **sales order** and the **purchase order** form, so a
list received by e-mail or kept in a spreadsheet can be turned into order lines in one step. The
same wizard is available on transfers through
:doc:`eyssen_product_bulk_add_stock <stock_helpers>`.

The wizard takes:

- :guilabel:`Format` — :guilabel:`Copy/Paste` (one product per line in a text box),
  :guilabel:`CSV` (a semicolon-separated file) or :guilabel:`Excel` (an ``.xlsx`` workbook, first
  sheet). Both file formats have an :guilabel:`Is there a header?` toggle.
- :guilabel:`Based On` — how each row is matched to a product: by :guilabel:`Default Code`
  (internal reference), :guilabel:`Barcode` or :guilabel:`Product Name`.
- :guilabel:`With Quantity` (on by default) and :guilabel:`With Price` — how many extra values each
  row carries. A live :guilabel:`Example` block shows the expected row format as these change. With
  neither enabled, every matched product is added with a quantity of one.
- :guilabel:`If Product Duplication` — what to do when a matched product already has a line on the
  order: :guilabel:`Stop` (the default here) raises an error and adds nothing, :guilabel:`Skip`
  leaves the existing line alone, :guilabel:`Replace` overwrites its quantity and price, and
  :guilabel:`Increase` adds the quantity on top.

.. screenshot:: inventory-bulk-editing-bulk-add-sale
   :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation) ‣ Add Bulk Products
   :shows: The "Add Bulk Products" wizard on a quotation, with Format "Copy/Paste", Based On "Default Code",
      "With Quantity" ticked, the live Example block and the paste box filled with four lines.
   :highlight: The "Based On" and "If Product Duplication" fields (red frame).
   :data: Four pasted lines of internal reference and quantity.
   :module: eyssen_product_bulk_add_sale
   :notes: English UI, light theme, 1440px width, crop to the wizard.

.. important::
   A row that cannot be matched to a product, or that does not parse (a wrong number of values, or
   a non-numeric quantity or price), stops the whole import with an error naming the offending row.
   Nothing is added until every row is valid.

.. note::
   The Excel format needs the ``openpyxl`` Python library in the Odoo environment.

==================================
Look up product information
==================================

The ``eyssen_barcode_app`` module adds a :guilabel:`Product Information` screen that answers a
simple question from the warehouse floor: *where is this product, and how much of it is
available?*

Open the screen
================

Go to the main apps menu and open the :menuselection:`Barcode` app, then click the
:guilabel:`Product Information` tile under :guilabel:`Basic Operations`.

.. screenshot:: barcode-product-lookup-app-home
   :menu: Barcode
   :shows: The Barcode app's home screen, with tiles grouped under "Basic Operations",
      "Warehouse Operations", and "Commercial Operations".
   :highlight: The "Product Information" tile (red frame).
   :data: n/a
   :module: eyssen_barcode_app
   :notes: English UI, light theme, 1440px width.

.. note::
   This screen is labelled :guilabel:`Termék információk` ("Product Information") in the app itself
   — the title is hardcoded in Hungarian and is not affected by the user's language setting.

Search for a product
=====================

Type into the search field, or use the :guilabel:`(camera)` button next to it to scan a barcode
with the device's camera, or scan directly with a USB/Bluetooth/keyboard-wedge scanner. The search
matches the :guilabel:`Barcode`, :guilabel:`Internal Reference`, and product name fields (partial
matches included), and lists every matching product below the search field.

.. screenshot:: barcode-product-lookup-search
   :menu: Barcode ‣ Product Information
   :shows: The Product Information screen with a search term entered and one matching product
      listed below it, including the "Print Labels" link and a stock table.
   :highlight: The search field and the stock table (red frame).
   :data: A demo product with two internal locations holding stock and one location with a
      package.
   :module: eyssen_barcode_app
   :notes: English UI, light theme, 1440px width.

For each matching product, the screen shows:

- The product name, and a :guilabel:`Címkék nyomtatása` ("Print Labels") link that opens the
  standard label-printing wizard for the product (see :doc:`../../inventory/product_management/labels`).
- :guilabel:`Vonalkód` ("Barcode") and :guilabel:`Azonosító` ("Internal Reference"), or a
  placeholder text when either is not set on the product.
- A table with one row per internal location currently holding stock of the product, with columns
  :guilabel:`Lokáció` ("Location"), :guilabel:`Csomag` ("Package", if the stock is inside a
  package), :guilabel:`Raktározott` ("On Hand"), :guilabel:`Lefoglalt` ("Reserved"), and
  :guilabel:`Elérhető` ("Available"), plus a totals row. If the product has no stock on hand
  anywhere, the table is replaced with :guilabel:`Nincs raktáron` ("Not in stock"). If the search
  term matches no product at all, :guilabel:`Nincs ilyen termék` ("No such product") is shown
  instead.

.. important::
   The row labels above (:guilabel:`Vonalkód`, :guilabel:`Azonosító`, :guilabel:`Lokáció`,
   :guilabel:`Csomag`, :guilabel:`Raktározott`, :guilabel:`Lefoglalt`, :guilabel:`Elérhető`) are
   hardcoded in Hungarian in the module and are shown this way regardless of the user's language.

.. note::
   Only *internal* locations are searched; stock in customer, vendor, or virtual locations is not
   listed on this screen.

.. seealso::
   :ref:`inventory/product_management/product-lookup`

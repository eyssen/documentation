=============================
Product and location barcodes
=============================

.. |GTIN| replace:: :abbr:`GTIN (Global Trade Item Number)`
.. |UPC| replace:: :abbr:`UPC (Universal Product Code)`
.. |EAN| replace:: :abbr:`EAN (European Article Number)`

Inventory operations like product configuration can be streamlined by taking advantage of barcode
scanning features. Assigning barcodes to products and locations is a key step, and users can
conveniently populate fields with a barcode scanner. This reduces manual entry, minimizes errors,
and speeds up common tasks like product selection, location assignment, and inventory adjustments.

Barcode nomenclature
=====================

Most retail products use EAN-13 barcodes, also known as Global Trade Identification Numbers (GTIN).
To create a new |GTIN| for a product, a company must have a GS1 Company Prefix. See :doc:`GS1
nomenclature <../operations/gs1_nomenclature>` for more information about using this system.

Odoo supports using any string as a barcode, so users can also create custom internal references to
use with barcode scanners. See :doc:`Default nomenclature <../operations/barcode_nomenclature>` to
learn about optional conventions around barcodes and default values in Odoo.

.. note::
   The default nomenclature (|UPC|/|EAN|) is active for every company out of the box, so no setup
   is needed to use it. See :doc:`../operations/barcode_nomenclature` and
   :doc:`../operations/gs1_nomenclature` for how to inspect the active rules or switch to GS1.

.. _inventory/barcode/set-barcodes:

Set product barcodes
=====================

Barcodes can be assigned to existing products from a product form, or in bulk from the products
list, in the **Inventory**, **Manufacturing**, or **Purchase** apps. The barcode field can be
populated either by typing or using scanner input.

From a product form
--------------------

To access a product's form, go to :menuselection:`Inventory app --> Products --> Products` and
select the product to add a barcode to.

In the :guilabel:`General Information` tab, click the :guilabel:`Barcode` field to either type in
the barcode or use a scanner to input the barcode value.

.. screenshot:: barcode-software-product-form-field
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ General Information
   :shows: The "Barcode" field on a product form, with the cursor active in the field.
   :highlight: The "Barcode" field (red frame).
   :data: Demo product with an EAN-13 barcode.
   :module: product
   :notes: English UI, light theme, 1440px width, crop to the General Information tab.

.. note::
   If using product variants, configure barcodes on individual variants and not the product
   template to allow scanning to retrieve the variants.

From the products list
------------------------

To set several barcodes at once without opening each product form, go to
:menuselection:`Inventory app --> Products --> Products`, switch to the list view, click the
:icon:`fa-sliders` :guilabel:`(Toggle columns)` icon at the top-right of the list, and enable the
:guilabel:`Barcode` column. The column can then be edited inline for each product.

.. screenshot:: barcode-software-products-list-barcode-column
   :menu: Inventory ‣ Products ‣ Products ‣ (list view)
   :shows: The products list with the "Barcode" column enabled and one cell being edited inline.
   :highlight: The "Barcode" column (red frame).
   :data: A handful of demo products, some with a barcode already set.
   :module: product
   :notes: English UI, light theme, 1440px width.

.. tip::
   To filter for the products that do not have barcodes yet, click the :icon:`fa-sort-desc`
   :guilabel:`(Toggle Search Panel)` icon to add a custom filter where the :guilabel:`Barcode`
   property is :guilabel:`is not set`.

   .. screenshot:: barcode-software-filter-no-barcode
      :menu: Inventory ‣ Products ‣ Products ‣ Filters ‣ Add Custom Filter
      :shows: The "Add Custom Filter" pop-up with "Barcode" "is not set" configured.
      :highlight: The filter condition (red frame).
      :data: n/a
      :module: product
      :notes: English UI, light theme, 1440px width.

.. _barcode/setup/location:

Print location barcodes
========================

Barcodes can be assigned to locations to keep track of where products are stored and manage
transfers, and are automatically available if the :doc:`Storage Locations
<../../inventory/warehouses_storage/inventory_management/use_locations>` feature is enabled.

To print barcodes for locations, go to :menuselection:`Inventory app --> Configuration -->
Settings`, scroll down to the :guilabel:`Warehouse` section, and click :icon:`fa-arrow-right`
:guilabel:`Locations`. Tick the boxes for locations and the :guilabel:`Print` button will appear,
downloading a PDF with barcodes for all selected locations.

.. screenshot:: barcode-software-print-location-barcodes
   :menu: Inventory ‣ Configuration ‣ Settings ‣ Warehouse ‣ Locations
   :shows: The locations list with several rows selected and the "Print" button visible in the
      list's action bar.
   :highlight: The "Print" button (red frame).
   :data: A handful of internal locations under WH/Stock.
   :module: stock
   :notes: English UI, light theme, 1440px width.

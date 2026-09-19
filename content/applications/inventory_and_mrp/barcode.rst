:nosearch:
:show-content:
:hide-page-toc:
:show-toc:

=======
Barcode
=======

Barcode scanning in this database is provided by a combination of Odoo's standard barcode
nomenclature engine and a set of eYssen modules that add scanning screens to *Inventory*,
*Purchase*, and *Sales*.

- The ``barcodes`` module supplies the barcode-nomenclature engine that decides what a scanned
  code means (a product, a location, a lot, and so on), and ``barcodes_gs1_nomenclature`` adds the
  rules needed to read GS1-128 barcodes. See :doc:`barcode/operations/barcode_nomenclature` and
  :doc:`barcode/operations/gs1_nomenclature`.
- ``eyssen_barcode_base`` provides the reusable scan widget used throughout the database: a text
  field that accepts input from a USB, Bluetooth, or keyboard-wedge scanner, plus a
  :guilabel:`(camera)` button that scans a barcode using the device's own camera (no separate
  scanner hardware required).
- ``eyssen_barcode_app`` adds a dedicated :menuselection:`Barcode` app with three screens: looking
  up a product's stock by barcode, scanning receipts/deliveries/internal transfers, and counting
  inventory by location. See :doc:`barcode/operations/product_lookup`, :doc:`barcode/operations/receipts_deliveries`,
  and :doc:`barcode/operations/inventory_adjustment`.
- ``eyssen_barcode_purchase`` and ``eyssen_barcode_sale`` add a scan button to draft purchase and
  sales orders. See :doc:`barcode/operations/scan_on_orders`.
- ``eyssen_barcode_stock`` adds a similar scan button to draft inventory transfers; it is
  documented with the rest of the transfer form in :doc:`inventory/product_management/stock_helpers`.

.. important::
   This database does **not** include Odoo's official, paid *Barcode* application (module
   ``stock_barcode``). Its mobile-optimized scanning screens, batch/wave/cluster transfer
   processing, and RFID support are not available; the eYssen modules above cover the equivalent
   day-to-day scanning needs instead.

.. note::
   Every screen listed above is available to any internal user (no dedicated access group is
   required beyond being logged in as an employee).

.. toctree::
   :titlesonly:
   :glob:

   barcode/setup
   barcode/operations

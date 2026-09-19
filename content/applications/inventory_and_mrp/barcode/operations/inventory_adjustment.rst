=================================
Count inventory with the scanner
=================================

The ``eyssen_barcode_app`` module adds an :guilabel:`Inventory Adjustment` flow that lets a
warehouse user pick a location and count what is on the shelf by scanning products, without typing
quantities into the standard :guilabel:`Physical Inventory` list directly.

Select a location
==================

Go to the main apps menu and open the :menuselection:`Barcode` app, then click the
:guilabel:`Inventory Adjustment` tile under :guilabel:`Warehouse Operations`. This opens a location
selector.

.. screenshot:: barcode-inventory-adjustment-location-selector
   :menu: Barcode ‣ Inventory Adjustment
   :shows: The "Inventory Adjustment - Select Location" screen, with the search/scan field,
      warehouse and location-type filters, and a list of matching locations below.
   :highlight: The search field and the location list (red frame).
   :data: A handful of internal locations under warehouse WH.
   :module: eyssen_barcode_app
   :notes: English UI, light theme, 1440px width.

Narrow down the list by scanning or typing a location's barcode or name into the search field, by
selecting a :guilabel:`Warehouse`, or by :guilabel:`Location Type` (:guilabel:`Internal Location` is
selected by default; :guilabel:`Vendor Location`, :guilabel:`View`, :guilabel:`Customer Location`,
:guilabel:`Inventory Loss`, :guilabel:`Production`, and :guilabel:`Transit Location` are also
available). Tap a location in the list to start counting it.

Count products at a location
==============================

The counting screen shows the selected location (read-only), an optional :guilabel:`Owner` field
for owned/consignment stock, a scan field, and a table of the products already counted at that
location during this session.

.. screenshot:: barcode-inventory-adjustment-count-screen
   :menu: Barcode ‣ Inventory Adjustment ‣ (a location)
   :shows: The Inventory Adjustment counting screen for one location, with the scan field and a
      table listing two counted products, their on-hand and counted quantities, the difference
      column, and the +/- buttons.
   :highlight: The counted-quantity column and the +/- buttons (red frame).
   :data: Location WH/Stock/Shelf 1 with two demo products already counted.
   :module: eyssen_barcode_app
   :notes: English UI, light theme, 1440px width.

Scanning a product's barcode adds it to the table (starting the count at `1`) or increases its
counted quantity by one if it is already listed; the :guilabel:`+`/:guilabel:`-` buttons on each row
do the same without a scanner, and the counted-quantity cell can also be typed into directly. The
:guilabel:`Difference` column compares the counted quantity against what Odoo currently has on
hand, and only appears once a product has been counted.

.. tip::
   Scanning a *location* barcode while on the counting screen (instead of a product barcode) jumps
   straight to that other location's counting screen, without going back through the location
   selector.

.. note::
   The table only lists products that have already been counted in this session (technically: quants
   with :guilabel:`Counted Quantity` set). It does not pre-list every product Odoo expects to find at
   the location.

Finalize the count
====================

This screen only records the counted quantities; it does not have an :guilabel:`Apply` button of
its own. To finish the adjustment, go to :menuselection:`Inventory app --> Operations --> Physical
Inventory`, find the counted lines for the location, and click :guilabel:`Apply` as described in
:doc:`../../inventory/warehouses_storage/inventory_management/count_products`. Counts entered from
the :guilabel:`Barcode` app appear in that same list, ordered by most recently updated first.

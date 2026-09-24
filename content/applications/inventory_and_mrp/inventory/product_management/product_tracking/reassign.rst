===========================
Reassign lot/serial numbers
===========================

Changing a product's tracking settings to use lots or serial numbers, *after* storing products in
Odoo without them, can lead to inconsistent records. Follow this documentation to learn how to use
an inventory adjustment to assign lot or serial numbers to products that were not originally
assigned lots.

.. screenshot:: inventory-reassign-warning
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ Inventory tab
   :shows: The warning shown on a product form after switching "Tracking" to lots or serial numbers while
      units are still in stock without a lot/serial number.
   :highlight: The warning message (red frame).
   :data: A storable product with 10 units on hand and no lot/serial number.
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the warning.

.. note::
   This document outlines the process of using two inventory adjustments: one to remove incorrect
   records *without* lot numbers, and another to save the quantities *with* the lot numbers.

.. seealso::
   - :doc:`Set up and use lot numbers <lots>`
   - :doc:`Use serial numbers <serial_numbers>`

Change on-hand quantity to zero
===============================

To change the product's settings to track by lots or serial numbers, begin by navigating to
:menuselection:`Inventory app --> Products --> Products`, and select the intended product.

Next, click the product's :guilabel:`On Hand` smart button to open the :guilabel:`Update Quantity`
page. In the :guilabel:`On Hand Quantity` column, change the value to zero.

.. note::
   If the product is stored in multiple locations, make sure the **total** on hand quantity at
   **all** locations is zero.

.. screenshot:: inventory-reassign-zero-quantity
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ On Hand
   :shows: The "Update Quantity" page of a product with the "On Hand Quantity" of the single stock line set
      to zero.
   :highlight: The "On Hand Quantity" cell (red frame).
   :data: One quant at location WH/Stock, quantity changed from 10 to 0.
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the quant line.

Change traceability setting
===========================

Return to the product form (:menuselection:`Inventory app --> Products --> Products`), and switch to
the :guilabel:`Inventory` tab. In the :guilabel:`Traceability` section, change the
:guilabel:`Tracking` option from :guilabel:`No Tracking` to :guilabel:`By Lots` or :guilabel:`By
Unique Serial Number`.

.. seealso::
   :doc:`expiration_dates`

.. screenshot:: inventory-reassign-tracking-field
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ Inventory tab
   :shows: The "Traceability" section of a product form with "Tracking" changed from "No Tracking" to "By
      Lots".
   :highlight: The "Tracking" field (red frame).
   :data: The same product as the previous screenshot, now with zero on hand.
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the Traceability section.

Restore on-hand quantity
========================

After manually changing the on-hand quantity to zero and changing the :guilabel:`Tracking` setting
to lots or serial numbers, restore the quantities by clicking the :guilabel:`On Hand` smart button
from the desired product form.

On the :guilabel:`Update Quantity` page, because the on-hand quantity had been previously changed to
zero, a :guilabel:`No Stock On Hand` warning appears on the page. From here, click the
:guilabel:`New` button in the top-left corner. Doing so reveals a new, modifiable line on the
:guilabel:`Update Quantity` page. Then, input a desired lot number in the :guilabel:`Lot/Serial
Number` field, and adjust the :guilabel:`On Hand Quantity` to its original value.

.. seealso::
   :doc:`../../warehouses_storage/inventory_management/count_products`

.. screenshot:: inventory-reassign-restore-quantity
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ On Hand ‣ New
   :shows: A new line on the "Update Quantity" page with the "Lot/Serial Number" field filled in and the "On
      Hand Quantity" set back to the original value; the "No Stock On Hand" warning is visible above.
   :highlight: The "Lot/Serial Number" and "On Hand Quantity" cells (red frames).
   :data: Lot "LOT0001", on-hand quantity 10, location WH/Stock.
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the new line and the warning.

.. tip::
   To find the original quantity, and adjust the :guilabel:`On Hand Quantity` accordingly, after
   assigning a new lot or serial number, click the :icon:`fa-pencil` :guilabel:`(pencil)` icon in
   the :guilabel:`On Hand Quantity` column. Then, click the :icon:`fa-history` :guilabel:`History`
   button on the far-right.

   .. screenshot:: inventory-reassign-history-button
      :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ On Hand ‣ (pencil icon in the On Hand Quantity
         column)
      :shows: The inventory-adjustment line being edited, with the clock-shaped "History" button visible at
         the far right of the row.
      :highlight: The "History" button (red frame).
      :data: The same product and quant as the previous screenshots.
      :module: stock
      :notes: English UI, light theme, 1440px width, crop to the row.

   The inventory adjustment that changed the on-hand quantity to zero is displayed in the
   :guilabel:`Quantity` field.

    .. screenshot:: inventory-reassign-history-entry
       :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ On Hand ‣ History
       :shows: The move-history list of the quant, showing the earlier inventory adjustment that set the
          on-hand quantity to zero, with its quantity value.
       :highlight: The "Quantity" value of the adjustment entry (red frame).
       :data: One inventory-adjustment move of -10 units.
       :module: stock
       :notes: English UI, light theme, 1440px width, crop to the history list.

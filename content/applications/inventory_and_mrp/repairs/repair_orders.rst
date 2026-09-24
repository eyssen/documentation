=====================
Process repair orders
=====================

.. |SO| replace:: :abbr:`SO (Sales Order)`
.. |DO| replace:: :abbr:`DO (Delivery Order)`
.. |RO| replace:: :abbr:`RO (Repair Order)`
.. |UoM| replace:: :abbr:`UoM (Unit of Measure)`

Sometimes, products delivered to customers can break or be damaged in transit, and need to be
returned for a refund, delivery of a replacement product, or repairs.

In Odoo, repairs for products returned by customers can be tracked in the *Repairs* app. Once
repaired, products can be redelivered to the customer.

The return and repair process for damaged products typically follows the below steps:

#. :ref:`Process return order for damaged product <repairs/repair_orders/return-order>`
#. :ref:`Create repair order for returned product <repairs/repair_orders/repair>`
#. :ref:`Return repaired product to customer <repairs/repair_orders/return-customer>`

Repair orders do not always start from a manual return, though: see
:ref:`Create repair orders automatically <repairs/repair_orders/automatic>` for the two settings
that let Odoo generate them on its own.

.. _repairs/repair_orders/return-order:

Return order
============

Returns can be processed in Odoo via *reverse transfers*, created directly from a sales order (SO)
once products have been delivered to a customer.

To create a return, navigate to the :menuselection:`Sales app`, and click into an |SO| from which a
product should be returned. Then, from the |SO| form, click the :guilabel:`Delivery` smart button.
Doing so opens the delivery order (DO) form.

From this form, click :guilabel:`Return`. This opens a :guilabel:`Reverse Transfer` pop-up window.

.. screenshot:: repairs-reverse-transfer-return
   :menu: Sales ‣ Orders ‣ (order) ‣ Delivery (smart button) ‣ Return
   :shows: The "Reverse Transfer" pop-up window with a "Product" line, its "Quantity", "Unit of
     Measure", and a trash icon to remove the line, plus "Return" and "Discard" buttons.
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the pop-up window.

This pop-up lists the :guilabel:`Product` included in the order, the :guilabel:`Quantity` delivered
to the customer, and the :guilabel:`Unit of Measure` the product was in.

Click the value in the :guilabel:`Quantity` field to change the quantity of the product to be
returned, if necessary.

Click the :guilabel:`🗑️ (trash)` icon at the far-right of the product line to remove it from the
return, if necessary.

Once ready, click :guilabel:`Return` to confirm the return. This creates a new receipt for the
returned products.

Once the product has been returned to the warehouse, receipt of the return can be registered in the
database by clicking :guilabel:`Validate` from the reverse transfer form.

.. tip::
   Once a reverse transfer for a return is validated, the value in the :guilabel:`Delivered` column
   on the original |SO| updates to reflect the difference between the original :guilabel:`Quantity`
   ordered, and the :guilabel:`Quantity` returned by the customer.

   .. screenshot:: repairs-quantity-delivered
      :menu: Sales ‣ Orders ‣ (order)
      :shows: The order lines of a sales order after a return, with the "Delivered" column showing
        a lower quantity than the "Ordered" column.
      :highlight: The "Delivered" column (red frame).
      :module: sale
      :notes: English UI, light theme, 1440px width, crop to the order lines.

.. _repairs/repair_orders/repair:

Create repair order
===================

Once products have been returned, their repairs can be tracked by creating a repair order (RO).

To create a new |RO|, navigate to :menuselection:`Repairs app`, and click :guilabel:`New`. This
opens a blank |RO| form.

.. screenshot:: repairs-left-hand-form
   :menu: Repairs ‣ New
   :shows: The left-hand column of a blank repair order form: "Customer", "Product to Repair",
     "Return", "Under Warranty" (unticked), and "Scheduled Date".
   :module: repair
   :notes: English UI, light theme, 1440px width, crop to the left-hand column.

On this form, begin by selecting a :guilabel:`Customer`. The customer selected should be for whom
the order will be invoiced and delivered.

In the :guilabel:`Product to Repair` field, click the drop-down menu to select the product that
needs repair. If necessary, click :guilabel:`Search More...` to open a :guilabel:`Search: Product to
Repair` pop-up window, and browse all products in the database.

Once a :guilabel:`Product to Repair` is selected, a new :guilabel:`Product Quantity` field appears
below it. In that field, enter the quantity (in a `0.00` format) of the product that requires
repair.

To the right of that value, click the drop-down list to select the unit of measure (UoM) for the
product.

If the product to repair is tracked :guilabel:`By Unique Serial Number` or :guilabel:`By Lots`, a
:guilabel:`Lot/Serial` field also appears. Select the specific lot or serial number of the returned
unit; this ensures the repair (and, later, its traceability report) is linked to that exact unit.

In the :guilabel:`Return` field, click the drop-down menu and select the return order from which the
product to be repaired comes from.

Tick the :guilabel:`Under Warranty` checkbox, if the product being repaired is covered by a
warranty. If ticked, the :guilabel:`Customer` is not charged for all the parts used in the repair
order.

In the :guilabel:`Scheduled Date` field, click the date to reveal a calendar popover window. From
this calendar, select a date for the repair, and click :guilabel:`Apply`.

.. screenshot:: repairs-completed-repair-form
   :menu: Repairs ‣ New
   :shows: The right-hand column of a filled-out repair order form: "Responsible", "Company",
     "Tags".
   :module: repair
   :notes: English UI, light theme, 1440px width, crop to the right-hand column.

In the :guilabel:`Responsible` field, click the drop-down menu and select the user who should be
responsible for the repair.

In the :guilabel:`Company` field, if in a multi-company environment, select which company this |RO|
belongs to.

In the :guilabel:`Tags` field, click the drop-down menu and select which tags should be applied to
this |RO|. New tags can be typed directly into the field, or managed from
:menuselection:`Repairs app --> Configuration --> Repair Orders Tags`.

Next to the |RO| reference, at the top of the form, click one of the :guilabel:`⭐⭐⭐ (stars)` to set
the :guilabel:`Priority` of the repair (:guilabel:`Normal` or :guilabel:`Urgent`).

.. tip::
   If custom fields were configured for the *Repairs* operation type used by this |RO| (see
   :menuselection:`Inventory app --> Configuration --> Operations Types --> Repairs`), they appear
   in a :guilabel:`Properties` widget below the main fields.

Parts tab
---------

Add, remove, or recycle parts in the :guilabel:`Parts` tab. To do so, click :guilabel:`Add a line`
at the bottom of the form, or click :guilabel:`Catalog` to browse and add products from a visual
product catalog.

In the :guilabel:`Type` column, click the box to reveal three options to choose from:
:guilabel:`Add` (selected by default), :guilabel:`Remove`, and :guilabel:`Recycle`.

.. screenshot:: repairs-type-column
   :menu: Repairs ‣ (order) ‣ Parts ‣ Add a line
   :shows: The "Type" column drop-down on a new parts line, with "Add", "Remove", and "Recycle"
     options.
   :module: repair
   :notes: English UI, light theme, 1440px width, crop to the line and its drop-down.

Choosing :guilabel:`Add` adds this part to the |RO|. Adding parts lists components for use in the
repair. If the components are used, the user completing the repair can record they were used. If
they were not used, the user can indicate that, too, and the components can be saved for another
use.

Choosing :guilabel:`Remove` removes this part from the |RO|. Removing parts lists components that
should be removed from the product being repaired during the repair process. If the parts are
removed, the user completing the repair can indicate they were removed.

Choosing :guilabel:`Recycle` recycles this part from the |RO|, designating it for later use or to be
repurposed for another use in the warehouse.

In the :guilabel:`Product` column, select which product (part) should be added, removed, or
recycled. In the :guilabel:`Demand` column, change the quantity, if necessary, to indicate what
quantity of this part should be used in the repair process.

In the :guilabel:`Done` column, change the value (in a `0.00` format) once the part has been
successfully added, removed, or recycled.

In the :guilabel:`Unit of Measure` column, select the |UoM| for the part.

Finally, in the :guilabel:`Used` column, tick the checkbox once the part has been used in the repair
process.

To add additional columns to the line, click the :guilabel:`(optional columns drop-down)` icon, at
the far-right of the header row. Select the desired options to add to the line.

.. screenshot:: repairs-additional-options
   :menu: Repairs ‣ (order) ‣ Parts ‣ (optional columns icon)
   :shows: The optional-columns drop-down at the top-right of the "Parts" tab list, with checkboxes
     for additional fields.
   :module: repair
   :notes: English UI, light theme, 1440px width, crop to the drop-down.

Once at least one part is confirmed, a :guilabel:`Component Status` indicator appears next to the
:guilabel:`Scheduled Date` field, showing whether all the parts needed for the repair are
:guilabel:`Available`, :guilabel:`Expected`, or :guilabel:`Late`.

Repair Notes and Miscellaneous tabs
-----------------------------------

Click the :guilabel:`Repair Notes` tab to add internal notes about this specific |RO|, and anything
the user performing the repair might need to know.

Click the blank text field to begin writing notes.

Click the :guilabel:`Miscellaneous` tab to see the :guilabel:`Operation Type` for this repair. By
default, this is set to :guilabel:`YourCompany: Repairs`, indicating this is a repair type
operation. Each warehouse automatically has its own :guilabel:`Repairs` operation type, visible
(read-only) on the warehouse's own form, under :menuselection:`Inventory app --> Configuration -->
Warehouses`.

Once all desired configurations have been made on the |RO| form, click :guilabel:`Confirm Repair`.
This moves the |RO| to the :guilabel:`Confirmed` stage, and reserves the necessary components needed
for the repair. If a component is out of stock, click :guilabel:`Check availability` to try to
reserve it again once it comes back in stock; click :guilabel:`Unreserve` to release components that
were already reserved.

A new :guilabel:`Forecasted` column appears on the product lines under the :guilabel:`Parts` tab,
displaying the availability of all components needed for the repair.

Once ready, click :guilabel:`Start Repair`. This moves the |RO| to the :guilabel:`Under Repair`
stage (in the upper-right corner). If the |RO| should be cancelled, click :guilabel:`Cancel Repair`;
this can be reversed later by clicking :guilabel:`Set to Draft`.

Once all products have been successfully repaired, the |RO| is completed. To register this in the
database, click :guilabel:`End Repair`.

.. note::
   If all parts added to the |RO| were not used, clicking :guilabel:`End Repair` causes an
   :guilabel:`Uncomplete Move(s)` pop-up window to appear.

   .. screenshot:: repairs-uncomplete-moves
      :menu: Repairs ‣ (order) ‣ End Repair
      :shows: The "Uncomplete Move(s)" pop-up window listing a part line with a difference between
        the initial demand and the quantity used, and "Discard" and "Validate" buttons.
      :module: repair
      :notes: English UI, light theme, 1440px width, crop to the pop-up window.

   The pop-up window informs the user that there is a difference between the initial demand and the
   actual quantity used for the order.

   If the :guilabel:`Used` quantity should be changed, click :guilabel:`Discard` or close the pop-up
   window. If the order should be confirmed, click :guilabel:`Validate`.

This moves the |RO| to the :guilabel:`Repaired` stage. A :guilabel:`Product Moves` smart button also
appears above the form.

Click the :guilabel:`Product Moves` smart button to view the product's moves history during and
after the repair process.

.. screenshot:: repairs-product-moves
   :menu: Repairs ‣ (order) ‣ Product Moves
   :shows: The stock move lines of a completed repair order, showing the parts consumed, removed,
     and recycled.
   :module: repair
   :notes: English UI, light theme, 1440px width.

.. _repairs/repair_orders/return-customer:

Return product to customer
--------------------------

Product is under warranty
~~~~~~~~~~~~~~~~~~~~~~~~~

Once the product has been successfully repaired, it can be returned to the customer.

Product is not under warranty
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the product is not under warranty, or should the customer bear the repair costs, click
:guilabel:`Create Quotation`. This opens a new |SO| form, pre-populated with the parts used in the
|RO|, with the total cost of the repair calculated. Once created, a :guilabel:`Sale Order` smart
button appears at the top of the |RO| form, linking back to it.

.. screenshot:: repairs-new-quotation
   :menu: Repairs ‣ (order) ‣ Create Quotation
   :shows: A new sales order form, pre-populated with the repair's customer and the parts used in
     the repair order as order lines, with the total.
   :module: repair
   :notes: English UI, light theme, 1440px width.

If this |SO| should be sent to the customer, click :guilabel:`Confirm`, and proceed to invoice the
customer for the repair.

.. tip::
   If the customer should be charged for a repair service, a service type product can be created and
   added to the |SO| for a repaired product.

To return the product to the customer, navigate to the :menuselection:`Sales app`, and select the
original |SO| from which the initial return was processed. Then, click the :guilabel:`Delivery`
smart button.

From the resulting list of operations, click the reverse transfer, indicated by the
:guilabel:`Source Document`, which should read `Return of WH/OUT/XXXXX`.

This opens the return form. At the top of this form, a :guilabel:`Repair Orders` smart button now
appears, linking this return to the completed |RO|.

Click :guilabel:`Return` at the top of the form. This opens a :guilabel:`Reverse Transfer` pop-up
window.

.. screenshot:: repairs-reverse-transfer-customer
   :menu: Sales ‣ Orders ‣ (order) ‣ Delivery (smart button) ‣ (reverse transfer) ‣ Return
   :shows: The "Reverse Transfer" pop-up window, on the return of the repaired product to the
     customer, with the "Product" line, "Quantity", and "Unit of Measure".
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the pop-up window.

This pop-up lists the :guilabel:`Product` included in the order, the :guilabel:`Quantity` delivered
to the customer, and the :guilabel:`Unit of Measure` the product was in.

Click the value in the :guilabel:`Quantity` field to change the quantity of the product to be
returned, if necessary.

Click the :guilabel:`🗑️ (trash)` icon at the far-right of the product line to remove it from the
return, if necessary.

Once ready, click :guilabel:`Return` to confirm the return. This creates a new delivery for the
returned products.

When the delivery has been processed and the product has been returned to the customer, click
:guilabel:`Validate` to validate the delivery.

.. _repairs/repair_orders/automatic:

Create repair orders automatically
==================================

Besides creating a repair order by hand, Odoo can also generate one automatically, in two cases.

Repair a returned product directly
----------------------------------

To be able to create a repair order directly from a return, without going through the *Repairs*
app, enable :guilabel:`Create Repair Orders from Returns` on the warehouse's return operation type:
navigate to :menuselection:`Inventory app --> Configuration --> Operations Types`, open the
:guilabel:`Returns` type for the relevant warehouse, and, in the :guilabel:`Repairs` section, tick
:guilabel:`Create Repair Orders from Returns`.

Once enabled, opening a validated reverse transfer shows a :guilabel:`Repair` button next to
:guilabel:`Return`. Clicking it opens a new |RO| form, pre-filled with the product, its quantity,
the customer, and the return itself in the :guilabel:`Return` field.

Create a repair order when a sale is confirmed
----------------------------------------------

To have Odoo automatically create a repair order whenever a specific product is sold, go to the
product's template form (:menuselection:`Sales app --> Products --> Products`), open the
:guilabel:`Inventory` tab, and tick the :guilabel:`Create Repair` checkbox.

Once confirmed, a sales order containing this product creates a linked, :guilabel:`Confirmed` |RO|
for each unit sold (one |RO| per serial number, for serialized products), using the warehouse's
:guilabel:`Repairs` operation type. A :guilabel:`Repair Order(s)` smart button then appears on the
sales order, linking to the generated |RO|\\(s).

.. important::
   This is intended for repair or maintenance services sold on a sales order (for example, a
   "diagnostic and repair" line), not for regular product sales; enabling it on a regular product
   would create a repair order every time that product is sold.

Link with other apps
====================

Depending on which apps are installed, additional smart buttons appear on the |RO| form, and on the
documents linked to it:

- If the *Purchase* app is installed and some parts had to be reordered, a :guilabel:`Purchase
  Orders` smart button appears on the |RO|, and a :guilabel:`Repair Orders` smart button appears on
  the resulting purchase order(s), linking the two records together.
- If the *Manufacturing* app is installed, a :guilabel:`Manufacturing Orders` smart button appears
  on the |RO| when parts are replenished through manufacturing, and a :guilabel:`Repair Orders`
  smart button appears on the corresponding manufacturing order.

.. seealso::
   - :doc:`../../sales/sales/products_prices/returns`
   - :doc:`../../services/equipment/equipment_measuring`
     for the eYssen *Equipment Management - Measuring Devices* module, which extends the repair
     order form with a :guilabel:`Calibration` mode for measuring equipment: see
     :ref:`repairs/repair_orders/calibration` below.

.. _repairs/repair_orders/calibration:

Calibration repair orders
=========================

.. note::
   Requires the *Equipment Management - Measuring Devices* module (``equipment_measuring``), which
   depends on the eYssen *Equipment Management* app (``equipment``). See
   :doc:`../../services/equipment/equipment_measuring` for the module itself.

When this module is installed, ticking the :guilabel:`Calibration` checkbox near the top of a |RO|
form turns it into a calibration record for a measuring device, and reveals a :guilabel:`Calibration`
group with the following fields:

- :guilabel:`Equipment`: the measuring device being calibrated; required, and restricted to
  equipment of the *Measuring* type from the eYssen *Equipment Management* app.
- :guilabel:`Calibration Date`: the date the calibration was performed.
- :guilabel:`Calibration Quality`: :guilabel:`Accredited` or :guilabel:`Werks`, indicating whether
  the calibration was performed by an accredited lab or in-house.
- :guilabel:`Result`: :guilabel:`Pass`, :guilabel:`Fail`, :guilabel:`Conditional Pass`, or
  :guilabel:`Conditional Fail`.
- :guilabel:`Performed By`: free-text name of the person who performed the calibration.
- :guilabel:`Certificate Number`: a read-only, gap-less certificate number, automatically assigned
  from a dedicated sequence as soon as the |RO| moves to :guilabel:`Under Repair`. It can never be
  entered or edited manually, cannot be cleared by turning :guilabel:`Calibration` back off, and a
  calibration that already has one cannot be reset to :guilabel:`New` or deleted.
- :guilabel:`Certificate`: an uploaded PDF or scan of the issued certificate.
- :guilabel:`Signed By` and :guilabel:`Sign Date`, and a :guilabel:`Customer Signature` field.
- :guilabel:`Work Performed` and :guilabel:`Calibration Notes` text fields.

.. important::
   The certificate number is a regulatory requirement: it is issued exactly once per calibration and
   cannot be changed by a user, even a database administrator, through the form.

Click :guilabel:`Print Worksheet`, in the header, to print the calibration worksheet report for this
|RO| (a plain repair prints the standard repair order report instead).

The :guilabel:`Calibrations` menu, under the eYssen *Equipment Management* app
(:menuselection:`Equipment Management --> Measuring Devices --> Calibrations`), lists every
calibration |RO| across all measuring devices, with its reference, certificate number, equipment,
calibration date, quality, result, customer, and status. From there, the search filters
:guilabel:`Accredited`, :guilabel:`Werks`, and :guilabel:`Voided Certificate` (cancelled repairs that
still carry an issued certificate number) can be used to narrow down the list, and results can be
grouped by :guilabel:`Calibration Quality`.

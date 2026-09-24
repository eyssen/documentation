========================
Manufacturing backorders
========================

.. |MO| replace:: :abbr:`MO (Manufacturing Order)`

In some cases, the full quantity of a manufacturing order cannot be produced immediately. When this
happens, Odoo *Manufacturing* allows for the manufacturing of partial quantities of the order and
creates a *backorder* for the remaining amount.

In the *Manufacturing* app, creating a backorder splits the original manufacturing order into two
orders. The reference tag for each order is the tag used for the original order, followed by a
hyphen and then an additional number to indicate that it's a backorder.

.. example::
   A company creates a manufacturing order with the reference tag *WH/MO/00175*, for 10 units of
   *Product X*. After starting work on the manufacturing order, the employee working the production
   line realizes there are only enough components in stock to produce five units of the product.

   Instead of waiting for additional stock of the components, they manufacture five units and create
   a backorder for the remaining five. This splits the manufacturing order into two separate orders:
   *WH/MO/00175-001* and *WH/MO/00175-002*.

   Order *001* contains the five units that have been manufactured, and is immediately marked as
   :guilabel:`Done`. Order *002* contains the five units that still need to be manufactured and is
   marked as :guilabel:`In Progress`. Once the remaining components are available, the employee
   returns to order *002* and manufactures the remaining units before closing the order.

Create a manufacturing backorder
================================

To create a backorder for part of a manufacturing order, begin by navigating to
:menuselection:`Manufacturing --> Operations --> Manufacturing Orders`. Select a manufacturing order
with a quantity of two or more or create one by clicking :guilabel:`Create`.

If a new manufacturing order is created, select a product from the :guilabel:`Product` drop-down
menu and enter a quantity of two or more in the :guilabel:`Quantity` field, then click
:guilabel:`Confirm` to confirm the order.

After manufacturing the quantity that is being produced immediately, enter that number in the
:guilabel:`Quantity` field at the top of the manufacturing order.

.. screenshot:: manufacturing-backorders-quantity-field
   :menu: Manufacturing app --> Operations --> Manufacturing Orders (open an MO)
   :shows: The top of an in-progress MO form, "Quantity" field edited to a value lower than the
      demand shown to its right.
   :highlight: The "Quantity" field.
   :data: Demo company "YourCompany"; MO for 10 units of "Product X", quantity set to 5.
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the header.

Next, click :guilabel:`Validate`, and a :guilabel:`You produced less than initial demand` pop-up
window appears, from which a backorder can be created. Click :guilabel:`Create Backorder` to split
the manufacturing order into two separate orders, with the reference tags *WH/MO/XXXXX-001* and
*WH/MO/XXXXX-002*.

.. screenshot:: manufacturing-backorders-create-button
   :menu: Manufacturing app --> Operations --> Manufacturing Orders (open the MO) --> Validate
   :shows: The "You produced less than initial demand" pop-up window, with "Create Backorder" and
      "No Backorder" buttons.
   :highlight: The "Create Backorder" button.
   :data: Demo company "YourCompany"; MO for 10 units of "Product X", 5 produced.
   :module: mrp
   :notes: English UI, light theme, 1440px width.

Order *001* contains the items that have been manufactured, and is closed immediately. Order *002*
is the backorder that contains the items that have yet to be manufactured, and remains open, to be
completed at a later date.

Once the remaining units can be manufactured, navigate to :menuselection:`Manufacturing -->
Operations --> Manufacturing Orders`, and then select the backorder manufacturing order. If all of
the remaining units are manufactured immediately, simply click :guilabel:`Validate` to close the
order.

If only some of the remaining units are manufactured immediately, create another backorder for the
remainder by following the steps detailed in this section.

.. seealso::
   For manufacturing orders that use routings, the operations must be completed on their
   :doc:`work orders <work_orders>` before the |MO| can be validated and a backorder created for
   it, as described above.

===========================
At confirmation reservation
===========================

.. _inventory/reservation_methods/at-confirmation:

.. |SO| replace:: :abbr:`SO (Sales Order)`

The *at confirmation* reservation method reserves products **only** when a sales order (SO) is
confirmed, **and** if enough stock of the products included in the |SO| is already available.

.. seealso::
   :doc:`About reservation methods <../reservation_methods>`

Configuration
=============

To set the reservation method to *at confirmation*, navigate to :menuselection:`Inventory app -->
Configuration --> Operations Types`. Then, select the desired :guilabel:`Operation Type` to
configure, or create a new one by clicking :guilabel:`New`.

In the :guilabel:`General` tab on the operation type form, locate the :guilabel:`Reservation Method`
field, and select :guilabel:`At Confirmation`.

.. screenshot:: reservation-methods-at-confirmation-operations-type
   :menu: Inventory ‣ Configuration ‣ Operations Types
   :shows: An operation type form for delivery orders with "At Confirmation" selected as the reservation method.
   :highlight: The "At Confirmation" option (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

Workflow
========

To see the *at confirmation* reservation method in action, create a new |SO| by navigating to
:menuselection:`Sales app --> New`.

Add a customer in the :guilabel:`Customer` field. Then, in the :guilabel:`Order Lines` tab, click
:guilabel:`Add a product`, and select a product to add to the quotation from the drop-down menu.
Finally, in the :guilabel:`Quantity` column, adjust the desired quantity of the product to sell.

Once ready, click :guilabel:`Confirm` to confirm the sales order.

Click the :guilabel:`📈 (area graph)` icon on the product line to reveal the product's
:guilabel:`Availability` tooltip, which reveals the :guilabel:`Reserved` number of units for this
order.

.. note::
   If there is **not** sufficient quantity of stock for the product included in the |SO|, the
   :guilabel:`📈 (area graph)` icon is red, instead of green.

   Instead of revealing the reserved number of units for the order, the :guilabel:`Availability`
   tooltip reads :guilabel:`Available`, and reveals the available number of units (e.g., `0 Units`).

.. screenshot:: reservation-methods-at-confirmation-availability-tooltip
   :menu: Sales app ‣ New
   :shows: A confirmed sales order line with the availability tooltip open, showing the reserved quantity for the product.
   :data: Sales order for 10 units of a storable product with 5 on hand.
   :module: stock
   :notes: English UI, light theme, 1440px width.

.. admonition:: Forecasted Report

   To see all the factors that affect product reservation, click the :guilabel:`View Forecast`
   internal link arrow to view the :guilabel:`Forecasted Report` dashboard.

   The :guilabel:`Forecasted Report` displays forecast information about the product(s) included in
   the sales order; namely, any live receipts of the product, and any active sales orders, which are
   listed in the :guilabel:`Used By` column. See how each order is fulfilled in the
   :guilabel:`Replenishment` column.

   Additionally, the :guilabel:`Forecasted` quantity is calculated at the top of the page, by adding
   the :guilabel:`On Hand` and :guilabel:`Incoming` quantity, and subtracting the
   :guilabel:`Outgoing` quantity, as shown below:

   .. screenshot:: reservation-methods-at-confirmation-forecasted-equation
      :menu: Inventory ‣ Reporting ‣ Forecasted Inventory
      :shows: The Forecasted Report page of a product, showing the forecasted quantity equation (on hand, incoming, outgoing).
      :module: stock
      :notes: English UI, light theme, 1440px width.

   If one order should be prioritized over another order, click the :guilabel:`Unreserve` button on
   the corresponding order line in the :guilabel:`Replenishment` column.

To deliver the products, click the :guilabel:`Delivery` smart button at the top of the sales order
form. To confirm that the reservation worked properly, ensure that the :guilabel:`Product
Availability` field reads `Available` (in green text), and the numbers in the :guilabel:`Demand` and
:guilabel:`Quantity` columns match (in this case, both should read `100.00`).

.. screenshot:: reservation-methods-at-confirmation-delivery-order
   :menu: Inventory ‣ Delivery Orders
   :shows: A delivery order created from a confirmed sales order, showing the Quantity and Reserved columns already filled in on the Operations tab.
   :module: stock
   :notes: English UI, light theme, 1440px width.

Once ready, click :guilabel:`Validate`.

.. seealso::
   - :doc:`Manual reservation <manually>`
   - :doc:`Before scheduled date reservation <before_scheduled_date>`

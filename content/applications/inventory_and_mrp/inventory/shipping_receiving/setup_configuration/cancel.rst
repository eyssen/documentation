==============================================
How to cancel a shipping request to a shipper?
==============================================

Overview
========

Odoo can handle various delivery methods, including third party
shippers. Odoo will be linked with the transportation company tracking
system.

It will allow you to manage the transport company, the real prices and
the destination.

You can easily cancel the request made to the carrier system.

How to cancel a shipping request?
=================================

-   If the delivery order is not **Validated**, then the request hasn't been
    made. You can choose to cancel the delivery or to change the
    carrier.

-   If you have clicked on **Validate**, the request has been made and you
    should have received the tracking number and the label. You can
    still cancel the request.
    Simply click on the **Cancel** button next to the **Carrier Tracking Ref**:

.. screenshot:: setup-configuration-cancel-cancel01
   :menu: Inventory ‣ Delivery Orders
   :shows: A validated delivery order with a Carrier Tracking Ref, showing the "Cancel" button next to it.
   :highlight: The "Cancel" button next to "Carrier Tracking Ref" (red frame).
   :module: delivery
   :notes: English UI, light theme, 1440px width.

You will now see that the shipment has been cancelled.

.. screenshot:: setup-configuration-cancel-cancel02
   :menu: Inventory ‣ Delivery Orders
   :shows: The same delivery order after cancelling the shipping request: the tracking reference is cleared and the "Send to Shipper" button is available again.
   :highlight: The cleared tracking reference (red frame).
   :module: delivery
   :notes: English UI, light theme, 1440px width.

You can now change the carrier if you wish.

How to send a shipping request after cancelling one?
====================================================

After cancelling the shipping request, you can change the carrier you
want to use. Confirm it by clicking on the **Send to shipper** button. You
will get a new tracking number and a new label.

.. screenshot:: setup-configuration-cancel-cancel03
   :menu: Inventory ‣ Delivery Orders
   :shows: The delivery order after choosing another carrier, with the "Send to Shipper" button that requests a new label and tracking number.
   :highlight: The "Send to Shipper" button (red frame).
   :module: delivery
   :notes: English UI, light theme, 1440px width.

.. seealso::
    * :doc:`invoicing`
    * :doc:`multipack`

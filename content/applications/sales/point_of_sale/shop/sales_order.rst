============
Sales orders
============

When working in retail, you might need to order products directly from your Point of sale.
Fortunately, Odoo Point of Sale is fully integrated with Odoo Sales, meaning that you can create a
sales order and pay for it directly from your point of sale.

Select a sales order
====================

From the **Point of Sale** application, open a new session. Then, click on
:guilabel:`Quotation/Order` to get the complete list of quotations and sales orders created on the
sales application.

.. screenshot:: pos-sales-order-button
   :menu: (POS interface) ‣ Register screen
   :shows: The POS register screen with the "Quotation/Order" button in the top bar.
   :highlight: The "Quotation/Order" button (red frame).
   :module: point_of_sale, pos_sale
   :notes: English UI, light theme, 1440px width, centered, crop to the top bar.

.. note::
   To ease finding the right sales order, you can filter that list on the **customer** or on the
   **order reference**. You can also set the customer before clicking on
   :guilabel:`Quotation/Order` to reduce the list to one particular customer.

Apply a down payment or settle the order
========================================

From the list of sales order, select one to make a payment.

.. screenshot:: pos-sales-order-list
   :menu: (POS interface) ‣ Quotation/Order
   :shows: The list of quotations and sales orders inside the POS, with the customer, date and total of each order.
   :module: point_of_sale, pos_sale
   :notes: English UI, light theme, 1440px width, centered.

You can either:

- Settle the order **partially**: after clicking on :guilabel:`Apply a down payment`, enter the
  percentage of down payment you want the customer to pay. Then, click on :guilabel:`ok` and proceed
  with the order.
- Settle the order **completely**: click on :guilabel:`Settle the order` to pay for the total of the
  sales order.

.. note::
   Once you settle a sales order, the applied down payment is automatically deducted from the total
   amount.

.. Seealso::
   - :doc:`/applications/sales/sales/invoicing/down_payment`

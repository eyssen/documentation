===================
Returns and refunds
===================

The Odoo *Sales* app provides two different ways to process returns. The method used depends on
whether or not an invoice has been sent.

Before invoicing
================

Returns are completed using *Reverse Transfers* when a customer decides to return a product
**before** an invoice has been sent or validated.

.. note::
   In order to use *Reverse Transfers*, the *Inventory* app **must** be installed.

To start a return before invoicing, navigate to the :menuselection:`Sales` app, select the desired
sales order, and click on the :guilabel:`Delivery` smart button to open the associated delivery
order.

.. screenshot:: sales-returns-delivery-smart-button
   :menu: Sales ‣ Orders ‣ Orders ‣ (a confirmed order)
   :shows: The button box of a confirmed sales order with the Delivery smart button.
   :highlight: The Delivery smart button (red frame).
   :data: Order S00042, 1 delivery.
   :module: sale_stock
   :notes: English UI, light theme, 1440px width, crop to the button box.

On the validated delivery order, click :guilabel:`Return`.

.. screenshot:: sales-returns-delivery-return-button
   :menu: Inventory ‣ Deliveries ‣ (a validated delivery)
   :shows: A validated delivery order in the Done state with the Return button in the header.
   :highlight: The Return button (red frame).
   :data: Delivery WH/OUT/00015 of order S00042.
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the header.

This opens a :guilabel:`Reverse Transfer` pop-up window.

By default, the :guilabel:`Quantity` matches the validated quantities from the delivery order.
Update the quantities, if necessary. Click on the :guilabel:`🗑️ (trash)` icon next to a line item
to remove it from the return.

.. screenshot:: sales-returns-reverse-transfer-popup
   :menu: Inventory ‣ Deliveries ‣ (a validated delivery) ‣ Return
   :shows: The "Reverse Transfer" pop-up window listing the delivered products with an editable return quantity.
   :highlight: The return quantity field (red frame).
   :data: 1 of 5 units returned.
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

Next, click :guilabel:`Return` to confirm the return. This generates a new warehouse operation for
the incoming returned product(s).

.. screenshot:: sales-returns-return-operation
   :menu: Inventory ‣ Returns ‣ (the return)
   :shows: The generated return operation, ready to be validated, with the returned quantity on its line.
   :highlight: The Validate button (red frame).
   :data: Return of 1 unit from WH/OUT/00015.
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the header and lines.

Upon receiving the return, the warehouse team validates the warehouse operation by clicking
:guilabel:`Validate`. Then, on the original sales order, the :guilabel:`Delivered` quantity updates
to reflect the difference between the initial validated quantities and the returned quantities.

.. screenshot:: sales-returns-updated-delivered-qty
   :menu: Sales ‣ Orders ‣ Orders ‣ (a confirmed order) ‣ Order Lines
   :shows: The Order Lines tab where the Delivered quantity has been reduced by the returned quantity.
   :highlight: The Delivered column (red frame).
   :data: Order S00042: 5 ordered, 4 delivered.
   :module: sale_stock
   :notes: English UI, light theme, 1440px width, crop to the order-lines table.

When an invoice is created, the customer receives an invoice **only** for the products they are
keeping, if any.

After invoicing
===============

Sometimes, customers return an item after they receive and/or pay for their invoice. In these
cases, a return using only *Reverse Transfers* is insufficient since validated, or sent, invoices
cannot be changed.

However, *Reverse Transfers* can be used in conjunction with *Credit Notes* to complete the
customer's return.

To start a return after invoicing, navigate to the relevant sales order in the
:menuselection:`Sales` app.

If there is a payment registered on the sales order, the payment details appear in the chatter, and
the invoice (accessible through the :guilabel:`Invoices` smart button) has a green :guilabel:`In
Payment` banner.

.. screenshot:: sales-returns-invoice-in-payment
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (a paid invoice)
   :shows: A posted customer invoice with the green "In Payment" ribbon in the upper-right corner.
   :highlight: The "In Payment" ribbon (red frame).
   :data: Invoice of order S00042.
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the top of the invoice.

From the sales order, click on the :guilabel:`Delivery` smart button to view the validated delivery
order. Then, click :guilabel:`Return` to open the :guilabel:`Reverse Transfer` pop-up window.

Next, edit the :guilabel:`Product` and/or :guilabel:`Quantity`, as needed for the return. Then,
click :guilabel:`Return`. This generates a new warehouse operation for the incoming returned
product(s), which is validated by the warehouse team once the return is received by clicking
:guilabel:`Validate`.

Then, on the sales order, the :guilabel:`Delivered` quantity updates to reflect the difference
between the initial validated quantities and the returned quantities.

To process a refund, navigate to the relevant invoice (from the sales order, click on the
:guilabel:`Invoices` smart button). Then, click the :guilabel:`Credit Note` button at the top of the
validated invoice.

.. screenshot:: sales-returns-credit-note-button
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (a posted invoice)
   :shows: A posted customer invoice with the "Credit Note" button in the header.
   :highlight: The "Credit Note" button (red frame).
   :data: Invoice of order S00042.
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the header.

Doing so reveals a :guilabel:`Credit Note` pop-up form.

.. screenshot:: sales-returns-credit-note-popup
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (a posted invoice) ‣ Credit Note
   :shows: The credit-note pop-up window with the Reason, Journal and Reversal Date fields.
   :highlight: The Reason field (red frame).
   :data: Reason "Returned goods".
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

Start by entering a :guilabel:`Reason displayed on Credit Note` and a specific :guilabel:`Journal`
to process the credit. Then, select a specific :guilabel:`Reversal Date`.

After the information is filled in, click :guilabel:`Reverse` or :guilabel:`Reverse and Create
Invoice`. Then, edit the draft, if needed.

Lastly, click :guilabel:`Confirm` to confirm the credit note.

When complete, a blue banner reading: :guilabel:`You have outstanding credits for this customer. You
can allocate them to mark this invoice as paid.` appears at the top of the page.

.. seealso::
   :doc:`../../../finance/accounting/customer_invoices/credit_notes`

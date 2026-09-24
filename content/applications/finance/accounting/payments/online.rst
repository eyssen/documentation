:show-content:

===============
Online payments
===============

To make it more convenient for your customers to pay the invoices you issue, you can activate the
**Invoice Online Payment** feature, which adds a *Pay Now* button on their **Customer Portal**. This
allows your customers to see their invoices online and pay directly with their favorite payment
method, making the payment process much easier.

.. screenshot:: accounting-online-payments-providers
   :menu: (customer portal) ‣ My Invoices ‣ (open an invoice) ‣ Pay Now
   :shows: Payment dialog of the customer portal listing the available payment methods/providers.
   :highlight: The list of payment methods (red frame).
   :data: Demo customer invoice; Wire Transfer and a test card provider enabled.
   :module: account_payment, payment
   :notes: English UI, light theme, 1440px width, logged in as the portal user.

Configuration
=============

Make sure your :doc:`payment providers are correctly configured <../../payment_providers>`.

.. note::
   By default, ":doc:`Wire Transfer </applications/finance/payment_providers/wire_transfer>`" is the
   only payment provider activated, but you still have to fill out the payment details.

To activate the Invoice Online Payment, go to :menuselection:`Accounting --> Configuration -->
Settings`, enable :guilabel:`Invoice Online Payment` in the :guilabel:`Customer Payments` section,
and click :guilabel:`Save`.

Customer Portal
===============

After issuing the invoice, click :guilabel:`Send` and send the invoice by email to the customer.
They will receive an email with a link that redirects them to the invoice on their **Customer
Portal**.

.. screenshot:: accounting-online-payments-email
   :menu: (customer mailbox) ‣ invoice email
   :shows: Invoice email received by the customer with the "View Invoice" button.
   :highlight: The "View Invoice" button (red frame).
   :data: Demo customer invoice sent by email.
   :module: account
   :notes: English UI, light theme, crop to the email body.

They can choose which payment provider to use by clicking :guilabel:`Pay Now`.

.. screenshot:: accounting-online-payments-pay-now
   :menu: (customer portal) ‣ My Invoices ‣ (open an invoice)
   :shows: Invoice page of the customer portal with the "Pay Now" button in the sidebar.
   :highlight: The "Pay Now" button (red frame).
   :data: Demo customer invoice, not paid.
   :module: account_payment
   :notes: English UI, light theme, 1440px width, logged in as the portal user.

.. seealso::

   - :doc:`/applications/finance/payment_providers`

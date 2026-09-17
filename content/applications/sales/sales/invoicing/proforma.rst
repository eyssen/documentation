==================
Pro-forma invoices
==================

A *pro-forma invoice* is an abridged or estimated invoice sent in advance of a delivery of goods. It
notes the kind and quantity of goods, their value, and other important information, such as weight
and transportation charges.

Pro-forma invoices are commonly used as preliminary invoices with a quotation. They are also used
during importation for customs purposes. They differ from a normal invoice, in that they are *not* a
demand (or request) for payment.

Configuration
=============

In order to utilize pro-forma invoices, the *Pro-Forma Invoice* feature **must** be activated.

To enable this feature, navigate to :menuselection:`Sales app --> Configuration --> Settings`, and
in the :guilabel:`Quotations \& Orders` section, click the checkbox next to :guilabel:`Pro-Forma
Invoice`. Then, click :guilabel:`Save` to save all changes.

.. screenshot:: sales-proforma-setting
   :menu: Sales ‣ Configuration ‣ Settings
   :shows: The Settings page scrolled to the "Quotations & Orders" section with the "Pro-Forma Invoice" checkbox enabled.
   :highlight: The "Pro-Forma Invoice" setting (red frame).
   :data: Demo company.
   :module: sale
   :notes: English UI, light theme, 1440px width, crop to the setting block.

Send pro-forma invoice
======================

With the :guilabel:`Pro-Forma Invoice` feature activated, the option to send a pro-forma invoice is
now available on any quotation or sales order, via the :guilabel:`Send Pro-Forma Invoice` button.

.. screenshot:: sales-proforma-send-button
   :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation)
   :shows: The button row at the top of a quotation, including the "Send PRO-FORMA Invoice" button.
   :highlight: The "Send PRO-FORMA Invoice" button (red frame).
   :data: Quotation S00021.
   :module: sale
   :notes: English UI, light theme, 1440px width, crop to the header.

.. note::
   Pro-forma invoices can **not** be sent for a sales order or quotation if an invoice for a down
   payment has already been sent, or for a recurring subscription.

   In either case, the :guilabel:`Send Pro-Froma Invoice` button does **not** appear.

   However, pro-forma invoices **can** be sent for services, event registrations, courses, and/or
   new subscriptions. Pro-forma invoices are not limited to physical, consumable, or storable goods.

When the :guilabel:`Send Pro-Forma Invoice` button is clicked, a pop-up window appears, from which
an email can be sent.

In the pop-up window, the :guilabel:`Recipients` field is auto-populated with the customer from the
sales order or quotation. The :guilabel:`Subject` field and the body of the email can be modified,
if necessary.

The pro-forma invoice is automatically added as an attachment to the email.

When ready, click :guilabel:`Send`, and Odoo instantly sends the email, with the attached pro-forma
invoice, to the customer.

.. screenshot:: sales-proforma-email-popup
   :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation) ‣ Send PRO-FORMA Invoice
   :shows: The email composer pop-up with the recipient, subject and body pre-filled and the pro-forma invoice PDF attached.
   :highlight: The attached pro-forma PDF (red frame).
   :data: Quotation S00021 for "Deco Addict".
   :module: sale
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

.. tip::
   To preview what the pro-forma invoice looks like, click on the PDF at the bottom of the email
   pop-up window *before* clicking :guilabel:`Send`. When clicked, the pro-forma invoice is
   downloaded instantly. Open that PDF to view (and review) the pro-forma invoice.

   .. screenshot:: sales-proforma-pdf
      :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation) ‣ Send PRO-FORMA Invoice
      :shows: The generated pro-forma invoice PDF, headed "PRO-FORMA INVOICE", with the customer block, the order lines and the totals.
      :highlight: The "PRO-FORMA INVOICE" title (red frame).
      :data: Quotation S00021.
      :module: sale
      :notes: English UI, light theme, crop to the PDF page.

.. seealso::
   :doc:`invoicing_policy`

================================================
Invoice based on delivered or ordered quantities
================================================

Different business policies might require different options for invoicing:

- The *Invoice what is ordered* rule is used as the default mode in Odoo *Sales*, which means
  customers are invoiced once the sales order is confirmed.
- The *Invoice what is delivered* rule invoices customers once the delivery is done. This rule is
  often used for businesses that sell materials, liquids, or food in large quantities. In these
  cases, the ordered quantity may differ slightly from the delivered quantity, making it preferable
  to invoice the quantity actually delivered.

Being able to have different invoicing options provides more flexibility.

Invoicing policy features
=========================

To activate the necessary invoicing policy features, go to :menuselection:`Sales app -->
Configuration --> Settings`, and under the :guilabel:`Invoicing` heading, select an
:guilabel:`Invoicing Policy` rule: :guilabel:`Invoice what is ordered` or :guilabel:`Invoice what is
delivered`.

.. screenshot:: sales-invoicing-policy-setting
   :menu: Sales ‣ Configuration ‣ Settings
   :shows: The Settings page scrolled to the "Invoicing" section, with the "Invoicing Policy" radio buttons "Invoice what is ordered" and "Invoice what is delivered".
   :highlight: The Invoicing Policy radio buttons (red frame).
   :data: Demo company.
   :module: sale
   :notes: English UI, light theme, 1440px width, crop to the setting block.

.. important::
   If the :guilabel:`Invoice what is delivered` rule is chosen, it is **not** possible to activate
   the :guilabel:`Automatic Invoice` feature, which automatically generates invoices when an online
   payment is confirmed.

Invoicing policy on product form
================================

On any product page, via the :menuselection:`Sales app --> Products --> Products dashboard`, locate
the :guilabel:`Invoicing Policy` option located under the :guilabel:`General Information` tab. It
can be changed manually using the drop-down menu.

.. screenshot:: sales-invoicing-policy-product-field
   :menu: Sales ‣ Products ‣ Products ‣ (a product) ‣ General Information
   :shows: A product form's General Information tab with the "Invoicing Policy" field set to "Delivered quantities".
   :highlight: The Invoicing Policy field (red frame).
   :data: Product "Cabinet with Doors".
   :module: sale
   :notes: English UI, light theme, 1440px width, crop to the Sales group of the tab.

Impact on sales flow
====================

In Odoo *Sales*, the basic sales flow starts with the creation of a quotation. Then, that quotation
is sent to a customer. Next, it needs to be confirmed, which turns the quotation into a sales order.
This, in turn, creates an invoice.

The following is a breakdown of how invoicing policy rules impact the aforementioned sales flow:

- :guilabel:`Invoice what is ordered`: No impact on the basic sales flow. An invoice is created as
  soon as a sale is confirmed.
- :guilabel:`Invoice what is delivered`: Minor impact on sales flow, because the delivered quantity
  needs to be manually entered on the sales order. Or, the *Inventory* app can be installed and used
  to confirm the delivered quantity before creating an invoice with the *Sales* app.

.. warning::
   If a user attempts to create an invoice without validating the delivered quantity, the following
   error message appears: :guilabel:`There is no invoiceable line. If a product has a Delivered
   quantities invoicing policy, please make sure that a quantity has been delivered.`

   .. screenshot:: sales-invoicing-policy-nothing-to-invoice
      :menu: Sales ‣ Orders ‣ Orders ‣ (a confirmed order) ‣ Create Invoice
      :shows: The warning dialog telling the user that there is nothing to invoice because no quantity has been delivered yet.
      :highlight: The warning message (red frame).
      :data: Order for a product invoiced on delivered quantities, nothing delivered.
      :module: sale
      :notes: English UI, light theme, 1440px width, crop to the dialog.

.. note::
   Once a quotation is confirmed, and the status changes from :guilabel:`Quotation sent` to
   :guilabel:`Sales order`, the delivered and invoiced quantities are available to view, directly
   from the sales order. This is true for both invoicing policy rule options.

   .. screenshot:: sales-invoicing-policy-delivered-invoiced-columns
      :menu: Sales ‣ Orders ‣ Orders ‣ (a confirmed order) ‣ Order Lines
      :shows: The Order Lines tab of a confirmed order showing the Quantity, Delivered and Invoiced columns side by side.
      :highlight: The Delivered and Invoiced columns (red frame).
      :data: One line, 10 ordered, 10 delivered, 0 invoiced.
      :module: sale_stock
      :notes: English UI, light theme, 1440px width, crop to the order-lines table.

   Odoo automatically adds the quantities to the invoice, both :guilabel:`Delivered` and
   :guilabel:`Invoiced`, even if it's a partial delivery, when the quotation is confirmed.

Finally, there are a few different options to create an invoice: :guilabel:`Regular invoice`,
:guilabel:`Down payment (percentage)` or :guilabel:`Down payment (fixed amount)`.

.. seealso::
   Be sure to check out the documentation explaining down payment options to learn more:
   :doc:`/applications/sales/sales/invoicing/down_payment`

:show-content:

=================
Customer invoices
=================

A customer invoice is a document issued by a company for products and/or services sold to a
customer. It records receivables as they are sent to customers. Customer invoices can include
amounts due for the goods and/or services provided, applicable sales taxes, shipping and handling
fees, and other charges. Odoo supports multiple invoicing and payment workflows.

.. seealso::
   :doc:`/applications/finance/accounting/customer_invoices/overview`

From draft invoice to profit and loss report, the process involves several steps once the goods (or
services) have been ordered/shipped (or rendered) to a customer, depending on the invoicing policy:

- :ref:`accounting/invoice/creation`
- :ref:`accounting/invoice/confirmation`
- :ref:`accounting/invoice/sending`
- :ref:`accounting/invoice/paymentandreconciliation`
- :ref:`accounting/invoice/followup`
- :ref:`accounting/invoice/reporting`

.. _accounting/invoice/creation:

Invoice creation
================

Draft invoices can be created directly from documents like sales orders or purchase orders or
manually from :menuselection:`Accounting --> Customers --> Invoices`, or from the
:guilabel:`Customer Invoices` journal card of the accounting dashboard.

An invoice must include the required information to enable the customer to pay promptly for their
goods and services. Make sure the following fields are appropriately completed:

- :guilabel:`Customer`: When a customer is selected, Odoo automatically pulls information from the
  customer record like the invoice address,
  :doc:`preferred payment terms <customer_invoices/payment_terms>`,
  :doc:`fiscal positions <taxes/fiscal_positions>`, receivable account, and more onto the invoice.
  To change these values for this specific invoice, edit them directly on the invoice. To change
  them for future invoices, change the values on the contact record.
- :guilabel:`Invoice Date`: If not set manually, this field is automatically set as the current date
  upon confirmation.
- :guilabel:`Due Date` or :doc:`payment terms <customer_invoices/payment_terms>`: To specify when
  the customer has to pay the invoice.
- :guilabel:`Journal`: Automatically set and can be changed if needed.
- :doc:`Currency <get_started/multi_currency>`. If the invoice's currency differs from the
  company's currency, the currency exchange rate is automatically displayed.

In the :guilabel:`Invoice Lines` tab:

- :guilabel:`Product`: Click :guilabel:`Add a line`, then search for and select the product.
- :guilabel:`Quantity`
- :guilabel:`Price`
- :doc:`Taxes <taxes>` (if applicable)

To access the product catalog and view all items in an organized display, click :doc:`Catalog
</applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/product_catalog>`.
When the products and quantities are selected, click :guilabel:`Back to Invoice` to return to the
invoice; the selected catalog items will appear in the invoice lines.

.. _accounting/invoice/line-tools:

Invoice line tools
------------------

The following eYssen modules add tools above or in the invoice lines of **draft** invoices and
bills:

- :guilabel:`Add Products from Delivery Notes` (*Invoicing from Stock Picking*,
  `eyssen_stock_picking_invoice`): loads the not yet invoiced quantities of validated delivery
  notes or receipts of the partner. See :doc:`customer_invoices/invoice_from_delivery_notes`.
- :icon:`fa-cubes` :guilabel:`Add Bulk Products` (*Add Bulk Products for Invoice*,
  `eyssen_product_bulk_add_invoice`): adds several products at once. In the pop-up window, select
  the :guilabel:`Format` (:guilabel:`Copy/Paste`, :guilabel:`CSV` or :guilabel:`Excel`), whether the
  file has a header (:guilabel:`Is there a header?`), how the products are identified
  (:guilabel:`Based On`: :guilabel:`Default Code`, :guilabel:`Barcode` or :guilabel:`Product Name`),
  whether the rows contain a quantity (:guilabel:`With Quantity`) and a unit price
  (:guilabel:`With Price`), and what happens if a product is already on the invoice (:guilabel:`If
  Product Duplication`: :guilabel:`Stop`, :guilabel:`Skip`, :guilabel:`Replace` or
  :guilabel:`Increase`). An example of the expected format is displayed in the window. Then, paste
  the rows in the :guilabel:`Products` field or upload the :guilabel:`File`, and click
  :guilabel:`Add`.

  .. note::
     - In :guilabel:`Copy/Paste` mode, write one product per line, with the quantity and the price
       separated by spaces (e.g., `cb 10 99`).
     - CSV files must use semicolons (`;`) as separators; the columns are: product identifier,
       quantity, price.

- :icon:`fa-files-o` :guilabel:`Add Previous Items` (*Add Items from Previous Invoice*,
  `eyssen_add_item_from_previous_invoice`): copies the product lines (product, quantity, unit price)
  of another invoice of the same type. Select the :guilabel:`Previous Invoice` and the :guilabel:`If
  Product Duplication` behavior, then click :guilabel:`Add`.
- Barcode scanning (*eYssen Barcode Invoice*, `eyssen_barcode_invoice`): scanning a product
  barcode adds the product to the invoice with a quantity of 1; if the product is already on the
  invoice, its quantity is increased.
- Copy line values (*Copying Invoice rows values*, `eyssen_copy_invoice_row_value`): enable the
  :icon:`fa-files-o` toggle above the lines to display copy buttons next to the
  :guilabel:`Product`, :guilabel:`Account`, :guilabel:`Analytic Distribution`, :guilabel:`Taxes` and
  :guilabel:`Disc.%` columns. Clicking a copy button on a line sets the same value on all the other
  product lines of the invoice (after confirmation).
- Quantity totals (*Add Quantity Total for Invoice*, `eyssen_quantity_total_invoice`): the totals
  block of the invoice displays the number of product and service types and the total quantity per
  unit of measure (:guilabel:`Sum Qty (detailed)`). The :guilabel:`Sum Qty` column is also available
  in the list of invoices.

.. note::
   Except for the quantity totals and the copy buttons, these tools require the Hungarian
   localization module (*Magyar számlázás és NAV adatszolgáltatás*, `eyssen_l10n_hu`), which
   provides the toolbar above the invoice lines.

.. screenshot:: accounting-invoice-line-tools
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (open a draft invoice)
   :shows: Draft invoice, "Invoice Lines" tab: the toolbar above the lines with the "Add Products from Delivery Notes" button (left) and the barcode, "Add Previous Items" and "Add Bulk Products" icon buttons and the copy toggle (right); the copy buttons are visible next to the Product, Account and Taxes columns; the totals block shows the quantity totals.
   :highlight: The toolbar buttons and the quantity totals (red frames).
   :data: Demo company "YourCompany HU"; draft invoice with three product lines.
   :module: eyssen_l10n_hu, eyssen_stock_picking_invoice, eyssen_product_bulk_add_invoice, eyssen_add_item_from_previous_invoice, eyssen_barcode_invoice, eyssen_copy_invoice_row_value, eyssen_quantity_total_invoice
   :notes: English UI, light theme, 1440px width.

.. _accounting/invoice/pricelist:

Pricelist on invoices
---------------------

With the *Account - Pricelist on Invoices* (`account_invoice_pricelist`) module, invoices have a
:guilabel:`Pricelist` field, filled in with the customer's pricelist. The pricelist is used to
compute the unit prices of the lines added manually to the invoice. If the pricelist is changed on a
draft invoice, click :guilabel:`Update Prices` to recompute the prices of the existing lines.
Invoices can also be grouped by :guilabel:`Pricelist` in the list view.

With the *Account Invoice Pricelist - Sale* (`account_invoice_pricelist_sale`) module, invoices
created from sales orders use the pricelist of the sales order.

.. note::
   The :guilabel:`Pricelist` field is only visible if pricelists are enabled in the Sales settings.

.. _accounting/invoice/comments:

Document comments
-----------------

With the *Account Comments* (`account_comment_template`) module, comments can be printed above or
below the invoice lines:

#. Go to :menuselection:`Accounting --> Configuration --> Management --> Document Comments` and
   create a comment template: enter a name, the :guilabel:`Template` text, the :guilabel:`Position
   on document` (:guilabel:`Top` or :guilabel:`Bottom`), the models (e.g., invoices), and
   optionally a :guilabel:`Company`, a :guilabel:`Partner`, and a :guilabel:`Filter Domain` to
   restrict where the template is available.
#. On the invoice, open the :guilabel:`Comments` tab and add the comment templates to print.

.. tip::
   The template text can contain dynamic placeholders, such as `{{object.partner_id.name}}`.

.. screenshot:: accounting-invoice-comment-template
   :menu: Accounting ‣ Configuration ‣ Management ‣ Document Comments ‣ New
   :shows: Comment template form with a name, the template text, position "Bottom", model "Journal Entry" and an empty domain.
   :highlight: The "Position on document" field (red frame).
   :data: Template "Reverse charge notice".
   :module: account_comment_template, base_comment_template
   :notes: English UI, light theme, 1440px width.

.. tip::
   To display the total amount of the invoice in words, go to :menuselection:`Accounting -->
   Configuration --> Settings` and activate the :guilabel:`Total amount of invoice in letters`
   option.

The :guilabel:`Journal Items` tab displays the accounting entries created. Additional invoice
information such as the :guilabel:`Customer Reference`, :guilabel:`Payment Reference`, :doc:`Fiscal
Positions <taxes/fiscal_positions>`, :doc:`Incoterms <customer_invoices/incoterms>`, and more can be
added or modified in the :guilabel:`Other Info` tab.

.. note::
   Odoo initially creates invoices in :guilabel:`Draft` status. Draft invoices have no accounting
   impact until they are :ref:`confirmed <accounting/invoice/confirmation>`.

.. seealso::
   :doc:`/applications/sales/sales/invoicing/proforma`

.. _accounting/invoice/confirmation:

Invoice confirmation
====================

Click :guilabel:`Confirm` when the invoice is completed. The invoice's status changes to
:guilabel:`Posted`, and a journal entry is generated based on the invoice configuration. On
confirmation, Odoo assigns each invoice a unique number from a defined :doc:`sequence
<customer_invoices/sequence>`.

.. note::
   - Once confirmed, an invoice can no longer be updated. Click :guilabel:`Reset to draft` if
     changes are needed.
   - If required, invoices and other journal entries can be locked once posted using the
     :ref:`Secure posted entries with hash <data-inalterability/restricted>` feature.
   - If an :doc:`approval rule <customer_invoices/invoice_approval>` applies to the invoice, it must
     be approved before it can be confirmed.

.. _accounting/invoice/edit-posted:

Correcting posted entries (administrators)
------------------------------------------

The *Invoice Fixer* (`invoice_fixer`) module adds an :guilabel:`Edit Posted Move` button to posted
journal entries, visible only to users with the :guilabel:`Administration: Settings` access right.
The :guilabel:`Edit Posted Move` window allows the administrator to:

- modify the :guilabel:`Debit`, :guilabel:`Credit`, :guilabel:`Quantity` and :guilabel:`Unit
  Price` of the existing lines (:guilabel:`Lines` tab);
- change the :guilabel:`Exchange Rate` of a foreign currency document;
- add new product lines with their :guilabel:`Product`, :guilabel:`Description`,
  :guilabel:`Quantity`, :guilabel:`Unit Price`, :guilabel:`Taxes` and :guilabel:`Account`
  (:guilabel:`Add New Lines` tab).

Click :guilabel:`Apply Changes` to save. The document totals are recomputed, and the changes are
logged in the chatter.

.. danger::
   The changes are written directly into the database, without resetting the document to draft and
   bypassing the usual checks (e.g., lock dates, entry hashing, electronic invoicing). Use this tool
   only to correct technical errors, and preferably with the help of your accountant: legally, a
   posted invoice must be corrected with a credit note.

.. screenshot:: accounting-invoice-edit-posted-move
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (open a posted invoice) ‣ Edit Posted Move
   :shows: "Edit Posted Move" dialog with the invoice reference, the "Lines" tab listing the journal items with editable Debit, Credit, Quantity and Unit Price columns, the "Add New Lines" tab, and the "Apply Changes" button.
   :highlight: The editable columns and the "Apply Changes" button (red frames).
   :data: Demo company "YourCompany HU"; posted invoice with two lines; administrator user.
   :module: invoice_fixer
   :notes: English UI, light theme, crop to the dialog.

.. _accounting/invoice/sending:

Invoice sending
===============

To set a preferred :guilabel:`Invoice sending` method for a customer, go to
:menuselection:`Accounting --> Customers --> Customers` and select the customer. In the
:guilabel:`Accounting` tab of the contact form (:guilabel:`Invoicing` tab if only the Invoicing app
is installed), select the preferred :guilabel:`Invoice sending`
method in the :guilabel:`Customer Invoices` section.

.. note::
   Sending letters in Odoo requires :doc:`In-App Purchase (IAP) <../../essentials/in_app_purchase>`
   credit or tokens.

To send the invoice to the customer, navigate back to the invoice record and follow these steps:

#. Click :guilabel:`Send`.
#. If the default invoice layout has not been customized
   yet, a :guilabel:`Configure your document layout` pop-up window appears. Configure the layout and
   click :guilabel:`Continue`.

   .. note::
      - The document layout can be changed at any time in the general settings.
      - To add a QR code for banking app payments to the invoice, enable the :guilabel:`QR Code`
        option in the :guilabel:`Configure Your Document Layout` window. To modify this option, go
        to :menuselection:`Accounting --> Configuration --> Settings`, scroll down to the
        :guilabel:`Customer Payments` section, and enable/disable the :guilabel:`QR Codes` option.

#. In the :guilabel:`Send` window:

   - If a preferred :guilabel:`Invoice sending` method was set in the contact form, it is selected
     by default. Select another one if needed.
   - If no preferred :guilabel:`Invoice sending` method was set in the contact form, select the
     method to use for sending the invoice to the customer.

#. Click :guilabel:`Send` if the :guilabel:`by Email` option is selected, or click
   :guilabel:`Download`.

.. _accounting/invoice/sending-multiple-invoices:

Sending multiple invoices
-------------------------

To send and print multiple invoices, go to :menuselection:`Accounting --> Customers --> Invoices`,
select them in the :guilabel:`Invoices` list view and click :guilabel:`Send`. The
:guilabel:`Send` window displays the selected invoice sending methods based on the preferred
method set.

A banner is added to the selected invoices to indicate they are part of an ongoing send and print
batch. This helps prevent the process from being triggered manually again, as it may take some time
to complete for exceptionally large batches.

To check all invoices that have not yet been sent, go to :menuselection:`Accounting --> Customers
--> Invoices`. In the :guilabel:`Invoices` list view, click into the search bar and filter on
:guilabel:`Not Sent`.

.. _accounting/invoice/paymentandreconciliation:

Payment and reconciliation
==========================

In Odoo, an invoice is considered :guilabel:`Paid` when the associated accounting entry has been
reconciled with a corresponding bank transaction.

.. seealso::
   - :doc:`payments`
   - :doc:`bank/reconciliation`

.. _accounting/invoice/followup:

Payment follow-up
=================

Odoo's :doc:`follow-up actions <payments/follow_up>` help companies follow up on customer invoices.
Different actions can be set up to remind customers to pay their outstanding invoices, depending on
how much the customer is overdue. These actions are bundled into follow-up levels that trigger when
an invoice is overdue by a certain number of days. If there are multiple overdue invoices for the
same customer, the actions are performed on the most overdue invoice.

.. _accounting/invoice/reporting:

Reporting
=========

.. _accounting/invoice/partner-reports:

Partner reports
---------------

.. _accounting/invoices/partner-ledger:

Partner Ledger
~~~~~~~~~~~~~~

The :guilabel:`Partner Ledger` report shows the balance of customers and suppliers. To access it,
go to :menuselection:`Accounting --> Accounting --> Ledgers --> Partner Ledger` (PDF report) or
:menuselection:`Accounting --> Reporting --> Dynamic Reports --> Partner Ledger` (interactive
report).

.. _accounting/invoices/aging-report:

Aged Receivable
~~~~~~~~~~~~~~~

To review outstanding customer invoices and their related due dates, use the :ref:`Aged Receivable
<accounting/reporting/aged-receivable>` report. To access it, go to :menuselection:`Accounting -->
Reporting --> Dynamic Reports --> Aged Receivable`, or use the :menuselection:`Accounting -->
Reporting --> Partner Reports --> Aged Partner Balance` PDF report.

.. _accounting/invoices/aged-payable:

Aged Payable
~~~~~~~~~~~~

To review outstanding vendor bills and their related due dates, use the :ref:`Aged Payable
<accounting/reporting/aged-payable>` report. To access it, go to :menuselection:`Accounting -->
Reporting --> Dynamic Reports --> Aged Payable`, or use the :menuselection:`Accounting -->
Reporting --> Partner Reports --> Aged Partner Balance` PDF report.

.. _accounting/invoices/profit-and-loss:

Profit and Loss
---------------

The :ref:`Profit and Loss <accounting/reporting/profit-and-loss>` statement shows details of income
and expenses.

.. _accounting/invoices/balance-sheet:

Balance sheet
-------------

The :ref:`Balance Sheet <accounting/reporting/balance-sheet>` summarizes the company's assets,
liabilities, and equity at a specific time.

.. toctree::
   :titlesonly:

   customer_invoices/overview
   customer_invoices/invoice_approval
   customer_invoices/invoice_from_delivery_notes
   customer_invoices/customer_addresses
   customer_invoices/payment_terms
   customer_invoices/terms_conditions
   customer_invoices/cash_discounts
   customer_invoices/credit_notes
   customer_invoices/cash_rounding
   customer_invoices/deferred_revenues
   customer_invoices/electronic_invoicing
   customer_invoices/sequence
   customer_invoices/snailmail
   customer_invoices/epc_qr_code
   customer_invoices/incoterms

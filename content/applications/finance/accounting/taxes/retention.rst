=================
Withholding taxes
=================

A **withholding tax**, also known as retention tax, mandates the payer of a customer invoice to
deduct a tax from the payment and remit it to the government. Typically, a tax is included in the
subtotal to calculate the total amount paid, while withholding taxes are directly subtracted from
the payment.

Configuration
=============

In Odoo, a withholding tax is defined by creating a negative tax. To create one, go
to :menuselection:`Accounting --> Configuration --> Taxes` and, in the :guilabel:`Amount` field,
enter a negative amount.

.. screenshot:: accounting-taxes-retention-negative-amount
   :menu: Accounting ‣ Configuration ‣ Taxes ‣ New
   :shows: Tax form of a withholding tax: Tax Computation "Percentage", Tax Type "Sales", Amount "-10.00 %".
   :highlight: The "Amount" field (red frame).
   :data: Tax "Retention 10%".
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the upper part of the form.

Then, go to the :guilabel:`Advanced Options` tab and create a retention :guilabel:`Tax Group`.

.. screenshot:: accounting-taxes-retention-tax-group
   :menu: Accounting ‣ Configuration ‣ Taxes ‣ (open the withholding tax) ‣ Advanced Options tab
   :shows: "Advanced Options" tab with the "Tax Group" field set to a "Retention" tax group.
   :highlight: The "Tax Group" field (red frame).
   :data: Tax "Retention 10%"; tax group "Retention".
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the tab.

.. tip::
   If the retention is a percentage of a regular tax, create a :guilabel:`Tax` with a
   :guilabel:`Tax Computation` as a :guilabel:`Group of Taxes`. Then, set both the regular tax and
   the retention one in the :guilabel:`Definition` tab.

Retention taxes on invoices
===========================

Once the retention tax has been created, it can be used on customer forms, sales orders, and
customer invoices.
Several taxes can be applied on a single customer invoice line.

.. screenshot:: accounting-taxes-retention-invoice
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (open a draft invoice)
   :shows: Invoice line with two taxes (a regular VAT and "Retention 10%"); the totals block shows the VAT and the negative retention amount.
   :highlight: The line's Taxes field and the totals block (red frames).
   :data: Demo customer; taxes "21%" and "Retention 10%".
   :module: account
   :notes: English UI, light theme, 1440px width.

.. seealso::

   :doc:`../taxes`

============
EPC QR codes
============

European Payments Council quick response codes, or **EPC QR codes**, are two-dimensional barcodes
that customers can scan with their **mobile banking applications** to initiate a **SEPA credit
transfer (SCT)** and pay their invoices instantly.

In addition to bringing ease of use and speed, it greatly reduces typing errors that would
potentially make for payment issues.

.. note::
   This feature is only available for companies in several European countries such as Austria,
   Belgium, Finland, Germany, and the Netherlands.

.. seealso::
   - :doc:`../bank`

Configuration
=============

Go to :menuselection:`Accounting --> Configuration --> Settings` and activate the :guilabel:`QR
Codes` feature in the :guilabel:`Customer Payments` section.

Configure your bank account's journal
-------------------------------------

Make sure that your :guilabel:`Bank Account` is correctly configured in Odoo with your IBAN and BIC.

To do so, go to :menuselection:`Accounting --> Configuration --> Journals`, open your bank journal,
then fill out the :guilabel:`Account Number` and :guilabel:`Bank` under the :guilabel:`Bank Account
Number` column.

.. screenshot:: accounting-epc-qr-code-bank-journal
   :menu: Accounting ‣ Configuration ‣ Journals ‣ (open the bank journal)
   :shows: Bank journal form with the "Account Number" (IBAN) and "Bank" fields filled in.
   :highlight: The "Account Number" and "Bank" fields (red frame).
   :data: Belgian demo company; bank journal with an IBAN.
   :module: account
   :notes: English UI, light theme, 1440px width.

Issue invoices with EPC QR codes
================================

EPC QR codes are added automatically to your invoices. Customers whose bank supports making payments
via EPC QR codes will be able to scan the code and pay the invoice.

Go to :menuselection:`Accounting --> Customers --> Invoices`, and create a new invoice.

Before posting it, open the :guilabel:`Other Info` tab. Odoo automatically fills out the
:guilabel:`Recipient Bank` field with your IBAN.

.. note::
   In the :guilabel:`Other Info` tab, the account indicated in the :guilabel:`Recipient Bank` field
   is used to receive your customer's payment. Odoo automatically populates this field with your
   IBAN by default and uses it to generate the EPC QR code.

When the invoice is printed or previewed, the QR code is included at the bottom.

.. screenshot:: accounting-epc-qr-code-invoice
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (open an invoice) ‣ Preview
   :shows: Invoice PDF with the EPC QR code and the payment communication at the bottom.
   :highlight: The QR code (red frame).
   :data: Belgian demo company; invoice in EUR; QR Codes setting enabled.
   :module: account_qr_code_sepa
   :notes: English UI, crop to the bottom of the invoice.

.. tip::
   If you want to issue an invoice without an EPC QR code, remove the IBAN indicated in the
   :guilabel:`Recipient Bank` field, under the :guilabel:`Other Info` tab of the invoice.

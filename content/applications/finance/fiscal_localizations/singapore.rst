=========
Singapore
=========

Add PayNow QR codes to invoices
===============================

PayNow is a payment service platform that allows customers to make instant domestic payments to
individuals and merchants in Singapore dollars via online and mobile banking.

Activate QR codes
-----------------

Go to :menuselection:`Accounting --> Configuration --> Settings`. Under the :guilabel:`Customer
Payments` section, activate the :guilabel:`QR Codes` feature.

PayNow bank account configuration
---------------------------------

Go to :menuselection:`Contacts --> Configuration --> Bank Accounts` and select the bank account to
activate PayNow. Set the :guilabel:`Proxy Type` and fill in the :guilabel:`Proxy Value` field
depending on the chosen type.

.. important::
   - The account holder's country must be set to `Singapore` on its contact form.
   - The account holder's city is mandatory.
   - You could also include the invoice number in the QR code by checking the :guilabel:`Include
     Reference` checkbox.

.. screenshot:: finance-fl-singapore-sg-paynow-bank-setting
   :menu: Contacts ‣ Configuration ‣ Bank Accounts ‣ (the bank account)
   :shows: A bank account form with "Proxy Type" set to a PayNow type (e.g. "UEN") and the "Proxy Value" filled in, "Include Reference" ticked.
   :highlight: The "Proxy Type" and "Proxy Value" fields.
   :data: Demo company "YourCompany SG", Singapore localization installed.
   :module: l10n_sg, account_qr_code_emv
   :notes: English UI, light theme, 1440px width.

.. seealso::
   :doc:`../accounting/bank`

Bank journal configuration
--------------------------

Go to :menuselection:`Accounting --> Configuration --> Journals`, open the bank journal, then fill
out the :guilabel:`Account Number` and :guilabel:`Bank` under the :guilabel:`Journal Entries` tab.

.. screenshot:: finance-fl-singapore-sg-bank-account-journal-setting
   :menu: Accounting ‣ Configuration ‣ Journals ‣ Bank ‣ Journal Entries tab
   :shows: The Journal Entries tab of the Bank journal with the "Account Number" and "Bank" fields filled in.
   :highlight: The "Account Number" and "Bank" fields.
   :data: Demo company "YourCompany SG".
   :module: account
   :notes: English UI, light theme, 1440px width.

Issue invoices with PayNow QR codes
-----------------------------------

When creating a new invoice, open the :guilabel:`Other Info` tab and set the :guilabel:`Payment
QR-code` option to *EMV Merchant-Presented QR-code*.

.. screenshot:: finance-fl-singapore-sg-qr-code-invoice-setting
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (an invoice) ‣ Other Info tab
   :shows: The Other Info tab of a customer invoice with the "Payment QR-code" drop-down set to "EMV Merchant-Presented QR-code".
   :highlight: The "Payment QR-code" field.
   :data: Demo company "YourCompany SG".
   :module: account_qr_code_emv
   :notes: English UI, light theme, 1440px width.

Ensure that the :guilabel:`Recipient Bank` is the one you configured, as Odoo uses this field to
generate the PayNow QR code.


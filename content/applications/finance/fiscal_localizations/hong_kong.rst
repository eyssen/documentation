=========
Hong Kong
=========

Configuration
=============

:ref:`Install <general/install>` the following modules to get the latest features of the Hong Kong
localization:

.. list-table::
   :header-rows: 1

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Hong Kong - Accounting`
     - `l10n_hk`
     - The base module to manage chart of accounting and localization for Hong Kong.

.. note::
   The Hong Kong payroll (including the IR56 forms) is **not** available in this edition.

FPS QR codes on invoices
========================

:abbr:`FPS (Faster Payment System)` is a payment service platform that allows customers to make
instant domestic payments to individuals and merchants in Hong Kong dollars or Renminbi via online
and mobile banking.

Activate QR codes
-----------------

Go to :menuselection:`Accounting app --> Configuration --> Settings`. Under the :guilabel:`Customer
Payments` section, tick the checkbox beside the :guilabel:`QR Codes` feature. Then, click
:guilabel:`Save`.

FPS bank account configuration
------------------------------

Go to :menuselection:`Contacts app --> Configuration --> Bank Accounts section --> Bank Accounts`.
Then select the bank account for FPS activation. Proceed to set the :guilabel:`Proxy Type` and fill
in the :guilabel:`Proxy Value` field, depending on the type chosen.

Remember to include the invoice number in the QR code, by ticking the :guilabel:`Include Reference`
checkbox.

.. screenshot:: finance-fl-hong-kong-hk-fps-bank-setting
   :menu: Contacts ‣ Configuration ‣ Bank Accounts ‣ (the FPS bank account)
   :shows: A bank account form with the "Proxy Type" field set to an FPS type (e.g. "FPS ID") and the "Proxy Value" filled in, plus the "Include Reference" checkbox ticked.
   :highlight: The "Proxy Type", "Proxy Value" and "Include Reference" fields.
   :data: Demo company "YourCompany HK", Hong Kong localization installed. Account holder in Hong Kong.
   :module: l10n_hk, account_qr_code_emv
   :notes: English UI, light theme, 1440px width.

.. important::
   - The account holder's country must be set to `Hong Kong` on its contact form.
   - The account holder's city is mandatory.
   - You could also include the invoice number in the QR code by checking the :guilabel:`Include
     Reference` checkbox.

.. seealso::
   :doc:`../accounting/bank`

Bank journal configuration
--------------------------

Go to :menuselection:`Accounting app --> Configuration --> Journals` and open the bank journal.
Then, fill out the :guilabel:`Account Number` and :guilabel:`Bank` fields, located in the
:guilabel:`Journal Entries` tab.

.. screenshot:: finance-fl-hong-kong-hk-bank-account-journal-setting
   :menu: Accounting ‣ Configuration ‣ Journals ‣ Bank ‣ Journal Entries tab
   :shows: The Journal Entries tab of the Bank journal with the "Account Number" and "Bank" fields filled in.
   :highlight: The "Account Number" and "Bank" fields.
   :data: Demo company "YourCompany HK", Hong Kong localization installed.
   :module: account
   :notes: English UI, light theme, 1440px width.

Issue invoices with FPS QR codes
--------------------------------

When creating a new invoice, open the :guilabel:`Other Info` tab and set the :guilabel:`Payment
QR-code` option to :guilabel:`EMV Merchant-Presented QR-code`.

.. screenshot:: finance-fl-hong-kong-hk-qr-code-invoice-setting
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (an invoice) ‣ Other Info tab
   :shows: The Other Info tab of a customer invoice with the "Payment QR-code" drop-down set to "EMV Merchant-Presented QR-code".
   :highlight: The "Payment QR-code" field.
   :data: Demo company "YourCompany HK", Hong Kong localization installed.
   :module: account_qr_code_emv
   :notes: English UI, light theme, 1440px width.

Ensure that the :guilabel:`Recipient Bank` is configured, as Odoo uses this field to generate the
FPS QR code.

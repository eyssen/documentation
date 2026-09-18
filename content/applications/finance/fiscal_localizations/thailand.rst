========
Thailand
========

Configuration
=============

:ref:`Install <general/install>` the :guilabel:`🇹🇭 Thailand` localization package to get all the
features of the Thai localization:

.. list-table::
   :header-rows: 1

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Thailand - Accounting`
     - `l10n_th`
     - Default :ref:`fiscal localization package <fiscal_localizations/packages>`

.. note::
   The Thai country-specific reports (sales and purchase tax reports, withholding PND tax report)
   are **not** available in this edition; the VAT grids can be reviewed in the :doc:`tax report
   <../accounting/reporting/dynamic_reports>`.

Chart of accounts and taxes
===========================

Odoo's fiscal localization package for Thailand includes the following taxes:

- VAT 7%
- VAT-exempted
- Withholding tax
- Withholding income tax

Tax invoice
===========

The **tax invoice PDF** report can be generated from Odoo through the **Invoicing** module. Users
have the  option to print PDF reports for normal invoices and tax invoices. To print out
**tax invoices**, users can click on :guilabel:`Print Invoices` in Odoo. Regular invoices can be
printed as **commercial invoices** by clicking on :menuselection:`Cog button (⚙️) --> Print -->
Commercial Invoice`.

.. screenshot:: finance-fl-thailand-tax-invoice
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (a posted invoice) ‣ Print
   :shows: A posted customer invoice with the Print menu open, showing the "Invoices" (tax invoice) and "Commercial Invoice" report entries.
   :highlight: The "Commercial Invoice" entry.
   :data: Demo company "YourCompany TH", Thai localization installed.
   :module: l10n_th
   :notes: English UI, light theme, 1440px width.

Headquarter/Branch number settings
----------------------------------

You can inform a company's **Headquarters** and **Branch number** in the **Contacts** app. Once
in the app, open the **contact form** of the company and under the :guilabel:`Sales & Purchase` tab:

- If the contact is identified as a branch, input the **Branch number** in the
  :guilabel:`Company ID` field.
- If the contact is a **Headquarters**, leave the :guilabel:`Company ID` field **blank**.

.. screenshot:: finance-fl-thailand-contact
   :menu: Contacts ‣ (a Thai company contact) ‣ Sales & Purchase tab
   :shows: A company contact form with the "Company ID" field in the Sales & Purchase tab filled in with the branch number (e.g. 00001).
   :highlight: The "Company ID" field.
   :data: Contact "Bangkok Trading Co., Ltd.", branch 00001.
   :module: l10n_th
   :notes: English UI, light theme, 1440px width.

.. tip::
   This information is used in the **tax invoice** PDF report.

PromptPay QR code on invoices
=============================

The **PromptPay QR code** is a QR code that can be added to invoices to allow customers to pay their
bills using the PromptPay-supported bank mobile application. The QR code is generated based on the
**invoice amount** and one of the following **merchant information**:

- Ewallet ID
- Merchant Tax ID
- Mobile Number

Activate QR codes
-----------------

Go to :menuselection:`Accounting --> Configuration --> Settings`. Under the :guilabel:`Customer
Payments` section, activate the :guilabel:`QR Codes` feature.

PromptPay QR bank account configuration
---------------------------------------

Go to :menuselection:`Contacts --> Configuration --> Bank Accounts` and select the bank account for
which you want to activate PromptPay QR. Set the :guilabel:`Proxy Type` and fill in the
:guilabel:`Proxy Value` field depending on the chosen type.

.. important::
   - The account holder's city is mandatory.
   - The :guilabel:`Include Reference` checkbox doesn't work for PromptPay QR codes.

.. screenshot:: finance-fl-thailand-qr-promptpay-bank
   :menu: Contacts ‣ Configuration ‣ Bank Accounts ‣ (the bank account)
   :shows: A bank account form with "Proxy Type" set to a PromptPay type (e.g. "Mobile Number") and the "Proxy Value" filled in, "Include Reference" ticked.
   :highlight: The "Proxy Type" and "Proxy Value" fields.
   :data: Demo company "YourCompany TH".
   :module: l10n_th, account_qr_code_emv
   :notes: English UI, light theme, 1440px width.

.. seealso::
   :doc:`../accounting/bank`

Bank journal configuration
--------------------------

Go to :menuselection:`Accounting --> Configuration --> Journals`, open the bank journal, then fill
in the :guilabel:`Account Number` and :guilabel:`Bank` under the :guilabel:`Journal Entries` tab.

.. screenshot:: finance-fl-thailand-qr-bank-journal
   :menu: Accounting ‣ Configuration ‣ Journals ‣ Bank ‣ Journal Entries tab
   :shows: The Journal Entries tab of the Bank journal with the "Account Number" and "Bank" fields filled in.
   :highlight: The "Account Number" and "Bank" fields.
   :data: Demo company "YourCompany TH".
   :module: account
   :notes: English UI, light theme, 1440px width.

Issue invoices with PromptPay QR code
-------------------------------------

When creating a new invoice, open the :guilabel:`Other Info` tab and set the :guilabel:`Payment
QR-code` option to :guilabel:`EMV Merchant-Presented QR-code`.

.. screenshot:: finance-fl-thailand-qr-code-invoice-emv
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (an invoice) ‣ Other Info tab
   :shows: The Other Info tab of a customer invoice with the "Payment QR-code" drop-down set to "EMV Merchant-Presented QR-code".
   :highlight: The "Payment QR-code" field.
   :data: Demo company "YourCompany TH".
   :module: account_qr_code_emv
   :notes: English UI, light theme, 1440px width.

Ensure that the :guilabel:`Recipient Bank` is the one you configured, as Odoo uses this field to
generate the PromptPay QR code.

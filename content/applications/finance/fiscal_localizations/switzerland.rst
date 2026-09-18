===========
Switzerland
===========

Configuration
=============

Install the 🇨🇭 **Swiss** :ref:`fiscal localization package <fiscal_localizations/packages>`
(`l10n_ch`) to get the Swiss chart of accounts (*Käfer / KMU*), the VAT rates with their VAT-form
grids, the QR-bill printing and the QR reference numbers described below.

.. note::
   The Swiss VAT return export (*Switzerland - Accounting Reports*), the localized financial
   reports, the Swiss payroll (ELM transmission) and the Point of Sale extensions are **not**
   available in this edition. The VAT-form grids can be reviewed in the :doc:`tax report
   <../accounting/reporting/dynamic_reports>`.

QR-bill
=======

The QR-bill (*QR-Rechnung*) replaced the former ISR payment slips. Odoo prints a compliant QR-bill
(payment part and receipt) for customer invoices whose recipient bank account is a Swiss IBAN or
QR-IBAN, when the invoice currency is CHF or EUR and both the company and the customer have a
complete postal address.

Bank account
------------

Go to :menuselection:`Accounting --> Configuration --> Bank Accounts` (or open the bank journal)
and enter the company's account number. When the IBAN is a **QR-IBAN** (its IID, positions 5–9,
is between 30000 and 31999), the :guilabel:`QR-IBAN` field is filled in automatically and the
QR-bill uses a structured *QR reference* (QRR); with a regular IBAN, a *Creditor Reference*
(SCOR, ISO 11649) is used instead.

.. screenshot:: finance-fl-switzerland-qr-iban
   :menu: Accounting ‣ Configuration ‣ Bank Accounts ‣ (the company's account)
   :shows: The bank account form with a QR-IBAN entered as "Account Number" (CH44 3199 9123 0008 8901 2) and the computed "QR-IBAN" field filled in below it.
   :highlight: The "QR-IBAN" field.
   :data: Demo company "YourCompany CH", Swiss localization installed; a test QR-IBAN.
   :module: l10n_ch
   :notes: English UI, light theme, 1440px width.

QR reference on invoices
------------------------

To ease the reconciliation process, use the QR reference as **Payment Reference** on your invoices.
Go to :menuselection:`Accounting --> Configuration --> Journals`, open the journal you use to issue
invoices (by default *Customer Invoices*), open the :guilabel:`Advanced Settings` tab and set the
:guilabel:`Communication Standard` field to :guilabel:`Switzerland`. The payment reference of each
invoice is then a 27-digit QR reference computed from the invoice number (or from the customer
number when the reference is based on the customer), printed on the invoice and encoded in the QR
code.

.. screenshot:: finance-fl-switzerland-journal-communication
   :menu: Accounting ‣ Configuration ‣ Journals ‣ Customer Invoices ‣ Advanced Settings tab
   :shows: The Advanced Settings tab of the Customer Invoices journal with the "Communication Standard" drop-down set to "Switzerland".
   :highlight: The "Communication Standard" field.
   :data: Demo company "YourCompany CH".
   :module: l10n_ch
   :notes: English UI, light theme, 1440px width.

Printing the QR-bill
--------------------

On a posted customer invoice, set the :guilabel:`Payment QR-code` field of the :guilabel:`Other
Info` tab to :guilabel:`Swiss QR bill`, then click :menuselection:`Print --> QR-bill`: the payment
part and receipt are added on a separate page of the invoice PDF. Several invoices can be printed
at once from the list view with the same menu; invoices that cannot be printed as QR-bills (wrong
currency, missing address, non-Swiss account) are listed in the :guilabel:`QR printing encountered
a problem` window, from which you can :guilabel:`Print All` valid ones.

.. screenshot:: finance-fl-switzerland-qr-bill-pdf
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (a posted invoice) ‣ Print ‣ QR-bill
   :shows: The QR-bill page of an invoice PDF: the receipt part on the left and the payment part with the Swiss QR code, creditor, reference and amount on the right.
   :highlight: The QR code.
   :data: Invoice INV/2025/00005 for a Swiss customer, 1,250.00 CHF, QR reference.
   :module: l10n_ch
   :notes: English UI, light theme, A4 PDF page.

Vendor payments
---------------

When registering a payment to a vendor whose bank account is a QR-IBAN, the payment must carry a
valid QR reference in the :guilabel:`Payment Reference` field; a warning is displayed on the payment
form otherwise, since banks refuse such payment files.

Currency rate update
====================

Currency rates can be updated automatically with the *eYssen currency rate updater* module (see
:ref:`multi-currency/config-rates-auto`); the Swiss Federal Tax Administration is not among its
providers, so the rates come from a generic provider (e.g., the ECB or xe.com) or must be entered
manually.

Taxes
=====

The Swiss VAT rates in force (8.1 % normal rate, 2.6 % reduced rate, 3.8 % special rate for
accommodation since 1 January 2024) are created by the localization, both as *included* and
*excluded* variants for sales and purchases, and mapped to the grids of the Swiss VAT form
(grids 302, 312, 342, 400, 405, …). When rates change, the new taxes are added by a module update;
archive the old ones and update your fiscal positions and default taxes accordingly.

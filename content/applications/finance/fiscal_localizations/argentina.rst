=========
Argentina
=========

Configuration
=============

Modules installation
--------------------

:ref:`Install <general/install>` the following modules to get all the features of the Argentinean
localization:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Argentina - Accounting`
     - `l10n_ar`
     - Default :ref:`fiscal localization package <fiscal_localizations/packages>`, which represents
       the minimal configuration to operate in Argentina under the :abbr:`AFIP (Administración
       Federal de Ingresos Públicos)` regulations and guidelines.
   * - :ref:`Argentinean eCommerce <argentina/ecommerce-electronic-invoicing>`
     - `l10n_ar_website_sale`
     - (optional) Allows the user to see Identification Type and AFIP Responsibility in the
       eCommerce checkout form in order to create invoices with the correct document type.
   * - :ref:`Argentina - Payment Withholdings <l10n_ar/payment-withholdings>`
     - `l10n_ar_withholding`
     - Allows registering withholdings during the payment of an invoice.

.. note::
   Electronic invoicing through the AFIP web services (CAE request, *Consult Invoice* in AFIP,
   vendor bill validation in AFIP, Electronic Fiscal Bond, FCE MiPyME, liquidity product direct
   sales) and the Argentinean VAT Book / VAT summary / IIBB reports are **not** available in this
   edition. Invoices are numbered and printed by Odoo with the AFIP document types, and the
   authorization (CAE) must be obtained outside Odoo when required.

.. _argentina/configure-your-company:

Configure your company
----------------------

Once the localization modules are installed, the first step is to set up the company's data. In
addition to the basic information, a key field to fill in is the :guilabel:`AFIP Responsibility
Type`, which represents the fiscal obligation and structure of the company.

.. screenshot:: finance-fl-argentina-select-responsibility-type
   :menu: Settings ‣ Users & Companies ‣ Companies ‣ (your company)
   :shows: The company form with the "AFIP Responsibility Type" field (Argentinean localization) set to "IVA Responsable Inscripto", next to the VAT (CUIT) and "Gross Income" fields.
   :highlight: The "AFIP Responsibility Type" field.
   :data: Demo company "YourCompany AR" (Responsable Inscripto), Argentinean localization installed.
   :module: l10n_ar
   :notes: English UI, light theme, 1440px width.

Chart of account
----------------

In Accounting, there are three different :guilabel:`Chart of Accounts` packages to choose from.
They are based on a company's AFIP responsibility type, and consider the difference between
companies that do not require as many accounts as the companies that have more complex fiscal
requirements:

- Monotributista (227 accounts);
- IVA Exento (290 accounts);
- Responsable Inscripto (298 Accounts).

.. screenshot:: finance-fl-argentina-select-fiscal-package
   :menu: Accounting ‣ Configuration ‣ Settings
   :shows: The "Fiscal Localization" block of the Accounting settings with the "Package" field drop-down open, showing the three Argentinean packages: Responsable Inscripto, Exento, Monotributista.
   :highlight: The "Package" drop-down.
   :data: Demo company "YourCompany AR" (Responsable Inscripto), Argentinean localization installed.
   :module: l10n_ar
   :notes: English UI, light theme, 1440px width.

Configure master data
---------------------

Partner
~~~~~~~

Identification type and VAT
***************************

As part of the Argentinean localization, document types defined by the AFIP are now available in the
**Partner form**. Information is essential for most transactions. There are six
:guilabel:`Identification Types` available by default, as well as 32 inactive types.

.. screenshot:: finance-fl-argentina-identification-types
   :menu: Accounting ‣ Configuration ‣ Identification Types
   :shows: The Identification Types list with the archived types shown (filter "Archived" active): the 6 active AFIP types (e.g. CUIT, CUIL, DNI, Pasaporte, Sigd, Foreign ID) and the inactive ones.
   :highlight: The active/inactive toggle column.
   :data: Demo company "YourCompany AR" (Responsable Inscripto), Argentinean localization installed.
   :module: l10n_ar, l10n_latam_base
   :notes: English UI, light theme, 1440px width.

.. note::
   The complete list of :guilabel:`Identification Types` defined by the AFIP is included in Odoo,
   but only the common ones are active.

AFIP responsibility type
************************

In Argentina, the document type and corresponding transactions associated with customers and
vendors is defined by the AFIP Responsibility type. This field should be defined in the **Partner
form**.

.. screenshot:: finance-fl-argentina-select-afip-responsibility-type
   :menu: Contacts ‣ (a partner) ‣ Sales & Purchase tab
   :shows: A partner form with the "AFIP Responsibility Type" drop-down open listing the responsibility types (IVA Responsable Inscripto, IVA Sujeto Exento, Consumidor Final, Responsable Monotributo, Cliente / Proveedor del Exterior, …).
   :highlight: The "AFIP Responsibility Type" field.
   :data: Partner "Deco Addict AR", identification type CUIT.
   :module: l10n_ar
   :notes: English UI, light theme, 1440px width.

Taxes
~~~~~

As part of the localization module, the taxes are created automatically with their related
financial account and configuration, e.g., 73 taxes for :guilabel:`Responsable Inscripto`.

.. screenshot:: finance-fl-argentina-automatic-tax-configuration
   :menu: Accounting ‣ Configuration ‣ Taxes
   :shows: The Taxes list of the Argentinean localization: Tax Name, Tax Type, Tax Scope and Label on Invoices columns, showing the IVA 21%, IVA 10.5%, IVA 27%, Percepción and Retención taxes.
   :data: Demo company "YourCompany AR" (Responsable Inscripto), Argentinean localization installed.
   :module: l10n_ar
   :notes: English UI, light theme, 1440px width.

Taxes types
***********

Argentina has several tax types, the most common ones are:

- :guilabel:`VAT`: this is the regular VAT and can have various percentages;
- :guilabel:`Perception`: advance payment of a tax that is applied on invoices;
- :guilabel:`Retention`: advance payment of a tax that is applied on payments.

Special taxes
*************

Some Argentinean taxes are not commonly used for all companies, and those less common options are
labeled as inactive in Odoo by default. Before creating a new tax, be sure to check if that tax is
not already included as inactive.

.. screenshot:: finance-fl-argentina-special-inactive-taxes
   :menu: Accounting ‣ Configuration ‣ Taxes ‣ Filters ‣ Archived
   :shows: The Taxes list with the "Archived" filter, showing the less common Argentinean taxes that are inactive by default (e.g. provincial Percepción IIBB taxes, Impuestos Internos).
   :highlight: The "Archived" filter chip.
   :data: Demo company "YourCompany AR" (Responsable Inscripto), Argentinean localization installed.
   :module: l10n_ar
   :notes: English UI, light theme, 1440px width.

.. _document-types:

Document types
~~~~~~~~~~~~~~

In some Latin American countries, like Argentina, some accounting transactions such as invoices and
vendor bills are classified by document types defined by the governmental fiscal authorities. In
Argentina, the `AFIP <https://www.afip.gob.ar/>`__ is the governmental fiscal authority that
defines such transactions.

The document type is an essential piece of information that needs to be clearly displayed in
printed reports, invoices, and journal entries that list account moves.

Each document type can have a unique sequence per journal where it is assigned. As part of the
localization, the document type includes the country in which the document is applicable (this data
is created automatically when the localization module is installed).

The information required for the :guilabel:`Document Types` is included by default so the user does
not need to fill anything on this view:

.. screenshot:: finance-fl-argentina-default-document-type-info
   :menu: Accounting ‣ Configuration ‣ Document Types
   :shows: The Document Types list of the Argentinean localization: Name, Doc Code Prefix, Country, Internal Type, Letter and AFIP code columns (e.g. Factura A / FA-A / 1, Nota de Crédito A / NC-A / 3).
   :data: Demo company "YourCompany AR" (Responsable Inscripto), Argentinean localization installed.
   :module: l10n_ar, l10n_latam_invoice_document
   :notes: English UI, light theme, 1440px width.

.. note::
   There are several :guilabel:`Document Types` types that are inactive by default, but can be
   activated as needed.

Letters
*******

For Argentina, the :guilabel:`Document Types` include a letter that helps indicate the type of
transaction or operation. For example, when an invoice is related to a(n):

- :guilabel:`B2B transaction`, a document type :guilabel:`A` must be used;
- :guilabel:`B2C transaction`, a document type :guilabel:`B` must be used;
- :guilabel:`Exportation Transaction`, a document type :guilabel:`E` must be used.

The documents included in the localization already have the proper letter associated with each
:guilabel:`Document Type`, so there is no further configuration necessary.

.. screenshot:: finance-fl-argentina-document-types-grouped-by-letters
   :menu: Accounting ‣ Configuration ‣ Document Types ‣ Group By ‣ Letter
   :shows: The Document Types list grouped by "Letter" (A, B, C, E, M …) with the groups expanded.
   :highlight: The group headers.
   :data: Demo company "YourCompany AR" (Responsable Inscripto), Argentinean localization installed.
   :module: l10n_ar
   :notes: English UI, light theme, 1440px width.

Use on invoices
***************

The :guilabel:`Document Type` on each transaction will be determined by:

- The journal entry related to the invoice (if the journal uses documents);
- The onditions applied based on the type of issuer and receiver (e.g., the type of fiscal regime of
  the buyer and the type of fiscal regime of the vendor).

Journals
--------

In the Argentinean localization, the journal can have a different approach depending on its usage
and internal type. To configure journals, go to :menuselection:`Accounting --> Configuration -->
Journals`.

For sales and purchase journals, it's possible to activate the option :guilabel:`Use Documents`,
which enables a list of :guilabel:`Document Types` that can be related to the invoices and vendor
bills. For more detail on invoices, please refer to the section :ref:`2.3 document types
<document-types>`.

If the sales or purchase journals do not have the :guilabel:`Use Documents` option activated, they
will not be able to generate fiscal invoices, meaning, their use case will be mostly limited to
monitoring account moves related to internal control processes.

AFIP information (also known as AFIP Point of Sale)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :guilabel:`AFIP POS System` is a field only visible for the **Sales** journals and defines the
type of AFIP POS that will be used to manage the transactions for which the journal is created.

The AFIP POS defines the following:

#. the document types that can be used in the journal;
#. the sequences of those document types (prefix = the AFIP POS number).

The available :guilabel:`AFIP POS System` values are :guilabel:`Pre-printed Invoice`,
:guilabel:`Online Invoice`, :guilabel:`Electronic Fiscal Bond - Online Invoice`, :guilabel:`Export
Voucher - Billing Plus`, :guilabel:`Export Voucher - Online Invoice`, and :guilabel:`Product Coding
- Online Voucher`. They correspond to the invoicing systems registered in the AFIP for the POS
(pre-printed forms or the AFIP online invoicing portal); Odoo does **not** call the AFIP web
services itself.

.. screenshot:: finance-fl-argentina-sales-journal
   :menu: Accounting ‣ Configuration ‣ Journals ‣ (a sales journal)
   :shows: A Sales journal form for Argentina with the "Use Documents?" checkbox, the "AFIP POS System" field (drop-down open: Pre-printed Invoice, Online Invoice, Electronic Fiscal Bond - Online Invoice, Export Voucher - Billing Plus, Export Voucher - Online Invoice, Product Coding - Online Voucher), "AFIP POS Number" and "AFIP POS Address".
   :highlight: The "AFIP POS System" field.
   :data: Journal "Ventas Preimpreso", AFIP POS Number 1.
   :module: l10n_ar
   :notes: English UI, light theme, 1440px width.

Here are some useful fields to know when working with AFIP POS journals:

- :guilabel:`AFIP POS Number`: is the number configured in the AFIP to identify the operations
  related to this AFIP POS (5 digits maximum);
- :guilabel:`AFIP POS Address`: is the field related to the commercial address registered for the
  POS, which is usually the same address as the company. For example, if a company has multiple
  stores (fiscal locations) then the AFIP will require the company to have one AFIP POS per
  location. This location will be printed in the invoice report.

Sequences
~~~~~~~~~

Each document type used in a journal has its own sequence; the document number is built as
*AFIP POS number - sequence* (e.g. `0001-00000002`). When posting the first invoice of a document
type, the number can be edited to continue the numbering already used in the AFIP.

.. note::
   When creating :guilabel:`Purchase Journals`, it's possible to define whether they are related to
   document types or not. In the case where the option to use documents is selected, there would be
   no need to manually associate the document type sequences, since the document number is provided
   by the vendor.

Usage and testing
=================

Invoice
-------

The information below applies to invoice creation once the partners and journals are created and
properly configured.

Document type assignation
~~~~~~~~~~~~~~~~~~~~~~~~~

When the partner is selected, the :guilabel:`Document Type` field will be filled in automatically
based on the AFIP document type:

- **Invoice for a customer IVA Responsable Inscripto, prefix A** is the type of document that shows
  all the taxes in detail along with the customer's information.

  .. screenshot:: finance-fl-argentina-prefix-a-invoice-for-customer
     :menu: Accounting ‣ Customers ‣ Invoices ‣ (a posted invoice)
     :shows: A posted customer invoice for a partner with AFIP responsibility "IVA Responsable Inscripto": the "Document Type" field shows "(1) Factura A" and the number FA-A 00001-00000001; taxes listed separately in the totals.
     :highlight: The "Document Type" field and the invoice number.
     :data: Customer "Deco Addict AR" (Responsable Inscripto).
     :module: l10n_ar
     :notes: English UI, light theme, 1440px width.

- **Invoice for an end customer, prefix B** is the type of document that does not detail the taxes,
  since the taxes are included in the total amount.

  .. screenshot:: finance-fl-argentina-prefix-b-invoice-for-end-customer
     :menu: Accounting ‣ Customers ‣ Invoices ‣ (a posted invoice)
     :shows: A posted customer invoice for a "Consumidor Final" partner: "Document Type" = "(6) Factura B", number FA-B 00001-00000001, taxes included in the line prices and totals.
     :highlight: The "Document Type" field.
     :data: Customer "Consumidor Final".
     :module: l10n_ar
     :notes: English UI, light theme, 1440px width.

- **Exportation Invoice, prefix E** is the type of document used when exporting goods that shows
  the incoterm.

  .. screenshot:: finance-fl-argentina-prefix-e-exporation-invoice
     :menu: Accounting ‣ Customers ‣ Invoices ‣ (a posted export invoice)
     :shows: A posted export invoice for a foreign customer: "Document Type" = "(19) Factura de Exportación E", number FA-E 00002-00000001, and the "Incoterm" field visible in the Other Info tab.
     :highlight: The "Document Type" field.
     :data: Customer "Foreign Customer Inc." (Cliente / Proveedor del Exterior).
     :module: l10n_ar
     :notes: English UI, light theme, 1440px width.

Even though some invoices use the same journal, the prefix and sequence are given by the
:guilabel:`Document Type` field.

The most common :guilabel:`Document Type` will be defined automatically for the different
combinations of AFIP responsibility type but it can be updated manually by the user before
confirming the invoice.

Invoice taxes
~~~~~~~~~~~~~

Based on the :guilabel:`AFIP Responsibility type`, the VAT tax can apply differently on the PDF
report:

- :guilabel:`A. Tax excluded`: in this case the taxed amount needs to be clearly identified in the
  report. This condition applies when the customer has the following AFIP Responsibility type of
  **Responsable Inscripto**;

  .. screenshot:: finance-fl-argentina-tax-amount-excluded
     :menu: Accounting ‣ Customers ‣ Invoices ‣ (a Factura A) ‣ Print
     :shows: The PDF of a Factura A: the lines show the untaxed unit price and the IVA 21% tax is listed as a separate amount in the totals block.
     :highlight: The tax lines in the totals block.
     :data: Customer Responsable Inscripto, one product line 1,000.00 + IVA 21%.
     :module: l10n_ar
     :notes: English UI, light theme, 1440px width.

- :guilabel:`B. Tax amount included`: this means that the taxed amount is included as part of the
  product price, subtotal, and totals. This condition applies when the customer has the following
  AFIP Responsibility types:

  - IVA Sujeto Exento;
  - Consumidor Final;
  - Responsable Monotributo;
  - IVA liberado.

  .. screenshot:: finance-fl-argentina-tax-amount-included
     :menu: Accounting ‣ Customers ‣ Invoices ‣ (a Factura B) ‣ Print
     :shows: The PDF of a Factura B: the line prices, subtotal and total include the IVA; no separate tax line is shown.
     :highlight: The totals block.
     :data: Customer Consumidor Final, one product line 1,210.00 tax included.
     :module: l10n_ar
     :notes: English UI, light theme, 1440px width.

Special use cases
~~~~~~~~~~~~~~~~~

Invoices for services
*********************

For invoices that include :guilabel:`Services` (the :guilabel:`AFIP Concept` is *Services* or
*Products and Services*), the AFIP requires to report the service starting and ending date; this
information can be filled in the :guilabel:`AFIP Service Start Date` and :guilabel:`AFIP Service
End Date` fields of the :guilabel:`Other Info` tab.

.. screenshot:: finance-fl-argentina-invoices-for-services
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (an invoice) ‣ Other Info tab
   :shows: The Other Info tab of a customer invoice for a service product: the "AFIP Concept" field shows "Services" and the "AFIP Service Start Date" / "AFIP Service End Date" fields are visible.
   :highlight: The "AFIP Service Start Date" and "AFIP Service End Date" fields.
   :data: Invoice with a service line "Consulting".
   :module: l10n_ar
   :notes: English UI, light theme, 1440px width.

If the dates are not selected manually before the invoice is validated, the values will be filled
automatically with the first and last day of the invoice's month.

.. screenshot:: finance-fl-argentina-service-dates
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (a posted service invoice) ‣ Other Info tab
   :shows: The same Other Info tab after posting: the AFIP Service Start/End dates filled automatically with the first and last day of the invoice month.
   :highlight: The two date fields.
   :data: Invoice date 2025-03-15 → service dates 2025-03-01 and 2025-03-31.
   :module: l10n_ar
   :notes: English UI, light theme, 1440px width.

Exportation invoices
********************

Invoices related to :guilabel:`Exportation Transactions` require that a journal uses an
exportation AFIP POS System (:guilabel:`Export Voucher - Online Invoice` or :guilabel:`Export
Voucher - Billing Plus`) so that the proper document type(s) can be associated.

.. screenshot:: finance-fl-argentina-exporation-journal
   :menu: Accounting ‣ Configuration ‣ Journals ‣ (export sales journal)
   :shows: A sales journal configured for exports: "AFIP POS System" = "Export Voucher - Online Invoice", "AFIP POS Number" 2, "Use Documents?" enabled.
   :highlight: The "AFIP POS System" field.
   :data: Journal "Ventas Exportación".
   :module: l10n_ar
   :notes: English UI, light theme, 1440px width.

When the customer selected in the invoice is configured with an AFIP responsibility type
:guilabel:`Cliente / Proveedor del Exterior` - :guilabel:`Ley N° 19.640`, Odoo automatically
assigns the:

- Journal related to the exportation AFIP POS;
- Exportation document type;
- Fiscal position: Compras/Ventas al exterior;
- Concepto AFIP: Products / Definitive export of goods;
- Exempt Taxes.

.. screenshot:: finance-fl-argentina-export-invoice
   :menu: Accounting ‣ Customers ‣ Invoices ‣ New (foreign customer)
   :shows: A new customer invoice for a partner with AFIP responsibility "Cliente / Proveedor del Exterior": journal, document type "Factura de Exportación E", fiscal position "Compras/Ventas al exterior", AFIP Concept "Products / Definitive export of goods" and exempt taxes filled automatically.
   :highlight: The "Journal", "Document Type" and "Fiscal Position" fields.
   :data: Customer "Foreign Customer Inc.".
   :module: l10n_ar
   :notes: English UI, light theme, 1440px width.

.. note::
   The Exportation Documents require Incoterms to be enabled and configured, which can be found in
   :menuselection:`Other Info --> Accounting`.

.. screenshot:: finance-fl-argentina-export-invoice-incoterm
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (export invoice) ‣ Other Info tab
   :shows: The Other Info tab of an export invoice with the "Incoterm" field set (e.g. FOB) in the Accounting section.
   :highlight: The "Incoterm" field.
   :data: Incoterm "FOB – FREE ON BOARD".
   :module: l10n_ar, account
   :notes: English UI, light theme, 1440px width.

Vendor bills
------------

Based on the purchase journal selected for the vendor bill, the :guilabel:`Document Type` is now a
required field. This value is auto-populated based on the AFIP Responsibility type of Issuer and
Customer, but the value can be changed if necessary.

.. screenshot:: finance-fl-argentina-changing-journal-document-type
   :menu: Accounting ‣ Vendors ‣ Bills ‣ New
   :shows: A new vendor bill with the "Journal" drop-down (purchase journals using documents) and the required "Document Type" field auto-filled from the vendor's AFIP responsibility type.
   :highlight: The "Journal" and "Document Type" fields.
   :data: Vendor "Proveedor SA" (Responsable Inscripto), document type Factura A.
   :module: l10n_ar
   :notes: English UI, light theme, 1440px width.

The :guilabel:`Document Number` field needs to be registered manually and the format will be
validated automatically. However, in case the format is invalid, a user error will be displayed
indicating the correct format that is expected.

.. screenshot:: finance-fl-argentina-vendor-bill-document-number
   :menu: Accounting ‣ Vendors ‣ Bills ‣ New
   :shows: A vendor bill with the "Document Number" field filled in as 00001-00000045 and, in a second state, the validation error pop-up shown when an invalid format is typed.
   :highlight: The "Document Number" field.
   :data: Vendor "Proveedor SA".
   :module: l10n_ar
   :notes: English UI, light theme, 1440px width.

The vendor bill number is structured in the same way as the customer invoices, excepted that the
document sequence is entered by the user using the following format: *Document Prefix - Letter -
Document Number*.

Special use cases
~~~~~~~~~~~~~~~~~

Untaxed concepts
****************

There are some transactions that include items that are not a part of the VAT base amount, such as
fuel and gasoline invoices.

The vendor bill will be registered using one item for each product that is part of the VAT base
amount, and an additional item to register the amount of the exempt concept.

.. screenshot:: finance-fl-argentina-vat-exempt
   :menu: Accounting ‣ Vendors ‣ Bills ‣ (a fuel bill)
   :shows: A vendor bill with two lines: the fuel product with IVA 21% and an additional line "Concepto no gravado" with the tax "IVA No Gravado", so the exempt amount is excluded from the VAT base.
   :highlight: The second, untaxed line.
   :data: Bill for fuel 10,000.00 + untaxed concept 500.00.
   :module: l10n_ar
   :notes: English UI, light theme, 1440px width.

Perception taxes
****************

The vendor bill will be registered using one item for each product that is part of the VAT base
amount, and the perception tax can be added in any of the product lines. As a result, there will be
one tax group for the VAT and another for the perception. The perception default value is always
:guilabel:`0.10`.

To edit the VAT perception and set the correct amount, you should use the :guilabel:`Pencil` icon
that is the next to the :guilabel:`Perception` amount. After the VAT perception amount has been set,
the invoice can then be validated.

.. screenshot:: finance-fl-argentina-enter-perception-amount
   :menu: Accounting ‣ Vendors ‣ Bills ‣ (a bill with perception)
   :shows: A vendor bill whose totals block shows a "Percepción IIBB" tax line; the perception amount is entered manually by clicking the tax amount in the totals.
   :highlight: The editable perception tax amount in the totals.
   :data: Bill 10,000.00 + IVA 21% + Percepción IIBB Buenos Aires 300.00.
   :module: l10n_ar
   :notes: English UI, light theme, 1440px width.

.. _l10n_ar/payment-withholdings:

Withholding management
----------------------

The Argentinean fiscal localization module is already loaded with the necessary withholdings
records, which can be seen by navigating to :menuselection:`Accounting app --> Configuration -->
Taxes` and removing the default :guilabel:`Sale or Purchase` filter. To verify these records, the
**Argentina Payment Withholdings** (`l10n_ar_withholding`) module must be :ref:`installed
<general/install>`:

Journal entries are *not* created when payments are posted unless :ref:`outstanding accounts
<accounting/journals/outstanding-accounts>` are set up. Thus, for this feature to work properly, it
is important to verify that *all* payment methods within the bank journals have an outstanding
payment and receipt account set.

.. screenshot:: finance-fl-argentina-l10n-ar-outstanding-payments
   :menu: Accounting ‣ Configuration ‣ Journals ‣ (bank journal) ‣ Incoming/Outgoing Payments tabs
   :shows: The Outgoing Payments tab of a bank journal with the "Outstanding Payments accounts" column filled for each payment method line (Manual, Checks) and, in the Incoming Payments tab, the "Outstanding Receipts accounts".
   :highlight: The outstanding account columns.
   :data: Journal "Banco Galicia".
   :module: l10n_ar_withholding, account
   :notes: English UI, light theme, 1440px width.

This configuration is crucial for the proper accounting of withholding transactions with clients
and vendors.

.. note::
   In Argentina, withholdings represent the cancellation of a specific portion of the total debt
   owed to a supplier or a reduction in the total payment to be collected from a customer.
   Therefore, one or multiple withholdings can be recorded for each payment applied to an invoice.

Configuration
~~~~~~~~~~~~~

While Odoo already creates most of the required withholdings inside the :guilabel:`Taxes`
menu, in several cases, it is necessary to apply or modify certain configurations to correctly
calculate the withholding amount on vendor payments. The following withholding types are available:

- :ref:`Earnings <l10n_ar/earnings-withholdings>`
- :ref:`Earnings Scale <l10n_ar/earnings-scale-withholdings>`
- :ref:`IIBB Total Amount <l10n_ar/iib-total-amount-withholdings>`
- :ref:`IIBB Non-Taxable <l10n_ar/iib-nontax-withholdings>`

.. _l10n_ar/earnings-withholdings:

Earnings
********

For :guilabel:`Earnings` withholdings, Odoo already has a record for each regime group, which is
stated under the name of the tax and the AFIP code.

Each of these records are ready to be used. As a good practice, the configuration should be double
checked to make sure the configuration is updated and well-applied. The fields to validate are:

- :guilabel:`Amount`: This is the percentage of the total payment amount which is withheld.
- :guilabel:`Non-Taxable Amount`: Up to this amount, the withholding does not apply.
- :guilabel:`Minimum Withholding`: If the calculated withholding amount is smaller than this value,
  the total withholding amount is set to `0.0`.
- :guilabel:`Withholding Sequence`: This field helps to automate the capture of a withholding number
  under the payment line. If this field is not set, a number is manually captured while adding a
  withholding to a payment.

.. screenshot:: finance-fl-argentina-l10n-ar-earnings
   :menu: Accounting ‣ Configuration ‣ Taxes ‣ (a withholding tax)
   :shows: A withholding tax form ("Retención Ganancias …") of type "Purchase" with the Advanced Options tab showing the "Withholding" fields: Withholding Type (Earnings), Withholding Sequence, Minimum Threshold, and the earnings scale fields.
   :highlight: The "Withholding Type" field.
   :data: Tax "Retención Ganancias - Servicios".
   :module: l10n_ar_withholding
   :notes: English UI, light theme, 1440px width.

.. _l10n_ar/earnings-scale-withholdings:

Earnings Scale
**************

In this particular case, a percentage does not need to be set. Instead, this withholding is
calculated based on the value of the :guilabel:`Scale` field.

To view, modify, or create new scales, navigate to :menuselection:`Accounting app --> Configuration
--> Earnings Scale`. By default, the Argentinian localization is preconfigured with two main scales.
However, scales should be created and updated as necessary to suit a business's needs.

.. note::
   Earnings scales are cumulative, which means that Odoo keeps track of the different records
   created for a bill and automatically calculates the proper withholding amount.

.. _l10n_ar/iib-total-amount-withholdings:

IIBB Total Amount
*****************

In this case, the necessary records related to the applicable province need to be created. The
withholding amount is calculated based on the percentage :guilabel:`Amount` set on the tax
configuration. Since Odoo does not automatically synchronize the percentages applicable to each
province, this information needs to be manually updated.

The recommendation, in this case, is to always duplicate and apply the different configurations for
each record to safeguard any technical configurations that allow the proper calculation and
accounting of the withholding.

.. _l10n_ar/iib-nontax-withholdings:

IIBB Untaxed
************

The configuration of non-taxable gross income withholdings is very similar to that of a :ref:`total
amount withholding <l10n_ar/iib-total-amount-withholdings>`, so the percentage :guilabel:`Amount` in
each of the records needs to be maintained. However, Odoo comes preconfigured with several records
that apply to different provinces. The difference, in this case, is that it is not necessary to
establish a non-taxable amount or minimum withholding for this record type.

Partner withholding assignation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the proper configuration is set on each possible withholding for partners, the applicable
withholdings need to be assigned to each contact. To do this, open the :guilabel:`Contacts` app and
select the desired partner. In the :guilabel:`Accounting` tab, find the :guilabel:`Purchase
Withholdings` table.

By using the additional fields :guilabel:`From Date` and :guilabel:`To Date`, the applicability of
multiple withholdings can be automated across different date ranges. The :guilabel:`ref` field
allows you to apply an internal control number to each withholding line, which is just for internal
reference, so it does not affect any transactions and is not visible on them. These fields are
accessible from the :icon:`oi-settings-adjust` :guilabel:`(adjust settings)` menu.

- :guilabel:`From Date`: the start of the withholding date range.
- :guilabel:`To Date`: the end of the withholding date range.
- :guilabel:`ref`: apply an internal control number to each withholding line that is only visible
  for internal reference and does not affect any transactions.

Automatic withholding calculation and application per payment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By applying new payments to vendor bills, Odoo automatically applies and calculates the proper
withholding into the payment. Based on the record's configuration, it may be necessary to use a
reference number for each withholding line.

More withholdings can be added, or computed withholdings can be edited if necessary.

.. screenshot:: finance-fl-argentina-l10n-ar-payment
   :menu: Accounting ‣ Vendors ‣ Bills ‣ (a bill) ‣ Register Payment
   :shows: The "Register Payment" pop-up for a vendor bill with the "Withholdings" table listing the automatically computed withholding lines (tax, base amount, withholding amount, reference) and the resulting net amount.
   :highlight: The "Withholdings" table.
   :data: Vendor "Proveedor SA"; Retención Ganancias and Retención IIBB lines.
   :module: l10n_ar_withholding
   :notes: English UI, light theme, 1440px width.

.. important::
   The total amount of the debt to be canceled is the total amount of the payment. However, Odoo
   still captures the net amount (i.e. the amount to be reconciled with the bank), which will be
   represented as the payment amount after the withholding application.

   .. screenshot:: finance-fl-argentina-l10n-ar-payment-registered
      :menu: Accounting ‣ Vendors ‣ Payments ‣ (a payment with withholdings)
      :shows: A posted vendor payment form showing the payment amount (net) and, in the "Withholdings" tab, the withholding lines with their numbers; the total debt cancelled appears in the journal entry.
      :highlight: The "Withholdings" tab.
      :data: Payment for "Proveedor SA".
      :module: l10n_ar_withholding
      :notes: English UI, light theme, 1440px width.

Check management
----------------

To install the *Third Party and Deferred/Electronic Checks Management* module, go to
:menuselection:`Apps` and search for the module by its technical name `l10n_latam_check` and click
the :guilabel:`Activate` button.

.. screenshot:: finance-fl-argentina-l10n-latam-check-module
   :menu: Apps
   :shows: The Apps list filtered on "check", showing the "Third Party and Deferred/Electronic Checks Management" (l10n_latam_check) module with its Install/Installed button.
   :highlight: The l10n_latam_check module card.
   :module: l10n_latam_check
   :notes: English UI, light theme, 1440px width.

This module enables the required configuration for journals and payments to:

- Create, manage, and control your different types of checks
- Optimize the management of *own checks* and *third party checks*
- Have an easy and effective way to manage expiration dates from your own and third party checks

Once all the configurations are made for the Argentinian invoicing flow, it is also needed
to complete certain configurations for the own checks and the third party checks flows.

Own checks
~~~~~~~~~~

Configure the bank journal used to create your own checks by going to :menuselection:`Accounting -->
Configuration --> Journals`, selecting the bank journal, and opening the :guilabel:`Outgoing
Payments` tab.

- :guilabel:`Checks` should be available as a :guilabel:`Payment Method`. If not, click
  :guilabel:`Add a line` and type `Checks` under :guilabel:`Payment Method` to add them
- Enable the :guilabel:`Use electronic and deferred checks` setting.

.. note::
   This last configuration **disables** the printing ability but enables to:

   - Enter check numbers manually
   - Adds a field to allocate the payment date of the check

.. screenshot:: finance-fl-argentina-bank-journal-conf
   :menu: Accounting ‣ Configuration ‣ Journals ‣ (bank journal) ‣ Outgoing Payments tab
   :shows: The Outgoing Payments tab of a bank journal with the "Checks" payment method line added and the "Use electronic and deferred checks" checkbox enabled.
   :highlight: The "Use electronic and deferred checks" checkbox.
   :data: Journal "Banco Galicia".
   :module: l10n_latam_check
   :notes: English UI, light theme, 1440px width.

Management of own checks
************************

Own checks can be created directly from the vendor bill. For this process, click on the
:guilabel:`Register Payment` button.

On the payment registration modal, select the bank journal from which the payment is to be made and
set the :guilabel:`Check Cash-In Date`, and the :guilabel:`Amount`.

.. screenshot:: finance-fl-argentina-payment-popup-vendorbill
   :menu: Accounting ‣ Vendors ‣ Bills ‣ (a bill) ‣ Register Payment
   :shows: The "Register Payment" pop-up with Payment Method "Checks" selected on the bank journal, showing the "Check Number", "Check Cash-In Date" and "Amount" fields.
   :highlight: The "Check Cash-In Date" field.
   :data: Vendor "Proveedor SA", check number 1001, cash-in date next month.
   :module: l10n_latam_check
   :notes: English UI, light theme, 1440px width.

.. note::
   To manage current checks, the :guilabel:`Check Cash-In Date` field must be left blank or filled
   in with the current date. To manage deferred checks, the :guilabel:`Check Cash-In Date` must be
   set in the future.

To manage your existing own checks, navigate to :menuselection:`Accounting --> Vendors --> Own
Checks`. This window shows critical information such as the dates when checks need to be paid, the
total quantity of checks, and the total amount paid in checks.

.. screenshot:: finance-fl-argentina-checks-menu-vendorbill
   :menu: Accounting ‣ Vendors ‣ Own Checks
   :shows: The Accounting app with the Vendors menu open, highlighting the "Own Checks" menu item.
   :highlight: The "Own Checks" menu entry.
   :module: l10n_latam_check
   :notes: English UI, light theme, 1440px width.

It is important to note that the list is pre-filtered by checks that are still *not reconciled* with
a bank statement - that were not yet debited from the bank - which can be verified with the
:guilabel:`Is Matched with a Bank Statement` field. If you want to see all of your own checks,
delete the :guilabel:`No Bank Matching` filter by clicking on the :guilabel:`X` symbol.

.. screenshot:: finance-fl-argentina-check-menu-list-vendorbill
   :menu: Accounting ‣ Vendors ‣ Own Checks
   :shows: The Own Checks list with the default "No Bank Matching" filter: columns Check Number, Check Cash-In Date, Partner, Journal, Amount and "Is Matched with a Bank Statement"; totals row at the bottom.
   :highlight: The "No Bank Matching" filter chip.
   :data: Three own checks, one already matched.
   :module: l10n_latam_check
   :notes: English UI, light theme, 1440px width.

Cancel an own check
*******************

To cancel an own check created in Odoo, navigate to :menuselection:`Accounting --> Vendors --> Own
Checks` and select the check to be cancelled, then click on the :guilabel:`Void Check` button. This
will break the reconciliation with the vendor bills and the bank statements and leave the check in a
**cancelled** state.

.. screenshot:: finance-fl-argentina-empty-check-button
   :menu: Accounting ‣ Vendors ‣ Own Checks ‣ (a check)
   :shows: A posted own-check payment form with the "Void Check" button in the header.
   :highlight: The "Void Check" button.
   :data: Check number 1001.
   :module: l10n_latam_check
   :notes: English UI, light theme, 1440px width.

Third party checks
~~~~~~~~~~~~~~~~~~

In order to register payments using third party checks, two specific journals need to be configured.
To do so, navigate to :menuselection:`Accounting --> Configuration --> Journals` and create two new
journals:

- `Third Party Checks`
- `Rejected Third Party Checks`

.. note::
   You can manually create more journals if you have multiple points of sale and need journals for
   those.

To create the *Third Party Checks* journal, click the :guilabel:`New` button and configure the
following:

- Type `Third Party Checks` as the :guilabel:`Journal Name`
- Select :guilabel:`Cash` as :guilabel:`Type`
- In the :guilabel:`Journal Entries` tab, set :guilabel:`Cash Account`: to `1.1.1.02.010 Cheques de
  Terceros`, input a :guilabel:`Short Code` of your choice, and select a :guilabel:`Currency`

.. screenshot:: finance-fl-argentina-auto-cash-account
   :menu: Accounting ‣ Configuration ‣ Journals ‣ (third party checks journal)
   :shows: The automatically created "Third Party Checks" cash journal form with its default account "Third Party Checks" (Bank and Cash account type).
   :highlight: The "Default Account" field.
   :module: l10n_latam_check
   :notes: English UI, light theme, 1440px width.

The available payment methods are listed in the *payments* tabs:

- For new incoming third party checks, go to :menuselection:`Incoming Payments tab --> Add a line`
  and select :guilabel:`New Third Party Checks`. This method is used to create *new* third party
  checks.
- For incoming and outgoing existing third party checks, go to :menuselection:`Incoming Payments tab
  --> Add a line` and select :guilabel:`Existing Third Party Checks`. Repeat the same step for the
  :guilabel:`Outgoing Payments` tab. This method is used to receive and/or pay vendor bills using
  already *existing* checks, as well as for internal transfers.

.. tip::
   You can delete pre-existing payment methods appearing by default when configuring the third
   party checks journals.

.. screenshot:: finance-fl-argentina-auto-payment-methods
   :menu: Accounting ‣ Configuration ‣ Journals ‣ (third party checks journal) ‣ Incoming Payments tab
   :shows: The Incoming and Outgoing Payments tabs of the Third Party Checks journal with the automatically created payment method lines: "New Third Party Checks", "Existing Third Party Checks".
   :highlight: The payment method lines.
   :module: l10n_latam_check
   :notes: English UI, light theme, 1440px width.

The *Rejected Third Party Checks* journal also needs to be created and/or configured. This journal
is used to manage rejected third party checks and can be utilized to send checks rejected at the
moment of collection or when coming from vendors when rejected.

To create the *Rejected Third Party Checks* journal, click the :guilabel:`New` button and configure
the following:

- Type `Rejected Third Party Checks` as the :guilabel:`Journal Name`
- Select :guilabel:`Cash` as :guilabel:`Type`
- In the :guilabel:`Journal Entries` tab, set :guilabel:`Cash Account`: to `1.1.1.01.002 Rejected
  Third Party Checks`, input a :guilabel:`Short Code` of your choice, and select a
  :guilabel:`Currency`

Use the same payment methods as the *Third Party Checks* journal.

New third party checks
**********************

To register a *new* third party check for a customer invoice, click the :guilabel:`Register Payment`
button. In the pop-up window, you must select :guilabel:`Third Party Checks` as journal for the
payment registration.

Select :guilabel:`New Third Party Checks` as :guilabel:`Payment Method`, and fill in the
:guilabel:`Check Number`, :guilabel:`Payment Date`, and :guilabel:`Check Bank`. Optionally, you can
manually add the :guilabel:`Check Issuer Vat`, but this is automatically filled by the customer's
VAT number related to the invoice.

.. screenshot:: finance-fl-argentina-third-party-payment-popup
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (an invoice) ‣ Register Payment
   :shows: The "Register Payment" pop-up with the Third Party Checks journal and the "New Third Party Checks" payment method: fields Check Number, Check Cash-In Date, Check Issuer VAT, Check Issuer Name, Check Bank and Amount.
   :highlight: The "New Third Party Checks" method and the check fields.
   :data: Customer "Deco Addict AR", check from Banco Nación.
   :module: l10n_latam_check
   :notes: English UI, light theme, 1440px width.

Existing third party checks
***************************

To pay a vendor bill with an *existing* check, click the :guilabel:`Register Payment` button. In the
pop-up window, you must select :guilabel:`Third Party Checks` as journal for the payment
registration.

Select :guilabel:`Existing Third Party Checks` as :guilabel:`Payment Method`, and select a check
from the :guilabel:`Check` field. The field shows all **available existing checks** to be used as
payment for vendor bills.

.. screenshot:: finance-fl-argentina-existing-third-party-popup
   :menu: Accounting ‣ Vendors ‣ Bills ‣ (a bill) ‣ Register Payment
   :shows: The "Register Payment" pop-up with the Third Party Checks journal and the "Existing Third Party Checks" payment method: the "Check" many2one selecting a check in portfolio and the amount filled automatically.
   :highlight: The "Check" field.
   :data: Vendor "Proveedor SA", check 4521 in portfolio.
   :module: l10n_latam_check
   :notes: English UI, light theme, 1440px width.

When an **existing third party check** is used, you can review the operations related to it. For
example, you can see if a third party check made to pay a customer invoice was later used as an
existing third party check to pay a vendor bill.

To do so, either go to :menuselection:`Accounting --> Customers --> Third Party Checks` or
:menuselection:`Accounting --> Vendors --> Own Checks` depending on the case, and click on a check.
In the :guilabel:`Check Current Journal` field, click on :guilabel:`=> Check Operations` to bring up
the check's history and movements.

.. screenshot:: finance-fl-argentina-check-operations-menulist
   :menu: Accounting ‣ Customers ‣ Third Party Checks
   :shows: The Third Party Checks list with the "Check Operations" action menu open, listing the available operations (deposit, transfer, return, …).
   :highlight: The "Check Operations" menu.
   :module: l10n_latam_check
   :notes: English UI, light theme, 1440px width.

The menu also displays critical information related to these operations, such as:

- The :guilabel:`Payment Type`, allowing to classify whether it is a payment *sent* to a vendor or a
  payment *received* from a customer
- The :guilabel:`Journal` in which the check is currently registered
- The **partner** associated with the operation (either customer or vendor).

.. _argentina/ecommerce-electronic-invoicing:

Ecommerce invoicing
-------------------

:ref:`Install <general/install>` the *Argentinian eCommerce* (`l10n_ar_website_sale`) module to
enable the following features and configurations:

- Clients being able to create online accounts for eCommerce purposes.
- Support for required fiscal fields in the eCommerce application.
- Receive payments for sale orders online.
- Generate invoices with the correct document type from the eCommerce application.

Configuration
~~~~~~~~~~~~~

Once all of the configurations are made for the Argentinian :ref:`invoicing
<argentina/configure-your-company>` flow, it is also necessary to complete certain configurations to
integrate the eCommerce flow.

Client account registration
***************************

To configure your website for client accounts, follow the instructions in the :doc:`checkout
<../../websites/ecommerce/checkout>` documentation.

Automatic invoice
*****************

Configure your website to generate invoices in the sales process by navigating to
:menuselection:`Website --> Configuration --> Settings` and activating the :guilabel:`Automatic
Invoice` feature in the :guilabel:`Invoicing` section to automatically generate the required
documents when the online payment is confirmed.

.. screenshot:: finance-fl-argentina-l10nar-automatic-invoicing-ecommerce
   :menu: Website ‣ Configuration ‣ Settings
   :shows: The Website settings scrolled to the "Invoicing" section with the "Automatic Invoice" checkbox enabled.
   :highlight: The "Automatic Invoice" checkbox.
   :module: website_sale, l10n_ar_website_sale
   :notes: English UI, light theme, 1440px width.

Since an online payment needs to be confirmed for the :guilabel:`Automatic Invoice` feature to
generate the document, a :doc:`payment provider <../payment_providers>` **must** be configured for
the related website.

Products
********

To allow your products to be invoiced when an online payment is confirmed, navigate to the desired
product from :menuselection:`Website --> eCommerce --> Products`. In the :guilabel:`General
Information` tab, set the :guilabel:`Invoicing Policy` to :guilabel:`Ordered quantities` and define
the desired :guilabel:`Customer Taxes`.

Invoicing flow for eCommerce
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the configurations mentioned above are all set, clients can complete the following required
steps in the *Argentinian eCommerce* flow to input fiscal fields in the checkout process.

Fiscal fields are available for input in the checkout process once the :guilabel:`Country` field is
set as `Argentina`. Inputting the fiscal data enables the purchase to conclude in the corresponding
document type.

.. screenshot:: finance-fl-argentina-l10nar-fiscal-fields-ar-ecommerce
   :menu: (website) ‣ Shop ‣ Checkout ‣ Address
   :shows: The eCommerce checkout address form with Country = Argentina, showing the additional required fields "Identification Type", "Identification Number" and "AFIP Responsibility Type".
   :highlight: The three Argentinean fiscal fields.
   :data: Country Argentina, Identification Type CUIT.
   :module: l10n_ar_website_sale
   :notes: English UI, light theme, 1440px width.

When the client makes a successful purchase and payment, the necessary invoice is generated with
the corresponding document type and layout.

.. seealso::
   :doc:`Client account creation <../../websites/ecommerce/checkout>`

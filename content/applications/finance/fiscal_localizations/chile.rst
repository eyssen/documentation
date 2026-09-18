=====
Chile
=====

.. _chile/configuration:

Modules
=======

:ref:`Install <general/install>` the following modules to utilize all the features of the Chilean
localization.

.. list-table::
   :header-rows: 1

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Chile - Accounting`
     - `l10n_cl`
     - Adds the minimal accounting features required for a company to operate in Chile under the
       :abbr:`SII (Servicio de Impuestos Internos)` regulations and guidelines.

.. note::
   - Odoo automatically installs the appropriate package for the company according to the country
     selected at the creation of the database.
   - Electronic invoicing with the :abbr:`SII (Servicio de Impuestos Internos)` (DTE emission and
     reception, CAF folios, electronic receipts, delivery guides, electronic exports, the
     eCommerce and Point of Sale electronic documents) and the *Propuesta F29* / *Balance
     Tributario (8 columnas)* reports are **not** available in this edition. Documents are numbered
     with the SII document types and printed by Odoo; the electronic documents must be issued
     through the SII portal (*Facturación MiPyme*) or another certified system.

Company information
===================

Navigate to :menuselection:`Settings --> Companies: Update Info` and ensure the following company
information is up-to-date and correctly filled in:

- :guilabel:`Company Name`
- :guilabel:`Address`:

  - :guilabel:`Street`
  - :guilabel:`City`
  - :guilabel:`State`
  - :guilabel:`ZIP`
  - :guilabel:`Country`

- :guilabel:`Tax ID`: enter the company's RUT; the :guilabel:`Identification Number` type must be
  :guilabel:`RUT`.
- :guilabel:`Company Activity Description`: enter a short description of the company's activity.

.. _chile/fiscal-info:

Fiscal information
==================

On the company's partner record (:menuselection:`Contacts --> (your company)`), select the
:guilabel:`Taxpayer Type` that applies:

- :guilabel:`VAT Affected (1st Category)`: for invoices that charge taxes to customers
- :guilabel:`Fees Receipt Issuer (2nd category)`: for suppliers who issue fees receipt (Boleta)
- :guilabel:`End Consumer`: only issues receipts
- :guilabel:`Foreigner`

The taxpayer type of the company and of the partner determine which document types can be used on
an invoice or bill.

Multicurrency
=============

Currency rates can be updated automatically with the *eYssen currency rate updater* module (see
:ref:`multi-currency/config-rates-auto`); the Chilean central bank / mindicador.cl service is not
among its providers, so the rates come from a generic provider (e.g., xe.com) or must be entered
manually.

.. _chile/partner-information:

Partner information
===================

Open the :menuselection:`Contacts` app and fill in the following fields on a new or existing
contact form so that the right document type is proposed on invoices and bills:

- :guilabel:`Name`
- :guilabel:`Email`
- :guilabel:`Identification Number` (type :guilabel:`RUT` for Chilean companies) and the number
- :guilabel:`Taxpayer Type`
- :guilabel:`Activity Description`

.. screenshot:: finance-fl-chile-partner-fields
   :menu: Contacts ‣ (a Chilean customer) ‣ Sales & Purchase tab
   :shows: A contact form for a Chilean company with the Identification Number type "RUT" and number, and in the Sales & Purchase tab the "Taxpayer Type" (VAT Affected (1st Category)) and "Activity Description" fields.
   :highlight: The "Taxpayer Type" and "Activity Description" fields.
   :data: Contact "Comercial Ejemplo SpA", RUT 76.123.456-7.
   :module: l10n_cl
   :notes: English UI, light theme, 1440px width.

Document types
==============

Accounting documents are categorized by :abbr:`SII (Servicio de Impuestos Internos)`-defined
document types.

Document types are created automatically upon installation of the localization module, and can be
managed by navigating to :menuselection:`Accounting --> Configuration --> Document Types`.

.. screenshot:: finance-fl-chile-document-types
   :menu: Accounting ‣ Configuration ‣ Document Types
   :shows: The Document Types list of the Chilean localization (Name, Doc Code Prefix, Country, Internal Type, SII code) e.g. "(33) Factura Electrónica", "(61) Nota de Crédito Electrónica", with the Active toggle column.
   :data: Demo company "YourCompany CL".
   :module: l10n_cl, l10n_latam_invoice_document
   :notes: English UI, light theme, 1440px width.

.. note::
   Several document types are inactive by default but can be activated by toggling the
   :guilabel:`Active` option.

Use on invoices
---------------

The document type on each transaction is determined by:

- The journal related to the invoice, identifying if the journal uses documents.
- The condition applied based on the type of issuer and recipient (e.g., the buyer or vendor's
  fiscal regime).

Journals
========

*Sales journals* in Odoo usually represent a business unit or location.

.. example::
   - Ventas Santiago.
   - Ventas Valparaiso.

For retail stores it is common to have one journal per :abbr:`POS (Point of Sale)`.

.. example::
   - Cashier 1.
   - Cashier 2.

The *purchase* transactions can be managed with a single journal, but sometimes companies use more
than one journal in order to handle some accounting transactions that are not related to vendor
bills. This configuration can easily be set by using the following model.

.. example::
   - Tax payments to the government.
   - Employees payments.

Create a sales journal
----------------------

To create a sales journal, navigate to :menuselection:`Accounting --> Configuration --> Journals`.
Then, click the :guilabel:`New` button, and fill in the following required information:

- :guilabel:`Type`: select :guilabel:`Sale` from the drop-down menu for customer invoice journals.
- :guilabel:`Use Documents`: check this field if the journal will use document types. This field is
  only applicable to purchase and sales journals that can be related to the different sets of
  document types available in Chile. By default, all the sales journals created will use documents.

Next, from the :guilabel:`Journal Entries` tab, define the :guilabel:`Default Income Account` and
:guilabel:`Dedicated Credit Note Sequence` in the :guilabel:`Accounting Information` section.

Each document type used in the journal gets its own sequence (folio). When the first document of a
type is created, edit its number to continue the folio range authorized by the SII for the company.

Chart of accounts
=================

The chart of accounts is installed by default as part of the data set included in the localization
module. The accounts are mapped automatically in:

- Taxes
- Default Account Payable
- Default Account Receivable
- Transfer Accounts
- Conversion Rate

.. seealso::
   :doc:`../accounting/get_started/chart_of_accounts`

Taxes
=====

As part of the localization module, taxes are created automatically with their related financial
account and configuration. These taxes can be managed from :menuselection:`Accounting -->
Configuration --> Taxes`.

Chile has several tax types, the most common ones are:

- **VAT**: the regular VAT can have several rates.
- **ILA**: the tax for alcoholic drinks.

.. seealso::
   :doc:`../accounting/taxes`


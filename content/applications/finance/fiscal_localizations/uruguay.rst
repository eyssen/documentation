=======
Uruguay
=======

.. |DGI| replace:: :abbr:`DGI (Dirección General Impositiva)`

.. _uruguay/intro:

Introduction
============

The Uruguayan localization provides the chart of accounts, the taxes, the identification types and
the |DGI| document types (e-Invoice, e-Ticket, export e-Invoice and their credit and debit notes)
needed to number and print the documents of a company in Uruguay.

.. note::
   Electronic invoicing (CFE) through the Uruware provider — the XML generation, electronic
   signature, connection to the |DGI|, CAE management, *addendas* and *leyendas* — is **not**
   available in this edition. Electronic documents must be issued through the |DGI| portal or a
   certified provider outside Odoo.

Glossary
--------

- **DGI**: *Dirección General Impositiva* is the government entity responsible for enforcing tax
  payments in Uruguay.
- **CFE**: *Comprobante Fiscal Electrónico*, the electronic documents defined by the |DGI|.

Configuration
=============

Modules installation
--------------------

:ref:`Install <general/install>` the following modules to get all the features of the Uruguayan
localization:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Uruguay - Accounting`
     - `l10n_uy`
     - Default :ref:`fiscal localization package <fiscal_localizations/packages>`: chart of
       accounts, taxes, identification types (RUT, CI, NIE, passport, …) and |DGI| document types.
   * - :guilabel:`Uruguay - Point of Sale`
     - `l10n_uy_pos`
     - Technical adjustments of the Point of Sale for Uruguay (installed automatically with the
       Point of Sale app).
   * - :guilabel:`Uruguay Website`
     - `l10n_uy_website_sale`
     - Always shows the business (B2B) fields, such as the identification number, at the eCommerce
       checkout.

Company
-------

To configure your company information, open the **Settings** app, scroll down to the
:guilabel:`Companies` section, click :guilabel:`Update Info`, and configure the following:

- :guilabel:`Company Name`
- :guilabel:`Address`, including the :guilabel:`Street`, :guilabel:`City`, :guilabel:`State`,
  :guilabel:`ZIP`, and :guilabel:`Country`
- :guilabel:`Tax ID`: enter the company's RUT.

After configuring the company in the database settings, navigate to :menuselection:`Contacts` and
search for your company to verify the following:

- the company type is set to :guilabel:`Company`.
- the :guilabel:`Identification Number` :guilabel:`Type` is :guilabel:`RUT / RUC`.

Master data
-----------

Chart of accounts
~~~~~~~~~~~~~~~~~

The :doc:`chart of accounts <../accounting/get_started/chart_of_accounts>` is installed by default
as part of the set of data included in the localization module, the accounts are mapped
automatically in taxes, default accounts payable, and default accounts receivable.

Accounts can be added or deleted according to the company's needs.

Contacts
~~~~~~~~

To create a contact, navigate to :menuselection:`Contacts app` and select :guilabel:`New`. Then
enter the following information:

- :guilabel:`Company Name`
- :guilabel:`Address`: :guilabel:`Street`, :guilabel:`City`, :guilabel:`State`, :guilabel:`ZIP`
  and :guilabel:`Country`
- :guilabel:`Identification Number`: select the identification :guilabel:`Type` and enter the
  :guilabel:`Number`. The identification type of the customer determines which document type
  (e-Invoice for a RUT, e-Ticket otherwise, export e-Invoice for foreign customers) is proposed on
  the invoice.

Taxes
~~~~~

As part of the Uruguay localization module, taxes are automatically created with their
configuration and related financial accounts (VAT 22 %, VAT 10 %, the 20 % reduced VAT, included variants, and the 0 % exempt taxes). Each
tax has a :guilabel:`Tax Category` (:guilabel:`VAT`) used to group the amounts in the reports.

.. screenshot:: finance-fl-uruguay-taxes
   :menu: Accounting ‣ Configuration ‣ Taxes
   :shows: The Taxes list of the Uruguayan localization with the 22% and 10% VAT sales and purchase taxes, the 20% reduced VAT and the 0% exempt taxes.
   :data: Demo company "YourCompany UY", Uruguayan localization installed.
   :module: l10n_uy
   :notes: English UI, light theme, 1440px width.

Document types
~~~~~~~~~~~~~~

Some accounting transactions, like *customer invoices* and *vendor bills* are classified by document
types. These are defined by the government fiscal authorities, in this case by the |DGI|.

Each document type can have a unique sequence per journal where it is assigned. The data is created
automatically when the localization module is installed, and the information required for the
document types is included by default.

To review the document types included in the localization, navigate to :menuselection:`Accounting
--> Configuration --> Document Types`.

.. screenshot:: finance-fl-uruguay-document-types
   :menu: Accounting ‣ Configuration ‣ Document Types
   :shows: The Document Types list of the Uruguayan localization: e-Invoice (111), e-Ticket (101), their credit/debit notes and the export e-Invoice (121), with Doc Code Prefix and Internal Type columns.
   :data: Demo company "YourCompany UY".
   :module: l10n_uy, l10n_latam_invoice_document
   :notes: English UI, light theme, 1440px width.

Sales journals
~~~~~~~~~~~~~~

On the sales journals, activate :guilabel:`Use Documents?` if the journal uses the |DGI| document
types. Each document type then gets its own sequence in the journal; edit the number of the first
document to continue the numbering authorized by the |DGI| (CAE range).

Workflows
=========

Customer invoices
-----------------

Create a :doc:`customer invoice <../accounting/customer_invoices>` as usual; the
:guilabel:`Document Type` is proposed from the customer's identification type and can be changed
before posting. The invoice number combines the document type prefix and the sequence (e.g.
`e-Invoice 0000001`). Credit notes and debit notes get the matching credit/debit note document
types.

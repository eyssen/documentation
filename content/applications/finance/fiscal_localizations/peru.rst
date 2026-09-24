====
Peru
====

.. |SUNAT| replace:: :abbr:`SUNAT (Superintendencia Nacional de Aduanas y de Administración Tributaria)`

Modules
=======

The following modules related to the Peruvian localization are available:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Peru - Accounting`
     - `l10n_pe`
     - Default :ref:`fiscal localization package <fiscal_localizations/packages>`: the PCGE chart
       of accounts, the taxes with their |SUNAT| codes, the |SUNAT| document types and
       identification types, the districts (*ubigeo*) and the list of Peruvian banks.
   * - :guilabel:`Peruvian - Point of Sale`
     - `l10n_pe_pos`
     - Adds the anonymous *Consumidor Final* customer and the identification type, city and district
       fields to the Point of Sale customer form (installed automatically with the Point of Sale
       app).
   * - :guilabel:`Peruvian eCommerce`
     - `l10n_pe_website_sale`
     - Always shows the business (B2B) fields, such as the identification number, at the eCommerce
       checkout.

.. note::
   Electronic invoicing with the |SUNAT| (signature providers Digiflow / IAP / SUNAT, CDR status,
   cancellations, detraction invoices, export invoices, electronic delivery guide GRE 2.0), the
   permanent inventory reports PLE 12.1 / 13.1 and the automatic e-invoicing of eCommerce and Point
   of Sale sales are **not** available in this edition. Invoices are numbered with the |SUNAT|
   document types and printed by Odoo; the electronic documents must be issued through the SUNAT
   portal or an OSE outside Odoo.

Configuration
=============

.. _peru/company:

Configure your company
----------------------

In addition to the basic information in the Company, set Peru as the :guilabel:`Country` and
enter the RUC (*Registro Único de Contribuyentes*) in the :guilabel:`Tax ID` field, with the
:guilabel:`Identification Number` type set to :guilabel:`RUC`. Fill in the complete address,
including the :guilabel:`District`.

.. screenshot:: finance-fl-peru-company
   :menu: Settings ‣ Users & Companies ‣ Companies ‣ (your company)
   :shows: The company form of a Peruvian company with the address (Street, District, City, State, Country = Peru) and the "Tax ID" (RUC 20557912879) with identification type "RUC".
   :highlight: The "District" and "Tax ID" fields.
   :data: Demo company "YourCompany PE", Peruvian localization installed.
   :module: l10n_pe
   :notes: English UI, light theme, 1440px width.

Chart of Account
----------------

The chart of accounts is installed by default as part of the set of data included in the
localization module, the accounts are mapped automatically in:

- Taxes
- Default Account Payable.
- Default Account Receivable

The chart of accounts for Peru is based on the most updated version of the :abbr:`PCGE (Plan
Contable General Empresarial)`, which is grouped in several categories and is compatible with NIIF
accounting.

Configure Master data
---------------------

Taxes
~~~~~

As part of the localization module the taxes are created automatically with their related
financial account and |SUNAT| configuration. Each tax carries, in the :guilabel:`Advanced Options`
tab (visible for Peruvian companies), the :guilabel:`Code` of the tax type defined by the |SUNAT|
(:guilabel:`IGV - General Sales Tax`, :guilabel:`ISC - Selective Excise Tax`,
:guilabel:`ICBPER - Plastic bag tax`, :guilabel:`EXP - Exportation`, :guilabel:`GRA - Free`,
:guilabel:`EXO - Exonerated`, :guilabel:`INA - Unaffected`, …), the :guilabel:`UNECE Code` of the
tax category, and, for ISC taxes, the ISC calculation type. If you create new taxes, fill in these
fields so that the printed documents show the right tax breakdown.

.. screenshot:: finance-fl-peru-taxes
   :menu: Accounting ‣ Configuration ‣ Taxes ‣ (IGV 18%) ‣ Advanced Options tab
   :shows: The Advanced Options tab of the "IGV 18%" tax with the "Code" field set to "IGV - General Sales Tax" and the "UNECE Code" set to "S - Standard rate".
   :highlight: The "Code" and "UNECE Code" fields.
   :data: Demo company "YourCompany PE".
   :module: l10n_pe
   :notes: English UI, light theme, 1440px width.

Fiscal Positions
~~~~~~~~~~~~~~~~

There are two main fiscal positions included by default when you install the Peruvian localization.

**Extranjero - Exportación**: Set this fiscal position on customers for Exportation transactions.

**Local Peru**: Set this fiscal position on local customers.

Document Types
~~~~~~~~~~~~~~

In some Latin American countries, including Peru, some accounting transactions like invoices and
vendor bills are classified by document types, defined by the government fiscal authorities, in
this case by the SUNAT.

Each document type can have a unique sequence per journal where it is assigned. As part of the
localization, the Document Type includes the country on which the document is applicable; the data
is created automatically when the localization module is installed.

The information required for the document types is included by default so the user does not need
to fill anything on this view (:menuselection:`Accounting --> Configuration --> Document Types`).

.. note::
   The documents supported on customer invoices are: Invoice (*Factura*), *Boleta*, Debit Note
   and Credit Note. The document type proposed on an invoice depends on the customer's
   identification type: a customer with a RUC gets a *Factura*, other customers a *Boleta*.

Journals
~~~~~~~~

When creating Sales Journals, the :guilabel:`Use Documents` field defines if the journal uses
Document Types. It is only applicable to Purchase and Sales journals, which are the ones that can
be related to the different set of document types available in Peru. By default, all the sales
journals created use documents. Each document type gets its own sequence in the journal, with the
series (e.g. `F001`, `B001`) as prefix; edit the number of the first document to set the series
registered with the |SUNAT|.

Partner
~~~~~~~

As part of the Peruvian localization, the identification types defined by the SUNAT (RUC, DNI,
CE, passport, …) are available on the Partner form; this information is essential for most
transactions, both for the sender company and for the customer, so make sure you fill it in on
your records. The address also has a :guilabel:`District` field (*ubigeo*) next to the city.

.. screenshot:: finance-fl-peru-id-type
   :menu: Contacts ‣ (a Peruvian customer)
   :shows: A contact form with the "Identification Number" type drop-down open (RUC, DNI, CE, Pasaporte, …) and a RUC number filled in, plus the "District" field in the address block.
   :highlight: The identification type field.
   :data: Contact "Comercial Andina SAC", RUC 20100070970, district Miraflores.
   :module: l10n_pe, l10n_latam_base
   :notes: English UI, light theme, 1440px width.

Point of Sale
=============

With the *Peruvian - Point of Sale* module, the Point of Sale customer form shows the
:guilabel:`Identification Number` type, the :guilabel:`City` and the :guilabel:`District` fields,
and the anonymous customer *Consumidor Final* is always loaded in the session so that sales without
customer data can be recorded as *Boleta* sales. This customer cannot be deleted.

eCommerce
=========

With the *Peruvian eCommerce* module, the checkout of a Peruvian website always displays the
business (B2B) fields (company name and identification number), so that the invoice created from
the order gets the right document type (*Factura* for a RUC, *Boleta* otherwise).

.. seealso::
   :doc:`Set up the Mercado Pago payment provider. <../payment_providers/mercado_pago>`

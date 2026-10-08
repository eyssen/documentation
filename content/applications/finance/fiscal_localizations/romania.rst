:show-content:
:show-toc:

=======
Romania
=======

The Romanian localization combines the standard :guilabel:`Romania - Accounting` package, the
standard E-Factura and E-Transport integrations of Odoo, and a set of *eYssen* modules. Together
they cover invoicing according to the Fiscal Code, the exchange rates of the National Bank of
Romania (BNR), bank statement and cash documents, E-Factura for businesses and individuals, the
declarations to the ANAF (*D300*, *D390*, *D394*, *D101*, SAF-T *D406*), the annual financial
statements, the mandatory accounting registers, fixed assets and stock accounting.

The Romanian features only apply to the companies whose **fiscal country** is Romania, so the
localization can be installed in a database that also contains Hungarian or Spanish companies (see
:doc:`romania/multi_company`).

.. _localizations/romania/modules:

Configuration
=============

:ref:`Install <general/install>` the following modules to get all the features of the Romanian
localization. Only the first ones are required for invoicing; install the others according to the
needs of the company. Some modules are installed automatically with the module they extend, as
mentioned in their description.

Standard modules
----------------

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Romania - Accounting`
     - `l10n_ro`
     - Default :ref:`fiscal localization package <fiscal_localizations/packages>`: chart of
       accounts, taxes and the :guilabel:`NRC` (trade register number) field on contacts.
   * - :guilabel:`Romania - E-invoicing`
     - `l10n_ro_edi`
     - Sends customer invoices in the CIUS-RO (UBL) format to the ANAF *SPV* platform (E-Factura).
       Installed automatically for Romanian companies.
   * - :guilabel:`Romania - Synchronize E-Factura`
     - `l10n_ro_efactura_synchronize`
     - Imports the vendor bills received in the SPV into a purchase journal.
   * - :guilabel:`Romania - E-Transport`
     - `l10n_ro_edi_stock`
     - Declares transports of goods to the ANAF e-Transport system from delivery orders and
       receipts (UIT code).
   * - :guilabel:`Romania - CPV Code`
     - `l10n_ro_cpv_code`
     - Adds the CPV (Common Procurement Vocabulary) code to products, required on some E-Factura
       lines.

Invoicing, taxes and exchange rates
-----------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Romania - Localization Base`
     - `l10n_ro_base`
     - :doc:`Foundation of the eYssen modules <romania/base>`: company settings, CNP, lookup of the
       contacts in the ANAF register, duplicate checks, legal holidays and working days, access to
       the Romanian menus.
   * - :guilabel:`Romania - Invoice Mentions`
     - `l10n_ro_invoice_report`
     - :doc:`Invoice layout <romania/invoicing>`: CUI, trade register number, share capital, series
       and number, *TVA la încasare*, *taxare inversă*, BNR rate and amounts in RON. Installed
       automatically with `l10n_ro_base`.
   * - :guilabel:`Romania - Non-deductible VAT`
     - `l10n_ro_nondeductible_vat`
     - :doc:`Purchase taxes with a limited or no VAT deduction <romania/nondeductible_vat>`
       (article 298) and the fiscal position that applies them.
   * - :guilabel:`Romania - BNR exchange rates`
     - `l10n_ro_currency_rate_bnr`
     - :doc:`BNR rates <romania/exchange_rates>` for the automatic update, loading of the historical
       rates, and the rate date rule of article 290.
   * - :guilabel:`Romania - E-Factura Extensions`
     - `l10n_ro_edi_extra`
     - :doc:`B2C invoices, Law 88/2026, submission deadline, storno invoices, SPV messages and ANAF
       check <romania/e_factura>`.
   * - :guilabel:`PoS Invoice - Romania`
     - `l10n_ro_pos_invoice`
     - :ref:`Data required to invoice a customer from the Point of Sale
       <localizations/romania/pos-invoice>`. Installed automatically with `eyssen_pos_invoice` and
       `l10n_ro_base`.

Bank and cash
-------------

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Romania - Bank statement import (MT940, CAMT.053, CSV)`
     - `l10n_ro_account_statement_import`
     - :doc:`Import of the statements of the Romanian banks <romania/bank_statements>` (MT940 for
       BCR, BRD, ING, BT, Raiffeisen and UniCredit, CAMT.053, CSV) and recognition of the partners
       by IBAN or CUI.
   * - :guilabel:`Romania - Cash Documents (eYssen)`
     - `l10n_ro_cash`
     - :doc:`Receipts, cash orders, cash register book and the cash limits <romania/cash>` of
       Law 70/2015, on the eYssen cash register.

ANAF declarations
-----------------

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Romania - ANAF Declarations Base`
     - `l10n_ro_declaration`
     - :doc:`Common framework of the declarations <romania/declarations>`: periods, versions, XML
       and XSD, validation with the ANAF *DUKIntegrator*, tax code catalogue.
   * - :guilabel:`Romania - D300 VAT Return (Decont de TVA)`
     - `l10n_ro_d300`
     - :doc:`VAT return <romania/d300>`, with the reconciliation with RO e-TVA.
   * - :guilabel:`Romania - D390 Recapitulative Statement (VIES)`
     - `l10n_ro_d390`
     - :doc:`Recapitulative statement of the intra-Community operations <romania/d390>`.
   * - :guilabel:`Romania - D394 Informative Statement (Domestic Supplies and Acquisitions)`
     - `l10n_ro_d394`
     - :doc:`Informative statement of the domestic supplies and acquisitions <romania/d394>`.
   * - :guilabel:`Romania - D101 Profit Tax Return and Micro-enterprise Tax`
     - `l10n_ro_d101`
     - :doc:`Annual profit tax return and micro-enterprise tax <romania/d101>`.
   * - :guilabel:`Romania - SAF-T D406 (Fișierul Standard de Control Fiscal)`
     - `l10n_ro_d406`
     - :doc:`SAF-T declaration D406 <romania/saft_d406>`, monthly or quarterly.
   * - :guilabel:`Romania - SAF-T D406 Assets`
     - `l10n_ro_d406_asset`
     - Annual D406 declaration of the fixed assets. Installed automatically with `l10n_ro_d406`
       and `l10n_ro_asset`.
   * - :guilabel:`Romania - SAF-T D406 Inventory`
     - `l10n_ro_d406_stock`
     - D406 inventory declaration, on request. Installed automatically with `l10n_ro_d406` and the
       stock valuation.

Financial statements, registers, assets and stock
-------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Romania - Financial Statements (Situații financiare, ANAF)`
     - `l10n_ro_financial_statements`
     - :doc:`Annual financial statements <romania/financial_statements>` (S1002 to S1005 and the
       half-year report S1027).
   * - :guilabel:`Romania - Accounting Registers (Dynamic Reports)`
     - `l10n_ro_dynamic_reports`
     - :doc:`Mandatory accounting registers <romania/statutory_registers>`.
   * - :guilabel:`Romania - Fixed Assets (eYssen)`
     - `l10n_ro_asset`
     - :doc:`Fixed assets <romania/fixed_assets>`: catalog of HG 2139/2004, linear, degressive and
       accelerated depreciation.
   * - :guilabel:`Romania - Stock Accounting`
     - `l10n_ro_stock_account`
     - :doc:`Romanian perpetual inventory postings <romania/inventory>`.
   * - :guilabel:`Romania - Stock Reports`
     - `l10n_ro_stock_report`
     - :doc:`Stock documents and reports <romania/inventory>`: NIR, delivery note (*aviz*),
       consumption voucher, stock card (*fișa de magazie*), inventory list.

.. note::
   The Romanian SAF-T export (**D.406 declaration**) is available with the
   :guilabel:`Romania - SAF-T D406 (Fișierul Standard de Control Fiscal)` module
   (`l10n_ro_d406`): see :doc:`romania/saft_d406`.

.. seealso::
   :doc:`Documentation on e-invoicing’s legality and compliance in Romania
   <../accounting/customer_invoices/electronic_invoicing/romania>`

.. _localizations/romania/company:

Company
-------

In :menuselection:`Settings --> General Settings --> Companies --> Update Info`, fill in the
company's :guilabel:`Tax ID` (CUI, with the `RO` prefix for VAT-registered companies) and, in the
company's contact form, the :guilabel:`NRC` (*Număr de ordine în Registrul Comerțului*).

The Romanian features of the eYssen modules are only active when the :guilabel:`Fiscal Country` of
the company, in the :guilabel:`Taxes` section of :menuselection:`Accounting --> Configuration -->
Settings`, is Romania. The other options of the company, such as the VAT on
collection system and the share capital, are in the :ref:`Romanian Localization settings
<localizations/romania/base-settings>`.

.. _localizations/romania/efactura:

E-Factura
=========

The standard integration described in this section sends the invoices to the ANAF *SPV* and
receives the vendor bills. The :doc:`rules that Romanian companies add to it <romania/e_factura>`
(invoices to individuals and Law 88/2026, submission deadline, storno invoices, SPV messages) are
provided by the eYssen *Romania - E-Factura Extensions* module.

.. _localizations/romania/efactura-spv:

Connection to the SPV
---------------------

Odoo sends the invoices to the ANAF *Spațiul Privat Virtual* (SPV) with the company's own OAuth
credentials. In :menuselection:`Accounting --> Configuration --> Settings --> Romanian E-Factura`:

#. Register an application on the ANAF developer portal with the :guilabel:`Callback URL` shown in
   the settings block, and copy the resulting :guilabel:`Client ID` and :guilabel:`Client Secret`
   into the corresponding fields.
#. Keep :guilabel:`Use Test Environment` enabled while testing; disable it for production.
#. Insert the digital signature USB token, click :guilabel:`Generate Token` and log in to ANAF. The
   :guilabel:`Access Token` and :guilabel:`Refresh Token` and their expiry dates are then filled in
   automatically; the token is refreshed by a scheduled action before it expires.

.. screenshot:: finance-fl-romania-efactura-settings
   :menu: Accounting ‣ Configuration ‣ Settings ‣ Romanian E-Factura
   :shows: The "Romanian E-Factura" settings block with the Callback URL, "Client ID", "Client Secret", the "Generate Token" button, the access/refresh token expiry dates and the "Use Test Environment" checkbox.
   :highlight: The "Generate Token" button.
   :data: Demo company "YourCompany RO", Romanian localization installed; test environment, throw-away credentials.
   :module: l10n_ro_edi
   :notes: English UI, light theme, 1440px width; use a throw-away secret.

Sending invoices
----------------

Once an invoice is posted, open :guilabel:`Send & Print` and keep the :guilabel:`Send E-Factura to
SPV` option enabled: the CIUS-RO XML is generated, attached to the invoice and uploaded to the
SPV. The :guilabel:`E-Factura Status` field of the invoice then shows :guilabel:`Sent`; click
:guilabel:`Fetch status` on the line of the :guilabel:`E-Factura` tab to retrieve the ANAF answer,
which sets the status to :guilabel:`Validated` (a failed document is listed as :guilabel:`Error` in
the tab). The validated document can be downloaded with :guilabel:`Download` in the
:guilabel:`E-Factura` tab of the invoice, and errors are logged in the chatter.

With the *Romania - E-Factura Extensions* module, the invoices to individuals are reported as
well, the invoices that are late are followed with reminders, and the messages of the SPV are
stored: see :doc:`romania/e_factura`.

.. screenshot:: finance-fl-romania-efactura-invoice
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (a sent invoice) ‣ E-Factura tab
   :shows: A posted customer invoice with the "E-Factura Status" field showing "Validated", the "Fetch status" button and the E-Factura tab listing the sent document with its index and the "Download" button.
   :highlight: The "E-Factura Status" field.
   :data: Demo company "YourCompany RO", invoice INV/2025/00003 validated in the test SPV.
   :module: l10n_ro_edi
   :notes: English UI, light theme, 1440px width.

Receiving vendor bills
----------------------

With the *Romania - Synchronize E-Factura* module, select the purchase journal in
:guilabel:`Import Vendor Bills in` in the same settings block. The scheduled action
:guilabel:`E-Factura: Synchronize with ANAF` then downloads the invoices addressed to the company in
the SPV and creates draft vendor bills from them in that journal.

E-Transport
===========

The *Romania - E-Transport* module declares the transport of goods to the ANAF e-Transport system
directly from the transfer. On a delivery order or receipt, the :guilabel:`eTransport` tab holds the
required data: operation type and scope, :guilabel:`Vehicle Number` (and trailers), the start and
end location types, border crossing point or customs office where applicable, and the carrier's
partner set on the delivery method. Click :guilabel:`Send eTransport` to obtain the :guilabel:`UIT`
code (listed in the :guilabel:`eTransport Documents` tab), :guilabel:`Fetch Status` to update the
:guilabel:`eTransport Status`, and :guilabel:`Amend eTransport` to send a correction. The UIT is
printed on the delivery slip.

.. screenshot:: finance-fl-romania-etransport-picking
   :menu: Inventory ‣ Operations ‣ Deliveries ‣ (a delivery order) ‣ eTransport tab
   :shows: A validated delivery order with the "Send eTransport" and "Fetch Status" buttons in the header and the eTransport tab: operation type, vehicle number, start/end location types and the returned "UIT" code with the "eTransport Status" = Validated.
   :highlight: The "UIT" field.
   :data: Demo company "YourCompany RO", delivery WH/OUT/00012, vehicle B123ABC.
   :module: l10n_ro_edi_stock
   :notes: English UI, light theme, 1440px width.

CPV codes
=========

The *Romania - CPV Code* module adds a :guilabel:`CPV Code` field to the product form (Invoicing
tab). Set it on the products sold to public institutions, so that the code is included
in the E-Factura lines when required.

.. toctree::
   :titlesonly:

   romania/base
   romania/invoicing
   romania/nondeductible_vat
   romania/exchange_rates
   romania/bank_statements
   romania/cash
   romania/e_factura
   romania/declarations
   romania/d300
   romania/d390
   romania/d394
   romania/d101
   romania/financial_statements
   romania/saft_d406
   romania/statutory_registers
   romania/fixed_assets
   romania/inventory
   romania/multi_company

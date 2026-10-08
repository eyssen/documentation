====================
SAF-T D406 (Romania)
====================

The *D406* informative declaration (*Declarația informativă D406 - Fișierul Standard de Control
Fiscal*) is the Romanian version of the :abbr:`SAF-T (Standard Audit File for Tax)`. It is an XML
file that contains the accounting data of a company (chart of accounts with balances, journal
entries, invoices, payments and, depending on the variant, fixed assets or stock) and is filed with
the :abbr:`ANAF (Agenția Națională de Administrare Fiscală, National Agency for Fiscal
Administration)`.

The eYssen modules generate the file from the accounting data of Odoo, check it and prepare it for
the upload to ANAF. They implement the ANAF schema version 2.4.9 and are aligned with the
*DUKIntegrator* validator version J2.2.18 (February 2026).

.. note::
   Odoo creates, checks and exports the file. It does not transmit it to ANAF: upload the exported
   file to the ANAF platform yourself, then record the submission in Odoo (see :ref:`Mark as
   submitted <localizations/romania/saft/submit>`).

.. _localizations/romania/saft/modules:

Modules
=======

:ref:`Install <general/install>` the modules of the variants you need to file. The *D406* module
installs the declarations framework (:doc:`declarations`) as a dependency.

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Romania - SAF-T D406 (Fișierul Standard de Control Fiscal)`
     - `l10n_ro_d406`
     - The *General* variant (monthly or quarterly), including the simplified variant for
       non-resident companies, the ANAF nomenclatures and the mapping of accounts, taxes, partners
       and units.
   * - :guilabel:`Romania - SAF-T D406 Assets`
     - `l10n_ro_d406_asset`
     - The yearly *Assets* variant. It is installed automatically when the *D406* module and the
       :doc:`Romanian fixed assets <fixed_assets>` module are installed.
   * - :guilabel:`Romania - SAF-T D406 Inventory`
     - `l10n_ro_d406_stock`
     - The *Inventory* variant, filed on request of ANAF. It is installed automatically when the
       *D406* module and the Inventory valuation (`stock_account`) are installed.

If you create a declaration of a variant whose module is missing, Odoo refuses to generate it and
tells you which module to install.

.. _localizations/romania/saft/variants:

The D406 variants
=================

All variants are the same document type in Odoo (:menuselection:`Accounting --> Romania (ANAF) -->
Declarations --> SAF-T D406`). The :guilabel:`D406 Type` decides the period and the content of the
file.

.. list-table::
   :header-rows: 1
   :widths: 18 22 12 28 20

   * - :guilabel:`D406 Type`
     - Period
     - Header comment
     - Content
     - Deadline
   * - :guilabel:`General (monthly / quarterly)`
     - Month or quarter (the VAT period of the company)
     - `L` (monthly), `T` (quarterly)
     - General ledger accounts, customers, suppliers, tax table, units of measure, analysis types,
       products, general ledger entries, sales invoices, purchase invoices and payments.
     - Last day of the month following the period
   * - :guilabel:`General (monthly / quarterly)` with :guilabel:`Non-resident (simplified)`
     - Month or quarter
     - `NL` (monthly), `NT` (quarterly)
     - Tax table, units of measure, products, sales invoices and purchase invoices only.
     - Last day of the month following the period
   * - :guilabel:`Assets (annual)`
     - Year
     - `A`
     - General ledger accounts, fixed assets and asset transactions.
     - 30 May of the following year
   * - :guilabel:`Inventory (on request)`
     - Month, quarter, semester or year
     - `C`
     - General ledger accounts, tax table, units of measure, movement types, products, physical
       stock, owners and movements of goods.
     - None: set by the ANAF request

The sub-sections that the schema requires but that a variant does not report are written empty. A
deadline that falls on a weekend or a public holiday is moved to the next working day.

.. note::
   The :guilabel:`General` D406 can only be created for the period types :guilabel:`Month` and
   :guilabel:`Quarter`, the :guilabel:`Assets` D406 only for a :guilabel:`Year`. A declaration of the
   same type, period and version can exist only once per company.

.. _localizations/romania/saft/config:

Configuration
=============

Prerequisites
-------------

Odoo only generates a D406 for a company that fulfils the following conditions:

- the **fiscal country** of the company is Romania. Only these companies are listed in the
  declarations, and the other companies of a multi-company database are ignored (see
  :doc:`multi_company`);
- the currency of the company is RON.

The validation also reports an error if:

- the company has no valid tax identification number (CUI), with a correct control digit;
- the declarant (last name, first name and position) is not filled in, either on the declaration or
  in the settings (see :doc:`declarations`).

Company settings
----------------

Go to :menuselection:`Accounting --> Configuration --> Settings`. In the :guilabel:`Romanian ANAF
Declarations` section, the :guilabel:`SAF-T (D406)` setting holds the company-level options:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`SAF-T Tax Accounting Basis`
     - The type of accounting and chart of accounts of the company, reported in the header of the
       file (`TaxAccountingBasis`). The default is `A` (commercial companies, OMFP 1802/2014). The
       other values are `I` (invoice accounting), `IFRS`, `BANK`, `INSURANCE`, `NORMA39`, `IFN`,
       `NORMA36`, `NORMA14`, `ONG`, `ONGE` and `BNR6`. The bundled ANAF chart used to map the
       accounts follows this choice for `A`, `IFRS`, `ONG` and `ONGE`.
   * - :guilabel:`SAF-T Reporting Period`
     - :guilabel:`Monthly` or :guilabel:`Quarterly`. It is the period of the general D406 and it
       follows the :guilabel:`VAT Period` of the company (monthly if the VAT period is monthly,
       quarterly otherwise). You can change it.
   * - :guilabel:`Non-resident Registered for VAT`
     - Tick it if the company is a non-resident registered for VAT in Romania. The general D406 is
       then the simplified variant (header comment `NL` or `NT`).
   * - :guilabel:`SAF-T Tax Entity`
     - Optional reference of the company, division or branch (`TaxEntity`).
   * - :guilabel:`Report Accounts without Balance`
     - Also reports the accounts that have no opening balance, no movement and no closing balance.
   * - :guilabel:`Report Analytic Distribution`
     - On by default. Reports the analytic distribution of the journal items (the analysis types and
       the analysis lines of the entries).
   * - :guilabel:`Maximum Compressed File Size (MB)`
     - 500 by default, the limit of ANAF for one D406 form. A bigger declaration is split into
       several files (see :ref:`localizations/romania/saft/split`).

.. _localizations/romania/saft/mapping:

Map the accounting data to the SAF-T codes
------------------------------------------

The SAF-T file uses its own codes for accounts, taxes, partners and units. The modules deduce them
from your data, and let you override each of them. Check the result before the first filing: the
validation reports the data that could not be mapped.

Accounts
   Open an account (:menuselection:`Accounting --> Configuration --> Chart of Accounts`) and go to
   its :guilabel:`SAF-T (D406)` tab. It shows the reported values and the overrides:

   - :guilabel:`SAF-T Account ID`: the number of the account in the file. If empty, the digits of the
     account code are used (`4111.01` becomes `411101`). It must be a non-zero integer.
   - :guilabel:`ANAF Standard Account`: the synthetic account of the ANAF chart. If empty, the
     longest synthetic account of the ANAF chart that starts the account number is used.
   - :guilabel:`SAF-T Account Type`: :guilabel:`Activ (debit balance)`, :guilabel:`Pasiv (credit
     balance)` or :guilabel:`Bifunctional (debit or credit)`. If empty, the bifunctional accounts
     of the chart (for example 121, 4428 and 473) are recognized by their number, the contra-asset
     accounts (28x, 29x, 39x, 49x, 59x) are *Pasiv*, and the other accounts follow the Odoo account
     type.

Taxes
   On a tax, the :guilabel:`SAF-T Tax Code` field sets the code explicitly. If it is empty, Odoo
   uses, in this order: the default of the chart of accounts template, the :guilabel:`Tax Mapping
   Rules` of the form D406 and the :guilabel:`Romanian Tax Codes` of the tax with the SAF-T codes
   defined by rate. Historic 19%, 9% and 5% taxes are mapped as well. Invoice lines without a tax
   are reported with the tax type `000`.

   The rules and the tax codes are under :menuselection:`Accounting --> Romania (ANAF) -->
   Configuration`. The ANAF lists themselves (:guilabel:`Tax Codes`, :guilabel:`Tax Types`,
   :guilabel:`Standard Accounts`, :guilabel:`Units of Measure` and :guilabel:`Code Lists`) are in
   :menuselection:`Accounting --> Romania (ANAF) --> Configuration --> SAF-T Nomenclatures`.

Partners
   On the :guilabel:`Invoicing` tab of a contact, the :guilabel:`SAF-T Identifier` field overrides the
   identifier of the customer or supplier. Otherwise Odoo builds it from the data of the commercial
   partner:

   .. list-table::
      :header-rows: 1
      :widths: 15 85

      * - Prefix
        - Used for
      * - `00`
        - Romanian company: `00` + CUI.
      * - `01`
        - Company with an EU VAT number: `01` + the VAT number.
      * - `02`
        - Company with a non-EU tax identifier: `02` + the identifier.
      * - `03`
        - Individual with a CNP (personal numeric code): `03` + CNP.
      * - `04`, `05`, `06`
        - Individuals without CNP and foreign companies without a VAT number: `04`, `05` or `06`
          + an internal code.
      * - `080000000000000`
        - Unidentified retail customers (receivable lines without partner).

Units and products
   On a unit of measure, :guilabel:`SAF-T Unit of Measure` selects the code of the ANAF nomenclature
   (UN/ECE recommendation 20/21). If empty, the code is deduced from the standard Odoo unit, or `H87`
   (piece) otherwise. On the :guilabel:`Accounting` tab of a product, :guilabel:`NC Code (SAF-T)`
   holds the 8-digit Combined Nomenclature code. Fill it where the law requires it (imports and
   exports, intra-Community movements, reverse charge by NC code, excise goods); it is reported as
   `0` otherwise.

Journals
   On the :guilabel:`Advanced Settings` tab of a journal, the :guilabel:`SAF-T (D406)` group has two
   fields: :guilabel:`SAF-T Payment Mechanism` (by default `10` for cash journals and `42` for bank
   journals) and :guilabel:`Self-billing (SAF-T)`. Tick the latter on the purchase journal of
   self-billed invoices (*autofacturi*): the invoices of the journal are reported with the invoice
   type and the self-billing indicator `389`.

.. _localizations/romania/saft/generate:

Generate and validate a declaration
===================================

To create a declaration, go to :menuselection:`Accounting --> Romania (ANAF) --> Declarations -->
SAF-T D406` and click :guilabel:`New`. The list only shows companies whose fiscal country is
Romania.

#. Select the :guilabel:`D406 Type`: :guilabel:`General (monthly / quarterly)`, :guilabel:`Assets
   (annual)` or :guilabel:`Inventory (on request)`. The :guilabel:`Assets` and :guilabel:`Inventory`
   types are only available if the matching module is installed.
#. Select the :guilabel:`Period Type`, the :guilabel:`Year` and the :guilabel:`Period`. The general
   variant is reported by month or quarter, the assets variant by year, and the inventory variant
   by month, quarter, semester or year.
#. Check the :guilabel:`Tax Accounting Basis`, the :guilabel:`Header Comment` and, for a
   non-resident, the :guilabel:`Non-resident (simplified)` box.
#. Click :guilabel:`Generate`. The declaration moves to :guilabel:`Computed`.
#. Click :guilabel:`Validate`. The declaration moves to :guilabel:`Validated`, or goes back to
   :guilabel:`Computed` if blocking errors are found.

.. note::
   Generation is only possible if the company is Romanian (fiscal country) and its currency is the
   Romanian leu (RON). A company that is not in RON, or a Hungarian company, is refused.

:guilabel:`Validate` runs three checks in order:

#. The **local checks** on the accounting data (see the table below).
#. The **XSD check** against the SAF-T schema bundled with the module (version 2.4.9).
#. The **DUKIntegrator check**, run by the DUK validator service configured in
   :doc:`declarations`. If no service is configured, this check is skipped (the status is
   :guilabel:`Not configured`) and only the local and XSD checks apply. If the service cannot be
   reached, the status is :guilabel:`Service unavailable` and a warning is added.

The results are listed in the :guilabel:`Validation` tab, with the :guilabel:`XSD Check` and
:guilabel:`DUK Validation` statuses. The :guilabel:`Errors` and :guilabel:`Warnings` smart buttons
open the message list. Errors block the export; warnings do not.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Check
     - Severity
     - Meaning
   * - `COMPANY_CUI`
     - Error
     - The tax identification number of the company is missing or its control digit is invalid.
   * - `DECLARANT`
     - Error
     - The last name, first name or position of the declarant is missing.
   * - `PARTNER_ID`
     - Error
     - A partner used in the period has no usable identifier, or its identifier is not valid.
   * - `ACCOUNT_UNMAPPED`, `ACCOUNT_CODE`, `ACCOUNT_DUPLICATE`
     - Error
     - An account does not match any account of the ANAF chart, has no numeric SAF-T account ID, or
       the same ID is used by two accounts.
   * - `TAX_UNMAPPED`
     - Error
     - A tax used in the period has no SAF-T tax code.
   * - `TRIAL_BALANCE`, `GLE_BALANCE`
     - Error
     - The opening and closing balances, or the general ledger entries, do not balance.
   * - `PARTNER_CITY`
     - Warning
     - The partner has no city; `-` is reported.
   * - `PAYABLE_NO_PARTNER`
     - Warning
     - A journal item of a payable account has no partner: it is reported with the identifier of the
       company. (The items of receivable accounts without partner are reported as unidentified
       retail customers, without a message.)
   * - `INVOICE_LINE_NO_TAX`
     - Warning
     - An invoice line has no tax.
   * - `TAX_INACTIVE`
     - Warning
     - The SAF-T tax code of a tax used in the period is inactive in the ANAF nomenclature.
   * - `PERIOD_OPEN`
     - Warning
     - The period has not ended yet.
   * - `PERIOD_TYPE`
     - Warning
     - The period type differs from the one set on the company.
   * - `UOM`
     - Error
     - A unit of measure is reported with a code that is not in the SAF-T nomenclature.

After a change in the accounting data or the mapping, click :guilabel:`Regenerate`, then
:guilabel:`Revalidate`.

.. _localizations/romania/saft/export:

Export and submit the file
==========================

#. Once the declaration is :guilabel:`Validated`, click :guilabel:`Export XML`. The file is
   downloaded, and the declaration moves to :guilabel:`Exported`. Use :guilabel:`Export XML Again`
   to download it again.
#. Upload the file to ANAF, in the SPV (*Spațiul Privat Virtual*, the ANAF online portal).
#. Back in Odoo, click :guilabel:`Mark as Submitted`. The :guilabel:`Submission Date` is set to today
   if it is empty. Fill in the :guilabel:`Submission Date` and the :guilabel:`Registration Number`
   given by ANAF in the :guilabel:`Validation` tab.

.. note::
   Odoo does not transmit the file to ANAF. :guilabel:`Mark as Submitted` only records that you did
   it.

The :guilabel:`Files` tab lists each file with its size and its XSD and DUK status, and lets you
download it. If a DUK report was requested in the settings, the PDF is available there too. The
file name is `D406_<CUI>_<period>_v<version>.xml`; for the assets and the inventory variants it
starts with `D406_A_` and `D406_C_` respectively.

.. _localizations/romania/saft/submit:

Mark as submitted, archive and correct
--------------------------------------

:guilabel:`Mark as Submitted` is only available on an exported declaration. To correct a declaration
that was already exported or submitted, click :guilabel:`Create Rectificative`. The new declaration
is a full new version of the same type and period, and it is generated and validated as usual. You
cannot create a rectificative while a newer version is still in progress.

When the rectificative is marked as submitted, the older versions are archived. Use
:guilabel:`Archive` to archive a declaration manually, and :guilabel:`Reset to Draft` to start over
before submission.

.. _localizations/romania/saft/split:

Large files
-----------

The file is generated in a streamed way, so big companies can be exported. If the compressed file
exceeds the size limit (500 MB by default), the sub-sections are distributed over several files. A
sub-section is never split, and each file has the full header with its position in the sequence
(`_1of3`, `_2of3`, ...). A multi-file export is downloaded as a ZIP archive. If a single
sub-section is bigger than the limit, an error is raised.

What each variant exports
=========================

General (`l10n_ro_d406`)
   The header, the master files (general ledger accounts, customers, suppliers, tax table, units of
   measure, analysis types, products), the general ledger entries of the period with the tax
   information, the source documents (sales invoices, purchase invoices and payments), and the
   opening and closing balances.

Non-resident
   If :guilabel:`Non-resident (simplified)` is ticked, the simplified file is generated. A
   non-resident can only file the general variant.

Assets (`l10n_ro_d406_asset`)
   Reported once a year, by 30 May of the following year (moved to the next working day if needed).
   It lists the purchase-type fixed assets that are running or closed, whose date is on or before the
   end of the year, and that were not disposed of before the year. The valuation is always the
   accounting one.
   The classification code comes from the HG 2139/2004 catalog (see :doc:`fixed_assets`). A
   warning (`ASSET_CATALOG`) is raised if the code is missing, and an error (`ASSET_ACCOUNT`) if
   the asset category has no asset account. The transactions are the acquisition (10, for the assets
   acquired in the year), the depreciation posted in the year (30) and the disposal.

   On the asset form, the :guilabel:`SAF-T (D406)` tab has the :guilabel:`Disposal Date (SAF-T)`,
   :guilabel:`Disposal Type (SAF-T)` and :guilabel:`Disposal Proceeds (SAF-T)` fields. The type and
   the proceeds appear once a disposal date is entered. The types are :guilabel:`Sale` (default),
   :guilabel:`Scrapping`, :guilabel:`Inventory shortage`, :guilabel:`Granted free of charge` and
   :guilabel:`Other`.

Inventory (`l10n_ro_d406_stock`)
   Requested by ANAF; there is no fixed deadline. It lists the physical stock per warehouse and
   storable product (quantity, opening and closing value, stock account), the owners of third-party
   stock, and the movements of goods of the period from the done stock moves (purchase,
   production, sale, returns, consumption, internal, inventory adjustment, scrap and other). The
   document type is NIR, AVIZ or BON, and the document number is the NIR number if there is one. A
   warning (`STOCK_ACCOUNT`) is raised if the category of a product has no stock valuation account.
   See :doc:`inventory`.

Known limitations
=================

- Payments: the settlement of invoices in other journals (for example a compensation made with a
  miscellaneous entry) is only reported in the general ledger.
- Inventory: the quantity of each warehouse is valued at the average unit cost of the valuation of
  the whole company. Stock owned by third parties is listed under the owners, but is not valued in
  the physical stock.
- Assets: the disposals come from the SAF-T fields of the asset, since the standard asset module
  has no disposal date. Revaluations and transfers are reported as 0.
- A Hungarian company, or a company in another currency than RON, cannot generate the declaration.

.. seealso::
   - :doc:`declarations`
   - :doc:`fixed_assets`
   - :doc:`inventory`
   - :doc:`multi_company`

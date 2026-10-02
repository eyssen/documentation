=====================
AEAT tax declarations
=====================

With the :ref:`Spanish localization (l10n_es) setup <localizations/spain/base-layer>`, the Spanish
tax declarations (*modelos*) of the AEAT are prepared in the Accounting app: the declaration
computes its boxes from the posted journal items of the period, creates the regularization entry if
the declaration has one, and exports the file (*fichero BOE*) that is uploaded to the AEAT
electronic office.

The declarations are installed with the *fiscal profile* of the company (self-employed person or
company). They can also be installed one by one: :ref:`install <general/install>` the *AEAT Base*
(`l10n_es_aeat`) module, which is the common framework of the declarations, and then the module of
each declaration.

.. list-table::
   :header-rows: 1
   :widths: 18 42 40

   * - Declaration
     - Content
     - Module and fiscal profile
   * - Modelo 303
     - VAT self-assessment, monthly or quarterly.
     - `l10n_es_aeat_mod303`; both profiles.
   * - Modelo 390
     - Annual VAT summary.
     - `l10n_es_aeat_mod390`; both profiles.
   * - Modelo 111
     - Withholdings on work income and professional activities.
     - `l10n_es_aeat_mod111`; both profiles.
   * - Modelo 190
     - Annual summary of the withholdings of the modelo 111 (informative return).
     - `l10n_es_aeat_mod190`; both profiles.
   * - Modelo 115
     - Withholdings on the rent of urban property.
     - `l10n_es_aeat_mod115`; both profiles.
   * - Modelo 180
     - Annual summary of the withholdings of the modelo 115 (informative return), see
       :ref:`localizations/spain/aeat/mod180`.
     - `l10n_es_aeat_mod180`; both profiles.
   * - Modelo 130
     - Instalment payment of the personal income tax (IRPF) of self-employed persons in direct
       estimation.
     - `l10n_es_aeat_mod130`; self-employed profile.
   * - Modelo 347
     - Annual declaration of operations with third parties above 3,005.06 €.
     - `l10n_es_aeat_mod347`; both profiles.
   * - Modelo 349
     - Recapitulative statement of intra-community operations.
     - `l10n_es_aeat_mod349`; both profiles.
   * - Modelo 369
     - VAT One-Stop-Shop (OSS) return for distance sales within the EU.
     - `l10n_es_aeat_mod369`; both profiles.
   * - Modelo 123
     - Withholdings on investment income (dividends, interest of loans and other income).
     - `l10n_es_aeat_mod123`; company profile.
   * - Modelo 193
     - Annual summary of the withholdings of the modelo 123 (informative return), see
       :ref:`localizations/spain/aeat/mod193`.
     - `l10n_es_aeat_mod193`; company profile.
   * - Modelo 216
     - Withholdings on the income of non-residents without a permanent establishment.
     - `l10n_es_aeat_mod216`; company profile.
   * - Modelo 296
     - Annual summary of the withholdings of the modelo 216 (informative return).
     - `l10n_es_aeat_mod296`; company profile.
   * - Modelo 202
     - Instalment payments of the corporate income tax, see
       :ref:`localizations/spain/aeat/mod202`.
     - `l10n_es_aeat_mod202`; company profile.
   * - VAT and IRPF books
     - *Libros registro* of issued and received invoices, exported to XLSX.
     - `l10n_es_vat_book`; both profiles.

The profiles also install the OSS extensions of the modelos 303 and 390 and of the VAT books
(`l10n_es_aeat_mod303_oss`, `l10n_es_aeat_mod390_oss` and `l10n_es_vat_book_oss`), the VAT prorate
modules of the modelos 303 and 390 (`l10n_es_vat_prorate`, `l10n_es_aeat_mod303_vat_prorate` and
`l10n_es_aeat_mod390_vat_prorate`) for the company profile, and the SII modules when the company is
an SII taxpayer (see :doc:`sii`).

The module `l10n_es_mis_report`, installed by both profiles, adds the official annual accounts (PGC
balance sheet and profit and loss), see :ref:`localizations/spain/aeat/annual-accounts`.

.. note::
   A declaration that is not part of the profile of the company, such as the modelo 130 for a
   company or the modelos 123, 193, 216, 296 and 202 for a self-employed person, is a separate
   module: install it from the :guilabel:`Apps` menu. Once installed, it appears in the same menu
   and works the same way.

Users with the *Accountant* role (and advisers) can create and file the declarations. The modelos
190 and 180 contain personal data of third parties and are restricted: they are only open to the
users of the technical groups *AEAT Model 190 (with access to sensitive data)* and *AEAT Model 180*,
which the administrator has by default. Add the users who file these two declarations to their
group, otherwise the menu is visible but the declaration cannot be opened.

.. _localizations/spain/aeat/configuration:

Configuration
=============

Default values of the declarations
----------------------------------

Go to :menuselection:`Accounting --> Configuration --> Settings`, and scroll to the
:guilabel:`AEAT Declarations` section. It is shown for Spanish companies, to the users who can file
the declarations. The values set here are proposed on every new declaration of the company:

- :guilabel:`Regularization entries`: the :guilabel:`AEAT Journal` (a miscellaneous journal) in
  which the regularization entries are posted, the :guilabel:`VAT Counterpart Account` (by default
  4750) for the VAT declarations whose counterpart is not computed by the declaration itself, such
  as the modelo 369, and the :guilabel:`Withholding Counterpart Account` (by default 4751) for the
  withholding declarations (111, 115, 123 and 216). The modelo 303 chooses 4750 or 4700 from its
  result by itself.
- :guilabel:`Submitter and frequency`: the :guilabel:`AEAT Contact Name`, :guilabel:`AEAT Contact
  Phone` and :guilabel:`AEAT Contact Email` printed in the declarations, and the :guilabel:`Filing
  Frequency` (:guilabel:`Quarterly` or :guilabel:`Monthly`). If the contact name is empty, the
  contact data of the current user is used. Monthly filing applies to large companies and to
  taxpayers registered in the REDEME or in the SII. A new declaration proposes the last closed
  period of this frequency; annual declarations propose the previous year.

When the *AEAT Base* module is installed, or when a Spanish chart of accounts is loaded, the empty
defaults of the company are filled in: the journal named *AEAT declarations* (code ``AEAT``, created
if the company has none) and the first accounts starting with 4750 and 4751.

.. note::
   Only the declarations that create a regularization entry use these accounts and the journal: the
   modelos 303, 369 and 202. The modelo 202 proposes its own accounts (4752 and 473), see
   :ref:`localizations/spain/aeat/mod202`. The other declarations only propose the period and the
   contact data.

.. screenshot:: finance-fl-spain-aeat-settings
   :menu: Accounting ‣ Configuration ‣ Settings ‣ AEAT Declarations
   :shows: The "AEAT Declarations" settings section with the "Regularization entries" block (AEAT Journal, VAT Counterpart Account 4750, Withholding Counterpart Account 4751), the "Submitter and frequency" block (contact name, phone, email, Filing Frequency "Quarterly") and the "Tax map check" link.
   :highlight: The "Filing Frequency" field.
   :data: Spanish demo company with the PGC chart of accounts.
   :module: l10n_es_aeat
   :notes: English UI, light theme, 1440px width.

.. _localizations/spain/aeat/tax-map:

Tax map check
-------------

Each declaration adds up the amounts of the taxes listed in its *tax map*: a tax that is in no map
line of an installed declaration is silently left out of the declarations. The :guilabel:`Tax map
check` setting shows how many active sales and purchase taxes of the company are in this situation.
Click the link to open the list of these taxes, or go to :menuselection:`Accounting -->
Configuration --> AEAT --> Taxes missing from the AEAT declarations`. In the tax list, the
:guilabel:`Missing from AEAT declarations` filter gives the same result.

Review the listed taxes: either the tax is not used, or it must be replaced by one of the default
Spanish taxes. A tax that you created by hand can be mapped by setting its :guilabel:`Equivalent
Tax (for AEAT mapping purposes)` to the default Spanish tax it corresponds to. The withholding
taxes of declarations that are not installed (for example 123, 216 and 296 for a self-employed
person) also appear in the list.

.. tip::
   The tax maps themselves can be consulted under :menuselection:`Accounting --> Configuration -->
   AEAT --> Tax mapping`. Do not modify them unless your tax adviser asks for it.

.. _localizations/spain/aeat/file:

File a declaration
==================

The declarations are under :menuselection:`Accounting --> Reporting --> AEAT`, one menu per
declaration, for example :menuselection:`Accounting --> Reporting --> AEAT --> AEAT 303 model`.

#. Click :guilabel:`New`. The :guilabel:`Year` and the :guilabel:`Period Type` of the last closed
   period, the contact data, and, for the declarations that create an entry, the journal and the
   counterpart account, are proposed from the
   :ref:`settings <localizations/spain/aeat/configuration>`. Change them if needed.
#. Select the :guilabel:`Statement Type`: :guilabel:`Normal`, or :guilabel:`Complementary` or
   :guilabel:`Substitutive` to correct a declaration already filed. For the last two, enter the
   :guilabel:`Previous declaration number`.
#. Click :guilabel:`Calculate`. The boxes of the declaration are computed from the posted journal
   items of the period. Open the :guilabel:`Tax lines` tab, and use the button at the end of a line
   to see the journal items that make up the amount of a box.
#. Fill in the boxes that are not computed automatically, if any, then click
   :guilabel:`Recalculate` if you changed accounting data in the meantime.
#. Click :guilabel:`Confirm` when the amounts are correct.
#. For the declarations that create a regularization entry (the modelos 303, 369 and 202), click
   :guilabel:`Create move` to post it: it moves the balances of the tax accounts to the counterpart
   account. Use :guilabel:`Show move` to open it. The other declarations have no entry.
#. Click :guilabel:`Export to BOE`, then :guilabel:`Export` in the dialog, and download the file to
   upload it in the AEAT electronic office.

.. screenshot:: finance-fl-spain-aeat-303
   :menu: Accounting ‣ Reporting ‣ AEAT ‣ AEAT 303 model ‣ (a calculated declaration)
   :shows: A calculated modelo 303 of the third quarter: header with Year, Period Type "3T", Statement Type "Normal", the journal and counterpart account, the result section with the result type, and the "Tax lines" tab listing the boxes and their amounts; buttons Recalculate, Confirm and Cancel in the header.
   :highlight: The "Calculate"/"Confirm" buttons and the "Tax lines" tab.
   :data: Spanish demo company with sales and purchases in the quarter.
   :module: l10n_es_aeat_mod303, l10n_es_aeat
   :notes: English UI, light theme, 1440px width.

.. important::
   The regularization entry is dated on the last day of the period. If this date is in a locked
   period, a warning banner is shown on the declaration as soon as it is opened (while it is not
   posted). The :guilabel:`Global Lock Date` and the :guilabel:`Hard Lock Date` prevent the entry
   from being created: :guilabel:`Create move` shows an error. The :guilabel:`Tax Return Lock Date`
   only shows the warning. Create the declaration entry before locking the period, or ask an
   adviser to move the lock date.

.. note::
   A banner also warns when active taxes used in the period are not in any AEAT tax map, as they
   are left out of the declaration. Click :guilabel:`Show taxes` to list them, and see
   :ref:`localizations/spain/aeat/tax-map`.

.. note::
   The files of the self-assessment returns (modelos 303, 390, 111, 115, 123, 130, 202 and 216)
   declare, in the field of the software developer of the AEAT file design, the software producer
   of the fork. It is the same producer as the one declared for Veri*Factu.

Specific declarations
---------------------

Modelo 303
   The :guilabel:`Result Type` shows whether the result is to be paid, returned, or compensated in
   later periods. The amount to compensate from previous periods is proposed from the previous
   declarations. In the last period of the year (4T or month 12), indicate whether the company is
   exempt from the modelo 390, and if so, fill in the additional data of the activities.

   For a company under the :ref:`cash accounting regime <localizations/spain/cash-accounting>`, the
   operations are reported in the boxes of their ordinary tax when they accrue: on collection or
   payment, and at the latest on 31 December of the following year. Boxes [62] and [63] (sales) and
   [74] and [75] (purchases) also report, for information, the base and the VAT of these operations
   when they would have accrued under the general rule, that is on the invoice date. These four
   boxes are not part of the result of the declaration.

Modelo 390
   The annual summary is computed for the whole year. Fill in the fields that are not computed
   automatically before confirming it.

   Under the :ref:`cash accounting regime <localizations/spain/cash-accounting>`, the VAT accrued
   in the year, including the accruals on 31 December of the following year, is reported in boxes
   [643] to [648] (base and VAT at 4 %, 10 % and 21 %) and no longer in boxes [01] to [06]. The
   total VAT of box [34] includes their VAT amounts.

Modelos 111 and 115
   The withholdings are computed from the withholding taxes of the vendor bills. In the modelo 111,
   fill in the boxes that Odoo cannot compute, such as the work income paid outside Odoo. The
   in-kind withholdings of professional activities, such as *7% Withholding income tax in cash* and
   *15% Withholding income tax in cash*, are reported in boxes [11] and [12]. The annual summaries
   are the modelos 190 (for the 111) and 180 (for the 115, see
   :ref:`localizations/spain/aeat/mod180`).

Modelo 347
   After :guilabel:`Calculate`, the :guilabel:`Partner records` tab lists the partners whose
   operations exceed the threshold; a record shown in red misses data needed for the declaration.
   Click :guilabel:`Send emails` to send each partner its record for verification, and use
   :guilabel:`Confirm as valid` when a partner agrees. Real estate rentals not declared in the
   modelo 115 can be added in the :guilabel:`Real Estate records` tab. To exclude a contact from
   the declaration regardless of its amounts, tick :guilabel:`Not included in 347 report` on the
   contact form.

   Under the :ref:`cash accounting regime <localizations/spain/cash-accounting>`, the operations of
   a partner with VAT due on payment (a company under the regime, or a supplier flagged as under the
   regime) are marked in the record: in the :guilabel:`Partner info` tab of the partner record,
   :guilabel:`Cash Basis Operation` is ticked and :guilabel:`Cash basis amount` shows the amount
   accrued in the year under the regime. These are the positions 281 and 284 to 299 of the file.
   The entries that accrue the VAT do not repeat the invoices in the annual amount.

Modelo 349
   The :guilabel:`Partner records` and :guilabel:`Refunds from other periods` tabs list the
   intra-community operations of the period. Delete the operations that must not be declared from
   these tabs before confirming.

Modelo 369
   The OSS return is computed from the OSS taxes of the distance sales to consumers of other EU
   countries.

Modelos 123, 216 and 296
   Like the modelos 111 and 115, they are computed from the withholding taxes of the vendor bills.
   The modelo 296 is the annual summary of the 216.

Modelos 180, 193 and 202
   See :ref:`localizations/spain/aeat/annual-summaries`.

.. _localizations/spain/aeat/annual-summaries:

Annual summaries and company returns
====================================

.. _localizations/spain/aeat/mod180:

Modelo 180: annual summary of rent withholdings
-----------------------------------------------

The modelo 180 is the informative return that summarizes, for the year, the withholdings on urban
property rents that you declared in the modelo 115: it lists each landlord and each rented
property with the base and the withholding. It has no amount to pay or to return, and it creates no
accounting entry.

**Before you start**

- The landlords are contacts with a VAT number and a ZIP code: the first two digits of the ZIP code
  give the province of the recipient in the file.
- The rented properties are recorded under :menuselection:`Accounting --> Configuration --> AEAT
  --> Real Estates` with the cadastral reference, the address, the city and the ZIP code. This menu
  and the :guilabel:`Real Estate` field of the invoice lines are shown to the users of the *Use AEAT
  Real Estates* group.
- Each rent line of the vendor bills uses one of the leases withholding taxes (*19% Withholding
  (leases)*, *19.5% Withholding (leases)*, *20% Withholding (leases)* or *21% Withholding
  (leases)*) and has its property in the :guilabel:`Real Estate` field.

**Prepare the declaration**

#. Go to :menuselection:`Accounting --> Reporting --> AEAT --> AEAT 180 model`, click
   :guilabel:`New` and select the :guilabel:`Year`. The contact data are proposed as for any other
   declaration.
#. Click :guilabel:`Calculate`. The result section shows the number of recipients ([01]), the base
   and the withholdings of the year ([02] and [03]), and the sign of the amounts.
#. Open the recipient records tab (:guilabel:`Registro de perceptores`): there is one record per
   landlord, property and withholding rate, with the base, the withholding, the percentage and the
   accrual year. Click the magnifier of a record to see the journal items of its base. You can
   correct a record in its form.
#. Click :guilabel:`Confirm`, then :guilabel:`Export to BOE` to get the file.

.. note::
   Some labels of this declaration are displayed in Spanish, for example the boxes
   :guilabel:`Base retenciones e ingresos a cuenta` and :guilabel:`Retenciones e ingresos a
   cuenta`, and the tabs :guilabel:`Líneas de impuestos` and :guilabel:`Registro de perceptores`.

.. important::
   - The number of recipients [01] is the number of records: a landlord with two properties, or
     with two withholding rates, counts twice. It is also the number of recipient records of the
     file.
   - A line without a property is included in the boxes [02] and [03], but it produces no
     recipient record: fill in the :guilabel:`Real Estate` field of every rent line before
     calculating, otherwise the records do not add up to the boxes.
   - :guilabel:`Calculate` and :guilabel:`Recalculate` delete and recreate all the records: do the
     corrections after the last calculation.
   - The declaration is an informative return: it is confirmed without a bank account or a result
     type.

**The BOE file.** It contains one declarant record and one recipient record per line of the
recipient records tab, all of 500 positions and ending with a line break. The recipient
identification comes from the contact (VAT number, name, and the province from the ZIP code) and the
property data from the real estate record (cadastral reference, address, municipality and ZIP code,
from which the province is taken). A blank province or municipality means that the ZIP code or the
city is missing on the contact or on the property.

.. _localizations/spain/aeat/mod193:

Modelo 193: annual summary of investment income withholdings
------------------------------------------------------------

The modelo 193 is the annual informative return of the withholdings on investment income that a
company paid to its partners or lenders: dividends, interest of loans and other income. It is
computed from the same withholding taxes as the quarterly modelo 123, so that its total can be
compared with the 123 returns of the year. It creates no accounting entry.

.. list-table::
   :header-rows: 1
   :widths: 50 20 30

   * - Withholding tax
     - Perception key
     - Nature
   * - *19% Withholding (dividend distribution)*
     - A
     - 02
   * - *19% Withholding (loans)*
     - B
     - 03
   * - *24% Withholding on capital*
     - C
     - 06
   * - *19% Withholding Directors and Administrators (Purchase company director)*
     - C
     - 10

**Prepare the declaration**

#. Go to :menuselection:`Accounting --> Reporting --> AEAT --> AEAT 193 Model`, click
   :guilabel:`New` and select the :guilabel:`Year`.
#. Set the :guilabel:`Declarant Nature`. :guilabel:`Other declarant (not a paying agent, depositary
   or issuer)` is the usual case of a company that pays dividends or interest directly to its
   partners or lenders. :guilabel:`Paying agent, depositary, issuer or entity of art. 26.1.a)
   LIRPF` also shows the :guilabel:`Payment` and :guilabel:`Penalties` data of the records and the
   box :guilabel:`Withholdings paid in`.
#. Click :guilabel:`Calculate`. There is one record per recipient, perception key and nature in the
   :guilabel:`Partner records` tab. A record shown in red misses its VAT number, its province code
   or a two-digit nature.
#. Review and correct the records, if needed: the VAT number and the province code (taken from the
   contact; :guilabel:`98` for a foreign contact), the nature, the :guilabel:`Perception Type`
   (:guilabel:`Monetary` or :guilabel:`In kind`) and, for the key A, the :guilabel:`Accrual Date`
   of the dividend (proposed as the last entry date; use the payment date of the distribution
   agreement).
#. Compare the :guilabel:`Withholdings` with the :guilabel:`Withholdings of the 123 returns` in the
   summary, which adds up the total of the 123 returns of the year that are not in draft or
   cancelled. Investigate any difference before confirming.
#. Click :guilabel:`Confirm`, then :guilabel:`Export to BOE`. The confirmation is refused while a
   record is incomplete.

.. screenshot:: finance-fl-spain-aeat-193
   :menu: Accounting ‣ Reporting ‣ AEAT ‣ AEAT 193 Model ‣ (a calculated declaration)
   :shows: A calculated modelo 193 of the last year: header with Year, Statement Type "Normal", Declarant Nature "Other declarant" and the "Manual records" checkbox; the summary with Number of recipients, Withholding base, Withholdings and Withholdings of the 123 returns; the "Partner records" tab with a recipient of the key A (nature 02), one of the key B (nature 03), and one record in red with a missing province code.
   :highlight: The "Withholdings" and "Withholdings of the 123 returns" fields.
   :data: Spanish demo company with dividend and loan withholdings paid to partners.
   :module: l10n_es_aeat_mod193, l10n_es_aeat_mod123, l10n_es_aeat
   :notes: English UI, light theme, 1440px width.

.. important::
   - Tick :guilabel:`Manual records` to keep the records when you recalculate, for example after
     correcting them by hand. Otherwise :guilabel:`Calculate` and :guilabel:`Recalculate` delete
     and recreate all the records, and your corrections are lost. Tick it after the first
     calculation: with the box ticked, :guilabel:`Calculate` creates no record.
   - The records can only be edited while the declaration is :guilabel:`Processed`.
   - The nature and the perception key assigned to the *24% Withholding on capital* (key C, nature
     06) must be checked for each case, as must the keys of any other tax mapped by hand.
   - The records of expenses of the depositary entities (art. 26.1.a) LIRPF) and the information on
     securities (ISIN code, securities account, securities loan) are not generated: they are
     exported with zeros or blanks, as is the distribution of the withholdings by tax
     administration.

The BOE file follows the record design of 2025 and later years: one declarant record and one
recipient record per line of the :guilabel:`Partner records` tab, of 500 positions each.

.. _localizations/spain/aeat/mod202:

Modelo 202: corporate income tax instalments
--------------------------------------------

The modelo 202 is the instalment payment (*pago fraccionado*) of the corporate income tax. There
are three instalments per tax period:

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Period
     - Filed in
     - Covers
   * - 1P
     - April
     - The first 3 months, until 31 March.
   * - 2P
     - October
     - The first 9 months, until 30 September.
   * - 3P
     - December
     - The first 11 months, until 30 November.

Two modalities exist, chosen in the :guilabel:`Modality` field, which can only be changed while the
declaration is a draft:

- :guilabel:`Art. 40.2 LIS: 18% of the last tax`: 18 % of the tax of the last tax period whose
  filing deadline has expired;
- :guilabel:`Art. 40.3 LIS: result of the period`: the accounting result of the first months of the
  tax period, adjusted. It is mandatory for a company whose turnover of the 12 previous months is
  over 6 million euros: tick :guilabel:`Turnover over 6 million euros` and the first modality is
  refused.

**Prepare the declaration**

#. Go to :menuselection:`Accounting --> Reporting --> AEAT --> AEAT 202 Model` and click
   :guilabel:`New`. The period is proposed from today's date: 1P from April to September, 2P in
   October and November, 3P in December, and the 3P of the previous year from January to March.
   :guilabel:`Start of the tax period` is proposed from the fiscal year of the company; correct it
   if the tax period started on another date.
#. In :guilabel:`Company data`, choose the :guilabel:`Modality` and fill in the data of the entity:
   the :guilabel:`CNAE` code, the :guilabel:`Corporate income tax rate (%)` (25 % by default), the
   :guilabel:`Turnover of the previous 12 months` band, and the boxes of the special regimes that
   apply, if any.
#. Click :guilabel:`Calculate`, then fill in the boxes below.

**Modality of art. 40.2 LIS.** Enter :guilabel:`[01] Instalment base` from the modelo 200 of the
last tax period whose deadline has expired (the tax, minus deductions, bonuses, withholdings and
payments on account). :guilabel:`[03] To pay` is 18 % of it. For a complementary declaration, enter
the result of the previous declaration in :guilabel:`[02] Result of the previous declaration`.

**Modality of art. 40.3 LIS.** Odoo computes from the accounting, from the start of the tax period
to the end of the months of the instalment:

- :guilabel:`[04] Accounting result after taxes`: profit and loss accounts of the groups 6 and 7;
- :guilabel:`[05]` and :guilabel:`[06]` corporate income tax, increases and decreases: accounts 630,
  633 and 638;
- :guilabel:`[28] Withholdings and payments on account`: debit balance of the accounts 473, without
  the entries of the 202 declarations;
- :guilabel:`[30] Instalments of previous periods`: the instalments of the same tax period of the
  202 declarations of this modality that are confirmed or posted.

All the other adjustments (other adjustments [07] and [08], 30 % of the depreciation [37],
capitalization and levelling reserves, offset of negative tax bases [14], bonuses [27] and the
others) are entered by hand. :guilabel:`[17] Percentage` is proposed from the tax rate: 5/7 of the
rate rounded down, or 19/20 of the rate rounded up when the turnover is at least 10 million euros
(17 % and 24 % for a rate of 25 %). If the entity applies several tax rates, tick :guilabel:`Several
tax rates`: the instalment is then entered per rate. :guilabel:`[33] Minimum payment` is only
shown for a turnover of at least 10 million euros and is entered by hand. :guilabel:`[34] To pay` is
the result [32] or the minimum payment if it is higher.

.. screenshot:: finance-fl-spain-aeat-202
   :menu: Accounting ‣ Reporting ‣ AEAT ‣ AEAT 202 Model ‣ (a calculated declaration)
   :shows: A calculated modelo 202 of the period 2P with the "Company data" block (Modality "Art. 40.3 LIS: result of the period", CNAE, tax rate 25, turnover band) and the "Art. 40.3 LIS modality" block with the boxes [04], [05], [17] "Percentage", [28], [32] and [34] "To pay"; buttons Recalculate, Confirm and Cancel in the header.
   :highlight: The boxes [17] Percentage and [34] To pay.
   :data: Spanish demo company with a profit and loss result in the first nine months.
   :module: l10n_es_aeat_mod202, l10n_es_aeat
   :notes: English UI, light theme, 1440px width.

**Confirm and pay**

#. Check the :guilabel:`Declaration type`, proposed from the result: :guilabel:`Nil` when there is
   nothing to pay, :guilabel:`Direct debit` when a bank account is set, :guilabel:`Payment`
   otherwise. You can change it while the declaration is not confirmed.
#. Click :guilabel:`Confirm`. A complementary declaration needs the result of the previous
   declaration ([02] or [31]).
#. When there is an amount to pay, click :guilabel:`Create move`: the instalment entry debits the
   :guilabel:`Payments on account account` (473 by default) and credits the
   :guilabel:`Counterpart account` (4752 by default), in the :guilabel:`Journal` of the
   declaration, dated on the last day of the period. Fill in the three fields if they are empty.
#. Click :guilabel:`Export to BOE`. The file follows the record design DR202 in force from 2025
   (version 1.3).

.. warning::
   Have the following checked by your tax adviser before filing: the proposed percentage [17], the
   minimum payment [33] and the formula of the result [32] are not verified for every case. The
   additional information of the declaration (debt waivers, Canary Islands investment reserve,
   special economic zone, and similar) is exported with zeros.

.. _localizations/spain/aeat/vat-book:

VAT and IRPF books
==================

Go to :menuselection:`Accounting --> Reporting --> AEAT --> Libros del IVA y del IRPF` and create a
book for the period, then click :guilabel:`Calculate`. The :guilabel:`Issued Invoices` and
:guilabel:`Received Invoices` tabs list the invoices with their taxes; the :guilabel:`Summary` tab
totals them per tax. Click :guilabel:`View Issued Invoices` or :guilabel:`View Received Invoices` to
display the books. Click :guilabel:`Export draft` to download them as an XLSX file; after
:guilabel:`Confirm`, the final file is downloaded with :guilabel:`Export BOE`.

Under the :ref:`cash accounting regime <localizations/spain/cash-accounting>`, the invoices with VAT
due on payment are booked once, on the day of the invoice, and their collections and payments are
recorded in the *Cobro/Pago (Operación Criterio de Caja)* columns of the XLSX file (RIVA art. 61
decies): one row per collection or payment, with its date, its amount, the means and the account.
The first one is on the row of the invoice, the following ones on additional rows that repeat the
identification of the invoice. Refunds give negative amounts. The means use the codes of the AEAT
format: 01 transfer, 02 cheque, 03 not collected or paid (the accrual on 31 December of the
following year), 04 other means (including an invoice reconciled with a refund) and 05 direct
debit. The entries that accrue the VAT are not booked as invoices.

.. _localizations/spain/aeat/annual-accounts:

Official annual accounts (PGC)
==============================

The official Spanish balance sheet and profit and loss, in the format of the annual accounts filed
with the Mercantile Registry, are available under :menuselection:`Accounting --> Reporting -->
Annual Accounts (PGC)`:

- :guilabel:`Balance Sheet (PGC)`;
- :guilabel:`Profit and Loss (PGC)`.

The menu is shown to the accountants and to the users with read-only accounting access. The report
of the current company opens directly, with two columns of calendar years, :guilabel:`Current year`
and :guilabel:`Previous year`, based on the posted entries only. The template (SMEs, complete, or
non-profit entities) follows the chart of accounts of the company. Click an amount to see the
journal items behind it, and use :guilabel:`Print` or :guilabel:`Export` to get a PDF or XLSX file.

The two reports of a company are created when the module is installed, when a Spanish chart of
accounts is loaded, or the first time the menu is opened. Accountants and advisers can also add
annotations to the report.

.. note::
   Only accounts numbered according to the PGC are included. An account with a custom code that is
   not a sub-account of a PGC account is not included in the report.

.. seealso::
   - :doc:`../spain`
   - :doc:`../../accounting/reporting`

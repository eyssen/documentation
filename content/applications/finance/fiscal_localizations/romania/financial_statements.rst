.. _localizations/romania/financial_statements:

==================================
Annual financial statements (ANAF)
==================================

The :guilabel:`Romania - Financial Statements (Situații financiare, ANAF)`
(`l10n_ro_financial_statements`) module prepares the annual financial statements and the accounting
reports of Romanian companies, forms **S1002**, **S1003**, **S1004** and **S1005**, and the
half-year report **S1027**. The forms are computed from the accounting, checked with the official
consistency rules of the ANAF structure, and exported as the XML files that ANAF defines for the
financial statements of the 2025 financial year (**OMF 2036/2025**; the half-year report follows
**OMF 1194/2025**).

This page describes the specific features of the financial statements. The general flow of the
Romanian declarations (statuses, deadlines, DUK validation, filing) is described in
:doc:`declarations`.

Which statement applies
=======================

.. list-table::
   :header-rows: 1
   :widths: 12 48 40

   * - Form
     - Content
     - Who files it
   * - S1002
     - F10 balance sheet (103 rows), F20 profit and loss account (70 rows), F30 informative data,
       F40 fixed assets.
     - Medium and large entities, and public interest entities.
   * - S1003
     - F10 abridged balance sheet (49 rows), F20 profit and loss account (70 rows), F30, F40.
     - Small entities.
   * - S1005
     - F10 abridged balance sheet (49 rows), F20 profit and loss account of micro-entities (9
       rows), F30 with chapter XIX, F40.
     - Micro-entities.
   * - S1004
     - Same content as S1002, filed as an annual accounting report.
     - Entities that file an annual accounting report instead of annual financial statements
       (art. 27, entities in liquidation, branches of entities of the European Economic Area...).
       Select the reason in :guilabel:`Reason of the Annual Report`.
   * - S1027
     - F10 abridged balance sheet, F20, F30 at 30 June.
     - Half-year accounting report. The structure bundled is the one of 30 June 2025; the half-year
       report was eliminated for 2026, and Odoo shows a warning for a 2026 report.

The form depends on the **category of the entity**, which Odoo helps to determine in the
:guilabel:`Classification` tab. The thresholds are those of OMFP 1802/2014 as amended by OMF
4164/2024; an entity belongs to a category when it does **not exceed two of the three limits** at
the balance sheet date:

.. list-table::
   :header-rows: 1
   :widths: 30 23 23 24

   * - Category
     - Total assets
     - Net turnover
     - Average number of employees
   * - Micro-entity (S1005)
     - 2,250,000 lei
     - 4,500,000 lei
     - 10
   * - Small entity (S1003)
     - 25,000,000 lei
     - 50,000,000 lei
     - 50
   * - Medium or large entity (S1002)
     - above the limits of small entities
     - above the limits of small entities
     - above the limits of small entities

Public interest entities always file the full statements (S1002). A small entity may also opt for
the full format.

Configuration
=============

:ref:`Install <general/install>` the :guilabel:`Romania - Financial Statements (Situații financiare,
ANAF)` module. It installs the Romanian accounting registers (:doc:`statutory_registers`) as a
dependency, because the balances come from their trial balance. The :doc:`D101 <d101>` module uses
the same computation.

Before the first statements, check:

- the company data of the :ref:`declarations <localizations/romania/declarations/configuration>`
  (declarant, main CAEN code);
- the **state** (county) of the address of the company: the statements need the ANAF county code,
  which is derived from it, and the validation fails without it;
- the **Company ID** (trade register number, for example `J12/1234/2010`) of the company, which is
  copied to the statements.

Accountants with the adviser (manager) access right can review the definition of the forms in
:menuselection:`Accounting --> Romania (ANAF) --> Configuration`:
:guilabel:`Financial Statement Rows` (the rows of each form, with the account expression that
computes them, which is editable data) and :guilabel:`Financial Statement Checks` (the official
consistency rules).

Prepare the financial statements
================================

#. Go to :menuselection:`Accounting --> Romania (ANAF) --> Declarations --> Financial Statements`
   and click :guilabel:`New`.
#. Choose the :guilabel:`Form` and the :guilabel:`Year`. For the half-year report (S1027), the
   period is the first half-year of the year. The :guilabel:`Deadline` is 150 days after the end of
   the year (45 days for the half-year report), moved to the next working day.
#. In the :guilabel:`Classification` tab, enter the :guilabel:`Average Number of Employees` and the
   number of employees at year end, for the current and the previous year, then click
   :guilabel:`Compute`. Odoo shows the :guilabel:`Total Assets`, :guilabel:`Net Turnover` and the
   :guilabel:`Suggested Category`. Confirm the category with :guilabel:`Use Suggested Category`, or
   select it in :guilabel:`Entity Category` and tick :guilabel:`Category Confirmed`; the form
   follows the category. Tick :guilabel:`Public Interest Entity` where it applies.
#. Check the :guilabel:`Header` tab: trade register number, CAEN codes, county code, form of
   ownership, the :guilabel:`Administrator`, the person who prepared the statements
   (:guilabel:`Prepared by`, :guilabel:`Preparer Quality`), the audit data and the flags. The
   statements must be :guilabel:`Approved according to the Law` before they are filed.
#. Review the tabs :guilabel:`F10 Balance Sheet`, :guilabel:`F20 Profit and Loss`,
   :guilabel:`F30 Informative Data` and :guilabel:`F40 Fixed Assets`. Fill in the manual data and the
   adjustments (see below), and click :guilabel:`Recompute` to refresh the totals.
#. Click :guilabel:`Validate`, resolve the errors, then click :guilabel:`Export XML`. The button
   :guilabel:`Print Summary` prints a summary of the statements.
#. Complete the filing outside Odoo (see below) and click :guilabel:`Mark as Submitted`.

How the amounts are computed
----------------------------

The account balances are **not computed by this module**. They come from the computation of the
Romanian **trial balance** (*Balanța de verificare*) of the accounting registers, the single place
where Odoo computes the Romanian account balances. The trial balance, the general ledger, the account
sheet, the inventory register, the financial statements, the :doc:`D101 <d101>` and the
micro-enterprise tax therefore always show the same figures. Only the **posted** journal entries are
included.

F10 balance sheet
   Closing balances of the trial balance at the end of the period. Column 1 is the end of the previous
   financial year (the beginning of the year) and column 2 the end of the period. The income and
   expense accounts (classes 6 and 7) are not balance sheet accounts: the result of the year that is
   not yet closed into account 121 is added to a virtual account 121, and the unclosed results of
   earlier years to a virtual account 117 (retained earnings). The account class decides, not the
   type of the account in Odoo.

F20 profit and loss account
   The turnovers of the period of the income and expense accounts (the previous year in column 1).
   The entries that close the accounts of classes 6 and 7 into account 121 are excluded when
   :guilabel:`Exclude Result Closing Entries` is ticked (the default), so that the statements are
   the same before and after the closing of the year.

F40 fixed assets
   Opening balance and debit and credit turnovers of the year per group of accounts: gross values,
   depreciation and impairment adjustments. The column "of which disposals" is manual.

.. note::
   The trial balance itself carries the unclosed result of earlier years to account 121 in its
   opening balance, while the statements show it in account 117. This is expected: the totals of
   equity agree.

Adjustments and manual rows
---------------------------

Each row and column has three values: the :guilabel:`Computed` value, an :guilabel:`Adjustment` that
you can type, and the resulting amount (:guilabel:`Col. 1`, :guilabel:`Col. 2`...). Adjustments are
kept when the statements are recomputed. Use the :guilabel:`All Rows` button to see and filter all
the rows of the statements in one list, and the journal items icon of a row to open the entries
behind it.

Four kinds of data need your attention:

- **Accounts to be split by nature.** Some accounts of the official form must be divided between two
  rows (for example, the debts due within and after one year, the prepaid items and the short and
  long term parts of 267, 296, 471, 472, 475 and 478). Odoo puts the whole balance in the first row
  of the official balance import; enter the other part as an **adjustment** in both rows.
- **Manual rows.** The rows with the computation :guilabel:`Manual`, mostly in the F30 informative
  data, hold data that the accounting cannot provide: arrears, research and development, dividends,
  public ownership data, the "of which ... affiliated entities" rows and the long-term debts. Fill
  them in as adjustments.
- **Derived cells.** The F30 chapter I (profit or loss of the unit) is derived from the F20, and the
  chapter III from the employee numbers of the :guilabel:`Classification` tab.
- **Column "of which disposals" of the F40.**

Checks
------

The validation of the statements runs the official rules of the ANAF structure (totals, signs, F10 =
F20 result, A+B+C-D-G-H-I = equity, F10 against F40, F20 against F30 for micro-entities) and, besides
them:

- **Result of the year.** If the result of the F10 (account 121) differs from the net result of the
  F20, check that the result of the previous year was transferred from 121 to 117 or 129 and that
  all the closing entries are posted.
- **Coverage.** A warning lists the accounts with a closing balance (classes 1 to 5) that no row of
  the balance sheet takes into account (for example, the VAT accounts 4426 and 4427 not settled into
  4423 or 4424), and the income and expense accounts that no row of the F20 reports.
- **Previous year.** The opening balances are compared with the closing balances of the statements
  already prepared for the previous year.
- **Header and classification.** Trade register number, CAEN codes (4 digits), county code,
  administrator and preparer, fiscal code and CECCAR registration of an authorised preparer, LEI
  code, auditor, the reason of the S1004, and the match between the form and the confirmed category.
- **Period.** Draft journal entries of the period are not included (a warning gives their number), a
  warning appears if the financial year is not locked (set the lock date in the accounting settings
  once the statements are final), and the forms require a financial year 2025 or later.

Corrections and limits
----------------------

Click :guilabel:`Create Rectificative` on an exported or submitted statement to prepare a corrected
version. The statements follow the calendar year: for a financial year that differs from the calendar
year, use the S1004 and adjust the amounts.

The following are **not** produced by Odoo: the notes to the financial statements, the statement of
changes in equity, the cash flow statement and the reports (management report, auditor report,
approval), consolidated statements (S1030), IFRS statements, the forms of banks, insurers and
financial investment companies (ASF), and the declaration of inactive entities (S1046).

.. _localizations/romania/financial_statements/filing:

XML validation and filing
-------------------------

The XML is validated against the XSD schemas published by ANAF for the forms (bundled unmodified),
and with DUKIntegrator if the :ref:`DUK validator service <localizations/romania/declarations/duk>` is
configured (install the validators of the forms `S1002`, `S1003`, `S1004`, `S1005` and `S1027` that
you use). The validation is done **without the PDF**: the official PDF of the financial statements
contains the mandatory ZIP file of the annexes (notes, reports, approval), which is assembled with
the ANAF assistance program and not with Odoo.

.. important::
   Odoo does not send the financial statements to ANAF. The filing package, with its annexes, is
   prepared and filed outside Odoo (see :ref:`localizations/romania/declarations/filing`).

.. seealso::
   - :doc:`declarations`
   - :doc:`d101`
   - :doc:`statutory_registers`

==================
Non-deductible VAT
==================

Some purchases give no right, or only a limited right, to deduct the VAT: passenger cars
(deduction limited to 50% by article 298 of the Fiscal Code), or goods and services that are not
used for taxable operations (article 297). The :guilabel:`Romania - Non-deductible VAT`
(`l10n_ro_nondeductible_vat`) module adds the purchase taxes and the fiscal position needed to
record them, and makes sure that the non-deductible part is reported correctly in the
:doc:`VAT return (D300) <d300>`.

The module only creates its data for companies that use the Romanian chart of accounts
(`ro`). It can be installed in a database that already contains Romanian companies: the taxes are
then created for them at once.

.. _localizations/romania/nd-taxes:

Taxes
=====

The Romanian chart of accounts (`l10n_ro`) already contains the *VAT 21% Non-deductible 50%* and
*VAT 11% Non-deductible 50%* taxes (labels `21% ND 50%` and `11% ND 50%`), where the deductible
half goes to the deductible VAT account and the non-deductible half is posted to account `6352`.
The module adds the variants that the chart does not have. All of them are purchase taxes of the
*Non-deductible VAT* tax group, with a 21% or an 11% rate.

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Tax
     - Deductible part
     - Non-deductible part
   * - `21% Ded. 50% (cost)`, `11% Ded. 50% (cost)`
     - 50%, to the deductible VAT account (`4426`).
     - 50%, added to the cost: posted to the account of the invoice line (an expense or a fixed
       asset account), as OMFP 1802/2014 requires.
   * - `21% Non-deductible (cost)`, `11% Non-deductible (cost)`
     - None.
     - 100%, added to the cost: posted to the account of the invoice line.
   * - `21% Non-deductible (6352)`, `11% Non-deductible (6352)`
     - None.
     - 100%, posted to the account `6352`.
   * - `21% ND 50%`, `11% ND 50%` (core `l10n_ro`)
     - 50%, to the deductible VAT account.
     - 50%, posted to the account `6352`.

Use the tax that matches the accounting policy of the company: *(cost)* when the VAT of a vehicle
or of an asset has to increase the value of the item, *(6352)* when it is booked as an expense.

.. _localizations/romania/nd-fiscal-position:

Fiscal position
===============

The :guilabel:`Limited VAT deduction 50% (art. 298)` fiscal position replaces the standard
deductible 21% and 11% purchase taxes with the `Ded. 50% (cost)` taxes. It is **not** applied
automatically. To record a purchase of a vehicle, select it in the :guilabel:`Fiscal Position`
field of the vendor bill (or of the purchase order) before you add the lines.

Reporting in the D300
=====================

The VAT return reports the full amount of a purchase, deductible or not:

- the full base and the full VAT are reported in the purchase rows `24` (21%) and `25` (11%);
- the non-deductible part of the VAT also carries the `ND - VAT` tax grid. It is shown in the
  memo line :guilabel:`ND - VAT - Non-deductible VAT included in rows 20-28 (art. 297-298
  limitation, memo)` of the Romanian tax report, and it is
  subtracted from the row `31` (sub-total of the deducted VAT) and from the
  row `35` (total of the deducted VAT);
- on credit notes, the signs of all the grids are reversed.

The tax lines of the non-deductible part are excluded from the tax closing entry, since they are
posted to an expense or an asset account and not to a VAT account.

.. seealso::
   :doc:`d300`

.. _localizations/romania/core-tax-fixes:

Corrections of the core Romanian localization
=============================================

The same release corrects three points of the standard `l10n_ro` module. The corrections are
applied to the existing Romanian companies when the module is upgraded, without deleting or
rewriting any posted journal item. They are listed in detail in the file
:file:`addons/l10n_ro/EYSSEN_CHANGES.md` of the source code.

VAT on collection taxes
-----------------------

The *VAT on collection* taxes for 21%, 11% and 9% (article 3) had inverted signs on their tax
grids, so that the VAT collected on payment appeared as a negative amount in the tax report. They
now behave like the other sales taxes: positive on invoices and negative on credit notes. The
journal items posted before the upgrade keep the grids they were posted with; the new signs
apply to the entries created afterwards. The D300 amounts stay correct for both, because the
:doc:`D300 <d300>` is computed from the tax codes of the taxes.

50% non-deductible taxes
------------------------

On `21% ND 50%` and `11% ND 50%`, only the deductible half carried the grid of the purchase row,
so that rows `24` and `25` showed half of the VAT and row `31` was equal to row `30`. The
non-deductible half now carries both the grid of the row and the `ND - VAT` grid, as described
above. Entries posted before the upgrade have no `ND - VAT` grid, so the figures of the past
periods do not change.

Account types of contra-asset and deferred-income accounts
----------------------------------------------------------

The chart of accounts typed the depreciation accounts (`28x`), the impairment accounts (`29x`),
the deferred investment subsidies (`475x`) and the deferred income from transferred assets
(`478x`) as income or expense accounts. They are balance sheet accounts: with the former types,
their balances appeared in the profit and loss report and were carried into the unallocated
earnings, so that the balance sheet did not balance. They are now typed as non-current or fixed
assets (`28x`, `29x`) and as current or non-current liabilities (`475x`, `478x`).

.. important::
   - Accounts that you customized (a code that no longer starts with the code of the chart, or a
     type that you changed) are left untouched.
   - Reports are computed from the account types at the time you run them. After the upgrade, the
     balance sheet of **past** periods therefore shows these accounts under their new types.
     Documents that you printed or filed earlier are not changed.
   - An account is **not** retyped if a posted entry has moved its balance to the result (an
     entry with a line on `121x` or `117x`), for example a manual year-end closing made while the
     account was typed as a profit and loss account. The upgrade logs a message starting with
     `l10n_ro 1.3` for each such account. Review these entries (normally reverse the part that
     closed the account to `121`), then set the account type yourself in
     :menuselection:`Accounting --> Configuration --> Chart of Accounts`.
   - The Romanian :doc:`financial statements <financial_statements>` and the :doc:`SAF-T D406
     <saft_d406>` work from the account numbers and are not affected by the types.

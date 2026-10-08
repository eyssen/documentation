=============================
Romanian statutory registers
=============================

Romanian companies must keep a set of accounting registers and make them available to the tax
authorities (OMFP 2634/2015, OMFP 1802/2014 and the Fiscal Code). The `l10n_ro_dynamic_reports`
module provides them as :doc:`dynamic reports <../../accounting/reporting/dynamic_reports>`, with
the Romanian layouts and columns.

.. note::
   The registers only read the companies whose **fiscal country** is Romania. They are available to
   users who have the :guilabel:`Romanian Localization User` group and the accounting
   :guilabel:`Accountant` access right.

.. _localizations/romania/registers/open:

Open a register
===============

Go to :menuselection:`Accounting --> Reporting --> Dynamic Reports --> Romania` and select the
register:

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Menu
     - Romanian name
     - Legal purpose
   * - :guilabel:`Trial Balance`
     - *Balanța de verificare*
     - Checks that debits equal credits, and summarizes every account.
   * - :guilabel:`General Journal`
     - *Registru jurnal*
     - Chronological record of all the accounting entries.
   * - :guilabel:`Account Sheets`
     - *Fișa de cont*
     - Detail of the entries of one or more accounts, with the running balance.
   * - :guilabel:`General Ledger`
     - *Cartea mare*
     - Systematic record of the turnover and balances of each account.
   * - :guilabel:`Sales Journal`
     - *Jurnal de vânzări*
     - VAT record of the sales invoices, the base of the D300 return.
   * - :guilabel:`Purchase Journal`
     - *Jurnal de cumpărări*
     - VAT record of the purchase invoices, the base of the D300 return.
   * - :guilabel:`Inventory Register`
     - *Registru inventar*
     - Balance sheet accounts at the end of the period, to compare with the stock-taking.

If you select no Romanian company in the company switcher, the report does not open and asks you to
select one. If you select several Romanian companies, the accounts are merged by account code.

.. tip::
   The report titles end with *(Romania)*, for example :guilabel:`General Journal (Romania)`.

Filters
=======

All the registers have the following filters:

- :guilabel:`Date Range`;
- :guilabel:`Show Draft Entries`: by default only posted entries are included;
- :guilabel:`Journals`.

Some registers add their own filters:

- **Trial balance**: :guilabel:`Account Level` (analytical accounts, synthetic accounts with 4 or 3
  digits, account groups, account classes) and :guilabel:`Hide Zero Lines`.
- **Account sheets**: :guilabel:`Account Class` (all classes, or class 1 to 9).

Trial balance
=============

The trial balance (*balanța de verificare*) has five pairs of debit and credit columns, the
*five equalities*:

#. :guilabel:`Opening Balance`
#. :guilabel:`Previous Turnover`
#. :guilabel:`Period Turnover`
#. :guilabel:`Total Amounts`
#. :guilabel:`Closing Balance`

Each class of accounts has a :guilabel:`Total class N` line, and the report ends with a
:guilabel:`Grand total`. Click an amount to open the matching journal items. The result of the
income and expense accounts (classes 6 and 7) of the previous periods is carried to the account 121
in the opening balance.

General journal
===============

The general journal (*registru jurnal*) lists the entries in chronological order, one row per entry,
with the columns :guilabel:`Date`, :guilabel:`Document`, :guilabel:`Explanation`, :guilabel:`Debit
Account`, :guilabel:`Credit Account`, :guilabel:`Debit Amount` and :guilabel:`Credit Amount`. You
can unfold an entry to see its accounting lines. The report ends with a :guilabel:`Total` row.

Account sheets
==============

The account sheet (*fișa de cont*) starts with an :guilabel:`Opening balance` row. Each following
row shows the date, the document, the explanation, the :guilabel:`Counterpart Account` (the first
four, then `...`), the debit and credit amounts and the running balance. The sheet ends with a
:guilabel:`Turnover and closing balance` row.

General ledger
==============

The general ledger (*cartea mare*) shows, for each account, the opening balance, the turnover and
the closing balance, each with a debit and a credit column. Unfold an account to see its monthly
turnover.

Sales and purchase journals
===========================

The sales and purchase journals have one row per document, with the date, the document number, the
partner, the tax ID and the total of the document. Then the base and the VAT are split in columns
by tax rate (21%, 11%, 9% and other rates).

The sales journal also has columns for the intra-EU supplies of goods and services, the exempt
operations (with or without the right of deduction, and not taxable), the domestic reverse charge,
and the VAT on payment (*TVA la încasare*). The purchase journal has columns for the intra-EU
acquisitions of goods, the services from abroad, the domestic reverse charge, the exempt or not
taxable operations, and the VAT on payment.

The column of a tax is chosen according to its :doc:`D300 <d300>` tax tag. For old taxes without
tag, the rate is used. Credit notes are shown with negative amounts. After the total line, the
report adds a summary line for each D300 row (for example `D300 row 09`), so the column totals can
be compared directly with the return.

Inventory register
==================

The inventory register (*registru inventar*) lists the balance sheet accounts (classes 1 to 5) at
the end of the period, grouped by class. It has the columns :guilabel:`Book Value Debit`,
:guilabel:`Book Value Credit`, :guilabel:`Inventory Value` and :guilabel:`Valuation Difference`.
The inventory value starts equal to the book value, so the difference is 0. When the stock-taking
shows a difference, book it in the accounting; it then appears in the register.

.. seealso::
   :doc:`inventory` for the stock documents and :doc:`financial_statements`.

Export
======

Click :guilabel:`XLSX` or :guilabel:`PDF` in the top bar to export the report. The export unfolds
all the lines.

.. note::
   The trial balance and the same balance calculation are also the source of the
   :doc:`financial_statements` and of the :doc:`d101` return, so the figures are consistent.

.. seealso::
   - :doc:`../../accounting/reporting/dynamic_reports`
   - :doc:`declarations`
   - :doc:`saft_d406`

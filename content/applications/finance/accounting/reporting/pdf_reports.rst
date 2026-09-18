===========================
Printable financial reports
===========================

Next to the interactive :doc:`Dynamic Reports <dynamic_reports>`, a set of wizard-driven reports
produces a fixed **PDF** (and, where installed, an **XLSX**) document for filing, for the auditor,
or for the board. You choose the period and the options in a dialog, and the document is generated
as it will be archived.

.. _accounting/pdf-reports/statements:

Financial Reports
=================

:menuselection:`Accounting --> Reporting --> Financial Reports`

- :guilabel:`Balance Sheet`
- :guilabel:`Profit and Loss`

.. _accounting/pdf-reports/partner:

Partner Reports
===============

:menuselection:`Accounting --> Reporting --> Partner Reports`

- :guilabel:`Partner Ledger` — the movements of each customer and vendor account, with the option to
  print the balance statement only.
- :guilabel:`Aged Partner Balance`, :guilabel:`Aged Receivable`, :guilabel:`Aged Payable` — the open
  amounts split into ageing buckets. Set the :guilabel:`Period Length (days)` (30 by default) to
  change the width of the buckets.

.. _accounting/pdf-reports/audit:

Audit Reports
=============

:menuselection:`Accounting --> Reporting --> Audit Reports`

- :guilabel:`General Ledger`
- :guilabel:`Trial Balance`
- :guilabel:`Journals Audit`
- :guilabel:`Tax Report`

.. _accounting/pdf-reports/daily:

Daily Reports
=============

:menuselection:`Accounting --> Reporting --> Daily Reports`

- :guilabel:`Cash Book` — the movements of the cash journals.
- :guilabel:`Bank Book` — the movements of the bank journals.
- :guilabel:`Day Book` — all movements of a period, day by day.

.. _accounting/pdf-reports/options:

Common options
==============

Most of the wizards share the same options:

:guilabel:`Start Date` / :guilabel:`End Date`
   The period covered. Balance-sheet style reports use the end date only.

:guilabel:`Target Moves`
   :guilabel:`All Posted Entries` (the default) or :guilabel:`All Entries`, which also includes
   unposted ones.

:guilabel:`Journals`
   The journals to include. Leave it on all journals for a complete report.

:guilabel:`Accounts`, :guilabel:`Partners`, :guilabel:`Analytic Accounts`
   Restrict the report to a selection.

:guilabel:`Display Accounts`
   Whether to print all accounts, only those with movements, or only those with a balance.

:guilabel:`Include Initial Balances`
   Starts the ledger from the opening balance of the period instead of zero.

:guilabel:`Sort by`
   The order of the journal items inside an account (by date or by journal and partner).

Click :guilabel:`Print` to generate the PDF. When the *Accounting XLSX Reports* module is installed,
the aged balance, general ledger, trial balance, partner ledger, financial, tax and journal audit
wizards also offer an :guilabel:`XLSX` button that produces the same content as a spreadsheet.

.. screenshot:: accounting-pdf-reports-wizard
   :menu: Accounting ‣ Reporting ‣ Audit Reports ‣ General Ledger
   :shows: The General Ledger wizard dialog with the Start Date / End Date, Target Moves, Journals,
      Accounts, Display Accounts, Include Initial Balances and Sort by options, and the Print and
      XLSX buttons at the bottom.
   :highlight: The Print and XLSX buttons (red frame).
   :data: Period 01/01/2026 – 12/31/2026, Target Moves "All Posted Entries".
   :module: accounting_pdf_reports, account_xlsx_reports
   :notes: English UI, light theme, dialog only.

.. _accounting/pdf-reports/customize:

Customize the printed statements
================================

The structure of the :guilabel:`Balance Sheet` and the :guilabel:`Profit and Loss` is stored as a
tree of report lines that you can adapt to your chart of accounts. Go to :menuselection:`Accounting
--> Configuration --> Financial Reports --> Account Reports` and open a report.

Each line has:

- a :guilabel:`Report Name` and a :guilabel:`Parent`, which place it in the tree;
- a :guilabel:`Type`, saying what the line sums up: a set of :guilabel:`Accounts`, a set of
  :guilabel:`Account Types`, another :guilabel:`Report Value`, or the sum of its children;
- a :guilabel:`Sign`, to reverse the sign of the balance when the report should show it the other
  way round;
- a :guilabel:`Display Detail` option, choosing whether the underlying accounts are printed under
  the line;
- a :guilabel:`Style` and a :guilabel:`Sequence`, controlling how and where the line is printed.

.. warning::
   These reports are the ones used for the statutory statements. Change them only in agreement with
   your accountant, and check the totals of the modified report against the
   :ref:`Trial Balance <accounting/reporting/trial-balance>` afterwards.

.. seealso::
   - :doc:`dynamic_reports`
   - :doc:`../reporting`

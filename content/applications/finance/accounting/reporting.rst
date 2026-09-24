:show-content:

=========
Reporting
=========

Accounting reporting is provided by three complementary sets of modules:

- the :doc:`Dynamic Reports <reporting/dynamic_reports>` (*Account Dynamic Reports*), an interactive
  on-screen report view with folding, filters, comparison, drill-down and XLSX/PDF export. This is
  where you consult the figures day to day;
- the :doc:`printable financial reports <reporting/pdf_reports>` (*Accounting Financial Reports*,
  *Cash Book / Day Book / Bank Book* and the XLSX export), which produce a fixed PDF or Excel
  document from a wizard, for filing and for the auditor;
- the specialized reports and declarations documented on the pages listed below
  (:doc:`tax returns <reporting/tax_returns>`, :doc:`Intrastat <reporting/intrastat>`,
  :doc:`analytic accounting <reporting/analytic_accounting>`, :doc:`budgets <reporting/budget>`).

.. _accounting/reporting/dynamic-list:

The dynamic reports
===================

All dynamic reports are available under :menuselection:`Accounting --> Reporting --> Dynamic
Reports`:

-  :ref:`accounting/reporting/trial-balance`
-  :ref:`accounting/reporting/executive-summary`
-  :ref:`accounting/reporting/balance-sheet`
-  :ref:`accounting/reporting/cash-flow-statement`
-  :ref:`accounting/reporting/profit-and-loss`
-  :ref:`accounting/reporting/general-ledger`
-  :ref:`accounting/reporting/partner-ledger`
-  :ref:`accounting/reporting/tax-report`
-  :ref:`accounting/reporting/journal-audit`
-  :ref:`accounting/reporting/aged-receivable`
-  :ref:`accounting/reporting/aged-payable`
-  :ref:`accounting/reporting/bank-reconciliation`
-  :ref:`accounting/reporting/deferred`
-  :ref:`accounting/reporting/ec-sales-list`

.. seealso::
   :doc:`reporting/dynamic_reports` — how to filter, fold, compare, annotate, and export a dynamic
   report.

.. _accounting/reporting/trial-balance:

Trial Balance
=============

The :guilabel:`Trial Balance` lists every account with its initial balance, the debit and credit of
the period, and the closing balance. It is the usual starting point of a period check: the total
debit and the total credit must be equal.

.. _accounting/reporting/balance-sheet:

Balance Sheet
=============

The :guilabel:`Balance Sheet` shows a snapshot of your organization's assets, liabilities, and
equity at a particular date.

.. _accounting/reporting/profit-and-loss:

Profit & Loss
=============

The :guilabel:`Profit & Loss` report (or **Income Statement**) shows your company's net income by
deducting expenses from revenue for the reporting period.

.. _accounting/reporting/executive-summary:

Executive Summary
=================

The :guilabel:`Executive Summary` provides an overview of all the important figures for overseeing
your company's performance.

It includes the following items:

- :guilabel:`Performance`:
    - :guilabel:`Gross profit margin`:
        The contribution of all sales your business makes **minus** any direct costs needed to
        make those sales (labor, materials, etc.).
    - :guilabel:`Net profit margin`:
        The contribution of all sales made by your business **minus** any direct costs needed to
        make those sales *and* fixed overheads your company has (electricity, rent, taxes
        to be paid as a result of those sales, etc.).
    - :guilabel:`Return on investment (per annum)`:
        The ratio of the net profit to the amount of assets the company used to make those profits.
- :guilabel:`Position`:
    - :guilabel:`Average debtors days`:
        The average number of days it takes your customers to (fully) pay you across all your
        customer invoices.
    - :guilabel:`Average creditors days`:
        The average number of days it takes you to (fully) pay your suppliers across all your bills.
    - :guilabel:`Short-term cash forecast`:
        How much cash is expected in or out of your business in the next month, i.e., the balance of
        your **Sales account** for the month **minus** the balance of your **Purchases account** for
        the month.
    - :guilabel:`Current assets to liabilities`:
        Also referred to as the **current ratio**, this is the ratio of current assets (:dfn:`assets
        that could be turned into cash within a year`) to the current liabilities (:dfn:`liabilities
        that will be due in the next year`). It is typically used to measure a company's ability to
        service its debt.

.. _accounting/reporting/general-ledger:

General Ledger
==============

The :guilabel:`General Ledger` report shows all transactions from all accounts for a selected date
range. The initial summary report shows the totals for each account. To expand an account and view
its details, click the :icon:`fa-caret-right` (:guilabel:`right arrow`) on the left.
This report is useful for reviewing each transaction that occurred during a specific period.

.. _accounting/reporting/partner-ledger:

Partner Ledger
==============

The :guilabel:`Partner Ledger` shows the same detail as the general ledger, but grouped by customer
and vendor instead of by account. Use it to reconstruct what a given partner owes you, or what you
owe them, transaction by transaction.

.. _accounting/reporting/aged-receivable:

Aged Receivable
===============

The :guilabel:`Aged Receivable` report shows the sales invoices awaiting payment during a selected
month and several months prior.

.. _accounting/reporting/aged-payable:

Aged Payable
============

The :guilabel:`Aged Payable` report displays information on individual bills, credit notes, and
overpayments you owe and how long these have gone unpaid.

.. _accounting/reporting/cash-flow-statement:

Cash Flow Statement
===================

The :guilabel:`Cash Flow Statement` shows how changes in balance sheet accounts and income affect
cash and cash equivalents and breaks the analysis down to operating, investing, and financing
activities.

.. _accounting/reporting/tax-report:

Tax Report
==========

The :guilabel:`Tax Report` shows the :guilabel:`NET` and :guilabel:`TAX` amounts for all the
taxes grouped by type (:guilabel:`Sales`/:guilabel:`Purchases`).

.. seealso::
   :doc:`reporting/tax_returns`

.. _accounting/reporting/journal-audit:

Journal Audit
=============

The :guilabel:`Journal Audit` lists the journal entries of a period journal by journal, with their
lines, so that a complete period can be reviewed entry by entry. It is the report auditors usually
ask for.

.. _accounting/reporting/bank-reconciliation:

Bank Reconciliation
===================

The :guilabel:`Bank Reconciliation` report compares, per bank journal, the balance of the bank
account in the books with the transactions that have already been reconciled, and lists what is
still outstanding. Use it to justify the difference between a bank statement balance and the
accounting balance at a given date.

.. _accounting/reporting/deferred:

Deferred Expense and Deferred Revenue
=====================================

The :guilabel:`Deferred Expense` and :guilabel:`Deferred Revenue` reports show, period by period,
the amounts that have been spread over time from bills and invoices.

.. seealso::
   - :doc:`vendor_bills/deferred_expenses`
   - :doc:`customer_invoices/deferred_revenues`

.. _accounting/reporting/ec-sales-list:

EC Sales List
=============

The :guilabel:`EC Sales List` gathers the intra-Community supplies of goods and services per
customer VAT number, as required for the recapitulative statement.

.. seealso::
   :doc:`reporting/intrastat`

.. toctree::
   :titlesonly:

   reporting/dynamic_reports
   reporting/pdf_reports
   reporting/tax_returns
   reporting/analytic_accounting
   reporting/budget
   reporting/intrastat
   reporting/data_inalterability
   reporting/year_end

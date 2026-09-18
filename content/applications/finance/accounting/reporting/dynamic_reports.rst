================
Dynamic Reports
================

The **Dynamic Reports** are the interactive accounting reports you consult on screen. They all share
the same view, so once you know how to drive one, you know how to drive them all: the filters are at
the top, the figures fold and unfold, any figure can be drilled down to the underlying entries, and
the result can be exported to XLSX or PDF.

The reports are listed under :menuselection:`Accounting --> Reporting --> Dynamic Reports` and are
described in :doc:`../reporting`.

.. _accounting/dynamic-reports/filters:

Filter the report
=================

The filter bar above the table holds the filters that are relevant for the report you opened. The
most common ones are:

:guilabel:`Date Range`
   The start and end date of the period. For balance-sheet style reports, only the end date is
   meaningful.

:guilabel:`Comparison`
   Adds one or more comparison columns. Choose the comparison mode in the dropdown, then set the
   number of :guilabel:`Periods` (up to three).

:guilabel:`Journals`, :guilabel:`Partners`, :guilabel:`Analytic Accounts`
   Restrict the report to a selection of journals, partners, or analytic accounts.

:guilabel:`Account Type`
   Restrict the report to a type of account.

:guilabel:`Show Draft Entries`
   Includes unposted journal entries. It is off by default, so the report shows posted entries only.

:guilabel:`Hide Zero Lines`
   Hides the lines whose value is zero on every column.

:guilabel:`Separate Debit/Credit`
   Shows the debit and the credit in two columns instead of one signed balance.

:guilabel:`Budget Comparison`
   Adds the budgeted amount and the variance next to the actuals. See :doc:`budget`.

:guilabel:`Currency Translation`
   Chooses how foreign-currency amounts are converted in the report.

.. screenshot:: accounting-dynamic-reports-filters
   :menu: Accounting ‣ Reporting ‣ Dynamic Reports ‣ Balance Sheet
   :shows: The Dynamic Report view with the search box, the visual toggles and the filter bar
      (Date Range, Comparison, Journals, Hide Zero Lines) above the folded report table.
   :highlight: The filter bar (red frame).
   :data: Demo company "YourCompany HU", fiscal year 2026, comparison with the previous period.
   :module: report_dynamic, account_dynamic_reports
   :notes: English UI, light theme, 1440px width.

.. _accounting/dynamic-reports/navigate:

Read and navigate the report
============================

- Click the :icon:`fa-caret-right` (:guilabel:`right arrow`) in front of a line to unfold it, and
  use :guilabel:`Unfold All` / :guilabel:`Fold All` in the top bar to expand or collapse everything
  at once.
- Click a figure to drill down to the journal items behind it, when the line supports it.
- Use the :guilabel:`Search...` box to keep only the lines whose label matches what you type.
- Click a column header to sort the report by that column.
- Long lists load progressively: click :guilabel:`Load more` at the bottom of a group to get the
  next batch.

.. _accounting/dynamic-reports/visuals:

Visual aids
===========

Five toggles next to the search box change how the figures are presented. They are personal display
options and do not alter the data:

:guilabel:`KPI Cards` (:icon:`fa-tachometer`)
   A row of headline figures above the table.

:guilabel:`Heatmap` (:icon:`fa-th`)
   Shades the cells according to their value. Two modes are available: :guilabel:`Absolute mode`
   colors by the size of the amount, :guilabel:`Variance mode` colors by the difference with the
   comparison column.

:guilabel:`Waterfall Chart` (:icon:`fa-area-chart`)
   Shows how the successive lines build up to the total. It requires at least two lines.

:guilabel:`Sparklines` (:icon:`fa-line-chart`)
   Adds a miniature trend curve at the end of each line.

:guilabel:`Financial Ratios` (:icon:`fa-calculator`)
   Opens a side panel with the ratios computed from the report.

.. _accounting/dynamic-reports/annotations:

Annotate a line
===============

Any line of a report can carry annotations, for example to justify a variance to the auditor. Open
the :icon:`fa-ellipsis-v` menu at the end of the line and add your note; annotated lines are then
marked with a warning badge, and the note records who wrote it and when. Annotations stay attached
to the line and are visible to the other users of the report.

.. _accounting/dynamic-reports/export:

Export
======

Two buttons in the top bar export what is currently displayed — including the filters, the
comparison columns and the folding state:

- :guilabel:`XLSX` produces a spreadsheet;
- :guilabel:`PDF` produces a printable document.

.. seealso::
   - :doc:`pdf_reports`
   - :doc:`../reporting`

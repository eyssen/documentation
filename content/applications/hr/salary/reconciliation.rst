==============
Reconciliation
==============

When the payroll calculation is done by an external provider, the figures that leave Odoo and the
figures that come back have to agree. *Reconciliation* imports the provider's statement, matches
every line to a :doc:`salary sheet <salary_sheets>` line, and reports what differs.

Import a statement
==================

Open the :doc:`salary period <salary_periods>` and click :guilabel:`Import Statement`. In the
dialog:

- :guilabel:`Provider`: the name of the payroll provider the file comes from.
- :guilabel:`File`: the CSV file returned by the provider.
- :guilabel:`Delimiter` and :guilabel:`First Row Is a Header`: how to read the file.
- :guilabel:`Employee Column`, :guilabel:`Component Column` and :guilabel:`Amount Column`: the
  position of each value in a row, counted from `0`.
- :guilabel:`Match Immediately`: run the matching right after the import.

The import creates an *external statement* with one line per row. The file itself is stored on the
statement together with its hash, so it is always possible to show which file a figure came from.

.. screenshot:: hr-salary-statement-import
   :menu: Salary ‣ Salary ‣ Salary Periods ‣ (open a period) ‣ Import Statement
   :shows: The Import Statement dialog with the Provider, File, Delimiter, header checkbox and the three column numbers filled in.
   :highlight: The column mapping fields (red frame).
   :data: Provider "Bérszámfejtő Kft.", file "2026-03-payroll.csv", semicolon delimiter.
   :module: hr_salary_sheet
   :notes: English UI, light theme, 1440px width. Use a throw-away sample file.

Matching
========

Click :guilabel:`Match` on the statement. Each line is matched by:

- the :guilabel:`Raw Employee Reference` against the :guilabel:`External Reference` of an
  :doc:`engagement <engagements>`, or against the employee;
- the :guilabel:`Raw Component Code` against the :ref:`external codes <salary/components>` of a
  salary component.

Every line ends up in one of the matching states: :guilabel:`Unmatched`,
:guilabel:`Automatically Matched`, :guilabel:`Manually Matched`, or :guilabel:`Ignored`, with the
reason in the :guilabel:`Matching Note`. The :guilabel:`Unmatched` counter on the statement shows
how many still need attention. Fix an unmatched line by filling in the missing external reference or
external code — or by selecting the employee, engagement and component on the statement line itself
— and run :guilabel:`Match` again. The full result of the run is kept in the
:guilabel:`Import Log` tab.

Click :guilabel:`Post` to write the matched amounts onto the salary sheet lines as
:guilabel:`External Amount`.

.. note::
   When a corrected file arrives, import it as a new statement and click :guilabel:`Supersede` on
   the old one. The superseded statement stays in the database, linked to its replacement, so the
   history of what was received stays complete.

Deviations
==========

Once external amounts are posted, every sheet line compares its own amount with the external one:

- :guilabel:`Deviation`: the difference between the two.
- The line is within tolerance when the difference stays under the :guilabel:`Tolerance Amount` and
  :guilabel:`Tolerance (%)` of its component, or under the company default when the component sets
  neither.
- A line outside tolerance takes the :guilabel:`Deviation Severity` of its component:
  :guilabel:`Information`, :guilabel:`Warning`, or :guilabel:`Blocking`.
- :guilabel:`External State` says whether the line was :guilabel:`Matched`, is
  :guilabel:`Not Imported`, or exists :guilabel:`Only External` — a figure the provider reports that
  has no counterpart in Odoo.

Every deviating line starts with the :guilabel:`Deviation Status` :guilabel:`Open`, and the lines
that are waiting for a decision carry two buttons — on the :guilabel:`Lines` tab of the
:doc:`salary sheet <salary_sheets>` and in :menuselection:`Salary app --> Reporting --> Salary
Analysis`:

- :icon:`fa-check` :guilabel:`(Accept the external figure)`: the provider's figure is the correct
  one, and the status becomes :guilabel:`Accepted`.
- :icon:`fa-ban` :guilabel:`(Waive the deviation)`: the difference is known and does not need to be
  followed up; the status becomes :guilabel:`Waived`.

A line whose deviation stays inside the tolerance shows no buttons, so what is left on screen is
what genuinely needs a decision. Use :icon:`fa-undo` :guilabel:`(Reopen the deviation)` to put a
decision back to :guilabel:`Open`.

Open the line itself to enter a :guilabel:`Deviation Note` explaining the decision; the handling
user is recorded in :guilabel:`Deviation Handled By`.

.. important::
   A :guilabel:`Blocking` deviation may only be waived by a user with the
   :guilabel:`Salary Approver` right.

The sheet's :guilabel:`Reconciliation` status summarizes the result:
:guilabel:`Not Imported`, :guilabel:`Matched`, :guilabel:`Deviation`, or :guilabel:`Waived`. The
period shows the number of :guilabel:`Open Deviations`, and by default a period with a blocking
deviation cannot be closed.

.. screenshot:: hr-salary-reconciliation-deviations
   :menu: Salary ‣ Reporting ‣ Salary Analysis
   :shows: The salary line list filtered to lines with a deviation, showing Employee, Component, Amount, External Amount, Deviation, the deviation status and the accept, waive and reopen buttons at the end of the row.
   :highlight: The accept and waive buttons on an open deviation (red frame).
   :data: Period "2026-03"; two deviating lines, one accepted and one still open.
   :module: hr_salary_sheet
   :notes: English UI, light theme, 1440px width.

Reporting
=========

:menuselection:`Salary app --> Reporting --> Salary Analysis` opens all salary sheet lines, which
can be grouped and pivoted by period, employee, component and nature, with the
:guilabel:`With a Deviation`, :guilabel:`Open Deviation` and :guilabel:`Only in the External File`
filters, in list, pivot and graph view.

.. seealso::
   - :doc:`salary_periods`
   - :doc:`configuration`

=============
Salary sheets
=============

A *salary sheet* is the monthly grid of one engagement: what the employee earns, what is deducted,
what the employer pays, and how many days of each kind the month contains. Every value on it is a
line referring to a :ref:`salary component <salary/components>` — the base salary included — so the
sheet can be compared line by line with the payroll provider's figures.

To see the sheets, go to :menuselection:`Salary app --> Salary --> Salary Sheets`. Sheets are
normally created from the :doc:`salary period <salary_periods>` rather than one by one.

The sheet form
==============

The header of the form shows the :guilabel:`Period`, the :guilabel:`Engagement`, the
:guilabel:`Employee` and the :guilabel:`Salary Term` the sheet was built from, and the totals:
:guilabel:`Gross`, :guilabel:`Reliefs`, :guilabel:`Deductions`, :guilabel:`Net`,
:guilabel:`Net Payable` and :guilabel:`Employer Cost`.

Lines tab
---------

Each line has:

- :guilabel:`Component` and its :guilabel:`Code`: what the line is.
- :guilabel:`Quantity` and :guilabel:`Amount`: how much of it. For a day or hour component, the
  quantity carries the value.
- :guilabel:`Input Basis`: whether the entered amount is a :guilabel:`Gross` or a :guilabel:`Net`
  figure. The other figure and the employer cost are derived from the line's
  :guilabel:`Contribution Regime`.
- :guilabel:`Source`: where the value came from — :guilabel:`Manual`, :guilabel:`Salary Term`,
  :guilabel:`Working Schedule`, or :guilabel:`External Import`. A manually entered value on a line
  that was generated keeps a :guilabel:`Manual Reason`.

Days tab
--------

:guilabel:`Worked Days`, :guilabel:`Leave Days`, :guilabel:`Sick Days` and :guilabel:`Unpaid Days`
are derived from the working schedule of the engagement and the validated time off of the month.
Which bucket a time off feeds is set through the :ref:`time off mapping <salary/time-off-mapping>`.

Reconciliation tab
------------------

Shows the :guilabel:`External Total` returned by the payroll provider, the :guilabel:`Deviation`
and the :guilabel:`Deviation (%)`, and the :guilabel:`Reconciliation` status. See
:doc:`reconciliation`.

.. screenshot:: hr-salary-sheet-form
   :menu: Salary ‣ Salary ‣ Salary Sheets ‣ (open a sheet)
   :shows: A confirmed salary sheet with the totals in the header, and the Lines tab showing the base salary, a bonus, a deduction and the day counters.
   :highlight: The Lines tab grid (red frame).
   :data: Employee "Anita Kovács", period "2026-03"; lines Base Salary, Variable Bonus, Other Deduction, Worked Days, Leave Days.
   :module: hr_salary_sheet, l10n_hu_hr_salary_sheet
   :notes: English UI, light theme, 1440px width.

Statuses
========

- :guilabel:`Draft`: the sheet is being filled in.
- :guilabel:`Confirmed`: the figures are ready to be handed over to the payroll provider. Click
  :guilabel:`Confirm`.
- :guilabel:`Closed`: the sheet is final. Sheets are closed together with their period, or
  individually with :guilabel:`Close`. A closed sheet keeps a snapshot, a hash, and the user and
  time of closing on the :guilabel:`Closing` tab.
- :guilabel:`Cancelled`: the sheet does not apply, for example because the engagement did not start.

:guilabel:`Reset to Draft` returns a confirmed sheet to :guilabel:`Draft`. Reopening a *closed*
sheet requires the :guilabel:`Salary Approver` right.

.. _salary/corrections:

Corrections
===========

A month that has already been reported is not edited. Open the closed sheet and click
:guilabel:`Create Correction`: a new sheet of the :guilabel:`Correction` type is created, linked to
the original through :guilabel:`Corrected Sheet`, and numbered with a
:guilabel:`Correction Sequence`. Enter the difference on the correction sheet and process it with
the current period.

.. note::
   Time off entered or changed after a month is closed does **not** change that month's sheet. The
   change has to be handled with a correction sheet, which is what keeps the reported figures and
   the Odoo figures in agreement.

.. seealso::
   - :doc:`salary_periods`
   - :doc:`reconciliation`

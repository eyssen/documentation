==============
Salary periods
==============

A *salary period* is one payroll month of one company. It is the unit that is opened, filled,
reconciled and finally closed. Closing a period freezes everything it contains.

To see the periods, go to :menuselection:`Salary app --> Salary --> Salary Periods`.

.. screenshot:: hr-salary-periods-list
   :menu: Salary ‣ Salary ‣ Salary Periods
   :shows: The Salary Periods list with the Name, From, To, Status, Total Gross, Total External and Total Deviation columns.
   :highlight: The Status and Total Deviation columns (red frame).
   :data: Demo company "YourCompany HU"; three monthly periods, the current one Open, the previous one Closed.
   :module: hr_salary_sheet
   :notes: English UI, light theme, 1440px width.

Create a period
===============

Click :guilabel:`New` and fill in:

- :guilabel:`From` and :guilabel:`To`: the first and last day of the month.
- :guilabel:`Payroll Mode`: :guilabel:`External Provider` when the payroll calculation is done
  outside Odoo — which is the normal case for this application — or :guilabel:`Internal`.
- :guilabel:`Working Days Override`: fill this in only when the legal number of working days of the
  month differs from the number computed from the company's working schedule. The value actually
  used is shown as :guilabel:`Working Days Used`.

Click :guilabel:`Open` to start the month.

Generate the salary sheets
==========================

On an open period, click :guilabel:`Generate Sheets`. In the dialog:

- :guilabel:`Engagements`: leave empty to generate a sheet for every running engagement, or select
  the engagements to generate for.
- :guilabel:`Include Draft Engagements`: also generate for engagements that have not been started.
- :guilabel:`Complete Existing`: add the missing default lines to sheets that already exist, instead
  of skipping those sheets.

Each generated :doc:`salary sheet <salary_sheets>` starts from the engagement's salary term and from
the working schedule and time off of the month.

.. tip::
   To put the same component on many sheets at once — a one-off bonus, for example — click
   :guilabel:`Batch Line` on the period, select the component, the amount and the sheets, and apply.

Reconcile and close
===================

The period walks through four statuses:

#. :guilabel:`Draft`: being prepared.
#. :guilabel:`Open`: sheets are generated and amounts are entered.
#. :guilabel:`Reconciling`: the external payroll statement has arrived and the deviations are being
   handled. Click :guilabel:`Start Reconciliation` to get here.
#. :guilabel:`Closed`: the month is final.

Click :guilabel:`Close` to close the period. Closing:

- refuses to run while any sheet still has a *blocking* deviation, unless the company setting
  :guilabel:`Closing Requires No Blocking Deviation` is switched off;
- stores a snapshot and a hash of the closed figures, together with :guilabel:`Closed By` and
  :guilabel:`Closed On`, on the :guilabel:`Closing` tab;
- makes every sheet, line and term of the month read-only, including through later changes to time
  off or to a contract.

.. important::
   Only a user with the :guilabel:`Salary Approver` right can :guilabel:`Reopen` a closed period,
   and a :guilabel:`Reopening Reason` has to be entered. The reason, the user and the date are kept
   on the :guilabel:`Reopening` tab, so that every intervention into a reported month stays
   traceable.

.. screenshot:: hr-salary-period-form
   :menu: Salary ‣ Salary ‣ Salary Periods ‣ (open a period)
   :shows: A salary period form in the Reconciling status, with the Generate Sheets, Import Statement, Batch Line and Close buttons in the header, the Totals and External groups, and the Salary Sheets tab.
   :highlight: The Totals and External groups with Total Gross, Total External and Total Deviation (red frame).
   :data: Period "2026-03", 12 sheets, one open deviation.
   :module: hr_salary_sheet
   :notes: English UI, light theme, 1440px width.

.. seealso::
   - :doc:`salary_sheets`
   - :doc:`reconciliation`

============================
Engagements and salary terms
============================

An *engagement* is one employment relationship between the company and a person. The same person may
hold several engagements at the same time — an employment relationship and a mandate contract, for
example — which a single contract record cannot express.

A *salary term* is what has been agreed for that engagement from a given date: the amount, what the
amount is expressed in, the share of full working time, and the contribution regime. Terms form a
dated chain, so the salary of any past month can always be reconstructed.

.. _salary/engagements:

Engagements
===========

To see the engagements, go to :menuselection:`Salary app --> People --> Engagements`.

.. screenshot:: hr-salary-engagements-list
   :menu: Salary ‣ People ‣ Engagements
   :shows: The Engagements list with the Employee, Engagement Type, Start Date, End Date, Current Term and Status columns, grouped by Status.
   :highlight: The Status column, with a running and an ended engagement (red frame).
   :data: Demo company "YourCompany HU"; employee "Anita Kovács" with a running employment engagement, employee "Péter Nagy" with an ended mandate engagement.
   :module: hr_salary_sheet, l10n_hu_hr_salary_sheet
   :notes: English UI, light theme, 1440px width.

Click :guilabel:`New` and fill in the form:

- :guilabel:`Employee`: the person the engagement belongs to. This field is **required**.
- :guilabel:`Engagement Type`: the legal form of the relationship, for example
  :guilabel:`Employment Relationship` or :guilabel:`Mandate Contract`. The available types come from
  the country's :ref:`localization <salary/engagement-types>`.
- :guilabel:`Contract`: an optional link to the employee's :doc:`contract <../employees/contracts>`.
  Engagement types whose :guilabel:`Requires Contract` option is enabled must have one.
- :guilabel:`Start Date` and :guilabel:`End Date`: the period the engagement runs for. Leave the end
  date empty while the engagement is open-ended.
- :guilabel:`Working Schedule`: the schedule that applies to this engagement. When it is left empty,
  the employee's own working schedule is used.
- :guilabel:`Department`: the department the engagement is reported under.
- :guilabel:`External Reference`: the identifier of this engagement in the external payroll program.
  The :doc:`statement import <reconciliation>` uses it to match the provider's lines.

Click :guilabel:`Start` to set the engagement to :guilabel:`Running`. Click :guilabel:`End` to close
it; the end date is set to today if it is still empty.

.. note::
   The :guilabel:`Suspended` indicator is set automatically while a validated time off of a
   *suspending* type covers today — unpaid leave or parental leave, for instance. Which time off
   types suspend an engagement is set on the :ref:`time off type <salary/time-off-mapping>`.

.. _salary/salary-terms:

Salary terms
============

Open an engagement and use the :guilabel:`Salary Terms` tab, or go to :menuselection:`Salary app -->
People --> Salary Terms` for the full list.

Click :guilabel:`New` and fill in the form:

- :guilabel:`Valid From`: the date the agreement takes effect. This field is **required**.
- :guilabel:`Valid To`: filled in automatically — the day before the next term starts, or the end
  date of the engagement.
- :guilabel:`Amount`: the agreed amount.
- :guilabel:`Amount Basis`: whether the amount is a :guilabel:`Gross` or a :guilabel:`Net` figure.
- :guilabel:`Amount Unit`: what the amount is expressed in — :guilabel:`Per Month`,
  :guilabel:`Per Hour`, :guilabel:`Per Day`, :guilabel:`Per Piece`, or :guilabel:`Per Event`.
- :guilabel:`Work Time Rate (%)`: the share of the full working schedule the term is agreed for,
  `100` for full time.
- :guilabel:`Working Schedule`: the schedule this term assumes, when it differs from the engagement.
- :guilabel:`Contribution Regime`: the regime the amount falls under. A
  :guilabel:`Secondary Regime` and a :guilabel:`Secondary Ratio (%)` can be added when part of the
  amount falls under a different regime.
- :guilabel:`Change Reason`: why this term was created — :guilabel:`Hire`, :guilabel:`Raise`,
  :guilabel:`Working Time Change`, :guilabel:`Regime Change`, :guilabel:`Role Change`,
  :guilabel:`Correction`, or :guilabel:`Termination`. The reason makes the salary history readable.
- :guilabel:`Notes`: any explanation of the change.

Click :guilabel:`Confirm` to put the term in force. Confirming a term sets the previous one to
:guilabel:`Superseded` and fills in its :guilabel:`Valid To` date.

.. screenshot:: hr-salary-term-form
   :menu: Salary ‣ People ‣ Salary Terms ‣ New
   :shows: A confirmed salary term form with the Scope, Agreement and Contributions groups filled in, and the Confirm button in the header.
   :highlight: The Agreement group with Amount, Amount Basis, Amount Unit and Work Time Rate (red frame).
   :data: Employee "Anita Kovács"; amount 650 000 HUF, gross, per month, work time rate 100, regime "General Rules", change reason "Raise".
   :module: hr_salary_sheet, l10n_hu_hr_salary_sheet
   :notes: English UI, light theme, 1440px width.

.. important::
   A term that a closed salary sheet already refers to is marked :guilabel:`Used in a Closed Month`
   and can no longer be changed. Correct such an agreement with a new term, or by reopening and
   correcting the month.

.. _salary/contract-wage:

Contracts and the agreed wage
=============================

With **Salary** installed, the :guilabel:`Salary Information` tab of a :doc:`contract
<../employees/contracts>` also shows the :guilabel:`Engagement` and the :guilabel:`Salary Term` that
apply. If the contract's :guilabel:`Wage` no longer matches the amount of the current term, a
:guilabel:`Take the wage from the salary term` button appears for salary managers, which copies the
agreed amount onto the contract.

.. seealso::
   - :doc:`salary_periods`
   - :doc:`configuration`

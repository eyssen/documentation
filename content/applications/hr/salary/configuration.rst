=============
Configuration
=============

The catalogues below define what a :doc:`salary sheet <salary_sheets>` can contain. They are
country-specific and are normally installed as data by a localization module, such as
:doc:`Hungary <hungary>`. Adjust them only when the company's own practice requires it.

The :guilabel:`Configuration` menu is only visible to users with the :guilabel:`Salary Manager`
right.

.. _salary/components:

Salary components
=================

A *salary component* is one row of the salary sheet: the base salary, a bonus, a deduction, a day
counter. Go to :menuselection:`Salary app --> Configuration --> Salary Components`.

- :guilabel:`Name` and :guilabel:`Code`: what the component is called and its internal code.
- :guilabel:`Nature`: what kind of item it is — :guilabel:`Base Salary`, :guilabel:`Earning`,
  :guilabel:`Deduction`, :guilabel:`Relief`, :guilabel:`Employer Cost`, :guilabel:`Net Payment`,
  :guilabel:`Measure`, or :guilabel:`Informative`.
- :guilabel:`Value Type`: whether the line carries an :guilabel:`Amount`, :guilabel:`Days`,
  :guilabel:`Hours`, or a :guilabel:`Rate`.
- :guilabel:`Day Type`: for day components only — which day bucket of the sheet the component feeds:
  :guilabel:`Worked`, :guilabel:`Paid Leave`, :guilabel:`Sick`, or :guilabel:`Unpaid`.
- :guilabel:`Sign`: `1` when the value increases the total it belongs to, `-1` when it decreases it.
- :guilabel:`In Gross`, :guilabel:`In Net` and :guilabel:`In Employer Cost`: which of the sheet's
  totals the line is added to.
- :guilabel:`Default Input Basis`: whether amounts are normally entered as :guilabel:`Gross` or
  :guilabel:`Net`.
- :guilabel:`Default Regime`: the contribution regime used when the line does not get one from the
  salary term.
- :guilabel:`Default Source`: where the value normally comes from — :guilabel:`Manual`,
  :guilabel:`Salary Term`, :guilabel:`Working Schedule`, or :guilabel:`External Import`.
- :guilabel:`On Every Sheet`: generate a line for this component on every new salary sheet, so the
  grid always has the same rows in the same order.
- :guilabel:`External Codes`: the code this component has at each payroll :guilabel:`Provider`.
  :doc:`Statement matching <reconciliation>` uses these codes.
- :guilabel:`Tolerance Amount`, :guilabel:`Tolerance (%)` and :guilabel:`Deviation Severity`: how
  much the external figure may differ before it is reported, and how seriously. A
  :guilabel:`Blocking` deviation prevents the month from being closed until it is handled.
- :guilabel:`Report Column`: a free label used to group the component on exports.

.. screenshot:: hr-salary-component-form
   :menu: Salary ‣ Configuration ‣ Salary Components ‣ (open a component)
   :shows: A salary component form for the base salary, with Nature, Value Type, the total inclusion checkboxes, the default source and the External Codes list.
   :highlight: The In Gross / In Net / In Employer Cost checkboxes and the External Codes list (red frame).
   :data: Component "Base Salary", code "BASE", nature Base Salary, one external code for provider "Bérszámfejtő Kft.".
   :module: hr_salary_sheet, l10n_hu_hr_salary_sheet
   :notes: English UI, light theme, 1440px width.

.. _salary/engagement-types:

Engagement types
================

An *engagement type* is the legal form of an employment relationship. Go to
:menuselection:`Salary app --> Configuration --> Engagement Types`.

- :guilabel:`Name` and :guilabel:`Code`.
- :guilabel:`Requires Contract`: engagements of this type must be linked to an employee
  :doc:`contract <../employees/contracts>`.
- :guilabel:`Default Regime`: the contribution regime proposed on a new salary term.
- :guilabel:`Country`: the country the type belongs to.

.. _salary/regimes:

Contribution regimes
====================

A *contribution regime* converts a gross amount into a net amount and into an employer cost. Go to
:menuselection:`Salary app --> Configuration --> Contribution Regimes`.

A regime has a :guilabel:`Name`, a :guilabel:`Code`, a :guilabel:`Country`, and a list of dated
rates. Each rate line has:

- :guilabel:`Valid From` and :guilabel:`Valid To`: the period the factors apply to.
- :guilabel:`Net Factor`: the share of the gross amount that remains as net.
- :guilabel:`Employer Cost Factor`: the multiplier from the gross amount to the employer's cost.
- :guilabel:`Tax Rate`: the rate the factors were derived from, for information.
- :guilabel:`Legal Reference`: the law or regulation the factors come from.

.. important::
   The factors are data, not a calculation. They give the expected figure that is compared with the
   payroll provider's result; they do not replace the payroll calculation. When rates change,
   add a **new** rate line with a new :guilabel:`Valid From` date instead of editing the old one —
   past months must keep the factors they were closed with.

.. _salary/time-off-mapping:

Time off mapping
================

Two settings connect :doc:`Time Off <../time_off>` to the salary sheet. Open a time off type in
:menuselection:`Time Off app --> Configuration --> Time Off Types`:

- :guilabel:`Suspends the Engagement`: a validated time off of this type suspends the employment
  relationship while it lasts. The :doc:`engagement <engagements>` is shown as
  :guilabel:`Suspended`.
- :guilabel:`Salary Component`: the component the absence is counted under on the salary sheet. Its
  :guilabel:`Day Type` decides which day bucket — worked, paid leave, sick, or unpaid — the days
  are added to.

.. note::
   A time off type with no :guilabel:`Salary Component` does not appear on the salary sheet at all.
   Check the mapping of every type in use after installing a localization.

.. _salary/company-settings:

Company settings
================

The reconciliation defaults are kept on the company record: the :guilabel:`Payroll Mode` and
:guilabel:`Payroll Provider`, the default :guilabel:`Deviation Tolerance (Amount)` and
:guilabel:`Deviation Tolerance (%)` used when a component sets none, and
:guilabel:`Closing Requires No Blocking Deviation`, which is enabled by default.

.. seealso::
   - :doc:`hungary`
   - :doc:`engagements`

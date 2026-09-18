=======
Hungary
=======

The Hungarian human resources localization consists of two modules:

- **Hungarian HR Localization** (`l10n_hu_hr`) adds the Hungarian employee data — FEOR-08
  occupation codes, personal income tax reliefs and identifier validation. It works without the
  **Salary** application and is described in the :doc:`Employees <../employees/new_employee>`
  documentation as well.
- **Hungarian Salary Sheet** (`l10n_hu_hr_salary_sheet`) fills the **Salary** application's
  catalogues with the Hungarian data set, and adds the two rules that are genuinely Hungarian.

.. note::
   `l10n_hu_hr` does **not** depend on the `l10n_hu` accounting localization; the two can be
   installed independently.

.. _salary/hu/employee-data:

Hungarian employee data
=======================

FEOR-08 occupation codes
------------------------

Every Hungarian employment registration quotes an occupation code of the FEOR-08 classification.
The catalogue is available in :menuselection:`Employees app --> Configuration --> FEOR-08 Codes`,
with the :guilabel:`Code`, the :guilabel:`Designation` and the :guilabel:`Major Group`.

Set the default code of a job position in the :guilabel:`FEOR-08 Code` field of the job position.
A :doc:`contract <../employees/contracts>` inherits the code of its job position and can override
it.

Identifier validation
---------------------

The standard :guilabel:`Identification No` and :guilabel:`SSN No` fields of employees and of their
:ref:`dependants <employees/dependants-emergency>` are validated as the Hungarian tax identification code
(*adóazonosító jel*) and social security number (*TAJ*), check digit included. Spaces and dashes are
removed automatically, so a value typed with separators is accepted rather than rejected.

.. _salary/hu/tax-reliefs:

Personal income tax reliefs
---------------------------

The statutory relief catalogue is in :menuselection:`Employees app --> Configuration --> Tax Relief
Types`, in the legally fixed order of application. Each type carries its
:guilabel:`Maximum Duration (Months)`, its :guilabel:`Age Limit`, and whether it
:guilabel:`Requires Dependants`.

Record the reliefs an employee actually claims on the employee form, in the
:guilabel:`Tax Reliefs` tab:

- :guilabel:`Relief Type`: the statutory relief claimed.
- :guilabel:`Monthly Amount`: the monthly amount of the relief.
- :guilabel:`Valid From` and :guilabel:`Valid To`: the period the claim covers.
- :guilabel:`Dependants`: the dependants the relief is based on, for the relief types that require
  them.
- :guilabel:`Declaration Date`: the date of the employee declaration the claim is based on.

The :guilabel:`Status` of a claim is :guilabel:`Future`, :guilabel:`Active`, or
:guilabel:`Expired`, derived from its validity dates.

.. screenshot:: hr-salary-hu-tax-reliefs
   :menu: Employees ‣ Employees ‣ (open an employee) ‣ Tax Reliefs
   :shows: The Tax Reliefs tab listing a family relief claim with its relief type, monthly amount, validity dates, the dependants it is based on and its status.
   :highlight: The Dependants column and the Status column (red frame).
   :data: Employee "Anita Kovács" with a family relief valid from 2026-01-01 based on two dependants, status Active.
   :module: l10n_hu_hr
   :notes: English UI, light theme, 1440px width. Use invented personal data.

Employment state
----------------

The :guilabel:`Employment State` field in the :guilabel:`HR Settings` tab of the employee form is
derived, not entered: :guilabel:`Active` while a contract is running, :guilabel:`Suspended` while a
suspending time off covers today, and :guilabel:`Terminated` once the departure date has passed. It
is empty for an employee with no running contract.

EKHO on the contract
--------------------

When an employee has opted for the simplified contribution to public revenues, tick
:guilabel:`EKHO` on the contract and enter the :guilabel:`Wage Taxed Normally` — the part of the
gross wage still taxed under the general rules; the remainder falls under EKHO. The contract also
shows the :guilabel:`Weekly Hours` derived from the working schedule, which is the figure Hungarian
employment registrations are filed with.

.. _salary/hu/data-set:

The Hungarian salary data set
=============================

Installing **Hungarian Salary Sheet** fills the :doc:`catalogues <configuration>` with:

- **Contribution regimes** with dated factors, each carrying the legal reference its factors come
  from: :guilabel:`General Rules`, :guilabel:`EKHO`, :guilabel:`Employment of a Pensioner`,
  :guilabel:`Simplified Employment` and :guilabel:`Tax Free`.
- **Engagement types**: :guilabel:`Employment Relationship`, :guilabel:`Mandate Contract`,
  :guilabel:`Character or Article Fee`, :guilabel:`Casual Work or Event`,
  :guilabel:`Employment of a Pensioner` and :guilabel:`Private Individual with a Tax Number`.
- **Salary components**: :guilabel:`Base Salary`, :guilabel:`Absence Pay Supplement`,
  :guilabel:`Weekend Premium`, :guilabel:`Variable Bonus`, :guilabel:`Sick Leave Loss`,
  :guilabel:`Other Deduction`, :guilabel:`Tax Relief`, :guilabel:`Expense Reimbursement`,
  :guilabel:`Commuting Allowance`, :guilabel:`Net Payout (Reported)`, and the day counters
  :guilabel:`Worked Days`, :guilabel:`Sick Days`, :guilabel:`Leave Days` and
  :guilabel:`Unpaid Days`.
- **Time off mapping**: which absence suspends the employment relationship and which day bucket of
  the salary sheet it feeds. The mapping is written at installation and a later change made by the
  company survives a module update.

Sick leave loss
---------------

Hungarian sick leave is paid at 70% of the absence pay, so 30% of it is lost. The
:guilabel:`Sick Leave Loss` line of a :doc:`salary sheet <salary_sheets>` is the only value the
localization derives; it is computed from the gross of the month, the working days of the
:doc:`period <salary_periods>` and the number of sick days. The rate factors are read from the
contribution regime in force on the first day of the period, so a change in the statutory rate is a
data change and the months already closed keep their own figures.

Tax relief lines
----------------

A :guilabel:`Tax Relief` line is generated on the salary sheet for each relief the employee has
declared, for the months its validity actually covers. The line keeps a reference to the claim it
came from.

Regime split
------------

Hungarian figures have to be handed over to the payroll provider split by taxation. The
:guilabel:`Regime Split` tab of a salary sheet reports the :guilabel:`Gross`, :guilabel:`Net` and
:guilabel:`Employer Cost` separately under :guilabel:`General Rules` and under :guilabel:`EKHO`.

.. screenshot:: hr-salary-hu-regime-split
   :menu: Salary ‣ Salary ‣ Salary Sheets ‣ (open a sheet) ‣ Regime Split
   :shows: The Regime Split tab with the General Rules and EKHO groups, each showing gross, net and employer cost.
   :highlight: The EKHO group (red frame).
   :data: Employee with an EKHO contract, period "2026-03"; part of the wage under general rules, the rest under EKHO.
   :module: l10n_hu_hr_salary_sheet
   :notes: English UI, light theme, 1440px width.

.. seealso::
   - :doc:`configuration`
   - :doc:`../employees/contracts`

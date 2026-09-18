=========
Contracts
=========

A *contract* records the terms of an employee's position: when the employment starts and ends, the
job position and department, the working schedule, and the gross wage. Every employee who is paid,
or whose working time has to be tracked against a schedule, needs a running contract.

.. _employees/contract-dashboard:

Contracts dashboard
===================

To open the list of contracts, go to :menuselection:`Employees app --> Contracts`.

The :guilabel:`Contracts` page lists all contracts, grouped by :guilabel:`Status`. The available
statuses are :guilabel:`New`, :guilabel:`Running`, :guilabel:`Expired`, and :guilabel:`Cancelled`.
Each group displays the number of contracts it contains.

.. screenshot:: hr-contracts-dashboard
   :menu: Employees ‣ Contracts
   :shows: The Contracts list grouped by Status, with the New, Running and Expired groups expanded.
   :highlight: The Status group headers with their contract counts (red frame).
   :data: Demo company "YourCompany HU"; at least one contract in each of New, Running and Expired.
   :module: hr_contract
   :notes: English UI, light theme, 1440px width.

.. note::
   The :guilabel:`Contracts` menu and the contract data are only visible to users in the
   :guilabel:`Employee Manager` or :guilabel:`Administrator` access group of the **Employees** app.

.. _employees/new-contract:

Create a contract
=================

To create a contract, click :guilabel:`New` on the :ref:`Contracts dashboard
<employees/contract-dashboard>`, and fill in the blank contract form.

General information
-------------------

- :guilabel:`Contract Reference`: the name of the contract, such as `John Smith Contract`. This
  field is **required**.
- :guilabel:`Employee`: the employee the contract belongs to.
- :guilabel:`Contract Start Date`: the date the contract takes effect. Contracts can be created
  retroactively or with a future start date. Today's date is filled in by default. This field is
  **required**.
- :guilabel:`Contract End Date`: the end date of a fixed-term contract. Leave it empty for an
  open-ended contract.
- :guilabel:`Working Schedule`: the :doc:`working schedule <working_schedules>` the employee is
  expected to follow. Leaving the field empty makes the employee fully flexible, with no expected
  hours. If the selected schedule differs from the one on the employee's work information, Odoo
  displays a warning next to the field.
- :guilabel:`Salary Structure Type`: the salary structure type the contract belongs to, for example
  :guilabel:`Employee` or :guilabel:`Worker`. Structure types group contracts that share the same
  pay period and working-time rules.
- :guilabel:`Department`: the department the employee works in. It is filled in from the employee
  record and can be changed.
- :guilabel:`Job Position`: the employee's job position. It is also filled in from the employee
  record.
- :guilabel:`Contract Type`: the type of employment, for example :guilabel:`Permanent`,
  :guilabel:`Temporary`, :guilabel:`Seasonal`, :guilabel:`Full-Time`, :guilabel:`Part-Time`,
  :guilabel:`Intern`, :guilabel:`Student`, :guilabel:`Apprenticeship`, :guilabel:`Thesis`,
  :guilabel:`Statutory`, and :guilabel:`Employee`.
- :guilabel:`HR Responsible`: the user responsible for validating the contract.

.. screenshot:: hr-contracts-new-contract
   :menu: Employees ‣ Contracts ‣ New
   :shows: A filled-in contract form with the status bar on New, and the Contract Reference, Employee, start and end dates, Working Schedule, Salary Structure Type, Department, Job Position and Contract Type fields completed.
   :highlight: The general information group above the tabs (red frame).
   :data: Employee "Anita Kovács", contract "Anita Kovács Contract", Working Schedule "Standard 40 hours/week", Contract Type "Permanent".
   :module: hr_contract
   :notes: English UI, light theme, 1440px width.

Salary Information tab
----------------------

Enter the employee's monthly gross :guilabel:`Wage` in this tab. The wage is used by reporting and
by any salary administration module installed on top of the contract.

.. note::
   With the :doc:`Salary <../salary>` application installed, this tab also shows the
   :guilabel:`Engagement` and the :guilabel:`Salary Term` that currently apply to the employee, and
   a :guilabel:`Take the wage from the salary term` button appears when the contract wage no longer
   matches the agreed salary term.

Details tab
-----------

Enter any free-text :guilabel:`Notes` about the contract here. This tab is only visible to
contract managers.

Contract status
===============

A new contract starts in the :guilabel:`New` status. Set the status with the status bar at the top
of the form:

- :guilabel:`New`: the contract is being prepared.
- :guilabel:`Running`: the contract is in force. A contract in the :guilabel:`New` status whose
  kanban state is set to ready and whose start date has arrived is set to :guilabel:`Running`
  automatically.
- :guilabel:`Expired`: the end date has passed. Contracts are expired automatically on their end
  date.
- :guilabel:`Cancelled`: the contract never took effect.

.. tip::
   Odoo notifies the :guilabel:`HR Responsible` before a contract expires and before an employee's
   work permit expires. The notice periods are set per company in :menuselection:`Settings -->
   Employees`.

Trial period and work permit
============================

The :guilabel:`End of Trial Period` date records when the employee's trial period ends, and the
:guilabel:`Work Permit No` and :guilabel:`Visa No` fields carry the corresponding values from the
:ref:`employee's HR settings <employees/hr-settings>`; editing them on the contract updates the
employee record as well.

.. seealso::
   - :doc:`working_schedules`
   - :doc:`../salary`

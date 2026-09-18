:show-content:

======
Salary
======

The **Salary** application administers what a company owes its employees, and reconciles it with the
figures returned by the payroll provider. It deliberately does **not** calculate payroll: there is
no formula engine and no tax calculation in the application. What it does is:

- record the :doc:`engagements <salary/engagements>` (employment relationships) of a person, and the
  dated chain of *salary terms* that fix the agreed amount;
- build a monthly :doc:`salary sheet <salary/salary_sheets>` per engagement, where every value —
  the base salary included — is a line referring to a component of a catalogue;
- :doc:`reconcile <salary/reconciliation>` those lines with the figures the external payroll
  program returns, and report the deviations;
- close the month immutably, so that a later correction of a time off request can never silently
  rewrite a month that has already been reported.

.. important::
   **Salary** requires the :doc:`Employees <employees>` and :doc:`Time Off <time_off>` applications,
   and it works on employee :doc:`contracts <employees/contracts>`.

   Everything that differs between countries — salary components, contribution regimes and
   engagement types — is data, shipped by a localization module. Install the localization for the
   company's country, for example :doc:`Hungary <salary/hungary>`, before using the application;
   without one the catalogues are empty.

.. cards::

   .. card:: Engagements and salary terms
      :target: salary/engagements

      Record employment relationships and the agreed salary that applies from a given date.

   .. card:: Salary periods
      :target: salary/salary_periods

      Open a month, generate its sheets, and close it immutably.

   .. card:: Salary sheets
      :target: salary/salary_sheets

      The monthly grid of amounts and days per engagement.

   .. card:: Reconciliation
      :target: salary/reconciliation

      Import the payroll provider's statement and handle the deviations.

   .. card:: Configuration
      :target: salary/configuration

      Salary components, engagement types, contribution regimes and time off mapping.

   .. card:: Hungary
      :target: salary/hungary

      The Hungarian data set and its specific rules.

.. _salary/access-rights:

Access rights
=============

The application ships three access groups, configured per user in :menuselection:`Settings -->
Users & Companies --> Users`:

- :guilabel:`Salary User`: sees the :guilabel:`Salary` menu, the engagements, terms, periods and
  sheets, and may enter amounts on an open sheet.
- :guilabel:`Salary Manager`: in addition, may confirm and close records, open the
  :guilabel:`Configuration` menu, and correct a wage that no longer matches the salary term.
- :guilabel:`Salary Approver`: may reopen a closed salary period or salary sheet.

Salary data is personal data of the employees. Only grant these groups to the people who administer
payroll.

.. toctree::
   :titlesonly:

   salary/engagements
   salary/salary_periods
   salary/salary_sheets
   salary/reconciliation
   salary/configuration
   salary/hungary

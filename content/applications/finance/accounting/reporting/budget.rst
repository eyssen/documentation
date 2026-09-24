=======
Budgets
=======

Managing budgets is an essential part of running a business. Budgets help people become more
intentional with the way money is spent and direct people to organize and prioritize their work to
meet financial goals. They allow the planning of a desired financial outcome and then measure the
actual performance against the plan.

Budgets in Odoo are built from two elements: **budgetary positions**, which say *which accounts* a
budget line follows, and **budgets**, which say *how much* is planned on those positions over a
period, optionally per analytic account.

.. note::
   Budgets are provided by the *Budget Management* module, which is installed together with
   :guilabel:`eYssen Accountant`.

.. _accounting/budget/positions:

Budgetary positions
===================

**Budgetary positions** are the accounts of your :doc:`chart of accounts
<../get_started/chart_of_accounts>` a budget is measured against, grouped under a meaningful name
(for example *Sales*, *Purchases of goods*, *Vehicle costs*).

To define them, go to :menuselection:`Accounting --> Configuration --> Management --> Budgetary
Positions` and click :guilabel:`New`. Enter a :guilabel:`Name` and select the :guilabel:`Accounts`
the position covers.

.. tip::
   Create one budgetary position per line you want to steer, and keep an account in a single
   position, otherwise the actual amounts are counted twice.

.. screenshot:: accounting-budget-position
   :menu: Accounting ‣ Configuration ‣ Management ‣ Budgetary Positions ‣ (a position)
   :shows: A budgetary position form with the Name field and the list of accounts it covers.
   :highlight: The Accounts list (red frame).
   :data: Position "Vehicle costs" covering the fuel, maintenance and insurance expense accounts.
   :module: om_account_budget
   :notes: English UI, light theme, 1440px width.

.. _accounting/budget/create:

Create a budget
===============

Go to :menuselection:`Accounting --> Configuration --> Management --> Budgets` and click
:guilabel:`New`. Fill out:

- :guilabel:`Budget Name`;
- :guilabel:`Responsible`, the user in charge of it;
- the :guilabel:`Period`, i.e. the :guilabel:`Start Date` and :guilabel:`End Date`.

Then add the budget lines in the :guilabel:`Budget Lines` tab. For each line, set:

:guilabel:`Budgetary Position`
   The position the line follows.

:guilabel:`Analytic Account`
   Optional. Restricts the line to a :doc:`analytic account <analytic_accounting>`, for example a
   project, a department, or a vehicle.

:guilabel:`Start Date` / :guilabel:`End Date`
   The period of the line. It may be shorter than the budget period, for example to plan month by
   month.

:guilabel:`Planned Amount`
   The amount you plan to earn or to spend. **Enter a positive amount for revenue and a negative
   amount for a cost.**

.. _accounting/budget/follow-up:

Follow the budget
=================

Three amounts are computed on each line as entries are posted:

:guilabel:`Practical Amount`
   What has actually been earned or spent so far, taken from the posted journal items of the
   accounts of the budgetary position (and of the analytic account, when one is set).

:guilabel:`Theoretical Amount`
   What should have been earned or spent at today's date, i.e. the planned amount prorated over the
   elapsed part of the line's period.

:guilabel:`Achievement`
   The practical amount as a percentage of the theoretical one. It tells you at a glance whether you
   are ahead of or behind the plan.

Lines that are over budget are highlighted in the list, in green for revenue and in red for costs.
Click a line to open the journal items behind its practical amount.

.. screenshot:: accounting-budget-lines
   :menu: Accounting ‣ Configuration ‣ Management ‣ Budgets ‣ (a budget)
   :shows: A budget form in the "Confirmed" state, with its Budget Lines tab listing the budgetary
      position, the analytic account, the period, and the Planned / Practical / Theoretical amounts
      with the Achievement percentage, one line highlighted as over budget.
   :highlight: The Practical, Theoretical and Achievement columns (red frame).
   :data: Budget "2026 operating budget" with four lines, one of them over budget.
   :module: om_account_budget
   :notes: English UI, light theme, 1440px width.

.. _accounting/budget/states:

Budget approval flow
====================

A budget goes through a short approval flow, shown in the status bar:

#. :guilabel:`Draft` — the budget is being prepared and can still be edited.
#. :guilabel:`Confirm` moves it to :guilabel:`Confirmed`, i.e. submitted for approval.
#. :guilabel:`Approve` moves it to :guilabel:`Validated`.
#. :guilabel:`Done` closes the budget at the end of its period.

:guilabel:`Cancel Budget` is available while the budget is confirmed or validated, and
:guilabel:`Reset to Draft` brings a cancelled budget back for editing.

.. _accounting/budget/analysis:

Budgets Analysis
================

:menuselection:`Accounting --> Reporting --> Management --> Budgets Analysis` opens all budget lines of
all budgets in one place, with list, pivot and graph views. Cancelled budgets are excluded by
default and the lines are grouped by budget. Use it to compare several budgets, to analyze the
achievement per analytic account, or to build a pivot of planned versus practical amounts.

.. tip::
   The planned amounts can also be displayed next to the actuals in the
   :doc:`dynamic reports <dynamic_reports>`, with the :guilabel:`Budget Comparison` filter.

.. seealso::
   - :doc:`analytic_accounting`
   - :doc:`dynamic_reports`

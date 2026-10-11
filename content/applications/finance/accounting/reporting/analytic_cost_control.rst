=====================
Analytic cost control
=====================

*Analytic Cost Control* (`account_analytic_cost_control`) adds plan-versus-actual cost control on top
of :doc:`analytic accounts <analytic_accounting>`: a cost plan per analytic account, the committed
and actual costs, the revenue, and the margin. A typical use is the follow-up of **work numbers**
(job numbers), but it works with any analytic plan: projects, cost centers, etc.

The module adds no field to the documents. Customer invoices, vendor bills, purchase and sales
order lines, timesheets, expenses, and stock valuation are booked to an analytic account through the
standard :ref:`analytic distribution <accounting/analytic_accounting/analytic-distribution>` of
their lines. The module then compares these booked items with the cost plan.

.. note::
   The module depends only on *Accounting*. The :guilabel:`Contract Value` of the summary is only
   available if *Sales* is installed, and the :guilabel:`Committed` column only if *Purchase* is
   installed.

.. _accounting/analytic_cost_control/activate:

Activate the feature
====================

Go to :menuselection:`Settings --> eYssen ERP`, and, in the :guilabel:`Analytic Cost Control`
section, enable :guilabel:`Analytic Cost Control`. Then, click :guilabel:`Save`.

The menus, the summary, and the cost plan are only displayed if analytic accounting is enabled. Go
to :menuselection:`Accounting --> Configuration --> Settings`, and, in the :guilabel:`Analytics`
section, enable :guilabel:`Analytic Accounting`. Then, click :guilabel:`Save`.

.. _accounting/analytic_cost_control/plan:

Configure an analytic plan
==========================

The module does **not** create any analytic plan when it is installed. Choose the plans to follow
up: either enable the cost control on an existing plan (e.g., :guilabel:`Projects`), or create a new
plan.

Go to :menuselection:`Accounting --> Configuration --> Analytic Plans`, open a plan, and set:

- :guilabel:`Cost Control`: the analytic accounts of this plan get the cost plan, the summary, and
  the plan / actual report.
- :guilabel:`Code Sequence` (optional, independent of :guilabel:`Cost Control`): select a sequence.
  The new analytic accounts of this plan that have no :guilabel:`Reference` get their reference from
  this sequence. For example, with the prefix `WN/%(year)s/`, the first work number of 2026 is
  `WN/2026/00001`.

.. important::
   Both options can only be set on a **root** analytic plan, not on a sub-plan. Otherwise, the error
   *Cost control and the code sequence can only be set on a root analytic plan.* is displayed.

.. tip::
   To follow up work numbers, create an analytic plan named `Work Numbers`, tick
   :guilabel:`Cost Control`, and create a sequence with the prefix `WN/%(year)s/` and a padding of
   `5` in :guilabel:`Code Sequence`. Projects carry the analytic accounts of all the plans, so the
   timesheets of a project that is linked to a work number are booked to it automatically.

.. _accounting/analytic_cost_control/classification:

How the analytic items are classified
=====================================

Every analytic item is classified when it is booked. The classification is stored and is used in the
summary, the lists, and the report.

**Revenue or cost**

An item is **revenue** if its financial account is an income account. An item without a financial
account is revenue if its amount is positive and it is not a timesheet. Any other item is a cost.

**Cost category**

A cost is either :guilabel:`Labour`, :guilabel:`Material`, or :guilabel:`Other Costs`. The category
is the first one that applies in this order:

#. the :guilabel:`Cost Category` of the financial account (:menuselection:`Accounting -->
   Configuration --> Chart of Accounts`, in the account form; the field is not displayed for income
   and balance sheet accounts);
#. the :guilabel:`Cost Category` of the product category (:menuselection:`Inventory --> Configuration
   --> Product Categories`, or the same menu of :guilabel:`Invoicing`, in the :guilabel:`Cost
   Control` group); sub-categories inherit it;
#. the product type: a service is :guilabel:`Labour`, a goods product is :guilabel:`Material`;
#. a timesheet line is :guilabel:`Labour`;
#. anything else is :guilabel:`Other Costs`.

**Own or external**

A cost is :guilabel:`External` if it comes from a vendor bill (including receipts), and
:guilabel:`Own` for everything else: timesheets, stock valuation, payroll, and miscellaneous entries.

.. note::
   If the :guilabel:`Cost Category` of a parent product category is changed, the items that are
   already booked are not recomputed. Changing it on the financial account or on the product's own
   category does recompute them.

.. _accounting/analytic_cost_control/account:

The analytic account form
=========================

The following elements are only displayed on the analytic accounts of a plan with
:guilabel:`Cost Control`, and only to the users of the :guilabel:`Analytic Accounting` group. To open
an account, go to :menuselection:`Accounting --> Accounting --> Cost Control`, or
:menuselection:`Accounting --> Configuration --> Analytic Accounts`.

The form has the new fields :guilabel:`Responsible Users` and :guilabel:`Original Plan Saved On`
(read-only), and its chatter also supports activities.

Cost plan
---------

The :guilabel:`Cost Plan` tab contains editable lines with the following columns, and the totals at
the bottom:

- :guilabel:`Cost Category`: :guilabel:`Labour`, :guilabel:`Material`, or :guilabel:`Other Costs`.
- :guilabel:`Own / External`.
- :guilabel:`Description`.
- :guilabel:`Original Plan`: read-only, set by the :guilabel:`Save as Original Plan` button.
- :guilabel:`Current Plan`: the amount that is currently planned.

The :guilabel:`Notes` tab contains free rich-text notes.

When the quotation is accepted, click :guilabel:`Save as Original Plan` and confirm the message *The
current cost plan overwrites the original plan. Continue?* The :guilabel:`Current Plan` of every
cost plan line is copied to its :guilabel:`Original Plan`, the date is recorded in
:guilabel:`Original Plan Saved On`, and a message is posted in the chatter. From then on, the
:guilabel:`Current Plan` can be adjusted while the :guilabel:`Original Plan` keeps the figures of the
quotation. If the account has no cost plan lines, an error is displayed.

The :guilabel:`Plan / Actual` smart button opens the :ref:`plan / actual analysis
<accounting/analytic_cost_control/report>` filtered on the account and grouped by cost category and
by own / external.

.. _accounting/analytic_cost_control/summary:

Summary
-------

The summary at the top of the form shows these indicators:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Indicator
     - Meaning
   * - :guilabel:`Contract Value`
     - The untaxed amount of the confirmed sales order lines distributed to this account, in
       proportion to the distribution percentage. Only displayed if *Sales* is installed.
   * - :guilabel:`Invoiced Revenue`
     - The revenue items booked to the account.
   * - :guilabel:`Actual Cost`
     - The cost items booked to the account.
   * - :guilabel:`Margin`
     - The invoiced revenue minus the actual cost, with the margin as a percentage of the revenue.
   * - :guilabel:`Planned Margin`
     - The contract value minus the current plan. Only displayed if there is a contract value.

Below the indicators, a table has one row per :guilabel:`Labour`, :guilabel:`Material`, and
:guilabel:`Other Costs`, and a :guilabel:`Total` row. Its columns are:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Column
     - Content
   * - :guilabel:`Original Plan`
     - The plan :guilabel:`At quotation`, with the date on which it was saved.
   * - :guilabel:`Current Plan`
     - The total, and its own / external split.
   * - :guilabel:`Committed`
     - The :guilabel:`Open purchase orders`: the part not yet billed of the confirmed purchase order
       lines distributed to this account, in proportion to the distribution percentage. The
       category comes from the product. Only displayed if *Purchase* is installed.
   * - :guilabel:`Actual Cost`
     - The total, and its own / external split.
   * - :guilabel:`Completion`
     - The actual cost divided by the plan, as a total and as an own / external split. It is green
       up to 90%, orange from 90% to 100%, and red above 100%. A dash is displayed if there is no
       plan.

Click an amount to see the records behind it: the actual amounts open the analytic items (filtered
by category and by own / external), :guilabel:`Invoiced Revenue` opens the revenue items,
:guilabel:`Committed` opens the purchase orders, and :guilabel:`Contract Value` opens the sales
orders.

.. note::
   The amounts are displayed in the currency of the company of the analytic account. Amounts in
   other currencies are converted at today's rate.

.. _accounting/analytic_cost_control/menus:

Menus
=====

Cost control list
-----------------

Go to :menuselection:`Accounting --> Accounting --> Cost Control` to list the analytic accounts of
the plans with :guilabel:`Cost Control`, with the columns :guilabel:`Reference`, :guilabel:`Name`,
:guilabel:`Plan`, :guilabel:`Customer`, :guilabel:`Responsible Users`, :guilabel:`Activities`,
:guilabel:`Cost`, :guilabel:`Revenue`, and :guilabel:`Margin`. The :guilabel:`I'm Responsible`
filter keeps the accounts of which you are a responsible user. Clicking :guilabel:`New` creates an
account in the first plan with :guilabel:`Cost Control`.

.. _accounting/analytic_cost_control/report:

Plan / actual analysis
----------------------

Go to :menuselection:`Accounting --> Reporting --> Management --> Plan / Actual Analysis`. The
report is available as a pivot table, a graph, and a list. It has one row per cost plan line and one
row per analytic item booked to an account of a plan with :guilabel:`Cost Control`.

- **Measures**: :guilabel:`Original Plan`, :guilabel:`Current Plan`, :guilabel:`Actual Cost`,
  :guilabel:`Remaining Plan` (the current plan minus the actual cost), :guilabel:`Revenue`, and
  :guilabel:`Margin` (the revenue minus the actual cost).
- **Dimensions**: :guilabel:`Analytic Account`, :guilabel:`Analytic Plan`, :guilabel:`Customer`,
  :guilabel:`Cost Category` (including :guilabel:`Revenue`), :guilabel:`Own / External`,
  :guilabel:`Source` (:guilabel:`Cost Plan` or :guilabel:`Booked`), :guilabel:`Financial Account`,
  :guilabel:`Product`, and :guilabel:`Date`.
- **Filters**: :guilabel:`Costs`, :guilabel:`Revenue`, :guilabel:`Own`, :guilabel:`External`, and
  :guilabel:`Date`.

.. note::
   The cost plan lines have no date. When a :guilabel:`Date` filter is applied, only the booked
   figures are displayed.

Analytic items
--------------

When the analytic items are opened from the summary, the list shows the additional columns
:guilabel:`Cost Category` and :guilabel:`Own / External`. In the search view, the items can be
grouped by :guilabel:`Cost Control Account`, :guilabel:`Cost Category`, and :guilabel:`Own /
External`.

.. seealso::
   - :doc:`analytic_accounting`
   - :doc:`budget`
   - :doc:`/applications/general/eyssen_erp_settings`

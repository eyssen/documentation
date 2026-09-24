=============
Sales targets
=============

The *Sales Target* module (``sales_target``) sets a measurable goal for a salesperson or for a
sales team over a period, and measures the achievement live from the orders and invoices in the
database.

Create a target
===============

Targets are kept in two lists, one per level:

- :menuselection:`Sales app --> Targets --> Salesperson Targets`
- :menuselection:`Sales app --> Targets --> Team Targets`

Click :guilabel:`New` and fill in:

- :guilabel:`Salesperson` or :guilabel:`Sales Team`: who the target belongs to.
- :guilabel:`Start Date` and :guilabel:`End Date`: the period measured.
- :guilabel:`Responsible`: who follows the target up. Defaults to the current user.
- :guilabel:`Measure`: what is counted towards the target (see below).
- :guilabel:`Target Amount`: the goal, in the company currency.
- :guilabel:`Company`: the company the target belongs to.

The :guilabel:`Reference` is generated automatically.

What is measured
================

The :guilabel:`Measure` field decides which documents count:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Measure
     - Counted
   * - :guilabel:`Confirmed Orders`
     - The untaxed amount of the sales orders confirmed in the period.
   * - :guilabel:`Fulfilled Order Lines`
     - The untaxed amount of the order lines actually delivered in the period.
   * - :guilabel:`Validated Invoices`
     - The untaxed amount of the customer invoices posted in the period.
   * - :guilabel:`Paid Invoices`
     - The untaxed amount of the customer invoices paid in the period.

Every amount is converted to the company currency, so targets can be compared across currencies.

Following the achievement
=========================

The target form shows the :guilabel:`Achieved Amount`, the :guilabel:`Difference` from the goal and
the :guilabel:`Achievement %`. Click :guilabel:`Refresh` to recompute them on demand.

Two tabs show exactly what was counted: :guilabel:`Contributing Order Lines` and
:guilabel:`Contributing Invoices`. Use them when a figure looks wrong — they are the audit trail of
the measurement.

.. screenshot:: sales-targets-form
   :menu: Sales ‣ Targets ‣ Salesperson Targets ‣ (a target)
   :shows: A salesperson target in the Confirmed state, with the period, the Measure and Target Amount fields, the Achievement group (achieved amount, difference, achievement %) and the Contributing Order Lines tab.
   :highlight: The Achievement group (red frame).
   :data: Target for "Marc Demo", Q1 2026, measure "Validated Invoices", target 50 000, achieved 38 400 (77%).
   :module: sales_target
   :notes: English UI, light theme, 1440px width, full form.

Target states
=============

A target moves through four states with the header buttons: :guilabel:`Draft` ‣
:guilabel:`Confirm` ‣ :guilabel:`Confirmed`, then :guilabel:`Close` to end it or
:guilabel:`Cancel` to drop it. :guilabel:`Reset to Draft` brings a closed or cancelled target back.

The :guilabel:`My Targets` filter on the list shows the targets of the current user; grouping by
:guilabel:`Salesperson`, :guilabel:`Sales Team` and :guilabel:`Status` is available in the search
panel.

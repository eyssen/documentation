======================
Subscription contracts
======================

A **contract** is the agreement with one customer. It holds the customer, the company and the
billing journal, the optional trial and coupon, the payment method used for automatic charging, and
the subscription lines that are actually billed.

Create a contract
=================

Go to :menuselection:`Subscriptions app --> Contracts` and click :guilabel:`New`. The
:guilabel:`Contract Number` is generated automatically on saving.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Customer`
     - The invoiced partner. Required.
   * - :guilabel:`Start Date` / :guilabel:`End Date`
     - The agreement's own dates. They are informative for the contract; each line carries its own
       billing dates.
   * - :guilabel:`Trial End`
     - While this date is in the future, the contract is :guilabel:`In Trial` and no recurring
       invoice is generated.
   * - :guilabel:`Coupon`
     - A :doc:`coupon <configuration>` applied to every recurring invoice of the contract.
   * - :guilabel:`Close Reason`
     - Filled in automatically when the contract is closed.
   * - :guilabel:`Company`
     - The company the contract belongs to. Only shown in a multi-company database.
   * - :guilabel:`Billing Journal`
     - The sales journal used for the generated invoices. Defaults to the company's sales journal.
   * - :guilabel:`Invoice Posting`
     - :guilabel:`Leave as draft for review` (default) or :guilabel:`Post automatically`. This is a
       contract-level policy: it applies to every line.
   * - :guilabel:`Currency`
     - The contract currency. All lines use it.
   * - :guilabel:`MRR` / :guilabel:`ARR`
     - Computed monthly and annual recurring revenue, normalised from the period of every active
       line. :guilabel:`ARR` is :guilabel:`MRR` × 12.
   * - :guilabel:`Payment Token`
     - The stored card or SEPA mandate used for :doc:`automatic charging <automatic_payments>`.
   * - :guilabel:`Dunning State`
     - :guilabel:`OK`, :guilabel:`Retry pending` or :guilabel:`Hard decline`. Read-only.

.. screenshot:: sales-subscriptions-contract-form
   :menu: Subscriptions ‣ Contracts ‣ (a contract)
   :shows: A subscription contract form in the Active state: the Customer field, the Contract group (dates, trial end, coupon), the Billing group (journal, invoice posting, MRR, ARR), the Payment group and the Lines tab.
   :highlight: The status bar and the Confirm/Suspend/Close buttons (red frame).
   :data: Contract SUB/2026/0012 for "Deco Addict", MRR 58.00, two lines.
   :module: subscription
   :notes: English UI, light theme, 1440px width, full form.

Contract states
===============

The contract moves through five states, using the buttons in the header:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - State
     - Meaning
   * - :guilabel:`Draft`
     - Being prepared. Click :guilabel:`Confirm` to activate it.
   * - :guilabel:`Active`
     - Billing runs. The lines can be invoiced by the :doc:`billing scheduled action <billing>`.
   * - :guilabel:`Suspended`
     - Billing is paused. Click :guilabel:`Reactivate` to resume, or :guilabel:`Close` to end it.
   * - :guilabel:`Expired`
     - The agreement ran out. It can be reactivated or closed.
   * - :guilabel:`Closed`
     - Final. A closed contract cannot be reopened.

The allowed transitions are enforced by the server, not only hidden in the interface:

- :guilabel:`Draft` ‣ :guilabel:`Active`
- :guilabel:`Active` ‣ :guilabel:`Suspended`, :guilabel:`Expired` or :guilabel:`Closed`
- :guilabel:`Suspended` ‣ :guilabel:`Active` or :guilabel:`Closed`
- :guilabel:`Expired` ‣ :guilabel:`Active` or :guilabel:`Closed`

Suspending a contract also pauses its lines; reactivating it resumes them without billing the
periods that elapsed while it was suspended. See :ref:`sales/subscriptions/pause-resume`.

Trial periods
=============

Set :guilabel:`Trial End` to a future date to give the customer a free period. While the contract is
in trial, the :guilabel:`In Trial` flag is set and the billing scheduled action skips its lines. A
daily scheduled action raises a to-do activity for the salesperson three days before the trial ends,
so the contract can be reviewed before the first invoice goes out.

Filters and grouping
====================

The contract list offers the :guilabel:`Draft`, :guilabel:`Active`, :guilabel:`Suspended`,
:guilabel:`Expired`, :guilabel:`Closed`, :guilabel:`In Trial`, :guilabel:`Payment Issue` and
:guilabel:`Archived` filters, and grouping by :guilabel:`Customer`, :guilabel:`State`,
:guilabel:`Billing Journal` and :guilabel:`Company`.

.. seealso::
   - :doc:`lines`
   - :doc:`billing`
   - :doc:`automatic_payments`

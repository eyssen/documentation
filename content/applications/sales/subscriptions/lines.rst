==================
Subscription lines
==================

A **subscription line** is what is actually billed. One contract can hold several lines, each with
its own product, price, billing period and dates. Lines are edited from the :guilabel:`Lines` tab of
a contract, or from :menuselection:`Subscriptions app --> Subscription Lines`.

Basic fields
============

- :guilabel:`Description`: the label of the line.
- :guilabel:`Product`: only products flagged as :doc:`subscription products <products>` are offered.
- :guilabel:`Service Address`: an address of the customer (or one of its child contacts) where the
  service is delivered. Optional.
- :guilabel:`Start Date`: the first day the line covers. Required — every period is derived from it.
- :guilabel:`Contract End`: the hard upper bound of automatic renewal. Once the billed periods reach
  this date, no further invoice is generated. Leave it empty for an open-ended subscription.
- :guilabel:`Auto-renew`: when disabled, billing stops after the first period.
- :guilabel:`UoM`, :guilabel:`Discount`, :guilabel:`Payment Term`: as on an ordinary invoice line.
- :guilabel:`Invoice Note`: overrides the invoice line label. The placeholders `#START#`, `#END#`
  and `#PERIOD#` are replaced with the billed period.

Read-only fields show where the line stands: :guilabel:`Paid Until` (the last day covered by a
posted invoice), :guilabel:`Next Period Start` and :guilabel:`Next Period End`,
:guilabel:`Last Invoice` and :guilabel:`Next Invoice`.

.. screenshot:: sales-subscriptions-line-form
   :menu: Subscriptions ‣ Subscription Lines ‣ (a line)
   :shows: A subscription line form: the status bar with the Activate/Pause/Close buttons, the Pricing group (product, pricing model, unit price, price basis), the billing group (period, invoice method, invoice basis, dates) and the Paid Until / Next Invoice fields.
   :highlight: The Pricing group (red frame).
   :data: Line "Hosting – Standard plan" on contract SUB/2026/0012, monthly, 29.00.
   :module: subscription
   :notes: English UI, light theme, 1440px width, full form.

Line states
===========

A line has the same five states as the contract: :guilabel:`Draft`, :guilabel:`Active`,
:guilabel:`Inactive`, :guilabel:`Expired` and :guilabel:`Closed`. The header buttons are
:guilabel:`Activate`, :guilabel:`Pause` and :guilabel:`Close`. Only :guilabel:`Active` lines are
invoiced.

.. _sales/subscriptions/pause-resume:

Pausing and resuming
--------------------

Pausing a line stops billing. When it is activated again, a :guilabel:`Billing Resumes On` date is
set: periods that ended before that date are **not** billed retroactively. A subscription paused for
six months therefore does not produce six invoices when it comes back.

Pricing
=======

The :guilabel:`Pricing Model` field decides how the invoiced amount is computed:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Pricing model
     - Calculation
   * - :guilabel:`Flat fee`
     - The agreed :guilabel:`Quantity` × :guilabel:`Unit price`.
   * - :guilabel:`Per seat`
     - The quantity comes from a seat source instead of the fixed quantity.
   * - :guilabel:`Usage-based`
     - The quantity comes from measured usage for the billed period.
   * - :guilabel:`Tiered`
     - The unit price depends on the quantity, using the brackets in the :guilabel:`Pricing Tiers`
       tab.

:guilabel:`Price Basis` says what the :guilabel:`Unit price` covers:

- :guilabel:`Per billing period`: the price covers one whole period, whatever its length.
- :guilabel:`Per month`: the price is a monthly rate, and the invoice multiplies it by the number of
  months in the billing period. The computed :guilabel:`Period Multiplier` field shows that factor.

Pricing tiers
-------------

For a :guilabel:`Tiered` line, add brackets in the :guilabel:`Pricing Tiers` tab: :guilabel:`Min
Qty`, :guilabel:`Max Qty` (exclusive; leave `0` for the open-ended top bracket) and :guilabel:`Unit
Price`. The :guilabel:`Mode` field decides how they are combined:

- :guilabel:`Graduated`: every bracket is priced separately and the results are added up.
- :guilabel:`Volume`: one single per-unit price is used, taken from the bracket the **total**
  quantity falls into.

.. example::
   Brackets `0–10` at `5.00`, `10–50` at `4.00` and `50–0` at `3.00`, with a quantity of 20:

   - :guilabel:`Graduated`: 10 × 5.00 + 10 × 4.00 = `90.00`
   - :guilabel:`Volume`: 20 × 4.00 = `80.00`

.. screenshot:: sales-subscriptions-line-tiers
   :menu: Subscriptions ‣ Subscription Lines ‣ (a tiered line) ‣ Pricing Tiers
   :shows: The Pricing Tiers tab of a subscription line with three brackets (Mode, Min Qty, Max Qty, Unit Price).
   :highlight: The tier list (red frame).
   :data: Graduated tiers 0–10 = 5.00, 10–50 = 4.00, 50–0 = 3.00.
   :module: subscription
   :notes: English UI, light theme, 1440px width, crop to the notebook.

Quantity
========

- :guilabel:`Quantity`: the agreed quantity of the line.
- :guilabel:`Quantity Source`: where the billable quantity comes from. :guilabel:`Static (contract
  quantity)` uses the agreed quantity; :guilabel:`Formula` evaluates a :doc:`quantity formula
  <configuration>`. Modules that extend the application add further sources.
- :guilabel:`Quantity Basis`: what to do when the measured quantity differs from the agreed one.
  :guilabel:`Contract quantity (measured value advisory)` invoices the agreed quantity and only
  raises an activity when the measurement diverges; :guilabel:`Measured value` invoices what was
  measured.
- :guilabel:`Quantity Formula`: the formula used when the source is :guilabel:`Formula`.

Billing period and dates
========================

- :guilabel:`Period`: the :doc:`billing period <configuration>` — for example `Monthly` or
  `Yearly`. It drives every date computation.
- :guilabel:`Invoice Method`:

  - :guilabel:`In advance`: the invoice is issued on the first day of the period it covers.
  - :guilabel:`In arrears`: it is issued the day after the period ends.

- :guilabel:`Invoice Basis`:

  - :guilabel:`Start date`: periods run from the line's own :guilabel:`Start Date`.
  - :guilabel:`Calendar`: periods are aligned to calendar month or year boundaries.
  - :guilabel:`Anchor Day`: periods start on a fixed day of the month, set in :guilabel:`Anchor
    Day`. Only days 1–28 are allowed, so that every month has one.

.. example::
   A line starting on 15 March with a monthly period bills 15 March – 14 April on the
   :guilabel:`Start date` basis, 1–31 March on the :guilabel:`Calendar` basis, and — with
   :guilabel:`Anchor Day` `1` — 1 March – 31 March.

History and invoices
====================

- :guilabel:`Invoices`: every invoice the line appears on.
- :guilabel:`Billed Periods`: one row per invoice line, with the exact period it covers, the
  quantity, the unit price and the invoice state. This is the audit trail of what was billed when.
- :guilabel:`Change History`: every change to the line — when, by whom, which field, the old and the
  new value — with the correction invoice, if one was issued.

.. screenshot:: sales-subscriptions-line-billed-periods
   :menu: Subscriptions ‣ Subscription Lines ‣ (a line) ‣ Billed Periods
   :shows: The Billed Periods tab listing the invoice, the period start and end, the quantity, the unit price, the subtotal and the invoice state badge.
   :highlight: The period start and end columns (red frame).
   :data: Three monthly periods of line "Hosting – Standard plan".
   :module: subscription
   :notes: English UI, light theme, 1440px width, crop to the notebook.

.. seealso::
   - :doc:`billing`
   - :doc:`configuration`

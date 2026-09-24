=============
Configuration
=============

The :menuselection:`Subscriptions app --> Configuration` menu holds the three records the
subscription lines are built from.

.. _sales/subscriptions/periods:

Billing periods
===============

A **billing period** is the recurrence a subscription line is billed on. Go to
:menuselection:`Subscriptions app --> Configuration --> Billing Periods`.

- :guilabel:`Period`: the name shown on the lines, for example `Monthly` or `Yearly`.
- :guilabel:`Period Type`: :guilabel:`Day`, :guilabel:`Week`, :guilabel:`Month` or
  :guilabel:`Year`. This is what every date computation uses.
- :guilabel:`Quantity`: how many of those units one period contains. `Period Type` = `Month` with
  `Quantity` = `3` is a quarterly period.
- :guilabel:`UoM`: an optional display unit from the *Working Time* unit category. It is **not**
  used for date arithmetic.

.. important::
   Always set the :guilabel:`Period Type` correctly: the dates are derived from it, not from the
   period's name or its unit of measure.

.. screenshot:: sales-subscriptions-billing-periods
   :menu: Subscriptions ‣ Configuration ‣ Billing Periods
   :shows: The Billing Periods list with the Period, Period Type, Quantity and UoM columns for a monthly, a quarterly and a yearly period.
   :highlight: The Period Type column (red frame).
   :data: Monthly (Month, 1), Quarterly (Month, 3), Yearly (Year, 1).
   :module: subscription
   :notes: English UI, light theme, 1440px width, crop to the list.

Coupons
=======

A **coupon** is a promotional code applied to every recurring invoice of the contract it is set on.
Go to :menuselection:`Subscriptions app --> Configuration --> Coupons`.

- :guilabel:`Description` and :guilabel:`Code`: the customer-facing redemption code is
  case-sensitive.
- :guilabel:`Discount Type`: :guilabel:`Percentage` or :guilabel:`Fixed amount`.
- :guilabel:`Discount Value`: the percentage (0–100), or the amount in the coupon's
  :guilabel:`Currency`.
- :guilabel:`Valid From` / :guilabel:`Valid To`: the validity window.
- :guilabel:`Max Uses`: `0` means unlimited. :guilabel:`Used` counts the redemptions.

.. screenshot:: sales-subscriptions-coupon-form
   :menu: Subscriptions ‣ Configuration ‣ Coupons ‣ (a coupon)
   :shows: A coupon form with the Code, the Discount group (type and value) and the Validity group (valid from/to, max uses, used count).
   :highlight: The Discount group (red frame).
   :data: Coupon "WELCOME10", percentage 10, valid for the current year, max uses 100.
   :module: subscription
   :notes: English UI, light theme, 1440px width, full form.

Quantity formulas
=================

A **quantity formula** computes the billable quantity of a subscription line whose
:guilabel:`Quantity Source` is :guilabel:`Formula`. Go to :menuselection:`Subscriptions app -->
Configuration --> Quantity Formulas`.

- :guilabel:`Name` and :guilabel:`Code`: the short internal identifier, for example `users_active`.
- :guilabel:`Formula`: a Python expression evaluated in a sandbox, which must assign a number to
  `result`.
- :guilabel:`Last Evaluated At`, :guilabel:`Last Result` and :guilabel:`Last Error` show the outcome
  of the latest evaluation. Formulas with an error are highlighted in the list.

.. important::
   Writing formulas requires knowledge of the data model, and a wrong formula changes what customers
   are invoiced. Reserve it for administrators, and check :guilabel:`Last Result` after every
   change.

.. screenshot:: sales-subscriptions-formula-form
   :menu: Subscriptions ‣ Configuration ‣ Quantity Formulas ‣ (a formula)
   :shows: A quantity formula form with the Name and Code fields, the Formula code area and the Last Evaluation group (last evaluated at, last result, last error).
   :highlight: The Last Evaluation group (red frame).
   :data: Formula "Active users" with code "users_active" and a last result of 12.
   :module: subscription
   :notes: English UI, light theme, 1440px width, full form.

Scheduled actions
=================

Three scheduled actions drive the application. All of them are delivered **inactive** and are
enabled in :menuselection:`Settings --> Technical --> Automation --> Scheduled Actions`:

.. list-table::
   :header-rows: 1
   :widths: 45 15 40

   * - Scheduled action
     - Interval
     - Purpose
   * - :guilabel:`Subscription: Generate Recurring Invoices`
     - 1 day
     - Creates the :doc:`recurring invoices <billing>`.
   * - :guilabel:`Subscription: Dunning Retry`
     - 4 hours
     - Re-attempts :doc:`declined charges <automatic_payments>`.
   * - :guilabel:`Subscription: Emit Alerts`
     - 1 day
     - Raises activities for ending trials and hard declines.

.. seealso::
   - :doc:`lines`
   - :doc:`billing`

==============================
Automatic payments and dunning
==============================

A contract can charge its recurring invoices automatically against a stored payment method, and
retry on a fixed schedule when a charge is declined.

Setting up automatic charging
=============================

#. Configure and enable a payment provider that supports saving payment methods
   (:doc:`../../finance/payment_providers`).
#. Let the customer save a payment method — a card or a SEPA mandate — for example from the
   :doc:`customer portal <portal>`.
#. Open the contract and select that method in the :guilabel:`Payment Token` field. Only tokens
   belonging to the contract's customer are offered.
#. Set :guilabel:`Invoice Posting` to :guilabel:`Post automatically`.

From then on, every recurring invoice generated for that contract is posted and charged
off-session.

.. important::
   A charge is only treated as successful when the payment transaction actually reports
   :guilabel:`Authorized` or :guilabel:`Done`. A provider that declines an off-session payment does
   not raise an error, so the absence of an error is never taken as a payment.

Dunning
=======

Every charge attempt is recorded as a **dunning attempt** on the contract's :guilabel:`Dunning
Attempts` tab, with its attempt number, timestamp, state, decline code and reason.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Attempt state
     - Meaning
   * - :guilabel:`Pending`
     - The charge is under way, or the provider has not answered yet.
   * - :guilabel:`Success`
     - The invoice was paid.
   * - :guilabel:`Soft Decline (retry)`
     - The charge failed and a retry is scheduled at :guilabel:`Next Retry At`.
   * - :guilabel:`Hard Decline (stop)`
     - No further retry is made.

The retry cadence is fixed: after the first failure the charge is retried after **1, 3, 7 and 14
days**. When those four retries are exhausted, the attempt becomes a :guilabel:`Hard Decline`.

The contract's :guilabel:`Dunning State` summarises where it stands: :guilabel:`OK`,
:guilabel:`Retry pending` or :guilabel:`Hard decline`. The :guilabel:`Payment Issue` filter on the
contract list finds the contracts that need attention.

.. screenshot:: sales-subscriptions-dunning-attempts
   :menu: Subscriptions ‣ Contracts ‣ (a contract) ‣ Dunning Attempts
   :shows: The Dunning Attempts tab of a contract with three attempts: attempt number, attempted-at timestamp, state badge, decline reason and next retry date.
   :highlight: The state badges and the Next Retry At column (red frame).
   :data: Contract SUB/2026/0012; one success, one soft decline with a retry scheduled.
   :module: subscription
   :notes: English UI, light theme, 1440px width, crop to the notebook. Use throw-away payment data.

Scheduled actions
=================

Two scheduled actions support automatic payments. Both are delivered inactive and must be enabled
in :menuselection:`Settings --> Technical --> Automation --> Scheduled Actions`:

- :guilabel:`Subscription: Dunning Retry` — every 4 hours; re-attempts the charges whose retry date
  has passed.
- :guilabel:`Subscription: Emit Alerts` — daily; raises a to-do activity for the salesperson when a
  trial ends within three days, and a high-priority activity for the accountant on a hard decline.

.. seealso::
   - :doc:`billing`
   - :doc:`../../finance/payment_providers`

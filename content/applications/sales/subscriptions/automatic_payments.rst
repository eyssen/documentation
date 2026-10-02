==============================
Automatic payments and dunning
==============================

A contract can charge its recurring invoices automatically against a stored payment method, and
retry on a fixed schedule when a charge is declined. It can also be collected by :ref:`SEPA direct
debit through your bank <sales/subscriptions/sepa-direct-debit>`.

Setting up automatic charging
=============================

#. Configure and enable a payment provider that supports saving payment methods
   (:doc:`../../finance/payment_providers`).
#. Let the customer save a payment method — a card or a SEPA mandate held by the provider — for
   example from the :doc:`customer portal <portal>`.
#. Open the contract and select that method in the :guilabel:`Payment Token` field. Only tokens
   belonging to the contract's customer are offered.
#. Set :guilabel:`Invoice Posting` to :guilabel:`Post automatically`.

From then on, every recurring invoice generated for that contract is posted and charged
off-session.

.. important::
   A charge is only treated as successful when the payment transaction actually reports
   :guilabel:`Authorized` or :guilabel:`Done`. A provider that declines an off-session payment does
   not raise an error, so the absence of an error is never taken as a payment.

.. _sales/subscriptions/dunning:

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
     - The charge is under way, or the provider has not answered yet. For a contract collected by
       :ref:`SEPA direct debit <sales/subscriptions/sepa-direct-debit>`, the invoice is waiting for
       a remittance, or for the bank statement to be reconciled.
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

.. _sales/subscriptions/sepa-direct-debit:

Collecting by SEPA direct debit
===============================

A contract can also be collected by **SEPA direct debit through your bank**, without card or online
payment provider. The recurring invoices are gathered in collection remittances (:doc:`debit orders
<../../finance/accounting/payments/payment_orders>`), you upload the file to your bank, and the
invoice is settled when the debit shows up on the bank statement. It is the usual way to collect
subscriptions of Spanish customers.

.. note::
   The feature is provided by the *Subscriptions - SEPA Direct Debit* module, installed
   automatically when the *Subscriptions*, *Account Banking SEPA Direct Debit* and *Account Payment
   Order Return* modules are installed.

Set up the contract
-------------------

#. The customer needs a **valid** :ref:`SEPA mandate <accounting/payment-orders/mandates>`. The
   customer can sign it :doc:`online <../../finance/accounting/payments/sepa_mandate_signature>`.
#. Create a :doc:`contract <contracts>` for the customer. The first valid mandate of the customer is
   proposed in :guilabel:`SEPA Mandate`, and, if the customer's payment mode uses :guilabel:`SEPA
   Direct Debit for customers`, it is proposed in :guilabel:`Direct Debit Payment Mode`.
#. Check both fields. The payment mode must be a direct debit mode of the contract's company, and
   the mandate a valid mandate of the customer (or of one of its contacts). You need both or none:
   saving only one stops with *SEPA direct debit needs both a direct debit payment mode and a
   mandate*.
#. Set :guilabel:`Invoice Posting` as usual.

When a mandate is selected, the :guilabel:`Payment Token` field is hidden: the card path is not used
for this contract. The invoices generated for the contract carry the payment mode and the mandate.

.. screenshot:: sales-subscriptions-sepa-contract
   :menu: Subscriptions ‣ Contracts ‣ (a contract)
   :shows: The Payment group of a contract with the Direct Debit Payment Mode "Collection remittance (SEPA) - CaixaBank" and the SEPA Mandate reference filled in, and no Payment Token field.
   :highlight: The Direct Debit Payment Mode and SEPA Mandate fields (red frame).
   :data: Contract SUB/2026/0012 for a customer with a valid SEPA mandate.
   :module: subscription_sepa_direct_debit
   :notes: English UI, light theme, 1440px width, crop to the Payment group.

Remittance settings
-------------------

Go to :menuselection:`Accounting --> Configuration --> Settings` and scroll to the
:guilabel:`SEPA/PAIN` section, :guilabel:`Subscription remittances`:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Setting
     - Description
   * - :guilabel:`Remittance Days`
     - Days of the month, separated by commas (for example ``1,15``), on which the invoices to
       collect are gathered into a draft debit order. Leave it empty to add each invoice to the
       draft debit order as soon as it is posted. A day that does not exist in a month (29 to 31) is
       skipped that month.
   * - :guilabel:`Collect Invoices Due Within (Days)`
     - Only the invoices due up to this number of days after the remittance day (7 by default) are
       collected.
   * - :guilabel:`Generate the Remittance File`
     - Also confirm the draft debit order and generate its file. The file still has to be uploaded
       to the bank by hand.
   * - :guilabel:`Remittance Responsible`
     - The user who receives the to-do *Subscription remittance ready: upload it to the bank*.

How an invoice is collected
---------------------------

#. **The invoice is posted**, automatically or by hand (if :guilabel:`Invoice Posting` is
   :guilabel:`Leave as draft for review`, the invoice enters the collection when you post it). A
   dunning attempt in the state :guilabel:`Pending` is created and the invoice waits for the
   remittance.
#. **The invoice goes into a debit order.** Without remittance days, it is added at once to the
   draft debit order of the payment mode (a new one is created when none is open). With remittance
   days, the daily scheduled action gathers, on those days, the posted invoices whose last attempt
   is pending, that are not in an active order yet and are due within the lead time, into draft
   debit orders. A note is posted on the order, and the responsible user gets the to-do.
#. **You upload the file.** Open the debit order, confirm it and generate the file (unless
   :guilabel:`Generate the Remittance File` did it), upload the file to your bank and click
   :guilabel:`File Successfully Uploaded`. The invoices are :guilabel:`In Payment`.
#. **The attempt succeeds when the invoice is paid.** After you import and reconcile the bank
   statement, the scheduled action sets the attempt to :guilabel:`Success` and the contract's
   :guilabel:`Dunning State` back to :guilabel:`OK`. Uploading the file is not enough: the attempt
   stays :guilabel:`Pending` until the debit is reconciled.

.. important::
   The scheduled action *Subscription: SEPA Direct Debit Remittance* is delivered inactive. Enable
   it in every case, even without remittance days: it also settles the attempts of the paid
   invoices.

When the bank returns a debit
-----------------------------

Confirm the :ref:`payment return <accounting/payment-orders/returns>` (typed or imported from the
report of the bank): the return reason is recorded as the decline code of the attempt of each
invoice of a SEPA contract, and the dunning applies:

- **soft return** (for example AM04, insufficient funds): the attempt becomes :guilabel:`Soft
  Decline (retry)`, and the invoice is collected again after 1, 3, 7 and 14 days as
  :ref:`described above <sales/subscriptions/dunning>`: the scheduled action *Subscription: Dunning
  Retry* creates a new attempt, and the invoice goes into a new debit order, at once or on the next
  remittance day. After the fourth retry the attempt becomes a :guilabel:`Hard Decline`;
- **hard return** (for example MD01, no mandate, AC04, closed account, or MD06, refund requested by
  the customer): the retries stop at once. The attempt becomes :guilabel:`Hard Decline (stop)`, the
  contract's :guilabel:`Dunning State` becomes :guilabel:`Hard decline` and the accountant gets the
  high-priority alert. Review the mandate with the customer before you collect again.

Whether a return is soft or hard is read from the :guilabel:`Return Type` of the return reason when
it is set (the Spanish localization sets it, see
:doc:`../../finance/accounting/payments/spanish_remittances`). Otherwise, these codes are treated as
hard: AC01, AC04, AC06, AC13, AG01, AG02, AM05, BE05, CNOR, CUST, DNOR, DUPL, FF01, MD01, MD02,
MD06, MD07, MS02, RC01, RR01, RR02, RR03, RR04 and SL01. Any other code, or a return without reason,
is soft.

Scheduled actions
=================

Three scheduled actions support automatic payments. They are delivered inactive and must be
enabled in :menuselection:`Settings --> Technical --> Automation --> Scheduled Actions`:

- :guilabel:`Subscription: Dunning Retry` — every 4 hours; re-attempts the charges whose retry date
  has passed.
- :guilabel:`Subscription: SEPA Direct Debit Remittance` — daily; gathers the invoices collected by
  :ref:`SEPA direct debit <sales/subscriptions/sepa-direct-debit>` into debit orders and sets the
  attempts of the paid invoices to :guilabel:`Success`.
- :guilabel:`Subscription: Emit Alerts` — daily; raises a to-do activity for the salesperson when a
  trial ends within three days, and a high-priority activity for the accountant on a hard decline.

.. seealso::
   - :doc:`billing`
   - :doc:`../../finance/payment_providers`
   - :doc:`../../finance/accounting/payments/payment_orders`
   - :doc:`../../finance/accounting/payments/sepa_mandate_signature`

:show-content:

========
Payments
========

In Odoo, payments can either be automatically linked to an invoice or bill or be stand-alone records
for use at a later date:

- If a payment is **linked to an invoice or bill**, it reduces/settles the amount due on the
  invoice. Multiple payments on the same invoice are possible.

- If a payment is **not linked to an invoice or bill**, the customer has an outstanding credit with
  the company, or the company has an outstanding debit with a vendor. Those outstanding amounts
  reduce/settle unpaid invoices/bills.

.. seealso::
   - :doc:`Internal transfers <bank/internal_transfers>`
   - :doc:`bank/reconciliation`

.. _accounting/payments/payment-methods:

Payment methods
===============

Several payment methods are available in Odoo to allow different configurations for different types
of payments. Examples of payment methods include manual payments (such as cash), :doc:`checks
<payments/pay_checks>`, and :doc:`online payment providers <payments/online>`. Payment methods can be
configured in the :guilabel:`Incoming Payments` and :guilabel:`Outgoing Payments` tabs of a bank or
cash journal.

.. seealso::
   :doc:`../../sales/point_of_sale/payment_methods` for Point of Sale

.. _accounting/payments/preferred-payment-methods:

Preferred payment method
------------------------

A contact's preferred payment method can be set so that when a payment is created for that contact,
the payment method is automatically selected by default. Invoices and bills can be filtered by
:guilabel:`Payment Method` to simplify :ref:`group <accounting/payments/group-payments>` payments.

To set a preferred :guilabel:`Payment Method` for a customer or a vendor, go to
:menuselection:`Accounting --> Customers --> Customers` or :menuselection:`Accounting --> Vendors
--> Vendors` and select the customer or vendor. In the :guilabel:`Sales & Purchase` tab of the
contact form, select the preferred :guilabel:`Payment Method` in the :guilabel:`Sales` section for
invoice payments or for vendor bill payments in the :guilabel:`Purchase` section.

.. tip::
   Access a full list of all contacts from the :guilabel:`Customers` or :guilabel:`Vendors` list
   view by removing the :guilabel:`Customers` or :guilabel:`Vendors` filter. Alternatively, access
   the full contact list through the Contacts app.

.. _accounting/payments/checks:

Checks
------

:doc:`Vendor bills can be paid by check <payments/pay_checks>` using a dedicated outgoing payment
method, which allows check numbers to be tracked and checks to be printed directly from Odoo.

For incoming customer check payments, you can use the default :guilabel:`Manual Payment` payment
method, or you can create a payment method specifically for checks to help identify such payments
quickly. To create a *Check* payment method, follow these steps:

#. Go to :menuselection:`Accounting --> Configuration --> Journals` and select the :guilabel:`Bank`
   journal.
#. In the :guilabel:`Incoming Payments` tab, click :guilabel:`Add a line`.
#. As :guilabel:`Payment Method`, select :guilabel:`Manual`, then enter `Check` as the
   :guilabel:`Name`.

When registering a customer payment :ref:`on an invoice <accounting/payments/from-invoice-bill>` or
:ref:`not related to an invoice <accounting/payments/not-tied>`, use the new :guilabel:`Check`
payment method.

.. note::
   Registering a customer payment by check in Odoo does not move funds. Checks must be deposited in
   order to make the payment. Once deposited to your bank, the check should appear as a :doc:`bank
   transaction <bank/transactions>`, at which point it can be :doc:`reconciled
   <bank/reconciliation>` with the registered payment.

.. tip::
   For best practice, enter the check number as the :guilabel:`Memo` when registering a customer
   payment by check.

.. _accounting/payments/from-invoice-bill:

.. _finance/accounting/register-payment-invoice-bill:

Registering payment from an invoice or bill
===========================================

To register a payment for an invoice or a bill, follow these steps:

#. Click :guilabel:`Pay` on a customer invoice or vendor bill. In the :guilabel:`Pay` window, select
   the :guilabel:`Journal` and the :guilabel:`Payment Date`.
#. If previously set, the contact's preferred :guilabel:`Payment Method` is automatically selected
   by default but can be updated if necessary.
#. If using :doc:`payment terms <customer_invoices/payment_terms>`, the :guilabel:`Amount` is
   automatically set based on the installment amounts defined by the payment term. To pay the full
   amount instead, click :guilabel:`full amount` in the message below the amount.
#. If necessary, edit the :guilabel:`Memo`.
#. Click :guilabel:`Create Payment`.

After the payment is registered, the customer invoice or vendor bill is marked as
:guilabel:`In payment`.

.. tabs::

   .. group-tab:: Without outstanding accounts

      If no :ref:`outstanding accounts <accounting/journals/outstanding-accounts>` are configured,
      no journal entry is created. To display more information about the payment, click the
      :guilabel:`Payments` smart button.

      When the invoice or vendor bill is :doc:`reconciled <bank/reconciliation>` with a bank
      transaction, its status is updated to :guilabel:`Paid`.

      .. note::
         - If a bank transaction is reconciled in a different currency, a journal entry is
           automatically created to post the currency exchange gains/loss amount.
         - When a bank transaction is reconciled with an invoice with cash-basis, a journal entry is
           automatically created to post the cash-basis tax amount.

   .. group-tab:: Using outstanding accounts

      By default, payments in Odoo do not create journal entries, but they can easily be configured
      to create journal entries using :ref:`outstanding accounts
      <accounting/journals/outstanding-accounts>`.

      Registering a payment on a customer invoice or vendor bill generates a new journal entry and
      reduces the :guilabel:`Amount Due` based on the payment amount. The counterpart is
      reflected in an :ref:`outstanding <accounting/journals/outstanding-accounts>` **receipts** or
      **payments** account. At this point, the customer invoice or vendor bill is marked as
      :guilabel:`In payment`. Then, when the payment is :doc:`reconciled <bank/reconciliation>` with
      a bank transaction, the invoice or vendor bill status changes to :guilabel:`Paid`.

      The :icon:`fa-info-circle` information icon next to the payment line displays more
      information about the payment. To access additional information, such as the related journal,
      click :guilabel:`View`.

      .. screenshot:: accounting-payments-information-icon
         :menu: Accounting ‣ Customers ‣ Invoices ‣ (open a paid invoice)
         :shows: Totals block with the payment line ("Paid on …") and the opened information popover showing the payment details and the "View" button.
         :highlight: The information icon and the popover (red frame).
         :data: Demo invoice with a registered payment; outstanding accounts configured.
         :module: account
         :notes: English UI, light theme, crop to the totals block.

      .. note::
         - Unreconciling a payment unlinks it from the invoice or bill but does not delete the
           payment.
         - If a payment is (un)reconciled in a different currency, a journal entry is automatically
           created to post the currency exchange gains/losses (reversal) amount.
         - If a payment is (un)reconciled on an invoice with cash-basis taxes, a journal entry is
           automatically created to post the cash-basis tax (reversal) amount.

      .. tip::
         If the main bank account is set as the outstanding account on the bank journal's payment
         method, registering the full payment on an invoice or bill moves the invoice/bill directly
         to the :guilabel:`Paid` status without requiring bank reconciliation.

.. _accounting/payments/not-tied:

Registering payments not tied to an invoice or bill
===================================================

When a new payment is registered via :menuselection:`Customers / Vendors --> Payments`, it is not
directly linked to an invoice or bill.

.. tabs::

   .. group-tab:: Without outstanding accounts

      Payments that are not linked to an invoice or bill should not be registered without using
      :ref:`outstanding accounts <accounting/journals/outstanding-accounts>`, as there is no way to
      associate the payment with the invoice or bill since no journal entry is created for the
      payment. The amount paid or received is not reflected in the accounting and the
      :guilabel:`Amount Due` is not updated based on the payment amount.

   .. group-tab:: Using outstanding accounts

      Instead, the payment's journal entry matches the :guilabel:`outstanding account` with the
      account receivable or the account payable until the payment is manually matched with its
      related invoice or bill. Then, :doc:`reconciling <bank/reconciliation>` the payment with the
      bank transaction completes the payment workflow.

.. _accounting/payments/payments-matching:

Payments matching
-----------------

.. note::
   During the :doc:`bank reconciliation <bank/reconciliation>` process, a remaining balance is
   identified if the total debits and credits do not match when records are compared with bank
   transactions. This balance must either be reconciled later or written off immediately.

.. _accounting/payments/matching-invoices-bills:

For a single invoice or bill
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. group-tab:: Without outstanding accounts

      By default, payments in Odoo do not create journal entries. As a result, there is no payment
      to match.

   .. group-tab:: Using outstanding accounts

      A blue banner appears when validating a new invoice/bill and an **outstanding payment** exists
      for this specific customer or vendor. To match it with the invoice or bill, click
      :guilabel:`Add` under :guilabel:`Outstanding Credits` or :guilabel:`Outstanding Debits`.

      .. screenshot:: accounting-payments-outstanding-add
         :menu: Accounting ‣ Customers ‣ Invoices ‣ (open a posted invoice)
         :shows: Totals block of a posted invoice with the "Outstanding Credits" section listing a customer payment and its "Add" button.
         :highlight: The "Add" button (red frame).
         :data: Demo customer with a registered payment not yet linked to the invoice; outstanding accounts configured.
         :module: account
         :notes: English UI, light theme, crop to the totals block.

      The invoice or bill is then marked as :guilabel:`In payment` until the payment is
      :doc:`reconciled <bank/reconciliation>` with its corresponding :doc:`bank transaction(s)
      <bank/transactions>`.

.. _accounting/payments/auto-reconcile-tool:

.. _accounting/payments/matching:

For multiple invoices or bills
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :guilabel:`Reconcile` tool (provided by the *Account Reconcile Oca* module) allows reconciling
journal items with each other (i.e., payments with customer invoices or vendor bills, or
miscellaneous journal items), account by account and partner by partner. To open it:

- go to :menuselection:`Accounting --> Accounting --> Reconcile`: each card groups the unreconciled
  journal items of an account (and partner);
- click :guilabel:`Reconcile` on an account line of the :doc:`chart of accounts
  <get_started/chart_of_accounts>` (for accounts that allow reconciliation), or use the
  :guilabel:`Reconcile` action of a contact form;
- or select journal items of the same account in :menuselection:`Accounting --> Accounting -->
  Journal Items` and click :menuselection:`Actions --> Reconcile`.

In the reconciliation view, select the journal items to match. When the selected debits and
credits are balanced, click :guilabel:`Reconcile`. Use :guilabel:`Clean` to clear the selection.
If a difference remains, it can be kept open or written off to another account before reconciling.

.. screenshot:: accounting-payments-reconcile-tool
   :menu: Accounting ‣ Accounting ‣ Reconcile ‣ (open a partner card)
   :shows: Reconciliation view of the receivable account of a customer: the unreconciled invoices and payments on the left, the selected items and the balance on the right, with the "Reconcile" and "Clean" buttons.
   :highlight: The "Reconcile" button (red frame).
   :data: Demo customer with two open invoices and one payment covering both.
   :module: account_reconcile_oca
   :notes: English UI, light theme, 1440px width.

.. note::
   Only journal items of the same account can be reconciled together.

.. _accounting/payments/group-payments:

Registering payments on multiple invoices/credit notes or bills/refunds (group payments)
========================================================================================

To register payments on multiple invoices/credit notes or bills/refunds, follow these steps:

#. Go to :menuselection:`Accounting --> Customers --> Invoices/Credit Notes` or
   :menuselection:`Accounting --> Vendors --> Bills/Refunds`.
#. In the list view, click into the search bar, group by :guilabel:`Payment Method`, select the
   relevant invoices/credit notes or bills/refunds and click :guilabel:`Pay`.
#. In the :guilabel:`Pay` window, select the :guilabel:`Journal` and the :guilabel:`Payment Date`.
#. If previously set, the contact's preferred :guilabel:`Payment Method` is automatically selected
   by default but can be updated if necessary.
#. If using :doc:`payment terms <customer_invoices/payment_terms>`, the :guilabel:`Amount` is
   automatically set based on the installment amounts defined by the payment term. To pay the full
   amount instead, click :guilabel:`full amount`.
#. To combine all payments from the same contact into a single payment, enable the :guilabel:`Group
   Payments` option, or leave it unchecked to create separate payments.
#. Click :guilabel:`Create payment`.

.. tabs::

   .. group-tab:: Without outstanding accounts

      The invoices or bills are then marked as :guilabel:`In payment` until they are
      :doc:`reconciled <bank/reconciliation>` with the bank transactions.

   .. group-tab:: Using outstanding accounts

      The invoices or bills are then marked as :guilabel:`In payment` until the bank transactions
      are :doc:`reconciled <bank/reconciliation>` with the payments.

.. _accounting/payments/partial-payment:

Registering a partial payment
=============================

To register a partial payment, click on :guilabel:`Pay` from the related invoice or bill.

.. tabs::

   .. group-tab:: Without outstanding accounts

      In the case of a partial payment (when the :guilabel:`Amount` paid is less than the total
      remaining amount on the invoice or the bill), fill in the :guilabel:`Amount` in the
      :guilabel:`Pay` window.

   .. group-tab:: Using outstanding accounts

      In the case of a partial payment (when the :guilabel:`Amount` paid is less than the total
      remaining amount on the invoice or the bill), the :guilabel:`Payment Difference` field
      displays the outstanding balance. There are two options:

      - :guilabel:`Keep open`: Keep the invoice or the bill open and mark it with a
        :guilabel:`Partial` banner;
      - :guilabel:`Mark as fully paid`: Select an account in the :guilabel:`Post Difference In`
        field and change the :guilabel:`Label` if needed. A journal entry will be created to balance
        the accounts payable or receivable with the selected account.

      .. screenshot:: accounting-payments-partial-payment
         :menu: Accounting ‣ Customers ‣ Invoices ‣ (open a posted invoice) ‣ Pay
         :shows: "Pay" dialog with an amount lower than the amount due, the "Payment Difference" and the "Keep open" / "Mark as fully paid" options; "Mark as fully paid" selected with the "Post Difference In" account and "Label" fields.
         :highlight: The payment difference options (red frame).
         :data: Invoice of 1,000 paid 990.
         :module: account
         :notes: English UI, light theme, crop to the dialog.

.. _accounting/payments/reconciling-payments:

Reconciling payments with bank transactions
===========================================

.. tabs::

   .. group-tab:: Without outstanding accounts

      Once a payment has been registered, the status of the invoice or bill is :guilabel:`In
      payment`. The next step is :doc:`reconciling <bank/reconciliation>` the related :doc:`bank
      transaction <bank/transactions>` line with the invoice or bill to finalize the payment
      workflow and mark the invoice or bill as :guilabel:`Paid`.

   .. group-tab:: Using outstanding accounts

      Once a payment has been registered, the status of the invoice or bill is :guilabel:`In
      payment`. The next step is :doc:`reconciling <bank/reconciliation>` the payment with the
      related :doc:`bank transaction <bank/transactions>` line to finalize the payment workflow and
      mark the invoice or bill as :guilabel:`Paid`.

.. _accounting/payments/recurring:

Recurring payments
==================

The *Odoo 18 Recurring Payment* (`om_recurring_payments`) module creates payments at regular
intervals, e.g., for rents or subscriptions paid by bank transfer.

#. Go to :menuselection:`Accounting --> Configuration --> Recurring Payment --> Recurring Template`
   and create a template: enter a :guilabel:`Name`, the :guilabel:`Journal`, the recurring period
   (days, weeks, months, or years) and :guilabel:`Recurring Interval`, and whether the payments are
   generated as :guilabel:`Un Posted` or :guilabel:`Posted` (:guilabel:`Generate Journal As`).
   Click :guilabel:`Done` to activate the template.
#. Go to :menuselection:`Accounting --> Configuration --> Recurring Payment --> Recurring Payment`
   and create a recurring payment: select the :guilabel:`Recurring Template`, the
   :guilabel:`Partner`, the :guilabel:`Payment Type` (:guilabel:`Send Money` or :guilabel:`Receive
   Money`), the :guilabel:`Amount`, and the :guilabel:`Start Date` and :guilabel:`End Date`.
#. Click :guilabel:`Done`. The planned payments are listed in the :guilabel:`Recurring Entries` tab.

A scheduled action creates the payments of the lines whose date has passed. A payment can also be
created manually with the :guilabel:`Create Payment` button of a line. To modify the recurring
payment, click :guilabel:`Set To Draft` (only possible if no payment has been created yet).

.. screenshot:: accounting-payments-recurring-payment
   :menu: Accounting ‣ Configuration ‣ Recurring Payment ‣ Recurring Payment ‣ (open a record)
   :shows: Recurring payment form in "Done" status: template, partner, payment type "Send Money", amount, journal, date range, period and interval; "Recurring Entries" tab with monthly lines and their status and "Create Payment" buttons.
   :highlight: The "Recurring Entries" tab (red frame).
   :data: Monthly office rent of 350,000 HUF for 12 months.
   :module: om_recurring_payments
   :notes: English UI, light theme, 1440px width.

.. toctree::
   :titlesonly:

   payments/online
   payments/follow_up
   payments/pay_checks
   payments/forecast
   payments/trusted_accounts

=================================
Payment orders and SEPA transfers
=================================

Payment orders group the vendor bills to pay into one bank file, and debit orders group the
customer invoices to collect by direct debit. The file is generated in the SEPA XML format
(*PAIN*) accepted by the banks of the SEPA area:

- **payment orders** (SEPA Credit Transfer) pay vendors from your bank account;
- **debit orders** (SEPA Direct Debit) collect customer invoices from your customers' bank accounts,
  based on the direct debit **mandates** signed by the customers.

.. note::
   The features are provided by the *Account Payment Order*, *Account Payment Mode*, *Account
   Payment Partner*, *Account Banking Mandate*, *Account Banking SEPA Credit Transfer*, and *Account
   Banking SEPA Direct Debit* modules. :ref:`Install <general/install>` the SEPA modules you need;
   the other modules are installed with them.

.. _accounting/payment-orders/configuration:

Configuration
=============

SEPA identifiers
----------------

Go to :menuselection:`Accounting --> Configuration --> Settings`, and scroll to the
:guilabel:`SEPA/PAIN` section:

- :guilabel:`Initiating Party Identifier` and :guilabel:`Initiating Party Issuer`: the identifiers
  given by your bank for the files you send, if your bank requires them;
- :guilabel:`SEPA Creditor Identifier`: the creditor identifier of your company, required for
  direct debits. It is composed of the country code, a check number, a business code, and a
  national identifier (in Spain, based on the tax ID of the company).

If your identifiers depend on the bank (as is common in Spain), enable :guilabel:`Multiple
identifiers`: the identifiers are then entered on each payment mode.

Payment modes
-------------

A *payment mode* defines how a payment is made: the payment method (for example SEPA Credit
Transfer) and the bank journal used. Go to :menuselection:`Accounting --> Configuration -->
Management --> Payment Modes`, and click :guilabel:`New`:

#. Enter a name, for example *SEPA transfer - Bank X*.
#. Select the :guilabel:`Payment Method`: :guilabel:`SEPA Credit Transfer to suppliers` for
   payment orders, or :guilabel:`SEPA Direct Debit for customers` for debit orders.
#. In :guilabel:`Link to Bank Account`, select *Fixed* to always use the same bank journal (then
   select it), or *Variable* to choose the bank journal on each order among the allowed ones.
#. Keep :guilabel:`Selectable in Payment Orders` ticked.
#. In the :guilabel:`Options for Payment Orders` section, set the :guilabel:`Default Payment
   Execution Date` of the orders and, if needed, tick :guilabel:`Group Transactions in Payment
   Orders` to pay several invoices of the same partner with one transfer.
#. In the :guilabel:`Select Move Lines to Pay - Default Values` section, set the default filters
   used to add journal items to the orders, for example :guilabel:`Linked to an Invoice or Refund`
   and the :guilabel:`Type of Date Filter`.

.. tip::
   The PAIN version used by the SEPA files is set on the payment method, under
   :menuselection:`Accounting --> Configuration --> Management --> Payment Methods`
   (:guilabel:`PAIN Version`). Keep the recommended version unless your bank asks for another one.

.. screenshot:: accounting-payment-orders-payment-mode
   :menu: Accounting ‣ Configuration ‣ Management ‣ Payment Modes ‣ New
   :shows: A payment mode form: name "SEPA transfer - Bank X", payment method "SEPA Credit Transfer to suppliers", Link to Bank Account "Fixed" with the bank journal, "Selectable in Payment Orders" ticked, and the "Options for Payment Orders" and "Select Move Lines to Pay - Default Values" sections.
   :highlight: The "Payment Method" and "Link to Bank Account" fields.
   :data: Demo company with a bank journal having an IBAN account.
   :module: account_payment_mode, account_payment_order
   :notes: English UI, light theme, 1440px width.

Contacts and invoices
---------------------

On the contact form, in the :guilabel:`Sales & Purchase` tab, select the :guilabel:`Customer
Payment Mode` and the :guilabel:`Supplier Payment Mode`. They are proposed on the invoices and
bills of the contact, in the :guilabel:`Payment Mode` field, which can be changed on a draft
invoice. For SEPA payments and debits, the contact must also have a bank account (IBAN).

.. _accounting/payment-orders/mandates:

Direct debit mandates
=====================

A direct debit requires a mandate signed by the customer, attached to the customer's bank
account. Go to :menuselection:`Accounting --> Customers --> Banking Mandates`, and click
:guilabel:`New`:

#. Select the customer's :guilabel:`Bank Account`.
#. Select the :guilabel:`Type of Mandate`: :guilabel:`Recurrent` for regular debits, or
   :guilabel:`One-Off` for a single debit.
#. Select the :guilabel:`Scheme`: :guilabel:`Basic (CORE)` for consumers and most customers, or
   :guilabel:`Enterprise (B2B)` for business customers that agreed to this scheme with their bank.
#. Enter the :guilabel:`Date of Signature of the Mandate`, and attach the :guilabel:`Scan of the
   Mandate`.
#. Click :guilabel:`Validate`.

To get the mandate signed, click :guilabel:`Print` to print the mandate form, or :guilabel:`Send by
Email` to send it to the customer.

The :guilabel:`Sequence Type for Next Debit` of a recurrent mandate is managed automatically: it
switches from :guilabel:`First` to :guilabel:`Recurring` after the first debit order is sent. A
mandate that has not been used for a long time is set to :guilabel:`Expired`.

.. _accounting/payment-orders/pay:

Pay vendors with a payment order
================================

#. Go to :menuselection:`Accounting --> Vendors --> Payment Orders`, and click :guilabel:`New`.
#. Select the :guilabel:`Payment Mode` (and the bank journal if the mode is variable).
#. Click :guilabel:`Create Payment Lines from Journal Items`, check the filters, then click
   :guilabel:`Add All Move Lines` to add all the matching open bills, or add them one by one.
#. Check the :guilabel:`Transactions` tab, then click :guilabel:`Confirm Payments`.
#. Click :guilabel:`Generate Payment File`. The SEPA XML file is attached to the order; download
   it and upload it in your online banking.
#. Once the bank has accepted the file, click :guilabel:`File Successfully Uploaded`. The payments
   are posted and reconciled with the bills.

.. tip::
   Bills can also be added from the list of vendor bills: select them, then click
   :menuselection:`Actions --> Add to Payment Order`. The lines are added to the draft payment
   order of the payment mode, or a new order is created.

.. screenshot:: accounting-payment-orders-order
   :menu: Accounting ‣ Vendors ‣ Payment Orders ‣ (a confirmed order)
   :shows: A confirmed payment order with the payment mode, bank journal, execution date, the "Transactions" tab listing three vendor bills with partner, IBAN and amount, and the "Generate Payment File" button in the header; statusbar Draft / Confirmed / File Generated / File Uploaded.
   :highlight: The "Generate Payment File" button.
   :data: Three open vendor bills of SEPA vendors with IBAN accounts.
   :module: account_payment_order, account_banking_sepa_credit_transfer
   :notes: English UI, light theme, 1440px width.

.. _accounting/payment-orders/debit:

Collect customer invoices with a debit order
============================================

The steps are the same as for payment orders, from :menuselection:`Accounting --> Customers -->
Debit Orders`, with a payment mode using :guilabel:`SEPA Direct Debit for customers`. Every
customer of the order must have a valid mandate on the bank account used; the mandate is proposed
automatically on the lines. Customer invoices can also be added with :menuselection:`Actions -->
Add to Debit Order`.

.. _accounting/payment-orders/returns:

Payment returns
===============

When a customer's bank returns a direct debit (for example, insufficient funds or a mandate
revoked by the customer), record the return so that the invoice is open again:

#. Go to :menuselection:`Accounting --> Customers --> Customer Payment Returns`, and click
   :guilabel:`New`.
#. Select the bank journal and the date of the return.
#. In the :guilabel:`Lines` tab, add a line per returned payment: select the returned payment
   (journal item), the :guilabel:`Amount`, and the :guilabel:`Return reason`. Bank charges can be
   recorded on the line as well. Alternatively, enter the references and click :guilabel:`Match`
   to find the payments.
#. Click :guilabel:`Confirm`. A journal entry removes the amount from the bank account, and the
   invoice is open again.

To debit the invoice again in a later debit order, tick :guilabel:`Include move lines from
returns` when adding the journal items to the order.

.. seealso::
   - :doc:`../payments`
   - :doc:`../bank/statement_import`

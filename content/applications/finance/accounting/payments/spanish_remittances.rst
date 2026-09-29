===================
Spanish remittances
===================

In Spain, companies collect and pay in **remittances** (*remesas*): one file per bank, with the
direct debits to collect from customers, the transfers to pay to vendors, the *confirming* of the
bank, or the issued promissory notes (*pagarés*). The *Spain - Payment Orders (remittances)* module
prepares all of this for every bank journal of a Spanish company, on top of the
:doc:`payment orders <payment_orders>`, so that an accountant does not have to build the payment
modes, the accounts and the return rules by hand.

.. note::
   The module is installed automatically when the Spanish fiscal localization and the *Account
   Payment Order* module are both installed. It needs the SEPA direct debit and credit transfer
   modules, which it installs as well.

.. _accounting/payment-orders/spain:

Remittance payment modes per bank
=================================

For a bank journal, the module creates the :ref:`payment modes
<accounting/payment-orders/configuration>` of the remittances you use. Each mode is *fixed* on the
bank journal and named after the bank, which is recognised from the entity code of the Spanish IBAN
of the journal (CaixaBank, Banco Santander, BBVA and Banco Sabadell are known; for another bank, the
name of the bank of the account or the name of the journal is used).

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Payment mode
     - Payment method
     - Notes
   * - :guilabel:`Collection remittance (SEPA) - <bank>`
     - :guilabel:`SEPA Direct Debit for customers`
     - Used on :guilabel:`Debit Orders`. The :guilabel:`Default Charges Account` of the bank
       journal is set to the account 626 (see :ref:`returns
       <accounting/payment-orders/spain-returns>`).
   * - :guilabel:`Payment remittance (SEPA) - <bank>`
     - :guilabel:`SEPA Credit Transfer to suppliers`
     - Used on :guilabel:`Payment Orders`.
   * - :guilabel:`Confirming - <bank>`
     - :guilabel:`Confirming AEF` (CaixaBank, Banco Santander) or :guilabel:`Confirming Sabadell`
       (Banco Sabadell)
     - Only offered when the bank has a confirming format and its module is installed. The
       account 400100 *Suppliers, confirming* is created if it does not exist.
   * - :guilabel:`Promissory note (pagaré) - <bank>`
     - The check payment method
     - Needs the check printing module. The notes are printed one by one, so the mode is not
       :guilabel:`Selectable in Payment Orders`. Uses the account 401 *Suppliers, trade bills
       payable*.

All the modes are created with the same defaults: the invoices of the same payment mode, linked to
an invoice or refund, posted, filtered on the due date, with :guilabel:`Group Transactions in
Payment Orders` ticked. :guilabel:`Default Batch Booking` is ticked for the SEPA modes, so that the
bank statement shows one single line for the whole file, and not ticked for the confirming and the
promissory notes. You can change everything afterwards in :menuselection:`Accounting -->
Configuration --> Management --> Payment Modes`.

Create the modes
----------------

There are two ways to create them:

- **In the Spanish company setup wizard**, in the :guilabel:`Bank` step
  (:menuselection:`Accounting --> Configuration --> Spain --> Company setup`): select the bank
  journal, then tick :guilabel:`Collection remittances (SEPA direct debit)` and
  :guilabel:`Payment remittances (SEPA credit transfer)` (both ticked by default), and
  :guilabel:`Confirming` and :guilabel:`Issued promissory notes (pagaré)` when they are offered.
  The summary of the wizard lists the payment modes created.
- **With the remittance wizard**, at any time, for example for a second bank:
  :menuselection:`Accounting --> Configuration --> Management --> Set up Spanish Remittances`.
  Select the :guilabel:`Bank Journal`, tick the remittance types and click :guilabel:`Create`. The
  list of the payment modes of the journal opens.

Running the setup again does not duplicate anything: a mode that already exists for the same
journal and payment method is kept as it is. The setup stops with an explicit message when nothing
is selected (remittance wizard), when the journal is not a bank journal, when the confirming
module of the bank is not installed, when the check printing module is missing (promissory notes),
or when no account 401 is found.

Outstanding accounts
====================

A remittance only settles the invoices if its payments have a journal entry, which requires an
:ref:`outstanding account on the payment method line
<accounting/payment-orders/outstanding-account>` of the bank journal. When the modes are created
with the setup above, the payment method line of the bank journal is added if it is missing, and
its account is set:

- for the SEPA remittances, to the outstanding receipts or payments account of the company;
- for the confirming, to the account 400100 *Suppliers, confirming*;
- for the promissory notes, to the account 401 *Suppliers, trade bills payable*.

Later, when you create or change a remittance payment mode of a Spanish company by hand, or when
the module is installed on a database that already has remittance modes, the payment method lines of
the journals that have no account receive the outstanding account of the company. A line that
already has an account is never changed.

Invoices paid by promissory note or confirming
==============================================

In Spain, a supplier invoice paid with a promissory note or through a confirming is not paid when
you issue the note or send the file: it is paid when the bank debits the amount (Código Civil,
art. 1170). The bills paid this way therefore stay :guilabel:`In Payment` until the bank debit is
matched:

#. Register the payment with the promissory note or the confirming remittance: the bill goes
   :guilabel:`In Payment`.
#. When the bank debits the amount at maturity, :doc:`import the bank statement
   <../bank/statement_import>` and reconcile the debit with the payment.
#. The bill becomes :guilabel:`Paid`.

This applies to the payments whose outstanding account is a payable or receivable account, as with
the accounts 401 and 400100 above. The SEPA remittances, which use an ordinary outstanding account,
follow the standard behaviour.

Confirming files
----------------

The AEF and Banco Sabadell confirming files are generated from a :guilabel:`Payment Order` with the
confirming payment mode (the AEF mode needs the :guilabel:`Contrato AEF Confirming` number of the
bank, the Sabadell mode the :guilabel:`Contrato BSConfirming` number). The processing date and the
date of the remittance when the execution date is :guilabel:`Immediately` are the date of the
user, not the UTC date: a file generated late in the evening in Spain carries the current day, and
not the previous one.

.. _accounting/payment-orders/spain-returns:

Returns of direct debits
========================

**Soft and hard returns.** The :ref:`payment returns <accounting/payment-orders/returns>` carry the
return reason of the bank (R-transaction codes of the AEB, *Cuaderno 19.14*). The module classifies
the codes as :guilabel:`Soft (collect again)` or :guilabel:`Hard (review the mandate)`:

- a *soft* return can be presented again, typically because of a temporary reason: AM04
  (insufficient funds), AM23 (amount exceeds the limit) and MS03 (unspecified reason, generated by
  the bank);
- a *hard* return should not be presented again before the mandate or the account has been reviewed
  with the customer, for example AC01 or AC04 (incorrect or closed account), MD01 (no mandate) or
  MD06 (refund request of the customer). All the other AEB codes are hard.

To see or change the classification, go to :menuselection:`Accounting --> Configuration -->
Management --> Return Reasons`. The list shows the :guilabel:`Return Type` and whether the code
is an :guilabel:`AEB Code`, and can be filtered on :guilabel:`Hard Returns` or :guilabel:`Soft
Returns`. A reason with another code has no type until you set one. Other features read the
classification: the :doc:`subscription dunning <../../../sales/subscriptions/automatic_payments>`
retries soft returns and stops on hard returns.

**Review the mandate.** When you confirm a return that contains a hard reason, a note is posted on
the mandate of the debit and a to-do activity, *Review the mandate after the hard return ...*, is
scheduled for today for the user who created the return. The mandate is **not** cancelled
automatically: depending on the customer, the right action is a new mandate, a new IBAN or a
cancellation. Do not include the invoice in a new debit order before you have decided.

**Charges of the return.** The bank charges of a returned debit are booked on the account 626
*Servicios bancarios y similares* by default: the module sets it as the :guilabel:`Default Charges
Account` of the bank journals of Spanish companies that have none, when it is installed and when
the collection remittances of a journal are created. See :ref:`the charges of a return
<accounting/payment-orders/returns-manual>`.

.. seealso::
   - :doc:`payment_orders`
   - :doc:`sepa_mandate_signature`
   - :doc:`../../fiscal_localizations/spain`

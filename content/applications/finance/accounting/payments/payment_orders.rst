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
   the other modules are installed with them. Payment returns come with the *Account Payment
   Return* modules. Three optional modules extend the flow: *SEPA Mandate Online Signature* (the
   customer signs the mandate online, see :doc:`sepa_mandate_signature`), *Subscriptions - SEPA
   Direct Debit* (subscription invoices are collected by direct debit, see :doc:`Automatic payments
   and dunning <../../../sales/subscriptions/automatic_payments>`), and *Spain - Payment Orders
   (remittances)*, installed automatically with the Spanish localization (see
   :doc:`spanish_remittances`).

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

.. note::
   An invalid :guilabel:`SEPA Creditor Identifier` is refused when it is saved. When the format
   requires an initiating party and none is set, the generation of the file stops with the message
   *Missing 'Initiating Party Issuer' and/or 'Initiating Party Identifier' for the company ...*. The
   online signature of mandates needs the :guilabel:`SEPA Creditor Identifier` of the *company* (see
   :doc:`sepa_mandate_signature`).

Payment modes
-------------

A *payment mode* defines how a payment is made: the payment method (for example SEPA Credit
Transfer) and the bank journal used. Go to :menuselection:`Accounting --> Configuration -->
Management --> Payment Modes`, and click :guilabel:`New`:

#. Enter a name, for example *SEPA transfer - Bank X*.
#. Select the :guilabel:`Payment Method`: :guilabel:`SEPA Credit Transfer to suppliers` for
   payment orders, or :guilabel:`SEPA Direct Debit for customers` for debit orders.
#. In :guilabel:`Link to Bank Account`, select *Fixed* to always use the same bank journal (then
   select it in :guilabel:`Fixed Bank Journal`), or *Variable* to choose the bank journal on each
   order among the :guilabel:`Allowed Bank Journals`.
#. Keep :guilabel:`Selectable in Payment Orders` ticked. Modes without it cannot be used on
   payment or debit orders.
#. In the :guilabel:`Options for Payment Orders` section, set the :guilabel:`Default Payment
   Execution Date` of the orders (:guilabel:`Immediately`, :guilabel:`Due Date` or :guilabel:`Fixed
   Date`) and, if needed, tick :guilabel:`Group Transactions in Payment Orders` to pay several
   invoices of the same partner with one transfer. On a debit order mode, tick
   :guilabel:`Disallow Debit Before Maturity Date` to refuse orders whose debit date is earlier
   than the due date of an invoice.
#. In the :guilabel:`Select Move Lines to Pay - Default Values` section, set the default filters
   used to add journal items to the orders, for example :guilabel:`Linked to an Invoice or Refund`
   and the :guilabel:`Type of Date Filter`.

.. screenshot:: accounting-payment-orders-payment-mode
   :menu: Accounting ‣ Configuration ‣ Management ‣ Payment Modes ‣ New
   :shows: A payment mode form: name "SEPA transfer - Bank X", payment method "SEPA Credit Transfer to suppliers", Link to Bank Account "Fixed" with the bank journal, "Selectable in Payment Orders" ticked, and the "Options for Payment Orders" and "Select Move Lines to Pay - Default Values" sections.
   :highlight: The "Payment Method" and "Link to Bank Account" fields.
   :data: Demo company with a bank journal having an IBAN account.
   :module: account_payment_mode, account_payment_order
   :notes: English UI, light theme, 1440px width.

.. tip::
   The file format (PAIN version) and the postal address mode of the SEPA files are global
   settings of the database, not options of the payment mode. See :ref:`SEPA file formats
   <accounting/payment-orders/formats>` before you change them.

.. _accounting/payment-orders/outstanding-account:

Outstanding account of the payment method
-----------------------------------------

When a payment order is uploaded, Odoo registers one payment per transaction with the payment
method line of the bank journal. With the accounting app installed, a payment only gets a journal
entry if that payment method line has an outstanding account. Without it, the order would be
uploaded and the invoices would stay unpaid without any message, so eYssen stops the order
instead.

Before you use a payment mode for the first time, make sure the bank journal is ready:

#. Go to :menuselection:`Accounting --> Configuration --> Journals` and open the bank journal of
   the payment mode.
#. For a debit order, open the :guilabel:`Incoming Payments` tab; for a payment order, open the
   :guilabel:`Outgoing Payments` tab.
#. Find the line of the SEPA payment method (:guilabel:`SEPA Direct Debit for customers` or
   :guilabel:`SEPA Credit Transfer to suppliers`), or click :guilabel:`Add a line` and select it.
#. Set the :guilabel:`Outstanding Receipts accounts` (debit orders) or :guilabel:`Outstanding
   Payments accounts` (payment orders), typically the same account as the other payment method
   lines of the journal.

If the account is missing, clicking :guilabel:`Confirm Payments` fails with the message *The
payments of the payment order ... would not create any journal entry because their payment method
has no outstanding account*, followed by the journal and payment method lines to fix. The order
stays in :guilabel:`Draft`; set the account and confirm the order again. The same check is repeated
when you click :guilabel:`File Successfully Uploaded`, for orders confirmed before this check
existed.

.. note::
   In a Spanish company, the outstanding account is set for you when the payment modes are created
   with the Spanish remittance setup, and the modules fill in the missing accounts of existing
   remittance modes when they are installed. See :doc:`spanish_remittances`.

Contacts and invoices
---------------------

On the contact form, in the :guilabel:`Sales & Purchase` tab, select the :guilabel:`Customer
Payment Mode` and the :guilabel:`Supplier Payment Mode`. They are proposed on the invoices and
bills of the contact, in the :guilabel:`Payment Mode` field, which can be changed on a draft
invoice. For SEPA payments and debits, the contact must also have a bank account (IBAN).

.. _accounting/payment-orders/formats:

SEPA file formats
-----------------

The content of the SEPA XML file depends on two settings: the **format** of the file (the *PAIN*
version) and the way the **postal addresses** of the parties (your company and the customers or
vendors) are written in it. Both are global settings of the database: they apply to all the
companies and all the bank journals.

Go to :menuselection:`Accounting --> Configuration --> Settings` and scroll to the
:guilabel:`SEPA/PAIN` section. Below the identifiers, you find, depending on the installed SEPA
modules:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Setting
     - Description
   * - :guilabel:`Credit Transfer Format`
     - PAIN version of the payment order files. :guilabel:`pain.001.001.09 (recommended for credit
       transfer)` is the format of the SEPA 2025 rulebook. Older versions (pain.001.001.02, .03,
       .04, .05 and pain.001.003.03 for Germany) remain available.
   * - :guilabel:`Credit Transfer Address Mode`
     - Postal address written in pain.001.001.09 files. Only shown when the format is
       pain.001.001.09.
   * - :guilabel:`Direct Debit Format`
     - PAIN version of the debit order files. :guilabel:`pain.008.001.08 (SEPA 2025 rulebook)` is
       the format of the SEPA 2025 rulebook for direct debits. Older versions (pain.008.001.02, .03,
       .04 and pain.008.003.02 for Germany) remain available.
   * - :guilabel:`Direct Debit Address Mode`
     - Postal address written in pain.008.001.08 files. Only shown when the format is
       pain.008.001.08.

.. screenshot:: accounting-payment-orders-sepa-formats
   :menu: Accounting ‣ Configuration ‣ Settings ‣ SEPA/PAIN
   :shows: The SEPA/PAIN section of the accounting settings with the initiating party fields, the Credit Transfer Format "pain.001.001.09" with the Credit Transfer Address Mode "Structured", and the Direct Debit Format "pain.008.001.08" with the Direct Debit Address Mode "Structured".
   :highlight: The two Format settings and their Address Mode fields.
   :data: New database with the SEPA credit transfer and SEPA direct debit modules installed.
   :module: account_banking_pain_base
   :notes: English UI, light theme, 1440px width, crop to the SEPA/PAIN section.

The same fields are available on the payment method, under :menuselection:`Accounting -->
Configuration --> Management --> Payment Methods` (:guilabel:`PAIN Version` and :guilabel:`Postal
Address Mode`); the settings simply edit the standard SEPA payment methods.

Postal address mode
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Mode
     - Address written in the file
   * - :guilabel:`Minimal (City + Country only)`
     - City (``TwnNm``) and country (``Ctry``) only.
   * - :guilabel:`Hybrid (City/Country + AdrLine)`
     - City and country, plus the post code (``PstCd``) and the street lines as free-text
       ``AdrLine`` elements when they are filled in.
   * - :guilabel:`Structured (Street, Post Code, City, Province, Country)`
     - Fully structured address: street (``StrtNm``, the street and the second street line of the
       contact separated by a comma), post code (``PstCd``), city (``TwnNm``), province
       (``CtrySubDvsn``, the state of the contact) and country (``Ctry``), without free-text lines.
       Empty fields are left out.

The older PAIN versions always write an unstructured address.

.. important::
   The European Payments Council (EPC) does not allow unstructured postal addresses from
   **15 November 2026**. Use the :guilabel:`Structured` mode with the SEPA 2025 formats
   (pain.001.001.09 and pain.008.001.08) and check with your bank before you keep another mode
   after that date.

With the SEPA 2025 formats, the **city of every party is mandatory**: generating the file fails with
the message *PAIN format ... requires City (TwnNm). Partner missing City: ...* when the company or
a customer or vendor of the order has no city. Fill in the street, the post code and the province
of the contacts as well when you use the structured mode.

Defaults for new and existing databases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A **new database** creates the SEPA payment methods with the SEPA 2025 formats and the structured
address: pain.001.001.09 for credit transfers, pain.008.001.08 for direct debits.

An **existing database keeps the format it already uses** when it is upgraded, as the standard
payment methods are never overwritten. Nothing changes in the files until you change the settings
yourself.

.. _accounting/payment-orders/formats-migration:

Migrate an existing database to the SEPA 2025 formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Do it well before 15 November 2026, and outside a period where you have to send an urgent order.

#. **Ask your bank(s)** to confirm that they accept pain.001.001.09 for transfers and
   pain.008.001.08 for direct debits, and whether they want a test file first. Keep the older format
   until they have confirmed it.
#. **Complete the contacts.** Make sure your company and the customers and vendors that appear in
   orders have a city; add the street, the post code and the state for the structured address.
   Contacts without a city make the file generation fail.
#. **Send or finish the pending orders** in the old format if you prefer a clean cut: the file is
   generated when you click :guilabel:`Generate Payment File`, so an order that is still
   :guilabel:`Draft` or :guilabel:`Confirmed` when you change the settings is generated in the new
   format. A file already generated is not modified.
#. Go to :menuselection:`Accounting --> Configuration --> Settings`, :guilabel:`SEPA/PAIN` section.
   Select :guilabel:`pain.001.001.09` in :guilabel:`Credit Transfer Format` and
   :guilabel:`pain.008.001.08` in :guilabel:`Direct Debit Format`, select :guilabel:`Structured` in
   the two :guilabel:`Address Mode` fields, and click :guilabel:`Save`.
#. **Generate a first file** with a small order and upload it to the bank. Odoo validates every
   file against the official XML schema and refuses to attach an invalid one. Check that the bank
   accepts the file and that the debits or transfers are processed as expected.
#. If you import the reports of the bank, note that the new status reports (pain.002.001.10) can be
   :ref:`imported <accounting/payment-orders/returns-import>` like the previous ones.

To go back, select the previous format in the same settings; the address mode of the older
formats is ignored.

.. _accounting/payment-orders/mandates:

Direct debit mandates
=====================

A direct debit requires a mandate signed by the customer, attached to the customer's bank
account. Go to :menuselection:`Accounting --> Customers --> Banking Mandates`, and click
:guilabel:`New`:

#. Select the customer's :guilabel:`Bank Account`. The mandate reference is generated on saving.
#. Select the :guilabel:`Type`: :guilabel:`Recurrent` for regular debits, or :guilabel:`One-Off` for
   a single debit.
#. Select the :guilabel:`Scheme`: :guilabel:`Basic (CORE)` for consumers and most customers, or
   :guilabel:`Enterprise (B2B)` for business customers that agreed to this scheme with their bank.
#. Enter the :guilabel:`Date of Signature of the Mandate` (it cannot be in the future), and attach
   the :guilabel:`Scan of the Mandate`.
#. Click :guilabel:`Validate`. A mandate cannot be validated without a bank account and a date of
   signature.

To get the mandate signed, you have three options:

- click :guilabel:`Print` to print the mandate form;
- click :guilabel:`Send by Email` (on a draft mandate) to send the form to the customer;
- with the *SEPA Mandate Online Signature* module, send the customer a link to sign the mandate
  online, or let the customer sign it in the customer portal. The signed mandate is created as
  :guilabel:`Valid`, with the signed document and the evidence attached, so you do not have to
  create it by hand. See :doc:`sepa_mandate_signature`.

The mandate is then proposed on the customer's invoices, in the :guilabel:`Direct Debit Mandate`
field, when their payment mode uses :guilabel:`SEPA Direct Debit for customers`: it is the first
valid mandate of the customer for the company of the invoice.

The :guilabel:`Sequence Type for Next Debit` of a recurrent mandate is managed automatically: it
switches from :guilabel:`First` to :guilabel:`Recurring` when the first debit order is marked as
uploaded, and a note is posted on the mandate. When a debit order is uploaded, the :guilabel:`Date
of the Last Debit` of its mandates is updated and a one-off mandate (or a recurrent mandate whose
sequence type is :guilabel:`Final`) is set to :guilabel:`Expired`. A daily scheduled action, *Set
SEPA Direct Debit Mandates to Expired*, also expires a valid mandate that has not been used for 36
months (counted from the signature date if it was never used).

A debit order line whose mandate is missing, not :guilabel:`Valid`, or a used one-off mandate stops
the confirmation of the order with an explicit message. A :guilabel:`Cancelled` mandate can be
put :guilabel:`Back to Draft` if it was cancelled by mistake.

.. _accounting/payment-orders/pay:

Pay vendors with a payment order
================================

#. Go to :menuselection:`Accounting --> Vendors --> Payment Orders`, and click :guilabel:`New`.
#. Select the :guilabel:`Payment Mode` (and the bank journal if the mode is variable).
#. Click :guilabel:`Create Payment Lines from Journal Items`, check the filters, then click
   :guilabel:`Add All Move Lines` to add all the matching open bills, or add them one by one.
#. Check the :guilabel:`Transactions` tab, then click :guilabel:`Confirm Payments`. The
   transactions are checked (bank account, amounts, dates) and one payment per transaction is
   registered; if the :ref:`outstanding account <accounting/payment-orders/outstanding-account>` of
   the payment method is missing, the order is refused with an explicit message. The status is then
   :guilabel:`Confirmed`.
#. Click :guilabel:`Generate Payment File`. The SEPA XML file is attached to the order; download
   it and upload it in your online banking.
#. Once the bank has accepted the file, click :guilabel:`File Successfully Uploaded`. The payments
   are posted and reconciled with the bills. The :guilabel:`Journal Entries` and
   :guilabel:`Payments` smart buttons of the order give access to the resulting records.

.. tip::
   Bills can also be added from the list of vendor bills: select the posted bills, then click
   :menuselection:`Actions --> Add to Payment/Debit Order`, or open a posted bill and click
   :guilabel:`Add to Payment Order`. The lines are added to the draft payment order of the payment
   mode of the bill, or a new order is created. The bill needs a payment mode and cannot be in an
   active order already.

.. note::
   :guilabel:`Cancel Payments` cancels the order and its payments; after the upload, the posted
   payments are set back to draft first, so the invoices are open again. :guilabel:`Back to Draft`
   reopens a cancelled order.

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
customer of the order must have a valid :ref:`mandate <accounting/payment-orders/mandates>`; the
mandate of the invoice is proposed automatically on the lines. Customer invoices can also be added
with :menuselection:`Actions --> Add to Payment/Debit Order`, or with :guilabel:`Add to Debit Order`
on a posted invoice.

Once the file is uploaded, the invoices are :guilabel:`In Payment`; they are :guilabel:`Paid` when
the debit appears on the bank statement and is reconciled, or open again if the bank returns the
debit (see :ref:`accounting/payment-orders/returns`).

.. seealso::
   - :doc:`Collect subscription invoices by direct debit
     <../../../sales/subscriptions/automatic_payments>`: subscription invoices with a mandate are
     gathered into collection remittances automatically.
   - :doc:`spanish_remittances` for the remittances per bank of Spanish companies.

.. _accounting/payment-orders/returns:

Payment returns
===============

When a customer's bank returns a direct debit (for example, insufficient funds or a mandate
revoked by the customer), record the return so that the invoice is open again. A return can be
entered by hand or imported from the file of the bank.

.. _accounting/payment-orders/returns-manual:

Enter a return by hand
----------------------

#. Go to :menuselection:`Accounting --> Customers --> Customer Payment Returns`, and click
   :guilabel:`New`.
#. Select the :guilabel:`Bank journal` and the :guilabel:`Return date`.
#. In the :guilabel:`Lines` tab, add a line per returned payment: select the returned payment
   (:guilabel:`Payment Reference`, the journal item), the :guilabel:`Amount`, and the
   :guilabel:`Return reason`. Alternatively, enter the references and click :guilabel:`Match` to
   find the payments.
#. If the bank charged fees, fill in the :guilabel:`Charges Amount` of the line (the
   :guilabel:`Charges Account` and :guilabel:`Charges Partner` columns can be shown with the column
   selector).
#. Click :guilabel:`Confirm`. A journal entry removes the amount from the bank account, and the
   invoice is open again.

The charges of a return are booked on the :guilabel:`Charges Account` of the line, with the
:guilabel:`Charges Partner`. To avoid filling them in on every return, set a :guilabel:`Default
Charges Account` and a :guilabel:`Default Charges Partner` on the bank journal (in a Spanish
company, the account 626 is set by the localization, see :doc:`spanish_remittances`). The defaults
are proposed when you enter a charges amount on the form, and they are also applied when you click
:guilabel:`Confirm` to lines that were created without the form, for example by the import of a
file. If a line has charges but neither the line nor the journal has a charges account,
:guilabel:`Confirm` stops with the message *Set the charges account of the return lines, or a
default charges account on the journal ...*: set the account on the line or on the journal and
confirm again.

.. _accounting/payment-orders/returns-import:

Import a return file
--------------------

With the *Account Payment Return Import ISO20022* module, banks' status reports can be imported
instead of typed:

#. Download the payment status report from your online banking. The supported formats are
   camt.054.001.02 and the SEPA rejection reports pain.002.001.03 and pain.002.001.10 (SEPA 2025
   rulebook), also as a ZIP file with several reports.
#. Go to :menuselection:`Accounting --> Customers --> Import Payment Return`, select the file, and
   keep :guilabel:`Match After Import` ticked to look for the returned payments automatically.
#. Click :guilabel:`Import`. One payment return is created per report, with a line per returned
   transaction and the return reason of the bank, in :guilabel:`Draft`. Check the lines, then click
   :guilabel:`Confirm` as above.

A pain.002.001.10 report can list the accepted transactions next to the rejected ones: only the
rejected transactions become return lines, the transactions with an accepted, pending or
partially accepted status are ignored, since they are not returns. The name of the debtor is read
from the new report structure as well.

.. note::
   The bank journal of the return is detected from the account number of the report, so the bank
   account of your company must be known in Odoo. If the file is not recognised, the import stops
   with an error: make sure the module for the format is installed.

To debit the invoice again in a later debit order, tick :guilabel:`Include move lines from
returns` when adding the journal items to the order. In a Spanish company, a return whose reason
is classified as *hard* also asks you to review the mandate first (see :doc:`spanish_remittances`).

.. seealso::
   - :doc:`../payments`
   - :doc:`../bank/statement_import`
   - :doc:`sepa_mandate_signature`
   - :doc:`spanish_remittances`
   - :doc:`Automatic payments and dunning <../../../sales/subscriptions/automatic_payments>`

==============================
Batch bank transfers (Hungary)
==============================

The *Batch Bank Transfer* module prepares the **bank file** for paying many vendor bills at once.
You collect the open bills in a *batch*, check the amounts and the expected bank balance, and click
:guilabel:`Approve`: Odoo generates the transfer file in the format of your bank, which you upload
in your online banking. The formats of the main Hungarian banks are supported.

.. note::
   The module generates the file and keeps track of which bills were sent to the bank. It does
   **not** register payments. The bills are paid as usual when the bank statement is imported and
   :doc:`reconciled <../bank/reconciliation>`. If your bank accepts SEPA files, use :doc:`payment
   orders <payment_orders>` instead.

:ref:`Install <general/install>` the :guilabel:`Batch Bank Transfer` module
(`eyssen_batch_bank_transfer`). It requires the Hungarian localization (`eyssen_l10n_hu`, see
:doc:`../../fiscal_localizations/hungary`). Users need the :guilabel:`Invoicing` access right to
create and edit batches; the read-only accounting access right can only read them. Batches are
separate for every company.

.. _accounting/batch-bank-transfer/prerequisites:

Prerequisites
=============

- The **bank account of your company** (:menuselection:`Accounting --> Configuration --> Bank
  Accounts`, or the :guilabel:`Bank Accounts` of the company contact) is filled in with its
  :guilabel:`Bank`, and the bank has its **BIC (SWIFT) code**. The BIC decides the :ref:`file format
  <accounting/batch-bank-transfer/formats>`. The largest Hungarian banks are loaded with the
  Hungarian localization.
- The **vendors have a bank account** (IBAN or Hungarian account number), and the bills you want to
  pay are linked to it in the :guilabel:`Recipient Bank` field. A bill without a bank account can be
  added to a batch, but the batch cannot be approved.
- The bills are **posted** and not fully paid.

.. _accounting/batch-bank-transfer/create:

Create a batch
==============

Go to :menuselection:`Accounting --> Vendors --> Batch Bank Transfers` and click :guilabel:`New`.
The batch is numbered automatically (for example *UTALASOK-000001*).

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Date`
     - Creation date of the batch. It is replaced by the approval date when the batch is approved.
   * - :guilabel:`Bank Value Date`
     - Date on which the bank debits the transfers. It is **tomorrow** by default and cannot be
       earlier than today.
   * - :guilabel:`Bank Account`
     - Bank account of your company that is debited (required). The :guilabel:`Currency` of the
       batch is the currency of this account; an account without a currency is treated as HUF.
   * - :guilabel:`Vendor Credit Notes`
     - Also load the vendor credit notes (the *Refunds* of the vendors). Off by default.
   * - :guilabel:`Customer Credit Notes`
     - Also load the customer credit notes (refunds that you pay back to customers). On by default.

.. tip::
   The defaults of the two credit note options are system parameters (`1` = on, `0` = off):
   `eyssen_batch_bank_transfer.config.default_customer_credit` for :guilabel:`Vendor Credit Notes`
   and `eyssen_batch_bank_transfer.config.default_business_credit` for :guilabel:`Customer Credit
   Notes`. Edit them in :menuselection:`Settings --> Technical --> System Parameters` in
   :ref:`developer mode <developer-mode>`.

.. screenshot:: accounting-batch-bank-transfer-form
   :menu: Accounting ‣ Vendors ‣ Batch Bank Transfers ‣ (a draft batch)
   :shows: Draft batch with the header buttons, the bank account, bank value date and credit options, the balance forecast block and the lines list with the "Selected" toggle, amounts and partner bank accounts.
   :highlight: The header buttons and the lines list (red frame).
   :data: Draft batch with three open vendor bills in HUF, one without a vendor bank account.
   :module: eyssen_batch_bank_transfer
   :notes: English UI, light theme, 1440px width.

.. _accounting/batch-bank-transfer/load:

Add the bills
=============

Use one of the buttons of the draft batch. Only posted bills with an open amount, of the company and
in the currency of the batch bank account, are loaded. The amount already sent to the bank in
approved batches is subtracted, so a bill that has been fully sent is not proposed again, and a
partly sent bill is proposed for the remaining amount.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Button
     - Bills loaded
   * - :guilabel:`Load Overdue Invoices`
     - Bills whose due date is today or earlier.
   * - :guilabel:`Due Within 14 Days and Overdue`
     - Bills due within the next 14 days, and the overdue ones.
   * - :guilabel:`Load Invoices by Due Date`
     - Bills due on or before the date you enter in the :guilabel:`Due On or Before` field.
   * - :guilabel:`Load All Invoices`
     - All the open bills, whatever the due date.
   * - :guilabel:`Load Invoices`
     - Opens the list of the bills so that you can pick them yourself: select the bills, then click
       :menuselection:`Actions --> Add Invoices to Batch Bank Transfer`. You are brought back to the
       batch.

To add bills that were **already sent to the bank** (for instance to repeat a transfer the bank
rejected), select them in the :guilabel:`Load Invoices` list and click :menuselection:`Actions -->
Add Previously Transferred Invoices to Batch Bank Transfer`: the line is created for the full
amount of the bill.

You can also work from the list of vendor bills at any time: the :guilabel:`Bank Transfer` column
shows whether a bill has been sent to the bank (:guilabel:`Not Sent`, :guilabel:`Partially Sent` or
:guilabel:`Fully Sent`). Enable it with the optional columns selector if it is hidden.

.. screenshot:: accounting-batch-bank-transfer-add-bills
   :menu: Accounting ‣ Vendors ‣ Batch Bank Transfers ‣ (a draft batch) ‣ Load Invoices
   :shows: List of vendor bills with the "Bank Transfer" column, three bills selected and the Actions menu open on "Add Invoices to Batch Bank Transfer".
   :highlight: The "Bank Transfer" column and the Actions menu entry (red frame).
   :data: Vendor bills in HUF, one of them partially sent.
   :module: eyssen_batch_bank_transfer
   :notes: English UI, light theme, 1440px width.

.. _accounting/batch-bank-transfer/lines:

Check the lines
===============

Every bill is a line of the batch. You can edit the following directly in the list:

- :guilabel:`Amount to Transfer`: the amount to pay. Lower it to pay a bill **partially**.
- :guilabel:`Comment`: the message for the beneficiary. It is filled with the vendor reference and
  the payment reference of the bill.
- :guilabel:`Selected`: marks the line, to move it to another batch (see below).

The :guilabel:`Transferred Amount` is what has already been sent to the bank for the bill in other
approved batches. A line is shown in **red** when its amount and the transferred amount exceed the
total of the bill, and in **orange** when the bill has no vendor bank account. The search box above
the list filters the lines.

- :guilabel:`Move Selected Invoices to New Batch` moves the :guilabel:`Selected` lines to a new
  draft batch with the same bank account, for instance to pay them on another day.
- :guilabel:`Clear` removes all the lines of the batch (the bills are not modified).

Balance forecast
----------------

The block next to the lines helps you to check that the account can cover the transfers. The
figures are calculated when the batch is saved, and the closing balance after the transfers is
updated when you change the lines.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Figure
     - Meaning
   * - :guilabel:`Bank Balance as of Date`
     - Balance of the bank journal(s) of the account up to the date of the batch.
   * - :guilabel:`Increase`
     - Amounts expected to come in: the open customer invoices in the currency of the account,
       overdue, due in the first week and due in the second week after the date.
   * - :guilabel:`Decrease`
     - Open vendor bills in the currency of the account: overdue, due in the first week and due in
       the second week after the date (click the arrow to expand the details).
   * - :guilabel:`Closing Balance at Date + 2 Weeks (Invoices)`
     - Balance plus increase minus decrease: the balance if all the bills due within two weeks were
       paid.
   * - :guilabel:`Closing Balance at Date + 2 Weeks (Transfers)`
     - Balance plus increase minus the total of **this batch**.

.. _accounting/batch-bank-transfer/approve:

Approve the batch and send the file
===================================

Click :guilabel:`Approve`. Odoo checks the batch, generates the file, attaches it to the batch and
downloads it. The status changes from :guilabel:`Draft` to :guilabel:`Sent to Bank`, the
:guilabel:`Date` becomes today, and the lines can no longer be edited. Upload the file in your
online banking and authorize the transfers there.

The batch cannot be approved, and an explicit message tells you why, when:

- a bill has no vendor bank account (*No partner bank account set for invoice ...*);
- the currency of the bank account does not fit the format (for example, a foreign-currency account
  with a format that only supports HUF);
- for a foreign-currency transfer from a CIB account, the bank of the vendor has no SWIFT/BIC code.

.. _accounting/batch-bank-transfer/formats:

File formats
------------

The format depends on the **BIC of the bank** of the company bank account selected on the batch.
Any other bank gets the :guilabel:`UNG` file.

.. list-table::
   :header-rows: 1
   :widths: 22 26 26 26

   * - Bank (BIC)
     - HUF account
     - Foreign currency account
     - Notes
   * - UniCredit Bank (BACXHUHB)
     - `.PAY` file, named after the bank value date (`yymmdd.PAY`)
     - Not available
     - Amounts in whole forints.
   * - OTP Bank (OTPVHUHB)
     - Electra XML file (`HUFTransactions`)
     - Electra XML file (`DEVTransactions`)
     - Encoded in ISO-8859-2. The file is named after the day of the approval (`yyyymmdd.xml`).
   * - CIB Bank (CIBHHUHB)
     - CSV file (`yyyymmdd_HUF.csv`)
     - CSV file (`yyyymmdd_HUF.csv`)
     - Semicolon-separated, named after the day of the approval. HUF amounts in whole forints,
       foreign currency amounts with two decimals. A foreign-currency transfer needs the SWIFT/BIC
       code of the vendor's bank.
   * - Any other bank
     - `.UNG` file (`UNyymmdd.UNG`)
     - Not available
     - Amounts in whole forints.

In the `.PAY` and `.UNG` files, the lines paid to the same vendor bank account are **combined** into
one transfer (the amounts are added, and the comments joined and shortened to 96 characters), and
the names, addresses and comments are written without accents.

Undo
----

Click :guilabel:`Undo` on a batch that has been sent to bank to cancel it: the attached files are
deleted, the :guilabel:`Date` is cleared and the batch is a :guilabel:`Draft` again, so you can
change it and generate a new file. Nothing is booked in the accounting by the module, so there is
nothing else to reverse. Undo a batch only if the file was **not** processed by the bank.

.. _accounting/batch-bank-transfer/reconcile:

After the bank has processed the transfers
==========================================

Import the bank statement (:doc:`../bank/statement_import`) and :doc:`reconcile
<../bank/reconciliation>` the debits with the bills, as for any other payment. The
:guilabel:`Bank Transfer` column of the vendor bills shows what was sent to the bank: a bill is
:guilabel:`Fully Sent` when the approved batches cover its open amount, and :guilabel:`Partially
Sent` when they cover only a part of it.

.. seealso::
   - :doc:`payment_orders`
   - :doc:`../../fiscal_localizations/hungary`

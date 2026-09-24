=========================
Import statement files
=========================

When your bank is not covered by :doc:`online synchronization <bank_synchronization>`, upload the
statement files your bank provides. Dedicated import modules read the export formats of several
Hungarian banks and of Wise, and turn each line of the file into a :doc:`bank transaction
<transactions>` ready for :doc:`reconciliation <reconciliation>`.

Available importers
===================

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Bank
     - File format
     - Menu
   * - OTP Bank
     - CSV, semicolon-separated
     - :menuselection:`Accounting --> Configuration --> Banks --> OTP Bank Statement Import`
   * - K&H Bank
     - Excel (.xls)
     - :menuselection:`Accounting --> Configuration --> Banks --> K&H Bank Statement Import`
   * - CIB Bank
     - CSV, semicolon-separated
     - :menuselection:`Accounting --> Configuration --> Banks --> CIB Bank Statement Import`
   * - Raiffeisen Bank
     - Excel (.xls)
     - :menuselection:`Accounting --> Configuration --> Banks --> Raiffeisen Bank Statement Import`
   * - Wise
     - CSV, comma-separated
     - :menuselection:`Accounting --> Configuration --> Banks --> Wise Bank Statement Import`

.. note::
   The importers require the *eYssen Accountant* module. Each bank is a separate module, so only the
   banks you actually use need to be installed.

Import a file
=============

Open the menu of your bank, then:

#. Click :guilabel:`Data file` and select the file exported from your bank's online banking.
#. Optionally tick :guilabel:`Create monthly statement` to group the imported transactions into one
   bank statement per month and per journal, instead of leaving them as loose transactions.
#. Click :guilabel:`Import`.

.. screenshot:: accounting-bank-statement-import-wizard
   :menu: Accounting ‣ Configuration ‣ Banks ‣ OTP Bank Statement Import
   :shows: The import dialog with the "Data file" upload field, the "Create monthly statement"
      checkbox and the Import / Cancel buttons.
   :highlight: The "Create monthly statement" checkbox.
   :data: A selected file named "otp_kivonat_2026_09.csv".
   :module: eyssen_account_bank_statement_import_otp
   :notes: English UI, light theme, dialog only.

.. _accounting/bank/import-journal-matching:

How transactions are assigned to a journal
------------------------------------------

For the bank importers, each row of the file carries the account number it belongs to. Odoo
normalizes that number, looks for the matching :guilabel:`Bank Account` in the right currency, and
books the row in the journal linked to it. This means one file may contain several accounts, and
each account is booked in its own journal.

The import stops with an explicit error when:

- the currency in the file is not active in the database;
- no bank account matches the account number and currency (:guilabel:`Bank account not found`);
- the matching bank account is not linked to any journal (:guilabel:`Journal not found`).

In these cases, correct the bank account or the journal under :menuselection:`Accounting -->
Configuration --> Banks --> Add a Bank Account` and import the file again.

The Wise importer works differently: Wise files have no account number, so you select the
:guilabel:`Journal` in the dialog.

.. tip::
   Importing the same file twice is safe. Each transaction is stored with the bank reference built
   from the file, and a transaction already present in the journal is skipped.

.. seealso::
   - :doc:`bank_synchronization`
   - :doc:`transactions`
   - :doc:`reconciliation`

=========================
Import statement files
=========================

When your bank is not covered by :doc:`online synchronization <bank_synchronization>`, upload the
statement files your bank provides. Dedicated import modules read the export formats of several
Hungarian banks and of Wise, and the standard file formats such as the Spanish *Norma 43*, and turn
each line of the file into a :doc:`bank transaction <transactions>` ready for :doc:`reconciliation
<reconciliation>`.

Files and online synchronization can also be combined, for example to load the history that
precedes the connection: see :ref:`accounting/bank/import-backfill`, and
:ref:`accounting/bank-sync/which-method` to choose between the two methods.

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

.. _accounting/bank/import-standard-files:

Standard statement files
========================

Statement files in a standard format are imported with the generic importer, which reads every
format whose module is installed, for example *camt* (CAMT Format Bank Statements Import), *OFX*
(Import OFX Bank Statement), spreadsheet files (Bank Statement TXT/CSV/XLSX Import) and, for Spanish
banks, the *AEB Norma 43* files (see :ref:`accounting/bank/import-n43`). The list of the formats
your database can read is displayed in the import dialog.

There are two ways to open the dialog:

- :menuselection:`Accounting --> Accounting --> Import Statement`;
- from the :guilabel:`Accounting Dashboard`, on the card of the bank journal: the
  :guilabel:`Import (OCA)` button (displayed when the :guilabel:`Bank Feeds` setting of the journal
  is a file import), or the :guilabel:`Import Statement (OCA)` link of the card.

Then:

#. Select the statement file.
#. Optionally click :ref:`Preview <accounting/bank/import-preview>` to check what would be
   imported.
#. Click :guilabel:`Import and View`.

A bank statement is created for each account of the file, in the bank journal whose bank account
matches the account number of the file, and the list of the new statements is displayed. The file is
attached to the first statement. Transactions that were already imported are not created a second
time, and a message tells you how many were ignored.

.. _accounting/bank/import-standard-journal:

Which journal is used
---------------------

If the file contains the account number, Odoo looks for the bank journal whose bank account has that
number, and checks that the currency of the file is the one of the journal. When the dialog was
opened from a journal card, that journal must be the one found for the file.

Some formats do not contain the account number. For them, open the dialog from the card of the right
bank journal on the :guilabel:`Accounting Dashboard`.

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Message
     - Cause and solution
   * - *This bank statement file format is not supported.*
     - The module for this format is not installed, or the file is not in the expected format.
   * - *The format of this bank statement file doesn't contain the bank account number, so you must
       start the wizard from the right bank journal in the dashboard.*
     - Open the dialog from the journal card, not from the menu.
   * - *Could not find any bank account with number ... linked to partner ...*
     - Create the bank account of your company and set it on the bank journal
       (:menuselection:`Accounting --> Configuration --> Journals`, :guilabel:`Account Number`).
   * - *The bank account with number ... exists in Odoo but it is not set on any bank journal.*
     - Set the account number on the bank journal.
   * - *The journal found for the file (...) is different from the selected journal (...).*
     - You opened the dialog from another journal than the one of the account in the file.
   * - *The currency of the bank statement (...) is not the same as the currency of the journal
       '...' (...).*
     - Set the currency on the journal, or import the file into the journal of the right currency.
   * - *The bank statement file uses currency '...' but there is no such currency in Odoo.*
     - Activate the currency.
   * - *The Bank Accounting Account is not set on the journal '...'.*
     - Set the :guilabel:`Bank Account` of the journal in its :guilabel:`Journal Entries` tab.
   * - *You have already imported this file, or this file only contains already imported
       transactions.*
     - Nothing new to import. When the journal is also fed by online synchronization, the message
       also lists the lines that the synchronization had booked.

After a successful import, the :guilabel:`Bank Feeds` setting of the journal becomes a file import
if it was not set yet. A journal that already has another source, for example :guilabel:`Online Bank
Sync`, keeps it.

.. _accounting/bank/import-preview:

Preview an import
-----------------

Click :guilabel:`Preview` instead of :guilabel:`Import and View` to see the result without importing
anything. Odoo reads the file and runs the whole import, then cancels it: no statement, no
transaction, no attachment is kept, and the :guilabel:`Bank Feeds` setting of the journal is not
changed. A message is displayed, titled *Statement import preview*:

- *Preview: N new transaction(s), total X.* gives the number of lines that would be created and the
  sum of their amounts, which you can compare with the total of the file;
- below it, the notifications of the import: the transactions already imported, and the lines
  skipped because online synchronization already booked them (see
  :ref:`accounting/bank/import-backfill`);
- if the import would fail, the error message that you would get, for example an unknown account
  number.

The dialog stays open, so you can fix the problem (or just go ahead) and click :guilabel:`Import and
View`. The preview is available in this dialog only, not in the importers of the Hungarian banks
above.

.. tip::
   Use the preview when you import a file that overlaps a period you already loaded, or before the
   first import into a journal fed by online synchronization.

.. _accounting/bank/import-n43:

Spanish banks: Norma 43
=======================

:ref:`Install <general/install>` the *Importación de extractos bancarios españoles (Norma 43)*
module (``l10n_es_account_statement_import_n43``) to import the *AEB Norma 43* files (:file:`.n43`,
also called *Cuaderno 43*) that all Spanish banks provide, with the generic dialog described above.
The journal is found from the account number of the file.

The bank journal form has a :guilabel:`Norm 43 options` section (:guilabel:`Advanced Settings`
tab):

- :guilabel:`Date type for N43 Import`: use the :guilabel:`Value Date` (default) or the
  :guilabel:`Operation Date` of the file as the date of the transaction;
- :guilabel:`Partner search for N43 import`: how the partner of each transaction is recognized
  (see below). The default is :guilabel:`All`;
- :guilabel:`Exclude pattern for N43 import`: a regular expression; the lines of the file whose
  label matches it, from its beginning, are not imported.

.. note::
   The import checks the control totals of the Norma 43 file (number of records, debit and credit
   totals and, when the file gives both an initial and a final balance, the final balance) and
   stops with an error if the file is incomplete.

.. _accounting/bank/import-n43-reimport:

Importing a file twice
----------------------

Every movement of the file gets an identifier made of the account, the operation and value
dates, the concepts, the amount, the document number, the references and the text of the
complementary records. Importing the same file again, or two files whose periods overlap (for
example the first half of the month, then the whole month), creates each movement only once, and
the message *N transactions had already been imported and were ignored.* tells you how many were
skipped. Two identical movements of the same file (for example two card payments of the same
amount on the same day) are told apart by their order, so both are kept.

.. important::
   The identifier is built from the whole movement: if a bank sends the same movement again with a
   different text or reference, it is imported again. Movements imported before this protection
   existed have no identifier and cannot be recognized: do not re-import a period that you already
   loaded with an earlier version.

.. _accounting/bank/import-n43-concepts:

Concept codes on the transactions
---------------------------------

Three fields of the Norma 43 movement are kept on the transaction, in its :guilabel:`Technical
Information` tab:

- :guilabel:`N43 common concept`: the two-digit AEB *common concept*, that is the same for all banks
  (for example 03 for direct debits, 04 for transfers, 12 for cards, 14 for returns and unpaid
  items, 15 for payrolls, 17 for interest, fees and taxes). The names of the codes are given in
  Spanish, as in the AEB specification;
- :guilabel:`N43 bank concept`: the three-character code that is specific to the bank;
- :guilabel:`N43 document number`: the document number of the movement.

You can search the transactions by :guilabel:`N43 common concept`, for example to find all the bank
charges. The fields are read-only and are only filled by the import.

.. _accounting/bank/import-n43-partner:

Recognizing the partner
-----------------------

With :guilabel:`Partner search for N43 import`, Odoo tries to set the partner of every imported
transaction from the complementary records of the movement. The counterparty name of the bank is
also kept in the transaction whether or not a partner is found. The options are :guilabel:`None`
(no search), one bank (:guilabel:`CaixaBank`, :guilabel:`Santander`, :guilabel:`Sabadell`,
:guilabel:`BBVA`, :guilabel:`Bankinter`, :guilabel:`Unicaja`, :guilabel:`Kutxabank`,
:guilabel:`ING`, :guilabel:`Abanca`, :guilabel:`Ibercaja`), or :guilabel:`All`.

With one bank, only the rule of that bank is used. With :guilabel:`All`, the rules are tried in
this order, until a partner is found:

#. the rule of the bank that issued the file, recognized by the bank code of the file (the four
   digits that follow the check digits in a Spanish IBAN; see the table);
#. a general search: the tax id (NIF, NIE or CIF, checked for validity) found in the concept texts
   against the :guilabel:`Tax ID` of your contacts, then a valid IBAN against the bank accounts of
   your contacts, then the counterparty name;
#. the rules of the other banks, in the order of the list above.

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Bank
     - Bank code
     - Rule
   * - CaixaBank
     - 2100
     - Original rule: tax id and name of the complementary records.
   * - Santander
     - 0049
     - Original rule: tax id and name of the complementary records.
   * - Sabadell
     - 0081
     - Original rule: name of the complementary records.
   * - BBVA
     - 0182
     - General search (tax id, IBAN, then the name read in the first two
       complementary records).
   * - Bankinter
     - 0128
     - General search (tax id, IBAN, then the name read in the first two
       complementary records).
   * - Unicaja
     - 2103, 2048 (former Liberbank)
     - General search (tax id, IBAN, then the name read in the first two
       complementary records).
   * - Kutxabank
     - 2095
     - General search (tax id, IBAN, then the name read in the first two
       complementary records).
   * - ING
     - 1465
     - General search (tax id, IBAN, then the name read in the first two
       complementary records).
   * - Abanca
     - 2080
     - General search (tax id, IBAN, then the name read in the first two
       complementary records).
   * - Ibercaja
     - 2085
     - General search (tax id, IBAN, then the name read in the first two
       complementary records).

The name search ignores the usual prefixes (*Transferencia de*, *Bizum de*, *Recibo*...), looks for
the longest match of more than 7 characters among your companies and main contacts, and never
returns your own company. A partner found by tax id or IBAN is the main contact of the company.

.. note::
   The rules of the seven banks added last are based on the published layouts of those banks and on
   sample files. Check the partners of your first imports, and use the reconciliation to correct
   them.

.. _accounting/bank/import-backfill:

Load history into a journal that is synchronized online
=======================================================

An :doc:`online synchronization <bank_synchronization>` starts when the connection is made: it does
not load the older transactions. To have the complete history in the journal, import the statement
files of the earlier period into the same journal.

#. Connect the journal and run the first synchronization
   (:ref:`accounting/bank-sync/run`).
#. Download from your bank the statement file of the period before the connection. It may overlap
   the synchronized period, for example when it ends a few days after the connection date.
#. On the card of the journal, click the :guilabel:`Import Statement (OCA)` link.
#. Click :ref:`Preview <accounting/bank/import-preview>` and read the message: the lines that the
   synchronization already booked are listed as *N transaction(s) were already synchronized online
   and were ignored*.
#. Click :guilabel:`Import and View`.

The journal keeps :guilabel:`Online Bank Sync` as its :guilabel:`Bank Feeds` source. The lines
skipped are not imported, and the opening balance of the new statement is set after them, as for the
transactions already imported.

.. note::
   This check is performed by the *Online Bank Sync: skip synchronized lines on file import* module
   (``account_bank_sync_statement_import``). It is installed automatically when the *Online Bank
   Sync* and the *Import Statement Files* modules are both installed. It applies to the generic
   import dialog and its formats (Norma 43, camt, OFX...), not to the importers of the Hungarian
   banks, which have their own duplicate check.

How a file line is matched
--------------------------

A line of the file is considered as already synchronized when the journal has a synchronized line
with the **same amount** and one of the following is true, checked in this order:

#. the line carries the **bank transaction id** of the synchronized line (in its reference or as a
   word of its label; a provider prefix such as ``EB-`` is ignored), and the dates are at most 7
   days apart, or the tolerance of the journal if it is larger;
#. the dates are within the **date tolerance** of the journal, and the labels, references or
   counterparty names have a word in common;
#. the line is the **only** synchronized line with that amount within the date tolerance.

Each synchronized line is used once: if the file holds two identical payments and the
synchronization booked one, the second one is imported. Lines already imported from a file are left
to the usual duplicate check.

The matching is configured on the bank journal, in the :guilabel:`Bank Account Number` group of the
:guilabel:`Journal Entries` tab:

- :guilabel:`Skip lines already synchronized online`: on by default. Switch it off to import every
  line of the file;
- :guilabel:`Date tolerance (days)`: 2 by default, displayed when the option is on. It is the
  maximum difference between the date of the line in the file and the date of the synchronized
  line. Banks often give a different date for the same transaction (value date or booking date, or
  a weekend in between).

If every line of the file was skipped, Odoo reports that the file was already imported, and adds the
list of the lines recognized as synchronized. The message lists at most 20 lines.

.. warning::
   The check works in one direction only: a later synchronization does not look at the lines that
   were imported from a file. Do not import a file for a period that the synchronization has not
   loaded yet, or the same transactions will be booked twice. Files are meant for the period that
   precedes the connection, or that the synchronization has already loaded.

.. tip::
   Rule 3 accepts a single synchronized line with the same amount as a match even without any
   common text. If two different payments of the same amount fall within the tolerance, check the
   list of skipped lines in the preview and lower the tolerance (0 means the same date) or switch
   the option off for that import.

.. seealso::
   - :doc:`bank_synchronization`
   - :doc:`enable_banking`
   - :doc:`transactions`
   - :doc:`reconciliation`

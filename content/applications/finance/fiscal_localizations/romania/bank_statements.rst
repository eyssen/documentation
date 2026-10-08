=====================
Bank statement import
=====================

The :guilabel:`Romania - Bank statement import (MT940, CAMT.053, CSV)`
(`l10n_ro_account_statement_import`) module extends the :ref:`generic statement import
<accounting/bank/import-standard-files>` with the MT940 files of the Romanian banks and with the
recognition of the customers and vendors of the Romanian companies in the imported transactions.
It reads:

- **MT940** files, with the layout of the transaction details of *Banca Comercială Română* (BCR),
  *BRD - Groupe Société Générale*, *ING Bank România*, *Banca Transilvania* (BT), *Raiffeisen
  Bank România* and *UniCredit Bank România*, and of any other bank that uses the SWIFT standard;
- **CAMT.053** files, with the standard camt statement import module;
- **CSV and Excel** files, with a mapping of the columns (*Statement Sheet Mappings*).

.. important::
   The importers have been developed from the public descriptions of the formats, and tested
   with synthetic statement files. They have **not** been verified with real files of the banks
   yet. See :ref:`localizations/romania/statement-status`. Use the :ref:`preview
   <accounting/bank/import-preview>` of the import dialog on the first files of each bank, and
   compare the balances and the totals with the statement of your bank.

Configuration
=============

:ref:`Install <general/install>` the module. The Romanian bank journals get a
:guilabel:`Romanian statement import` group in the :guilabel:`Advanced Settings` tab
(:menuselection:`Accounting --> Configuration --> Journals`, bank journals of a company whose
fiscal country is Romania):

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Purpose
   * - :guilabel:`MT940 bank format`
     - Layout of the transaction details (field `:86:`) of the MT940 files of the bank:
       :guilabel:`Automatic (from the BIC / IBAN of the statement)` (the default), one of the six
       banks, or :guilabel:`Other bank (generic MT940)`. With the automatic mode, the bank is
       detected from the BIC or from the IBAN of the statement (`RNCB`, `BRDE`, `INGB`, `BTRL`,
       `RZBR`, `BACX`); select the bank explicitly if the detection fails.
   * - :guilabel:`MT940 transaction date`
     - Date given to the imported lines: :guilabel:`Booking date` (the default; the value date is
       used if the bank provides no booking date) or :guilabel:`Value date`.
   * - :guilabel:`Find partners by CUI / IBAN`
     - Enabled by default. When the bank does not identify the account of the counterparty, Odoo
       looks for an IBAN or a Romanian fiscal code in the details of the transaction, and sets the
       partner.

Set the bank account number (IBAN) of the company on the journal, so that Odoo can find the
journal of a file from the account number it contains.

Import a statement
==================

Open the import dialog with :menuselection:`Accounting --> Accounting --> Import Statement`, or
from the card of the bank journal on the :guilabel:`Accounting Dashboard`, as described in
:ref:`accounting/bank/import-standard-files`, and select the file. Odoo recognizes MT940 files by
their content. A file can contain several statements (several accounts or several days); they are
all imported.

For each MT940 statement, Odoo creates a bank statement with the opening and closing balance of
the file. Each transaction line gets:

- the date, according to the :guilabel:`MT940 transaction date` of the journal;
- the label (details of the transaction), the reference of the customer or of the bank, and the
  amount, with its sign;
- the name and the account number of the counterparty, if the bank provides them;
- a unique import identifier, so that importing the same file again is refused and a transaction
  already imported is never created twice.

The files can be encoded in UTF-8 or in Windows-1250 (the Central European encoding of Romanian
diacritics).

.. note::
   An MT940 file for another bank account than the one of the selected journal is refused with an
   error message.

Recognition of the partner
--------------------------

On the journals of Romanian companies with :guilabel:`Find partners by CUI / IBAN` enabled, and for
all formats (MT940, CAMT.053 and spreadsheets), the partner of a transaction without partner is
found as follows:

#. The IBANs found in the transaction details (excluding the accounts of the company) are looked
   up in the bank accounts of the contacts.
#. Otherwise, the Romanian fiscal codes (*CUI* or *CIF*, with or without the `RO` prefix, written
   as `CUI 23456783`, `CIF`, `Cod fiscal` or `RO23456783`) are looked up in the :guilabel:`Tax ID`
   of the contacts.

The partner is only set if the match is **unambiguous**: when several contacts share the same
IBAN or fiscal code, the transaction is left without partner. The partner is then available for
the :doc:`reconciliation <../../accounting/bank/reconciliation>` of the line.

CSV and Excel files
-------------------

The module does not provide predefined column mappings for the CSV exports of the banks. Create
a mapping for each bank export in :menuselection:`Accounting --> Configuration --> Accounting -->
Statement Sheet Mappings`, set it as the default in the :guilabel:`Statement Import Map` group of
the journal (:guilabel:`Advanced Settings` tab), or select it in the import dialog. The recognition of the partners by
IBAN or CUI also applies to these files.

.. _localizations/romania/statement-status:

Formats verified so far
=======================

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Format
     - Bank
     - Status
   * - MT940
     - BCR, BRD, ING, BT, Raiffeisen
     - Tested with synthetic and anonymous sample files built from the public format
       descriptions. **Not verified** with real bank files.
   * - MT940
     - UniCredit
     - Tested with an inline synthetic sample of the parser only (same layout as BCR and
       Raiffeisen). **Not verified** with real bank files.
   * - MT940
     - Other banks
     - Generic SWIFT parser. **Not verified** with real bank files.
   * - CAMT.053
     - Any
     - Tested with a synthetic Romanian sample. **Not verified** with real bank files.
   * - CSV / Excel
     - Any
     - Tested with a synthetic file and mapping. No predefined mapping for the banks.

.. seealso::
   - :doc:`../../accounting/bank/statement_import`
   - :doc:`../romania`

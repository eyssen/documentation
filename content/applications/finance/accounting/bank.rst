:show-content:

======================
Bank and cash accounts
======================

You can manage as many bank or cash accounts as needed on your database. Configuring them correctly
allows you to have all your banking data up-to-date and ready for :doc:`reconciliation
<bank/reconciliation>` with your journal entries.

In Odoo Accounting, each bank account has a dedicated journal set to post all entries in a dedicated
account. Both the journal and the account are automatically created and configured whenever you add
a bank account.

.. note::
   :ref:`Cash journals <accounting/journals/cash>` and accounts must be configured manually.

Bank and cash journals are displayed by default on the :guilabel:`Accounting Dashboard` in the form
of cards which include action buttons.

.. screenshot:: accounting-bank-dashboard-card
   :menu: Accounting ‣ Dashboard
   :shows: The Accounting Dashboard with one bank journal card ("Bank") showing the stacked
      :guilabel:`Transactions`, :guilabel:`Reconcile 12 Items` and :guilabel:`Sync now` buttons on
      the left, and the :guilabel:`Balance`, :guilabel:`Last Statement` figures, the
      :guilabel:`5 to check` link and the circular reconciliation-progress indicator on the right.
   :highlight: The bank journal card (red frame).
   :data: Demo company "YourCompany HU"; a bank journal with unreconciled statement lines and a
      non-zero balance.
   :module: account, account_reconcile_oca, eyssen_accountant, account_bank_sync
   :notes: English UI, light theme, 1440px width, crop to the card.

.. _accounting/bank/manage:

Manage bank and cash accounts
=============================

.. _accounting/bank/create:

Create a bank account
---------------------

To add a bank account, go to the :guilabel:`Accounting Dashboard` and, on the card of a bank journal
that has no bank account yet, click :guilabel:`Bank Setup`. Fill out the bank information (account
number, bank, and the journal the account is linked to) and click :guilabel:`Create`.

.. note::
   - Odoo automatically detects the bank account type (e.g., IBAN) and enables some features
     accordingly.
   - A default :ref:`bank journal <accounting/journals/bank>` is available and can be used to
     configure your bank account by going to :menuselection:`Accounting --> Configuration -->
     Accounting: Journals --> Bank`. Open it and edit the different fields to match your bank
     account information.
   - A bank account can also be added from :menuselection:`Accounting --> Configuration --> Banks
     --> Add a Bank Account`.

.. _accounting/bank/sync:

Connect a bank for automatic synchronization
--------------------------------------------

Instead of importing statements by hand, you can let Odoo fetch the transactions from your bank or
from a payment institution. Synchronization is provided by the *Online Bank Sync* modules, which
connect a journal to a remote account and book the incoming transactions as bank statement lines.

.. seealso::
   :doc:`bank/bank_synchronization`

.. _accounting/bank/import:

Import statement files
----------------------

If your bank is not covered by a synchronization provider, upload the statement files your bank
produces. Odoo reads the common exchange formats, and dedicated modules read the proprietary export
formats of several Hungarian banks.

.. seealso::
   :doc:`bank/statement_import`

.. toctree::
   :titlesonly:

   bank/bank_synchronization
   bank/statement_import
   bank/transactions
   bank/reconciliation
   bank/reconciliation_models
   bank/internal_transfers
   bank/cash_register
   bank/foreign_currency

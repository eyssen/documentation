===========================================
Manage a bank account in a foreign currency
===========================================

In Odoo, every transaction is recorded in the default currency of the company, and reports are all
based on that default currency. When you have a bank account in a foreign currency, for every
transaction, Odoo stores two values:

-  The debit/credit in the currency of the *company*;
-  The debit/credit in the currency of the *bank account*.

Configuration
=============

Activate multi-currencies
-------------------------

To work with multiple currencies, activate the currencies you need and, if required, the automatic
update of their rates.

.. seealso::
   :doc:`../get_started/multi_currency`

Create a new bank account
-------------------------

In the accounting application, go to :menuselection:`Accounting --> Configuration --> Journals` and
create a new one. Enter a :guilabel:`Journal Name` and set the :guilabel:`Type` to `Bank`. In the
:guilabel:`Journal Entries` tab, enter a **short code**, a **currency**, and then finally click on
the :guilabel:`Bank Account` field to create a new account. In the pop-up window of the account
creation, enter a name, a code (ex.: 550007), set its type to `Bank and Cash`, set a currency type,
and save. When you are back on the **journal**, click on the :guilabel:`Account Number` field, and
in the pop-up window, fill out the :guilabel:`Account Number`, :guilabel:`Bank` of your account, and
save.

.. screenshot:: accounting-foreign-currency-journal
   :menu: Accounting ‣ Configuration ‣ Journals ‣ (a foreign-currency bank journal)
   :shows: A bank journal form with the Journal Entries tab open, showing the short code, the
      foreign Currency, the Bank Account and the Account Number.
   :highlight: The :guilabel:`Currency` field (red frame).
   :data: Journal "Bank EUR", currency EUR, company currency HUF.
   :module: account
   :notes: English UI, light theme, 1440px width.

Upon creation of the journal, Odoo automatically links the bank account to the journal. It can be
found under :menuselection:`Accounting --> Configuration --> Accounting: Chart of Accounts`.

Vendor bill in a foreign currency
=================================

To pay a bill in a foreign currency, simply select the currency next to the :guilabel:`Journal`
field and register the payment. Odoo automatically creates and posts the foreign **exchange gain or
loss** as a new journal entry.

.. screenshot:: accounting-foreign-currency-bill
   :menu: Accounting ‣ Vendors ‣ Bills ‣ (a bill)
   :shows: A vendor bill header with the Currency field set to a foreign currency next to the
      Journal field, and the bill total displayed in that currency.
   :highlight: The :guilabel:`Currency` field (red frame).
   :data: Bill of 1,200.00 EUR in a HUF company.
   :module: account
   :notes: English UI, light theme, crop to the header.

.. note::
   Note that you can pay a foreign bill with another currency. In that case, Odoo automatically
   converts between the two currencies.

Exchange differences
====================

The exchange gain or loss realized when a foreign-currency invoice or bill is paid is posted
automatically in the journal and on the accounts configured for it.

.. seealso::
   :ref:`Exchange difference entries <multi-currency/config-exch-diff>`

To review the foreign-currency balances of your accounts at a given date, use the
:ref:`Trial Balance <accounting/reporting/trial-balance>` or the :ref:`General Ledger
<accounting/reporting/general-ledger>` with the :guilabel:`Currency Translation` filter.

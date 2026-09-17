=================
Deferred expenses
=================

**Deferred expenses** and **prepayments** (also known as **prepaid expenses**) are both costs that
have already occurred for products or services yet to be received.

Such costs are **assets** for the company that pays them since it already paid for products and
services but has either not yet received them or not yet used them. The company cannot report them
on the current **profit and loss statement**, or *income statement*, since the payments will be
effectively expensed in the future.

These future expenses must be deferred on the company's balance sheet until the moment in time they
can be **recognized**, at once or over a defined period, on the profit and loss statement.

For example, let's say we pay $1200 at once for one year of insurance. We already pay the cost now
but haven't used the service yet. Therefore, we post this new expense in a *prepayment account* and
decide to recognize it on a monthly basis. Each month, for the next 12 months, $100 will be
recognized as an expense.

Prepayment account
==================

Deferred expenses are recorded on an account of type :guilabel:`Prepayments` (see
:ref:`account types <chart-of-account/type>`). Make sure such an account exists in your
:doc:`chart of accounts <../get_started/chart_of_accounts>`, and select it on the vendor bill
line (or as the product's expense account) instead of the expense account.

.. _vendor_bills/deferred/recognition:

Recognizing deferred expenses periodically
==========================================

The periodic recognition of deferred expenses can be automated with the *Odoo 18 Assets Management*
(`om_account_asset`) module, using a dedicated :doc:`asset category <assets>`:

#. Go to :menuselection:`Accounting --> Configuration --> Management --> Asset Category` and create
   a category, e.g., *Prepaid insurance*:

   - :guilabel:`Asset Account` and :guilabel:`Depreciation Entries: Asset Account`: your
     prepayment account;
   - :guilabel:`Depreciation Entries: Expense Account`: the expense account on which the cost is
     recognized;
   - :guilabel:`Number of Entries`: e.g., `12`, and :guilabel:`One Entry Every`: `1` month;
   - :guilabel:`Computation Method`: :guilabel:`Linear`;
   - optionally :guilabel:`Prorata Temporis` and :guilabel:`Auto-Confirm Assets`.

#. On the vendor bill, select this category in the :guilabel:`Asset Category` column of the
   deferred line (or set it as the product's :guilabel:`Asset Type`). The line's account is replaced
   by the prepayment account.
#. When the bill is confirmed, a record is created in :menuselection:`Accounting --> Configuration
   --> Management --> Assets` with the recognition schedule in its :guilabel:`Depreciation Board`
   tab.
#. The recognition entries (debit expense, credit prepayment) are generated monthly, or manually
   from :menuselection:`Accounting --> Accounting --> Generate Entries --> Generate Assets Entries`.

.. screenshot:: accounting-deferred-expenses-category
   :menu: Accounting ‣ Configuration ‣ Management ‣ Asset Category ‣ New
   :shows: Asset category "Prepaid insurance" with the prepayment account as Asset Account and Depreciation Entries: Asset Account, an insurance expense account as Depreciation Entries: Expense Account, 12 entries, one entry every 1 month, Linear method.
   :highlight: The account fields (red frame).
   :data: Demo company "YourCompany HU" with a prepayment account (e.g., "391 Aktív időbeli elhatárolás").
   :module: om_account_asset
   :notes: English UI, light theme, 1440px width.

.. note::
   The expense can also be recognized manually with miscellaneous journal entries (debit the
   expense account, credit the prepayment account), created from :menuselection:`Accounting -->
   Accounting --> Journal Entries`.

.. _vendor_bills/deferred/report:

Deferred expense report
=======================

The :guilabel:`Deferred Expense` report shows the balance of the :guilabel:`Prepayments` accounts at
a given date. To access it, go to :menuselection:`Accounting --> Reporting --> Dynamic Reports -->
Deferred Expense`.

.. screenshot:: accounting-deferred-expenses-report
   :menu: Accounting ‣ Reporting ‣ Dynamic Reports ‣ Deferred Expense
   :shows: Interactive "Deferred Expense" report listing the prepayment accounts and their balances at the selected date, with the date and journal filters.
   :data: Demo company "YourCompany HU" with a prepaid insurance bill.
   :module: account_dynamic_reports
   :notes: English UI, light theme, 1440px width.

.. seealso::
   - :doc:`assets`
   - :doc:`../customer_invoices/deferred_revenues`

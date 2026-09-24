=================
Deferred revenues
=================

**Deferred revenues**, or **unearned revenues**, are invoices addressed to customers
for goods yet to be delivered or services yet to be rendered.

The company cannot report them on the current **profit and loss statement**, or *income statement*,
since the goods and services will be effectively delivered/rendered in the future.

These future revenues must be deferred on the company's balance sheet among the current liabilities
until they can be **recognized**, at once or over a defined period, on the profit and loss
statement.

For example, let's say a business sells a software license of $1200 for 1 year. They immediately
invoice it to the customer but can't consider it earned yet, as the future months of licensing have
not yet been delivered. Therefore, they post this new revenue in a deferred revenue account and
recognize it on a monthly basis. Each month, for the next 12 months, $100 will be recognized as
revenue.

Deferred revenue account
========================

Deferred revenues are recorded on an account of type :guilabel:`Current Liabilities` (see
:ref:`account types <chart-of-account/type>`). Make sure such an account exists in your
:doc:`chart of accounts <../get_started/chart_of_accounts>`.

To defer a revenue, select the deferred revenue account on the customer invoice line (or set it as
the income account of the product or product category) instead of the income account.

.. _customer_invoices/deferred/recognition:

Recognizing deferred revenues
=============================

At the end of each period (e.g., every month), recognize the earned part of the revenue with a
miscellaneous journal entry:

#. Go to :menuselection:`Accounting --> Accounting --> Journal Entries` and click :guilabel:`New`.
#. Select a miscellaneous journal and the accounting :guilabel:`Date`.
#. Add a line debiting the deferred revenue account and a line crediting the income account with
   the amount to recognize (e.g., $100).
#. Click :guilabel:`Post`.

.. tip::
   To speed up the monthly entries, duplicate the previous recognition entry (:icon:`fa-cog`
   :guilabel:`Actions` → :guilabel:`Duplicate`) and change its date.

.. screenshot:: accounting-deferred-revenues-recognition-entry
   :menu: Accounting ‣ Accounting ‣ Journal Entries ‣ New
   :shows: Miscellaneous journal entry with two lines: debit "Deferred revenue" 100, credit "Software licenses" income 100.
   :highlight: The two journal items (red frame).
   :data: Demo company "YourCompany HU"; deferred revenue account of type Current Liabilities.
   :module: account
   :notes: English UI, light theme, 1440px width.

.. _customer_invoices/deferred/report:

Deferred revenue report
=======================

The :guilabel:`Deferred Revenue` report shows the balance of the :guilabel:`Current Liabilities`
accounts at a given date, including the deferred revenue accounts. To access it, go to
:menuselection:`Accounting --> Reporting --> Dynamic Reports --> Deferred Revenue`.

.. screenshot:: accounting-deferred-revenues-report
   :menu: Accounting ‣ Reporting ‣ Dynamic Reports ‣ Deferred Revenue
   :shows: Interactive "Deferred Revenue" report listing the current liability accounts and their balances at the selected date, with the date and journal filters.
   :data: Demo company "YourCompany HU" with a deferred software license invoice.
   :module: account_dynamic_reports
   :notes: English UI, light theme, 1440px width.

.. seealso::
   - :doc:`../vendor_bills/deferred_expenses`
   - :doc:`../customer_invoices`

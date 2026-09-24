============================
Tax return (VAT declaration)
============================

Companies with a registered :abbr:`VAT (Value Added Tax)` number must submit a **tax return** on
a monthly or quarterly basis, depending on their turnover and the registration regulation. A tax
return - or VAT return - gives the tax authorities information about the taxable transactions made
by the company. The **output tax** is charged on the number of goods and services sold by a
business, while the **input tax** is the tax added to the price when goods or services are
purchased. Based on these values, the company can calculate the tax amount they have to pay or be
refunded.

.. note::
   You can find additional information about VAT and its mechanism on this page from the European
   Commission: `"What is VAT?" <https://ec.europa.eu/taxation_customs/business/vat/what-is-vat_en>`_.

.. _tax-returns/prerequisites:

Prerequisites
=============

.. _tax-returns/tax-grids:

Tax Grids
---------

Odoo generates tax reports based on the :guilabel:`Tax Grids` settings that are configured on your
taxes. Therefore, it is crucial to make sure that all recorded transactions use the right taxes.
You can see the :guilabel:`Tax Grids` by opening the :guilabel:`Journal Items` tab of any
invoice and bill.

.. screenshot:: accounting-tax-returns-grids
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (an invoice) ‣ Journal Items
   :shows: The Journal Items tab of a posted invoice with the "Tax Grids" column showing the grids
      the tax lines feed.
   :highlight: The "Tax Grids" column (red frame).
   :data: An invoice with a 27% VAT line feeding two grids.
   :module: account
   :notes: English UI, light theme, crop to the tab.

To configure your tax grids, go to :menuselection:`Accounting --> Configuration --> Taxes`,
and open the tax you want to modify. There, you can edit your tax settings, along with the tax
grids that are used to record invoices or refunds.

.. note::
   Taxes and reports are usually already pre-configured in Odoo: a :ref:`fiscal localization package
   <fiscal_localizations/packages>` is installed according to the country you select at the creation
   of your database.

.. _tax-returns/close:

Close a tax period
==================

.. _tax-returns/lock-date:

Tax lock date
-------------

Any new transaction whose accounting date is prior to the :guilabel:`Tax Return Lock Date` has its tax
values moved to the next open tax period. This is useful to make sure that no change can be made to
a report once its period is closed.

Therefore, we recommend locking your tax date before working on your closing entry. This way, other
users cannot modify or add transactions that would have an impact on it, which can help you avoid
some tax declaration errors.

To check the current tax lock date, or to edit it, go to :menuselection:`Accounting --> Accounting
--> Lock Dates` and set :guilabel:`Tax Return Lock Date` under :guilabel:`Management Closing`.

.. seealso::
   :ref:`Lock dates <year-end/lock-dates>`

.. _tax-returns/report:

Tax return
----------

Once all the transactions involving taxes have been posted for the period you want to report, open
the :guilabel:`Tax Report` by going to :menuselection:`Accounting --> Reporting --> Dynamic Reports
--> Tax Report`, and set the :guilabel:`Date Range` to the period you want to declare. The report
shows the :guilabel:`NET` and :guilabel:`TAX` amounts per tax, grouped by
:guilabel:`Sales`/:guilabel:`Purchases`, and includes all the values to report to the tax
authorities, along with the amount to be paid or refunded.

Export it with the :guilabel:`PDF` or :guilabel:`XLSX` button to keep the document that supports the
declaration. A printable version is also available under :menuselection:`Accounting --> Reporting
--> Audit Reports --> Tax Report`.

.. seealso::
   :doc:`dynamic_reports`

.. _tax-returns/closing-entry:

Closing entry
-------------

The entry that moves the VAT balances to the tax payable or receivable account is recorded manually:
create a journal entry in your miscellaneous journal (:menuselection:`Accounting --> Accounting -->
Journal Entries --> New`) that offsets the balances of the VAT accounts shown by the tax report, and
post it at the last date of the period.

.. tip::
   Set the :ref:`tax lock date <tax-returns/lock-date>` before posting the closing entry, and check
   the VAT account balances on the :ref:`Trial Balance <accounting/reporting/trial-balance>`
   afterwards: they should be zero for the closed period.

.. seealso::
   * :doc:`../taxes`
   * :doc:`../get_started`
   * :doc:`../../fiscal_localizations`

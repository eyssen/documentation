=============
United States
=============

.. |GAAP| replace:: :abbr:`GAAP (Generally Acceptable Accounting Practices)`
.. |FASB| replace:: :abbr:`FASB (Financial Accounting Standards Board)`
.. |SEC| replace:: :abbr:`SEC (Securities and Exchange Commission)`
.. |COA| replace:: :abbr:`CoA (Chart of Accounts)`
.. |AR| replace:: :abbr:`AR (Accounts Receivable)`
.. |AP| replace:: :abbr:`AP (Accounts Payable)`
.. |CFS| replace:: :abbr:`CFS (Cash Flow Statement)`
.. |NACHA| replace:: :abbr:`NACHA (National Automated Clearing House Association)`
.. |ACH| replace:: :abbr:`ACH (Automated Clearing House)`

The Odoo fiscal localization package for the United States follows the Generally Acceptable
Accounting Principles (GAAP) accounting standards and rules used to prepare financial statements,
as outlined by the Financial Accounting Standards Board (FASB) and adopted by the Securities and
Exchange Commission (SEC).

.. seealso::
   - `Financial Accounting Standards Board (FASB) <https://asc.fasb.org/Home>`_
   - `Securities and Exchange Commission (SEC) <https://www.sec.gov/>`_

Configuration
=============

Below are the available modules in Odoo for accounting use in the United States.

.. note::
   The modules listed below are either for reference only or are optional, as the core requirements
   to operate under the US fiscal localization in Odoo are already included under the default
   package that came installed during database initialization.

   Verify the default package is in use by navigating to :menuselection:`Accounting App -->
   Settings` and under the :guilabel:`Fiscal Localization` section at the top, look for the `Generic
   Chart Template` selection to be listed next to the :guilabel:`Package` field label. This chart
   template includes the necessary settings for the US localization for the Odoo *Accounting* app.

   .. screenshot:: finance-fl-united-states-us-l10n-generic-chart-template
      :menu: Accounting ‣ Configuration ‣ Settings ‣ Fiscal Localization
      :shows: The "Fiscal Localization" block of the Accounting settings with the "Package" field showing "Generic Chart Template".
      :highlight: The "Package" field.
      :data: Demo company "YourCompany US".
      :module: l10n_us, account
      :notes: English UI, light theme, 1440px width.

Modules installation
--------------------

:ref:`Install <general/install>` the following modules to get all the features of the United States
localization:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`United States - Accounting`
     - `l10n_us`
     - Base accounting module for United States localization.

.. note::
   The US accounting reports (including the Check Register and the 1099 report), the US check
   layouts, the NACHA payment files, the AvaTax integration and the US payroll (with the ADP
   export) are **not** available in this edition. The generic :doc:`financial reports
   <../accounting/reporting>` (including the :ref:`cash flow statement
   <accounting/reporting/cash-flow-statement>`) and the generic :doc:`check printing
   <../accounting/payments/pay_checks>` layouts can be used instead.

.. _l10n_us/coa:

Chart of accounts
=================

The :doc:`chart of accounts (COA) <../accounting/get_started/chart_of_accounts>` for the United
States localization, in Odoo, follows the standard |GAAP| structure, with accounts grouped into
seven main categories, with corresponding numeric values that prefix individual journal entries:

- **Receivable**: the balance of money (or credit) due to the business for goods or services
  delivered or used, but not yet paid for by customers. |AR| is indicated by the journal code
  labeled (or beginning) with :guilabel:`1`.
- **Payable**: the business's short-term obligations owed to its creditors or suppliers, which have
  not yet been paid. |AP| is indicated by the journal code labeled (or beginning) with
  :guilabel:`2`.
- **Equity**: the amount of money that would be returned to a company's shareholders if all of the
  assets were liquidated and all of the company's debt was paid off in the case of liquidation.
  Equity is indicated by the journal code labeled (or beginning) with :guilabel:`3` or
  :guilabel:`9`.
- **Assets**: items listed on the balance sheet that contains economic value or have the ability to
  generate cash flows in the future, such as a piece of machinery, a financial security, or a
  patent. Assets are indicated by the journal code labeled (or beginning) with :guilabel:`1`.
- **Liability**: refers to a company's financial debts or obligations that arise during the course
  of business operations. Liabilities are indicated by the journal code labeled (or beginning) with
  :guilabel:`2`.
- **Income**: synonymous with *net income*, this is the profit a company retains after paying off
  all relevant expenses from sales revenue earned. Income is indicated by the journal code labeled
  (or beginning) with :guilabel:`4` or :guilabel:`6`.
- **Expenses**: the cost of operations that a company incurs to generate revenue. Expenses are
  indicated by the journal code labeled (or beginning) with a :guilabel:`6`.

.. tip::
   Predefined accounts are included in Odoo, as part of the |CoA| that's installed with the US
   localization package. The accounts listed below are preconfigured to perform certain operations
   within Odoo. It is recommended to **not** delete these accounts; however, if changes are needed,
   rename the accounts instead.

   .. list-table::
     :header-rows: 1
     :stub-columns: 1

     * - :guilabel:`Type`
       - :guilabel:`Account Name`
     * - :guilabel:`Current Assets`
       - | :guilabel:`Bank Suspense Account`
         | :guilabel:`Outstanding Receipts`
         | :guilabel:`Outstanding Payments`
         | :guilabel:`Liquidity Transfer`
         | :guilabel:`Stock Valuation`
         | :guilabel:`Stock Interim (Received)`
         | :guilabel:`Stock Interim (Delivered)`
         | :guilabel:`Cost of Production`
     * - :guilabel:`Income`
       - | :guilabel:`Foreign Exchange Gain`
         | :guilabel:`Cash Difference Gain`
         | :guilabel:`Cash Discount Gain`
     * - :guilabel:`Expenses`
       - | :guilabel:`Cash Discount Loss`
         | :guilabel:`Foreign Exchange Loss`
         | :guilabel:`Cash Difference Loss`
     * - :guilabel:`Current Year Earnings`
       - :guilabel:`Undistributed Profits/Losses`
     * - :guilabel:`Receivable`
       - :guilabel:`Account Receivable`
     * - :guilabel:`Payable`
       - :guilabel:`Account Payable`

.. seealso::
   - :doc:`../accounting/get_started/chart_of_accounts`
   - :doc:`../accounting/get_started/cheat_sheet`

View, edit, and sort accounts
-----------------------------

Access the *Chart of Accounts* dashboard in Odoo by navigating to :menuselection:`Accounting app
--> Configuration --> Accounting: Chart of Accounts`.

From the :guilabel:`Chart of Accounts` dashboard, create new accounts by clicking the
:guilabel:`New` button in the top-left corner of the dashboard and :ref:`filling in the
corresponding form <chart-of-account/create>`. Search and sort through existing accounts by using
specific :guilabel:`Filters` and :guilabel:`Group By` criteria, which are available in the search
drop-down menu.

To filter accounts by category, click the :icon:`fa-caret-down` :guilabel:`(caret down)` icon to
access the drop-down menu and look under the :guilabel:`Filters` column for individual selections.
Clicking on a specific category will only show accounts that match that particular filter.

To view all the available account types, remove all of the filters in the search bar, and then click
the :icon:`fa-caret-down` :guilabel:`(caret down)` icon to access the drop-down menu. From there,
select :guilabel:`Account Type` under the :guilabel:`Group By` column heading to list all of the
account types in the table.

.. screenshot:: finance-fl-united-states-us-l10n-coa-account-types
   :menu: Accounting ‣ Configuration ‣ Chart of Accounts ‣ Group By ‣ Account Type
   :shows: The Chart of Accounts list grouped by "Account Type" (Receivable, Bank and Cash, Current Assets, … Income, Expenses) with the groups collapsed.
   :highlight: The group headers.
   :data: Demo company "YourCompany US", generic chart template.
   :module: account
   :notes: English UI, light theme, 1440px width.

Besides structure, there are other key differences in the chart of accounts in the United States,
compared to other countries:

- **Specificity**: US |GAAP| often requires more detailed accounts compared to some other countries.
  This can include separate accounts for various types of revenue, expenses, and assets, providing
  more granular information in financial reports.
- **Regulatory Requirements**: In the United States, there are specific regulatory requirements set
  by bodies such as the |SEC| for publicly traded companies. These requirements may influence the
  structure and content of the |COA| to ensure compliance with reporting standards.
- **Industry Practices**: Certain industries in the United States may have unique accounting
  requirements or specialized |COA| structures. For example, financial institutions often have
  specific accounts related to loans, investments, and interest income.
- **Tax Considerations**: The |COA| may also reflect tax considerations, such as accounts for
  deductible expenses, deferred tax assets, and liabilities, to ensure compliance with tax laws and
  facilitate tax reporting.

These differences, ultimately, should be reflected in the |COA| structure itself, with the addition
of new accounts, as needed, in order to meet the demands of US accounting reporting requirements.

.. seealso::
   - :ref:`Create a new account <chart-of-account/create>`
   - :doc:`../../essentials/search`

.. _l10n_us/taxes:

Taxes
=====

In the United States, tax rates and what is considered taxable vary by jurisdiction. Default *Sales*
and *Purchase* taxes are created automatically when the Odoo *Accounting* application is installed.
To manage existing or configure additional taxes, navigate to :menuselection:`Accounting -->
Configuration --> Taxes`.

.. _l10n_us/cash-discount:

Cash discount
=============

Cash discounts can be configured from :menuselection:`Accounting app --> Payment Terms`. Each
payment term can be set up with a cash discount and reduced tax.

.. seealso::
   :doc:`../accounting/customer_invoices/cash_discounts`

.. _l10n_us/ach-electronic-transfers:

ACH - electronic transfers
==========================

Automated Clearing House (ACH) payments are a modern way to transfer funds electronically between
bank accounts, replacing traditional paper-based methods. |ACH| payments are commonly used for
direct deposits, bill payments, and business transactions.

Receive ACH payments: payment provider integration
--------------------------------------------------

|ACH| payments are supported by *Authorize.net* and *Stripe* payment integrations in Odoo.

.. seealso::
   - :ref:`Setting up Authorize.net for ACH payments (Odoo) <authorize/ach_payments>`
   - `Authorize.net's ACH payment processing for small businesses documentation
     <https://www.authorize.net/resources/blog/2021/ach-payments-for-small-businesses.html>`_
   - :doc:`Setting up Stripe for ACH payments (Odoo) <../payment_providers/stripe>`
   - `Stripe's ACH Direct Debit documentation <https://docs.stripe.com/payments/ach-debit>`_

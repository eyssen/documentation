====================
United Arab Emirates
====================

.. _uae/installation:

Installation
============

:ref:`Install <general/install>` the following modules to get all the features of the **United Arab
Emirates** localization:

.. list-table::
   :header-rows: 1

   * - Name
     - Technical name
     - Description
   * - :guilabel:`United Arab Emirates - Accounting`
     - ``l10n_ae``
     - Default :doc:`fiscal localization package </applications/finance/fiscal_localizations>`.
       Includes all accounts and taxes.
   * - :guilabel:`Gulf Cooperation Council - Point of Sale`
     - ``l10n_gcc_pos``
     - Includes the GCC-compliant bilingual (English/Arabic) POS receipt; installed automatically
       with the Point of Sale app.

.. note::
   The U.A.E. payroll (salary rules, end of service provision), the corporate tax report and the
   localized accounting reports are **not** available in this edition.

Chart of accounts
=================

Go to :menuselection:`Accounting --> Configuration --> Chart of Accounts` to view all default
accounts available for the UAE localization package. You can filter by :guilabel:`Code` using the
numbers on the far left or by clicking on :menuselection:`Group By --> Account Type`. You can
:guilabel:`Enable`/:guilabel:`Disable` reconciliation or **configure** specific accounts according
to your needs.

.. important::
   - Always keep at least one **receivable account** and one **payable account** active.
   - It is also advised to **keep the accounts below active**, as they are used either as transitory
     accounts by Odoo or are specific to the **UAE localization package**.

     .. list-table::
        :header-rows: 1

        * - Code
          - Account Name
          - Type
        * - 102011
          - Accounts Receivable
          - Receivable
        * - 102012
          - Accounts Receivable (POS)
          - Receivable
        * - 201002
          - Payables
          - Payable
        * - 101004
          - Bank
          - Bank and Cash
        * - 105001
          - Cash
          - Bank and Cash
        * - 100001
          - Liquidity Transfer
          - Current Assets
        * - 101002
          - Outstanding Receipts
          - Current Assets
        * - 101003
          - Outstanding Payments
          - Current Assets
        * - 104041
          - VAT Input
          - Current Assets
        * - 100103
          - VAT Receivable
          - Non-current Assets
        * - 101001
          - Bank Suspense Account
          - Current Liabilities
        * - 201017
          - VAT Output
          - Current Liabilities
        * - 202001
          - End of Service Provision
          - Current Liabilities
        * - 202003
          - VAT Payable
          - Non-current Liabilities
        * - 999999
          - Undistributed Profits/Losses
          - Current Year Earnings
        * - 400003
          - Basic Salary
          - Expenses
        * - 400004
          - Housing Allowance
          - Expenses
        * - 400005
          - Transportation Allowance
          - Expenses
        * - 400008
          - End of Service Indemnity
          - Expenses

Taxes
=====

To access your taxes, go to :menuselection:`Accounting --> Configuration --> Taxes`.
Activate/deactivate, or :doc:`configure </applications/finance/accounting/taxes>` the
taxes relevant to your business by clicking on them. Remember to only set tax accounts on the **5%**
tax group, as other groups do not need closing. To do so, enable the :doc:`developer mode
<../../general/developer_mode>` and go to :menuselection:`Configuration --> Tax Groups`. Then, set a
:guilabel:`Tax current account (payable)`, :guilabel:`Tax current account (receivable)`, and an
:guilabel:`Advance Tax payment account` for the **5%** group.

.. note::
   The :abbr:`RCM (Reverse Charge Mechanism)` is supported by Odoo.

.. screenshot:: finance-fl-uae-taxes
   :menu: Accounting ‣ Configuration ‣ Taxes
   :shows: The Taxes list of the U.A.E. localization: the 5% sales and purchase VAT taxes, the 0% and exempt taxes and the reverse-charge (RCM) taxes, with the Tax Type and Active columns.
   :data: Demo company "YourCompany AE", U.A.E. localization installed.
   :module: l10n_ae
   :notes: English UI, light theme, 1440px width.

Currency exchange rates
=======================

Currency rates can be updated automatically with the *eYssen currency rate updater* module (see
:ref:`multi-currency/config-rates-auto`). The UAE Central Bank exchange rates web service is one of
its providers: in :menuselection:`Accounting --> Configuration --> Settings --> Currencies`, select
it as :guilabel:`Provider`, choose the :guilabel:`Interval Unit`, and click the update button
(:icon:`fa-refresh`) to fetch the rates immediately.

Invoices
--------

The UAE localization package allows the generation of invoices in English, Arabic, or both. The
localization also includes a line to display the **VAT amount** per line.

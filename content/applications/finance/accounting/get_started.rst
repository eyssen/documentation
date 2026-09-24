:show-content:

===========
Get started
===========

When you first open the Accounting app, the accounting dashboard (:menuselection:`Accounting --> Dashboard`) welcomes you with a
step-by-step onboarding banner that helps you get started. The banner is displayed as long as no
entry has been recorded in the journals, and until you close it.

The settings visible in the onboarding banner can still be modified later by going to
:menuselection:`Accounting --> Configuration --> Settings`.

.. note::
   - Odoo automatically installs the appropriate **Fiscal Localization Package** for your company,
     according to the country selected at the creation of the database. This way, the right
     accounts, reports, and taxes are ready-to-go. :ref:`Click here <fiscal_localizations/packages>`
     for more information about Fiscal Localization Packages.
   - The full accounting features described in this documentation (journals, ledgers, financial
     reports, assets, budgets, lock dates, etc.) are provided by the *Odoo 18 Accounting Community*
     (`om_account_accountant`) and *eYssen Accountant* (`eyssen_accountant`) modules. When they are
     installed, the app is displayed as **Accounting** instead of **Invoicing**.

Accounting onboarding banner
============================

The step-by-step Accounting onboarding banner is composed of three steps:

.. screenshot:: accounting-get-started-onboarding-banner
   :menu: Accounting ‣ Dashboard
   :shows: Accounting dashboard of a new database with the onboarding banner and its three steps: "Set Company Data", "Set Periods", "Review Chart of Accounts".
   :highlight: The onboarding banner (red frame).
   :data: New demo company "YourCompany HU" without any journal entry.
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the banner.

#. :ref:`invoicing-setup-company`
#. :ref:`accounting-setup-periods`
#. :ref:`accounting-setup-chart`

.. _invoicing-setup-company:

Company Data
------------

Add your company's details, such as the name, address, logo, website, phone number, email address,
and Tax ID or VAT number. These details are then displayed on your documents, such as invoices.

.. note::
   You can also change the company's details by going to :menuselection:`Settings --> General
   Settings`, scrolling down to the :guilabel:`Companies` section, and :guilabel:`Update Info`.

.. _accounting-setup-periods:

Accounting Periods
------------------

Define the :guilabel:`Opening Date` of your accounting and the :guilabel:`Fiscal Year End` (last
day and month of the fiscal year), which are used to generate reports automatically.

By default, the fiscal year ends on the 31st of December, as this is the most common use.

.. note::
   You can also change the end of the fiscal year by going to :menuselection:`Accounting -->
   Configuration --> Settings`, in the :guilabel:`Fiscal Year` part of the :guilabel:`Fiscal
   Periods` section (:guilabel:`Last Day` field).

.. _accounting-setup-fiscal-years:

Fiscal years
~~~~~~~~~~~~

If a fiscal year is longer or shorter than one calendar year (e.g., the first year of a company),
enable :guilabel:`Fiscal Years` in the :guilabel:`Fiscal Periods` section of the settings, then go
to :menuselection:`Accounting --> Configuration --> Fiscal Year` and create the fiscal year with its
:guilabel:`Start Date` and :guilabel:`End Date`. The reports use these dates to compute the fiscal
year's results.

.. screenshot:: accounting-get-started-fiscal-periods-settings
   :menu: Accounting ‣ Configuration ‣ Settings
   :shows: "Fiscal Periods" section with the "Fiscal Year" block ("Last Day": December 31) and the "Fiscal Years" option enabled with its "Fiscal Years" link button.
   :highlight: The "Fiscal Periods" section (red frame).
   :data: Demo company "YourCompany HU".
   :module: account, om_fiscal_year
   :notes: English UI, light theme, 1440px width, crop to the section.

.. note::
   This feature is provided by the *Odoo 18 Fiscal Year & Lock Date* (`om_fiscal_year`) module,
   which also adds the :menuselection:`Accounting --> Accounting --> Lock Dates` menu.

.. _accounting-setup-chart:

Chart of Accounts
-----------------

With this step, you can add accounts to your **Chart of Accounts** and indicate their initial
opening balances (:guilabel:`Opening Debit` and :guilabel:`Opening Credit` columns).

Basic settings are displayed on this page to help you review your Chart of Accounts. To access all
the settings of an account, open the account line.

.. screenshot:: accounting-get-started-setup-chart-of-accounts
   :menu: Accounting ‣ Dashboard ‣ onboarding banner ‣ Review Chart of Accounts
   :shows: Editable list of accounts with the Code, Account Name, Type, Allow Reconciliation, Opening Debit and Opening Credit columns; a few opening balances filled in.
   :highlight: The "Opening Debit" and "Opening Credit" columns (red frame).
   :data: Demo company "YourCompany HU" with the Hungarian chart of accounts.
   :module: account
   :notes: English UI, light theme, 1440px width.

.. note::
   :doc:`Click here <get_started/chart_of_accounts>` for more information on how to configure your
   Chart of Accounts.

Other initial settings
======================

.. _accounting-setup-bank:

Bank Account
------------

To add a bank account, go to :menuselection:`Accounting --> Configuration --> Add a Bank Account`
and fill out the form:

- :guilabel:`Account Number`: your bank account number (IBAN in Europe).
- :guilabel:`Bank`: select or create the bank institution.
- :guilabel:`Bank Identifier Code`: the bank's BIC or SWIFT code.
- :guilabel:`Journal`: this field is displayed if you have an existing bank journal that is not
  linked yet to a bank account. If so, select the journal you want to use to record the financial
  transactions linked to this bank account. Leave it empty to create a new bank journal.

.. note::
   :doc:`Click here <bank>` for more information about bank accounts and the import or
   synchronization of bank statements.

.. _accounting-setup-taxes:

Taxes
-----

Go to :menuselection:`Accounting --> Configuration --> Taxes` to create new taxes, (de)activate, or
modify existing taxes. Depending on the :doc:`localization package <../fiscal_localizations>`
installed on your database, taxes required for your country are already configured.

.. note::
   :doc:`Click here <taxes>` for more information about taxes.

.. _invoicing-setup-layout:

Documents Layout
----------------

To customize the default invoice layout, go to :menuselection:`Settings --> General Settings`,
scroll down to the :guilabel:`Companies` section, and click :guilabel:`Configure Document Layout`.

.. tip::
   Add your **bank account number** and a link to your **General Terms & Conditions** in the
   footer. This way, your contacts can find the full content of your GT&C online without having to
   print them on the invoices you issue.

.. _invoicing-setup-invoice:

Create Invoice
--------------

Create your first invoice from :menuselection:`Accounting --> Customers --> Invoices`. See
:doc:`customer_invoices` for more information.

.. _invoicing-setup-payments:

Online Payments
---------------

To let your customers pay their invoices online, go to :menuselection:`Accounting --> Configuration
--> Online Payments --> Payment Providers` and :doc:`enable the desired providers <../payment_providers>`.

.. seealso::
   * :doc:`bank`
   * :doc:`get_started/chart_of_accounts`
   * :doc:`get_started/consolidation`
   * :doc:`bank/bank_synchronization`
   * :doc:`../fiscal_localizations`

.. toctree::
   :titlesonly:

   get_started/cheat_sheet
   get_started/chart_of_accounts
   get_started/consolidation
   get_started/journals
   get_started/multi_currency
   get_started/avg_price_valuation

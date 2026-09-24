=============
Consolidation
=============

Consolidation allows combining financial data from **multiple separate companies**, each with its
own books, into a unified view, providing a "fair image" of the entire group's financial health.

It helps create a clear, comprehensive view of the group's financial performance by combining data
from multiple companies.

.. note::
   Consolidating companies involves **legally separate entities**, whereas :ref:`branches
   <general/companies/branches>` are **subdivisions** of a single legal entity which often share the
   head office's resources (journals, taxes, accounts, fiscal positions) and are not consolidated in
   the same way.

.. _consolidation_tools:

Consolidation tools
===================

**Several tools** combined together will contribute to the construction of the financial
consolidation:

.. _consolidation_account_mapping:

#. **Account Mapping:** Similar accounts from different companies can be mapped together. To map
   accounts, go to :menuselection:`Accounting --> Configuration --> Chart of Accounts` and open the
   account. In the :guilabel:`Mapping` tab, enter a code in the corresponding company
   :guilabel:`Code` column to map the account.

   .. screenshot:: accounting-consolidation-account-mapping
      :menu: Accounting ‣ Configuration ‣ Chart of Accounts ‣ (open a shared account) ‣ Mapping tab
      :shows: "Mapping" tab of a shared account listing each company with its own "Code".
      :highlight: The company / code lines (red frame).
      :data: Two demo companies "YourCompany HU" and "YourCompany AT" sharing the account "Income".
      :module: account
      :notes: English UI, light theme, 1440px width; the tab is only visible in multi-company databases.

   .. note:: :ref:`Import mapping <consolidation_import_account_mapping>` or merge existing
      accounts using the :ref:`merging tool <consolidation_merge_tool>` can simplify the process.

   .. _consolidation_multi_ledgers:

#. **Multi-Ledgers:** Ledgers are fundamental to the process of consolidation. They are either:

   - *Regular Ledgers:* Each company in the consolidation scope has its own standard accounting
     ledger where all the regular day-to-day transactions are recorded. It excludes the company's
     consolidation adjustment journals.

   - *Multi-Ledger for Consolidation:* The company doing the actual consolidation also has a
     special multi-ledger. This one includes all the other companies' consolidation adjustments
     journals (the ones excluded from their own ledgers). This allows for viewing the total impact
     of all the adjustments.

   To create a new ledger, go to :menuselection:`Accounting --> Configuration --> Multi-Ledger`
   and click :guilabel:`New`. Enter a name, pick the company the ledger is linked to and, most
   importantly, determine which journals are to be excluded from the ledger.

   .. _consolidation_company_selector:

#. **Multi-Company Selector:** The consolidated view can be accessed using the multi-company
   selector. Selecting the consolidating company as the current company and making the other
   companies visible in the selector, all the journal items are displayed from the consolidating
   company's perspective.

   .. screenshot:: accounting-consolidation-company-selector
      :menu: (top bar) ‣ company selector
      :shows: Company selector dropdown opened; the parent company is the current company and the subsidiaries are also checked.
      :highlight: The checked companies (red frame).
      :data: Demo companies "YourCompany HU" (parent) and "YourCompany AT" (subsidiary).
      :module: base
      :notes: English UI, light theme, crop to the top-right corner.

.. _consolidation_merge_tool:

Account merging
===============

Accounts can be merged to reduce the number of accounts and standardize them across companies. This
is optional; consolidation works without it.

To use the merge tool, select all the companies with an account that needs to be merged in the
company selector in the top right corner of the screen.

.. screenshot:: accounting-consolidation-merge-select-companies
   :menu: (top bar) ‣ company selector
   :shows: Company selector dropdown with all the companies that have accounts to merge checked.
   :highlight: The checked companies (red frame).
   :data: Demo companies "YourCompany HU" and "YourCompany AT".
   :module: base
   :notes: English UI, light theme, crop to the top-right corner.

Then, go to :menuselection:`Accounting --> Configuration --> Chart of Accounts` and select the
accounts to merge. Click the :icon:`fa-cog` :guilabel:`Actions` menu and select :guilabel:`Merge
accounts` (available to users with the :guilabel:`Advisor` access right).

In the :guilabel:`Merge accounts` window, enable the :guilabel:`Group by name?` option if needed,
select the accounts to merge in the list, and click :guilabel:`Merge`.

The selected accounts are then merged into a single shared account, accessible by all the chosen
companies, just as if the account had been directly created to be shared.

.. _consolidation_unmerge_tool:

Account unmerging
=================

Accounts can also be unmerged if needed.

.. warning::

   Note that unmerging accounts **will not unmerge the chatters** of the accounts. Once merged, the
   changes' histories are permanently merged.

To unmerge accounts, select a company with a shared account in the company selector at the top
right corner of the screen. Then, go to :menuselection:`Accounting --> Configuration --> Chart of
Accounts` and select the account to unmerge. Click the :icon:`fa-cog` :guilabel:`Actions` menu and
select :guilabel:`Unmerge account`.

A confirmation pop-up window will appear, listing how the accounts will be split.

.. screenshot:: accounting-consolidation-unmerge-confirmation
   :menu: Accounting ‣ Configuration ‣ Chart of Accounts ‣ (select a shared account) ‣ Actions ‣ Unmerge account
   :shows: Confirmation dialog listing, for each company, the new account that will be created, with the Unmerge and Cancel buttons.
   :highlight: The "Unmerge" button (red frame).
   :data: Shared account "Income" between "YourCompany HU" and "YourCompany AT".
   :module: account
   :notes: English UI, light theme, crop to the dialog.

Click :guilabel:`Unmerge`. A new account linked to each company will be created for the previously
shared account.

.. _consolidation_import_account_mapping:

Import a mapping
================

To **import an account mapping**, select all the related companies in the company selector at the
top right corner of the screen and go to :menuselection:`Accounting --> Configuration --> Chart of
Accounts`.

First, to choose the fields to export, select the accounts, click the :icon:`fa-cog`
:guilabel:`Actions` button and select :guilabel:`Export`. Then, in the :guilabel:`Export data`
window, add the :guilabel:`Code mapping/Code`, :guilabel:`Code Mapping/Company` and
:guilabel:`External ID` fields using the :icon:`fa-plus` icon and click :guilabel:`Export`. No other
field is required.

Second, rework it in a spreadsheet adding the desired code for each company on desired accounts.

Third, to reimport the file (xlsx or csv format) in Odoo, click the :icon:`fa-cog` icon next to
the view title, select :guilabel:`Import records`, click :guilabel:`Upload File`, select the file,
check the field mapping, and click :guilabel:`Import`.

Finally, the codes now take into account the mapping company per company.

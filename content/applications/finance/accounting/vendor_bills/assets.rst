===================================
Non-current assets and fixed assets
===================================

**Non-current Assets**, also known as **long-term assets**, are investments that are expected to be
realized after one year. They are capitalized rather than being expensed and appear on the company's
balance sheet. Depending on their nature, they may undergo **depreciation**.

**Fixed Assets** are a type of Non-current Assets and include the properties bought for their
productive aspects, such as buildings, vehicles, equipment, land, and software.

For example, let's say we buy a car for $ 27,000. We plan to amortize it over five years, and we
will sell it for $ 7,000 afterward. Using the linear, or straight-line, depreciation method,
$ 4,000 are expensed each year as **depreciation expenses**. After five years, the **Accumulated
Depreciation** amount reported on the balance sheet equals $ 20,000, leaving us with $ 7,000 of
**Not Depreciable Value**, or Salvage value.

Assets are managed by the *Odoo 18 Assets Management* (`om_account_asset`) module. For each asset,
Odoo computes a **depreciation board** and creates the depreciation entries periodically.

Odoo supports the following depreciation methods (:guilabel:`Computation Method`):

- :guilabel:`Linear`: the depreciation amount is the gross value divided by the number of
  depreciations.
- :guilabel:`Degressive`: the depreciation amount is the residual value multiplied by the
  :guilabel:`Degressive Factor`.

.. note::
   The Hungarian localization (*eYssen Hungarian Asset Localization*, `eyssen_l10n_hu_asset`) adds a
   :menuselection:`Accounting --> Fixed Assets` menu and Hungarian-specific asset features; see
   :doc:`../../fiscal_localizations/hungary/assets`.

.. _assets/categories:

Asset categories
================

Asset categories define how the assets are recorded and depreciated. To create one, go to
:menuselection:`Accounting --> Configuration --> Management --> Asset Category` and click
:guilabel:`New`. Fill in the following fields:

- :guilabel:`Asset Type`: the name of the category (e.g., *Computers*).
- :guilabel:`Journal Entries` section:

  - :guilabel:`Journal`: the journal in which the depreciation entries are posted.
  - :guilabel:`Asset Account`: the account used to record the purchase of the asset at its
    original price.
  - :guilabel:`Depreciation Entries: Asset Account`: the account used in the depreciation entries
    to decrease the asset value (e.g., the accumulated depreciation account).
  - :guilabel:`Depreciation Entries: Expense Account`: the account used in the periodical entries
    to record a part of the asset as an expense.
  - :guilabel:`Analytic Account` / :guilabel:`Analytic Distribution`: the analytic distribution of
    the depreciation entries.

- :guilabel:`Periodicity` section:

  - :guilabel:`Time Method Based On`: :guilabel:`Number of Entries` (fixed number of depreciations
    and time between them) or :guilabel:`Ending Date` (time between depreciations and date after
    which no depreciation is computed).
  - :guilabel:`Number of Entries` or :guilabel:`Ending date`.
  - :guilabel:`One Entry Every`: the number of months between two depreciations.

- :guilabel:`Additional Options` section:

  - :guilabel:`Auto-Confirm Assets`: automatically confirms the assets created from vendor bills
    and posts their depreciation entries when they are generated. Otherwise, the depreciation
    entries are created as drafts.
  - :guilabel:`Group Journal Entries`: groups the depreciation entries of all the assets of the
    category into one journal entry per period.
  - :guilabel:`Depreciation Dates`: :guilabel:`Based on Last Day of Purchase Period` or
    :guilabel:`Manual (Defaulted on Purchase Date)`.

- :guilabel:`Depreciation Method` section: the :guilabel:`Computation Method`, the
  :guilabel:`Degressive Factor`, and the :guilabel:`Prorata Temporis` option.

.. screenshot:: accounting-assets-category-form
   :menu: Accounting ‣ Configuration ‣ Management ‣ Asset Category ‣ New
   :shows: Asset category form "Computers": Journal "Miscellaneous Operations", the three accounts, Periodicity (Number of Entries: 36, One Entry Every: 1 month), Additional Options (Auto-Confirm Assets ticked), Depreciation Method "Linear".
   :highlight: The "Journal Entries" and "Periodicity" sections (red frames).
   :data: Demo company "YourCompany HU" with the Hungarian chart of accounts.
   :module: om_account_asset
   :notes: English UI, light theme, 1440px width.

.. _assets/prorata:

What does "Prorata Temporis" mean?
----------------------------------

The :guilabel:`Prorata Temporis` option indicates that the first depreciation entry of the asset is
computed from the purchase date instead of the first day of the period. The first depreciation is
then reduced proportionally to the number of days remaining in the period.

.. note::
   The :guilabel:`Prorata Temporis` option is not available when the time method is based on an
   ending date.

.. _assets/from-bills:

Assets from vendor bills
========================

Assets can be created automatically when a vendor bill is confirmed:

- On the product form, in the :guilabel:`Accounting` tab, select an :guilabel:`Asset Type` (asset
  category). When the product is added to a vendor bill, the category is set on the bill line; or
- On the vendor bill, select the :guilabel:`Asset Category` directly on the invoice line. The
  line's account is replaced by the category's :guilabel:`Asset Account`.

When the bill is confirmed, an asset is created for each line with an asset category, with the
line's untaxed amount (in the company currency) as :guilabel:`Gross Value`. If the category has the
:guilabel:`Auto-Confirm Assets` option, the asset is confirmed immediately; otherwise, it is created
in :guilabel:`Draft` status.

.. note::
   - A vendor bill with a confirmed (running) asset cannot be reset to draft.
   - If the bill is reset to draft or cancelled, its draft assets are archived.

.. screenshot:: accounting-assets-bill-line
   :menu: Accounting ‣ Vendors ‣ Bills ‣ (open a draft bill)
   :shows: Draft vendor bill with one line for a laptop; the "Asset Category" column set to "Computers" and the account replaced by the asset account.
   :highlight: The "Asset Category" column (red frame).
   :data: Demo vendor; product "Laptop" (1,200,000 HUF); category "Computers".
   :module: om_account_asset
   :notes: English UI, light theme, 1440px width.

.. _assets/create:

Create an asset manually
========================

To create an asset manually, go to :menuselection:`Accounting --> Configuration --> Management -->
Assets` and click :guilabel:`New`. Fill in:

- :guilabel:`Asset Name`, :guilabel:`Asset Category`, :guilabel:`Reference`, and :guilabel:`Date`;
- :guilabel:`Depreciation Dates` (and the :guilabel:`First Depreciation Date` for manual dates);
- :guilabel:`Gross Value`: the purchase value of the asset;
- :guilabel:`Salvage Value`: the value that is not depreciated;
- :guilabel:`Vendor` and :guilabel:`Invoice`, if relevant.

The depreciation parameters are copied from the category and can be modified in the
:guilabel:`Depreciation Information` tab.

Click :guilabel:`Compute Depreciation` to (re)compute the :guilabel:`Depreciation Board`, then click
:guilabel:`Confirm` to start the depreciation. The asset status becomes :guilabel:`Running`.

.. screenshot:: accounting-assets-asset-form
   :menu: Accounting ‣ Configuration ‣ Management ‣ Assets ‣ (open a running asset)
   :shows: Running asset "Laptop" with the buttons (Compute Depreciation, Sell or Dispose, Set to Draft, Modify Depreciation), the "Items" smart button, Gross Value, Salvage Value, Residual Value, and the "Depreciation Board" tab with the depreciation lines (Depreciation Date, Depreciation, Cumulative Depreciation, Residual) and their posting indicators.
   :highlight: The "Depreciation Board" tab (red frame).
   :data: Asset "Laptop", 1,200,000 HUF, 36 monthly depreciations, first three lines posted.
   :module: om_account_asset
   :notes: English UI, light theme, 1440px width.

.. _assets/entries:

Depreciation entries
====================

The depreciation entries are created by a scheduled action once a month for all the running assets,
for the depreciation lines whose date has passed.

To create them manually, go to :menuselection:`Accounting --> Accounting --> Generate Entries -->
Generate Assets Entries`, select the :guilabel:`Date` until which the entries must be generated, and
click :guilabel:`Generate Entries`. A single depreciation line can also be posted from the
depreciation board.

The entries are posted automatically if the category has the :guilabel:`Auto-Confirm Assets`
option; otherwise, they are created as drafts and must be posted manually. When the residual value
of an asset reaches zero, the asset is closed.

Click the :guilabel:`Items` smart button of an asset to see its journal entries.

.. _assets/modify:

Modification of an asset
========================

To change the depreciation duration of a running asset, click :guilabel:`Modify Depreciation`. In
the :guilabel:`Modify Asset` window, enter the :guilabel:`Reason`, the new number of depreciations
(or the new ending date) and the period length, then click :guilabel:`Modify`. The unposted
depreciation lines are recomputed, and the change is logged in the chatter.

.. _assets/disposal:

Disposal of fixed assets
========================

To sell or dispose of an asset, open it and click :guilabel:`Sell or Dispose`. The unposted
depreciation lines are removed and replaced by a single depreciation line of the residual value,
dated today. The corresponding journal entry is created as a draft: review and post it. Once the
residual value is zero, the asset is closed.

.. tip::
   Record the sale itself with a customer invoice, as usual.

.. _assets/reporting:

Assets analysis
===============

To analyze your assets, go to :menuselection:`Accounting --> Reporting --> Management --> Assets`.
The :guilabel:`Assets Analysis` report is available in pivot and graph views and can be filtered by
status (e.g., :guilabel:`Draft`) and grouped by category or date.

.. screenshot:: accounting-assets-analysis
   :menu: Accounting ‣ Reporting ‣ Management ‣ Assets
   :shows: "Assets Analysis" pivot view grouped by asset category, with the gross, depreciated and residual amounts.
   :data: Demo company "YourCompany HU" with several running assets.
   :module: om_account_asset
   :notes: English UI, light theme, 1440px width.

.. seealso::
   - :doc:`deferred_expenses`
   - :doc:`../get_started/chart_of_accounts`

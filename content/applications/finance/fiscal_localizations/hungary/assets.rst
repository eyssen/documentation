======================
Hungarian fixed assets
======================

The :guilabel:`eYssen Hungarian Asset Localization` (`eyssen_l10n_hu_asset`) module extends the
:doc:`asset management <../../accounting/vendor_bills/assets>` of the Accounting app with the
Hungarian practice:

- rate-based linear depreciation according to the Accounting Act (*Szt.*), prorated by days from the
  activation date, and a :guilabel:`Lump Sum Depreciation` method;
- an informative depreciation board according to the Corporate Tax Act (*Tao.*), kept in parallel
  and never posted;
- an activation (commissioning) date with a draft activation journal entry;
- a :guilabel:`Dispose Asset` wizard for scrapping, sale and other withdrawals;
- inventory number, responsible employees, inventory location and other record-keeping fields;
- commissioning, increase, decrease and scrapping protocols.

The module adds the :menuselection:`Accounting --> Fixed Assets` menu with the entries
:guilabel:`Assets`, :guilabel:`Asset Categories`, :guilabel:`Post Depreciation` (administrators
only) and :guilabel:`Asset Analysis`. The standard asset menus remain available.

.. note::
   The Hungarian calculation applies to purchase-type assets whose :guilabel:`Computation Method` is
   :guilabel:`Lump Sum Depreciation`, or :guilabel:`Linear` with :guilabel:`Time Method Based On` set
   to :guilabel:`Number of Entries`, a depreciation rate greater than zero and a period length of 1,
   3, 6 or 12 months. Every other asset (degressive, ending-date based, or linear with a zero rate)
   keeps the standard behavior described in :doc:`../../accounting/vendor_bills/assets`.

Asset categories
================

Open :menuselection:`Accounting --> Fixed Assets --> Asset Categories`. In addition to the standard
fields:

- :guilabel:`Depreciation Rate (Accounting Act)`: the yearly depreciation rate, copied to the assets
  of the category. Enter it as a fraction (`0.2` means 20%, `0.145` means 14.5%);
- :guilabel:`Depreciation Rate (Corporate Tax Act)`: the yearly rate of the tax depreciation board
  (20% is used if it is empty);
- :guilabel:`Computation Method` gains the :guilabel:`Lump Sum Depreciation` option: the whole value
  is written off in one entry on the activation date (for example, for low-value assets);
- :guilabel:`Acquisition Account`: the construction-in-progress account (*beruházások*, e.g., `161`)
  credited by the activation entry. It is required to confirm an asset;
- :guilabel:`Disposal Expense Account`: the expense account (e.g., `86…`) that receives the net book
  value when an asset is disposed of. It is required to dispose of an asset;
- :guilabel:`Disposal Income Account`: informative; the sales revenue itself is booked by the
  customer invoice.

.. screenshot:: finance-fl-hungary-asset-category
   :menu: Accounting ‣ Fixed Assets ‣ Asset Categories ‣ (category)
   :shows: Asset category form with the "Depreciation Method" section ("Computation Method" = Linear, "Depreciation Rate (Accounting Act)" 0.20, "Depreciation Rate (Corporate Tax Act)" 0.20, period length 12 months) and the "Journal Entries" section with the "Acquisition Account", "Disposal Expense Account" and "Disposal Income Account" fields.
   :highlight: The two depreciation rate fields and the three Hungarian accounts (red frames).
   :data: Category "Office equipment", asset account 143, depreciation account 149, expense account 571, acquisition account 161.
   :module: eyssen_l10n_hu_asset
   :notes: English UI, light theme, 1440px width, crop to the form sheet.

Assets
======

On the asset form (:menuselection:`Accounting --> Fixed Assets --> Assets`):

- :guilabel:`Activation Date`: the day the asset was put into service. The activation entry and the
  depreciation board start from this date; it is mandatory to confirm the asset.
- In the :guilabel:`Depreciation Information` tab, the field labelled :guilabel:`Degressive Factor`
  holds the yearly **accounting depreciation rate** of linear assets (copied from the category), and
  :guilabel:`Depreciation Rate (Corporate Tax Act)` holds the tax rate. The :guilabel:`Number of
  Depreciations` is computed from the rate and the period length and is read-only.
- The :guilabel:`Special` tab contains the :guilabel:`Inventory Responsible` and the
  :guilabel:`Asset Responsibles` (employees), the :guilabel:`Inventory Number` (also shown in the
  name of the asset and searchable), a :guilabel:`QR Code` text, the :guilabel:`Inventory
  Warehouse`, an informative :guilabel:`Analytic Plan` and :guilabel:`Analytic Account`, the
  :guilabel:`Consumed Development Reserve` (*fejlesztési tartalék*, informative), and the
  :guilabel:`Opening Depreciated Amount` for assets taken over from another system with depreciation
  already booked.
- The :guilabel:`TAO Board` tab shows the yearly corporate tax depreciation: :guilabel:`Year`,
  :guilabel:`Depreciation Date`, :guilabel:`Current Depreciation`, :guilabel:`Cumulative
  Depreciation` and :guilabel:`Remaining Value`.

How the boards are computed
---------------------------

- **Accounting board**: the depreciation lines are dated at the **end** of each period (month,
  quarter, half-year or year) of the fiscal year. The amount of a full period is (gross value −
  salvage value) × rate × period length / 12. The first line is prorated by the actual calendar days
  from the activation date to the end of the period; the last line takes the remainder, so the board
  always ends at zero.

  .. example::
     Gross value 1,200,000 HUF, salvage value 200,000 HUF, rate 0.20, yearly periods, activated on
     15 April 2026: 143,014 HUF in 2026 (261 of 365 days), 200,000 HUF in each of the next four
     years, and the remaining 56,986 HUF in 2031.

- **TAO board**: yearly lines at the end of the fiscal year. The first year is prorated on a 360-day
  (12 × 30) basis from the activation date. The board is recomputed together with the accounting
  board and is never posted.
- The :guilabel:`Opening Depreciated Amount` reduces the residual value on both boards; lines that
  are fully covered by it are not generated.

Confirm and depreciate
----------------------

Click :guilabel:`Confirm`. For Hungarian assets, a **draft** journal entry *<asset name>:
Activation* is created on the journal of the category at the activation date, debiting the asset
account and crediting the :guilabel:`Acquisition Account` with the gross value. Review and post it
from the :guilabel:`Activation Journal Entry` link. Confirming does not post any depreciation: the
due lines are posted by the monthly scheduled action of the asset management or with
:menuselection:`Accounting --> Fixed Assets --> Post Depreciation`.

Several draft assets can be confirmed at once from the list view with :menuselection:`Action -->
Confirm Assets`.

.. warning::
   Do not enable :guilabel:`Auto-Confirm Assets` on categories that use the Hungarian calculation:
   assets created from vendor bills have no activation date, so the bill could not be posted.

To change the period length of a running asset, use :guilabel:`Modify Depreciation`; the number of
depreciations stays computed. The rate itself can only be changed while the asset is in draft.

Dispose of an asset
-------------------

The standard :guilabel:`Sell or Dispose` button is hidden on Hungarian assets. Click
:guilabel:`Dispose Asset` (available on running and on fully depreciated assets) and fill in the
:guilabel:`Disposal Date`, the :guilabel:`Disposal Type` (:guilabel:`Scrapping`, :guilabel:`Sale` or
:guilabel:`Other Withdrawal`) and the :guilabel:`Disposal Reason`. The wizard

#. removes the unposted depreciation lines and adds a catch-up line up to the disposal date, with a
   draft depreciation entry;
#. creates the draft entry *<asset name>: Disposal*: accumulated depreciation and
   :guilabel:`Disposal Expense Account` (net book value) on the debit side, the asset account (gross
   value) on the credit side;
#. closes the asset, fills in the :guilabel:`Disposal` section of the form and shortens the TAO
   board to the year of the disposal.

Both entries remain in draft for review. In case of a sale, the revenue is invoiced separately with
a customer invoice. A disposed asset cannot be reset to draft or confirmed again. The disposal date
cannot precede the activation date or the last posted depreciation, and cannot fall into a locked
period.

.. screenshot:: finance-fl-hungary-asset-dispose
   :menu: Accounting ‣ Fixed Assets ‣ Assets ‣ (running asset) ‣ Dispose Asset
   :shows: The "Dispose Asset" dialog with the read-only asset, "Disposal Date", "Disposal Type" set to "Sale" with the blue information box about invoicing the revenue separately, "Disposal Reason", and the "Dispose Asset" and "Cancel" buttons.
   :highlight: The "Disposal Type" field and the information box (red frame).
   :data: Asset "Laptop - LT-0012", disposal date today, reason "Sold to employee".
   :module: eyssen_l10n_hu_asset
   :notes: English UI, light theme, 1440px width, crop to the dialog.

Protocols
=========

The :guilabel:`Print` menu of the asset form and list contains four PDF protocols:
:guilabel:`Commissioning Protocol` (*üzembe helyezési jegyzőkönyv*), :guilabel:`Asset Increase
Protocol` (*állománynövekedési jegyzőkönyv*), :guilabel:`Asset Decrease Protocol`
(*állománycsökkenési jegyzőkönyv*) and :guilabel:`Scrapping Protocol` (*selejtezési jegyzőkönyv*).
The scrapping protocol shows the net value according to both the Accounting Act and the Corporate
Tax Act.

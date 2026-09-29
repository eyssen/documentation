====================
Spanish fixed assets
====================

The *Spain - Fixed Assets* module adds the Spanish depreciation rules to the :doc:`asset management
<../../accounting/vendor_bills/assets>` of the Accounting app:

- three Spanish depreciation methods on asset categories and assets: straight line over the useful
  life, fixed annual percentage (official coefficient tables) and declining balance;
- a depreciation start date, for assets that are put into use after their purchase date;
- depreciation periods that follow the calendar, with the first period prorated by days;
- the non-deductible VAT and the VAT prorata part of the vendor bill line included in the value of
  the assets created from vendor bills.

.. note::
   - The module is part of the :ref:`supported combination of Spanish modules
     <localizations/spain/module-choice>` and is installed with the :ref:`fiscal profile
     <localizations/spain/fiscal-profile>` when it is available on the server. It depends on the
     *Odoo 18 Assets Management* module and on *AEAT Base*.
   - The alternative community fixed asset modules (*Assets Management* and its Spanish version)
     cannot be installed together with it: Odoo refuses the installation, also from the command
     line.
   - The Spanish rules only apply to assets. Deferred revenues keep the standard depreciation
     engine.

Asset categories
================

Go to :menuselection:`Accounting --> Configuration --> Management --> Asset Category` and open or
create a category. In the depreciation settings of the category, select the :guilabel:`Spanish
Depreciation Method`:

- :guilabel:`Linear (useful life)`: the depreciable value is spread evenly over the useful life,
  which is the number of depreciations multiplied by the number of months between two
  depreciations.
- :guilabel:`Fixed annual percentage`: every year, the :guilabel:`Annual Depreciation Percentage`
  of the depreciable value is depreciated (use the percentage of the official depreciation
  coefficient tables).
- :guilabel:`Declining balance`: every year, the :guilabel:`Annual Depreciation Percentage` of the
  remaining value is depreciated. The remaining value is depreciated in full in the last period of
  the useful life.

Leave the :guilabel:`Spanish Depreciation Method` empty to use the standard depreciation engine
described in :doc:`../../accounting/vendor_bills/assets`. When a Spanish method is selected, the
standard :guilabel:`Computation Method`, :guilabel:`Degressive Factor` and :guilabel:`Prorata
Temporis` fields are hidden, as the Spanish method replaces them.

The :guilabel:`Annual Depreciation Percentage` is required for the fixed annual percentage and
the declining balance methods; it must be greater than 0 and at most 100.

With a Spanish method, the number of months between two depreciations (:guilabel:`One Entry
Every`) must be 1, 2, 3, 4, 6 or 12, so that the periods fit into a calendar year.

.. _localizations/spain/assets-period-end:

Depreciation periods
--------------------

The :guilabel:`Depreciate to Period End` option (enabled by default) determines how the
depreciation periods are counted:

- **Enabled**: the periods follow the calendar (month, quarter, half-year or fiscal year, according
  to the number of months between two depreciations). The first period is prorated by days from
  the depreciation start date, and every depreciation line is dated on the last day of its period.
- **Disabled**: the periods are counted from the depreciation start date and are never prorated.

.. screenshot:: finance-fl-spain-asset-category
   :menu: Accounting ‣ Configuration ‣ Management ‣ Asset Category ‣ (a category)
   :shows: An asset category form with "Spanish Depreciation Method" set to "Fixed annual percentage", the "Annual Depreciation Percentage" field (e.g., 25) and the "Depreciate to Period End" option enabled; the standard computation method fields are hidden.
   :highlight: The three Spanish fields (red frame).
   :data: Demo company "YourCompany ES"; category "Equipos para procesos de información", 4 depreciations every 12 months, 25%.
   :module: l10n_es_asset, om_account_asset
   :notes: English UI, light theme, 1440px width, crop to the form sheet.

Assets
======

When an asset is created with a category, it takes over the Spanish depreciation settings of the
category. On a draft asset, the settings can also be changed directly: go to
:menuselection:`Accounting --> Configuration --> Management --> Assets`, open the asset, and adjust
the :guilabel:`Spanish Depreciation Method`, the :guilabel:`Annual Depreciation Percentage` and the
:guilabel:`Depreciate to Period End` option.

If the asset is put into use later than its purchase date, fill in the :guilabel:`Depreciation Start
Date` (the date the asset is available for use). The depreciation is then computed from this date
instead of the asset :guilabel:`Date`.

Click :guilabel:`Compute Depreciation` to compute the depreciation board with the Spanish rules.
The lines that are already posted are kept; only the lines that are not posted yet are recomputed.

.. note::
   The Spanish settings of an asset can only be changed while the asset is in draft.

Assets from vendor bills
========================

When an asset is created from a vendor bill line with an asset category, its value includes the
part of the VAT of the line that is not deductible: the non-deductible VAT and, for companies
applying the VAT prorata, the non-deductible part of the prorata. These amounts are taken from the
AEAT tax information of the bill.

.. seealso::
   - :doc:`../../accounting/vendor_bills/assets`
   - :doc:`../spain`

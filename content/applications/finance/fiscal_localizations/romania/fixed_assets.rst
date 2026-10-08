=========================
Fixed assets (Romania)
=========================

The `l10n_ro_asset` module adapts the fixed asset management to the Romanian rules. It adds the
classification of the *HG 2139/2004* (the government decision that sets the classification catalog
and the useful lives of fixed assets), three Romanian depreciation methods, and two printable
documents: the asset sheet and the asset register.

.. note::
   The Romanian rules only apply to **purchase-type** assets (not sales deferrals) of companies
   whose fiscal country is Romania. The other assets keep the standard depreciation.

Classification catalog
======================

The catalog is available in :menuselection:`Accounting --> Configuration --> Management -->
Fixed Asset Catalog (Romania)`. It is pre-filled with about 25 common codes of the HG 2139/2004,
grouped under their chapters. Each code has a :guilabel:`Denomination`, a :guilabel:`Minimum Useful
Life (Years)` and a :guilabel:`Maximum Useful Life (Years)`. Accounting managers can add codes.

Set up an asset category
========================

On the asset category, the :guilabel:`Romanian Depreciation` group is shown for Romanian companies.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Romanian Depreciation Method`
     - :guilabel:`Linear`, :guilabel:`Degressive` or :guilabel:`Accelerated`.
   * - :guilabel:`Catalog Code`
     - Code of the HG 2139/2004. The useful life takes the minimum of the code by default.
   * - :guilabel:`Useful Life (Years)`
     - Duration of the depreciation.
   * - :guilabel:`First Year Rate (%)`
     - For the accelerated method. 50 by default; it must be above 0 and at most 50.

The same group is available on each asset, with the computed :guilabel:`Degressive Coefficient` and
:guilabel:`Annual Depreciation Rate (%)`. The method, the catalog code and the useful life of an
asset can only be changed in draft. The :guilabel:`Commissioning Date` is next to the date of the
asset; it defaults to the date of the asset, and the depreciation starts the month after. If the
useful life is outside the range of the catalog code, a banner warns you that the tax depreciation
follows the catalog.

Depreciation methods
====================

The depreciation board has one line per month, dated on the last day of the month. The years of
the useful life are counted from the first depreciation month. The last month absorbs the rounding
differences, and the salvage value is respected. Posted lines are kept when the board is
recomputed.

Linear
   The same amount every year. The annual rate is 100 / useful life.

Degressive
   The rate is the linear rate times a coefficient, applied to the remaining value: 1.5 for a
   useful life of 2 to 5 years, 2.0 for 6 to 10 years and 2.5 above 10 years (1.0 for a useful life
   of one year). When the linear amount of the remaining value becomes higher, the depreciation
   switches to linear.

Accelerated
   The first year takes the :guilabel:`First Year Rate (%)` (50% at most), and the remainder is
   linear over the remaining years.

.. example::
   An asset of 12,000 over 5 years in linear mode gives 60 monthly entries of 200.00, starting at the
   end of the month after the commissioning. A degressive asset of 10,000 over 5 years depreciates by
   3,000, then 2,100, then 1,633.33 for the last three years. An accelerated asset of 12,000 over 4
   years gives 12 entries of 500 in the first year, then 166.67 per month.

Documents
=========

Asset sheet
-----------

On the asset, click :guilabel:`Print Asset Sheet` to print the *Fișa mijlocului fix* (OMFP
2634/2015, form 14-2-2): the data of the asset, the operations, and the depreciation by year
(planned and booked).

Asset register
--------------

Go to :menuselection:`Accounting --> Reporting --> Management --> Fixed Asset Register (Romania)`,
select the :guilabel:`At Date` and the :guilabel:`Companies`, then click :guilabel:`Print`. The
*Registrul mijloacelor fixe* is a landscape PDF with the number, the inventory number, the name, the
classification code, the commissioning date, the useful life, the method, the input value, the
accumulated depreciation and the net book value of each asset. It lists the purchase-type assets
that are running or closed and dated on or before the selected date; the accumulated depreciation
is the sum of the posted lines up to that date. The documents are printed in Romanian if the
language is installed.

Differences with other localizations
====================================

- The :doc:`Hungarian assets <../hungary/assets>` use a rate-based board per accounting and tax rules
  (*Szt.* / *Tao*), an activation date, protocols, and a dispose wizard.
- The :doc:`Spanish assets <../spain/fixed_assets>` use three Spanish methods (linear over the
  useful life, fixed annual percentage and declining balance), with periods that follow the
  calendar.
- The Romanian assets use the catalog codes of the HG 2139/2004 and a monthly engine with a
  useful life in years.

Interaction with SAF-T
======================

The :doc:`SAF-T D406 <saft_d406>` assets variant reads the catalog code, the useful life and rate,
the commissioning date and the SAF-T disposal fields of the asset. Fill the catalog code on each
category to avoid a warning at validation.

.. seealso::
   - :doc:`saft_d406`
   - :doc:`../../accounting/vendor_bills/assets`

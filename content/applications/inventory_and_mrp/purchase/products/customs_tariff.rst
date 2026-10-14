==============================
Customs tariff and import duty
==============================

Goods bought from outside the European Union pay import duty when they are released for free
circulation. The rate depends on the **customs tariff code** of the goods and on their **origin**,
and it changes over time: new free trade agreements, anti-dumping duties, safeguard measures. The
eYssen *Customs Tariff (EU TARIC)* module (``product_customs_tariff``) keeps the official EU tariff
in the database, shows the expected import duty on the product form, and gives the duty to the
:ref:`expected cost <inventory/supplier-products/expected-cost>` of the vendor pricelists.

Customs duties are the same in every EU country: the Hungarian (NAV) and Spanish (AEAT) tariff
consultations show the same TARIC data. VAT and excise duties are national and are not part of the
tariff.

.. note::
   The module gives an estimate for planning, not a customs declaration. Tariff quotas,
   company-specific anti-dumping rates (additional codes) and end-use relief are not applied
   automatically; the estimate uses the general rate and says so.

Where the data comes from
=========================

The European Commission (DG TAXUD) publishes the TARIC database every month as XLSX extractions in
the public CIRCABC library *TARIC & Quota Data and Information*. Reuse is authorised under Commission
Decision 2011/833/EU. The module imports:

- the **nomenclature**: every Combined Nomenclature (CN, 8 digits) and TARIC (10 digits) line with
  its description and its place in the hierarchy;
- the **import duty measures**: third country duty, autonomous tariff suspensions, tariff
  preferences, anti-dumping and countervailing duties, additional duties, and the flag of the goods
  under the Carbon Border Adjustment Mechanism (CBAM); and
- the **geographical areas**: countries and country groups (for example `1011` ERGA OMNES, the GSP
  groups), with the countries excluded from a measure.

The descriptions are in English; descriptions in other languages are loaded when the Commission
publishes them in the same library.

Updating the tariff
-------------------

Go to :menuselection:`Purchase --> Configuration --> Settings`, section :guilabel:`Customs Tariff`:

- :guilabel:`Update Customs Tariff Automatically` checks the library every week and imports a newly
  published month. The date and size of the last import are shown below the option.
- :guilabel:`Update Now` opens the update window: :guilabel:`Download from the EU` downloads and
  imports the newest month at once. A full import takes one to two minutes.

If the server cannot reach the internet, download the files from CIRCABC and upload them in the same
window with their original names: at least :file:`Nomenclature EN.xlsx` and
:file:`Duties Import 01-99.xlsx`, and for a complete result also
:file:`Geographical areas composition.xlsx`, :file:`Geographical areas description.xlsx` and
:file:`Measure exclusions.xlsx`. Then click :guilabel:`Import Uploaded Files`.

.. screenshot:: purchase-customs-tariff-settings
   :menu: Purchase ‣ Configuration ‣ Settings
   :shows: The "Customs Tariff" section with the automatic update option, the date and size of the last
      import, and the "Update Now" and "Tariff Codes" links.
   :highlight: The last import line (red frame).
   :data: October 2026 data imported.
   :module: product_customs_tariff
   :notes: English UI, light theme, 1440px width, crop to the section.

Tariff codes
============

:menuselection:`Purchase --> Configuration --> Customs Tariff --> Customs Tariff Codes` lists the
declarable codes. Search by code with or without spaces (``7208 51`` or ``720851``) or by
description. A code shows:

- its :guilabel:`Parent` line and :guilabel:`CN Code` (the first 8 digits);
- :guilabel:`Declarable`: the lowest-level line that can be used in a customs declaration;
- the :guilabel:`Full Description` tab with the descriptions of all levels up to the chapter;
- the :guilabel:`Measures` tab with the measures attached to the line itself. The measures of the
  parent lines also apply to it;
- the :guilabel:`Products` button with the products that use the code; and
- :guilabel:`Open in TARIC`, which opens the official TARIC consultation for the code.

:guilabel:`Customs Tariff Measures` and :guilabel:`Customs Geographical Areas` in the same menu
list all imported measures and areas. Measures can also be added by hand (source
:guilabel:`Manual`); they are kept when the tariff is updated.

Tariff code on the product
==========================

On the product form, in the :guilabel:`Inventory` tab, select the :guilabel:`Customs Tariff Code`
(only declarable codes) and the :guilabel:`Origin of Goods`. The :guilabel:`HS Code` is filled from
the tariff code, so delivery slips and carrier integrations use it too.

As soon as a code is set, the :guilabel:`Import Duty` section shows:

- :guilabel:`Import Duty (%)`: the duty for the origin of goods today, as a percentage of the
  customs value;
- :guilabel:`CBAM Goods`, when the goods fall under the Carbon Border Adjustment Mechanism and CBAM
  certificates are due on their embedded emissions;
- the breakdown: third country duty, suspension, anti-dumping or countervailing duty, additional
  duty, with a warning when a rate has conditions, quotas or minimum / maximum amounts; and
- :guilabel:`Open in TARIC`, with the code and the origin already filled in.

Without an origin of goods, the general (ERGA OMNES) duty is shown. Tariff preferences are not
included on the product form, because they need a proof of preferential origin from the vendor; the
vendor pricelist takes them into account (see below).

.. screenshot:: purchase-customs-tariff-product
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ Inventory tab
   :shows: The Logistics group with the customs tariff code, HS code and origin of goods, and the Import
      Duty section with the rate, the CBAM flag and the duty breakdown.
   :highlight: The "Import Duty" section (red frame).
   :data: Hot-rolled steel plate, tariff code 7208 51 20 10, origin China.
   :module: product_customs_tariff
   :notes: English UI, light theme, 1440px width, crop to the Inventory tab.

How the duty is determined
==========================

For a tariff code, an origin and a date, the module takes the measures of the code and of all its
parent lines that are valid on that date and apply to the origin (the country itself, a group it
belongs to, or ERGA OMNES, unless the country is excluded):

#. the **third country duty** of the most specific line;
#. an **autonomous tariff suspension** replaces it when it is lower;
#. with **preferential origin**, the lowest **tariff preference** of the origin replaces it when it
   is lower (free trade agreements, GSP, the customs union with Türkiye);
#. **anti-dumping and countervailing duties** and **additional duties** are added on top. For
   company-specific anti-dumping rates the residual rate (all other companies) is used.

The result is an ad valorem rate (percentage of the customs value) and, for some goods, specific
duties in EUR per unit, per 100 kg, per hectolitre and so on.

.. example::
   Hot-rolled non-alloy steel plate (7208 51 20 10) from China in October 2026: third country duty
   0%, definitive anti-dumping duty 73.7% (residual rate), additional duty 50% (out-of-quota rate of
   the EU steel measure); CBAM goods. Total: 123.7% of the customs value.

Use in the expected purchase cost
=================================

With the *Supplier Product Management* module installed, every vendor pricelist line calculates its
import duty from the tariff code of the product. See :ref:`Expected cost
<inventory/supplier-products/expected-cost>`.

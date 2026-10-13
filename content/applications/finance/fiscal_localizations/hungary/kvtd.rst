================================
Environmental product fee (KVTD)
================================

The :guilabel:`Hungary - Environmental Product Charge (KVTD)` (`l10n_hu_kvtd`) module keeps the
register of the environmental product fee (*környezetvédelmi termékdíj*, Act LXXXV of 2011, Ktdt.),
prints the required clauses on the invoices and prepares the quarterly summary of the NAV
:guilabel:`KTBEV` return. It can be installed from the Apps menu or by ticking
:guilabel:`Hungarian KVTD` in the :doc:`eYssen ERP settings <../../../general/eyssen_erp_settings>`.

Since 1 January 2025 the product fee only applies to three product streams; packaging, electrical and
electronic equipment, batteries, tyres, office paper and advertising paper are covered by the
:doc:`extended producer responsibility (EPR) <epr>` instead:

- **other petroleum products**: lubricating, hydraulic and industrial oils (KT groups `602`, `603`,
  `604`);
- **other plastic products**: artificial flowers and plants (`301`) and plastic carrier bags (`311`,
  `312`, `316`, `351`, `352`, by thickness and biodegradability);
- **other chemical products**: soaps, detergents and cleaning products (`701`) and cosmetics (`702`).

.. note::
   - The fee does not change the price, the taxes or the journal entry of the invoice. The module
     keeps the register and the summary; the return itself is filed on the :guilabel:`KTBEV` form of
     NAV.
   - The module replaces the earlier `eyssen_l10n_hu_kvtd` module. See :ref:`Changing from the earlier
     module <localizations/hungary/kvtd-migration>`.

Configuration
=============

Settings
--------

Go to :menuselection:`Accounting --> Configuration --> Settings`, section :guilabel:`Hungarian
Product Charge (KVTD)`:

- :guilabel:`Product Charge Method`: when the obligation arises.

  - :guilabel:`Placing on the market (customer invoices)`: the fee is recorded on the domestic
    customer invoices of the company (Ktdt. 5. §).
  - :guilabel:`Stock-in (vendor bills, Ktdt. 6. §)`: the fee is recorded on the vendor bills of goods
    bought from abroad. The stock-in method can only be chosen from the first day of a year and must
    be notified to NAV by 31 January.

- :guilabel:`Product Charge Register Start`: invoices with an earlier fulfillment date do not create
  register lines (default: 1 January 2025).
- :guilabel:`Domestic Petroleum Producer`: tick it if the company produces petroleum products in
  Hungary. For these products the **first buyer** is liable for the fee (Ktdt. 3. § (2) b)), unless
  the company takes it over on the invoice.
- :guilabel:`Small Quantity Lump Sum`: the company pays the yearly lump sum of Ktdt. 15/B. § instead
  of the fee and files a yearly return.
- :guilabel:`Print KT Code and Charge on Invoices`: prints the KT code, the rate and the fee amount
  under every invoice line for every customer.

.. screenshot:: finance-fl-hungary-kvtd-settings
   :menu: Accounting ‣ Configuration ‣ Settings
   :shows: Settings page scrolled to the "Hungarian Product Charge (KVTD)" section with the method, the register start date, "Domestic Petroleum Producer", "Small Quantity Lump Sum" and "Print KT Code and Charge on Invoices".
   :highlight: The "Product charge method" block (red frame).
   :data: Demo company "YourCompany HU"; method "Placing on the market"; start 01/01/2025.
   :module: l10n_hu_kvtd
   :notes: English UI, light theme, 1440px width, crop to the section.

KT product groups and rates
---------------------------

:menuselection:`Accounting --> Configuration --> Product Charge (KVTD) --> KT Product Groups` lists
the KT product groups (the first three digits of the KT code) with their product stream, their
customs tariff numbers and their current rate. The groups and the rates valid from 1 January 2025
are loaded with the module:

.. list-table::
   :header-rows: 1
   :widths: 15 55 30

   * - KT group
     - Products
     - Rate (HUF/kg)
   * - `602`, `603`, `604`
     - Motor, gear and industrial oils
     - 114
   * - `301`
     - Plastic flowers, foliage and fruit imitations
     - 1 900
   * - `311`, `351`
     - Plastic carrier bags, not biodegradable
     - 1 681
   * - `312`, `316`, `352`
     - Plastic carrier bags, biodegradable
     - 281
   * - `701`
     - Soaps, surface-active agents, detergents
     - 11
   * - `702`
     - Beauty and body care products
     - 57

The rates of the carrier bags are 1 900 HUF/kg (biodegradable: 500 HUF/kg) reduced by the EPR fee of
the bag (Ktdt. 2. melléklet). For carrier bags the quantity is also kept in pieces.

Each group has a :guilabel:`Rates` tab with :guilabel:`Valid From` and :guilabel:`Valid To` dates:
when a rate changes, close the old line and add a new one. The register always uses the rate valid
on the fulfillment date of the invoice. Overlapping periods are not allowed.

Products
--------

On the :guilabel:`Product Charge (KVTD)` tab of the product form:

- :guilabel:`Product Charge Liability`:

  - :guilabel:`According to the company method` (default): every domestic sale is charged with the
    *placing on the market* method; only purchases from abroad with the *stock-in* method.
  - :guilabel:`Always liable`: also charged when bought from a Hungarian supplier (stock-in method).
  - :guilabel:`Not liable (charge paid by the supplier)`: the company is not the first domestic
    distributor of the product.

- One line per KT group contained in **one unit** of the product:

  - :guilabel:`KT Group`;
  - :guilabel:`Weight per Unit (kg)`: the chargeable mass in one unit of measure of the product;
  - :guilabel:`Pieces per Unit`: carrier bags only;
  - :guilabel:`Origin`: :guilabel:`Domestic production` or :guilabel:`Imported (EU or third country)`;
  - :guilabel:`Role`: charged under its own tariff number, or component or accessory of another
    product;
  - :guilabel:`Supplementary Code` (computed): the last two characters of the KT code, `B1`, `B2`,
    `K1` or `K2`;
  - :guilabel:`Variant` (optional, with variants): a line for one variant replaces the lines without
    variant for that variant, for example when the 1 l and the 4 l bottles have different weights.

:guilabel:`Product Charge per Unit (HUF)` shows the fee of one unit at the current rates.

.. screenshot:: finance-fl-hungary-kvtd-product
   :menu: Inventory ‣ Products ‣ Products ‣ (product) ‣ Product Charge (KVTD) tab
   :shows: Product form with the "Product Charge (KVTD)" tab open: liability, charge per unit, and one line with KT group, weight, origin, role, supplementary code and charge per unit.
   :highlight: The charge lines (red frame).
   :data: Product "Motor oil 5W-30 4 l"; KT group 602, 3.6 kg, imported, own tariff number, K1, 410.40 HUF.
   :module: l10n_hu_kvtd
   :notes: English UI, light theme, 1440px width, crop to the tab.

Customers and take-over
-----------------------

The :guilabel:`Accounting` tab of company contacts contains the :guilabel:`Product Charge (KVTD)`
section:

- :guilabel:`Print KT Code and Charge on Invoices`: the customer is entitled to a refund and asked for
  the details of Ktdt. 13. § (3) on the invoice.
- :guilabel:`Take Over Petroleum Charge on Invoice`: as the producer of a domestic petroleum product,
  the company takes over the buyer's obligation on the invoice (Ktdt. 14. § (4)).

Contractual take-over (Ktdt. 14. § (5)) is recorded in :menuselection:`Accounting --> Configuration
--> Product Charge (KVTD) --> Take-over Contracts`: :guilabel:`Customer (Taking Over)`,
:guilabel:`Legal Basis` (the buyer exports at least 60% or stores the goods in a tax warehouse, or
contract manufacturing), the validity (at most 3 years), the optional :guilabel:`KT Groups` and
:guilabel:`Registered by NAV On`. The contract is effective only from its registration by NAV
(Ktdt. 14/A. §).

Invoices
========

When an invoice is posted, a register line is created for every charge line of its products:
quantity = invoiced quantity converted to the unit of the product × weight per unit, fee = quantity
× rate valid on the fulfillment date. The lines are listed on the :guilabel:`Product Charge` tab of
the invoice (visible to invoicing users and accountants).

The register line gets the full 7-character KT code: KT group + handling code + supplementary code,
for example `60201K1`.

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Case
     - Handling code
     - Result
   * - Domestic sale
     - `01`
     - Fee payable.
   * - Delivery abroad (shipping address outside Hungary)
     - –
     - Not reportable (Ktdt. 4. § (2) a)).
   * - Customer with an effective take-over contract
     - `77` or `78`
     - Reported without fee; the invoice gets the clause of the contract.
   * - Take-over on the invoice (domestic petroleum product of a producer)
     - `73`
     - Fee payable by the company; the invoice gets the clause with the amount.
   * - Domestic petroleum product of a producer, no take-over
     - –
     - Not reportable: the first buyer is liable.

Credit notes reverse the lines of the original invoice in proportion to the credited quantity, with
the same KT code and rate. If a credit note or a corrective invoice only corrects the price (no goods
were returned), tick :guilabel:`No Product Charge Effect` on it; the field can also be changed after
posting, the lines are then rebuilt.

If the charge lines of a product are completed later, select the posted invoices in the list view and
use :menuselection:`Actions --> Rebuild product charge lines` (accounting administrators). Lines that
belong to a closed return summary are not changed.

.. important::
   Only invoices create register lines. Point of Sale orders without an invoice are not included;
   the return summary warns about them, add their quantities as manual register lines.

Invoice clauses
---------------

The printed customer invoice shows, before the payment terms:

- with contractual take-over: *A termékdíj-kötelezettség a Ktdt. 14. § (5) bekezdés a) [b)] pontja
  alapján a vevőt terheli.*
- with take-over on the invoice: *Az egyéb kőolajtermék vevője nem termékdíj-kötelezett, a bruttó
  árból … Ft termékdíj átvállalásra került.*

When the details are requested (customer or company setting), every line shows the KT code, the
quantity, the rate and the fee, and the invoice shows the name, address and tax number of the liable
company. Lump-sum payers cannot print these details (Ktdt. 13. § (2)).

Register and returns
====================

Register
--------

:menuselection:`Accounting --> Reporting --> Product Charge (KVTD) --> Product Charge Register` lists
the register lines with date, KT code, product, invoice, partner, quantity, rate, fee and status
(:guilabel:`Chargeable`, :guilabel:`Reported without charge`, :guilabel:`Not reportable`,
:guilabel:`Legacy (before 2025)`). Group by KT code or quarter, or open the pivot view. Opening stock
(stock-in method), own use and corrections can be entered as manual lines.

Quarterly return summary
------------------------

:menuselection:`Accounting --> Reporting --> Product Charge (KVTD) --> Product Charge Returns`:

#. Create a summary with :guilabel:`Quarterly` (or :guilabel:`Yearly (lump sum)`), the year and the
   quarter.
#. Click :guilabel:`Compute`: the register lines of the period are summed by KT code and rate. The
   quantity is rounded to two decimals of kg (Ktdt. 11. § (4)) and the fee is quantity × rate.
   :guilabel:`Payable` is zero if the total is below 1 000 HUF (Ktdt. 12. § (2)); for lump-sum
   payers it is the yearly lump sum of the categories used.
#. Check the warnings: draft invoices of the period, lines without rate, negative balances, lines of
   earlier periods that are in no return (for example late credit notes, which belong to their own
   period), Point of Sale orders without invoice, and the yearly limit of the lump sum (40 kg
   petroleum products, 2 kg artificial flowers, 75 kg carrier bags, 200 kg chemical products).
#. :guilabel:`Export XLSX` downloads the summary and the detailed register for filling in the
   :guilabel:`KTBEV` form.
#. File the return in NAV by the 20th day of the month following the quarter and pay the fee by the
   same day. Record :guilabel:`Submitted On` and :guilabel:`NAV Filing Number`, then click
   :guilabel:`Close`: the register lines of the period are locked.

:guilabel:`Reopen` (accounting administrators) unlocks the summary for a correction.

.. screenshot:: finance-fl-hungary-kvtd-return
   :menu: Accounting ‣ Reporting ‣ Product Charge (KVTD) ‣ Product Charge Returns ‣ (summary)
   :shows: Return summary form of a quarter with the Compute, Export XLSX and Close buttons, the totals, and the summary lines by KT code (quantity, rate, fee, number of lines).
   :highlight: The summary lines (red frame).
   :data: "Product charge 2026 Q1"; lines 60201K1 10.80 kg × 114 = 1 231 HUF and 35101B1 2.40 kg × 1 681 = 4 034 HUF.
   :module: l10n_hu_kvtd
   :notes: English UI, light theme, 1440px width, crop to the form sheet.

.. _localizations/hungary/kvtd-migration:

Changing from the earlier module
================================

The earlier `eyssen_l10n_hu_kvtd` module and `l10n_hu_kvtd` use different data and can be installed
side by side for the change:

#. Install `l10n_hu_kvtd`.
#. Set the KT groups and the weights on the products. The petroleum products of the earlier module
   can be copied (the packaging and the other categories that moved to EPR are not needed any more;
   carrier bags were packaging in the earlier module and need their new KT group).
#. Keep the earlier lines of already filed periods as read-only *legacy* lines, and rebuild the
   invoices of the first period not yet filed with :menuselection:`Actions --> Rebuild product
   charge lines`.
#. Uninstall `eyssen_l10n_hu_kvtd`.

.. tip::
   eYssen provides a migration script for these steps; ask your eYssen contact.

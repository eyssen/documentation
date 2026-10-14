======================================
Extended producer responsibility (EPR)
======================================

The :guilabel:`Hungary - Extended Producer Responsibility (EPR / KGYF)` (`l10n_hu_epr`) module
implements the Hungarian extended producer responsibility (*kiterjesztett gyártói felelősség*,
Government Decree 80/2023. (III. 14.)): it keeps the EPR register of the products placed on the
Hungarian market by KF code, prints the invoice clauses, and prepares the quarterly data report
(OKIRkapu data package :guilabel:`KG:KGYF-NÉ`) as an XML file validated against the official schema.
It can be installed from the Apps menu or by ticking :guilabel:`Hungarian EPR` in the
:doc:`eYssen ERP settings <../../../general/eyssen_erp_settings>`.

The EPR covers packaging, single-use plastic products, electrical and electronic equipment,
batteries, vehicles, tyres, office paper, advertising paper, frying oil and fat, textiles and wooden
furniture. The fee is collected by the concessionaire MOHU MOL Hulladékgazdálkodási Zrt. The products
still subject to the environmental product fee are handled by the :doc:`KVTD module <kvtd>`.

.. note::
   - The data report is uploaded to OKIRkapu by the user: OKIRkapu has no machine interface, the
     module generates the file.
   - The fee is not posted by the module. MOHU invoices it quarterly on the basis of the data report;
     record the MOHU invoice as a vendor bill and link it to the report to compare the amounts.

How the obligation works
========================

- The **producer** is whoever places a product on the Hungarian market for the first time: the
  domestic manufacturer, or the importer or EU purchaser at its first domestic sale (80/2023. Korm.
  r. 16. §). A company buying from a Hungarian supplier and reselling is not liable.
- Every separable component of a packaging (bottle, cap, label, film, carton) has its own KF code
  and fee (11. § (5)).
- The producer reports the quantities by KF code quarterly, by the 20th day of the month following
  the quarter, to the national waste management authority through OKIRkapu (27. §). MOHU invoices
  the fee on this basis; it is payable within 15 days of receipt (21. § (1)).
- Records are kept for at least 5 years and must be traceable item by item (26. §, 28. §).

KF codes
--------

The KF code has 8 characters:

.. list-table::
   :header-rows: 1
   :widths: 15 35 50

   * - Characters
     - Meaning
     - Where it comes from in Odoo
   * - 1–2
     - Product stream (11 packaging, 12 single-use plastic, 13 EEE, …)
     - EPR component of the product
   * - 3–4
     - Material stream (e.g. 01 PET, 20 corrugated board)
     - EPR component of the product
   * - 5–6
     - Group (e.g. 10 consumer packaging, 20 transport packaging)
     - EPR component of the product
   * - 7
     - Obligation code: 1 collective, 2 individual, A / B customer declaration
     - Company setting and customer declaration
   * - 8
     - Origin: 1/2/3 domestic, 5/6/7 brought in from abroad, 8 own use
     - Origin and role of the component

Example: `11202013` is corrugated board (20), non-reusable transport packaging (20), collective
fulfillment (1), packaging produced in Hungary (3).

Configuration
=============

Settings
--------

Go to :menuselection:`Accounting --> Configuration --> Settings`, section :guilabel:`Hungarian EPR
(Extended Producer Responsibility)`:

- :guilabel:`EPR Producer`: the company is a producer and keeps an EPR register.
- :guilabel:`EPR Register Method`:

  - :guilabel:`Placing on the market (customer invoices)`: the register lines are created from the
    domestic customer invoices.
  - :guilabel:`Stock-in (vendor bills, 26/A. §)`: the register lines are created from the vendor bills
    of goods bought from abroad. This method can be chosen from the first day of a quarter, with an
    opening inventory.

- :guilabel:`EPR Register Start`: invoices with an earlier fulfillment date do not create register
  lines.
- :guilabel:`EPR Fulfilment`: :guilabel:`Collective (through the concessionaire)` or
  :guilabel:`Individual`. Individual fulfillment is only possible for EEE, batteries and vehicles
  (7–9. §); for every other product stream collective fulfillment is reported.
- :guilabel:`OKIRkapu data`: the :guilabel:`KÜJ Number` (environmental client identifier), the
  :guilabel:`EPR Registration Number`, the :guilabel:`EPR Contact Person` (a contact with address,
  phone and e-mail) and the :guilabel:`EPR Contact Position`. They are required for the XML.
- :guilabel:`Print EPR Clauses on Invoices`: prints the clauses of 21. § on the customer invoices.

The company address and the Hungarian :guilabel:`VAT Number` of the company are also used in the
data report.

.. screenshot:: finance-fl-hungary-epr-settings
   :menu: Accounting ‣ Configuration ‣ Settings
   :shows: Settings page scrolled to the "Hungarian EPR (Extended Producer Responsibility)" section with "EPR Producer" ticked, the method, start date and fulfillment, the OKIRkapu data and "Print EPR Clauses on Invoices".
   :highlight: The "OKIRkapu data" block (red frame).
   :data: Demo company "YourCompany HU"; KÜJ 123456789; contact "Kovács Anna", position "ügyvezető".
   :module: l10n_hu_epr
   :notes: English UI, light theme, 1440px width, crop to the section. Use a fictitious KÜJ number.

KF codes, fee codes and rates
-----------------------------

- :menuselection:`Accounting --> Configuration --> EPR --> KF Codes` lists the valid first six
  characters of the KF codes (80/2023. Korm. r. 2. melléklet) with the material stream, the group and
  the fee code. The list is loaded with the module and updated with it.
- :menuselection:`Accounting --> Configuration --> EPR --> EPR Fee Codes and Rates` lists the fee
  codes (`M01` plastic packaging, `P01` paper packaging, `V01` metal packaging, `SUP01` single-use
  plastic, `E01`–`E06` EEE, `A11`–`A51` batteries, …) with dated rates in HUF/kg, net of VAT, and
  their concession and municipal elements. The rates of 2025 and 2026 are loaded with the module;
  when a new fee decree is published, close the old rate and add the new one.

Products
--------

On the :guilabel:`EPR` tab of the product form:

- :guilabel:`EPR Liability`: :guilabel:`According to the company method` (default),
  :guilabel:`Always liable` (also when bought from a Hungarian supplier, stock-in method) or
  :guilabel:`Not liable (another company placed it on the market)`.
- One line per **EPR component** of one unit of the product:

  - :guilabel:`Component`: e.g. *bottle*, *cap*, *label*, *shrink film*, *carton box*;
  - :guilabel:`KF Code (1-6)`: search by code, material or group; the :guilabel:`Fee Code` is shown
    next to it;
  - :guilabel:`Weight per Unit (kg)`: the mass in one unit of measure of the product (six decimals);
  - :guilabel:`Role`: :guilabel:`Packaging`, :guilabel:`Product placed on the market on its own` or
    :guilabel:`Component or accessory of another product`. KF codes of the packaging stream can only
    be used for packaging;
  - :guilabel:`Origin`: :guilabel:`Produced in Hungary` or :guilabel:`Brought in from abroad (EU or
    third country)`;
  - :guilabel:`Origin Code` (computed): the 8th character of the KF code;
  - :guilabel:`Variant` (optional, with variants): lines of a variant replace the lines without
    variant for that variant.

- For electrical and electronic equipment, batteries, tyres, textiles, furniture and the other
  product streams, add a line for the product itself (role *on its own* or *component*), next to the
  lines of its packaging.

:guilabel:`EPR Weight per Unit (kg)` and :guilabel:`EPR Fee per Unit (HUF)` show the totals of one
unit at the current rates.

.. screenshot:: finance-fl-hungary-epr-product
   :menu: Inventory ‣ Products ‣ Products ‣ (product) ‣ EPR tab
   :shows: Product form with the "EPR" tab: liability, weight and fee per unit, and two component lines (bottle and carton box) with KF code, fee code, weight, role, origin and fee per unit.
   :highlight: The component lines (red frame).
   :data: Product "Mineral water 0.5 l × 12"; bottle 110110 (M01) 0.24 kg imported packaging; carton box 112020 (P01) 0.30 kg domestic packaging.
   :module: l10n_hu_epr
   :notes: English UI, light theme, 1440px width, crop to the tab.

Customer declarations
---------------------

A customer who ships at least 60% of the products abroad (22. §), or who uses frying oil or fat as
raw material (22/A. §), can declare it. Sales covered by the declaration are reported with obligation
code `A` or `B`, without fee, and the declaring customer is listed in the data report.

Record the declarations in :menuselection:`Accounting --> Configuration --> EPR --> Customer
Declarations`:

- :guilabel:`Registration Number`: the filing number of the declaration at the authority (printed on
  the invoice);
- :guilabel:`Customer (Declarant)` and :guilabel:`Type`;
- :guilabel:`Valid From` and :guilabel:`Valid To`: at most 3 years (22/B. §);
- :guilabel:`Sent to the Authority On`: the declaration is effective from the day it was sent to the
  authority (26. § (6));
- :guilabel:`KF Codes (1-6)`: the codes covered by the declaration (required). A 22/A. § declaration
  can only cover frying oil and fat.

Customers who asked for the clause *A kiterjesztett gyártói felelősségi díj megfizetésre kerül.*
(21. § (5)) are marked with :guilabel:`EPR Clause Requested` in the :guilabel:`Accounting` tab of the
contact.

Invoices
========

When an invoice is posted, a register line is created for every EPR component of its products:
quantity = invoiced quantity converted to the unit of the product × weight per unit, fee = quantity
× rate valid on the fulfillment date. The lines are shown on the :guilabel:`EPR` tab of the invoice
(visible to invoicing users and accountants).

- Deliveries abroad (shipping address outside Hungary) are not reportable (16. § (4)).
- Sales covered by an effective customer declaration are reported without fee, with obligation code
  `A` or `B`.
- With the stock-in method, purchases from Hungarian suppliers are not reportable unless the product
  is :guilabel:`Always liable`.
- Credit notes reverse the lines of the original invoice in proportion to the credited quantity, with
  the same KF code, rate and declaration. If a credit note or a corrective invoice only corrects the
  price, tick :guilabel:`No EPR Effect` on it; the field can also be changed after posting.
- If the EPR components of a product are completed later, select the posted invoices in the list view
  and use :menuselection:`Actions --> Rebuild EPR lines` (accounting administrators). Lines of a
  closed data report are not changed.

.. important::
   Only invoices create register lines. Point of Sale orders without an invoice, foreign packaging
   removed in Hungary (own use, origin code `8`, 17. § (3)) and the opening inventory of the stock-in
   method are entered as manual lines in the EPR register.

Invoice clauses
---------------

The printed customer invoice shows, before the payment terms (not on retail sales to consumers
without a tax number):

- *A kiterjesztett gyártói felelősségi díj megfizetése az eladót terheli.* when the company declares
  and pays the fee of the invoice (21. § (2));
- *A kiterjesztett gyártói felelősségi díj a vevő nyilatkozata alapján nem került megfizetésre (a
  nyilatkozat iktatási száma: …).* for sales covered by a declaration (21. § (3));
- *A kiterjesztett gyártói felelősségi díj megfizetésre kerül.* if the customer asked for it and no
  other clause applies (21. § (5)).

With the stock-in method, the clause of 21. § (2) is printed on the domestic sales of the products
with EPR components.

.. _l10n_hu/epr/expected-cost:

EPR fee in the expected cost
============================

With *Supplier Product Management* installed, the module
:guilabel:`Supplier Product Management - Hungarian EPR` (`supplier_product_management_l10n_hu_epr`)
is installed automatically. It fills the :guilabel:`EPR Fee per Unit` of the vendor pricelist lines
from the EPR components of the product: weight per unit × current rate of the fee code, summed over
the components and converted to the unit of the pricelist line. The fee becomes part of the
:ref:`expected cost <inventory/supplier-products/expected-cost>` of the line.

The fee is filled only when the company pays it for goods bought from that vendor, following the
same rules as the register:

- no fee if the EPR register is not active or the product's :guilabel:`EPR Liability` is
  :guilabel:`Not liable (another company placed it on the market)`;
- with :guilabel:`Always liable`, or with the placing-on-the-market method, the fee is always
  counted;
- with the stock-in method, the fee is counted for vendors abroad, not for Hungarian vendors.

The fee is recalculated when the vendor, the product or its EPR components change; it can be
overwritten by hand on the line.

Register and data report
========================

Register
--------

:menuselection:`Accounting --> Reporting --> EPR --> EPR Register` lists the register lines with
date, KF code, fee code, product and component, invoice, partner, quantity, rate, fee and status
(:guilabel:`Fee payable`, :guilabel:`Reported without fee`, :guilabel:`Not reportable`). Group by KF
code, fee code, product stream or quarter, or open the pivot view.

Quarterly data report
---------------------

:menuselection:`Accounting --> Reporting --> EPR --> EPR Data Reports`:

#. Create a report with the year and the quarter. The :guilabel:`Deadline` (20th day of the month
   after the quarter) is shown.
#. Click :guilabel:`Compute`. The register lines of the quarter are summed by KF code:

   - deliveries in the :guilabel:`Summary` tab as *placed on the market* rows (data package block
     `KG_KGYF_NE_TERMEK_FORG`), with the declaring buyers of the `A` and `B` codes;
   - credit notes as *returned* rows with positive quantities (block `KG_KGYF_NE_TERMEK_VISSZA`);
   - the :guilabel:`Expected Fee` tab: quantity × rate by fee code and rate, net of the returns.

   Quantities are in kg with three decimals; codes netting to zero are left out. Without any line the
   report is a :guilabel:`Zero Report`.
#. Check the warnings: draft invoices of the quarter, lines of earlier quarters that are in no report
   (late credit notes), returned products, missing rates, declarations without buyer address, Point
   of Sale orders without invoice, and missing OKIRkapu data.
#. :guilabel:`Export XML (OKIRkapu)` computes the draft report again, builds the
   :guilabel:`KG:KGYF-NÉ` XML and validates it against the official XSD (version 1.16).
   :guilabel:`Export XLSX` downloads the summary, the expected fee and the detailed register.
#. Click :guilabel:`Close`: the register lines of the quarter are locked.
#. In OKIRkapu, create the data package with :guilabel:`Új adatcsomag XML-ből`, upload the XML,
   check it and submit it. Record :guilabel:`Submitted On` and :guilabel:`OKIR Filing Number`, then
   click :guilabel:`Mark as Submitted`.
#. When the MOHU invoice arrives, add it to :guilabel:`MOHU Invoices` in the :guilabel:`Expected Fee`
   tab: :guilabel:`Invoiced by MOHU (net)` and :guilabel:`Difference` show the comparison. A
   complaint with the correct data can be filed within 15 days of receipt (21. § (7)).

.. screenshot:: finance-fl-hungary-epr-report
   :menu: Accounting ‣ Reporting ‣ EPR ‣ EPR Data Reports ‣ (report)
   :shows: Data report form of a quarter in the Closed state with the Export XML (OKIRkapu), Export XLSX and Mark as Submitted buttons, the totals, and the Summary tab listing KF codes with quantity, fee and declaring buyers.
   :highlight: The "Export XML (OKIRkapu)" button and the summary rows (red frame).
   :data: "EPR 2026 Q1"; rows 11011017 4.800 kg, 11202013 3.000 kg, 112020A3 3.000 kg (buyer "Minta Kft."), returned 11011017 0.960 kg.
   :module: l10n_hu_epr
   :notes: English UI, light theme, 1440px width, crop to the form sheet.

Corrections
-----------

The data of a submitted quarter can be corrected once a year, between 1 January and 31 March of the
following year, or with a complaint against the MOHU invoice within 15 days (27. § (6), 21. § (7)).
Create a new report for the quarter with :guilabel:`Correction` ticked and fill in
:guilabel:`Disputed MOHU Invoice` or :guilabel:`Authority Case Number`. The correction takes a
snapshot of all register lines of the quarter; the lines stay linked to the original report.

.. note::
   The following cases are not supported by the module: the yearly report of small producers
   (`KG:KGYF-ÉV`), take-over contracts, deposit-return (DRS) products, the lump sum for wine bottles
   and vehicles, and the handling data of individual fulfillment.

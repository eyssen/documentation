=========
Intrastat
=========

Intrastat is the data collection and statistics production system for goods traded among EU member
states. It collects data on:

- Commercial transactions of goods for use, consumption, investment, or resale with ownership
  transfer;
- Goods movements without transfer of ownership (e.g., stock relocations or moves of goods
  before or after outsourced production or processing, and after maintenance or repair);
- Returns of goods.

.. note::
   Although the Intrastat system continues to be used, the term Intrastat is not used in the `latest
   legislation <http://data.europa.eu/eli/reg/2019/2152/2022-01-01>`_, referring instead to
   *intra-Union trade in goods statistics*.

.. seealso::
   `Eurostat Statistics Explained - Glossary: Intrastat
   <https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Intrastat>`_

Intrastat support is provided by the *Intrastat Reporting Base*, *Intrastat Product*, *Product
Harmonized System Codes* and *Intrastat* (Hungarian report) modules. Once installed, they add an
:guilabel:`Intrastat` section under :menuselection:`Accounting --> Configuration` and under
:menuselection:`Accounting --> Reporting`.

.. _intrastat/general-configuration:

General configuration
=====================

Reference data
--------------

The declaration codes are maintained under :menuselection:`Accounting --> Configuration -->
Intrastat`:

- :guilabel:`H.S. Codes` — the commodity codes (see :ref:`intrastat/commodity-code`);
- :guilabel:`Transaction Types` — the codes identifying the nature of a transaction;
- :guilabel:`Transport Modes` — the codes identifying the presumed mode of transport;
- :guilabel:`Supplementary Units` — the units used instead of, or next to, the weight;
- :guilabel:`Intrastat Regions` — the regional codes, where the member state requires them.

Fiscal positions
----------------

A :doc:`fiscal position <../taxes/fiscal_positions>` carries an :guilabel:`Intrastat` setting that
decides whether the invoices using it are part of the declaration. Set it on the fiscal positions
used for intra-Community trade, so that domestic and non-EU transactions are excluded automatically.

Reminders
---------

The company can appoint the users who are reminded that a declaration is due, and an address the
reminder is sent to, in the :guilabel:`Intrastat` settings of the company.

.. _intrastat/product-configuration:

Product configuration
=====================

All products must be properly configured to be included in the Intrastat declaration.

.. _intrastat/commodity-code:

Commodity code
--------------

Commodity codes are internationally recognized reference numbers used to classify goods depending on
their **nature**. Intrastat uses the `Combined Nomenclature
<https://taxation-customs.ec.europa.eu/customs-4/calculation-customs-duties/customs-tariff/combined-nomenclature_en>`_.

Codes are maintained under :menuselection:`Accounting --> Configuration --> Intrastat --> H.S.
Codes`, where each code holds its :guilabel:`H.S. Code`, its :guilabel:`Description` and, where
applicable, a :guilabel:`Local Code`. A code can be assigned to a whole **product category**, in
which case every product of that category inherits it, or to a single product.

To set it on a product, go to :menuselection:`Accounting --> Customers --> Products`, select a
product, and set the :guilabel:`H.S. Code` in the :guilabel:`General Information` tab. The field is
hidden on services.

.. _intrastat/quantity:

Quantity: weight and supplementary unit
---------------------------------------

Depending on the nature of the goods, it is necessary to specify either the product's weight in
kilos (without packaging) or the product's supplementary unit, such as square meter (`m2`), number
of items (`p/st`), liter (`l`), or gram (`g`). The supplementary unit to use is defined on the
H.S. code; the product only has to carry its :guilabel:`Weight`.

.. _intrastat/origin-country:

Country of origin
-----------------

To add the product's country of origin, go to :menuselection:`Accounting --> Customers --> Products`
and select a product. In the :guilabel:`General Information` tab, set the :guilabel:`Country of
Origin`.

.. _intrastat/invoice-bill-configuration:

Invoices and bills configuration
================================

Once products are properly configured, several settings are available on the invoices and bills you
create, in the :guilabel:`Other Info` tab:

.. _intrastat/transaction-code:

Transaction code
----------------

:guilabel:`Intrastat Transaction Type` identifies the nature of the transaction. It defaults from
the fiscal position and can be changed per document.

.. _intrastat/partner-country:

Partner country and region
--------------------------

:guilabel:`Destination Country` represents the vendor's country for bills and the customer's country
for invoices. It is computed automatically from the contact's :guilabel:`Country` and can be
corrected per document. Where regions are required, the origin/destination region is taken from the
company's Intrastat region, or from the warehouse's :guilabel:`Intrastat Region`
(:menuselection:`Inventory --> Configuration --> Warehouses`).

.. _intrastat/transport-code:

Transport code
--------------

:guilabel:`Intrastat Transport Mode` identifies the presumed **mode of transport** used to send the
goods (arrival or dispatch). It is only displayed when the company's Intrastat declaration is set to
the extended level.

.. _intrastat/value:

Value of the goods
------------------

The value of a good is the untaxed :guilabel:`Subtotal` (:guilabel:`Price` multiplied by
:guilabel:`Quantity`) of an invoice line.

The per-line Intrastat details of a document can be reviewed in the :guilabel:`Intrastat transaction
details` tab of the invoice or bill, where :guilabel:`Compute` recalculates them from the product
master data. The tab is reserved to the users who have the corresponding access right.

.. screenshot:: accounting-intrastat-invoice-other-info
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (an intra-Community invoice) ‣ Other Info
   :shows: The Other Info tab of an invoice with the Intrastat Transaction Type, Intrastat Transport
      Mode and Destination Country fields filled in, below the Incoterm fields.
   :highlight: The Intrastat fields (red frame).
   :data: Invoice to an Austrian customer, transaction type 11, transport mode 3 (road).
   :module: intrastat_base, intrastat_product
   :notes: English UI, light theme, crop to the tab.

.. _intrastat/partner:

Partner configuration
=====================

Two fields from the partner's contact form are used with Intrastat: :guilabel:`VAT` and
:guilabel:`Country`. The country can be :ref:`corrected <intrastat/partner-country>` on the
invoice or bill.

.. _intrastat/declaration:

Prepare the declaration
=======================

Go to :menuselection:`Accounting --> Accounting --> Intrastat --> Intrastat Product Declaration` and
click :guilabel:`New`. Set the :guilabel:`Year` and the :guilabel:`Period` (month), the
:guilabel:`Type` (:guilabel:`Arrivals` or :guilabel:`Dispatches`), the :guilabel:`Action` and the
:guilabel:`Reporting Level`, then:

#. Click :guilabel:`Generate Lines from Invoices`. Odoo collects the invoice lines of the period and
   fills the :guilabel:`Transactions` tab with one computation line per invoice line, each carrying
   the commodity code, the country, the transaction and transport codes, the weight, the
   supplementary units and the fiscal value. Anything missing is reported so it can be corrected on
   the source document.
#. Review the :guilabel:`Declaration Lines` tab, where the computation lines are aggregated the way
   the administration expects them, and check the :guilabel:`Number of Declaration Lines` and the
   :guilabel:`Total Fiscal Amount`.
#. Click :guilabel:`Confirm` when the declaration is correct. :guilabel:`Back to Draft` reopens it
   if a correction is needed; the :guilabel:`Revision` number keeps track of the corrections.
#. Click :guilabel:`Generate XML File` to produce the file for the administration; it is stored on
   the declaration as the :guilabel:`XML Attachment`. :guilabel:`Excel Export` produces a
   spreadsheet of the same content for internal review.

.. screenshot:: accounting-intrastat-declaration
   :menu: Accounting ‣ Accounting ‣ Intrastat ‣ Intrastat Product Declaration ‣ (a declaration)
   :shows: An Intrastat product declaration in the Draft state with the year, period, type and
      reporting level, the header buttons (Generate Lines from Invoices, Confirm, Generate XML File,
      Excel Export) and the Transactions tab filled with computation lines.
   :highlight: The header buttons (red frame).
   :data: Declaration "Dispatches 2026-08" with twelve computation lines.
   :module: intrastat_product, eyssen_intrastat
   :notes: English UI, light theme, 1440px width.

.. _intrastat/hu-report:

Hungarian Intrastat report
==========================

For Hungarian companies, :menuselection:`Accounting --> Reporting --> Intrastat --> Intrastat HU
Report` produces the spreadsheet expected by the Hungarian Central Statistical Office. Set the
start and end date and whether the report covers customer invoices or vendor bills, then click
:guilabel:`Excel`.

.. note::
   The labels of this report's dialog are currently in Hungarian.

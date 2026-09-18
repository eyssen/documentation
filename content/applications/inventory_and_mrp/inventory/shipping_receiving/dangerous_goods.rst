=====================
Dangerous goods (ADR)
=====================

Companies that ship hazardous substances by road in Europe must classify those goods according to
the *European Agreement concerning the International Carriage of Dangerous Goods by Road* (ADR), and
must know, for every consignment, how close it is to the exemption threshold of the agreement. Two
eYssen modules bring that information into Odoo: the products carry their ADR classification, and
every transfer shows the resulting **ADR points**.

.. seealso::
   `ADR (treaty) <https://en.wikipedia.org/wiki/ADR_(treaty)>`_ and the
   `UNECE ADR files <https://unece.org/transportdangerous-goods/adr-2021-files>`_

Configuration
=============

Install the *ADR Dangerous Goods* module (``l10n_eu_product_adr``). It ships with the dangerous
goods catalog — Table A of chapter 3 of the ADR specification — so no data has to be entered before
products can be classified.

.. warning::
   The shipped catalog is generated from a public spreadsheet. The specification itself sometimes
   lists several options or additional restrictions for one entry, and that complexity is **not**
   encoded in the data. Verify each dangerous good used in the database against the current
   specification, and adjust it to the situation in the warehouse.

Access rights
-------------

The module defines two access groups, *ADR Goods User* and *ADR Goods Administrator*. Membership of
one of them is required to see the ADR information on the product form; every Inventory user is
added to the user group by default. The dangerous goods catalog menus other than
:guilabel:`Dangerous Goods` itself are only visible in :ref:`developer mode <developer-mode>`.

Dangerous goods catalog
-----------------------

Go to :menuselection:`Inventory app --> Configuration --> Dangerous Goods --> Dangerous Goods` to
review the catalog. Each entry carries:

- :guilabel:`UN Number`: the UN number of the substance or article, or of the generic (n.o.s.) entry
  it is assigned to.
- :guilabel:`Name and description`: the proper shipping name, in upper case.
- :guilabel:`Class` and :guilabel:`Classification code`: the ADR danger class and its code.
- :guilabel:`Labels`: the placards that must be affixed to packages, containers, tanks and vehicles.
- :guilabel:`Limited Quantity` and its unit of measure.
- :guilabel:`Packing Instructions`.
- :guilabel:`Transport category`: `0` to `4`, `-`, :guilabel:`CARRIAGE PROHIBITED` or
  :guilabel:`Not subject to ADR`. This is what drives the points calculation.
- :guilabel:`Tunnel restriction code`: which road tunnels the consignment may pass through.

.. screenshot:: shipping-receiving-dangerous-goods-catalog
   :menu: Inventory ‣ Configuration ‣ Dangerous Goods ‣ Dangerous Goods
   :shows: A dangerous goods record from the ADR catalog, showing the UN Number, Name and description, Class, Classification code, Labels, Limited Quantity, Transport category and Tunnel restriction code.
   :data: UN 1203 "PETROL", class 3, transport category 2.
   :module: l10n_eu_product_adr
   :notes: English UI, light theme, 1440px width.

Classify a product
==================

Open a storable product and tick :guilabel:`Is dangerous` in the :guilabel:`Inventory` tab. A
:guilabel:`Dangerous Goods` tab appears, where the :guilabel:`Dangerous Goods` entry from the
catalog is selected; the class, classification code, limited quantity, packing instructions,
transport category, tunnel restriction code and the hazard labels are then filled in from the
catalog and shown read-only.

Products whose variants differ in their hazard classification can tick :guilabel:`Dangerous goods
settings on variants`: the dangerous goods entry is then chosen per variant instead of once for the
whole product, and a variant may also carry no entry at all.

.. screenshot:: shipping-receiving-dangerous-goods-product-tab
   :menu: Inventory ‣ Products ‣ Products
   :shows: The "Dangerous Goods" tab of a product form, with the dangerous goods entry selected and the class, classification code, limited quantity, transport category, tunnel restriction code and hazard labels filled in from the catalog.
   :highlight: The "Dangerous Goods" selection field (red frame).
   :data: Product "Petrol 5 l", UN 1203.
   :module: l10n_eu_product_adr
   :notes: English UI, light theme, 1440px width.

Extended product data
---------------------

Installing the companion module *l10n Eu Product Adr Dangerous Goods*
(``l10n_eu_product_adr_dangerous_goods``) adds the further data sheets many warehouses and safety
officers need, on the product variant form:

- **Packaging**: :guilabel:`Content Packaging` with its unit, :guilabel:`Packaging group`,
  :guilabel:`Label 1`, :guilabel:`Label 2`, :guilabel:`Label 3` and :guilabel:`Flash point(°C)`.
- **Storage**: :guilabel:`Storage class`, :guilabel:`Packaging type`, :guilabel:`Storage
  temperature` and :guilabel:`WGK class` (German water hazard class).
- **Other**: :guilabel:`Environmentally hazardous`, :guilabel:`VOC in%`, :guilabel:`N.A.G.`,
  :guilabel:`VeVA Code: Empty packaging`, :guilabel:`VeVA Code: Full package`, :guilabel:`H-No`,
  :guilabel:`Hazard identification` and the :guilabel:`Limited amount` reference.

.. note::
   These fields are filled in manually; they are not derived from the ADR catalog.

ADR points on transfers
=======================

Every transfer shows an :guilabel:`ADR points` figure in the :guilabel:`Other Info` tab, computed as
the sum of its lines. For each line, Odoo takes the quantity — the product's weight when the product
has one, otherwise the quantity converted to the product's reference unit of measure — and
multiplies it by the factor of the goods entry: a factor tied to the UN number where the agreement
defines one, and otherwise the factor of the transport category (category 1 → 50, 2 → 3, 3 → 1,
4 → 0). Lines whose product carries no dangerous goods entry contribute nothing.

The figure lets the warehouse see at a glance whether a consignment stays under the ADR exemption
threshold, and therefore whether the full set of transport requirements applies to the vehicle.

.. screenshot:: shipping-receiving-dangerous-goods-picking-points
   :menu: Inventory ‣ Delivery Orders
   :shows: The "Other Info" tab of a delivery order containing hazardous products, showing the "ADR points" field.
   :highlight: The "ADR points" field (red frame).
   :data: Delivery order with two hazardous lines.
   :module: l10n_eu_product_adr
   :notes: English UI, light theme, 1440px width.

.. important::
   The ADR points are an aid, not a compliance statement. When a product's weight is not filled in,
   the calculation assumes that the reference unit of measure (kilogram or liter) matches the ADR
   unit, so keep product weights accurate for the figure to be meaningful.

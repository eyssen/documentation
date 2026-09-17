================
Units of measure
================

.. |UOM| replace:: :abbr:`UoM (Unit of Measure)`
.. |PO| replace:: :abbr:`PO (Purchase Order)`
.. |POs| replace:: :abbr:`POs (Purchase Orders)`
.. |RFQ| replace:: :abbr:`RFQ (Request for Quotation)`
.. |SO| replace:: :abbr:`SO (Sales Order)`

In some cases, handling products in different units of measure is necessary. For example, a business
can buy products from a country that uses the metric system, and then sell those products in a
country that uses the imperial system. In that case, the business needs to convert the units.

Another case for unit conversion is when a business buys products in a big pack from a supplier, and
then sells those products in individual units.

Odoo can be set up to use different *units of measure (UoM)* for one product.

Configuration
=============

To use different units of measure in Odoo, first go to :menuselection:`Inventory app -->
Configuration --> Settings`, and under the :guilabel:`Products` section, activate the
:guilabel:`Units of Measure` setting. Then, click :guilabel:`Save`.

.. screenshot:: inventory-uom-enable-setting
   :menu: Inventory ‣ Configuration ‣ Settings
   :shows: The Inventory settings page scrolled to the "Products" section, with the "Units of Measure"
      checkbox enabled.
   :highlight: The "Units of Measure" checkbox (red frame).
   :data: Demo company "YourCompany".
   :module: stock, uom
   :notes: English UI, light theme, 1440px width, crop to the "Products" settings block.

Units of measure categories
===========================

After enabling the *Units of Measure* setting, view the default units of measure categories in
:menuselection:`Inventory app --> Configuration --> UoM Categories`. The category is important for
unit conversion; Odoo can convert a product's units from one unit to another **only** if both units
belong to the same category.

.. screenshot:: inventory-uom-categories
   :menu: Inventory ‣ Configuration ‣ UoM Categories
   :shows: The "Units of Measure Categories" list with the default categories (Units, Weight, Working Time,
      Length / Distance, Volume) and their reference unit shown in the "Uom" column.
   :highlight: The reference unit values in the "Uom" column (they are rendered in blue).
   :data: Default Odoo unit-of-measure categories, no custom category added yet.
   :module: uom
   :notes: English UI, light theme, 1440px width, crop to the list.

Each units of measure category has a reference unit. The reference unit is highlighted in blue in
the :guilabel:`Uom` column of the :guilabel:`Units of Measure Categories` page. Odoo uses the
reference unit as a base for any new units.

To create a new unit, first select the correct category from the :guilabel:`Units of Measure
Categories` page. For example, to sell a product in a box of six units, click the :guilabel:`Unit`
category line. Then, on the category page that appears, click :guilabel:`Add a line` in the
:guilabel:`Units of Measure` tab. Then, in the :guilabel:`Unit of Measure` field, title the new
unit, such as `Box of 6`, then in the :guilabel:`Type` field, select the appropriate size reference,
such as :guilabel:`Bigger than the reference Unit of Measure`.

If applicable, enter a :guilabel:`UNSPSC Category`, which is a globally recognized `code managed by
GS1 <https://www.unspsc.org/>`_, that **must** be purchased in order to use.

In the :guilabel:`Ratio` field, enter how many individual units are in the new |UOM|, such as
`6.00000` when using the example of the `6-Pack` (since a box of six is six times *bigger* than the
reference unit, `1.00000`).

.. screenshot:: inventory-uom-new-unit
   :menu: Inventory ‣ Configuration ‣ UoM Categories ‣ Units
   :shows: The "Units" category form, "Units of Measure" tab, with a new line named "Box of 6", Type "Bigger
      than the reference Unit of Measure" and Ratio 6.00000 next to the reference unit "Units" (ratio
      1.00000).
   :highlight: The newly added "Box of 6" line (red frame).
   :data: Demo company "YourCompany"; the "Units" category with its default "Units" and "Dozens" units plus
      the new "Box of 6".
   :module: uom
   :notes: English UI, light theme, 1440px width, crop to the units table.

Specify a product's units of measure
====================================

To set units of measure on a product, first go to :menuselection:`Inventory app --> Products -->
Products` and select a product to open its product form page.

In the :guilabel:`General Information` tab, edit the :guilabel:`Unit of Measure` field to specify
the unit of measure that the product is sold in. The specified unit is also the unit used to keep
track of the product's inventory and internal transfers.

Edit the :guilabel:`Purchase UoM` field to specify the unit of measure that the product is purchased
in.

Advanced units of measure
=========================

The eYssen *Advanced UoM* module (``eyssen_uom``) extends unit-of-measure categories so that derived
quantities — surfaces, volumes and specific gravity — can be computed from a length or a weight unit
instead of being maintained by hand.

Category type
-------------

On every unit-of-measure category (:menuselection:`Inventory app --> Configuration --> UoM
Categories`), a :guilabel:`Type` field classifies what the category measures:
:guilabel:`Unit`, :guilabel:`Weight`, :guilabel:`Time`, :guilabel:`Working Time`,
:guilabel:`Length / Distance`, :guilabel:`Surface`, :guilabel:`Volume` or
:guilabel:`Specific Gravity`. The type is also shown as a column on the
:guilabel:`Units of Measure Categories` list, and is inherited (read-only) by every unit in the
category.

The type decides which reference fields appear on the units inside the category:

- For a :guilabel:`Surface` or :guilabel:`Volume` category, each unit gets a
  :guilabel:`Reference Length` field — the length unit the surface or volume is derived from (for
  example `cm` for `cm³`).
- For a :guilabel:`Specific Gravity` category, each unit gets a :guilabel:`Reference Weight` and a
  :guilabel:`Reference Volume` field (for example `g` and `cm³` for `g/cm³`).

The module also raises the precision of the :guilabel:`Ratio` column to ten decimals, which is
needed for conversions between volume and specific-gravity units.

.. note::
   The module adds the :guilabel:`Specific Gravity` and :guilabel:`Time` categories and the `cm³`,
   `g/cm³`, `kg/m³`, `Month` and `Year` units, if they are not present yet.

.. screenshot:: inventory-uom-category-type
   :menu: Inventory ‣ Configuration ‣ UoM Categories ‣ (a category)
   :shows: A unit-of-measure category form with the eYssen "Type" field set to "Specific Gravity", and the
      units table below showing the "Reference Weight" and "Reference Volume" columns filled in for the
      "g/cm³" unit.
   :highlight: The "Type" field and the "Reference Weight" / "Reference Volume" columns (red frames).
   :data: Category "Specific Gravity" with the units "g/cm³" (reference) and "kg/m³".
   :module: eyssen_uom
   :notes: English UI, light theme, 1440px width, crop to the form and the units table.

UNECE codes
-----------

With the ``uom_unece`` module installed, every unit of measure carries a :guilabel:`UNECE Code`
field, holding the code of the unit in the standard nomenclature of the United Nations Economic
Commission for Europe. The codes are pre-loaded for the standard units and are used by electronic
document formats that require a standardized unit code.

.. note::
   The Hungarian e-invoicing and electronic reporting formats expect UNECE unit codes. Keep this
   field filled in on every unit that appears on customer documents.

.. _inventory/product_replenishment/unit-conversion:

Unit conversion
===============

Odoo automatically converts unit measurements when products have different :abbr:`UoMs (Units of
Measure)` and purchase :abbr:`UoMs (Units of Measure)`.

This occurs in various scenarios, including:

#. :ref:`Vendor orders <inventory/product_replenishment/buy-in-uom>`: purchase |UOM| on purchase
   orders (POs) converts to |UOM| on internal warehouse documents
#. :ref:`Automatic replenishment <inventory/product_replenishment/replenish>`: generates |POs| when
   the stock levels of a product (tracked in |UOM|) dips below a certain level. But, the |POs| are
   created using the purchase |UOM|
#. :ref:`Sell products <inventory/product_replenishment/sell-in-uom>`: if a different |UOM| is used
   on the sales order (SO), the quantity is converted to the warehouse's preferred |UOM| on the
   delivery order

.. _inventory/product_replenishment/buy-in-uom:

Buy products in the purchase UoM
--------------------------------

When creating a new request for quotation (RFQ) in the *Purchase* app, Odoo automatically uses the
product's specified purchase unit of measure. If needed, manually edit the :guilabel:`UoM` value on
the |RFQ|.

After the |RFQ| is confirmed into a |PO|, click the :guilabel:`Receipt` smart button at the top of
the |PO|.

Odoo automatically converts the purchase unit of measure into the product's sales/inventory unit of
measure, so the :guilabel:`Demand` column of the delivery receipt shows the converted quantity.

.. example::
   When the product's purchase :guilabel:`UoM` is `Box of 6`, and its sales/inventory unit of
   measure is `Units`, the |PO| shows the quantity in boxes of six, and the receipt (and other
   internal warehouse documents) shows the quantity in units.

   .. screenshot:: inventory-uom-purchase-order
      :menu: Purchase ‣ Orders ‣ Purchase Orders ‣ (a confirmed order)
      :shows: A confirmed purchase order line for a product whose purchase unit of measure is "Box of 6":
         Quantity 3 and UoM "Box of 6".
      :highlight: The "UoM" cell showing "Box of 6" and the "Quantity" cell showing 3 (red frame).
      :data: Vendor "Azure Interior"; one order line, product with Unit of Measure "Units" and Purchase UoM
         "Box of 6".
      :module: purchase, uom
      :notes: English UI, light theme, 1440px width, crop to the order lines. Caption to convey: an order of
         three quantities placed in the purchase UoM "Box of 6".

   .. screenshot:: inventory-uom-receipt
      :menu: Purchase ‣ Orders ‣ Purchase Orders ‣ (the same order) ‣ Receipt
      :shows: The receipt generated from the purchase order above, with the Demand column showing 18 Units —
         the three boxes of six converted into the product's inventory unit of measure.
      :highlight: The "Demand" quantity and the "Units" unit of measure on the operation line (red frame).
      :data: The receipt WH/IN/00001 for the same product and vendor as the purchase order screenshot.
      :module: stock, uom
      :notes: English UI, light theme, 1440px width, crop to the Operations tab. Caption to convey: on
         warehouse receipt the recorded quantities are in the internal unit of measure "Units".

.. _inventory/product_replenishment/replenish:

Replenishment
-------------

A request for quotation for a product can also be generated directly from the product form using
the :guilabel:`Replenish` button.

After clicking :guilabel:`Replenish`, a replenish assistant box pops up. The purchase unit of
measure can be manually edited in the :guilabel:`Quantity` field, if needed. Then, click
:guilabel:`Confirm` to create the |RFQ|.

.. important::
   A |PO| can **only** be automatically generated if at least **one** vendor is listed in the
   product form's :guilabel:`Purchase` tab.

.. screenshot:: inventory-uom-replenish
   :menu: Inventory ‣ Products ‣ Products ‣ (a product)
   :shows: A product form with the "Replenish" button visible in the button box at the top of the form.
   :highlight: The "Replenish" button (red frame).
   :data: A storable product that has at least one vendor on its "Purchase" tab.
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the top of the product form.

Navigate to the created |PO| by clicking the :guilabel:`Forecasted` smart button on the product
form. Scroll down to the :guilabel:`Forecasted Inventory` section, and in the :guilabel:`Requests
for quotation` line, click the |RFQ| reference number to open the draft |RFQ|. If necessary, the
purchase |UOM| can be edited directly on the |PO|.

.. _inventory/product_replenishment/sell-in-uom:

Sell in a different UoM
-----------------------

When creating a new quotation in the *Sales* app, Odoo automatically uses the product's specified
unit of measure. If needed, the :guilabel:`UoM` can be manually edited on the quotation.

After the quotation is sent to the customer, and confirmed into a sales order (SO), click the
:guilabel:`Delivery` smart button at the top of the |SO|. Odoo automatically converts the unit of
measure into the product's inventory unit of measure, so the :guilabel:`Demand` column of the
delivery shows the converted quantity.

For example, if the product's |UOM| on the |SO| was changed to `Box of 6`, but its inventory unit of
measure is `Units`, the |SO| shows the quantity in boxes of six, and the delivery shows the quantity
in units.

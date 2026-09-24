==========================
Product data extensions
==========================

The eYssen modules on this page extend the product record itself: they add a dedicated
**Products** app menu, a rule-driven internal reference generator, a material composition, a
product lifecycle stage that can gate sales and purchases, seasons, computed dimensions, product
images in list views and bulk media upload. Every module is independent — install only the ones a
company needs.

Products app
============

``eyssen_product`` adds a stand-alone :guilabel:`Products` application, so product data can be
maintained without going through **Inventory** or **Sales**:

- :menuselection:`Products --> Products` and :menuselection:`Products --> Product Variants`;
- :menuselection:`Products --> Configuration --> Product Categories` and
  :menuselection:`Products --> Configuration --> Attributes`; and
- :menuselection:`Products --> Configuration --> Product Families`, a simple list of product
  families with a :guilabel:`Name` and a :guilabel:`Description`.

.. screenshot:: inventory-product-data-products-app
   :menu: Products
   :shows: The eYssen "Products" app with its menu bar open, showing the Products, Product Variants,
      Reports and Configuration menus.
   :highlight: The app's menu bar (red frame).
   :data: A catalog with a few hundred products.
   :module: eyssen_product
   :notes: English UI, light theme, 1440px width, crop to the top of the page with the menu open.

.. note::
   :guilabel:`Product Families` are currently only a list of records: no field on the product links
   to a family yet, so the list serves as a reference table until that link is added.

Generated internal references
=============================

``eyssen_product_default_code`` generates a product's :guilabel:`Internal Reference` from rules
instead of leaving it to be typed by hand, so references stay consistent and predictable across a
large catalog.

Reference rules
---------------

Rules live under :menuselection:`Products --> Configuration --> Reference Rules`. Each rule has a
:guilabel:`Name`, a :guilabel:`Company`, a :guilabel:`Sequence` (which rule is tried first), an
:guilabel:`Active` flag and a :guilabel:`Filter Type` that decides which products it applies to.
A read-only :guilabel:`Preview` shows what a reference built by the rule looks like.

A rule is built from ordered **lines**, each contributing one part of the reference:

- a fixed text part (its :guilabel:`Chars` value);
- a part taken from a product **attribute** — with :guilabel:`Attribute Value Field` choosing
  between the value's :guilabel:`Name` and its :guilabel:`Reference Value`; or
- a **sequence** number, with a configurable :guilabel:`Sequence Padding` (number of digits,
  four by default) and :guilabel:`Start Number`, counted per the fields listed in the line.

.. screenshot:: inventory-product-data-reference-rule
   :menu: Products ‣ Configuration ‣ Reference Rules ‣ (a rule)
   :shows: A reference rule form with its Name, Company, Sequence, Filter Type and the read-only Preview,
      and the rule lines below showing a fixed-text part, an attribute part and a sequence part with its
      padding and start number.
   :highlight: The "Preview" field and the rule lines (red frames).
   :data: A rule producing references such as "SH-BLK-0001" from a fixed prefix, the Colour attribute and a
      four-digit sequence.
   :module: eyssen_product_default_code
   :notes: English UI, light theme, 1440px width, full form.

Reference values on attributes and categories
---------------------------------------------

So that a reference stays short, an attribute value carries a separate
:guilabel:`Product Reference Value` (for example `BLK` for the colour *Black*), used instead of its
full name when a rule's line is set to use the reference value. Product categories carry a
:guilabel:`Sequence for default code`, which lets the sequence part of a reference be counted per
category.

.. screenshot:: inventory-product-data-attribute-reference-value
   :menu: Products ‣ Configuration ‣ Attributes ‣ (an attribute)
   :shows: An attribute's value list with the "Product Reference Value" column filled in next to each value's
      name.
   :highlight: The "Product Reference Value" column (red frame).
   :data: Attribute "Colour" with the values Black/BLK, White/WHT and Red/RED.
   :module: eyssen_product_default_code
   :notes: English UI, light theme, 1440px width, crop to the value list.

Material composition
====================

``eyssen_product_material`` records what a product is made of, in percentages, which is required
for textile and footwear labelling among others.

The materials are maintained under :menuselection:`Products --> Configuration --> Materials`. Each
material has a translatable :guilabel:`Material Name` and belongs to a :guilabel:`Material Group`
(for example *Upper*, *Lining*, *Sole*); a group has a translatable :guilabel:`Group Name` and a
:guilabel:`Sequence` that orders the groups on a product.

On the product form, one line per material records the :guilabel:`Material Group`, the
:guilabel:`Material` and its :guilabel:`Percentage`. A computed :guilabel:`Material Info` summary
and a rendered :guilabel:`Material Pct` breakdown make the composition easy to read and to reuse on
reports.

.. screenshot:: inventory-product-data-material
   :menu: Inventory ‣ Products ‣ Products ‣ (a product)
   :shows: The material lines of a product form, each with its Material Group, Material and Percentage, and
      the computed composition summary next to them.
   :highlight: The material lines and the computed summary (red frames).
   :data: A shoe with Upper 100% leather, Lining 100% textile and Sole 100% rubber.
   :module: eyssen_product_material
   :notes: English UI, light theme, 1440px width, crop to the material section.

Product stages
==============

``eyssen_product_stage`` gives every product a lifecycle :guilabel:`Stage`, and lets each stage
decide what may be done with the product. This is how an unfinished product record is kept out of
quotations, orders and deliveries until its data is complete.

Stages are configured under :menuselection:`Products --> Configuration --> Product Stages`. A stage has:

- a translatable :guilabel:`Name`, a :guilabel:`Sequence`, a :guilabel:`Color` and an
  :guilabel:`Active` flag;
- :guilabel:`Required Fields` and :guilabel:`Required Attributes` — what must be filled in on the
  product before it can reach the stage;
- :guilabel:`Groups` and :guilabel:`Users` — who may move a product into the stage;
- the permission switches :guilabel:`Allow Sale Order Send`, :guilabel:`Allow Sale Order Confirm`,
  :guilabel:`Allow Purchase Order Send`, :guilabel:`Allow Purchase Order Confirm`,
  :guilabel:`Allow Stock Picking` and :guilabel:`Allow Account Move`, all enabled by default; and
- :guilabel:`Create Reference`, which generates the product's internal reference (see above) when
  it does not have one yet.

.. screenshot:: inventory-product-data-stage-form
   :menu: Products ‣ Configuration ‣ Stages ‣ (a stage)
   :shows: A product stage form with the Name, Sequence and Color, the Required Fields and Required
      Attributes lists, the Groups and Users restrictions, and the six permission switches.
   :highlight: The permission switches (red frame).
   :data: Stage "Draft" with Allow Sale Order Confirm and Allow Stock Picking disabled.
   :module: eyssen_product_stage
   :notes: English UI, light theme, 1440px width, full form.

The product's :guilabel:`Stage` is tracked in the chatter, and a product variant inherits the stage
of its template. When a document contains a product whose stage does not allow the operation, that
action — sending or confirming a quotation, sending or confirming a purchase order, validating a
transfer, or posting an invoice — is blocked with an error naming the product.

.. screenshot:: inventory-product-data-stage-blocked
   :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation) ‣ Confirm
   :shows: The error raised when confirming a quotation that contains a product whose stage does not allow
      sales order confirmation, naming the product and its stage.
   :highlight: The error text (red frame).
   :data: One order line for a product in the "Draft" stage.
   :module: eyssen_product_stage
   :notes: English UI, light theme, 1440px width, crop to the error dialog.

Seasons
=======

``eyssen_product_season`` groups products into selling seasons. A season
(:menuselection:`Sales --> Configuration --> Szezonok`) has a name, a start and an end date, a
colour and the list of products that belong to it, with a counter showing how many products it
contains. On the product form, a product can belong to several seasons at once.

.. note::
   The labels of this module are currently Hungarian in the source code (*Szezon*, *Szezon
   kezdete*, *Szezon vége*, *Termékek*), so they appear in Hungarian regardless of the interface
   language until translations are added.

.. screenshot:: inventory-product-data-seasons
   :menu: Products ‣ Configuration ‣ Seasons
   :shows: The seasons list with each season's name, start and end date and the number of products it
      contains, in the colours assigned to them.
   :highlight: None.
   :data: Four seasons, e.g. "SS25" and "AW25".
   :module: eyssen_product_season
   :notes: English UI, light theme, 1440px width, full list view. The field labels appear in Hungarian.

Dimensions and computed volume
==============================

``eyssen_product_dimension`` computes a product's volume from its physical dimensions instead of
having it typed in. In the :guilabel:`Dimensions` group of the product's :guilabel:`Inventory` tab,
choose a :guilabel:`Shape` — cuboid, cylinder, hollow section, tube or sphere — and only the
dimensions that shape needs remain visible:

- length, width and height/thickness for a cuboid or a hollow section;
- length and diameter for a cylinder or a tube;
- diameter only for a sphere; and
- a wall thickness for a hollow section or a tube.

From those, the product's :guilabel:`Volume` and a :guilabel:`Net Volume` (the volume of the
material itself, so a hollow section or tube excludes its cavity) are computed, converted into the
company's volume unit of measure through the :guilabel:`Dimensional UoM`. The module also adds the
same dimension, volume and weight fields, each with its own unit of measure, to
:doc:`packagings <configure/packaging>`.

.. screenshot:: inventory-product-data-dimensions
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ Inventory tab
   :shows: The "Dimensions" group of a product form with the "Shape" field set to "Hollow section", the
      length, width, height and wall thickness fields visible, and the computed Net Volume below them.
   :highlight: The "Shape" field and the computed "Net Volume" (red frames).
   :data: A steel hollow section, 6000 x 40 x 40 mm with a 2 mm wall.
   :module: eyssen_product_dimension
   :notes: English UI, light theme, 1440px width, crop to the group. Some field labels appear in Hungarian.

.. important::
   The volume computation reads the reference length unit of the company's volume unit of measure,
   which is set up by the :ref:`Advanced UoM module <inventory/uom/advanced>`. If those units are
   not configured, saving dimensions raises a validation error.

.. note::
   The length, width, height, diameter and wall-thickness labels are currently Hungarian in the
   source code, as are the shape names.

Product image in list views
===========================

``eyssen_product_list_view_image`` adds the product image as a small thumbnail column to the
products and product variants **list** views, so a catalog can be scanned visually without
switching to the kanban view. The column is shown by default and can be hidden from the
optional-column selector.

Bulk media upload
=================

``product_media`` speeds up maintaining a product's extra images:

- an :guilabel:`Upload Media` action takes several files at once and creates one extra product
  image per file, named after the file;
- an :guilabel:`Set as Main Image` action on an extra image swaps it with the product's main image;
  and
- a :guilabel:`Delete All Extra Media` action clears every extra image of a product in one step.

.. note::
   This module targets the webshop's product gallery. The webshop-side presentation of those images
   is documented with the **Website** application.

Bill of materials on the product form
=====================================

``eyssen_mrp_bom_on_product`` makes a product's bill of materials editable directly on the product
form, instead of only in the **Manufacturing** app. A :guilabel:`Selected BoM` field picks which
bill of materials is shown, and the fields below it — :guilabel:`Reference`, :guilabel:`BoM Type`,
:guilabel:`Quantity`, :guilabel:`Unit of Measure`, the component lines, the by-products, the
operations, :guilabel:`Manufacturing Readiness`, :guilabel:`Operation Type`,
:guilabel:`Flexible Consumption`, :guilabel:`Operation Dependencies`,
:guilabel:`Manufacturing Lead Time` and :guilabel:`Days to prepare Manufacturing Order` — all edit
that bill of materials in place. Buttons step through the product's bills of materials and create a
new one, and the component and by-product lists can be filled from the
:doc:`product catalog <../warehouses_storage/inventory_management/product_catalog>`.

.. seealso::
   :doc:`Bills of materials <../../manufacturing/basic_setup/bill_configuration>`

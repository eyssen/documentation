==========================
Product data extensions
==========================

The eYssen modules on this page extend the product record itself: they add a dedicated
**Products** app menu, a rule-driven internal reference generator, a material master with
densities and a material composition, a product lifecycle stage that can gate sales and purchases,
seasons, computed dimensions and weights, product images in list views and bulk media upload. Every module is independent — install only the ones a
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

.. _inventory/product_data/material:

Materials and material composition
==================================

``eyssen_product_material`` keeps a master list of materials. It records what a product is made of,
in percentages, which is required for textile and footwear labelling among others, and it holds the
technical data (grade, standard and density) that weight calculations need, for example for steel
structures (see :doc:`../../manufacturing/cad_bom_import`).

The materials are maintained under :menuselection:`Products --> Configuration --> Materials`. Each
material has a translatable :guilabel:`Material Name` and belongs to a :guilabel:`Material Group`
(for example *Upper*, *Lining*, *Sole*, or *Steel (structural)*); a group has a translatable
:guilabel:`Group Name` and a :guilabel:`Sequence` that orders the groups on a product. In addition, a
material has:

- a :guilabel:`Code`, the short designation of the material or grade, such as ``S235JR``, ``1.4301``
  or ``EN AW-6060``;
- a :guilabel:`Standard` that defines it, such as EN 10025-2;
- :guilabel:`Aliases`, other designations of the same material separated by commas (for example
  ``OL37, St37-2, Fe360`` for S235JR); and
- a :guilabel:`Density` with its :guilabel:`Density Unit` (a unit of the *Specific Gravity*
  category, kg/m³ by default). :guilabel:`Density (kg/m³)` shows the value converted to kg/m³, which
  is the value used in computations.

The search box of the list finds a material by name, code or alias. When another module looks up a
designation (the CAD import does, for the grades written on a drawing), the comparison ignores case,
accents, spaces, dashes and dots, so ``St 37-2`` finds the material that lists ``St37-2``. There is
no approximate match: a designation that is not in the master, such as S275J0 when only S275JR
exists, is not replaced by a similar one.

The standard data contains three groups and eight materials:

.. list-table::
   :header-rows: 1
   :widths: 30 25 25 20

   * - Material
     - Group
     - Standard
     - Density (kg/m³)
   * - S235JR (aliases S235, OL37, St37-2, Fe360, ...)
     - Steel (structural)
     - EN 10025-2
     - 7850
   * - S275JR (S275, OL44, St44-2, Fe430, ...)
     - Steel (structural)
     - EN 10025-2
     - 7850
   * - S355J2 (S355, OL52, St52-3, Fe510, ...)
     - Steel (structural)
     - EN 10025-2
     - 7850
   * - S460 (S460N, S460NL, S460M, S460ML)
     - Steel (structural)
     - EN 10025-3 and -4
     - 7850
   * - 1.4301 (AISI 304)
     - Stainless steel
     - EN 10088-2
     - 7900
   * - 1.4404 (AISI 316L)
     - Stainless steel
     - EN 10088-2
     - 8000
   * - EN AW-6060
     - Aluminium
     - 
     - 2700
   * - EN AW-6082
     - Aluminium
     - 
     - 2700

On the product form, the tab :guilabel:`Materials` has one line per material with the
:guilabel:`Material Group`, the :guilabel:`Material` and its :guilabel:`Percentage`. A computed
:guilabel:`Material Info` summary and a rendered :guilabel:`Material Pct` breakdown make the
composition easy to read and to reuse on reports.

Below them, the :guilabel:`Main Material` is the material used for weight computations, and
:guilabel:`Density (kg/m³)` shows its density. It is filled in from the composition line with the
highest percentage (the first group wins a tie), and it can also be set directly, for example to the
steel grade of a profile that has no composition lines. Without composition lines the material you set
is kept.

.. screenshot:: inventory-product-data-material
   :menu: Inventory ‣ Products ‣ Products ‣ (a product)
   :shows: The material lines of a product form, each with its Material Group, Material and Percentage, and
      the computed composition summary and the Main Material next to them.
   :highlight: The material lines, the computed summary and the Main Material (red frames).
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

.. _inventory/product_data/dimensions:

Dimensions, computed volume and weight
======================================

``eyssen_product_dimension`` computes a product's volume, and optionally its weight, from its
physical dimensions instead of having them typed in. In the :guilabel:`Dimensions` group of the
product's :guilabel:`Inventory` tab, choose a :guilabel:`Shape`: :guilabel:`Cuboid`,
:guilabel:`Cylinder`, :guilabel:`Hollow Section`, :guilabel:`Tube`, :guilabel:`Sphere` or
:guilabel:`Open Profile`. Only the dimensions that shape needs remain visible:

- length (x), width (y) and height/thickness (z) for a cuboid or a hollow section;
- length (x) and diameter (d) for a cylinder or a tube;
- diameter (d) only for a sphere;
- a wall thickness (wt) for a hollow section or a tube; and
- for an open profile, the length (x), the height (z) as *h*, the width (y) as *b*, the web thickness
  (wt) and, for I, H and U profiles, the flange thickness (tf).

All dimensions are in the :guilabel:`Dimensional UoM` of the product (millimetres, for example).

Open profiles
-------------

The shape :guilabel:`Open Profile` describes rolled and cold-formed sections. Its
:guilabel:`Profile Type` is one of:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Profile type
     - Cross-section area
   * - :guilabel:`I / H`
     - 2 x b x tf + (h - 2 x tf) x tw
   * - :guilabel:`U (channel)`
     - The same formula, with one web.
   * - :guilabel:`L (angle)`
     - t x (h + b - t), with the two legs h and b and the thickness t.
   * - :guilabel:`Z` and :guilabel:`C`
     - t x (h + 2 x b - 2 x t), on the centre line of the sheet. Lips are ignored.
   * - :guilabel:`Other`
     - Not computed: enter the :guilabel:`Cross-section Area` directly, for example from a catalogue.

Root and toe radii of rolled sections are ignored, so the computed area is slightly smaller than a
catalogue value; type the catalogue area in :guilabel:`Cross-section Area` when you need it exact.

Volume, area and weight
-----------------------

From the dimensions, the product's :guilabel:`Volume` (the gross volume of the enclosing shape) and a
:guilabel:`Net Volume` (the volume of the material itself, so a hollow section or tube excludes its
cavity) are computed, converted into the company's volume unit of measure through the
:guilabel:`Dimensional UoM`. The :guilabel:`Cross-section Area` is the area perpendicular to the length:
it is computed for every shape except the sphere (and :guilabel:`Other` profiles), and it can be
entered by hand for profiles.

When the product has a :ref:`Main Material <inventory/product_data/material>` with a density, the
:guilabel:`Computed Weight` is the net weight of **one unit of measure of the product**:

- for a product measured by length (m), the weight per metre: cross-section area x density;
- for a product measured by area (m²), the weight per m² (cuboid plates: thickness x density);
- for a product measured by volume, volume x density;
- for a product measured by weight, that weight; and
- otherwise, the weight of one piece.

The weight of the product itself is never overwritten unless you ask for it:

- tick :guilabel:`Weight from Dimensions` and the product's :guilabel:`Weight` always equals the
  computed weight, also when the dimensions, the unit of measure, the main material or the density of
  the material change later; or
- click :guilabel:`Compute weight` to set the weight once.

The module also adds the same dimension, volume and weight fields, each with its own unit of measure,
to :doc:`packagings <configure/packaging>`.

.. screenshot:: inventory-product-data-dimensions
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ Inventory tab
   :shows: The "Dimensions" group of a product form with the "Shape" field set to "Open Profile" and the
      profile type "I / H", the dimension fields, the Cross-section Area, the Net Volume, the Computed
      Weight and the "Weight from Dimensions" checkbox.
   :highlight: The "Shape" field, the "Cross-section Area" and the "Weight from Dimensions" checkbox (red
      frames).
   :data: A steel IPE 200 beam (h 200, b 100, tw 5.6, tf 8.5 mm), unit of measure metre, main material
      S235JR.
   :module: eyssen_product_dimension
   :notes: English UI, light theme, 1440px width, crop to the group.

.. important::
   The computation reads the reference length unit of the company's volume unit of measure, which is
   set up by the :ref:`Advanced UoM module <inventory/uom/advanced>`. If those units are not
   configured, saving dimensions raises a validation error. The module also checks that the
   thicknesses fit the dimensions (twice the wall thickness cannot reach the width or height) and
   that no dimension is negative.

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

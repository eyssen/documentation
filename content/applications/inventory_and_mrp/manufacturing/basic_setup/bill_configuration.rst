=================
Bill of materials
=================

.. |BOM| replace:: :abbr:`BoM (Bill of Materials)`
.. |BOMs| replace:: :abbr:`BoMs (Bills of Materials)`
.. |MO| replace:: :abbr:`MO (Manufacturing Order)`

A *bill of materials* (or *BoM* for short) documents specific components, along with their
respective quantities, that are needed to produce or repair a product. In Odoo, |BoMs| serve as
blueprints for manufactured goods and kits, and often include production operations and step-by-step
guidelines, as well.

BoM setup
=========

To create a |BOM|, go to :menuselection:`Manufacturing app --> Products --> Bills of Materials` and
click :guilabel:`New`.

Next, set the :guilabel:`BoM Type` to :guilabel:`Manufacture this product`.

Then, specify :ref:`required components <manufacturing/basic_setup/setup-components>` and, if
necessary, define any :ref:`manufacturing operations <manufacturing/basic_setup/setup-operations>`.

.. tip::
   Individual |BOMs| can also be quickly accessed or created by clicking the :guilabel:`Bill of
   Materials` smart button on any product form, as accessible through the *Sales*, *Inventory*, and
   *Manufacturing* apps, as well as through any internal links where a product is referenced (such
   as in a field or a line item).

The |BOM| form also has the following header fields:

- :guilabel:`Product Variant`: restricts the |BOM| to one specific variant of the product; only
  shown when the product has :doc:`variants <../advanced_configuration/product_variants>`. When
  left blank, the |BOM| applies to every variant.
- :guilabel:`Quantity`: the smallest quantity that this |BOM| can produce. If the |BOM| uses
  operations, make sure this matches the work center's capacity.
- :guilabel:`Reference`: an optional internal code for the |BOM|.
- :guilabel:`BoM Type`: besides :guilabel:`Manufacture this product` and :guilabel:`Kit`, a
  :guilabel:`Subcontracting` type becomes available once subcontracting is configured (see
  :doc:`../subcontracting/subcontracting_basic`).
- :guilabel:`Company`: restricts the |BOM| to one company, in a multi-company database.

Once the |BOM| is saved, two smart buttons appear: :guilabel:`Operations Performance`, which opens
a report of the completed work orders for the |BOM|'s operations, and :guilabel:`BoM Overview`,
which opens a full breakdown of the |BOM|'s components, operations, and costs, including those of
any sub-assemblies.

.. screenshot:: manufacturing-bom-example
   :menu: Manufacturing ‣ Products ‣ Bills of Materials ‣ (BoM)
   :shows: A BoM form for product "Drawer", Components tab, listing several component lines with quantities.
   :data: Product "Drawer"; components "Drawer Case", "Drawer Slide", "Drawer Handle".
   :module: mrp
   :notes: English UI, light theme, 1440px width. Caption: "BoM for Drawer, Components tab."


.. seealso::
   - :doc:`../advanced_configuration/kit_shipping`
   - :doc:`../subcontracting/subcontracting_basic`
   - :doc:`Bill of materials on the product form
     <../../inventory/product_management/product_data>`

.. _manufacturing/basic_setup/setup-components:

Components
----------

In the :guilabel:`Components` tab of a |BOM|, specify components used to manufacture the product by
clicking :guilabel:`Add a line`. From the :guilabel:`Components` drop-down menu, select from
existing products or create a new product by typing the name and selecting either the
:guilabel:`Create " "` option to quickly add the line item, or the :guilabel:`Create and edit...`
option to add the component and continue to its configuration form. Alternatively, click
:guilabel:`Catalog` to add components from the product catalog view.

.. screenshot:: manufacturing-bom-add-component
   :menu: Manufacturing ‣ Products ‣ Bills of Materials ‣ (BoM) ‣ Components tab
   :shows: The Components tab with the product drop-down open, showing a search result and the "Create" and "Create and edit..." options.
   :highlight: The component drop-down menu.
   :data: BoM for product "Drawer"; searching for component "Drawer Handle".
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the tab.

Optionally, access additional fields by clicking the :icon:`oi-settings-adjust` :guilabel:`(settings
adjust)` icon to the far-right of the :guilabel:`Components` tab. Tick the checkboxes for the
following features to enable these columns:

- :guilabel:`Apply on Variants`: specify which :doc:`product variant
  <../advanced_configuration/product_variants>` each component is used in. When the field is left
  blank, the component is used in all product variants.

.. _manufacturing/basic_setup/consumed-in-operation:

- :guilabel:`Consumed in Operation`: specify the operation using the component. Useful for
  determining :ref:`manufacturing readiness <manufacturing/basic_setup/manufacturing-readiness>`.
- :guilabel:`Highlight Consumption`: tick the checkbox to force operators to check the
  :guilabel:`Consumed` checkbox on a manufacturing order (MO).

  .. screenshot:: manufacturing-bom-consumed-field
     :menu: Manufacturing ‣ Operations ‣ Manufacturing Orders ‣ (MO) ‣ Components tab
     :shows: The Components tab of an MO with a component line and its "Consumed" checkbox, unticked.
     :highlight: The "Consumed" checkbox.
     :data: MO "WH/MO/00001" for product "Drawer"; component "Drawer Handle".
     :module: mrp
     :notes: English UI, light theme, 1440px width, crop to the component line.

  Not doing so triggers the :guilabel:`Consumption Warning` error message, where the consumed
  component quantity must be manually inputted. Otherwise, the operation cannot be completed.

  .. screenshot:: manufacturing-bom-consumption-warning
     :menu: Manufacturing ‣ Operations ‣ Manufacturing Orders ‣ (MO) ‣ Produce All
     :shows: The "Consumption Warning" dialog listing a component whose consumed quantity differs from the BoM quantity, with a field to confirm the actual quantity used.
     :data: MO "WH/MO/00001" for "Drawer"; component "Drawer Handle" consumed 3 instead of 2.
     :module: mrp
     :notes: English UI, light theme, 1440px width, crop to the dialog.

.. _manufacturing/basic_setup/setup-operations:

Operations
----------

Add an *operation* to a |BOM| to specify instructions for production and register time spent on an
operation. To use this feature, first enable the *Work Orders* feature by going to
:menuselection:`Manufacturing app --> Configuration --> Settings`. In the :guilabel:`Operations`
section, tick the :guilabel:`Work Orders` checkbox to enable the feature.

.. seealso::
   :doc:`../advanced_configuration/work_order_dependencies`

.. screenshot:: manufacturing-bom-enable-work-orders
   :menu: Manufacturing ‣ Configuration ‣ Settings
   :shows: The Settings page scrolled to "Operations"; the "Work Orders" checkbox ticked.
   :highlight: The "Work Orders" checkbox.
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the setting block.

Next, navigate to the |BOM| by going to :menuselection:`Manufacturing app --> Products --> Bill of
Materials` and selecting the desired |BOM|. To add a new operation, go to the :guilabel:`Operations`
tab, and click :guilabel:`Add a line`.

.. tip::
   Every operation of every |BOM| can also be managed from a single list, by going to
   :menuselection:`Manufacturing app --> Configuration --> Operations`. From either list, click the
   :guilabel:`Archive Operation` button on an operation's form to archive it.

Doing so opens the :guilabel:`Create Operations` pop-up window, where the various fields of the
operation are configured:

- :guilabel:`Operation`: name of the operation.
- :guilabel:`Work Center`: select existing locations to perform the operation, or create a new work
  center by typing the name and selecting the :guilabel:`Create " "` option.
- :guilabel:`Apply on Variants`: specify if this operation is only available for certain product
  variants. If the operation applies to all product variants, leave this field blank.

  .. seealso::
     :doc:`Configuring BoMs for product variants <../advanced_configuration/product_variants>`

- :guilabel:`Duration Computation`: choose how time spent on the operation is tracked. Opt for
  :guilabel:`Compute based on tracked time` to use the operation's time tracker or :guilabel:`Set
  duration manually` if operators can record and modify time themselves.

  Choosing the :guilabel:`Compute based on tracked time` option enables the :guilabel:`Based on last
  __ work orders` option, which automatically estimates the time to complete this operation based on
  the last few operations. Choosing :guilabel:`Set duration manually` enables the :guilabel:`Default
  Duration` field instead.
- :guilabel:`Default Duration`: estimated amount of time to complete the operation; used for
  `planning manufacturing orders <https://www.youtube.com/watch?v=TK55jIq00pc>`_ and determining
  `work center availability <https://www.youtube.com/watch?v=3YwFlD97Bio>`_.
- :guilabel:`Company`: specify the company the |BOM| is available in.

Include operation details in the :guilabel:`Work Sheet` tab. Choose :guilabel:`PDF` to attach a file
or :guilabel:`Google Slide` with *public* access to share a link. Select :guilabel:`Text` to type
instructions in the :guilabel:`Description` text field.

.. tip::
   Type `/` for a list of formatting options and features, including ChatGPT.

   .. screenshot:: manufacturing-bom-description-chatgpt
      :menu: Manufacturing ‣ Products ‣ Bills of Materials ‣ (BoM) ‣ Operations tab ‣ (operation) ‣ Work Sheet ‣ Text
      :shows: The Description text field's power box (triggered by typing "/") listing formatting options, including a "ChatGPT" entry.
      :highlight: The "ChatGPT" entry in the power box.
      :module: mrp, web_editor
      :notes: English UI, light theme, 1440px width, crop to the power box.

.. screenshot:: manufacturing-bom-create-operations
   :menu: Manufacturing ‣ Products ‣ Bills of Materials ‣ (BoM) ‣ Operations tab ‣ Add a line
   :shows: The "Create Operations" pop-up window filled in with an Operation, Work Center, Duration Computation and Default Duration.
   :data: Operation "Assembly" on work center "Assembly Line 1", default duration 60 minutes.
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the dialog.

Finally, click :guilabel:`Save \& Close` to close the pop-up window. To add more operations, click
:guilabel:`Save & New` and repeat the same steps above to configure another operation.

.. note::
   Each operation is unique, as it is always exclusively linked to one |BOM|.

.. tip::
   After creating an operation, click the :guilabel:`Copy Existing Operations` button to choose an
   operation to duplicate.

   .. screenshot:: manufacturing-bom-copy-existing-operations
      :menu: Manufacturing ‣ Products ‣ Bills of Materials ‣ (BoM) ‣ Operations tab
      :shows: The Operations tab with the "Copy Existing Operations" link button, and a selection list of operations from other BoMs.
      :highlight: The "Copy Existing Operations" button.
      :module: mrp
      :notes: English UI, light theme, 1440px width, crop to the tab.

Miscellaneous
-------------

The :guilabel:`Miscellaneous` tab contains more |BoM| configurations to customize procurement,
calculate costs, and define how components are consumed.

.. _manufacturing/basic_setup/manufacturing-readiness:

- :guilabel:`Manufacturing Readiness`: choosing :guilabel:`When components for 1st operation are
  available` shows the :guilabel:`Component Status` as **available** as soon as the components
  consumed by the first operation are in stock. This indicates that although not all components are
  available, operators can at least begin with the first operation. Choosing :guilabel:`When all
  components are available` only shows the status as **available** once every component is in
  stock. The :guilabel:`Component Status` shown on a confirmed |MO| takes one of four values:
  :guilabel:`Available`, :guilabel:`Expected` (a receipt is scheduled in time), :guilabel:`Late`
  (a receipt is scheduled, but too late), or :guilabel:`Not Available`.

  .. tip::
     Specify which operation consumes each component on the |BoM| in the :ref:`Highlight
     Consumption field <manufacturing/basic_setup/consumed-in-operation>`.

  .. screenshot:: manufacturing-bom-component-status
     :menu: Manufacturing ‣ Operations ‣ Manufacturing Orders ‣ (confirmed MO)
     :shows: A confirmed MO with the "Component Status" smart button/label showing "Available" in green.
     :highlight: The "Component Status" indicator.
     :data: MO "WH/MO/00001" for product "Drawer", all components in stock.
     :module: mrp
     :notes: English UI, light theme, 1440px width, crop to the status area.

- :guilabel:`Flexible Consumption`: specifies if components used can deviate from the quantity
  defined on the |BoM|. Choose :guilabel:`Blocked` if operators **must** adhere strictly to the
  |BoM| quantity. Otherwise, choose :guilabel:`Allowed` or :guilabel:`Allowed with warning`.
- :guilabel:`Routing`: select the preferred warehouse's manufacturing operation type for products
  produced in multiple warehouses. If left blank, this warehouse's `Manufacturing` operation type is
  used by default.
- :guilabel:`Operation Dependencies`: enables sequencing rules between the |BOM|'s operations. See
  :doc:`../advanced_configuration/work_order_dependencies` for details.
- :guilabel:`Project`: link the |BOM| to a project, so that manufacturing orders created from it
  are automatically linked to that project too. Only visible with the *Project* app installed.
- :guilabel:`Manuf. Lead Time`: define the number of days needed to complete a |MO| from the date of
  confirmation.
- :guilabel:`Days to prepare Manufacturing Order`: number of days needed to replenish components, or
  manufacture sub-assemblies of the product. Click the :guilabel:`Compute` button to have Odoo
  calculate this value automatically, based on the components' and sub-assemblies' replenishment
  lead times.

.. seealso::
   :doc:`Lead times <../../inventory/warehouses_storage/replenishment/lead_times>`

.. screenshot:: manufacturing-bom-misc-tab
   :menu: Manufacturing ‣ Products ‣ Bills of Materials ‣ (BoM) ‣ Miscellaneous tab
   :shows: The Miscellaneous tab of a BoM with Manufacturing Readiness, Flexible Consumption, Routing, Manuf. Lead Time and Days to prepare Manufacturing Order fields filled in.
   :data: BoM for product "Drawer".
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the tab.

Add by-products to BoMs
=======================

A *by-product* is a residual product that is created during production in addition to the main
product of a |BOM|. Unlike the primary product, there can be more than one by-product on a |BOM|.

To add by-products to a |BOM|, first enable the *By-Products* feature in
:menuselection:`Manufacturing app --> Configuration --> Settings`. In the :guilabel:`Operations`
section, tick the checkbox for :guilabel:`By-Products` to enable the feature.

.. screenshot:: manufacturing-bom-byproducts-setting
   :menu: Manufacturing ‣ Configuration ‣ Settings
   :shows: The Settings page scrolled to "Operations"; the "By-Products" checkbox ticked.
   :highlight: The "By-Products" checkbox.
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the setting block.

Once the feature is enabled, add by-products to a |BOM| by clicking the :guilabel:`By-products` tab.
Click :guilabel:`Add a line` (or :guilabel:`Catalog` to pick one from the product catalog), and fill
in the :guilabel:`By-product`, :guilabel:`Quantity`, and :guilabel:`Unit of Measure`. Optionally,
specify a :guilabel:`Produced in Operation` for the by-product.

Two more columns can be enabled from the :icon:`oi-settings-adjust` :guilabel:`(settings adjust)`
icon at the top-right of the list: :guilabel:`Cost Share (%)`, the percentage of the |MO|'s total
production cost assigned to the by-product (the total of all by-products on a |BOM| cannot exceed
100%), and :guilabel:`Apply on Variants`, which restricts the by-product line to specific
:doc:`product variants <../advanced_configuration/product_variants>`.

.. example::
   The by-product, `Mush`, is created in the `Grind grapes` operation when producing `Red Wine`.

   .. screenshot:: manufacturing-bom-add-by-product
      :menu: Manufacturing ‣ Products ‣ Bills of Materials ‣ (BoM) ‣ By-products tab
      :shows: The By-products tab of the "Red Wine" BoM with a line for by-product "Mush", quantity and "Grind grapes" as the Produced in Operation.
      :data: BoM for product "Red Wine"; by-product "Mush"; operation "Grind grapes".
      :module: mrp
      :notes: English UI, light theme, 1440px width, crop to the tab.

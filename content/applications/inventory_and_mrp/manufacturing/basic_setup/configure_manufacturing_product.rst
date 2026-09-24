===================================
Manufacturing product configuration
===================================

.. _manufacturing/management/configure-manufacturing-product:
.. |BOM| replace:: :abbr:`BoM (Bill of Materials)`

In order to manufacture a product in Odoo *Manufacturing*, the product must be properly configured.
Doing so consists of enabling the *Manufacturing* route and configuring a bill of materials (BoM)
for the product. Once these steps are completed, the product is selectable when creating a new
manufacturing order.

Activate the Manufacture route
==============================

The Manufacture route is activated for each product on its own product page. To do so, begin by
navigating to :menuselection:`Manufacturing --> Products --> Products`. Then, select an existing
product, or create a new one by clicking :guilabel:`New`.

On the product page, select the :guilabel:`Inventory` tab, then enable the :guilabel:`Manufacture`
checkbox in the :guilabel:`Operations` section. This tells Odoo the product can be manufactured.

.. screenshot:: manufacturing-configure-product-route
   :menu: Manufacturing ‣ Products ‣ Products ‣ (product) ‣ Inventory tab
   :shows: The Inventory tab of a product form, "Operations" section, with the "Manufacture" route checkbox ticked among the other route checkboxes.
   :highlight: The "Manufacture" checkbox.
   :data: Product "Drawer".
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the "Operations" section.

.. _manufacturing/basic_setup/lot-serial-tracking:

Lot/serial number tracking
--------------------------

The assignment of lots or serial numbers to newly manufactured products is optional. To optionally
:doc:`assign lots or serial numbers <../../inventory/product_management/product_tracking>`
to newly manufactured products, go to the :guilabel:`General Information` tab. In the
:guilabel:`Tracking` field, select :guilabel:`By Unique Serial Number` or :guilabel:`By Lots`. This
field only appears once the *Lots & Serial Numbers* feature is enabled in
:menuselection:`Inventory app --> Configuration --> Settings`.

Doing so enables the :guilabel:`Lot/Serial Number` field on a confirmed manufacturing order, where
the produced lot or serial number is registered (or auto-generated, for products tracked by serial
number) before clicking :guilabel:`Produce All`.

.. screenshot:: manufacturing-configure-product-lot-field
   :menu: Manufacturing ‣ Operations ‣ Manufacturing Orders ‣ (confirmed MO)
   :shows: A confirmed MO for a serial-tracked product with the "Lot/Serial Number" field, next to the "Produce All" button, showing an auto-generated serial number.
   :highlight: The "Lot/Serial Number" field.
   :data: MO "WH/MO/00001" for a serial-tracked product.
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the top of the form.

Configure a bill of materials (BoM)
===================================

Next, a |BOM| must be configured for the product so Odoo knows how it is manufactured. A |BOM| is a
list of the components and operations required to manufacture a product.

To create a |BOM| for a specific product, navigate to :menuselection:`Manufacturing --> Products -->
Products`, then select the product. On the product page, click the :guilabel:`Bill of Materials`
smart button at the top of the page, then select :guilabel:`New` to configure a new |BOM|.

.. screenshot:: manufacturing-configure-product-bom-button
   :menu: Manufacturing ‣ Products ‣ Products ‣ (product)
   :shows: A product form with the "Bill of Materials" smart button in the button box.
   :highlight: The "Bill of Materials" smart button.
   :data: Product "Drawer", no BoM yet.
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the button box.

On the |BOM|, the :guilabel:`Product` field auto-populates with the product. In the
:guilabel:`Quantity` field, specify the number of units that the BoM produces.

Add a component to the |BOM| by selecting the :guilabel:`Components` tab and clicking :guilabel:`Add
a line`. Select a component from the :guilabel:`Component` drop-down menu, then enter the quantity
in the :guilabel:`Quantity` field. Continue adding components on new lines until all components have
been added.

.. screenshot:: manufacturing-configure-product-components-tab
   :menu: Manufacturing ‣ Products ‣ Bills of Materials ‣ (BoM) ‣ Components tab
   :shows: The Components tab with two component lines and their quantities filled in.
   :data: BoM for product "Drawer"; components "Drawer Case" and "Drawer Slide".
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the tab.

Next, select the :guilabel:`Operations` tab. Click :guilabel:`Add a line` and a :guilabel:`Create
Operations` pop-up window appears. In the :guilabel:`Operation` field, specify the name of the
operation being added (e.g. Assemble, Cut, etc.). Select the work center where the operation will be
carried out from the :guilabel:`Work Center` drop-down menu. Finally, click :guilabel:`Save & Close`
to finish adding operations, or :guilabel:`Save & New` to add more.

.. important::
   The :guilabel:`Operations` tab only appears if the :guilabel:`Work Orders` setting is enabled. To
   do so, navigate to :menuselection:`Manufacturing --> Configuration --> Settings`, then enable the
   :guilabel:`Work Orders` checkbox.

.. screenshot:: manufacturing-configure-product-operations-tab
   :menu: Manufacturing ‣ Products ‣ Bills of Materials ‣ (BoM) ‣ Operations tab
   :shows: The Operations tab with one operation line, "Assembly", assigned to work center "Assembly Line 1".
   :data: BoM for product "Drawer"; operation "Assembly" on work center "Assembly Line 1".
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the tab.

.. admonition:: Learn more

   The section above provides instructions for creating a basic |BOM| that allows a product to be
   manufactured in Odoo. However, it is by no means an exhaustive summary of all the options
   available when configuring a |BOM|. For more information about bills of materials, see the
   documentation on how to :doc:`create a bill of materials <bill_configuration>`.

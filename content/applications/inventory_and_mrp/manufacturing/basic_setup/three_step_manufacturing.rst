========================
Three-step manufacturing
========================

.. _manufacturing/management/three_step_manufacturing:
.. |BOM| replace:: :abbr:`BoM (Bill of Materials)`
.. |MO| replace:: :abbr:`MO (Manufacturing Order)`

Odoo *Manufacturing* allows users to manufacture products using one, two, or three steps. When using
three-step manufacturing, Odoo creates a pick components transfer, a manufacturing order (MO), and a
store finished products transfer, and updates inventory counts based on the number of components
removed, and finished products created.

.. tip::
   The number of steps used in manufacturing is set at the warehouse level, allowing for each
   warehouse to use a different number of steps. To change the number of steps used for a specific
   warehouse, begin by navigating to :menuselection:`Inventory --> Configuration --> Warehouses`,
   and then select a warehouse from the :guilabel:`Warehouses` screen.

   On the :guilabel:`Warehouse Configuration` tab, find the :guilabel:`Manufacture` radio input
   field, and select one of the three options: :guilabel:`Manufacture (1 step)`, :guilabel:`Pick
   components and then manufacture (2 steps)`, or :guilabel:`Pick components, manufacture and then
   store products (3 steps)`.

   .. screenshot:: manufacturing-three-step-warehouse-type
      :menu: Inventory ‣ Configuration ‣ Warehouses ‣ (warehouse)
      :shows: Warehouse configuration page, "Warehouse Configuration" tab, with the "Manufacture" radio field showing its three options and "Pick components, manufacture and then store products (3 steps)" selected.
      :highlight: The "Manufacture" radio input field.
      :data: Demo company "YourCompany"; warehouse "YourCompany".
      :module: mrp
      :notes: English UI, light theme, 1440px width, crop to the "Manufacture" field.

.. important::
   Products must be properly configured before they can be manufactured in Odoo. For details on how
   to do so, see the documentation on how to :ref:`configure a product for manufacturing
   <manufacturing/management/configure-manufacturing-product>`.

Create manufacturing order
==========================

To manufacture a product in Odoo *Manufacturing*, begin by navigating to
:menuselection:`Manufacturing --> Operations --> Manufacturing Orders`, and then click
:guilabel:`New` to create a new |MO|.

On the new |MO|, select the product to be produced from the :guilabel:`Product` drop-down menu. The
:guilabel:`Bill of Material` field auto-populates with the associated Bill of Materials (BoM).

If a product has more than one |BOM| configured for it, the specific |BOM| can be selected in the
:guilabel:`Bill of Material` field, and the :guilabel:`Product` field auto-populates with the
associated product.

After a |BOM| has been selected, the :guilabel:`Components` and :guilabel:`Work Orders` tabs
auto-populate with the components and operations specified on the |BOM|. If additional components or
operations are required for the |MO| being configured, add them to the :guilabel:`Components` and
:guilabel:`Work Orders` tabs by clicking :guilabel:`Add a line`.

Finally, click :guilabel:`Confirm` to confirm the |MO|.

Process pick components transfer
================================

After confirming a three-step |MO|, a :guilabel:`Transfers` smart button appears at the top of the
page. Click it to be taken to the :guilabel:`Transfers` page for the |MO|. The page lists two
transfers: *WH/PC/XXXXX* (the pick components transfer), and *WH/SFP/XXXXX* (the store finished
products transfer).

Select :guilabel:`WH/PC/XXXXX` to open the pick components transfer for the |MO|. This transfer is
used to track the movement of components from the locations where they are stored to the location
where they are used to manufacture the product.

After transferring the components out of their storage location, click :guilabel:`Validate` at the
top of the transfer, followed by :guilabel:`Apply` on the :guilabel:`Immediate Transfer?` pop-up
window that appears. Doing so marks the transfer as :guilabel:`Done`, and updates inventory counts
to reflect the quantity of components transferred.

Finally, return to the |MO| by clicking the :guilabel:`WH/MO/XXXXX` breadcrumb at the top of the
page.

.. screenshot:: manufacturing-three-step-mo-breadcrumb
   :menu: Manufacturing ‣ Operations ‣ Manufacturing Orders ‣ (MO) ‣ Transfers ‣ pick components transfer
   :shows: The validated pick components transfer with the "WH/MO/00001" breadcrumb link at the top, next to "WH/PC/00001" and "WH/SFP/00001".
   :highlight: The "WH/MO/00001" breadcrumb (red frame).
   :data: MO "WH/MO/00001" for product "Chair"; transfers "WH/PC/00001" and "WH/SFP/00001".
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the breadcrumb area.

Process manufacturing order
===========================

An |MO| is processed by completing all of the work orders listed under its :guilabel:`Work Orders`
tab. This can be done on the |MO| itself, or from the :guilabel:`Work Orders` list (see
:doc:`../workflows/work_orders`).

Basic workflow
--------------

To complete work orders from the |MO| itself, begin by navigating to :menuselection:`Manufacturing
--> Operations --> Manufacturing Orders`, and then select a manufacturing order.

On the |MO| page, select the :guilabel:`Work Orders` tab. Once work begins on the first work order
that needs to be completed, click the :guilabel:`Start` button for that work order. Odoo
*Manufacturing* then starts a timer that keeps track of how long the work order takes to complete.

.. screenshot:: manufacturing-three-step-start-button
   :menu: Manufacturing ‣ Operations ‣ Manufacturing Orders ‣ (MO) ‣ Work Orders tab
   :shows: The Work Orders tab of a confirmed MO with a work order line and its green "Start" button.
   :highlight: The "Start" button (red frame).
   :data: MO "WH/MO/00001" for product "Chair"; work order "Assembly" on work center "Assembly Line 1".
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the work order line.

When the work order is completed, click the :guilabel:`Done` button for that work order. Repeat the
same process for each work order listed on the :guilabel:`Work Orders` tab.

.. screenshot:: manufacturing-three-step-done-button
   :menu: Manufacturing ‣ Operations ‣ Manufacturing Orders ‣ (MO) ‣ Work Orders tab
   :shows: The Work Orders tab of an MO with a running work order and its "Done" button.
   :highlight: The "Done" button (red frame).
   :data: MO "WH/MO/00001" for product "Chair"; work order "Assembly" in progress.
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the work order line.

After completing all of the work orders, click :guilabel:`Produce All` at the top of the screen to
mark the |MO| as :guilabel:`Done`, and register the manufactured product(s) into inventory.

.. tip::
   For more information on processing work orders from the :guilabel:`Work Orders` list, including
   how to pause a work order, block a work center, and how time is tracked, see
   :doc:`../workflows/work_orders`.

Process finished product transfer
=================================

After completing the |MO|, return to the order's :guilabel:`Transfers` page by clicking the
:guilabel:`Transfers` button at the top of the order. This time, select :guilabel:`WH/SFP/XXXXX` to
open the store finished products transfer. This transfer is used to track the movement of finished
products from the location where they were manufactured to the location where they are stored.

After transferring the finished products to their storage location, click :guilabel:`Validate` at
the top of the transfer, followed by :guilabel:`Apply` on the :guilabel:`Immediate Transfer?` pop-up
window that appears. Doing so marks the transfer as :guilabel:`Done`, and updates inventory counts
to reflect the quantity of finished products transferred.

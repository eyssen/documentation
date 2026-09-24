=============
Batch picking
=============

.. _inventory/misc/batch_picking:

*Batch picking* enables a single picker to handle multiple orders at once, reducing the number of
times needed to navigate to a warehouse location. When picking in batches, orders are grouped and
consolidated into a picking list. After the picking, the batch is taken to an output location, where
the products are sorted into their respective delivery packages.

Since orders *must* be sorted at the output location after being picked, this picking method suits
businesses with a few products that are ordered often. Storing high-demand items in easily
accessible locations can increase the number of orders that are fulfilled efficiently.

Batch picking is ideal for industries or warehouses that handle high order volumes with a stable
demand. This method increases efficiency by allowing workers to pick items for multiple orders in
one trip through the warehouse, reducing travel time and boosting productivity.

Configuration
=============

To activate the batch picking option, begin by going to :menuselection:`Inventory app -->
Configuration --> Settings`. Under the :guilabel:`Operations` section, check the :guilabel:`Batch,
Wave & Cluster Transfers` box.

.. screenshot:: picking-methods-batch-transfer-checkbox
   :menu: Inventory ‣ Configuration ‣ Settings
   :shows: The Inventory settings page scrolled to "Operations", with the "Batch Transfers" checkbox enabled.
   :highlight: The "Batch Transfers" checkbox (red frame).
   :module: stock_picking_batch
   :notes: English UI, light theme, 1440px width.

Since batch picking is a method to optimize the *pick* operation in Odoo, the :guilabel:`Storage
Locations` and :guilabel:`Multi-Step Routes` options under the :guilabel:`Warehouse` heading must
also be checked on this settings page. When finished, click :guilabel:`Save`.

.. screenshot:: picking-methods-batch-locations-routes-checkbox
   :menu: Inventory ‣ Configuration ‣ Settings
   :shows: The Inventory settings page scrolled to "Warehouse", with the "Storage Locations" and "Multi-Step Routes" checkboxes enabled.
   :highlight: Both checkboxes (red frame).
   :module: stock_picking_batch
   :notes: English UI, light theme, 1440px width.

.. seealso::
   - :doc:`Delivery in two steps <../daily_operations/receipts_delivery_two_steps>`
   - :doc:`../daily_operations/delivery_three_steps`

Create batch transfers
======================

To manually group transfers directly from the :menuselection:`Inventory app`, hover over the
desired operation type from the :guilabel:`Inventory Overview` menu (e.g. the :guilabel:`Receipts`
Kanban card), click the :icon:`fa-ellipsis-v` :guilabel:`(vertical ellipsis)` icon, then select
:guilabel:`Prepare Batch`.

.. screenshot:: picking-methods-batch-prepare
   :menu: Inventory
   :shows: The Inventory overview with the operation-type card menu open, showing the "Prepare Batch" option.
   :highlight: The "Prepare Batch" option (red frame).
   :module: stock_picking_batch
   :notes: English UI, light theme, 1440px width.

On the batch transfer form, fill the following fields out accordingly:

- :guilabel:`Responsible`: employee assigned to the picking. Leave this field blank if *any* worker
  can fulfill this picking.
- :guilabel:`Operation Type`: from the drop-down menu, select the operation type under which the
  picking is categorized.
- :guilabel:`Scheduled Date`: specifies the date by which the :guilabel:`Responsible` person should
  complete the transfer to the output location.

.. seealso::
   To learn more about the :guilabel:`Dock Location`, :guilabel:`Vehicle`, and :guilabel:`Vehicle
   Category` fields, see :doc:`dispatch management system
   <../../shipping_receiving/setup_configuration/dispatch>`.

Next, in the :guilabel:`Transfers` list, click :guilabel:`Add a line` to open the :guilabel:`Add:
Transfers` window.

If the :guilabel:`Operation Type` field was filled, the list will filter transfer records matching
the selected :guilabel:`Operation Type`.

Click the :guilabel:`New` button to create a new transfer.

Once the transfer records are selected, click :guilabel:`Confirm` to confirm the batch picking.

.. example::
   A new batch transfer is assigned to the :guilabel:`Responsible`, `Joel Willis`, for the `Pick`
   :guilabel:`Operation Type`. The :guilabel:`Scheduled Date` is set to `August 11`.

   .. screenshot:: picking-methods-batch-transfer-form
      :menu: Inventory ‣ Operations ‣ Batch Transfers ‣ New
      :shows: An empty batch transfer form with the Responsible, Operation Type and Scheduled Date fields, and the Transfers tab below.
      :module: stock_picking_batch
      :notes: English UI, light theme, 1440px width.

   Clicking the :guilabel:`Add a line` button opens the :guilabel:`Add:Transfers` window,
   displaying only pickings. This is because the :guilabel:`Operation Type` was set to `Pick` on the
   batch transfer form.

   Click the checkbox to the left of the transfers, `WH/PICK/00001` and `WH/PICK/00002`, to include
   them in the new transfer. Then, click the :guilabel:`Select` button to close the
   :guilabel:`Add:Transfers` window.

   .. screenshot:: picking-methods-batch-add-transfers-window
      :menu: Inventory ‣ Operations ‣ Batch Transfers ‣ New
      :shows: The "Add: Transfers" pop-up window with several delivery orders selected by checkbox.
      :data: Three delivery orders of the same operation type.
      :module: stock_picking_batch
      :notes: English UI, light theme, 1440px width.

.. _inventory/warehouses_storage/add-batch-transfers:

Add batch from transfers list
-----------------------------

Another method of creating batch transfers is available using the :guilabel:`Add to batch` option in
a list. Navigate to the :menuselection:`Inventory app --> Operations` drop-down menu, and select any
of the :guilabel:`Transfers` to open a filtered list of transfers.

.. screenshot:: picking-methods-batch-transfers-drop-down
   :menu: Inventory app ‣ Operations
   :shows: The Inventory app Operations drop-down menu opened, listing Transfers, Batch Transfers, Replenishment, Procurement, Scrap and Landed Costs.
   :highlight: The "Batch Transfers" menu item (red frame).
   :module: stock_picking_batch
   :notes: English UI, light theme, 1440px width.

On the transfers list, select the checkbox to the left of the selected transfers to add in a batch.
Next, navigate to the :icon:`fa-cog` :guilabel:`Actions` button, and click :guilabel:`Add to batch`
from the resulting drop-down menu.

.. screenshot:: picking-methods-batch-add-to
   :menu: Inventory ‣ Operations ‣ Transfers
   :shows: The transfers list with several rows selected and the gear (Actions) menu open, showing "Add to batch".
   :highlight: The "Add to batch" action (red frame).
   :module: stock_picking_batch
   :notes: English UI, light theme, 1440px width.

Doing so opens an :guilabel:`Add to batch` pop-up window, wherein the employee
:guilabel:`Responsible` for the picking can be assigned.

Choose from the two radio options to add to :guilabel:`an existing batch transfer` or create
:guilabel:`a new batch transfer`.

Add a :guilabel:`Description` for this batch.

.. tip::
   The :guilabel:`Description` field can be used to add additional information to help workers
   identify the source of the batch, where to place the batch, what shipping containers to use, etc.

To create a batch to be processed at a later time, select the :guilabel:`Draft` checkbox.

Conclude the process by clicking :guilabel:`Confirm`.

.. screenshot:: picking-methods-batch-add-to-window
   :menu: Inventory ‣ Operations ‣ Transfers
   :shows: The "Add to batch" pop-up window, with the "a new batch transfer" option and the Responsible field.
   :highlight: The "a new batch transfer" option (red frame).
   :module: stock_picking_batch
   :notes: English UI, light theme, 1440px width.

Automatic batches
-----------------

Batches can be automatically created and assigned based on several criteria. The *Automatic Batches*
option is defined on the *operation type* level.

.. example::
   In a multi-steps delivery process, the picking operation can be grouped by customer, while the
   shipping operation can be organized by carrier and destination country.

To enable *Automatic Batches*, navigate to :menuselection:`Inventory app --> Configuration -->
Operation Types`, and select the desired operation type (e.g. :guilabel:`Delivery`,
:guilabel:`Pick`, etc). Then, select one or more :guilabel:`Batch Grouping` criteria by ticking the
appropriate checkbox. Even if more than one grouping option is selected, only one batch is created.

Batches can be automatically generated based on the following criteria:

- :guilabel:`Contact`
- :guilabel:`Carrier`
- :guilabel:`Destination Country`
- :guilabel:`Source Location`
- :guilabel:`Destination Location`

.. screenshot:: picking-methods-batch-auto-grouping
   :menu: Inventory ‣ Configuration ‣ Operations Types
   :shows: An operation type form with the "Automatic Batches" option enabled and the grouping criteria checkboxes (Contact, Destination Country, Carrier, Source Location, Destination Location) visible.
   :highlight: The grouping criteria block (red frame).
   :module: stock_picking_batch
   :notes: English UI, light theme, 1440px width.

Process batch transfer
======================

Handle batch transfers in the :menuselection:`Inventory app --> Operations --> Batch Transfers`
page.

From here, select the intended transfer from the list. Then, on the batch transfer form, input the
:guilabel:`Done` quantities for each product, under the :guilabel:`Detailed Operations` tab.
Finally, select :guilabel:`Validate` to complete the picking.

.. tip::
   Be certain the batch transfer is complete when the :guilabel:`Validate` button is highlighted in
   purple. If the :guilabel:`Check Availability` button is highlighted instead, that means there are
   items in the batch that are currently *not* available in-stock.

.. _inventory/management/batch-transfers-example:

.. example::
   In a batch transfer involving products from pickings, `WH/PICK/00001` and `WH/PICK/00002`, the
   :guilabel:`Detailed Operations` tab shows that the product, `Cabinet with Doors`, has been picked
   because the :guilabel:`Done` column matches the value in the :guilabel:`Reserved` column.
   However, `0.00` quantities have been picked for the other product, `Cable Management Box`.

   .. screenshot:: picking-methods-batch-process-transfer
      :menu: Inventory ‣ Operations ‣ Batch Transfers
      :shows: A batch transfer form with the Operations tab open, listing the products of two different pickings with their source locations.
      :data: Batch of two delivery orders.
      :module: stock_picking_batch
      :notes: English UI, light theme, 1440px width.

Only in-stock products are visible in the :guilabel:`Detailed Operations` tab.

To view the complete product list, switch to the :guilabel:`Operations` tab. On this list, the
:guilabel:`Demand` column indicates the required quantity for the order. The :guilabel:`Reserved`
column shows the available stock to fulfill the order. Lastly, the :guilabel:`Done` column specifies
the products that have been picked, and are ready for the next step.

.. example::
   The product, `Desk Pad`, from the same batch as the :ref:`example above
   <inventory/management/batch-transfers-example>`, is only visible in the :guilabel:`Operations`
   tab because there are no :guilabel:`Reserved` quantities in stock to fulfill the batch transfer.

   Click the :guilabel:`Check Availability` button to search the stock again for available products.

   .. screenshot:: picking-methods-batch-operations-tab
      :menu: Inventory ‣ Operations ‣ Batch Transfers
      :shows: The Operations tab of a batch transfer where the quantity of one line could not be reserved in full.
      :highlight: The line with the missing reserved quantity (red frame).
      :module: stock_picking_batch
      :notes: English UI, light theme, 1440px width.

Create backorder
----------------

On the batch transfer form, if the :guilabel:`Done` quantity of the product is *less* than the
:guilabel:`Reserved` quantity, a pop-up window appears.

This pop-up window provides the option: :guilabel:`Create Backorder?`.

Clicking the :guilabel:`Create Backorder` button automatically creates a new batch transfer.

.. note::
   When creating a new backorder, the transfers that have **not** been validated in the batch will
   be removed from it.

Click :guilabel:`No Backorder` to finish the picking *without* creating another batch picking.

Click :guilabel:`Discard` to cancel the validation, and return to the batch transfer form.

.. screenshot:: picking-methods-batch-create-backorder
   :menu: Inventory ‣ Operations ‣ Batch Transfers
   :shows: The "Create Backorder?" pop-up window shown after validating a partially picked batch transfer.
   :highlight: The "Create Backorder" button (red frame).
   :module: stock_picking_batch
   :notes: English UI, light theme, 1440px width.

====================================
Organize a cross-dock in a warehouse
====================================

Cross-docking is the process of sending products that are received directly to the customers,
without making them enter the stock. The trucks are simply unloaded in a *Cross-Dock* area in order
to reorganize products and load another truck.

.. screenshot:: daily-operations-cross-dock-cross1
   :menu: (diagram)
   :shows: A schematic drawing of a cross-dock: an inbound truck unloading into a cross-dock area where goods are re-sorted and immediately loaded onto an outbound truck, bypassing stock.
   :module: stock
   :notes: Simple schematic drawing, no Odoo UI.

Configuration
=============

In the *Inventory* app, open :menuselection:`Configuration --> Settings` and activate the
*Multi-Step Routes*.

.. screenshot:: daily-operations-cross-dock-cross2
   :menu: Inventory ‣ Configuration ‣ Settings
   :shows: The Inventory settings page scrolled to "Warehouse", with the "Multi-Step Routes" checkbox enabled (which also enables "Storage Locations").
   :highlight: The "Multi-Step Routes" checkbox (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

.. note::
   Doing so will also enable the *Storage Locations* feature.

Now, both *Incoming* and *Outgoing* shipments should be configured to work with 2 steps. To adapt
the configuration, go to :menuselection:`Inventory --> Configuration --> Warehouses` and edit your
warehouse.

.. screenshot:: daily-operations-cross-dock-cross3
   :menu: Inventory ‣ Configuration ‣ Warehouses
   :shows: A warehouse form with "Incoming Shipments" set to two steps and "Outgoing Shipments" set to two steps.
   :highlight: The "Incoming Shipments" and "Outgoing Shipments" options (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

This modification will lead to the creation of a *Cross-Docking* route that can be found in
:menuselection:`Inventory --> Configuration --> Routes`.

.. screenshot:: daily-operations-cross-dock-cross4
   :menu: Inventory ‣ Configuration ‣ Routes
   :shows: The routes list with the "Cross-Dock" route that was created automatically by the two-step configuration.
   :highlight: The "Cross-Dock" route row (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

Configure products with Cross-Dock Route
========================================

Create the product that uses the *Cross-Dock Route* and then, in the inventory tab, select the
routes *Buy* and *Cross-Dock*. Now, in the purchase tab, specify the vendor to who you buy the
product and set a price for it.

.. screenshot:: daily-operations-cross-dock-cross5
   :menu: Inventory ‣ Products ‣ Products
   :shows: A product form with the Purchase tab open, showing the vendor and the purchase price.
   :data: Product "Cross-dock item", vendor "Wood Corner".
   :module: stock
   :notes: English UI, light theme, 1440px width.

.. screenshot:: daily-operations-cross-dock-cross6
   :menu: Inventory ‣ Products ‣ Products
   :shows: The same product form with the Inventory tab open, showing the "Buy" and "Cross-Dock" routes ticked in the Operations section.
   :highlight: The "Buy" and "Cross-Dock" route checkboxes (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

Once done, create a sale order for the product and confirm it. Odoo will automatically create two
transfers which will be linked to the sale order. The first one is the transfer from the *Input
Location* to the *Output Location*, corresponding to the move of the product in the *Cross-Dock*
area. The second one is the delivery order from the *Output Location* to your *Customer Location.
Both are in state *Waiting Another Operation* because we still need to order the product to our
supplier.

.. screenshot:: daily-operations-cross-dock-cross7
   :menu: Sales ‣ Orders ‣ Orders
   :shows: A confirmed sales order for the cross-docked product, with the Delivery smart button showing two transfers.
   :highlight: The Delivery smart button (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

.. screenshot:: daily-operations-cross-dock-cross8
   :menu: Sales ‣ Orders ‣ Orders
   :shows: The two transfers linked to the sales order (Input to Output, and Output to Customers), both in "Waiting Another Operation" status.
   :highlight: The status column (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

Now, go to the *Purchase* app. There, you will find the purchase order that has been automatically
triggered by the system. Validate it and receive the products in the *Input Location*.

.. screenshot:: daily-operations-cross-dock-cross9
   :menu: Purchase ‣ Orders ‣ Requests for Quotation
   :shows: The purchase order that the cross-dock route generated automatically for the sales order.
   :module: stock
   :notes: English UI, light theme, 1440px width.

.. screenshot:: daily-operations-cross-dock-cross10
   :menu: Purchase ‣ Orders ‣ Purchase Orders
   :shows: The receipt of the purchase order being validated, with the destination set to the Input location.
   :highlight: The "Destination Location" field (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

When the products have been received from the supplier, you can go back to your initial sale order
and validate the internal transfer from *Input* to *Output*.

.. screenshot:: daily-operations-cross-dock-cross11
   :menu: Inventory ‣ Operations ‣ Transfers
   :shows: The internal transfer from Input to Output now in "Ready" status.
   :highlight: The "Ready" status (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

.. screenshot:: daily-operations-cross-dock-cross12
   :menu: Inventory ‣ Operations ‣ Transfers
   :shows: The same internal transfer after validation, in "Done" status.
   :module: stock
   :notes: English UI, light theme, 1440px width.

The delivery order is now ready to be processed and can be validated too.

.. screenshot:: daily-operations-cross-dock-cross13
   :menu: Inventory ‣ Delivery Orders
   :shows: The delivery order from Output to the customer, now in "Ready" status.
   :module: stock
   :notes: English UI, light theme, 1440px width.

.. screenshot:: daily-operations-cross-dock-cross14
   :menu: Inventory ‣ Delivery Orders
   :shows: The validated delivery order in "Done" status, completing the cross-dock flow.
   :module: stock
   :notes: English UI, light theme, 1440px width.

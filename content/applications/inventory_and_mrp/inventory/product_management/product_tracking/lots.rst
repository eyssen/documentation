===========
Lot numbers
===========

.. |PO| replace:: :abbr:`PO (Purchase Order)`
.. |SO| replace:: :abbr:`SO (Sales Order)`
.. |DO| replace:: :abbr:`DO (Delivery Order)`
.. |list| replace:: :icon:`fa-list` :guilabel:`(list)`

*Lots* are one of the two ways to identify and track products in Odoo. They typically represent a
specific batch of products that were received, stored, shipped, or manufactured in-house.

Manufacturers assign lot numbers to groups of products sharing common properties, facilitating
end-to-end traceability through their lifecycles.

Lots are useful for managing large quantities of manufactured or received products, aiding in
tracing items back to their group, particularly for product recalls or :doc:`expiration dates
<expiration_dates>`.

.. seealso::
   :doc:`serial_numbers`

Enable lots & serial numbers
============================

To track products using lots, enable the *Lots & Serial Numbers* feature. Go to the
:menuselection:`Inventory app --> Configuration --> Settings`, scroll down to the
:guilabel:`Traceability` section, and tick the checkbox next to :guilabel:`Lots & Serial Numbers`.
Then, click :guilabel:`Save`.

.. seealso::
   - :doc:`Tracking expiration dates <expiration_dates>`
   - :ref:`Print GS1 barcodes for lots and serial numbers <barcode/operations/gs1-lots>`

.. screenshot:: inventory-lots-enable-setting
   :menu: Inventory ‣ Configuration ‣ Settings
   :shows: The Inventory settings page scrolled to the "Traceability" section with the "Lots & Serial
      Numbers" checkbox enabled.
   :highlight: The "Lots & Serial Numbers" checkbox (red frame).
   :data: Demo company "YourCompany".
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the "Traceability" settings block.

.. _inventory/management/track_products_by_lots:

Track by lots
=============

Once the :guilabel:`Lots & Serial Numbers` feature is activated, configure individual products to be
tracked using lots. To do this, go to :menuselection:`Inventory app --> Products --> Products`, and
choose a product to configure.

On the product form, click into the :guilabel:`General Information` tab. In the :guilabel:`Track
Inventory` field, tick the checkbox, then select :guilabel:`By Lots` from the drop-down menu. Now,
new or existing lot numbers can be assigned to newly-received or manufactured batches of this
product.

.. seealso::
   :doc:`expiration_dates`

.. important::
   If a product has stock on-hand prior to activating tracking by lots or serial numbers, a warning
   message appears. Use an :doc:`inventory adjustment <reassign>` to assign lot numbers to existing
   products in stock.

.. screenshot:: inventory-lots-track-by-lots
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ General Information tab
   :shows: A product form with the "Track Inventory" checkbox ticked and "By Lots" selected in its
      drop-down.
   :highlight: The "Track Inventory" field set to "By Lots" (red frame).
   :data: A storable product with no stock on hand yet.
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the field.

Assign lots for shipping and receiving
======================================

Assign new lot numbers to :ref:`incoming goods <inventory/product_management/assign-lots>` on the
receipt form. When shipping :ref:`outgoing goods
<inventory/product_management/assign-lots-delivery>`, select products with specific lot numbers on
the delivery order form.

.. _inventory/product_management/assign-lots:

On receipts
-----------

Assigning new or existing lot numbers to incoming goods can be done directly on receipts.

To begin, go to the :menuselection:`Purchase` app to `create and confirm
<https://www.youtube.com/watch?v=o_uI718P1Dc>`_ a |PO| for products tracked by lot numbers. Then,
click the :guilabel:`Receipt` smart button that appears at the top of the page to navigate to the
warehouse receipt form.

.. note::
   Alternatively, navigate to an existing receipt by going to the :menuselection:`Inventory` app,
   clicking the :guilabel:`Receipts` Kanban card, and choosing the desired receipt.

.. important::
   Clicking :guilabel:`Validate` before assigning a lot number triggers an error, indicating that a
   lot number **must** be assigned before validating the receipt.

   .. screenshot:: inventory-lots-validate-error
      :menu: Inventory ‣ Receipts ‣ (a receipt) ‣ Validate
      :shows: The error pop-up shown when a receipt for a lot-tracked product is validated before any lot
         number has been assigned.
      :highlight: The error text (red frame).
      :data: Receipt WH/IN/00001 for a lot-tracked product, demand 10, no lot assigned.
      :module: stock
      :notes: English UI, light theme, 1440px width, crop to the pop-up.

On the receipt form, on the product line in the :guilabel:`Operations` tab, select the |list| icon
to the right of the product that is tracked by lot numbers.

.. screenshot:: inventory-lots-list-icon
   :menu: Inventory ‣ Receipts ‣ (a receipt) ‣ Operations tab
   :shows: The Operations tab of a receipt with the list icon at the right end of the line of a lot-tracked
      product.
   :highlight: The list icon on the product line (red frame).
   :data: Receipt WH/IN/00001 with one line for a lot-tracked product.
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the operation line.

Doing so opens the :guilabel:`Open: Stock move` pop-up window, where the :guilabel:`Lot/Serial
Number` and :guilabel:`Quantity` are assigned.

The two ways to assign lot numbers: **manually** and **importing**.

Manual assignment
~~~~~~~~~~~~~~~~~

To manually assign lot numbers, click :guilabel:`Add a line`. Input the :guilabel:`Lot/Serial
Number`, :guilabel:`Store To` location for the lot, :guilabel:`Quantity`, and :guilabel:`Destination
Package`, if any.

.. note::
   To assign multiple lot numbers, or store to multiple locations, click :guilabel:`Add a line`, and
   type a new :guilabel:`Lot/Serial Number` for additional quantities. Repeat until the total in the
   :guilabel:`Quantity` column matches the :guilabel:`Demand` at the top.

.. screenshot:: inventory-lots-assign-manually
   :menu: Inventory ‣ Receipts ‣ (a receipt) ‣ Operations tab ‣ (list icon)
   :shows: The "Open: Stock move" pop-up with two manually added lines, each with its own "Lot/Serial
      Number", "Store To" location and "Quantity", the total matching the demand.
   :highlight: The "Lot/Serial Number" column (red frame).
   :data: Lots "LOT0001" (6 units) and "LOT0002" (4 units), demand 10, location WH/Stock.
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

Import lots
~~~~~~~~~~~

In the :guilabel:`Open: Stock move` pop-up window, click :guilabel:`Import Serials/Lots`, then paste
the bulk lot numbers, in the :guilabel:`Lots/Serial numbers` field.

.. screenshot:: inventory-lots-import-lots
   :menu: Inventory ‣ Receipts ‣ (a receipt) ‣ Operations tab ‣ (list icon) ‣ Import Serials/Lots
   :shows: The "Import Lots" pop-up with several lot numbers pasted, one per line, into the "Lots/Serial
      numbers" field, and the "Keep current lines" checkbox visible.
   :highlight: The "Lots/Serial numbers" field (red frame).
   :data: Five lot numbers LOT0001 to LOT0005.
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the pop-up. Caption to convey: lot numbers pasted
      into the "Lots/Serial numbers" field of the Import Lots pop-up.

Tick the :guilabel:`Keep current lines` checkbox to generate *additional* lot numbers in the
:guilabel:`Open: Stock move` pop-up window. To replace the lot numbers in the list, leave the
:guilabel:`Keep current lines` option unticked.

Finally, click :guilabel:`Generate`.

Once all product quantities have been assigned a lot number, click :guilabel:`Save` to close the
pop-up window. Then, click :guilabel:`Validate` on the receipt form.

.. seealso::
   :ref:`Traceability report for lot numbers <inventory/product_management/lot-traceability>`

.. _inventory/product_management/assign-lots-delivery:

On delivery orders
------------------

Odoo makes it possible to specify which lot numbers for a product are chosen for outgoing shipment
on a delivery order form.

To begin, create or select an existing quotation from the :menuselection:`Sales` app. After
confirming the |SO|, the :guilabel:`Delivery` smart button becomes available. Click the
:guilabel:`Delivery` smart button to view the warehouse receipt form for that specific |SO|.

.. note::
   Alternatively, navigate to delivery orders by going to the :menuselection:`Inventory` app, and
   clicking the :guilabel:`Delivery Orders` kanban card.

Clicking the :guilabel:`Delivery` smart button opens the the delivery order form, where lot numbers
are picked for delivery. In the :guilabel:`Operations` tab, click the |list| icon to the right of
the product that is tracked by lot numbers. Clicking that icon reveals a :guilabel:`Open: Stock
move` pop-up window.

In the pop-up window, the chosen lot number and its storage location is displayed in the
:guilabel:`Pick From` column, with the with the full :guilabel:`Quantity` taken from that specific
lot (if there is enough stock in that particular lot).

If there is insufficient stock in that lot, or if partial quantities of the :guilabel:`Demand`
should be taken from multiple lots, change the :guilabel:`Quantity` directly.

.. note::
   The lot automatically chosen for delivery orders varies, depending on the selected removal
   strategy (:abbr:`FIFO (First In, First Out)`, :abbr:`LIFO (Last In, First Out)`, or :abbr:`FEFO
   (First Expiry, First Out)`). It also depends on the ordered quantity, and whether the lot's
   on-hand quantity is enough to fulfill the order.

.. seealso::
   :doc:`../../shipping_receiving/removal_strategies`

Repeat the above steps to select enough lots to fulfill the :guilabel:`Demand`, and click
:guilabel:`Save` to close the pop-up window. Lastly, click the :guilabel:`Validate` button on the
|DO| to deliver the products.

.. screenshot:: inventory-lots-pick-from
   :menu: Inventory ‣ Delivery Orders ‣ (a delivery order) ‣ Operations tab ‣ (list icon)
   :shows: The "Open: Stock move" pop-up of a delivery order, where the "Pick From" column shows the chosen
      lot number with its storage location, and the "Quantity" taken from that lot.
   :highlight: The "Pick From" column (red frame).
   :data: Two lines: LOT0001 at WH/Stock for 6 units and LOT0002 at WH/Stock for 4 units, demand 10.
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

.. seealso::
   :ref:`Traceability report for lot numbers <inventory/product_management/lot-traceability>`

Lot management
==============

Manage and view existing lot numbers for products in the :guilabel:`Lot/Serial Numbers` dashboard by
going to :menuselection:`Inventory app --> Products --> Lots/Serial Numbers`.

By default, lot numbers are grouped by product, and selecting the drop-down menu for each product
displays the existing lot numbers. Select a lot number to :ref:`modify or add details
<inventory/product_management/edit-lot>` linked to the lot. Lot numbers can also be :ref:`created
<inventory/product_management/create-new-lot>` from this page, by clicking the :guilabel:`New`
button.

.. screenshot:: inventory-lots-dashboard
   :menu: Inventory ‣ Products ‣ Lots/Serial Numbers
   :shows: The Lots/Serial Numbers list grouped by product by default, with one product group expanded to
      show its lot numbers.
   :highlight: None.
   :data: Two or three lot-tracked products with several lots each.
   :module: stock
   :notes: English UI, light theme, 1440px width, full list view. Caption to convey: lot numbers grouped by
      product on the Lot/Serial Number dashboard.

.. _inventory/product_management/edit-lot:

Modify lot
----------

Clicking a lot from the :guilabel:`Lot/Serial Number` dashboard reveals a separate page where
additional information can be provided about the lot.

.. tip::
   Odoo automatically generates a new :guilabel:`Lot/Serial Number` to follow the most recent
   number. However, it can be edited, by clicking the line under the :guilabel:`Lot/Serial Number`
   field, and changing the generated number to any desired one.

On the lot number form, the following fields can be modified:

- :guilabel:`Lot/Serial Number`: change the lot number linked to the :guilabel:`Product`
- :guilabel:`Internal Reference`: records an alternative lot/serial number used within the warehouse
  that differs from the one used by the supplier manufacturer.
- :guilabel:`Company`: specify the company where the lot number is available.
- :guilabel:`Description` tab: add extra details about the lot or serial number in this text field.

Two further fields are read-only and are only visible to users with the *Inventory / Administrator*
access right, once the lot has been moved:

- :guilabel:`Location`: the internal location where the remaining quantity of the lot is currently
  stored.
- :guilabel:`Delivered To`: the customer the lot was last delivered to, which makes a recall or a
  warranty claim easy to trace back. The same value is available as an optional
  :guilabel:`Transfer to` column on the :guilabel:`Lots/Serial Numbers` list.

Three smart buttons at the top of the form open the lot's stock information:

- :guilabel:`Transfers`: the transfers (receipts, deliveries, internal moves) in which the lot was
  used. The button is hidden while the lot has not been delivered yet.
- :guilabel:`Location`: the on-hand quantity of the lot per storage location.
- :guilabel:`Traceability`: the full :ref:`traceability report
  <inventory/product_management/lot-traceability>` of the lot.

.. important::
   On existing lots, the :guilabel:`Product` and :guilabel:`On Hand Quantity` fields **cannot** be
   modified, as the lot numbers are linked with existing stock moves.

.. screenshot:: inventory-lots-lot-form
   :menu: Inventory ‣ Products ‣ Lots/Serial Numbers ‣ (a lot)
   :shows: A lot form with the "Lot/Serial Number", "Internal Reference", "Product", "Company", "On Hand
      Quantity" and "Description" fields, and the "Location" and "Traceability" smart buttons at the top.
   :highlight: The "Internal Reference" and "Description" fields (red frames).
   :data: Lot "LOT0001" of a lot-tracked product, on-hand quantity 6.
   :module: stock
   :notes: English UI, light theme, 1440px width, full form.

.. seealso::
   :doc:`Set expiration dates for lots <expiration_dates>`

Add property
~~~~~~~~~~~~

To add custom fields to lots for enhanced traceability, there are two methods of adding properties
on a lot number form:

#. Click the :icon:`fa-cog` :guilabel:`(cog)` icon at the top-left of the page, then select
   :icon:`fa-cogs` :guilabel:`Add Properties` from the drop-down menu.
#. Click the :icon:`fa-plus` :guilabel:`Add a Property` button, located below the existing fields.

Name and :doc:`configure the new field </applications/essentials/property_fields>`. Once finished,
enter the property value in the new field.

.. example::
   The new property, `Wood type`, is added. The value is recorded as `Cherry wood`.

   .. screenshot:: inventory-lots-add-property
      :menu: Inventory ‣ Products ‣ Lots/Serial Numbers ‣ (a lot) ‣ Add a Property
      :shows: A lot form with a custom property added below the standard fields: a field named "Wood type"
         with the value "Cherry wood".
      :highlight: The new "Wood type" property field (red frame).
      :data: Lot "LOT0001"; one text property.
      :module: stock
      :notes: English UI, light theme, 1440px width, crop to the properties area.

.. seealso::
   :doc:`Configuring custom properties </applications/essentials/property_fields>`

.. _inventory/product_management/create-new-lot:

Reserve lot number for a product
--------------------------------

To create a lot number for a product, begin by going to :menuselection:`Inventory app --> Products
--> Lot/Serial Numbers`, and click :guilabel:`New`.

.. important::
   Creating a lot number reserves it for a product but **does not** assign it. To assign lot
   numbers, refer to the section on :ref:`assigning lot numbers on receipts
   <inventory/product_management/assign-lots>`.

.. tip::
   While Odoo automatically generates a new :guilabel:`Lot/Serial Number` to follow the most recent
   number, it can be edited and changed to any desired number, by clicking the line under the
   :guilabel:`Lot/Serial Number` field on the lot form, and changing the generated number.

Once the new :guilabel:`Lot/Serial Number` is generated, click the blank field next to
:guilabel:`Product` to reveal a drop-down menu. From this menu, select the product to which this new
number will be assigned.

.. example::
   The lot number, `000001`, is created for the product, `Drawer Black`.

   .. screenshot:: inventory-lots-reserve-number
      :menu: Inventory ‣ Products ‣ Lots/Serial Numbers ‣ New
      :shows: A new, unsaved lot form with the "Lot/Serial Number" set to "000001" and the "Product" field
         set to a product.
      :highlight: The "Lot/Serial Number" and "Product" fields (red frames).
      :data: Lot number "000001" for the product "Drawer Black".
      :module: stock
      :notes: English UI, light theme, 1440px width, crop to the form header.

After a new lot number has been created, saved, and assigned to the desired product, the lot number
is saved as an existing lot number linked to the product, and can be selected when :ref:`assigning
lot numbers to products on a receipt <inventory/product_management/assign-lots>`.

Manage lots for different operations types
==========================================

By default, new lots can only be created when receiving products, and existing lot numbers cannot
be used. For sales orders, only existing lot numbers can be utilized, and new ones cannot be created
on the delivery order.

To change the ability to use new (or existing) lot numbers on any operation type, go to the
:menuselection:`Inventory app --> Configuration --> Operations Types`, and select the desired
operation type.

On the operation type form, under the :guilabel:`Lots/Serial Numbers` section, tick the
:guilabel:`Create New` checkbox to enable new lot numbers to be created during this operation type.
Choose :guilabel:`Use Existing ones` if only existing lot numbers can be selected.

.. screenshot:: inventory-lots-operation-type
   :menu: Inventory ‣ Configuration ‣ Operations Types ‣ (an operation type)
   :shows: An operation type form, "Lots/Serial Numbers" section, with the "Create New" and "Use Existing
      ones" checkboxes visible.
   :highlight: The "Create New" and "Use Existing ones" checkboxes (red frame).
   :data: Operation type "YourCompany: Receipts".
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the "Lots/Serial Numbers" section.

.. tip::
   For inter-warehouse transfers involving products tracked by lots, it can be useful to enable the
   :guilabel:`Use Existing Lots/Serial Numbers` option for warehouse receipts.

.. _inventory/product_management/lot-traceability:

Display lots on delivery slips
==============================

When selling products tracked with lots, it is possible to include the lot numbers on the delivery
slips sent to customers. This can be helpful to customers in cases where lot numbers are needed,
such as filing an RMA or repair request, or registering the product.

To include lot numbers on delivery slips, open the :menuselection:`Inventory` app, and navigate to
:menuselection:`Configuration --> Settings`. Scroll down to the :guilabel:`Traceability` section,
tick the :guilabel:`Display Lots & Serial Numbers on Delivery Slips` checkbox, and click
:guilabel:`Save`.

After enabling the :guilabel:`Display Lots & Serial Numbers on Delivery Slips` setting, lot numbers
are listed on delivery slips for products tracked by lots, once the delivery order is validated.

To view lot numbers on delivery orders and delivery slips, navigate to the
:menuselection:`Inventory` app, click on :guilabel:`Delivery Orders`, and select an order containing
a product tracked using lots.

To view the lot numbers of products included in the order, make sure the :guilabel:`Operations` tab
is selected, then click the :icon:`oi-settings-adjust` :guilabel:`(adjust)` button to the right of
the tab. Ensure that the :guilabel:`Serial Numbers` checkbox is ticked, which causes a
:guilabel:`Serial Numbers` column to appear. The lot number(s) for each product included in the
order are displayed in this column.

When the order is ready to be processed, click :guilabel:`Validate` to confirm the delivery and add
product information to the delivery slip.

At the top of the order's form, click the :icon:`fa-cog` :guilabel:`(Actions)` button, and select
:guilabel:`Print --> Delivery Slip`. The delivery slip is then downloaded. Open the delivery slip
using the device's browser or file manager. Lot numbers are listed next to their respective products
in the :guilabel:`Lot/Serial Number` column.

.. screenshot:: inventory-lots-delivery-slip
   :menu: Inventory ‣ Delivery Orders ‣ (a validated delivery) ‣ Actions ‣ Print ‣ Delivery Slip
   :shows: The order-lines table of a printed delivery slip PDF, where each product line is followed by its
      lot number in the "Lot/Serial Number" column.
   :highlight: The "Lot/Serial Number" column (red frame).
   :data: One lot-tracked product with two lots on the delivery.
   :module: stock
   :notes: English UI, light theme; crop of the PDF page to the order-lines table. Requires "Display Lots &
      Serial Numbers on Delivery Slips" to be enabled.

.. _inventory/product_management/lot-labels:

Print lot labels
================

Labels carrying the lot number and its barcode can be printed straight from a transfer. On a
receipt, a delivery order or an internal transfer, click the :icon:`fa-cog` :guilabel:`(Actions)`
button and select :menuselection:`Print --> Labels`, then choose :guilabel:`Lot/SN Labels` in the
pop-up window that appears.

The label wizard then offers:

- :guilabel:`Quantity to print`: :guilabel:`One per lot/SN` prints a single label for each lot on the
  transfer, while :guilabel:`One per unit` prints one label per unit received or delivered.

  .. note::
     If the unit of measure of a lot is not in the *Units* category, the lot is treated as a single
     unit and only one label is printed for it.

- :guilabel:`Format`: :guilabel:`4 x 12` produces a PDF sheet of labels, :guilabel:`ZPL Labels`
  produces output for a Zebra label printer.

.. screenshot:: inventory-lots-print-labels
   :menu: Inventory ‣ Receipts ‣ (a validated receipt) ‣ Actions ‣ Print ‣ Labels
   :shows: The lot label wizard with "Quantity to print" set to "One per lot/SN" and the "Format" field showing
      the "4 x 12" and "ZPL Labels" choices.
   :highlight: The "Quantity to print" and "Format" fields (red frame).
   :data: A receipt with two lots of a lot-tracked product.
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

.. seealso::
   :doc:`Custom product labels <../labels>`

Traceability
============

Manufacturers and companies can refer to traceability reports to see the entire lifecycle of a
product: where it came from, when it arrived, where it was stored, who it went to (and when).

To see the full traceability of a product, or group by lots, go to the :menuselection:`Inventory app
--> Products --> Lots/Serial Numbers`. Doing so reveals the :menuselection:`Lots/Serial Numbers`
dashboard.

From here, products with lot numbers assigned to them will be listed by default, and can be expanded
to show the lot numbers those products have assigned to them.

To group by lots, begin by removing any filters in the :guilabel:`Search...` bar. Then, click the
:icon:`fa-caret-down` :guilabel:`(caret down)` icon to open a drop-down menu of :guilabel:`Filters`,
:guilabel:`Group By` options, and :guilabel:`Favorites`. Under the :guilabel:`Group By` section,
click the :guilabel:`Add Custom Group` option, and select :guilabel:`Lot/Serial Number` from the
drop-down menu.

Doing so reorganizes all the records on the page to display all existing lots and serial numbers,
and can be expanded to show all quantities of products with that assigned number.

.. screenshot:: inventory-lots-group-by-number
   :menu: Inventory ‣ Products ‣ Lots/Serial Numbers
   :shows: The Lots/Serial Numbers list with the default filters removed and a custom group by "Lot/Serial
      Number" applied, so every existing lot and serial number is listed as its own group.
   :highlight: The applied "Lot/Serial Number" group in the search bar (red frame).
   :data: Several lot- and serial-tracked products.
   :module: stock
   :notes: English UI, light theme, 1440px width, show the search bar and the grouped list.

Traceability report
-------------------

To view a full stock moves report for a lot number, select the lot number line from the
:guilabel:`Lots/Serial Number` dashboard. On the lot number form, click the :guilabel:`Traceability`
smart button.

.. screenshot:: inventory-lots-traceability-report
   :menu: Inventory ‣ Products ‣ Lots/Serial Numbers ‣ (a lot) ‣ Traceability
   :shows: The traceability report of one lot: the list of stock moves that used the lot, with date,
      reference, source and destination location and quantity.
   :highlight: None.
   :data: Lot "LOT0001" with a receipt and a delivery move.
   :module: stock
   :notes: English UI, light theme, 1440px width, full list view.

.. seealso::
   :doc:`../product_tracking`

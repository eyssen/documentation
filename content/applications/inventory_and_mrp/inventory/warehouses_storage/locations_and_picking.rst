=============================
Locations and picking helpers
=============================

Odoo's stock reservation logic treats every internal location the same way once a removal strategy
is chosen: it does not let a warehouse restrict a given transfer (or sales order) to a subset of
shelves, it has no quick hierarchical/type filter on the locations list, and its built-in removal
strategies (FIFO, LIFO, closest location, FEFO) cannot be reordered by an arbitrary, manually-ranked
priority. This page documents four small eYssen modules that close those gaps: two that let an
operation type, transfer or sales order be pinned to specific **storage categories** for picking,
one that adds a **search panel** to the locations list, and one that adds a rank-based **removal
priority** strategy and reflects it on the delivery report.

Key features
============

Restricting picking to specific storage categories
--------------------------------------------------

.. screenshot:: inventory-locations-picking-operation-type
   :menu: Inventory ‣ Configuration ‣ Operations Types ‣ (a delivery type)
   :shows: The "Locations" group of an operation type form with the "Allow Pick from Storage Categories"
      tags field holding one or two storage categories.
   :highlight: The "Allow Pick from Storage Categories" field (red frame).
   :data: Operation type "YourCompany: Delivery Orders"; categories "Forward pick" and "Shelf A".
   :module: eyssen_stock_location_pickable
   :notes: English UI, light theme, 1440px width, crop to the Locations group.

The ``eyssen_stock_location_pickable`` module adds an :guilabel:`Allow Pick from Storage
Categories` field on the operation type, and the same field on the transfer itself.

- On the :guilabel:`Operation Type` form it acts as the **default** for new transfers of that type.
  It is empty by default, which means no restriction.
- On the :guilabel:`Transfer` form the field is filled in from the operation type when the transfer
  is created, but stays editable as long as the transfer is neither :guilabel:`Done` nor
  :guilabel:`Cancelled`, so a single transfer can deviate from its operation type's default.

.. screenshot:: inventory-locations-picking-transfer-allow-categories
   :menu: Inventory ‣ Transfers ‣ (a draft delivery)
   :shows: A draft transfer form with the "Allow Pick from Storage Categories" field next to the operation
      type, holding one storage category.
   :highlight: The "Allow Pick from Storage Categories" field (red frame).
   :data: Delivery WH/OUT/00001, allowed category "Forward pick".
   :module: eyssen_stock_location_pickable
   :notes: English UI, light theme, 1440px width, crop to the header fields.

When the field holds one or more categories, reservation only considers stock sitting in a location
whose :guilabel:`Storage Category` is one of the selected categories, **or** in a location that has
no storage category set at all — locations with a *different* storage category are excluded.

.. important::
   The restriction is a pure **reservation filter** — it does not add a "pickable" flag on the
   location or on the storage category. A location is eligible simply because its storage category
   is in the allowed list, or because it has none.

The filter applies no matter what triggers the reservation: a manual :guilabel:`Check
Availability`, a chained move, or entering quantities by hand on the :guilabel:`Operations` tab.
The setting is also carried over to a backorder when one is created.

Propagating the restriction from sale orders
--------------------------------------------

.. screenshot:: inventory-locations-picking-sale-order
   :menu: Sales ‣ Orders ‣ Quotations ‣ New
   :shows: A quotation with the "Allow Pick from Storage Categories" field next to the "Warehouse" field in
      the shipping information.
   :highlight: The "Allow Pick from Storage Categories" field (red frame).
   :data: Customer "Deco Addict", warehouse "YourCompany HU", allowed category "Forward pick".
   :module: eyssen_stock_location_pickable_sale
   :notes: English UI, light theme, 1440px width, crop to the shipping fields.

The ``eyssen_stock_location_pickable_sale`` module extends the same restriction to the sales flow.
It adds the :guilabel:`Allow Pick from Storage Categories` field on the :guilabel:`Sales Order`,
next to :guilabel:`Warehouse` in the shipping information, editable while the order is a
:guilabel:`Draft`.

When the order is confirmed and the delivery is created, the categories chosen on the order are
copied onto that delivery automatically — no manual step is needed on the transfer.

.. note::
   Requires the ``eyssen_stock_location_pickable`` module.

Quick location filtering with the search panel
----------------------------------------------

.. screenshot:: inventory-locations-picking-search-panel
   :menu: Inventory ‣ Configuration ‣ Locations
   :shows: The locations list with the left search panel open, showing the hierarchical "Location" facet and
      the multi-select "Type" facet with a record count next to each option.
   :highlight: The two search-panel facets (red frame).
   :data: A warehouse with several nested internal locations plus the virtual and partner locations.
   :module: eyssen_stock_location_searchpanel
   :notes: English UI, light theme, 1440px width, full list view with the panel open.

The ``eyssen_stock_location_searchpanel`` module adds a search panel with two facets to the
locations list:

- :guilabel:`Location` — a hierarchical filter that drills down the warehouse tree and narrows the
  list to a parent location and everything below it; and
- :guilabel:`Type` — a multi-select filter on the location type (Internal, Customer, Vendor,
  Inventory Loss, Production, Transit…) with a record count next to each option.

The panel appears automatically on any list that uses the standard locations search view — no
configuration is required after installation.

Ranking locations for the removal strategy
------------------------------------------

.. screenshot:: inventory-locations-picking-removal-priority
   :menu: Inventory ‣ Configuration ‣ Locations ‣ (a location)
   :shows: A location form with the "Removal Priority" field next to "Removal Strategy" in the Logistics
      section.
   :highlight: The "Removal Priority" field (red frame).
   :data: Location "WH/Stock/Shelf 1" with removal priority 10.
   :module: eyssen_stock_removal_priority
   :notes: English UI, light theme, 1440px width, crop to the Logistics section.

The ``eyssen_stock_removal_priority`` module adds a new, custom **removal strategy** alongside
Odoo's built-in FIFO, LIFO, closest-location and FEFO strategies.

- A :guilabel:`Removal Priority` whole number (default ``1000``) is added to the location, shown on
  the location form next to :guilabel:`Removal Strategy` and as a column on the locations list.
- A new :guilabel:`Priority` removal strategy becomes selectable wherever a removal strategy is
  chosen — on a location's :guilabel:`Removal Strategy` field or on a product category's
  :guilabel:`Force Removal Strategy` field.

.. screenshot:: inventory-locations-picking-priority-strategy
   :menu: Inventory ‣ Configuration ‣ Product Categories ‣ (a category)
   :shows: A product category form with the "Force Removal Strategy" drop-down open, listing "Priority"
      among the available strategies.
   :highlight: The "Priority" entry in the drop-down (red frame).
   :data: Product category "All / Saleable".
   :module: eyssen_stock_removal_priority
   :notes: English UI, light theme, 1440px width, crop to the field and the open drop-down.

When :guilabel:`Priority` is the active removal strategy, the available stock is taken in
**ascending removal priority** order, using the location name and then the record order to break
ties — the same tie-breaking Odoo already applies for the *closest location* strategy. A **lower**
:guilabel:`Removal Priority` number is therefore picked **before** a higher one, so shelves can be
ranked explicitly (for example front-of-shelf bins at ``10`` against bulk overflow storage at
``1000``) instead of relying purely on stock age or physical distance.

.. note::
   Quants without a lot are still always sorted after quants with a lot, matching standard Odoo
   behavior for all removal strategies.

The module also adjusts the **Delivery Slip** report: the operations table, which normally lists
the move lines by source and destination location name, is re-sorted by the source location's
removal priority first, so the printed pick list follows the same shelf order the reservation used.

.. screenshot:: inventory-locations-picking-delivery-slip-order
   :menu: Inventory ‣ Delivery Orders ‣ (a validated delivery) ‣ Actions ‣ Print ‣ Delivery Slip
   :shows: The operations table of a printed delivery slip PDF, where the lines are ordered by the removal
      priority of their source location rather than by location name.
   :highlight: The source-location column showing the priority order (red frame).
   :data: Three move lines from locations with removal priorities 10, 100 and 1000.
   :module: eyssen_stock_removal_priority
   :notes: English UI, light theme; crop of the PDF page to the operations table.

Configuration
=============

Storage-category picking restriction
------------------------------------

#. Enable :doc:`Storage Locations <inventory_management/use_locations>` and
   :doc:`Storage Categories <../shipping_receiving/daily_operations/storage_category>` in
   :menuselection:`Inventory --> Configuration --> Settings`: the :guilabel:`Allow Pick from Storage
   Categories` field only has an effect once locations carry a storage category.
#. Define storage categories and assign them to locations under :menuselection:`Inventory -->
   Configuration --> Warehouse Management --> Storage Categories`, then set each location's
   :guilabel:`Storage Category` field.
#. Set a default restriction on an operation type under :menuselection:`Inventory -->
   Configuration --> Operations Types --> (open a type) --> Allow Pick from Storage Categories`.
#. Optionally override the restriction per transfer on the transfer form, or — with
   ``eyssen_stock_location_pickable_sale`` installed — per sales order in the shipping information
   before confirming the order.

Location search panel
---------------------

No configuration is required. Once ``eyssen_stock_location_searchpanel`` is installed, the
:guilabel:`Location` and :guilabel:`Type` facets appear on :menuselection:`Inventory -->
Configuration --> Locations`.

Removal priority strategy
-------------------------

#. Rank your locations under :menuselection:`Inventory --> Configuration --> Locations`: open each
   location and set its :guilabel:`Removal Priority` (lower numbers are picked first; the default
   is ``1000`` for every location).
#. Activate the strategy either on the location itself (:guilabel:`Removal Strategy` field) or, to
   enforce it for every location holding a given product family, on the product category's
   :guilabel:`Force Removal Strategy` field under :menuselection:`Inventory --> Configuration -->
   Product Categories`. In both cases select :guilabel:`Priority`.

Usage
=====

To restrict a delivery type to a picking area:

#. Go to :menuselection:`Inventory --> Configuration --> Operations Types` and open the
   :guilabel:`Delivery` type used by the relevant warehouse.
#. In the :guilabel:`Allow Pick from Storage Categories` field, add the storage categories that are
   allowed to fulfil deliveries of this type (for example, only forward-pick shelves, excluding bulk
   reserve storage).
#. Confirm a sales order for a product stocked in both an allowed and a non-allowed location, and
   check the resulting delivery: :guilabel:`Check Availability` only reserves quants from the
   allowed storage categories (or from locations with no storage category at all).
#. If needed, open the delivery and adjust :guilabel:`Allow Pick from Storage Categories` directly
   on the transfer before it is done.

To rank shelves for the priority removal strategy:

#. Set a :guilabel:`Removal Priority` on each candidate location (lower = picked first).
#. Set the product's category :guilabel:`Force Removal Strategy` to :guilabel:`Priority`.
#. Deliver the product and confirm that reservation — and the printed delivery slip — picks from
   the lowest-priority-number location first.

.. tip::
   The locations search panel makes it fast to check this setup: filter the :guilabel:`Locations`
   list to :guilabel:`Internal` locations under the relevant warehouse and compare each location's
   :guilabel:`Removal Priority` and :guilabel:`Storage Category` columns side by side.

Scope and modules
=================

- ``eyssen_stock_location_pickable`` — the :guilabel:`Allow Pick from Storage Categories` field on
  operation types and transfers, and the reservation-time storage-category filter.
- ``eyssen_stock_location_pickable_sale`` — the same field on sales orders, propagated to the
  delivery automatically on confirmation.
- ``eyssen_stock_location_searchpanel`` — the :guilabel:`Location` and :guilabel:`Type` search
  panel on the locations list view.
- ``eyssen_stock_removal_priority`` — the :guilabel:`Removal Priority` field, the :guilabel:`Priority`
  removal strategy, and the priority-ordered delivery slip report.

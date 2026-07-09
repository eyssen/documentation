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

.. Screenshot plan:
.. locations_and_picking-picking-type-allow-categories.png
..   Operation Types form, "Locations" group, showing the "Allow Pick from Storage Categories"
..   many2many tags field. Path: Inventory --> Configuration --> Operations Types --> open a
..   Delivery operation type.
.. locations_and_picking-picking-form-allow-categories.png
..   A draft/in-progress transfer form showing the "Allow Pick from Storage Categories" field next
..   to the operation type. Path: Inventory --> open a draft delivery transfer.
.. locations_and_picking-sale-order-allow-categories.png
..   A quotation form showing the "Allow Pick from Storage Categories" field next to the Warehouse
..   field in the shipping information. Path: Sales --> Orders --> New --> fill in a customer and
..   product, view the shipping fields.
.. locations_and_picking-location-search-panel.png
..   The stock.location list view with the left-hand search panel open, showing the "Location"
..   hierarchical facet and the "Type" multi-select facet with counters. Path: Inventory -->
..   Configuration --> Locations.
.. locations_and_picking-location-removal-priority-field.png
..   A location form showing the "Removal Priority" field next to "Removal Strategy". Path:
..   Inventory --> Configuration --> Locations --> open a location.
.. locations_and_picking-removal-strategy-priority-option.png
..   A product category form with the "Force Removal Strategy" dropdown open, showing "Priority" as
..   a selectable option. Path: Inventory --> Configuration --> Product Categories --> open a
..   category --> click the Force Removal Strategy field.
.. locations_and_picking-delivery-report-priority-order.png
..   The printed delivery slip PDF, with its operations table ordered by the source locations'
..   removal priority. Path: open a validated delivery --> Print --> Delivery Slip.

Key features
============

Restricting picking to specific storage categories
--------------------------------------------------

.. image:: locations_and_picking/locations_and_picking-picking-type-allow-categories.png
   :alt: Operation Types form with the Allow Pick from Storage Categories field

The ``eyssen_stock_location_pickable`` module adds an :guilabel:`Allow Pick from Storage
Categories` field (technical name ``allow_pick_categories``, a many2many to
``stock.storage.category``) on the operation type, and a matching field on the transfer itself.

- On the :guilabel:`Operation Type` form it acts as the **default**: any storage category can be
  added, and it is left empty by default (no restriction).
- On the :guilabel:`Transfer` form the field is **computed from the operation type** when the
  transfer is created, but stays editable (:guilabel:`readonly=False`) as long as the transfer is
  not :guilabel:`Done` or :guilabel:`Cancelled`, so a specific transfer can deviate from its
  operation type's default.

When the field holds one or more categories, reservation only considers quants sitting in a
location whose :guilabel:`Storage Category` is one of the selected categories, **or** in a
location that has no storage category set at all — locations with a *different* storage category
are excluded. This filter is applied by overriding ``stock.quant._get_gather_domain()`` and
``stock.quant._get_quants_by_products_locations()``, and is only active when the
``allow_pick_categories`` context key is set.

.. important::
   The restriction is a pure **reservation filter** — it does not add a "pickable" flag on the
   location or storage category themselves. A location is eligible simply because its storage
   category is in the allowed list (or it has none).

To make sure the filter applies no matter which code path triggers reservation — a manual
:guilabel:`Check Availability`, a backorder, a chained move, or manual quantity entry on the
operations tab — ``stock.move`` overrides ``_action_assign()``, ``_get_available_quantity()`` and
``_set_quantity_done_prepare_vals()`` to inject the transfer's ``allow_pick_categories`` into the
context before delegating to the standard logic. The value also survives backorder creation: the
picking's ``copy_data()`` is overridden to copy ``allow_pick_categories`` onto the backorder copy.

Propagating the restriction from sale orders
--------------------------------------------

.. image:: locations_and_picking/locations_and_picking-sale-order-allow-categories.png
   :alt: Sales order form with the Allow Pick from Storage Categories field

The ``eyssen_stock_location_pickable_sale`` module extends ``eyssen_stock_location_pickable`` to
the sales flow. It adds the same :guilabel:`Allow Pick from Storage Categories` field on the
:guilabel:`Sales Order`, placed next to :guilabel:`Warehouse` in the shipping information, editable
while the order is a :guilabel:`Draft`.

When the order is confirmed and a delivery is created, ``stock.move._get_new_picking_values()`` is
overridden to copy the sales order's ``allow_pick_categories`` onto the new delivery automatically —
no manual step is needed on the transfer.

Quick location filtering with the search panel
----------------------------------------------

.. image:: locations_and_picking/locations_and_picking-location-search-panel.png
   :alt: Locations list view with the search panel open

The ``eyssen_stock_location_searchpanel`` module inherits the standard locations search view
(``stock.view_location_search``) and adds a :guilabel:`searchpanel` with two facets:

- :guilabel:`Location` — a hierarchical filter (``location_id``) that lets you drill down the
  warehouse tree and filter the list to a parent location and its descendants; and
- :guilabel:`Type` — a multi-select filter on the location's :guilabel:`usage` (Internal, Customer,
  Vendor, Inventory Loss, Production, Transit…) with a record count shown next to each option.

The panel appears automatically on any list that uses the standard locations search view — no
configuration is required after installation.

Ranking locations for the removal strategy
------------------------------------------

.. image:: locations_and_picking/locations_and_picking-location-removal-priority-field.png
   :alt: Location form with the Removal Priority field

The ``eyssen_stock_removal_priority`` module adds a new, custom **removal strategy** alongside
Odoo's built-in FIFO, LIFO, closest-location and FEFO strategies.

- A :guilabel:`Removal Priority` integer field (technical name ``removal_priority``, default
  ``1000``) is added to :guilabel:`Location` and shown on both the location form (next to
  :guilabel:`Removal Strategy`) and the locations list view.
- A related, stored ``removal_priority`` field is added on ``stock.quant`` so each quant inherits
  its location's rank.
- A new :guilabel:`Priority` removal method (``product.removal`` record, method code ``priority``)
  is registered, making it selectable anywhere a removal strategy is chosen — on a location's
  :guilabel:`Removal Strategy` field or a product category's :guilabel:`Force Removal Strategy`
  field.

.. image:: locations_and_picking/locations_and_picking-removal-strategy-priority-option.png
   :alt: Force Removal Strategy field showing the Priority option

When :guilabel:`Priority` is the active removal strategy for a product/location, ``stock.quant``
overrides ``_gather()`` so that eligible quants are sorted by **ascending removal priority** first,
then by the location's full name, then by quant ID — the same tie-breaking pattern Odoo already
uses for the *closest location* strategy. A **lower** :guilabel:`Removal Priority` number is
therefore picked **before** a higher one, letting you rank shelves explicitly (e.g. front-of-shelf
bins at ``10`` vs. bulk overflow storage at ``1000``) instead of relying purely on stock age or
physical distance.

.. note::
   Quants without a lot are still always sorted after quants with a lot, matching standard Odoo
   behavior for all removal strategies.

The module also adjusts the **Delivery Slip** report (``stock.report_picking``): the operations
table, which normally lists move lines sorted by source and destination location name, is
re-sorted by the source location's removal priority first, so the printed pick list reflects the
same shelf order the reservation logic used.

.. image:: locations_and_picking/locations_and_picking-delivery-report-priority-order.png
   :alt: Delivery slip PDF with operations sorted by removal priority

Configuration
=============

Storage-category picking restriction
------------------------------------

#. Enable multi-location: **Storage Categories** and the :guilabel:`Allow Pick from Storage
   Categories` fields only matter once locations use a storage category, which requires the
   :guilabel:`Storage Locations` setting (group ``stock.group_stock_multi_locations``).
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

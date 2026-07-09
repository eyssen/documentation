===============================
Stock control and availability
===============================

eYssen ships a set of small, focused *Stock* modules that tighten up how on-hand quantities are
guarded and reported: a hard stop on negative stock, a per-warehouse breakdown of on-hand, free and
forecasted quantities that is precomputed for fast list, kanban and sale-order views, and a set of
physical size and load attributes on storage locations. All four are optional and are switched on
independently from the eYssen settings screen.

.. Screenshot plan:
..
.. - stock_control-negative-stock-settings.png
..   Settings app --> eYssen ERP (left menu) --> Stock section. Capture the "Disallow Negative
..   Stock" setting row with its help text.
..
.. - stock_control-negative-stock-product.png
..   Open any storable product (Inventory app --> Products --> Products --> pick one), tab
..   General Information, scroll to the Logistics/weight group. Capture the "Allow Negative Stock"
..   checkbox next to the product's other logistics fields.
..
.. - stock_control-negative-stock-error.png
..   Trigger the guard: on a product WITHOUT the override enabled, open an inventory adjustment or
..   a delivery for a location with less stock than requested and validate it. Capture the
..   resulting "You cannot validate this stock operation..." validation error dialog.
..
.. - stock_control-advanced-stock-settings.png
..   Settings app --> eYssen ERP --> Stock section. Capture the "Advanced Stock" setting row plus,
..   once enabled, the "Use Background Jobs (queue_job)" checkbox and the "Recompute All" button
..   underneath it.
..
.. - stock_control-warehouse-config.png
..   Inventory app --> Configuration --> Warehouses --> open a warehouse --> Warehouse
..   Configuration tab. Capture the "Stock" group: "Calculate WH Stock on Product" and "Visible WH
..   Stock on Product" checkboxes, and — after toggling one — the red "settings have changed"
..   banner with the "Update All" button.
..
.. - stock_control-product-stock-widget.png
..   Open a storable product form (General Information tab). Capture the read-only "Stock Data"
..   widget showing one line per enabled warehouse (On Hand / Free / Forecasted) and the small
..   refresh icon button next to it.
..
.. - stock_control-product-list-columns.png
..   Inventory app --> Products --> Products, switch to list view, open the optional-columns
..   (sliders) dropdown on the top-right of the list header. Capture the list with a couple of
..   "<Warehouse> On Hand / Free / Forecasted" columns enabled, and the dropdown itself showing the
..   available per-warehouse columns.
..
.. - stock_control-sale-order-line-popover.png
..   Open a sale order with at least one confirmed line, click the delivery/availability icon
..   next to a line's quantity to open the "Qty at Date" popover. Capture the popover with the
..   added "All Warehouses" table at the bottom, listing on hand/free/forecasted per warehouse.
..
.. - stock_control-location-load.png
..   Inventory app --> Configuration --> Locations --> open an internal location. Capture the
..   "Size & Load" group with the length/width/height, dimension UoM, volume, volume UoM, weight
..   and weight UoM fields.

Preventing negative stock
==========================

By default Odoo allows a stock quant to go negative — useful for some workflows, but often a sign
of a data-entry mistake or a missed reservation. The ``eyssen_stock_disallow_negative_stock``
module adds a hard validation guard: any stock move or adjustment that would leave a quant with a
negative quantity in an **internal** or **transit** location is rejected outright, unless an
explicit override has been switched on for that product, its product category, or the location
itself.

The guard only applies to **storable** products of type :guilabel:`Goods` (``type = 'consu'`` with
``is_storable`` set) — services and consumable-but-non-storable products are never checked.

Overrides
---------

An :guilabel:`Allow Negative Stock` checkbox is added in three places, and **any one of them**
being enabled is enough to allow negative stock for that combination:

- the product's :guilabel:`Inventory` tab (visible only for storable goods);
- the product category's :guilabel:`Logistics` group; and
- the stock location's form.

.. image:: stock_control/stock_control-negative-stock-product.png
   :alt: Allow Negative Stock checkbox on a storable product

If none of the three overrides is enabled and an operation would push the quantity below zero, Odoo
blocks the operation with a validation error naming the product, its internal reference and the
location.

.. image:: stock_control/stock_control-negative-stock-error.png
   :alt: Validation error raised when an operation would create negative stock

.. note::
   The check only looks at ``internal`` and ``transit`` location usages. Customer, vendor,
   inventory-loss and production locations are not covered by this guard.

Per-warehouse stock data (Advanced Stock)
==========================================

The ``eyssen_stock_advanced_stock`` module precomputes, per product variant, the **on-hand**,
**free** and **forecasted** quantity in every warehouse that has been opted in, and stores the
result in a dedicated ``product.stock.data`` model (one row per product/warehouse/quantity kind)
instead of recalculating it on every page load. This keeps product list, kanban and sale-order
views fast even on large catalogs, while still reflecting stock changes automatically.

.. image:: stock_control/stock_control-advanced-stock-settings.png
   :alt: Advanced Stock setting and Recompute All button

Per-warehouse opt-in
---------------------

Stock data is only computed for warehouses that are explicitly enabled. On each warehouse's
:guilabel:`Warehouse Configuration` tab, a :guilabel:`Stock` group exposes two switches:

- :guilabel:`Calculate WH Stock on Product` — turns on the per-warehouse computation for that
  warehouse; and
- :guilabel:`Visible WH Stock on Product` — additionally exposes that warehouse's figures as
  dynamic optional columns and search filters on the product list and search views (only available
  once calculation is enabled).

.. image:: stock_control/stock_control-warehouse-config.png
   :alt: Warehouse Configuration tab with the Stock group and Update All button

Toggling either switch creates or removes, per warehouse, three read-only technical fields on both
``product.template`` and ``product.product`` — ``x_eyssen_wh_pt_<warehouse_id>_onhand`` /
``_free`` / ``_forecasted`` (and the ``_pp_`` equivalents on the variant) — and regenerates the
supporting list/search view extensions that expose them as optional columns and as
:guilabel:`<quantity kind> in <Warehouse>` search filters. Because changing the configuration does
not retroactively fill these fields, a red warning banner appears on the warehouse form until the
:guilabel:`Update All` button is used to recompute everything.

Viewing the data
-----------------

On the product form, a read-only :guilabel:`Stock Data` widget on the :guilabel:`General
Information` tab lists on-hand, free and forecasted quantities for every enabled warehouse, with a
small refresh button next to it to force an immediate recompute for that product. The same widget
is shown in the product kanban and list views (as an optional column).

.. image:: stock_control/stock_control-product-stock-widget.png
   :alt: Stock Data widget on the product form

.. image:: stock_control/stock_control-product-list-columns.png
   :alt: Product list with per-warehouse optional columns enabled

On a sale order, opening a confirmed line's :guilabel:`Qty at Date` popover shows an extra
:guilabel:`All Warehouses` table with the same on-hand/free/forecasted breakdown, in addition to
the line-level stock widget.

.. image:: stock_control/stock_control-sale-order-line-popover.png
   :alt: Qty at Date popover extended with the All Warehouses breakdown

Automatic recomputation
-------------------------

The precomputed figures are kept in sync automatically whenever stock changes:

- a stock quant is created, or its quantity or reserved quantity changes;
- a stock move is confirmed, cancelled, or has its demand quantity or source/destination location
  edited (this also catches quantity shifts that move no quant, such as a reservation at a
  zero-stock warehouse); and
- a purchase order is confirmed or cancelled.

All of these funnel into a single per-transaction "dirty set" of affected product templates, so
several triggers on the same product within one transaction collapse into one recompute. By
default the recompute runs right after the transaction commits, in its own database cursor, so a
recompute failure never turns an otherwise successful operation into an error — it is logged and
self-heals on the next stock change.

.. tip::
   Enabling :guilabel:`Use Background Jobs (queue_job)` in the settings moves that same
   per-template recompute into asynchronous ``queue_job`` jobs instead, which helps avoid UI
   timeouts on large stock pickings. It requires the ``queue_job`` module to be installed first —
   the setting refuses to save otherwise.

Full recompute
----------------

Besides the automatic incremental updates, the data can be rebuilt for every storable product at
once with the :guilabel:`Recompute All` button in the settings, or with a warehouse's own
:guilabel:`Update All` button (which delegates to the same full recompute). Use this after bulk
data changes, or whenever the warning banner asks for it.

Legacy warehouse stock calculation
=====================================

``eyssen_stock_calculate_wh_stock`` is the earlier implementation of the same idea: the same
:guilabel:`Calculate WH Stock on Product` / :guilabel:`Visible WH Stock on Product` switches on the
warehouse form, the same dynamic per-warehouse ``x_eyssen_wh_pt_*`` / ``x_eyssen_wh_pp_*`` fields
and optional list columns, and the same :guilabel:`Update All` / :guilabel:`Recompute All` actions
— but it stores the computed figures directly on the product as a stored JSON field
(``product_wh_stocks``) plus a stored HTML summary (``product_wh_stocks_html``) shown with a plain
HTML widget, rather than in the searchable ``product.stock.data`` model. Recomputation on stock
quant changes and purchase order confirm/cancel is per-product and runs in a fresh cursor after
each transaction, without the shared dirty-set batching or the background-job option that
``eyssen_stock_advanced_stock`` offers.

.. important::
   ``eyssen_stock_calculate_wh_stock`` and ``eyssen_stock_advanced_stock`` manage the same
   dynamically generated per-warehouse field names and the same named list/search view extensions.
   Only one of the two should be installed on a given database — installing both leads to the two
   modules overwriting each other's generated fields and views.

Storage location size and load
=================================

``eyssen_stock_load`` adds physical size and load attributes to stock locations, for tracking the
usable dimensions and load capacity of a shelf, bin, or storage location. A :guilabel:`Size & Load`
group is added to the stock location form (and the corresponding columns to the locations list
view) with:

- length, width and height/thickness fields, each expressed in a configurable length unit of
  measure (defaulting to the system's reference length unit);
- a :guilabel:`Volume` field with its own volume unit of measure; and
- a :guilabel:`Weight` field with its own weight unit of measure.

.. image:: stock_control/stock_control-location-load.png
   :alt: Size and Load group on the stock location form

.. note::
   The length/width/height fields ship with hard-coded Hungarian labels in the source code
   (*Hosszúság (x)*, *Szélesség (y)*, *Magasság / Vastagság (z)* — Length, Width, and
   Height/Thickness respectively) rather than translatable strings, so they display in Hungarian
   regardless of the interface language until a translation is added.

.. important::
   The :guilabel:`Volume` field is not yet computed from the length/width/height dimensions — the
   underlying compute method is a stub that always stores ``0``. Treat it as a placeholder until
   this is implemented.

Configuration
===============

Each module is switched on independently under :menuselection:`Settings app --> eYssen ERP -->
Stock`:

- :guilabel:`Disallow Negative Stock` — installs ``eyssen_stock_disallow_negative_stock``;
- :guilabel:`Calculate Warehouse Stock` — installs the legacy ``eyssen_stock_calculate_wh_stock``;
- :guilabel:`Advanced Stock` — installs ``eyssen_stock_advanced_stock``; and
- :guilabel:`Size & Load Management` — installs ``eyssen_stock_load``.

.. important::
   Only enable one of :guilabel:`Calculate Warehouse Stock` and :guilabel:`Advanced Stock` — see
   the warning above.

Once :guilabel:`Advanced Stock` is enabled, also enable :guilabel:`Use Background Jobs
(queue_job)` (immediately below it in the settings) if the ``queue_job`` module is available and
stock recomputation should not run inline with stock operations.

Usage
=======

#. **Allow negative stock where it is legitimate.** Before relying on the guard, review products,
   categories and locations that need an exception (for example a location used purely for
   corrective adjustments) and tick :guilabel:`Allow Negative Stock` on the appropriate record.
#. **Opt warehouses into per-warehouse stock data.** On each warehouse that should report separate
   figures, tick :guilabel:`Calculate WH Stock on Product`, and additionally
   :guilabel:`Visible WH Stock on Product` if the per-warehouse breakdown should appear as optional
   list columns and search filters.
#. **Run a full recompute after opting in.** Use the warehouse's :guilabel:`Update All` button (or
   :guilabel:`Recompute All` in the settings) so the new warehouse's figures are filled in
   immediately instead of waiting for the next stock movement.
#. **Check stock from the product or the sale order.** Use the :guilabel:`Stock Data` widget on
   the product form, the optional per-warehouse list columns, or the extended :guilabel:`Qty at
   Date` popover on a sale order line to see on-hand, free and forecasted quantities per warehouse
   without leaving the record.
#. **Record location size and load** on the locations that need it, so downstream reporting or
   putaway logic has length, width, height, and weight data to work with.

Scope and modules
====================

- ``eyssen_stock_disallow_negative_stock`` — blocks stock operations that would push a quant
  negative in internal/transit locations, with per-product, per-category and per-location
  overrides.
- ``eyssen_stock_advanced_stock`` — current per-warehouse on-hand/free/forecasted computation,
  stored in the searchable ``product.stock.data`` model, with dynamic per-warehouse fields, product
  and sale-order-line widgets, and automatic/background recomputation.
- ``eyssen_stock_calculate_wh_stock`` — earlier per-warehouse stock computation with the same
  warehouse-level switches, stored as JSON/HTML fields directly on the product; superseded by
  ``eyssen_stock_advanced_stock``.
- ``eyssen_stock_load`` — adds length/width/height, volume and weight attributes to stock
  locations.

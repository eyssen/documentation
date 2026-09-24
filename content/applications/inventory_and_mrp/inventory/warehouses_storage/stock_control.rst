===============================
Stock control and availability
===============================

eYssen ships a set of small, focused *Stock* modules that tighten up how transfers and on-hand
quantities are guarded and reported: a hold flag and a reservation reset on the transfer itself, a
hard stop on negative stock, a per-warehouse breakdown of on-hand, free and forecasted quantities
that is precomputed for fast list, kanban and sale-order views, and a set of physical size and load
attributes on storage locations. Each one is optional and is switched on independently from the
eYssen settings screen.

.. _inventory/warehouses_storage/eyssen-stock:

Holding a transfer and clearing quantities
==========================================

``eyssen_stock`` is the shared eYssen :guilabel:`Inventory` layer the other modules on this page
build on. On its own it adds three controls that change how a transfer behaves.

Hold
----

A :guilabel:`Hold` toggle on the transfer form marks a transfer as *not to be processed*. Holding a
transfer **releases its reservation**, so the stock becomes available for other orders again;
releasing the hold reserves it back. A red :guilabel:`On Hold` ribbon marks a held transfer, and a
read-only :guilabel:`Hold Reason` explains why — filled in automatically by whatever put the
transfer on hold. Both fields are tracked in the chatter.

The toggle is also available as a column on the :guilabel:`Transfers` list, and the search bar
gains :guilabel:`On Hold` and :guilabel:`Off Hold` filters. A transfer that is
:guilabel:`Done` or :guilabel:`Cancelled` can no longer be held.

.. screenshot:: inventory-stock-control-hold
   :menu: Inventory ‣ Transfers ‣ (a ready transfer)
   :shows: A transfer form with the "Hold" toggle enabled, the read-only "Hold Reason" next to it and the red
      "On Hold" ribbon in the top-right corner.
   :highlight: The "Hold" toggle and the "On Hold" ribbon (red frames).
   :data: Delivery WH/OUT/00003 held with the reason "Waiting for payment".
   :module: eyssen_stock
   :notes: English UI, light theme, 1440px width, crop to the header and the ribbon.

Set quantities to zero
----------------------

A :guilabel:`Set Quantities to Zero` button above the operation lines clears the reserved
quantities of a :guilabel:`Ready` transfer in one click, which is the quickest way to start a pick
over. The :guilabel:`Demand` is kept, so the transfer can simply be reserved again; lines that are
already in a package are left untouched. The button is only available while the transfer is
:guilabel:`Ready` — on any other state it reports that quantities can only be cleared when the
transfer is ready.

.. screenshot:: inventory-stock-control-set-quantities-to-zero
   :menu: Inventory ‣ Transfers ‣ (a ready transfer) ‣ Operations tab
   :shows: A ready transfer with the "Set Quantities to Zero" button above the operation lines, whose
      quantities are still filled in.
   :highlight: The "Set Quantities to Zero" button (red frame).
   :data: Delivery WH/OUT/00004 with three reserved lines.
   :module: eyssen_stock
   :notes: English UI, light theme, 1440px width, crop to the button and the lines.

Reserving from packages
-----------------------

A :guilabel:`Prevent Reservation from Packages` option on the operation type
(:menuselection:`Inventory app --> Configuration --> Operations Types`), **enabled by default**,
keeps automatic reservation away from stock that is already inside a package: only unpackaged stock
is reserved. Moves for which a package was chosen explicitly are unaffected. Turn the option off on
operation types that are expected to break open packages.

.. screenshot:: inventory-stock-control-prevent-package-reservation
   :menu: Inventory ‣ Configuration ‣ Operations Types ‣ (an operation type)
   :shows: An operation type form showing the "Prevent Reservation from Packages" checkbox next to "Show
      Entire Packs".
   :highlight: The "Prevent Reservation from Packages" checkbox (red frame).
   :data: Operation type "YourCompany: Delivery Orders", option enabled.
   :module: eyssen_stock
   :notes: English UI, light theme, 1440px width, crop to the packages options.

.. note::
   The module also raises the length limit of a warehouse's :guilabel:`Short Name` to 32
   characters, and shows the forecasted quantity together with the unit of measure on the on-hand
   badge of the product kanban and list views.

Preventing negative stock
==========================

By default Odoo allows a stock quant to go negative — useful for some workflows, but often a sign
of a data-entry mistake or a missed reservation. The ``eyssen_stock_disallow_negative_stock``
module adds a hard validation guard: any stock move or adjustment that would leave a quant with a
negative quantity in an **internal** or **transit** location is rejected outright, unless an
explicit override has been switched on for that product, its product category, or the location
itself.

.. screenshot:: inventory-stock-control-negative-stock-setting
   :menu: Settings ‣ eYssen ERP ‣ Stock
   :shows: The "Stock" block of the eYssen ERP settings page, with the "Disallow Negative Stock" setting row
      and its help text ("If you turn it on, the system will not allow the stock to go negative by default.
      Negative stock can be allowed on by stock location or by product.").
   :highlight: The "Disallow Negative Stock" setting row (red frame).
   :data: Demo company "YourCompany HU"; the setting enabled.
   :module: eyssen_base, eyssen_stock_disallow_negative_stock
   :notes: English UI, light theme, 1440px width, crop to the setting row.

The guard only applies to **storable** products of type :guilabel:`Goods` (``type = 'consu'`` with
``is_storable`` set) — services and consumable-but-non-storable products are never checked.

Overrides
---------

An :guilabel:`Allow Negative Stock` checkbox is added in three places, and **any one of them**
being enabled is enough to allow negative stock for that combination:

- the product's :guilabel:`Inventory` tab (visible only for storable goods);
- the product category's :guilabel:`Logistics` group; and
- the stock location's form.

.. screenshot:: inventory-stock-control-allow-negative-product
   :menu: Inventory ‣ Products ‣ Products ‣ (a storable product) ‣ Inventory tab
   :shows: The "Allow Negative Stock" checkbox on a storable product's Inventory tab, next to the other
      logistics fields.
   :highlight: The "Allow Negative Stock" checkbox (red frame).
   :data: A storable product of type Goods; the checkbox left unticked.
   :module: eyssen_stock_disallow_negative_stock
   :notes: English UI, light theme, 1440px width, crop to the field group. The checkbox is only shown for
      storable goods.

If none of the three overrides is enabled and an operation would push the quantity below zero, Odoo
blocks the operation with a validation error naming the product, its internal reference and the
location.

.. screenshot:: inventory-stock-control-negative-stock-error
   :menu: Inventory ‣ Delivery Orders ‣ (a delivery) ‣ Validate
   :shows: The validation error raised when an operation would push a quant negative: "You cannot validate
      this stock operation because the stock of the <product> (<reference>) at <location> would go
      negative!"
   :highlight: The error text (red frame).
   :data: A product with no override enabled, delivering more than the quantity on hand at WH/Stock.
   :module: eyssen_stock_disallow_negative_stock
   :notes: English UI, light theme, 1440px width, crop to the error dialog.

.. note::
   The check only looks at ``internal`` and ``transit`` location usages. Customer, vendor,
   inventory-loss and production locations are not covered by this guard.

.. _inventory/warehouses_storage/advanced-stock:

Per-warehouse stock data (Advanced Stock)
==========================================

The ``eyssen_stock_advanced_stock`` module precomputes, per product variant, the **on-hand**,
**free** and **forecasted** quantity in every warehouse that has been opted in, and stores the
result in a dedicated ``product.stock.data`` model (one row per product/warehouse/quantity kind)
instead of recalculating it on every page load. This keeps product list, kanban and sale-order
views fast even on large catalogs, while still reflecting stock changes automatically.

.. screenshot:: inventory-stock-control-advanced-stock-settings
   :menu: Settings ‣ eYssen ERP ‣ Stock
   :shows: The "Advanced Stock" setting row, with the "Use Background Jobs (queue_job)" checkbox and the
      "Recompute All" button that appear underneath it once it is enabled.
   :highlight: The "Use Background Jobs (queue_job)" checkbox and the "Recompute All" button (red frames).
   :data: Advanced Stock enabled; queue_job installed.
   :module: eyssen_stock_advanced_stock
   :notes: English UI, light theme, 1440px width, crop to the setting rows.

Per-warehouse opt-in
---------------------

Stock data is only computed for warehouses that are explicitly enabled. On each warehouse's
:guilabel:`Warehouse Configuration` tab, a :guilabel:`Stock` group exposes two switches:

- :guilabel:`Calculate WH Stock on Product` — turns on the per-warehouse computation for that
  warehouse; and
- :guilabel:`Visible WH Stock on Product` — additionally exposes that warehouse's figures as
  dynamic optional columns and search filters on the product list and search views (only available
  once calculation is enabled).

.. screenshot:: inventory-stock-control-warehouse-config
   :menu: Inventory ‣ Configuration ‣ Warehouses ‣ (a warehouse) ‣ Warehouse Configuration tab
   :shows: The "Stock" group of the Warehouse Configuration tab with the "Calculate WH Stock on Product" and
      "Visible WH Stock on Product" checkboxes, and the red banner with the "Update All" button shown after
      a switch was toggled.
   :highlight: The two checkboxes and the "Update All" button (red frames).
   :data: Warehouse "YourCompany HU" with calculation just enabled, so the banner is visible.
   :module: eyssen_stock_advanced_stock
   :notes: English UI, light theme, 1440px width, crop to the Stock group and the banner.

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

.. screenshot:: inventory-stock-control-stock-data-widget
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ General Information tab
   :shows: The read-only "Stock Data" widget on a product form, with one line per enabled warehouse showing
      the On Hand, Free and Forecasted quantity, and the small refresh icon next to it.
   :highlight: The "Stock Data" widget and its refresh icon (red frames).
   :data: Two warehouses opted in, both holding stock of the product.
   :module: eyssen_stock_advanced_stock
   :notes: English UI, light theme, 1440px width, crop to the widget.

.. screenshot:: inventory-stock-control-product-list-columns
   :menu: Inventory ‣ Products ‣ Products
   :shows: The products list with two per-warehouse columns enabled (e.g. "<Warehouse> On Hand" and
      "<Warehouse> Free"), and the optional-column drop-down open showing the available per-warehouse
      columns.
   :highlight: The open optional-column drop-down (red frame).
   :data: Two warehouses with "Visible WH Stock on Product" enabled; five or six products.
   :module: eyssen_stock_advanced_stock
   :notes: English UI, light theme, 1440px width, full list view with the drop-down open.

On a sale order, opening a confirmed line's :guilabel:`Qty at Date` popover shows an extra
:guilabel:`All Warehouses` table with the same on-hand/free/forecasted breakdown, in addition to
the line-level stock widget.

.. screenshot:: inventory-stock-control-qty-at-date-popover
   :menu: Sales ‣ Orders ‣ Orders ‣ (a confirmed order)
   :shows: The "Qty at Date" popover of a confirmed sales order line, extended at the bottom with the "All
      Warehouses" table listing the on-hand, free and forecasted quantity per warehouse.
   :highlight: The "All Warehouses" table (red frame).
   :data: A confirmed sales order line for a product stocked in two warehouses.
   :module: eyssen_stock_advanced_stock
   :notes: English UI, light theme, 1440px width, crop to the popover.

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

.. screenshot:: inventory-stock-control-location-size-load
   :menu: Inventory ‣ Configuration ‣ Locations ‣ (an internal location)
   :shows: The "Size & Load" group of a stock location form with the length, width, height/thickness fields
      and their dimensional unit of measure, the Volume field with its volume unit, and the Weight field
      with its weight unit.
   :highlight: The "Size & Load" group (red frame).
   :data: Location "WH/Stock/Shelf 1" with dimensions filled in and a weight capacity set.
   :module: eyssen_stock_load
   :notes: English UI, light theme, 1440px width, crop to the group. The length/width/height labels are
      currently Hungarian in the source code.

.. note::
   The unit-of-measure fields of this group filter on the unit-of-measure :guilabel:`Type`
   introduced by the :doc:`Advanced UoM module
   <../product_management/configure/uom>` (``eyssen_uom``), so that module must be installed as
   well for the default units to be found.

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
- :guilabel:`Advanced Stock` — installs ``eyssen_stock_advanced_stock``; and
- :guilabel:`Size & Load Management` — installs ``eyssen_stock_load``.

.. important::
   The same settings page still shows a :guilabel:`Calculate Warehouse Stock` switch. It belongs to
   an earlier implementation of per-warehouse stock data that has been superseded by
   :guilabel:`Advanced Stock` and is no longer shipped, so **do not enable it**.

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
- ``eyssen_stock_load`` — adds length/width/height, volume and weight attributes to stock
  locations.

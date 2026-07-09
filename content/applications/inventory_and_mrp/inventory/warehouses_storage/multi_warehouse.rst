==========================
Multi-warehouse operations
==========================

Companies that stock the same products in more than one warehouse need three things standard Odoo
does not fully provide out of the box: a controlled way to move goods *between* warehouses through
an arbitrary number of pick/pack/ship steps, the ability to source individual sales order lines from
different warehouses instead of one warehouse per order, and a webshop that pools availability across
several warehouses instead of a single one. The eYssen multi-warehouse modules add all three, plus
carrier-specific pickup/delivery address logic for internal transfers shipped through the eYssen
**Custom** and **GLS** delivery integrations.

.. Screenshot plan:
.. - multi_warehouse-warehouse-config.png: Warehouse form, "Inter Warehouse Transfer" notebook page,
..   with "Can be used for internal transit" checked and both an Out Steps and an In Steps list
..   populated, plus the green/orange validity banner. Path: Inventory --> Configuration -->
..   Warehouses --> open a warehouse --> Inter Warehouse Transfer tab.
.. - multi_warehouse-warehouse-steps-list.png: The standalone "Warehouse Steps" list showing rows for
..   several warehouses with their Direction (In/Out), Operation Type, Source and Destination Location
..   columns. Path: Inventory --> Configuration --> Warehouse Steps.
.. - multi_warehouse-picking-type-config.png: An Operation Type form scrolled to the "Package In" /
..   "Package Out" / "All In Packing" / "Allow Reverse Picking" checkboxes (with Reverse Picking Type
..   visible once Allow Reverse Picking is checked). Path: Inventory --> Configuration --> Operation
..   Types --> open one --> scroll near "Show Entire Packs".
.. - multi_warehouse-transfer-list.png: The Internal Transfers list with a few records in different
..   states (Draft, Waiting for Source Warehouse, In Transit, Done) so the colored state badges are
..   visible. Path: Inventory --> Transfers --> Internal Transfers.
.. - multi_warehouse-transfer-form-draft.png: A draft Internal Transfer form with Source Warehouse,
..   Destination Warehouse and Carrier filled in, and the "Create Picking" / "Create Orders" / "Start
..   Transfer" header buttons visible. Path: Internal Transfers --> New.
.. - multi_warehouse-transfer-pickings-chain.png: A confirmed Internal Transfer form, Pickings tab,
..   showing several chained pickings (one per step) with different states, ending in a Done picking
..   at the destination warehouse. Path: open an in-progress Internal Transfer --> Pickings tab.
.. - multi_warehouse-picking-internal-header.png: A stock.picking form that belongs to an internal
..   transfer, showing the transfer-specific header (Mark as Todo / Check Availability / Validate /
..   Print) and the "View Int.Transfer" smart button in the button box. Path: open one of the pickings
..   from the Pickings tab above.
.. - multi_warehouse-sale-order-line-warehouse.png: A sales order form (multi-warehouse group enabled)
..   with the order line list showing the per-line "Warehouse" column, two lines set to two different
..   warehouses. Path: Sales --> Orders --> New --> add two order lines --> show the Warehouse column.
.. - multi_warehouse-gls-tracking-package.png: An outgoing picking that belongs to an internal transfer
..   and is configured for GLS ("Package In" operation type), showing a stock.quant.package with its
..   GLS tracking status/parcel number. Path: open an internal-transfer outgoing picking with GLS
..   packaging --> Detailed Operations / package.
.. - multi_warehouse-website-settings.png: Website --> Configuration --> Settings, scrolled to the
..   Shop - Products section, showing the "Warehouse" field (core) and the eYssen "More Warehouses"
..   many2many-tags field underneath it, populated with two or more warehouses.

Key features
============

Inter-warehouse transfers
--------------------------

.. image:: multi_warehouse/multi_warehouse-transfer-form-draft.png
   :alt: Draft Internal Transfer form with source/destination warehouse and carrier

A new ``stock.internal.transfer`` record represents one shipment of goods from a **Source
Warehouse** to a **Destination Warehouse**, both of which must be flagged as usable for internal
transit (see :ref:`multi_warehouse/configuration`). The record is automatically classified as an
:guilabel:`Intracompany transfer` or an :guilabel:`Intercompany transfer` depending on whether the
two warehouses belong to the same company, and it tracks a **Carrier**, a sequence-based
**Transfer Reference** (``IT000001``, ...) and a rollup of the transferred quantities.

An internal transfer moves through the following states: :guilabel:`Draft` →
:guilabel:`Waiting for Source Warehouse` → :guilabel:`Source Processing` → :guilabel:`In Transit`
→ :guilabel:`Destination Processing` → :guilabel:`Done` (with a :guilabel:`Reconciliation
Required` side state and a :guilabel:`Cancelled` state). Draft transfers cannot be deleted once
they leave the draft state.

- For an **intracompany** transfer, :guilabel:`Create Picking` generates the first stock picking
  directly, using the first configured out-step of the source warehouse.
- For an **intercompany** transfer, :guilabel:`Create Orders` instead creates a linked
  :guilabel:`Source Order` (a sales order on the source company) and a :guilabel:`Destination
  Order` (a purchase order on the destination company), and finding the right cross-company
  partner records automatically where possible.
- :guilabel:`Start Transfer` confirms the first picking and moves the transfer to
  :guilabel:`Waiting for Source Warehouse`.

Multi-step routing between warehouses
--------------------------------------

.. image:: multi_warehouse/multi_warehouse-warehouse-config.png
   :alt: Warehouse form, Inter Warehouse Transfer tab with In/Out steps and validity banner

Each warehouse that can act as a source or destination of an internal transfer defines its own
chain of **Out Steps** (how goods leave the warehouse toward the transit location) and **In
Steps** (how goods arrive from the transit location into the warehouse). Every step is a
``stock.warehouse.step`` record pointing to an :guilabel:`Operation Type`; source and destination
locations are read from that operation type.

The system automatically renumbers and validates the chain whenever steps are added, edited or
removed:

- the **first** out step must start at the warehouse's stock location, and the **last** out step
  must end at a *transit* location;
- the **first** in step must start at a *transit* location, and the **last** in step must end at
  the warehouse's stock location;
- consecutive steps must connect (each step's destination must equal the next step's source), and
  the chain may not contain loops.

The warehouse form shows a live validity banner (:guilabel:`it_settings_valid_msg`) summarizing
any problem found; :guilabel:`Inter Warehouse Transfer` fields other than the toggle are hidden
until :guilabel:`Can be used for internal transit` is checked. As an internal transfer's pickings
are validated one by one, :guilabel:`action_next_step` automatically creates the next picking in
the chain — carrying over open moves, package levels and move-to-move links — until the goods
reach the destination warehouse's stock location, at which point the transfer is marked
:guilabel:`Done` (or :guilabel:`Reconciliation Required` if any quantity was under-delivered along
the way).

.. image:: multi_warehouse/multi_warehouse-transfer-pickings-chain.png
   :alt: Internal Transfer form, Pickings tab with a chain of pickings across steps

.. note::
   A ``stock.internal.transfer.template`` model exists to pre-fill a warehouse's step chain from a
   reusable template, but only the template's :guilabel:`Name` is currently implemented — the
   template selector on the warehouse form (:guilabel:`Create Steps from Template`) does not yet
   populate the steps.

Packaging, unpacking and reverse pickings
-------------------------------------------

.. image:: multi_warehouse/multi_warehouse-picking-type-config.png
   :alt: Operation Type form with Package In / Package Out / Allow Reverse Picking options

Each :guilabel:`Operation Type` gains four extra options used by the transfer chain:

- :guilabel:`Package In` — the picking must have every move covered by a package before it can be
  validated (:guilabel:`button_validate` raises an error otherwise); when this is set on the step
  the transfer's carrier is copied onto the picking automatically.
- :guilabel:`Package Out` — the picking must be fully unpacked (no remaining package levels)
  before it can be validated.
- :guilabel:`All In Packing` — reserved flag for packaging rules (no validation logic yet).
- :guilabel:`Allow Reverse Picking` and :guilabel:`Reverse Picking Type` — when a picking is
  validated with a shortfall (delivered quantity lower than demanded), the shortfall is
  automatically split into a **reverse picking** on the chosen operation type (or the same one if
  none is set), returning the missing quantity to the original source location(s). If the missing
  quantity had come from more than one source location in the original picking, an activity is
  scheduled on the reverse picking asking a warehouse user to double-check the split.

Custom and GLS delivery for internal transfers
-------------------------------------------------

.. image:: multi_warehouse/multi_warehouse-picking-internal-header.png
   :alt: Picking form for an internal-transfer leg with the internal-transfer header and smart button

Pickings that belong to an internal transfer use a dedicated header (:guilabel:`Mark as Todo`,
:guilabel:`Check Availability`, :guilabel:`Validate`, :guilabel:`Print`) instead of the standard
one, and expose a :guilabel:`View Int.Transfer` smart button; the same button is added to sales
order and purchase order forms whenever they are linked to a transfer.

When the **Custom** or **GLS** delivery modules build the shipping label for a picking that
belongs to an internal transfer, the pickup and delivery addresses are taken from the *transfer's*
source and destination warehouse partners instead of the sale order's customer:

- ``eyssen_stock_multi_warehouse_delivery_custom`` overrides ``custom_pickupaddress`` /
  ``custom_deliveryaddress`` on ``stock.picking`` to resolve the source/destination warehouse
  partner.
- ``eyssen_stock_multi_warehouse_delivery_gls`` overrides ``gls_pickupaddress`` /
  ``gls_deliveryaddress`` the same way, additionally prefixing the resulting name with the
  warehouse's company name (``<Company> - <Partner>``) so the GLS label clearly shows which
  company location is shipping or receiving.

.. image:: multi_warehouse/multi_warehouse-gls-tracking-package.png
   :alt: Internal-transfer picking with a GLS-tracked package

For GLS, once every package on a picking reaches GLS tracking status ``05`` (handed over), the
picking is validated automatically — this lets a multi-step transfer leg complete itself as soon
as GLS confirms all parcels have moved, without a warehouse user manually clicking
:guilabel:`Validate`. GLS parcel identifiers (:guilabel:`gls_parcel_id`,
:guilabel:`gls_parcel_number`) are also carried over onto the repackaged package created for each
next step, and the transfer list/search can look transfers up by GLS tracking number.

Splitting sales orders across warehouses
------------------------------------------

.. image:: multi_warehouse/multi_warehouse-sale-order-line-warehouse.png
   :alt: Sales order lines with a per-line Warehouse column

``eyssen_sale_multiple_warehouse`` adds a required :guilabel:`Warehouse` field directly on
**sales order lines**, defaulting to the salesperson's default warehouse. This lets a single
order be delivered from several warehouses at once — for example, one order line shipped from the
main warehouse and another from a regional one — instead of forcing the whole order onto a single
:guilabel:`Warehouse` at header level:

- changing the order-level :guilabel:`Warehouse` field propagates that warehouse to every existing
  order line;
- the line-level warehouse is passed into procurement (:guilabel:`_prepare_procurement_values`),
  so each line generates its delivery from its own warehouse; and
- the :guilabel:`Make to Order` indicator on a line is computed from that line's own warehouse
  route, not the order's.

The :guilabel:`Warehouse` column is only shown to users in the **Multiple Warehouses** group
(``stock.group_stock_multi_warehouses``, enabled automatically by Odoo once a company has more
than one warehouse) and becomes read-only once the order leaves the :guilabel:`Quotation` /
:guilabel:`Quotation Sent` stage.

Webshop stock pooling across warehouses
-------------------------------------------

.. image:: multi_warehouse/multi_warehouse-website-settings.png
   :alt: Website settings with the More Warehouses field under Shop - Products

``eyssen_website_sale_multiple_warehouse`` lets a website draw stock availability from **several**
warehouses instead of the single core :guilabel:`Warehouse` field. A website with one or more
:guilabel:`More Warehouses` selected pools its availability across all of them:

- on a product page, the displayed :guilabel:`free_qty` (used for the "in stock" / quantity
  widgets) is the sum of the *forecasted* quantity of the product across every warehouse in
  :guilabel:`More Warehouses`, read from the pre-aggregated stock figures maintained by
  ``eyssen_stock_advanced_stock``;
- in the cart, the same pooled quantity is used to validate that a requested cart quantity does
  not exceed what is available across those warehouses, instead of only the single website
  warehouse.

If a website has no :guilabel:`More Warehouses` configured, availability falls back to the order's
own :guilabel:`Warehouse`, matching the standard single-warehouse ``website_sale_stock`` behavior.

.. _multi_warehouse/configuration:

Configuration
=============

#. **Enable multi-warehouse mode.** This is a standard Odoo mechanism, not an eYssen setting:
   creating a second warehouse for a company (:menuselection:`Inventory --> Configuration -->
   Warehouses --> New`) automatically activates the :guilabel:`Storage Locations` setting and
   grants the **Multiple Warehouses** access group to internal users. The per-line
   :guilabel:`Warehouse` column on sales orders and the website's :guilabel:`More Warehouses`
   field are only visible to users in this group.
#. **Flag the warehouses used for internal transfers.** On each source and destination warehouse
   (:menuselection:`Inventory --> Configuration --> Warehouses`), open the
   :guilabel:`Inter Warehouse Transfer` tab and check :guilabel:`Can be used for internal
   transit`.
#. **Configure the Out/In step chain** for each of those warehouses in the same tab (or globally
   under :menuselection:`Inventory --> Configuration --> Warehouse Steps`), picking an
   :guilabel:`Operation Type` per step. The banner on the warehouse form must turn green
   (:guilabel:`Step settings are valid.`) before the warehouse can be used as a transfer source or
   destination — ``stock.internal.transfer`` restricts its :guilabel:`Source Warehouse` /
   :guilabel:`Destination Warehouse` fields to warehouses with a valid, transit-enabled step chain.
#. **Set packaging behavior on the relevant operation types**
   (:menuselection:`Inventory --> Configuration --> Operation Types`): enable :guilabel:`Package
   In` on outgoing steps that must be packed before shipping (e.g. before handing off to GLS),
   :guilabel:`Package Out` on incoming steps that must be fully unpacked, and
   :guilabel:`Allow Reverse Picking` (with an optional dedicated :guilabel:`Reverse Picking Type`)
   wherever short deliveries should generate a reverse picking automatically.
#. **Install the matching delivery module** if internal-transfer pickings should carry
   carrier-specific pickup/delivery addresses: ``eyssen_stock_multi_warehouse_delivery_custom`` for
   the eYssen Custom carrier, ``eyssen_stock_multi_warehouse_delivery_gls`` for GLS. Both simply
   extend ``eyssen_stock_multi_warehouse`` and require the corresponding base delivery module
   (``eyssen_delivery_custom`` / ``eyssen_delivery_gls``) to already be installed.
#. **Enable per-line warehouses on quotations** by installing ``eyssen_sale_multiple_warehouse`` —
   no extra settings screen is involved; the :guilabel:`Warehouse` order-line column appears as
   soon as the Multiple Warehouses group (step 1) is active.
#. **Enable webshop stock pooling** by installing ``eyssen_website_sale_multiple_warehouse`` (which
   requires ``eyssen_stock_advanced_stock``), then go to :menuselection:`Website --> Configuration
   --> Settings`, scroll to the :guilabel:`Shop - Products` section, and fill in
   :guilabel:`More Warehouses` next to the standard :guilabel:`Warehouse` field.

Usage
=====

Running an internal transfer
------------------------------

#. Go to :menuselection:`Inventory --> Transfers --> Internal Transfers` and create a new record.
#. Set the :guilabel:`Source Warehouse`, :guilabel:`Destination Warehouse` and :guilabel:`Carrier`.
   The :guilabel:`Type` (:guilabel:`Intracompany transfer` / :guilabel:`Intercompany transfer`) is
   computed automatically from the two warehouses' companies.
#. For an intracompany transfer, click :guilabel:`Create Picking`, then open the picking and add
   the products and quantities to move; for an intercompany transfer, click :guilabel:`Create
   Orders` to generate the linked sales/purchase orders instead.
#. Click :guilabel:`Start Transfer` to confirm the first picking. The transfer moves to
   :guilabel:`Waiting for Source Warehouse`.
#. Process and validate each picking in turn from the :guilabel:`Pickings` tab (or from the
   picking's own :guilabel:`View Int.Transfer` smart button). Each validated picking automatically
   spawns the next step's picking until the goods reach the destination warehouse, at which point
   the transfer reaches :guilabel:`Done`.
#. If a picking is under-delivered on an operation type with :guilabel:`Allow Reverse Picking`
   enabled, a reverse picking is created for the shortfall automatically; if it needs manual
   attention (multiple source locations), a to-do activity is scheduled on that reverse picking.

Selling from multiple warehouses on one order
-------------------------------------------------

#. On a sales order, add order lines as usual. Each line defaults to the salesperson's default
   warehouse.
#. Show or edit the :guilabel:`Warehouse` column on the order line list (or set it on each line's
   form) to route individual lines to a different warehouse, as long as the order is still a
   quotation.
#. Confirm the order — each line generates its delivery from its own warehouse.

Selling across pooled warehouses on the webshop
----------------------------------------------------

#. Configure :guilabel:`More Warehouses` on the website as described in
   :ref:`multi_warehouse/configuration`.
#. On the shop, the quantity/availability shown for a storable product reflects the sum of
   forecasted stock across all of those warehouses, not just one.
#. When a customer adds a quantity to the cart, availability is validated against the same pooled
   total.

Scope and modules
==================

- ``eyssen_stock_multi_warehouse`` — the ``stock.internal.transfer`` model, warehouse step
  configuration, the :guilabel:`Internal Transfers` and :guilabel:`Warehouse Steps` menus, and the
  packaging/reverse-picking operation-type options.
- ``eyssen_stock_multi_warehouse_delivery_custom`` — routes internal-transfer pickup/delivery
  addresses through the transfer's warehouses for the eYssen Custom carrier.
- ``eyssen_stock_multi_warehouse_delivery_gls`` — the same address routing for GLS, plus
  GLS-parcel-aware auto-validation and package re-creation along the transfer chain.
- ``eyssen_sale_multiple_warehouse`` — adds the per-order-line :guilabel:`Warehouse` field on sales
  orders.
- ``eyssen_website_sale_multiple_warehouse`` — pools webshop stock availability and cart validation
  across a website's configured :guilabel:`More Warehouses`.

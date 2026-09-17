==========================
Multi-warehouse operations
==========================

Companies that stock the same products in more than one warehouse need three things standard Odoo
does not fully provide out of the box: a controlled way to move goods *between* warehouses through
an arbitrary number of pick/pack/ship steps, the ability to source individual sales order lines from
different warehouses instead of one warehouse per order, and a webshop whose availability is
computed from several warehouses (or from explicit stock rules) instead of a single warehouse. The
eYssen multi-warehouse modules add all three, plus carrier-specific pickup/delivery address logic
for internal transfers shipped through the eYssen **Custom** and **GLS** delivery integrations.

Key features
============

Inter-warehouse transfers
--------------------------

.. screenshot:: inventory-multi-warehouse-transfer-draft
   :menu: Inventory ‣ Transfers ‣ Internal Transfers ‣ New
   :shows: A draft internal transfer form with the Source Warehouse, Destination Warehouse and Carrier
      filled in, and the "Create Picking", "Create Orders" and "Start Transfer" buttons in the header.
   :highlight: The header buttons (red frame).
   :data: Source "YourCompany HU", destination "Store", carrier "GLS"; transfer reference IT000001.
   :module: eyssen_stock_multi_warehouse
   :notes: English UI, light theme, 1440px width, crop to the header and the main fields.

An :guilabel:`Internal Transfer` record represents one shipment of goods from a **Source
Warehouse** to a **Destination Warehouse**, both of which must be flagged as usable for internal
transit (see :ref:`multi_warehouse/configuration`). The record is automatically classified as an
:guilabel:`Intracompany transfer` or an :guilabel:`Intercompany transfer` depending on whether the
two warehouses belong to the same company, and it carries a required :guilabel:`Carrier`, a
sequence-based transfer reference (``IT000001``, …), an optional :guilabel:`Description` and a
rollup of the transferred quantities (:guilabel:`Sum Qty`).

An internal transfer moves through the following states: :guilabel:`Draft` →
:guilabel:`Waiting for Source Warehouse` → :guilabel:`Source Processing` → :guilabel:`In Transit`
→ :guilabel:`Destination Processing` → :guilabel:`Done` (with a :guilabel:`Reconciliation
Required` side state and a :guilabel:`Cancelled` state). Draft transfers cannot be deleted once
they leave the draft state.

- For an **intracompany** transfer, :guilabel:`Create Picking` generates the first stock picking
  directly, using the first configured out-step of the source warehouse.
- For an **intercompany** transfer, :guilabel:`Create Orders` instead creates a linked
  :guilabel:`Source Order` (a sales order on the source company) and a :guilabel:`Destination
  Order` (a purchase order on the destination company), resolving the cross-company partner
  records automatically where possible.
- :guilabel:`Start Transfer` confirms the first picking and moves the transfer to
  :guilabel:`Waiting for Source Warehouse`.

.. screenshot:: inventory-multi-warehouse-transfer-list
   :menu: Inventory ‣ Transfers ‣ Internal Transfers
   :shows: The Internal Transfers list with records in different states (Draft, Waiting for Source Warehouse,
      In Transit, Done), so the coloured state badges are visible, next to the transfer reference, the source
      and destination warehouse and the carrier.
   :highlight: The "State" column (red frame).
   :data: Four internal transfers, one per state.
   :module: eyssen_stock_multi_warehouse
   :notes: English UI, light theme, 1440px width, full list view.

Multi-step routing between warehouses
--------------------------------------

.. screenshot:: inventory-multi-warehouse-warehouse-steps
   :menu: Inventory ‣ Configuration ‣ Warehouses ‣ (a warehouse) ‣ Inter Warehouse Transfer tab
   :shows: The "Inter Warehouse Transfer" tab with "Can be used for internal transit" ticked, a populated
      Out Steps list and In Steps list, and the validity banner below them.
   :highlight: The two step lists and the validity banner (red frames).
   :data: Two out steps (Pick, Ship) and two in steps (Receive, Store) on the warehouse "YourCompany HU";
      the banner reads "Step settings are valid."
   :module: eyssen_stock_multi_warehouse
   :notes: English UI, light theme, 1440px width, crop to the tab.

Each warehouse that can act as a source or destination of an internal transfer defines its own
chain of :guilabel:`Out Steps` (how goods leave the warehouse toward the transit location) and
:guilabel:`In Steps` (how goods arrive from the transit location into the warehouse). Every step
points to an :guilabel:`Operation Type`, and the step's source and destination location are read
from that operation type.

The system automatically renumbers and validates the chain whenever steps are added, edited or
removed:

- the **first** out step must start at the warehouse's stock location, and the **last** out step
  must end at a *transit* location;
- the **first** in step must start at a *transit* location, and the **last** in step must end at
  the warehouse's stock location;
- consecutive steps must connect (each step's destination must equal the next step's source), and
  the chain may not contain loops.

The warehouse form shows a live validity banner summarizing any problem found; the
:guilabel:`Inter Warehouse Transfer` fields other than the toggle stay hidden until
:guilabel:`Can be used for internal transit` is ticked. As the transfer's pickings are validated
one by one, the next picking in the chain is created automatically — carrying over the open moves
and the packages — until the goods reach the destination warehouse's stock location, at which point
the transfer is marked :guilabel:`Done`, or :guilabel:`Reconciliation Required` if any quantity was
under-delivered along the way.

.. screenshot:: inventory-multi-warehouse-pickings-chain
   :menu: Inventory ‣ Transfers ‣ Internal Transfers ‣ (an in-progress transfer) ‣ Pickings tab
   :shows: The Pickings tab of a confirmed internal transfer, listing one picking per step with different
      statuses, ending with a Done picking at the destination warehouse.
   :highlight: The chain of pickings and their statuses (red frame).
   :data: Four pickings: two Done at the source, one In Transit, one Ready at the destination.
   :module: eyssen_stock_multi_warehouse
   :notes: English UI, light theme, 1440px width, crop to the tab.

.. screenshot:: inventory-multi-warehouse-warehouse-steps-list
   :menu: Inventory ‣ Configuration ‣ Warehouse Steps
   :shows: The standalone "Warehouse Steps" list with rows for several warehouses, showing the Warehouse,
      Direction (In/Out), Operation Type, Source Location and Destination Location columns.
   :highlight: None.
   :data: Two warehouses, each with two out steps and two in steps.
   :module: eyssen_stock_multi_warehouse
   :notes: English UI, light theme, 1440px width, full list view.

.. note::
   A step **template** is foreseen for pre-filling a warehouse's step chain from a reusable
   definition, but only the template's :guilabel:`Name` is implemented so far — the
   :guilabel:`Create Steps from Template` selector on the warehouse form does not yet populate the
   steps.

Packaging, unpacking and reverse pickings
-------------------------------------------

.. screenshot:: inventory-multi-warehouse-operation-type-options
   :menu: Inventory ‣ Configuration ‣ Operations Types ‣ (an operation type)
   :shows: The operation type form scrolled to the "Package In", "Package Out", "All In Packing" and "Allow
      Reverse Picking" checkboxes, with the "Reverse Picking Type" field visible because "Allow Reverse
      Picking" is ticked.
   :highlight: The four checkboxes and the "Reverse Picking Type" field (red frame).
   :data: Operation type used as an out step; Package In and Allow Reverse Picking ticked.
   :module: eyssen_stock_multi_warehouse
   :notes: English UI, light theme, 1440px width, crop to the option block near "Show Entire Packs".

Each :guilabel:`Operation Type` gains four extra options used by the transfer chain:

- :guilabel:`Package In` — the picking can only be validated once every move is covered by a
  package; when this option is set on the step, the transfer's carrier is copied onto the picking
  automatically.
- :guilabel:`Package Out` — the picking must be fully unpacked (no remaining package levels)
  before it can be validated.
- :guilabel:`All In Packing` — reserved for future packaging rules; it has no effect yet.
- :guilabel:`Allow Reverse Picking` and :guilabel:`Reverse Picking Type` — when a picking is
  validated with a shortfall (delivered quantity lower than demanded), the shortfall is
  automatically split into a **reverse picking** on the chosen operation type (or the same one if
  none is set), returning the missing quantity to the original source location(s). If the missing
  quantity had come from more than one source location in the original picking, an activity is
  scheduled on the reverse picking asking a warehouse user to double-check the split.

Custom and GLS delivery for internal transfers
-------------------------------------------------

.. screenshot:: inventory-multi-warehouse-picking-header
   :menu: Inventory ‣ Transfers ‣ Internal Transfers ‣ (a transfer) ‣ Pickings tab ‣ (a picking)
   :shows: A picking that belongs to an internal transfer, with the transfer-specific header buttons ("Mark
      as Todo", "Check Availability", "Validate", "Print") and the "View Int.Transfer" smart button in the
      button box.
   :highlight: The header buttons and the "View Int.Transfer" smart button (red frames).
   :data: One leg of the transfer IT000001.
   :module: eyssen_stock_multi_warehouse
   :notes: English UI, light theme, 1440px width, crop to the header and button box.

Pickings that belong to an internal transfer use a dedicated header (:guilabel:`Mark as Todo`,
:guilabel:`Check Availability`, :guilabel:`Validate`, :guilabel:`Print`) instead of the standard
one, and expose a :guilabel:`View Int.Transfer` smart button; the same button is added to sales
order and purchase order forms whenever they are linked to a transfer.

When the **Custom** or **GLS** delivery modules build the shipping label for a picking that
belongs to an internal transfer, the pickup and delivery addresses are taken from the *transfer's*
source and destination warehouse partners instead of the sale order's customer:

- ``eyssen_stock_multi_warehouse_delivery_custom`` resolves the pickup and delivery address from
  the source and destination warehouse's contact for the eYssen *Custom* carrier.
- ``eyssen_stock_multi_warehouse_delivery_gls`` does the same for GLS, and additionally prefixes
  the name with the warehouse's company (``<Company> - <Contact>``) so the GLS label clearly shows
  which company location is shipping or receiving.

.. screenshot:: inventory-multi-warehouse-gls-package
   :menu: Inventory ‣ Transfers ‣ Internal Transfers ‣ (a transfer) ‣ Pickings tab ‣ (a GLS leg) ‣ (package)
   :shows: A package of an internal-transfer outgoing picking shipped through GLS, showing its GLS parcel
      number and tracking status.
   :highlight: The GLS parcel number and tracking status (red frame).
   :data: One package with a GLS parcel number; use a throw-away parcel number, not a real one.
   :module: eyssen_stock_multi_warehouse_delivery_gls
   :notes: English UI, light theme, 1440px width, crop to the package fields.

For GLS, once every package on a picking reaches the *handed over* GLS tracking status, the picking
is validated automatically — so a multi-step transfer leg completes itself as soon as GLS confirms
all parcels have moved, without a warehouse user clicking :guilabel:`Validate`. The GLS parcel
identifiers are carried over onto the repackaged package created for the next step, and an internal
transfer can be looked up by its :guilabel:`Package Number` or :guilabel:`Tracking Number` in the
transfer list.

Splitting sales orders across warehouses
------------------------------------------

.. screenshot:: inventory-multi-warehouse-so-line-warehouse
   :menu: Sales ‣ Orders ‣ Quotations ‣ New
   :shows: A quotation whose order-line list shows the per-line "Warehouse" column, with two lines set to
      two different warehouses.
   :highlight: The "Warehouse" column (red frame).
   :data: Line 1 from "YourCompany HU", line 2 from "Store".
   :module: eyssen_sale_multiple_warehouse
   :notes: English UI, light theme, 1440px width, crop to the order lines. The column requires the Multiple
      Warehouses group.

``eyssen_sale_multiple_warehouse`` adds a required :guilabel:`Warehouse` field directly on
**sales order lines**, defaulting to the salesperson's default warehouse. This lets a single
order be delivered from several warehouses at once — for example, one order line shipped from the
main warehouse and another from a regional one — instead of forcing the whole order onto a single
:guilabel:`Warehouse` at header level:

- changing the order-level :guilabel:`Warehouse` field propagates that warehouse to every existing
  order line;
- each line generates its delivery from its own warehouse; and
- the :guilabel:`Make to Order` indicator on a line follows that line's own warehouse route, not
  the order's.

The :guilabel:`Warehouse` column is only shown to users in the **Multiple Warehouses** group, which
Odoo enables automatically once a company has more than one warehouse, and becomes read-only once
the order leaves the :guilabel:`Quotation` / :guilabel:`Quotation Sent` stage.

Webshop stock availability
--------------------------

``eyssen_website_sale_advanced_stock`` decides what availability the webshop shows, based on the
pre-aggregated per-warehouse figures of :ref:`Advanced Stock
<inventory/warehouses_storage/advanced-stock>` (see :doc:`stock_control`). A :guilabel:`Stock Mode` field on the website
selects between two modes:

- :guilabel:`Per Warehouse` — availability is the total across the warehouses listed in the
  website's :guilabel:`Warehouses` field. This replaces the standard single
  :guilabel:`Warehouse` of the webshop, and falls back to it when the list is empty.
- :guilabel:`Rule-based` — availability is computed from explicit stock filters, which makes it
  possible to distinguish *what can be shipped now* from *what is on its way*.

.. screenshot:: inventory-multi-warehouse-website-stock-mode
   :menu: Website ‣ Configuration ‣ Settings
   :shows: The "Shop - Products" section of the website settings with the standard "Warehouse" field, the
      eYssen "Stock Mode" selector set to "Per Warehouse", and the "Warehouses" tags field below it holding
      two warehouses.
   :highlight: The "Stock Mode" selector and the "Warehouses" field (red frames).
   :data: Website "eYssen Shop"; warehouses "YourCompany HU" and "Store".
   :module: eyssen_website_sale_advanced_stock
   :notes: English UI, light theme, 1440px width, crop to the Shop - Products section. The Stock Mode
      selector is only visible to users in the Multiple Warehouses group.

Rule-based mode
~~~~~~~~~~~~~~~

In :guilabel:`Rule-based` mode the website defines up to four availability levels. Each level has
its own stock filter and its own :guilabel:`Quantity Type` — :guilabel:`Free to Use (On Hand -
Reserved)`, :guilabel:`On Hand` or :guilabel:`Forecasted`:

- :guilabel:`Available` — always active; this is the quantity the webshop treats as sellable.
- :guilabel:`Immediate`, :guilabel:`Short Term` and :guilabel:`Long Term` — each switched on
  separately, for showing longer delivery promises next to the immediately sellable quantity.

A fifth, independent rule covers business customers:

- :guilabel:`B2B Stock` — when enabled, a separate availability is computed from the selected
  :guilabel:`Storage Categories`, optionally narrowed further by a :guilabel:`Domain Override`.

.. screenshot:: inventory-multi-warehouse-website-stock-rules
   :menu: Website ‣ Configuration ‣ Settings
   :shows: The website settings with "Stock Mode" set to "Rule-based", showing the "Available" block with its
      Quantity Type and filter, the "Immediate", "Short Term" and "Long Term" toggles, the "B2B Stock"
      toggle with its Storage Categories field, and the "Recompute Stock" button at the bottom.
   :highlight: The "Available" block and the "Recompute Stock" button (red frames).
   :data: Available = Free to Use with no extra filter; Immediate enabled with Forecasted; B2B Stock enabled
      with the storage category "Wholesale".
   :module: eyssen_website_sale_advanced_stock
   :notes: English UI, light theme, 1440px width, crop to the rule blocks.

.. important::
   Changing any of these settings does not recompute the stored figures. A warning banner appears
   in the settings until the :guilabel:`Recompute Stock` button is used.

.. note::
   The availability shown on a product page and the check performed when a quantity is added to the
   cart are both read live from stock, so a reservation made by a confirmed sales order is
   reflected immediately even between two recomputations.

.. note::
   Requires ``eyssen_stock_advanced_stock``. The earlier
   ``eyssen_website_sale_multiple_warehouse`` module, which only pooled forecasted stock across a
   website's warehouses, is superseded by this one and is no longer shipped.

.. _multi_warehouse/configuration:

Configuration
=============

#. **Enable multi-warehouse mode.** This is a standard Odoo mechanism, not an eYssen setting:
   creating a second warehouse for a company (:menuselection:`Inventory --> Configuration -->
   Warehouses --> New`) automatically activates the :guilabel:`Storage Locations` setting and
   grants the **Multiple Warehouses** access group to internal users. The per-line
   :guilabel:`Warehouse` column on sales orders and the website's :guilabel:`Stock Mode` field are
   only visible to users in this group.
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
#. **Configure webshop availability** by installing ``eyssen_website_sale_advanced_stock`` (which
   requires ``eyssen_stock_advanced_stock``), then go to :menuselection:`Website --> Configuration
   --> Settings`, scroll to the :guilabel:`Shop - Products` section, set :guilabel:`Stock Mode` and
   either list the website's :guilabel:`Warehouses` or define the availability rules. Finish with
   :guilabel:`Recompute Stock`.

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

Selling across several warehouses on the webshop
----------------------------------------------------

#. Set the website's :guilabel:`Stock Mode` and its :guilabel:`Warehouses` (or availability rules)
   as described in :ref:`multi_warehouse/configuration`, then click :guilabel:`Recompute Stock`.
#. On the shop, the availability shown for a storable product reflects the configured warehouses or
   rules instead of a single warehouse.
#. When a customer adds a quantity to the cart, it is validated against the same figure.

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
- ``eyssen_website_sale_advanced_stock`` — webshop availability per warehouse or from explicit
  stock rules, with four availability levels and a separate B2B rule.

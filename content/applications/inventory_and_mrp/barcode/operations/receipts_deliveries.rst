=====================================================
Scan receipts, deliveries, and internal transfers
=====================================================

The ``eyssen_barcode_app`` module's :guilabel:`Warehouse Operations` flow replaces Odoo's official
*Barcode* application (module ``stock_barcode``, not installed in this database): it lets a
warehouse user browse transfers by operation type and process them (receipts, delivery orders,
internal transfers, and any other configured operation type) by scanning products and packages.

Browse operation types
========================

Go to the main apps menu and open the :menuselection:`Barcode` app, then click the
:guilabel:`Warehouse Operations` tile.

.. screenshot:: barcode-warehouse-operations-home
   :menu: Barcode ‣ Warehouse Operations
   :shows: The Warehouse Operations screen, listing operation types as cards with their
      ready-to-process picking count.
   :highlight: One operation-type card and its count badge (red frame).
   :data: Operation types Receipts, Delivery Orders, and Internal Transfers, each with a few ready
      pickings.
   :module: eyssen_barcode_app
   :notes: English UI, light theme, 1440px width.

Optionally filter the list by typing part of a :guilabel:`Warehouse` name, and choose whether the
cards are sorted by :guilabel:`Picking Count Order` (most pickings ready first, the default) or
:guilabel:`Name Order` using the two buttons above the list. Tap an operation type card to open its
pickings.

List and filter pickings
==========================

The :guilabel:`Picking Operations` screen lists the transfers of the selected operation type that
are not yet done (or cancelled), each shown as a card with its priority star, reference, status,
source document, and any scheduling information.

.. screenshot:: barcode-warehouse-operations-picking-list
   :menu: Barcode ‣ Warehouse Operations ‣ (an operation type)
   :shows: The Picking Operations screen for one operation type, with the scan field, the "Show
      done" toggle, and a list of pickings below it.
   :highlight: The scan field and the picking list (red frame).
   :data: Operation type "Receipts" with three open transfers.
   :module: eyssen_barcode_app
   :notes: English UI, light theme, 1440px width.

Scan or type into the field to narrow the list down to the picking that matches:

- a **product's barcode** — only pickings with a not-yet-fully-scanned line for that product remain;
- a **picking's own reference** (e.g. `WH/IN/00023`) — jumps straight to that picking;
- a **package's barcode**, including a GLS parcel number — only pickings whose destination packages
  include that package remain.

Toggle :guilabel:`Show done` to also include already-validated and cancelled transfers in the list.
Tap a picking card to open it for scanning.

Scan a transfer
================

The scanning screen shows the transfer's reference and state, a scan field, the product lines on
the left, and any packages on the right.

.. screenshot:: barcode-warehouse-operations-scan-screen
   :menu: Barcode ‣ Warehouse Operations ‣ (an operation type) ‣ (a picking)
   :shows: The scanning screen for one transfer, with the scan field, the product-lines column on
      the left (color-coded by scanned quantity), and the packages column on the right.
   :highlight: The scan field and the product-lines column (red frame).
   :data: A receipt with three product lines, one fully scanned (green), one partially scanned
      (yellow), and one not started (red).
   :module: eyssen_barcode_app
   :notes: English UI, light theme, 1440px width.

Scanning a product's barcode increases its scanned quantity by one; each line can also be adjusted
with its :guilabel:`+`/:guilabel:`-` buttons, or filled to the full expected quantity in one click
with its :guilabel:`Set` button. Lines are colored red (nothing scanned yet), yellow (partially
scanned), or green (fully scanned), and not-yet-started lines are kept in the middle of the list
while completed ones sink to the bottom.

.. note::
   Whether the scan field looks for a product or for a package barcode depends on the transfer: it
   scans products while any product line is not yet assigned to a package, and switches to
   scanning packages once every line has been placed into one (unless :guilabel:`Force Unpacking`
   is enabled on the operation type, in which case it always scans products).

Working with packages
------------------------

If the operation type has :guilabel:`Force Packaging` enabled (see
:doc:`../../inventory/warehouses_storage/multi_warehouse`), a :guilabel:`Create New Package` toggle
appears above the product lines; turning it on and then scanning a product creates a new package and
puts that product inside it. A banner (in Hungarian: :guilabel:`Új csomag létrehozáshoz scannelje be
az első terméket`, "To create a new package, scan the first product") is shown while this mode is
active. If :guilabel:`All In Packing` is enabled instead, an :guilabel:`All In` button offers to put
everything remaining into a single package at once.

Each package on the right can be opened or closed with its folder icon, and — while
:guilabel:`Force Unpacking` is enabled — unpacked again with its :guilabel:`Unpack` button. Tapping
a package selects it, after which scanned products are added to that package instead of to a new
one.

Finish the transfer
======================

Once the relevant quantities have been scanned, click :guilabel:`Finish Scan` to validate the
transfer using the scanned quantities (unscanned quantities on a line are left unreserved). If the
operation type has :guilabel:`Allow Reverse Picking` enabled and not everything was scanned, the
button instead reads :guilabel:`Finish Scan - create reverse` and asks for confirmation (in
Hungarian: :guilabel:`Biztos, hogy lezárod a szállítólevelet? A nem scannelt mennyiség visszakerül
készletre!`, "Are you sure you want to close the delivery note? The unscanned quantity will be
returned to stock!") before creating the automatic reverse transfer described in
:doc:`../../inventory/warehouses_storage/multi_warehouse`.

Once a transfer is :guilabel:`Done`, any shipping label already generated for it (GLS, Foxpost, MPL,
or a custom carrier — see :doc:`../../inventory/shipping_receiving/setup_configuration/gls`,
:doc:`../../inventory/shipping_receiving/setup_configuration/foxpost`,
:doc:`../../inventory/shipping_receiving/setup_configuration/mpl`, and
:doc:`../../inventory/shipping_receiving/setup_configuration/custom`) can be printed directly from
this screen, and a :guilabel:`Vissza` ("Back") button returns to the picking list.

.. important::
   The operation type setting :guilabel:`Show Next Picking Button` is meant to add a
   :guilabel:`Következő` ("Next") button here to jump straight to the next ready transfer, but the
   button does not currently work in this version of the module.

============================
Delivery slip customizations
============================

eYssen extends Odoo's standard **Delivery Slip** report and the underlying transfer (``stock.picking``)
with a set of features requested by warehouse and accounting teams: extra fields printed on the slip
(transport vehicle, partner document number, EKÁER), a dedicated tab surfacing the sales order behind a
dropshipped receipt, pricing information on the transfer itself, and the option to hide the standard
"remaining quantities not yet delivered" backorder table. Each feature is delivered by its own,
independently installable module, so a company only enables the pieces it needs.

.. Screenshot plan:
.. - delivery_slips-picking-form-fields.png: Inventory app -> open any outgoing delivery in "Waiting"
..   or "Ready" state -> the transfer Form view, header area, showing the "Address for sending an
..   Invoice" field next to the customer and, further down, the "Partner Delivery Note Number",
..   "Transport Vehicle" and "EKÁER" fields next to Source Document. Click path: Inventory -> Deliveries
..   -> open a delivery order.
.. - delivery_slips-product-category-note.png: Inventory -> Configuration -> Product Categories -> open
..   a category -> Logistics section, showing the "Note on the Delivery Note" rich-text field filled in.
..   Click path: Inventory -> Configuration -> Product Categories -> open/create a category.
.. - delivery_slips-report-pdf.png: the printed Delivery Slip PDF for a delivery whose product category
..   has a note set and whose partner has a follow-up (invoicing) contact, showing the "Delivery Note"
..   title, the "Address for sending an Invoice" block, the Partner Delivery Note Number / Transport
..   vehicle / EKÁER fields, the category note, and (for a Hungarian company) the
..   Consignor/Consignee acknowledgment block at the bottom. Click path: open a delivery order -> Print
..   -> Delivery Slip.
.. - delivery_slips-so-info-tab.png: a receipt (incoming transfer) generated from a purchase order that
..   was itself created from a dropshipped sales order -> Form view -> the "Rendelés információk" /
..   Order information notebook tab, showing the linked sale order name and its product/quantity lines,
..   and the "Frissítés" (refresh) button. Click path: Purchase -> open the vendor's RFQ/PO -> Receipt
..   smart button -> open the receipt -> the last notebook tab.
.. - delivery_slips-priced-picking-form.png: an outgoing delivery created from a sales order -> Form
..   view, Operations tab, showing the "Currency" field, the "Unit Price" column added to the move
..   lines list, and the "Untaxed Amount (Demand)" / "Untaxed Amount (Completed)" totals in the
..   bottom-right pricing box. Click path: Inventory -> Deliveries -> open a delivery -> Operations tab.
.. - delivery_slips-invoice-price-warning.png: a customer invoice created from a delivery, with one
..   invoice line's unit price manually changed so it no longer matches the delivery's recorded price
..   -> Form view showing the orange warning banner above the invoice lines listing the mismatched
..   line(s). Click path: Accounting -> Customers -> Invoices -> open an invoice created from a
..   delivery -> edit a line's price.
.. - delivery_slips-report-no-backorder-section.png: the printed Delivery Slip PDF for a partially
..   delivered transfer that has an open backorder, showing that the "Remaining quantities not yet
..   delivered" table is absent (compare against the stock backorder table normally shown by Odoo).
..   Click path: create a partial delivery that generates a backorder -> open the original delivery ->
..   Print -> Delivery Slip.

Key features
============

Extra fields on the slip
-------------------------

.. image:: delivery_slips/delivery_slips-picking-form-fields.png
   :alt: Delivery order form showing the follow-up address, partner document number, vehicle and EKÁER fields

The base extension adds several fields to every stock transfer (:guilabel:`stock.picking`) and prints
them on the :guilabel:`Delivery Slip` report:

- :guilabel:`Address for sending an Invoice` — a :guilabel:`res.partner` field shown on outgoing
  transfers. It is auto-filled with the customer's child contact of type :guilabel:`Invoice/Follow-up
  address` (searched by ``parent_id`` and ``type = 'followup'``) but can be overridden manually;
- :guilabel:`Partner Delivery Note Number` — a free-text field for the delivery note number the
  customer or vendor uses on their own paperwork. It is shown on incoming transfers, is editable only
  while the transfer is not yet fully processed, and is **unique per partner** (enforced by a database
  constraint);
- :guilabel:`Transport Vehicle` and :guilabel:`EKÁER` — free-text fields for the transport vehicle
  identifier and the Hungarian EKÁER (Electronic Public Road Trade Control System) number; and
- :guilabel:`Delivery Date` — an optional date to record when goods physically arrived, for cases where
  that differs from the date the transfer was validated in Odoo.

Both :guilabel:`Transport Vehicle` and :guilabel:`EKÁER` are also added as optional columns to the
transfers list view and as search filters, and the main search box additionally matches the
:guilabel:`Partner Delivery Note Number`.

On the printed :guilabel:`Delivery Slip`, these fields appear in the document header alongside the
existing :guilabel:`Source Document`, and the follow-up address (when set) is printed as its own
"Address for sending an Invoice" block. The report title is also changed to :guilabel:`Delivery Note`,
with the transfer reference shown as a subtitle.

Per-category note on the delivery note
----------------------------------------

.. image:: delivery_slips/delivery_slips-product-category-note.png
   :alt: Product category form with the Note on the Delivery Note field filled in

A rich-text :guilabel:`Note on the Delivery Note` field is added to :guilabel:`Product Categories`
(:menuselection:`Inventory --> Configuration --> Product Categories`, in the :guilabel:`Logistics`
section). When a transfer contains products from one or more categories that have this note filled in,
every distinct note is concatenated and printed as its own block near the bottom of the
:guilabel:`Delivery Slip`, just above the signature area — for example to print handling instructions
or legal wording that only applies to certain product families.

.. note::
   For Hungarian companies (``country_code == 'HU'``), the printed slip additionally shows a fixed
   acknowledgment-of-receipt statement with :guilabel:`Consignor` / :guilabel:`Consignee` signature
   lines, followed by the free-text :guilabel:`Note` field of the transfer itself if it is filled in.
   The standard Odoo electronic-signature block is removed and replaced by this printed acknowledgment.

.. image:: delivery_slips/delivery_slips-report-pdf.png
   :alt: Printed Delivery Note PDF showing the header fields, the category note and the acknowledgment block

Sales order info on dropshipped receipts
-------------------------------------------

.. image:: delivery_slips/delivery_slips-so-info-tab.png
   :alt: Receipt form showing the Order information tab with the linked sale order and quantities

For warehouses that dropship, a receipt or delivery is often only linked to a *purchase* order, while
the sales order that triggered it is one step removed. This feature adds an :guilabel:`Order
information` tab (labeled :guilabel:`Rendelés információk` in the current build) to the transfer form.
The tab only appears when the transfer's :guilabel:`Source Document` matches one or more purchase
orders.

For each matching purchase order, the module resolves the originating sales order — first via the
standard dropshipping link (:guilabel:`Sales Order` set on the purchase order), and if that is empty,
by matching the purchase order's own :guilabel:`Source Document` to a sales order name — and lists,
per sales order, the product lines and quantities that are also present on the current transfer. A
:guilabel:`Frissítés` (:guilabel:`Refresh`) button lets a user manually recompute this information if
the underlying orders changed after the transfer was created.

Priced transfers
-----------------

.. image:: delivery_slips/delivery_slips-priced-picking-form.png
   :alt: Delivery order Operations tab showing the currency, unit price column and untaxed totals

This feature adds price and currency information directly to the transfer, so warehouse and finance
users can see the monetary value of what is being moved without leaving the transfer:

- a :guilabel:`Currency` field on the transfer (defaults to the company currency, and is automatically
  set from the linked sales order's pricelist currency, or the linked purchase order's currency, when
  the transfer is created from an order);
- a :guilabel:`Unit Price` on every move line, auto-copied from the originating sales order line or
  purchase order line (converted into the transfer's currency) when the line is created. For lines
  added manually, the price defaults to the vendor-specific price (variant vendor pricing, then general
  vendor pricing) on incoming transfers, or otherwise to the product's cost;
- :guilabel:`Subtotal (Demand)` and :guilabel:`Subtotal (Completed)` columns per move line — the
  ordered quantity and the actually processed quantity, each multiplied by the unit price; and
- :guilabel:`Untaxed Amount (Demand)` and :guilabel:`Untaxed Amount (Completed)` totals for the whole
  transfer, shown in the :guilabel:`Operations` tab and available as optional columns on the transfers
  list.

.. note::
   These fields live on the transfer's backend :guilabel:`Form` and :guilabel:`List` views. The printed
   :guilabel:`Delivery Slip` PDF itself is not modified by this feature — pricing is a backend-only
   tool for internal valuation and for the invoice consistency check below.

Invoice price consistency check
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: delivery_slips/delivery_slips-invoice-price-warning.png
   :alt: Customer invoice form showing the price mismatch warning banner above the invoice lines

On the customer invoice form, a warning banner is shown above the invoice lines whenever an invoice
line's unit price differs from the :guilabel:`Unit Price` recorded on the stock move(s) it was
generated from. This helps accounting catch cases where the invoiced price was changed after the goods
were already shipped at a different price.

Hiding the "remaining quantities" section
--------------------------------------------

.. image:: delivery_slips/delivery_slips-report-no-backorder-section.png
   :alt: Printed Delivery Slip for a partial delivery with the remaining-quantities table hidden

By default, when a delivery is only partially fulfilled and a backorder remains, Odoo's
:guilabel:`Delivery Slip` prints an extra :guilabel:`Remaining quantities not yet delivered:` table
listing the products and quantities still pending on the open backorder(s). This module forces that
table to never be printed, on every :guilabel:`Delivery Slip`, regardless of whether a backorder
exists. It is an install-and-forget behavior change with no configuration of its own — companies that
prefer to keep backorder information off the customer-facing document, for example because it is
tracked internally instead, install this module and the section disappears everywhere.

Configuration
=============

All four modules are plain, independently installable Odoo apps with no dedicated settings screen:

#. Go to :menuselection:`Apps`, remove the :guilabel:`Apps` filter, and search for the module by name
   or technical name (see :guilabel:`Scope and modules` below).
#. Click :guilabel:`Activate` / :guilabel:`Install`.
#. The corresponding fields, view changes and report changes are available immediately — no follow-up
   configuration step is required.

.. important::
   ``eyssen_stock_priced_delivery_note`` depends on ``eyssen_stock_deliveryslip``, which is
   automatically installed first. Its ``post_init_hook`` also backfills :guilabel:`Currency` and
   :guilabel:`Unit Price` on every existing transfer and stock move at install time (from the linked
   sales order's pricelist, or from the sales order line's price), so historical transfers are not left
   blank after activating the module.

The only per-record configuration points are:

- the :guilabel:`Note on the Delivery Note` field on each :guilabel:`Product Category`
  (:menuselection:`Inventory --> Configuration --> Product Categories`), for the category-note feature; and
- the :guilabel:`Address for sending an Invoice` field on a transfer, which is normally auto-filled but
  can be corrected manually per transfer.

Usage
=====

#. Open or create a delivery or receipt under :menuselection:`Inventory --> Deliveries` /
   :menuselection:`Inventory --> Receipts`.
#. Fill in :guilabel:`Partner Delivery Note Number`, :guilabel:`Transport Vehicle` and/or
   :guilabel:`EKÁER` as needed; the :guilabel:`Address for sending an Invoice` is pre-filled
   automatically when the customer has a follow-up contact.
#. If the transfer originates from a purchase order that itself came from a sales order, open the
   :guilabel:`Order information` tab to see which sales order(s) and quantities are behind it, and use
   :guilabel:`Frissítés` to refresh it if needed.
#. If pricing is enabled, check the :guilabel:`Currency` field and the per-line :guilabel:`Unit Price`
   in the :guilabel:`Operations` tab; the :guilabel:`Untaxed Amount (Demand)` / :guilabel:`(Completed)`
   totals update automatically.
#. Click :guilabel:`Print --> Delivery Slip` to generate the PDF. The printed document shows the header
   fields, any applicable category note, and — for Hungarian companies — the acknowledgment-of-receipt
   block instead of the standard signature block. The backorder "remaining quantities" table appears or
   not depending on whether ``eyssen_stock_disable_remaining_quantities_on_ds`` is installed.
#. When invoicing the delivery, review any price-mismatch warning shown on the invoice before posting
   it.

Scope and modules
==================

- ``eyssen_stock_deliveryslip`` — the base extension: follow-up invoicing address, partner delivery
  note number, transport vehicle, EKÁER, delivery date, the per-category note, and the reworked
  :guilabel:`Delivery Slip` report header and acknowledgment block.
- ``eyssen_stock_deliveryslip_so_info`` — adds the :guilabel:`Order information` tab that surfaces the
  sales order(s) and quantities behind a purchase-order-originated transfer (dropshipping).
- ``eyssen_stock_priced_delivery_note`` — adds currency, unit price and demand/completed subtotals to
  transfers, and the invoice-vs-delivery price consistency warning.
- ``eyssen_stock_disable_remaining_quantities_on_ds`` — unconditionally removes the "Remaining
  quantities not yet delivered" backorder table from the printed :guilabel:`Delivery Slip`.

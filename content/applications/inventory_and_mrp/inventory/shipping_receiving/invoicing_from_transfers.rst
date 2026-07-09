==========================
Invoicing from transfers
==========================

Standard Odoo invoices a sale or a purchase order as a whole (or through the order's own
*Create Invoice* wizard); it does not let a warehouse user turn a specific, already-validated
**delivery** or **receipt** into an invoice, and it does not keep an explicit record of exactly
which transfers ended up on which invoice line. eYssen customers who invoice per delivery note, who
group several deliveries for the same customer onto one collective invoice, or who need to trace an
invoice line back to the physical goods movement that justifies it, need both of these capabilities.
This feature adds an :guilabel:`Invoicing` action directly on stock transfers, an invoice-status
indicator per transfer, and a permanent two-way link between pickings and the invoices/vendor bills
generated from them.

.. Screenshot plan:
   .. invoicing_from_transfers-picking-list-status.png — Inventory app, Deliveries list view, with
      the "Invoice Status" column visible (badges: Not invoiced / To Invoice / Fully Invoiced / Over
      Invoiced) and the "To be Invoice" filter applied. Path: Inventory --> Deliveries --> Filters -->
      To be Invoice.
   .. invoicing_from_transfers-picking-form-button.png — A validated (Done) outgoing delivery form,
      showing the "Számlázás" header button, the "Invoice Status" field next to Source Document, and
      the "Invoiced" quantity column on the operations list. Path: Inventory --> Deliveries --> open a
      Done transfer.
   .. invoicing_from_transfers-bulk-invoice-action.png — Deliveries list view with several Done rows
      for the same customer selected via checkboxes, and the gear/Actions menu open showing the
      "Számlázás" action. Path: Inventory --> Deliveries --> select rows --> Actions (gear icon).
   .. invoicing_from_transfers-no-need-to-invoice.png — Picking form, "Other Info" tab, "Számlázás"
      group, with "No need to invoice" checked and a "Reason" filled in. Path: open a transfer -->
      Other Info tab --> scroll to the Számlázás group.
   .. invoicing_from_transfers-add-from-deliveries.png — A draft customer invoice (or vendor bill)
      form with a customer set, showing the "Add Products from Delivery Notes" button above the
      invoice lines table. Path: Accounting --> Customer Invoices --> New --> set Customer.
   .. invoicing_from_transfers-select-deliveries-wizard.png — The "Selection of Delivery Notes"
      popup wizard, listing candidate Done/unbilled transfers for the invoice's partner, with one or
      more rows selected and the "Loading Items" button visible. Path: from the invoice form, click
      "Add Products from Delivery Notes".
   .. invoicing_from_transfers-invoice-lines-detail.png — The resulting invoice's Invoice Lines tab,
      with the "Delivery Note" column and the green/red truck "fully delivered" icon column visible
      next to the product lines. Path: invoice form --> Invoice Lines tab, after loading lines from
      the wizard.
   .. invoicing_from_transfers-invoice-picking-smart-buttons.png — Two linked records side by side (or
      two crops): the picking form with the "Invoices" smart button (pencil-square icon) in the
      button box, and the invoice form with the "Pickings" smart button (truck icon) in its button
      box. Path: open an already-invoiced transfer, and the invoice created from it.
   .. invoicing_from_transfers-purchase-bill-link.png — A posted vendor bill created from a confirmed
      purchase order, with the "Pickings" smart button in the button box. Path: Purchase --> a
      confirmed order --> Create Bill --> post the bill --> open the bill form.

Invoice status on stock transfers
==================================

.. image:: invoicing_from_transfers/invoicing_from_transfers-picking-list-status.png
   :alt: Deliveries list view with the Invoice Status column and filter

Every :guilabel:`stock.picking` (delivery, receipt or internal transfer) gets an
:guilabel:`Invoice Status` field with five possible values: :guilabel:`Not invoiced`,
:guilabel:`To Invoice`, :guilabel:`Fully Invoiced`, :guilabel:`Over Invoiced`, and
:guilabel:`No need to invoice`. It is computed by comparing the total quantity moved on the
transfer's operations against the quantity already picked up by invoice lines, and is shown as a
colored badge on both the transfers list and the transfer form.

The list view also gets a :guilabel:`Direction` concept exposed as :guilabel:`Type of Operation`
(:guilabel:`Receipt`, :guilabel:`Delivery` or :guilabel:`Internal Transfer`), a
:guilabel:`To be Invoice` quick filter, and a :guilabel:`Group By: Invoice State` option, so
accounting can quickly find every completed transfer that is still waiting to be billed.

On the operations tab of the picking form, each line shows an :guilabel:`Invoiced` quantity column
next to the demand, color-coded green when the line is fully invoiced, orange when nothing has been
invoiced yet, blue when it is partially invoiced, and red when it is over-invoiced.

Creating an invoice directly from one or more transfers
==========================================================

.. image:: invoicing_from_transfers/invoicing_from_transfers-picking-form-button.png
   :alt: Delivery form with the Invoicing header button

A completed transfer whose :guilabel:`Invoice Status` is :guilabel:`Not invoiced` or
:guilabel:`To Invoice` shows an :guilabel:`Invoicing` header button (labeled ``Számlázás`` in the
current UI). The same action is also available as a bulk action from the transfers list, so several
transfers can be selected and invoiced together in one click.

.. image:: invoicing_from_transfers/invoicing_from_transfers-bulk-invoice-action.png
   :alt: Deliveries list with several rows selected and the Invoicing bulk action

When triggered — on one picking or on a multi-selection — the action:

- requires every selected transfer to belong to the **same partner**, be in the **Done** state, and
  share the **same currency**; otherwise it stops with a clear error;
- decides the target document type from the transfer's operation type: **outgoing** transfers create
  a customer invoice, any other direction (receipts, internal transfers used as vendor movements)
  creates a vendor bill;
- resolves a **fulfillment date** per transfer — for a delivery it prefers Odoo's actual completion
  date and falls back to the transfer's own delivery date; for a receipt it prefers the recorded
  delivery date (which may be earlier than the date the receipt was validated in Odoo) and falls back
  to the completion date;
- if the selected transfers do not all share the same fulfillment date, the partner must have the
  :guilabel:`Aggregate Invoice Agreement` box checked (a Hungarian-localization setting on the
  customer), otherwise the action is refused — a single invoice may not silently combine several
  fulfillment dates without that agreement in place;
- still refuses to combine transfers whose fulfillment dates fall in **different calendar months**,
  even with an aggregate agreement; and
- creates a new draft invoice/bill for the resolved partner, date and currency, and immediately fills
  it with one line per unbilled stock move on the selected transfers (see below), then opens the new
  document.

Adding delivery-note lines to an existing invoice
=====================================================

.. image:: invoicing_from_transfers/invoicing_from_transfers-add-from-deliveries.png
   :alt: Draft invoice with the Add Products from Delivery Notes button

Invoices do not have to originate from a transfer. Any draft invoice or vendor bill that already has
a :guilabel:`Customer`/:guilabel:`Vendor` set shows an :guilabel:`Add Products from Delivery Notes`
button above the invoice lines. It opens a :guilabel:`Selection of Delivery Notes` wizard prefiltered
to that partner's **Done** transfers that are not yet fully invoiced (excluding internal transfers).

.. image:: invoicing_from_transfers/invoicing_from_transfers-select-deliveries-wizard.png
   :alt: Selection of Delivery Notes wizard

After picking one or more transfers and clicking :guilabel:`Loading Items`, the wizard adds one
invoice line per remaining-to-invoice stock move, carrying over the product, the unbilled quantity,
the move's unit price (or the linked sales order line's price when the move has none), the
fulfillment date of that specific line, and a link back to the sale order line and/or purchase order
line where applicable. The sign of the quantity is adjusted automatically so the same wizard also
works when loading return/refund moves onto a credit note. Unless the invoice is an aggregate invoice
or a corrective/reversal document (which must keep the original invoice's date), the header
:guilabel:`Invoice/Bill Date` and :guilabel:`Delivery Date` are updated to the latest line date, and
the contributing sale orders are appended to the invoice's :guilabel:`Origin`.

Picking–invoice traceability
================================

.. image:: invoicing_from_transfers/invoicing_from_transfers-invoice-lines-detail.png
   :alt: Invoice lines with the Delivery Note column and fully-delivered indicator

Every invoice line created from a transfer — whether through the :guilabel:`Invoicing` button above,
the :guilabel:`Add Products from Delivery Notes` wizard, or Odoo's own sale/purchase order invoicing
— keeps a link to the exact stock move(s) it was invoiced from. This is exposed in several places:

- invoice lines get a read-only :guilabel:`Delivery Note` column listing the name(s) of the picking(s)
  behind the line (with the partner's own document reference in brackets when one was recorded on the
  receipt), and an unlabeled icon column showing a green truck when the line's invoiced quantity
  matches what was actually delivered/received, or a red truck otherwise;
- the stock move form gets an :guilabel:`Invoice Lines` group listing the invoice line(s) it has been
  billed on (visible to the Invoicing group);
- the transfer form gets an :guilabel:`Invoices` smart button, and the invoice/bill form gets a
  matching :guilabel:`Pickings` smart button — both open the linked record(s) directly, as a form when
  there is only one, or as a filtered list when there are several;

.. image:: invoicing_from_transfers/invoicing_from_transfers-invoice-picking-smart-buttons.png
   :alt: Invoices smart button on a picking and Pickings smart button on an invoice

- once a stock move is done and has an invoice line linked to it, its quantity can no longer be
  edited — Odoo refuses the change with an error, so an already-invoiced movement cannot silently
  drift out of sync with the invoice.

On the sale side, Odoo's standard :guilabel:`Create Invoice` flow is extended so that, for each sale
order line, only the done, non-scrapped, customer-facing stock moves that still have an unbilled
quantity (or, for a refund, only the moves flagged :guilabel:`To Refund`) are linked to the new
invoice line — so this traceability is populated automatically even when invoicing straight from the
sales order rather than from a transfer.

Purchase order invoicing
============================

.. image:: invoicing_from_transfers/invoicing_from_transfers-purchase-bill-link.png
   :alt: Vendor bill with the Pickings smart button

The same traceability applies on the purchase side: creating a vendor bill from a purchase order
links each bill line to the receiving stock move(s) that cover its quantity, respecting the product's
invoicing policy — :guilabel:`Ordered quantities` uses the ordered-minus-invoiced quantity,
:guilabel:`Received quantities` uses the received-minus-invoiced quantity — and walking the moves
from most to least recent.

A vendor bill can also be created **before** the goods are received when the product is invoiced on
ordered quantities. In that case, once the corresponding receipt is later validated, the newly done
stock move is retroactively linked to the vendor bill line that was already posted for that purchase
order line, so the :guilabel:`Pickings` smart button and the delivery-note traceability stay correct
even when invoicing happens ahead of the physical receipt.

Excluding a transfer from invoicing
=======================================

.. image:: invoicing_from_transfers/invoicing_from_transfers-no-need-to-invoice.png
   :alt: Other Info tab with the No need to invoice checkbox

A transfer that will never be billed — a sample shipment, an internal correction, and so on — can be
flagged :guilabel:`No need to invoice` on its :guilabel:`Other Info` tab, with a mandatory
:guilabel:`Reason` text. This sets its :guilabel:`Invoice Status` to :guilabel:`No need to invoice`
and removes it from the :guilabel:`To be Invoice` filter and from the :guilabel:`Invoicing` button's
scope.

.. important::
   Only users in the **Invoicing/Accounting Manager** group (``account.group_account_manager``) are
   allowed to set or clear this flag; anyone else attempting to edit it gets a permission error.

Configuration
================

The feature requires no dedicated settings screen — it activates automatically once the three modules
described below are installed on top of ``sale_stock`` and/or ``purchase``. It does rely on a couple
of fields owned by other eYssen modules:

- the customer's :guilabel:`Aggregate Invoice Agreement` checkbox (Hungarian localization,
  ``eyssen_l10n_hu``) must be enabled on :menuselection:`Contacts` before that customer's transfers
  with different fulfillment dates can be combined onto one invoice;
- the receipt's own partner document reference (``eyssen_stock_deliveryslip``), when filled in, is
  appended to the :guilabel:`Delivery Note` label shown on invoice lines.

.. note::
   Only the **Invoicing/Accounting Manager** group can toggle :guilabel:`No need to invoice` on a
   transfer; no separate access right needs to be granted for the rest of the feature beyond the
   normal Inventory and Invoicing access groups.

Usage
========

#. Validate a delivery or a receipt as usual so it reaches the **Done** state.
#. From the transfer's list view or form, check its :guilabel:`Invoice Status`. If it is
   :guilabel:`Not invoiced` or :guilabel:`To Invoice`, click :guilabel:`Invoicing` (on the form) or
   select several same-partner transfers and run the bulk action from the list.
#. Review the draft invoice/bill Odoo opens: it is already filled with one line per unbilled stock
   move, complete with product, quantity, price and delivery-note reference. Adjust and post it as
   any other invoice.
#. To add more transfers to an invoice that already exists (for example a partially loaded draft, or
   an invoice created manually), open it, click :guilabel:`Add Products from Delivery Notes`, select
   the additional transfers in the wizard and click :guilabel:`Loading Items`.
#. From either side of the link, use the smart buttons to navigate: :guilabel:`Invoices` on a
   transfer to see what it was billed on, or :guilabel:`Pickings` on an invoice/bill to see which
   transfers it covers.
#. If a transfer should never be invoiced, open it, go to :guilabel:`Other Info`, tick
   :guilabel:`No need to invoice` and fill in the :guilabel:`Reason`.

Scope and modules
=====================

The feature is delivered by three modules:

- ``eyssen_stock_picking_invoice`` — the :guilabel:`Invoicing` button and bulk action on transfers,
  the transfer :guilabel:`Invoice Status`/:guilabel:`No need to invoice` fields, the
  :guilabel:`Add Products from Delivery Notes` wizard, and the :guilabel:`Delivery Note` /
  fully-delivered columns on invoice lines.
- ``eyssen_stock_picking_invoice_link`` — the underlying many-to-many link between stock moves and
  invoice lines, the :guilabel:`Invoices`/:guilabel:`Pickings` smart buttons, the protection against
  editing an already-invoiced move, the automatic linking when invoicing from a sale order, and
  correct re-linking when a credit note is created (fork of the OCA
  ``stock_picking_invoice_link`` module).
- ``eyssen_purchase_stock_picking_invoice_link`` — extends the same link to purchase orders and
  vendor bills, including the retroactive link for goods invoiced before receipt (fork of the OCA
  ``purchase_stock_picking_invoice_link`` module).

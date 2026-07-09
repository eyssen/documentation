=======================
Payment-gated delivery
=======================

For prepayment sales flows — a proforma invoice, a down payment, or any other "pay first, ship
later" arrangement — goods must not physically leave the warehouse before the money has actually
arrived. **Payment-gated delivery** holds the outgoing delivery of a sale order for as long as the
order is unpaid: it blocks both the stock reservation and the :guilabel:`Validate` button, then
releases automatically the moment every invoice is settled. A privileged user can still override the
hold and ship early, and the override is fully traced in the chatter.

.. Screenshot plan:
.. - payment_gated_delivery-payment-term-toggle.png: Payment Terms form (Accounting/Invoicing app
..   --> Configuration --> Payment Terms --> open or create a term), showing the
..   "Require payment before delivery" checkbox next to the terms note field.
.. - payment_gated_delivery-order-banner.png: A confirmed sale order that uses a gated payment term
..   and has an unpaid invoice, showing the orange "Delivery is held until this order is paid."
..   banner above the order sheet. Click path: Sales app --> Orders --> open such an order.
.. - payment_gated_delivery-picking-on-hold.png: The delivery's transfer form for that order, showing
..   the red "On Hold" ribbon plus the "Hold" toggle (on) and "Hold Reason" = "Awaiting payment for
..   delivery". Click path: from the sale order, click the "Delivery" smart button.
.. - payment_gated_delivery-validate-blocked-error.png: The error dialog raised when clicking
..   "Validate" on that held delivery ("This delivery is held until the order is paid...").
..   Click path: on the held delivery form, click Validate.
.. - payment_gated_delivery-release-button.png: The held delivery's header showing the yellow
..   "Release for delivery" button (visible only to users in the "Deliver without payment" group)
..   and its confirmation popup. Click path: log in as a user with that group, open the held
..   delivery, click "Release for delivery".
.. - payment_gated_delivery-release-chatter.png: The same delivery's chatter after confirming the
..   release, showing the logged message "Delivery manually released for shipping before full
..   payment by <user>." Click path: after confirming the release popup, scroll to the chatter.
.. - payment_gated_delivery-deliver-without-payment-group.png: The user form's Access Rights /
..   Preferences area showing the "Deliver without payment" group (Inventory category) being
..   assigned. Click path: Settings app --> Users & Companies --> Users --> open a user.
.. - payment_gated_delivery-auto-release-paid-invoice.png: The customer invoice after registering
..   full payment (Payment Status = "Paid"), next to the now-released delivery (no ribbon, state
..   "Ready"). Click path: Accounting app --> Customer Invoices --> open the invoice tied to the
..   order --> Register Payment --> pay the full amount --> reopen the delivery.
.. - payment_gated_delivery-backorder-rehold.png: A backorder transfer created from a partially
..   validated, still-unpaid delivery, showing it re-acquired the "On Hold" ribbon on creation.
..   Click path: on a manually released but still-unpaid delivery, validate a partial quantity so
..   Odoo proposes a backorder, then open the resulting backorder transfer.

.. image:: payment_gated_delivery/payment_gated_delivery-order-banner.png
   :align: center
   :alt: Sale order banner warning that delivery is held until payment.

The reusable "On Hold" primitive
=================================

Payment-gated delivery is built on top of a generic hold mechanism that lives in the base
``eyssen_stock`` module and is available on every transfer, independent of sales or payments:

- a :guilabel:`Hold` toggle and a read-only :guilabel:`Hold Reason` field on :guilabel:`stock.picking`;
- a red :guilabel:`On Hold` ribbon on the transfer form whenever :guilabel:`Hold` is ticked, plus
  :guilabel:`On Hold` / :guilabel:`Off Hold` filters in the transfers list search panel; and
- the methods ``action_set_hold(reason)`` and ``action_release_hold()``, which set or clear
  :guilabel:`Hold` and :guilabel:`Hold Reason` together.

Setting :guilabel:`Hold` immediately unreserves the transfer's stock moves; releasing it re-triggers
reservation (``_action_assign``) so the transfer picks back up available stock automatically. Any
module — not only ``sale_stock_payment_gate`` — can put a transfer on hold this way and expect
reservation to stay off until it is released.

.. note::
   By itself, the generic :guilabel:`Hold` only stops *reservation*. It does not block
   :guilabel:`Validate` — that additional, stricter guard is specific to the payment gate described
   below.

The payment-term flag
======================

.. image:: payment_gated_delivery/payment_gated_delivery-payment-term-toggle.png
   :align: center
   :alt: Payment term form with the Require payment before delivery checkbox.

Whether an order is gated at all is decided by its **payment term**. The
:guilabel:`Require payment before delivery` checkbox, added to the payment term form, marks a term
as "pay before you ship." Orders using a payment term with the checkbox off — for example a
cash-on-delivery term — are never held. Orders with no payment term at all are likewise never held.

Holding the delivery on order confirmation
===========================================

When a sale order is confirmed, and its payment term requires payment before delivery, every
not-yet-done, not-yet-cancelled *outgoing* picking of that order is put on hold in one step:
:guilabel:`Hold` is ticked, :guilabel:`Hold Reason` is set to *"Awaiting payment for delivery,"* and
the gate's own :guilabel:`Held for payment` field is set as well. If the order is already fully paid
at confirmation time (for example, a proforma or down payment was settled before confirmation), no
hold is applied and the delivery proceeds normally.

.. image:: payment_gated_delivery/payment_gated_delivery-picking-on-hold.png
   :align: center
   :alt: Delivery transfer showing the On Hold ribbon and the payment hold reason.

The hard gate: no reservation, no validation
=============================================

A payment-held delivery is blocked twice over, so it cannot slip through either the automatic or the
manual path:

- **No reservation.** The gate overrides stock-move reservation so that any move belonging to a
  payment-held picking is skipped, both when Odoo auto-assigns stock on confirmation and when a user
  clicks :guilabel:`Check Availability`. This check is on the gate's own :guilabel:`Held for payment`
  flag, so it holds even if the generic :guilabel:`Hold` toggle is separately cleared.
- **No validation.** Clicking :guilabel:`Validate` on a payment-held delivery raises an error instead
  of shipping the goods, pointing the user to the :guilabel:`Release for delivery` button described
  below.

.. image:: payment_gated_delivery/payment_gated_delivery-validate-blocked-error.png
   :align: center
   :alt: Error dialog blocking validation of a payment-held delivery.

.. important::
   Directly writing :guilabel:`Held for payment` = *unchecked* on a picking is blocked for any user
   who is **not** in the :guilabel:`Deliver without payment` group. Only that group's
   :guilabel:`Release for delivery` button (or a privileged/system write) can lift the gate — a plain
   :guilabel:`write()` from another flow cannot silently bypass it.

Automatic release when the order is paid
=========================================

.. image:: payment_gated_delivery/payment_gated_delivery-auto-release-paid-invoice.png
   :align: center
   :alt: Fully paid customer invoice next to its now-released delivery.

An order counts as **delivery-paid** once every posted customer invoice linked to it reaches payment
status :guilabel:`Paid` or :guilabel:`In Payment`. A ``base.automation`` rule watches the
:guilabel:`Payment Status` field on customer invoices (``account.move``, ``out_invoice``) and, on
every create or write that touches it, re-evaluates all outgoing, not-done pickings of the related
orders:

- if the order is now fully paid, any picking still on payment hold is released — :guilabel:`Held for
  payment`, :guilabel:`Hold` and :guilabel:`Hold Reason` are all cleared, and reservation runs again
  automatically; and
- if the order is **not** fully paid and a picking is not currently held (and was not manually
  released — see below), it is re-held with the reason *"Payment reversed - delivery re-blocked."*

.. note::
   :guilabel:`In Payment` counts as paid because it represents a full receipt for which reconciliation
   with the bank statement is still pending. A **partial** payment never releases the hold. The gate
   assumes the linked invoice(s) cover the full order amount — with a native *partial* down payment,
   a fully-paid partial invoice would release the whole delivery early; that scenario is explicitly
   out of scope.

Re-blocking on payment reversal
================================

Because the same automation re-evaluates the order on *every* change to :guilabel:`Payment Status`,
reversing a payment (for example, unreconciling or cancelling a payment so the invoice drops back to
:guilabel:`Not Paid`) automatically re-applies the hold to any not-done delivery of that order — as
long as the delivery was not manually released by a privileged user.

.. tip::
   The gate reads only the standard ``account.move`` / ``payment_state`` fields on posted customer
   invoices. It does not depend on any localization: the same logic releases the delivery whether the
   order was settled through a Hungarian NAV *proforma* / *díjbekérő* invoice, a regular down-payment
   invoice, or any other module that eventually posts and pays a customer invoice against the order.

Manual override: releasing a delivery before payment
======================================================

.. image:: payment_gated_delivery/payment_gated_delivery-release-button.png
   :align: center
   :alt: Release for delivery button on a held transfer, with its confirmation prompt.

Sometimes a delivery genuinely needs to ship before the order is fully paid (goodwill shipment,
trusted customer, manual arrangement). The :guilabel:`Release for delivery` button on the transfer's
header does this:

- it is visible only when the picking is on payment hold, and only to users in the
  :guilabel:`Deliver without payment` security group;
- clicking it asks for confirmation, then clears :guilabel:`Held for payment`, :guilabel:`Hold` and
  :guilabel:`Hold Reason`, and sets :guilabel:`Manually released for delivery` to keep track of the
  override; and
- a chatter message records **who** released the delivery and **when**.

.. image:: payment_gated_delivery/payment_gated_delivery-release-chatter.png
   :align: center
   :alt: Chatter entry logging the manual release of a delivery.

A delivery flagged :guilabel:`Manually released for delivery` is **not** re-held by the automatic
sync described above, even if the order later turns out to be unpaid again — the manual decision is
respected until someone re-applies a hold by hand.

Backorders inherit the hold
============================

If a payment-held (or previously released) delivery is only partially shipped and Odoo creates a
backorder for the remainder, the backorder is re-evaluated against the same rule as the original
delivery: when the order still requires payment before delivery and is not yet fully paid, the new
backorder transfer is put on hold again, with the same *"Awaiting payment for delivery"* reason —
even if the original transfer had been manually released.

.. image:: payment_gated_delivery/payment_gated_delivery-backorder-rehold.png
   :align: center
   :alt: Backorder transfer automatically re-held for payment.

Order-level visibility
=======================

The sale order form shows a warning banner — *"Delivery is held until this order is paid."* — above
the order sheet whenever any of the order's deliveries is currently on payment hold. This is driven
by the computed :guilabel:`Delivery held for payment` field, so sales staff see the gated status at a
glance without opening the transfer.

Configuration
=============

#. Make sure ``sale_stock_payment_gate`` is installed. It automatically pulls in ``eyssen_stock``,
   ``sale_stock``, ``account`` and ``base_automation``.
#. Go to :menuselection:`Accounting/Invoicing app --> Configuration --> Payment Terms`, open (or
   create) the payment term used for prepaid/proforma sales, and tick :guilabel:`Require payment
   before delivery`. Leave the checkbox unticked on terms such as cash-on-delivery.
#. Grant the :guilabel:`Deliver without payment` group (category :guilabel:`Inventory`) to the users
   who are allowed to override the gate — for example warehouse supervisors — via
   :menuselection:`Settings app --> Users & Companies --> Users`. This group also needs ordinary
   inventory read/write access to actually see and release the transfer.

.. image:: payment_gated_delivery/payment_gated_delivery-deliver-without-payment-group.png
   :align: center
   :alt: Assigning the Deliver without payment group to a user.

No further setup is required: the ``base.automation`` rule and the hold/release logic are active as
soon as the module is installed and at least one payment term has the flag enabled.

Usage
=====

#. Confirm a sale order that uses a gated payment term. Its outgoing delivery is created and
   immediately put on hold, unless the order is already fully paid.
#. The order form shows the :guilabel:`Delivery is held until this order is paid.` banner, and the
   delivery transfer shows the :guilabel:`On Hold` ribbon with :guilabel:`Hold Reason` = *"Awaiting
   payment for delivery."* :guilabel:`Check Availability` does not reserve stock, and
   :guilabel:`Validate` refuses to run.
#. Create and post the customer invoice (proforma, down payment, or regular invoice) for the order,
   then register the full payment. As soon as the invoice's :guilabel:`Payment Status` reaches
   :guilabel:`Paid` or :guilabel:`In Payment`, the automation releases the delivery: the hold is
   cleared and stock is reserved again.
#. Validate the now-released delivery normally.
#. If early shipment is unavoidable, a user with the :guilabel:`Deliver without payment` group can
   open the held transfer and click :guilabel:`Release for delivery` instead of waiting for payment.
   The override is logged in the chatter and survives later payment-status changes; if a backorder is
   later created for the remaining quantity on that same order, it is re-held automatically unless the
   order has become fully paid by then.

Scope and modules
==================

The feature is delivered by two modules:

- ``eyssen_stock`` — the generic, reusable :guilabel:`Hold` / :guilabel:`Hold Reason` primitive on
  transfers (ribbon, toggle, search filters, and the reservation-blocking/re-reserval logic), used
  here as the base building block.
- ``sale_stock_payment_gate`` — the payment gate itself: the :guilabel:`Require payment before
  delivery` payment-term flag, the hold-on-confirm logic, the hard reservation/validation block, the
  ``base.automation``-driven auto-release and re-block on payment changes, the
  :guilabel:`Deliver without payment` group with its :guilabel:`Release for delivery` button and
  chatter trail, the backorder re-hold, and the order-level warning banner.

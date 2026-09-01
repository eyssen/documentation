==============================
Handling withdrawals (backend)
==============================

This page describes how an RMA agent works with confirmed withdrawal declarations in the backend,
how a withdrawal is turned into a physical return, and the full **RMA approval process** that the
derived return then follows.

The Withdrawals menu
====================

Confirmed declarations are listed under :menuselection:`Sales --> Orders --> Withdrawals`. This menu
is kept **separate** from :menuselection:`Sales --> Orders --> RMAs`: the :guilabel:`RMAs` list shows
only ordinary returns, while the :guilabel:`Withdrawals` list shows only withdrawal declarations.

The list shows at least the declaration reference (e.g. ``RMA/2026/00034``), the customer, and the
:guilabel:`Posted` state. Open a row to work the declaration form.

Records arrive here automatically from the portal, already in the :guilabel:`Posted` state.

.. important::
   **Posted is the correct final state for a withdrawal.** The declaration is not “stuck in draft”
   and is not supposed to be marked :guilabel:`Done`. Logistics and refunds always happen on a
   **separate ordinary RMA** created with :guilabel:`Start Return / Refund` (see below).

The withdrawal declaration form
===============================

A withdrawal record looks like an RMA form but the header and sheet are withdrawal-specific:

- a blue **info banner** that reminds the agent: this is the legal declaration; use
  :guilabel:`Start Return / Refund` for the physical return;
- a **Withdrawal Declaration** group with the read-only :guilabel:`Consumer Name`,
  :guilabel:`Consumer Email`, :guilabel:`Withdrawal Confirmed On` (the durable-proof timestamp), the
  :guilabel:`Confirmation Email` state, and — once a return has been started — the
  :guilabel:`Source Withdrawal` link on the *derived* RMA;
- the **order lines** with the withdrawn products and quantities (one line per serial for
  serial-tracked products); and
- two dedicated header buttons: :guilabel:`Start Return / Refund` (Hungarian UI:
  :guilabel:`Visszáru / visszatérítés indítása`) and :guilabel:`Resend Confirmation`.

The :guilabel:`Post`, :guilabel:`Done` and :guilabel:`Delete` buttons that exist on ordinary RMAs are
**hidden** for a withdrawal, because a declaration is never processed through that flow.

The declaration snapshot
------------------------

The :guilabel:`Declaration` notebook tab shows the **immutable HTML snapshot** captured at
confirmation time: the declaration title, the consumer's name and e-mail, the submission timestamp
and the list of products and quantities. This snapshot is the legal record and is never recomputed.
It should match the confirmation e-mail content.

Non-rejectable guarantees
=========================

Because a withdrawal is a legally binding statement, several database-level guards prevent it from
being treated like a rejectable RMA:

- a declaration **line cannot be set to** :guilabel:`Rejected`;
- the manual :guilabel:`Post`, mark-as-:guilabel:`Done` and auto-approve actions all **refuse to
  run** on a withdrawal; and
- the *is-withdrawal* flag is set at creation and **cannot be changed** afterwards, so a record can
  never be flipped between an ordinary RMA and a withdrawal.

The confirmation e-mail
=======================

The durable-medium confirmation e-mail is sent automatically when the declaration is confirmed. It
lists **every product line** on the declaration (reference, consumer, timestamp, and a table of
products and quantities). It is **resilient by design** — a mail failure must never invalidate an
already-valid withdrawal:

- the :guilabel:`Confirmation Email` field tracks the state: :guilabel:`Pending`, :guilabel:`Sent`
  or :guilabel:`Failed`;
- if sending fails, the error is logged and a **to-do activity** is scheduled for the agent instead
  of raising an error; and
- the agent can retry at any time with the :guilabel:`Resend Confirmation` button. There is **no
  automatic retry cron** — recovery is always a deliberate manual action.

.. warning::
   The e-mail body is a **QWeb** template (``mail.template``). Edit it only as technical/QWeb source
   (or through a controlled update). The visual HTML editor can break the product table loop so that
   only the last line (often a shipping product) appears in the e-mail while the backend still shows
   every line. After any edit, send a test and verify **all** products appear.

Starting the physical return and refund
=======================================

A withdrawal record never moves stock or money on its own. When the consumer ships the goods back
(or the agent otherwise decides to process the return), the agent clicks :guilabel:`Start Return /
Refund` (:guilabel:`Visszáru / visszatérítés indítása` in Hungarian).

Agent checklist (withdrawal → goods back → refund)
--------------------------------------------------

#. Open the declaration under :menuselection:`Sales --> Orders --> Withdrawals` (not under
   :guilabel:`RMAs`).
#. Review the lines and the :guilabel:`Declaration` tab snapshot.
#. Click :guilabel:`Start Return / Refund`. A **new ordinary RMA** opens in :guilabel:`Draft`.
#. On that RMA: set a return reason if needed → :guilabel:`Post` → accept each line
   (thumbs-up) → :guilabel:`Done`.
#. Validate the **incoming transfer** when the parcel physically arrives (same as any other return).
#. Create the **credit note / refund** the same way you always did for returns — the withdrawal
   itself does not change invoicing.

What :guilabel:`Start Return / Refund` creates
----------------------------------------------

This creates a **separate, ordinary RMA** from the withdrawal's lines:

- the new RMA is a normal, *rejectable* return (it is **not** a withdrawal);
- it links back to the declaration through the :guilabel:`Source Withdrawal` field; and
- the original withdrawal record stays **inert, immutable and non-rejectable** — it is never run
  through the picking or refund logic itself.
- **Shipping / delivery lines are skipped.** If an older declaration still lists a carrier line
  (from before the shipping exclusion), that line is not copied onto the derived RMA. A
  *shipping-only* withdrawal cannot start a physical return (the system shows an error).

.. note::
   The withdrawn quantities are not double-counted. While the derived return RMA exists, the
   originating withdrawal is excluded from the open-quantity budget, so the same units are never
   counted as committed twice.

The new RMA then follows the standard RMA approval process described below.

When you already handled the return without RMA
-----------------------------------------------

If the goods were already taken back with the classic stock return (or the money was already
refunded) **before** the agent used :guilabel:`Start Return / Refund`:

- the **withdrawal declaration can stay as-is** — it remains the legal proof of the consumer's
  statement;
- **do not** start a second return RMA for the same units if stock and money are already settled;
- optionally add an internal note on the withdrawal so colleagues know the logistics were closed
  outside this flow.

When the parcel was not collected (non-pickup)
----------------------------------------------

A “customer never took the parcel / carrier brought it back” case is **logistics**, not the same as
processing a portal withdrawal through :guilabel:`Done`. Use the ordinary return / non-pickup RMA
path (or your existing carrier process). The withdrawal, if the consumer also declared one, still
only means “legal statement on file” until you deliberately start a return or cancel the need for
one.

The RMA approval process
========================

The return RMA — whether created from a withdrawal, from the portal, or manually — moves through a
three-state lifecycle: **Draft → Posted → Done**. Each step is gated by a security group.

Draft → Posted
--------------

:guilabel:`Post` validates and submits the request (requires the **RMA Manager** group):

- every line with a positive quantity must have a **return reason**;
- the RMA receives its sequence reference; and
- the order is tagged on the linked sales order with the *requested* status.

The :guilabel:`Apply Reason to Lines` helper can set one reason (and its destination location) on
all draft lines at once.

Posted → line decisions
-----------------------

Each line is then individually **accepted** or **rejected** (requires the **RMA Approval** group):

- :guilabel:`Accept` — the accepted quantity may not exceed the delivered quantity;
- :guilabel:`Reject` — a **reason for rejection** is mandatory.

Posted → Done
-------------

:guilabel:`Mark as Done` finalizes the RMA (requires the **RMA Approval** group). It is only allowed
once **every** line has been accepted or rejected. On completion the system **generates the stock
pickings**:

- **incoming** pickings for returned/replaced/refunded and non-pickup lines; and
- **outgoing** pickings for replacement and resend lines, respecting the warehouse's multi-step
  delivery configuration.

Returns putaway
~~~~~~~~~~~~~~~

Each returned product is routed to a destination resolved in this order:

#. an explicit **destination location** set on the line (or inherited from the reason);
#. the **shelf** (configured storage category) under the warehouse where the product already has the
   most stock on hand;
#. the company's **WEB return location** (when it belongs to that warehouse); otherwise
#. the warehouse stock location.

See :doc:`configuration` for the shelf category and WEB return location settings.

Order status feedback
=====================

As the return progresses, the linked sales order is automatically tagged with the current RMA
status — for example *requested*, *refused*, *being returned*, *taken back* or *closed* — so the
sales team always sees the live state. A non-pickup return additionally flags the order as needing a
manual refund for the finance team.

.. important::
   Withdrawal declarations never receive an order status tag and never appear in the order-status
   feedback: only the ordinary RMAs do. The withdrawal itself remains a pure legal record.

Security groups
===============

The actions above are restricted to the RMA security groups:

- **RMA User** — create RMAs and start a return from a withdrawal;
- **RMA Manager** — post and delete RMAs; and
- **RMA Approval** — accept or reject lines and mark an RMA as done.

.. note::
   The **Sales / Administrator** (Sales manager) group includes **RMA Approval** by default. Sales
   managers therefore see the :menuselection:`Sales --> Orders --> RMAs` and :guilabel:`Withdrawals`
   menus and can process withdrawals out of the box, without any extra per-user configuration. Grant
   the **RMA Manager** group separately to users who also need to configure return reasons or delete
   RMAs.

.. seealso::
   - The consumer-facing flow: :doc:`consumer_portal`
   - Periods, deadlines and putaway settings: :doc:`configuration`

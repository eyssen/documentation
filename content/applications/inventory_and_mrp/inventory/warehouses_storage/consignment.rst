=================
Consignment stock
=================

**Consignment stock** lets a company ship goods to a customer's own site while keeping legal
ownership of them until the customer actually sells or uses the goods. The customer is only
invoiced for what they consumed, and can send unsold goods back at any time — the company never
loses track of what is on-site, what has been paid for, and what has been returned.

The ``eyssen_consignment`` module builds this on top of standard **Sales** and **Inventory**: it
adds a dedicated stock location per consignment customer, keeps stock legally owned by the company
even while it physically sits at the customer, tracks delivered/settled/returned quantities on
each sale order line, and drives periodic **settlement** (what got sold), **return** (what came
back unsold) and **verification** (physical stock check) cycles through a single
:guilabel:`Consignment` document.

How consignment stock works
============================

Per-customer consignment location
----------------------------------

.. screenshot:: inventory-consignment-customer-form
   :menu: Contacts ‣ (a customer) ‣ Sales & Purchase tab
   :shows: The "Customer Consignment" group of a customer form with "Can Buy on Consignment" enabled, the
      consignment stock location, the "Consignment Stock Count" and, in the header, the "Settlement Report"
      button.
   :highlight: The "Can Buy on Consignment" checkbox and the "Settlement Report" button (red frames).
   :data: Customer "Deco Addict" with a consignment location holding a few products.
   :module: eyssen_consignment
   :notes: English UI, light theme, 1440px width, crop to the group and the header button.

Every consignment customer gets its own dedicated stock location. On the customer's
form (:menuselection:`Contacts --> a customer --> Sales & Purchase tab --> Customer Consignment`),
enabling :guilabel:`Can Buy on Consignment` automatically creates a location flagged as a
**Customer Consignment Location**, of the *Customer Location* type and linked back to the partner, as a child of the
company's configured :guilabel:`Customer Consignment Stock Location`. Renaming the customer later
renames the location to match.

- :guilabel:`Buy on Consignment by Default` pre-checks new sale orders and deliveries for that
  customer as consignment automatically.
- The :guilabel:`Consignment Stock` smart button opens the stock quants currently held at that
  customer's location.
- The setting **cannot be disabled** while the customer still has stock at that location — the
  system blocks it until everything has been settled or returned.
- For a delivery-address contact under a company, the consignment section is only usable if the
  **parent company** already has :guilabel:`Can Buy on Consignment` enabled.

.. important::
   Consigned stock never becomes the customer's property while it sits at their location.
   Whenever an outgoing delivery for a consignment order is validated, the resulting stock quants
   at the customer's consignment location are re-owned to the **company**, not the customer. The
   goods only leave the company's books once a settlement report confirms they were actually sold.

Consignment sale orders and deliveries
----------------------------------------

.. screenshot:: inventory-consignment-sale-order
   :menu: Sales ‣ Orders ‣ Orders ‣ (a confirmed consignment order)
   :shows: A confirmed sales order with the "Consignment Order" checkbox ticked next to the payment terms,
      and the order-line list showing the "Cons. Remaining Quantity" column.
   :highlight: The "Consignment Order" checkbox and the "Cons. Remaining Quantity" column (red frames).
   :data: Two order lines; 10 delivered, 4 settled, 0 returned, so 6 remaining on the first line.
   :module: eyssen_consignment
   :notes: English UI, light theme, 1440px width, crop to the header fields and the order lines.

A sale order exposes a :guilabel:`Consignment Order` checkbox next to the payment terms (only
visible if the customer :guilabel:`Can Buy on Consignment`, and pre-checked automatically when the
customer has :guilabel:`Buy on Consignment by Default`). Deliveries generated from a consignment
order automatically inherit the same flag, and a delivery's :guilabel:`Consignment Order` flag can
also be set directly if a picking is created outside the normal sale flow.

.. screenshot:: inventory-consignment-policy-warning
   :menu: Sales ‣ Orders ‣ Quotations ‣ (a consignment quotation)
   :shows: The red alert banner above the order lines listing the products that cannot be sold on
      consignment because their "Sale Policy" resolves to "Disabled".
   :highlight: The alert banner (red frame).
   :data: One order line whose product has Sale Policy "Disabled".
   :module: eyssen_consignment
   :notes: English UI, light theme, 1440px width, crop to the banner and the offending line.

Per-product control — every product can be restricted from consignment sales individually with its
:guilabel:`Sale Policy` (see :ref:`consignment/configuration`). If a consignment order or delivery
contains a product whose policy resolves to :guilabel:`Disabled` — or if the customer is not
allowed to buy on consignment at all — a red warning banner lists the offending products, and
sending the quotation, confirming the order, or validating the delivery is blocked until the issue
is resolved.

.. screenshot:: inventory-consignment-delivery
   :menu: Inventory ‣ Delivery Orders ‣ (a delivery from a consignment order)
   :shows: The outgoing delivery of a consignment order with the "Consignment Order" checkbox next to the
      read-only "Owner" field, and the destination set to the customer's consignment location.
   :highlight: The "Consignment Order" checkbox, the "Owner" field and the destination location (red
      frames).
   :data: Delivery WH/OUT/00002 to "Deco Addict"'s consignment location; owner is the company.
   :module: eyssen_consignment
   :notes: English UI, light theme, 1440px width, crop to the header fields.

On the outgoing delivery itself, the destination location is automatically forced to the
customer's consignment location (overriding any other destination set on the transfer), and the
:guilabel:`Owner` field becomes read-only — it stays under the company's ownership, per the note
above.

Cons. Quantity on the sale order line
========================================

Each sale order line on a consignment order tracks four running quantities, shown as optional
columns on the order line list:

- :guilabel:`Cons. Delivered Quantity` — the quantity actually delivered to the customer's
  consignment location (computed from done, non-scrapped stock moves).
- :guilabel:`Cons. Settled Quantity` — the quantity a **Sales Settlement Report** has confirmed as
  sold.
- :guilabel:`Cons. Returned Quantity` — the quantity a **Returns Submission** report has sent back
  unsold.
- :guilabel:`Cons. Remaining Quantity` — delivered minus settled minus returned: what is still
  physically out at the customer, neither paid for nor returned yet.

.. important::
   Consigned goods are **not invoiced on delivery**. For consignment lines the quantity to invoice
   excludes both the remaining (still out, unsettled) and the returned quantity — only settled
   goods become billable. This is what makes the settlement report the trigger for invoicing
   instead of the delivery itself.

.. _consignment/settlement-reports:

Consignment Settlement Reports
=================================

.. screenshot:: inventory-consignment-report-list
   :menu: Sales ‣ Orders ‣ Consignment
   :shows: The consignment settlement report list with records of all three types and their Draft, Done and
      Cancelled state badges, next to the reference, customer and date.
   :highlight: The "State" column (red frame).
   :data: Four reports: two Sales Settlement Reports (one draft, one done), one Returns Submission and one
      cancelled.
   :module: eyssen_consignment
   :notes: English UI, light theme, 1440px width, full list view.

All settlement, return and verification cycles are handled through a single
:guilabel:`Consignment Settlement Report` document, listed under
:menuselection:`Sales --> Orders --> Consignment`. Each report has a sequence reference
(``CSR/<year>/#####``), belongs to one customer, and has a :guilabel:`Type`:

- :guilabel:`Sales Settlement Report` — records what the customer actually sold/consumed.
- :guilabel:`Returns Submission` — records what the customer is sending back unsold.
- :guilabel:`Inventory Verification` — a read-only style snapshot of the raw physical quantity at
  the customer's location, used purely to reconcile stock; it is never confirmed into an invoice or
  a return.

.. tip::
   The normal entry point is the :guilabel:`Settlement Report` button on the customer's form: it
   finds (or creates) that customer's current draft report and refreshes its lines automatically.
   A report can also be created directly from the :guilabel:`Consignment` menu.

Syncing lines with physical stock
------------------------------------

.. screenshot:: inventory-consignment-settlement-form
   :menu: Sales ‣ Orders ‣ Consignment ‣ (a draft Sales Settlement Report)
   :shows: A draft settlement report with its line list (Product, Cons. Quantity, Settled Quantity) and the
      "Add Bulk Products", "Set All", "Set Null" and "Confirm" buttons.
   :highlight: The "Settled Quantity" column and the "Set All" / "Set Null" header buttons (red frames).
   :data: Customer "Deco Addict"; four product lines, two of them partly settled.
   :module: eyssen_consignment
   :notes: English UI, light theme, 1440px width, crop to the header buttons and the lines.

Refreshing a draft report (automatically when opened via the customer button, or explicitly when
:guilabel:`Set to Draft` is used) recomputes one line per product, with :guilabel:`Cons. Quantity`
set to the physical quantity on hand at the customer's consignment location.

.. note::
   On **Sales Settlement Report** and **Returns Submission** reports, any quantity already
   committed to a previous, not-yet-arrived consignment return is subtracted from
   :guilabel:`Cons. Quantity`, so a fully-returned product correctly shows ``0`` instead of the
   stale physical count. **Inventory Verification** reports intentionally skip this adjustment and
   always show the raw physical quantity, since their purpose is stock reconciliation.

For each line, the agent enters (or edits) the :guilabel:`Settled Quantity` — capped between ``0``
and :guilabel:`Cons. Quantity` — either row by row, with the header :guilabel:`Set All` /
:guilabel:`Set Null` shortcuts, or in bulk:

.. screenshot:: inventory-consignment-bulk-products
   :menu: Sales ‣ Orders ‣ Consignment ‣ (a draft report) ‣ Add Bulk Products
   :shows: The "Add Bulk Products" dialog with the Format and "Based On" fields, the live example text and
      the paste/CSV/Excel input.
   :highlight: The "Format" and "Based On" fields (red frame).
   :data: Format "Copy/Paste", Based On "Default Code", three pasted lines.
   :module: eyssen_consignment
   :notes: English UI, light theme, 1440px width, crop to the dialog.

:guilabel:`Add Bulk Products` opens a wizard that resets every line to unsettled and then applies
quantities pasted as text, or uploaded as a CSV/Excel file, matching each row to a product by
internal reference, barcode, or product name.

Serial and lot-tracked products
------------------------------------

For a tracked product, :guilabel:`Settled Quantity` is not typed in directly: the agent opens the
line's :guilabel:`Lots/Serials` picker and selects the exact serials/lots present at the customer's
location (only lots actually on hand there are selectable). The picked total must equal the
quantity being settled or returned before the report can be confirmed, and each serial movement is
recorded so the same serial can never be both settled and returned for the same customer.

Confirming a settlement report
------------------------------------

:guilabel:`Confirm` is only available on a draft report with at least one settled/returned
quantity, and behaves differently by type:

**Sales Settlement Report** — matches the settled quantities FIFO against that customer's open
consignment sale order lines (oldest order first), then:

- creates an internal transfer moving the settled quantity from the customer's consignment
  location to the company's own consignment stock location;
- increases :guilabel:`Cons. Settled Quantity` on every matched sale order line;
- generates a single customer invoice, one invoice line per matched sale order line, using that
  line's price, discount and taxes; and
- sets the report to :guilabel:`Done`, linking the generated picking and invoice (visible from the
  :guilabel:`Pickings` and :guilabel:`Invoices` smart buttons).

**Returns Submission** — FIFO-matches the same way, then:

.. screenshot:: inventory-consignment-return-report
   :menu: Sales ‣ Orders ‣ Consignment ‣ New (Type = Returns Submission)
   :shows: A draft Returns Submission report with the return quantities filled in on its lines, ready to be
      confirmed.
   :highlight: The "Type" field set to "Returns Submission" and the filled-in "Settled Quantity" column (red
      frames).
   :data: Customer "Deco Addict"; two products being sent back unsold.
   :module: eyssen_consignment
   :notes: English UI, light theme, 1440px width, crop to the header fields and the lines.

- creates a **Consignment Return** :doc:`RMA <../../../sales/withdrawal/backend>` sourced from the
  customer's consignment location, one line per matched sale order line;
- increases :guilabel:`Cons. Returned Quantity` on every matched sale order line; and
- auto-approves the RMA, which schedules (but does not yet validate) an incoming receipt back into
  the warehouse — the physical arrival is still confirmed manually by a warehouse operator, which
  is exactly why the sync above has to discount it from the next report's :guilabel:`Cons.
  Quantity`.

.. note::
   Only **Sales Settlement Report** type documents can be cancelled (:guilabel:`Cancel Settlement`)
   once done — this reverses the invoice (credit note) and the stock move, and rewinds
   :guilabel:`Cons. Settled Quantity` on the sale order lines. Returns are undone through the RMA
   flow instead, not by cancelling the settlement report.

.. important::
   Once a report is :guilabel:`Done` or :guilabel:`Cancelled`, its settled/consigned quantities and
   audit links are locked against further edits — they must be reset with :guilabel:`Set to Draft`
   first, which also re-checks that no leftover audit data blocks the transition.

.. _consignment/configuration:

Configuration
================

.. screenshot:: inventory-consignment-settings
   :menu: Inventory ‣ Configuration ‣ Settings
   :shows: The "Traceability" section of the Inventory settings showing, right below "Set owner on stored
      products", the "Customer Consignment Stock Location", "Customer Consignment Report Operation Type" and
      "Consignment Sale Product Policy" fields.
   :highlight: The three consignment fields (red frame).
   :data: Location "Partner Locations/Consignment", operation type "Consignment settlement", policy
      "Enabled".
   :module: eyssen_consignment
   :notes: English UI, light theme, 1440px width, crop to the Traceability settings block.

Company-wide settings, at :menuselection:`Inventory --> Configuration --> Settings`, in the
**Traceability** section right below :guilabel:`Set owner on stored products`:

- :guilabel:`Customer Consignment Stock Location` — the parent location under which every new
  customer's consignment location is created. Required before :guilabel:`Can Buy on Consignment`
  can be enabled on any customer.
- :guilabel:`Customer Consignment Report Operation Type` — the operation type used for the internal
  transfers generated when a settlement report is confirmed or cancelled.
- :guilabel:`Consignment Sale Product Policy` — the company-wide default (:guilabel:`Enabled` /
  :guilabel:`Disabled`) applied to products whose own :guilabel:`Sale Policy` is left on
  :guilabel:`Use default`.

.. screenshot:: inventory-consignment-product-policy
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ Sales tab
   :shows: The "Consignment" group of a product's Sales tab with the "Sale Policy" field (Use default /
      Enabled / Disabled), and the "Consignment Stock" smart button in the button box above.
   :highlight: The "Sale Policy" field and the "Consignment Stock" smart button (red frames).
   :data: A product with Sale Policy "Use default" and stock at one customer's consignment location.
   :module: eyssen_consignment
   :notes: English UI, light theme, 1440px width, crop to the tab and the button box.

Per product, on the product's :guilabel:`Sales` tab, the :guilabel:`Sale Policy` field
(:guilabel:`Use default` / :guilabel:`Enabled` / :guilabel:`Disabled`) overrides the company policy
for that product specifically. The :guilabel:`Consignment Stock` smart button (also available in
the product list and kanban views) opens the quants currently held for that product across every
customer's consignment location.

Access rights are limited to the **Sales / User** group, which can create and edit settlement
reports and their lines but never delete them, preserving the audit trail. An additional admin-only recovery action (restricted to the **Inventory / Administrator**
group) is available on a cancelled report to clear leftover audit data if a cancellation was
interrupted.

Usage
=======

#. **Enable the customer.** On the customer's form, set :guilabel:`Can Buy on Consignment` (the
   company-wide :guilabel:`Customer Consignment Stock Location` must be configured first).
   Optionally enable :guilabel:`Buy on Consignment by Default` so new orders default to consignment.
#. **Sell and deliver.** Create a sale order for the customer — :guilabel:`Consignment Order` is
   pre-checked if configured by default, or can be checked manually. Confirm the order and validate
   the delivery as usual; the goods land at the customer's consignment location, still owned by the
   company.
#. **Settle what was sold.** Periodically, open the customer's :guilabel:`Settlement Report` button
   (or the :guilabel:`Consignment` menu), review the :guilabel:`Cons. Quantity` per product, enter
   the :guilabel:`Settled Quantity` for what the customer reports as sold — row by row, with
   :guilabel:`Set All`/:guilabel:`Set Null`, or via :guilabel:`Add Bulk Products` — and
   :guilabel:`Confirm`. The system invoices the customer and moves that stock off the consignment
   books.
#. **Return what wasn't sold.** Create (or reuse) a :guilabel:`Returns Submission` report the same
   way, enter the quantities being sent back, and :guilabel:`Confirm`. A **Consignment Return** RMA
   is created and auto-approved; validate the resulting incoming receipt once the goods physically
   arrive back at the warehouse.
#. **Reconcile stock.** Use an :guilabel:`Inventory Verification` report at any time to see the raw
   physical quantity currently sitting at the customer's location, without affecting invoicing or
   returns.

Scope and modules
====================

- ``eyssen_consignment`` — the full consignment feature: the per-customer consignment location,
  the consignment flag and warnings on sale orders/quotations and deliveries, the
  :guilabel:`Cons. *` quantity fields on sale order lines, the :guilabel:`Consignment` settlement/
  return/verification reports and their invoicing and RMA integration, the per-product sale policy,
  and the related company settings.

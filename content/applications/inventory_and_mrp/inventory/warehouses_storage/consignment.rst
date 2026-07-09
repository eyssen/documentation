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

.. Screenshot plan:
.. - consignment-partner-form.png: res.partner form, "Sales & Purchase" tab, "Customer Consignment"
..   group with "Can Buy on Consignment" enabled, showing the consignment stock location and stock
..   count, plus the header "Settlement Report" button. Path: Contacts app -> open a customer that
..   already has consignment enabled -> Sales & Purchase tab -> scroll to "Customer Consignment".
.. - consignment-sale-order.png: sale order form with "Consignment Order" checked next to the
..   payment terms, and the order lines list showing the "Cons. Remaining Quantity" column. Path:
..   Sales app -> Orders -> open a confirmed consignment order.
.. - consignment-warning.png: the red "cannot be sold/picked on consignment" alert banner shown
..   above the order lines / picking lines when a product's consignment sale policy is Disabled.
..   Path: Sales app -> Orders -> a consignment quotation that includes a product whose Sale Policy
..   (Sales tab) is set to Disabled.
.. - consignment-delivery-picking.png: the outgoing delivery (stock.picking) form for a consignment
..   order, showing the "Consignment Order" checkbox next to the Owner field. Path: Inventory app ->
..   Transfers -> open the outgoing delivery generated from a consignment sale order.
.. - consignment-menu.png: the Sales -> Orders -> Consignment list view showing settlement-report
..   records with their Draft/Done/Cancelled state badges. Path: Sales app -> Orders -> Consignment.
.. - consignment-settlement-report-form.png: a draft Sales Settlement Report form with the line list
..   (Product, Cons. Quantity, Settled Quantity) and the "Add Bulk Products" / "Set All" / "Set Null"
..   / "Confirm" buttons visible. Path: Consignment menu -> open a draft report of Type "Sales
..   Settlement Report" (or trigger one from a customer's "Settlement Report" button).
.. - consignment-return-report.png: a draft Returns Submission report (Type = "Returns Submission")
..   with settled/return quantities filled in, ready to Confirm. Path: Consignment menu -> New ->
..   set Type to "Returns Submission".
.. - consignment-bulk-product-wizard.png: the "Add Bulk Products" dialog (Format, Based On, example
..   text, paste/CSV/Excel input). Path: on a draft settlement report, click the cubes-icon "Add Bulk
..   Products" button.
.. - consignment-product-policy.png: the product template form, Sales tab, "Consignment" group
..   showing the "Sale Policy" field, and the "Consignment Stock" smart button in the button box.
..   Path: Sales/Inventory app -> Products -> open a product -> Sales tab.
.. - consignment-settings.png: Inventory -> Configuration -> Settings, "Traceability" section,
..   showing "Customer Consignment Stock Location", "Customer Consignment Report Operation Type" and
..   "Consignment Sale Product Policy" fields right below "Set owner on stored products". Path:
..   Inventory app -> Configuration -> Settings.

How consignment stock works
============================

Per-customer consignment location
----------------------------------

.. image:: consignment/consignment-partner-form.png
   :alt: Customer form with Can Buy on Consignment enabled and the consignment stock location

Every consignment customer gets its own dedicated :guilabel:`stock.location`. On the customer's
form (:menuselection:`Contacts --> a customer --> Sales & Purchase tab --> Customer Consignment`),
enabling :guilabel:`Can Buy on Consignment` automatically creates a location flagged as a
**Customer Consignment Place** (usage ``customer``, linked back to the partner) as a child of the
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

.. image:: consignment/consignment-sale-order.png
   :alt: Sale order with the Consignment Order flag and consignment quantity columns

A sale order exposes a :guilabel:`Consignment Order` checkbox next to the payment terms (only
visible if the customer :guilabel:`Can Buy on Consignment`, and pre-checked automatically when the
customer has :guilabel:`Buy on Consignment by Default`). Deliveries generated from a consignment
order automatically inherit the same flag, and a delivery's :guilabel:`Consignment Order` flag can
also be set directly if a picking is created outside the normal sale flow.

.. image:: consignment/consignment-warning.png
   :alt: Warning banner listing products that cannot be sold or picked on consignment

Per-product control — every product can be restricted from consignment sales individually with its
:guilabel:`Sale Policy` (see :ref:`consignment/configuration`). If a consignment order or delivery
contains a product whose policy resolves to :guilabel:`Disabled` — or if the customer is not
allowed to buy on consignment at all — a red warning banner lists the offending products, and
sending the quotation, confirming the order, or validating the delivery is blocked until the issue
is resolved.

.. image:: consignment/consignment-delivery-picking.png
   :alt: Consignment delivery picking with the forced Owner field

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

.. image:: consignment/consignment-menu.png
   :alt: Consignment menu listing settlement reports with Draft, Done and Cancelled states

All settlement, return and verification cycles are handled through the ``consignment.settlement.report``
document, listed under :menuselection:`Sales --> Orders --> Consignment`. Each report has
a sequence reference (``CSR/<year>/#####``), belongs to one customer, and has a :guilabel:`Type`:

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

.. image:: consignment/consignment-settlement-report-form.png
   :alt: Draft settlement report with Cons. Quantity and Settled Quantity per product

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

.. image:: consignment/consignment-bulk-product-wizard.png
   :alt: Add Bulk Products dialog with copy/paste, CSV and Excel import

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

.. image:: consignment/consignment-return-report.png
   :alt: Returns Submission report ready to confirm

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

.. image:: consignment/consignment-settings.png
   :alt: Inventory settings with the three consignment configuration fields

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

.. image:: consignment/consignment-product-policy.png
   :alt: Product Sales tab with the consignment Sale Policy field and stock smart button

Per product, on the product's :guilabel:`Sales` tab, the :guilabel:`Sale Policy` field
(:guilabel:`Use default` / :guilabel:`Enabled` / :guilabel:`Disabled`) overrides the company policy
for that product specifically. The :guilabel:`Consignment Stock` smart button (also available in
the product list and kanban views) opens the quants currently held for that product across every
customer's consignment location.

Access rights are limited to the **Sales / User** group (``sales_team.group_sale_salesman``), which
can create and edit settlement reports and their lines but never delete them, preserving the audit
trail. An additional admin-only recovery action (restricted to the **Inventory / Administrator**
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

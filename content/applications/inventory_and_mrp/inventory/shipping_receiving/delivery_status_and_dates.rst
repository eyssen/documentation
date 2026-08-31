==========================
Delivery status and dates
==========================

Odoo's standard **Sales** app already tracks whether a confirmed order is *Not Delivered*,
*Started*, *Partially Delivered* or *Fully Delivered*, based purely on the state of its linked
delivery orders. In day-to-day operations this is not quite enough: warehouse and sales teams also
need to know *how much* of an order has physically gone out, *when* the last shipment left, and
what to do with a delivery that will never exactly match the ordered quantity (bulk or liquid
goods) or that was cancelled outright. Separately, on Hungarian companies the accounting rules
require an invoice's posting date and its delivery (fulfillment) date to match exactly, which the
standard stock/invoicing integration can silently break on corrective invoices. This page documents
the two eYssen modules that close these gaps.

.. seealso::
   - :doc:`setup_configuration/gls`
   - :doc:`setup_configuration/foxpost`
   - :doc:`setup_configuration/mpl`
   - :doc:`cash_on_delivery`

.. Screenshot plan:
   .. delivery_status_and_dates-order-form-status.png
      A confirmed sales order form (state = "sale") with a partially delivered order, on the
      "Other Info" tab, "Delivery" group. Shows the Delivery Status badge/field, the Delivery %
      progress bar and the Last Delivery Date field together.
      Click path: Sales --> Orders --> open a confirmed order that has been partially delivered
      --> Other Info tab.
   .. delivery_status_and_dates-force-full-delivery-button.png
      The same order form, zoomed on the header, showing the "Fully Delivered" button next to the
      status bar (order not yet fully/cancelled delivered).
      Click path: Sales --> Orders --> open a confirmed, not-fully-delivered order --> header.
   .. delivery_status_and_dates-reset-button.png
      An order where "Fully Delivered" has already been forced, showing the "Reset Delivery
      Status" header button and the chatter message logged by the override.
      Click path: same order as above, after clicking "Fully Delivered" --> header + chatter.
   .. delivery_status_and_dates-order-list-badges.png
      The Sales --> Orders list view with the Delivery Status column showing colored badges
      (green/orange/blue/red) and the Delivery % and Last Delivery Date optional columns enabled
      via the column-picker.
      Click path: Sales --> Orders --> click the column-picker (sliders icon) at the top-right of
      the list and enable "Delivery %" and "Last Delivery Date".
   .. delivery_status_and_dates-search-filters.png
      The search panel's Filters dropdown open on the Orders list, showing "Not Delivered",
      "Delivery Started", "Partially Delivered", "Fully Delivered", "Delivery Cancelled" and the
      "Group By: Delivery Status" option.
      Click path: Sales --> Orders --> click into the search bar --> Filters tab.
   .. delivery_status_and_dates-dashboard-list.png
      The "Delivery Status" reporting list view, showing Order, Partner, Order Date, Commitment
      Date, Expected, First Delivery, Last Delivery, Delivery Status badge, Delivery % bar and
      Total columns.
      Click path: Sales --> Reporting --> Delivery Status.
   .. delivery_status_and_dates-dashboard-pivot.png
      The same reporting action switched to the Pivot view, delivery status as columns and order
      month as rows, with Delivery % and Total as measures.
      Click path: Sales --> Reporting --> Delivery Status --> Pivot view button.
   .. delivery_status_and_dates-invoice-delivery-date.png
      A Hungarian customer invoice form, "Other Info" tab, showing the Delivery Date field next to
      the accounting Date field, both holding the same value; ideally a corrective invoice so the
      "Origin/Corrected invoice" link is also visible.
      Click path: Accounting --> Customers --> Invoices --> open a HU corrective invoice --> Other
      Info tab.

Delivery status on the sales order
===================================

.. image:: delivery_status_and_dates/delivery_status_and_dates-order-form-status.png
   :alt: Sales order form showing the Delivery Status, Delivery % and Last Delivery Date fields

On a confirmed order, the :guilabel:`Delivery` group of the :guilabel:`Other Info` tab shows three
complementary indicators, right after the standard :guilabel:`Delivery Status` field:

- :guilabel:`Delivery %` — the percentage of the ordered quantity that has actually been delivered,
  computed from ``qty_delivered`` versus ``product_uom_qty`` across all order lines whose product is
  **not** a service. It is only shown while the order is confirmed.
- :guilabel:`Last Delivery Date` — the completion date/time of the most recent **done**, **outgoing**
  delivery linked to the order (``picking_ids`` filtered on ``state == 'done'`` and
  ``picking_type_code == 'outgoing'``). It only reflects deliveries that already left the warehouse —
  not the *first* delivery (that is the standard ``effective_date`` field, still shown separately).

Both fields are stored and recompute automatically whenever the order lines or its transfers change,
so they can be used directly in filters, groupings and the reporting dashboard described below.

Cancelled deliveries
---------------------

The standard :guilabel:`Delivery Status` field only distinguishes *Not Delivered*, *Started*,
*Partially Delivered* and *Fully Delivered* — a fully cancelled order still shows as *Not Delivered*.
This module adds a fifth value, :guilabel:`Cancelled`: whenever an order has at least one delivery
and **every** one of its transfers is in the :guilabel:`Cancelled` state, the order's delivery status
is shown as :guilabel:`Cancelled` instead.

.. note::
   The field's built-in help text ("Blue: Not Delivered/Started, Orange: Partially Delivered, Green:
   Fully Delivered") is Odoo's own and is not extended for the new state. In the list and Kanban
   views added by this module, :guilabel:`Cancelled` is shown with a red (danger) color to keep it
   visually distinct from the other three.

Manual "Fully Delivered" override
==================================

.. image:: delivery_status_and_dates/delivery_status_and_dates-force-full-delivery-button.png
   :alt: Confirmed order header with the "Fully Delivered" override button

For bulk or liquid goods, the delivered quantity almost never matches the ordered quantity to the
last decimal, so the computed status stays :guilabel:`Partially Delivered` forever even though the
delivery is, for all practical purposes, complete. The :guilabel:`Fully Delivered` header button lets
a user override this manually on a confirmed order:

#. Click :guilabel:`Fully Delivered` in the order's header. This sets the technical
   :guilabel:`Forced Fully Delivered` flag (``force_full_delivery``) and immediately recomputes the
   delivery status to :guilabel:`Fully Delivered`, regardless of the actual delivered quantities. A
   chatter message records that the status was manually forced.
#. The button is only available on confirmed orders whose current status is not already
   :guilabel:`Fully Delivered` or :guilabel:`Cancelled`, and disappears once the override is active.
#. A :guilabel:`Reset Delivery Status` button then appears in its place. Clicking it clears the
   override and lets the status recompute from the real delivered quantities again, also logging a
   chatter message.

.. image:: delivery_status_and_dates/delivery_status_and_dates-reset-button.png
   :alt: Order header after the override, showing the Reset Delivery Status button

.. important::
   The override never touches stock: no picking, move or backorder is created, cancelled or
   validated by either button. It only changes what the :guilabel:`Delivery Status` field reports. A
   :guilabel:`Cancelled` order always takes priority over the override — if every delivery on the
   order is cancelled, the status shows :guilabel:`Cancelled` even while
   :guilabel:`Forced Fully Delivered` is set.

Delivery status in list and search views
=========================================

.. image:: delivery_status_and_dates/delivery_status_and_dates-order-list-badges.png
   :alt: Orders list view with color-coded Delivery Status badges and optional columns

The :guilabel:`Delivery Status` column is enabled by default (colored badge: green for
:guilabel:`Fully Delivered`, orange for :guilabel:`Partially Delivered`, blue for :guilabel:`Not
Delivered`/:guilabel:`Started`, red for :guilabel:`Cancelled`) on both the
:menuselection:`Sales --> Orders` list and the :guilabel:`Quotations` list. :guilabel:`Delivery %`
and :guilabel:`Last Delivery Date` are added to both lists as optional (hidden by default) columns,
toggled from the column-picker.

.. image:: delivery_status_and_dates/delivery_status_and_dates-search-filters.png
   :alt: Search panel Filters showing the five delivery-status filters and the Group By option

The order search panel gains one filter per delivery status — :guilabel:`Not Delivered`,
:guilabel:`Delivery Started`, :guilabel:`Partially Delivered`, :guilabel:`Fully Delivered` and
:guilabel:`Delivery Cancelled` — plus a :guilabel:`Last Delivery Date` date filter and a
:guilabel:`Group By: Delivery Status` option.

Delivery-status dashboard
==========================

.. image:: delivery_status_and_dates/delivery_status_and_dates-dashboard-list.png
   :alt: Delivery Status reporting list view

A dedicated reporting menu, :menuselection:`Sales --> Reporting --> Delivery Status`, gives a
cross-order view limited to confirmed orders (``state = 'sale'``). Its list view combines the order
reference, customer, order date, :guilabel:`Commitment Date`, :guilabel:`Expected` date
(``expected_date``), :guilabel:`First Delivery` (the standard ``effective_date``),
:guilabel:`Last Delivery` (``last_delivery_date``), the :guilabel:`Delivery Status` badge, the
:guilabel:`Delivery %` progress bar, the order total and the salesperson.

.. image:: delivery_status_and_dates/delivery_status_and_dates-dashboard-pivot.png
   :alt: Delivery Status reporting pivot view

The same action also offers :guilabel:`Pivot` and :guilabel:`Graph` views: the pivot breaks down
:guilabel:`Delivery %` and the order total by delivery status (columns) and order month (rows); the
graph shows total order value per delivery status as a bar chart.

Actual customer receipt date
=============================

Beyond the sales order, this module also adds an :guilabel:`Actual Customer Receipt Date`
(``delivered_date``) field on the delivery (:guilabel:`stock.picking`) itself. It is a technical,
read-only field, not exposed on any view by this module — it exists to record the moment the
consumer actually took delivery of the goods (as reported by carrier tracking), which can be
noticeably later than ``date_done`` (when the warehouse validated the transfer and handed it to the
carrier).

The field is populated through the idempotent ``_set_delivered()`` hook, which:

- only applies to **outgoing** transfers whose destination location is a customer location;
- silently ignores an empty/falsy timestamp; and
- never overwrites an existing value — the first confirmed receipt is authoritative, later calls
  with a different timestamp are no-ops.

.. note::
   ``eyssen_sale_delivery_status`` only defines the field and this hook; it is the carrier-tracking
   integrations (e.g. the :doc:`GLS <setup_configuration/gls>`,
   :doc:`Foxpost <setup_configuration/foxpost>` and :doc:`MPL <setup_configuration/mpl>` delivery
   methods) that call ``_set_delivered()`` once they detect an actual-delivery tracking event, and
   other eYssen modules (such as the RMA return-window logic) that read the resulting date. Consult
   those modules' own documentation for details.

Hungarian invoice fulfillment-date consistency
================================================

.. image:: delivery_status_and_dates/delivery_status_and_dates-invoice-delivery-date.png
   :alt: Hungarian customer invoice showing the Delivery Date field aligned with the Date field

Odoo's core accounting keeps a :guilabel:`Delivery Date` field (``delivery_date``) on every invoice.
When the **Inventory** app is installed, ``sale_stock`` automatically syncs that field to the linked
sale order's :guilabel:`Effective Date` (the completion date of its first delivery) every time the
invoice is recomputed. Separately, ``eyssen_l10n_hu`` enforces a Hungarian NAV requirement on
posting: for a Hungarian company, an invoice's accounting :guilabel:`Date` and its
:guilabel:`Delivery Date` must be identical, or :guilabel:`Post` refuses with *"The Accounting Date
is not the same as the Fulfillment Date!"*. To satisfy this, corrective invoices and credit notes
are made to inherit both dates directly from the original invoice they correct or reverse.

The problem this module solves is a compute-ordering one: because ``sale_stock``'s own
:guilabel:`Delivery Date` recompute always tries to re-stamp the field from the sale order's
effective date, that logic can run *after* ``eyssen_l10n_hu``'s "inherit from the original invoice"
logic depending on the exact combination of installed apps — silently pulling a corrective invoice's
delivery date away from the original invoice's date again, and breaking the accounting-date /
delivery-date match at :guilabel:`Post` time.

``eyssen_l10n_hu_sale_stock_delivery_date`` is a small, dependency-only module (it adds no views,
menus or new fields) that depends on **both** ``sale_stock`` and ``eyssen_l10n_hu``. Depending on
both guarantees its ``account.move._compute_delivery_date()`` override runs after ``sale_stock``'s,
so the corrective-invoice logic always has the final say:

- moves that are already :guilabel:`Posted` are left untouched (recomputing ``delivery_date`` on a
  posted, already-hashed entry must never happen);
- on any other move, if it has a :guilabel:`Corrected Invoice` or is a reversal
  (``reversed_entry_id``), both :guilabel:`Delivery Date` and :guilabel:`Date` are forced to the
  original invoice's delivery date, undoing any stock-driven re-sync; and
- as a general safety net, if :guilabel:`Delivery Date` and :guilabel:`Date` still disagree afterward,
  :guilabel:`Date` is aligned to :guilabel:`Delivery Date` (or vice-versa if :guilabel:`Delivery
  Date` is empty).

.. important::
   This logic is intentionally duplicated, line for line, between ``eyssen_l10n_hu`` and
   ``eyssen_l10n_hu_sale_stock_delivery_date`` — the module's own code comments say so explicitly.
   If this behavior is ever changed, both modules must be updated together, or a Hungarian company
   with both ``sale_stock`` and ``eyssen_l10n_hu`` installed but this module missing can end up with
   the exact desync it was written to prevent.

Configuration
=============

Both modules are ordinary Odoo apps, installed from :menuselection:`Apps`; neither has a
:guilabel:`Settings` toggle.

- **Sale Delivery Status** (``eyssen_sale_delivery_status``) depends on ``sale_management``,
  ``stock`` and ``sale_stock``. Installing it is enough to get the extra fields, list/search
  additions and the reporting menu — there is nothing further to configure.
- **eYssen Sale Stock Delivery Date** (``eyssen_l10n_hu_sale_stock_delivery_date``) depends on
  ``sale_stock`` and ``eyssen_l10n_hu``, and is **not** auto-installed and not required by any other
  eYssen module. Install it explicitly on any Hungarian company (``eyssen_l10n_hu`` installed) that
  also uses stock-driven sales invoicing (``sale_stock``) — otherwise corrective invoices on that
  database remain exposed to the fulfillment-date desync described above.

.. tip::
   The :guilabel:`Fully Delivered` and :guilabel:`Reset Delivery Status` buttons and the delivery
   fields on the order form require no security group beyond ordinary access to Sales orders — there
   is no dedicated permission for this feature.

Usage
=====

#. Confirm a sales order with a delivery route as usual. As transfers are validated, the standard
   :guilabel:`Delivery Status`, plus this module's :guilabel:`Delivery %` and :guilabel:`Last
   Delivery Date`, update automatically on the order's :guilabel:`Other Info` tab.
#. If every delivery on the order ends up cancelled, the status switches to :guilabel:`Cancelled`
   instead of staying at :guilabel:`Not Delivered`.
#. For bulk/liquid goods that will never reach exactly 100%, click :guilabel:`Fully Delivered` in the
   header once the shipment is effectively complete; click :guilabel:`Reset Delivery Status` later if
   the override needs to be undone.
#. Use the :guilabel:`Filters` and :guilabel:`Group By: Delivery Status` options on
   :menuselection:`Sales --> Orders`, or the dedicated :menuselection:`Sales --> Reporting -->
   Delivery Status` dashboard, to review delivery progress across orders.
#. On Hungarian companies with both modules installed, correcting or reversing an invoice keeps its
   :guilabel:`Delivery Date` and :guilabel:`Date` aligned with the original invoice automatically —
   no manual date entry is needed on the corrective invoice itself.

Delivery status on the customer portal
=======================================

The delivery indicators described above live on the sales order form, lists and reporting dashboard
— back-office screens a webshop customer never sees. The small companion module
``sale_delivery_status_ws`` publishes the same indicators on the website customer portal, so
logged-in customers can follow the progress of their own deliveries themselves instead of asking
support. It is a pure display module: it adds no settings, menus or new fields — installing it from
:menuselection:`Apps` is the on/off switch — and it requires ``eyssen_sale_delivery_status`` (whose
fields it displays), ``sale_stock`` and the **Website** app. It is not installed automatically;
enable it explicitly
on any database whose webshop customers should see delivery progress.

Orders list
------------

When a customer signs in on the website and opens :menuselection:`My Account --> Your Orders`, the
order list gains two extra columns after :guilabel:`Total`:

- :guilabel:`Delivery Status` — a colored pill badge per order. The portal deliberately uses
  shorter, customer-friendly wording than the backend delivery-status labels:

  .. list-table::
     :header-rows: 1
     :widths: 40 30 30

     * - Backend delivery status
       - Portal badge
       - Badge color
     * - :guilabel:`Fully Delivered`
       - :guilabel:`Delivered`
       - Green
     * - :guilabel:`Partially Delivered`
       - :guilabel:`Partial`
       - Yellow
     * - :guilabel:`Started`
       - :guilabel:`Started`
       - Blue
     * - :guilabel:`Not Delivered`
       - :guilabel:`Pending`
       - Grey
     * - :guilabel:`Cancelled`
       - :guilabel:`Cancelled`
       - Red

- :guilabel:`Delivery %` — the order's delivery percentage, rounded down to a whole number
  (currently rendered with a doubled percent sign, e.g. *42%%*, due to a template quirk — see the
  note under :ref:`the order detail page <delivery_status_and_dates/portal_detail_page>`). It is
  only shown for orders that have a delivery status at all.

.. note::
   Both columns are hidden on narrow (phone-width) screens, the same way standard portal lists (for
   example, the invoices list) already trim secondary columns to stay readable.

.. _delivery_status_and_dates/portal_detail_page:

Order detail page
------------------

Opening an order from that list, the :guilabel:`Sale Information` table of the order's portal page
gains up to three extra rows:

- :guilabel:`Delivery Status:` — the same colored badge as in the orders list;
- :guilabel:`Delivered:` — a green progress bar labelled with the order's delivery percentage;
- :guilabel:`Last Delivery:` — the date (without time of day) of the most recent completed delivery.

.. note::
   In the current version of the module, the percentage is rendered with a doubled percent sign
   (e.g. *42%%*) — both in the orders list's :guilabel:`Delivery %` column and in this bar's label
   and width. Because ``42%%`` is not a valid CSS width, the bar does not visually fill to the
   delivery percentage until this template quirk is fixed.

Each row only appears once its underlying value is set: a quotation, or a confirmed order without
any delivery order yet, shows none of them, and the progress-bar row stays hidden while the
delivered percentage is still zero.

Because the values come straight from the fields maintained by ``eyssen_sale_delivery_status``, the
portal always agrees with the back office — portal wording aside. An order manually forced with
:guilabel:`Fully Delivered` shows the green :guilabel:`Delivered` badge to the customer, and an
order whose every delivery was cancelled shows the red :guilabel:`Cancelled` badge.

Scope and modules
==================

- ``eyssen_sale_delivery_status`` — adds the :guilabel:`Delivery %`, :guilabel:`Last Delivery Date`
  and :guilabel:`Cancelled` delivery status to sale orders, the manual :guilabel:`Fully Delivered`
  override, the delivery-status search filters and list columns, the
  :menuselection:`Sales --> Reporting --> Delivery Status` dashboard, and the
  :guilabel:`Actual Customer Receipt Date` field on deliveries.
- ``eyssen_l10n_hu_sale_stock_delivery_date`` — keeps a Hungarian corrective/reversal invoice's
  :guilabel:`Delivery Date` (fulfillment date) aligned with its original invoice, independent of the
  sale order's stock-driven effective date, so the NAV accounting-date/delivery-date rule enforced by
  ``eyssen_l10n_hu`` keeps holding at :guilabel:`Post` time.
- ``sale_delivery_status_ws`` — shows the delivery status (in customer-friendly wording) and the
  delivery percentage to logged-in customers on both the website portal's :guilabel:`Your Orders`
  list and the order's own portal page, and additionally the last delivery date on the order's own
  portal page only.

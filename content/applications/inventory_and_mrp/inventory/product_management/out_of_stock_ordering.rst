=====================
Out-of-stock ordering
=====================

By default, Odoo prevents customers and sales teams from being fully aware of stock shortages only
through the *forecasted* quantity shown on a product. The **Sale Out of Stock Ordering** feature adds
an explicit, three-state stock status — :guilabel:`Order`, :guilabel:`Preorder` and
:guilabel:`Backorder` — to every storable product, and lets a company decide, per product and
company-wide, whether preorder and backorder sales are allowed at all. Sales orders that violate the
policy are flagged with an on-screen warning and are blocked from being sent or confirmed until the
issue is resolved.

.. Screenshot plan:
   .. out_of_stock_ordering-settings.png — Settings > General Settings, eYssen ERP app tab, "Sale"
      section, with the "Sale Out of Stock Ordering (Preorder, Backorder)" checkbox enabled and the
      resulting "Out of Stock Mode", "Preorder Default Policy", "Backorder Default Policy",
      "Preorder Mixed Policy" and "Backorder Mixed Policy" fields visible.
      Click path: Settings --> General Settings --> eYssen ERP tab --> Sale section.
   .. out_of_stock_ordering-product-status-auto.png — Storable product form, General Information tab,
      "Sale Out of Stock" section, with "Out of Stock Mode" set to Auto: shows the read-only
      "Sale Stock Status" badge (e.g. red Backorder) plus the "Preorder Policy" and "Backorder Policy"
      selection fields.
      Click path: Sales --> Products --> Products --> open a storable product.
   .. out_of_stock_ordering-product-status-manual.png — Same product form and section, but with
      "Out of Stock Mode" set to Manual: shows the editable, colored "Sale Stock Status" selection
      field instead of the computed badge.
      Click path: Settings --> General Settings, switch "Out of Stock Mode" to Manual and save, then
      reopen the product from Sales --> Products --> Products.
   .. out_of_stock_ordering-bulk-update.png — Products list view with several storable products
      selected, "Actions" (gear icon) menu open on "Bulk Update", showing the "Sale Out of Stock
      Status" field in the wizard (Manual mode).
      Click path: Sales --> Products --> Products --> select several products --> Actions --> Bulk
      Update.
   .. out_of_stock_ordering-order-warning.png — Quotation form with a red warning banner above the
      order lines listing which products cannot be sold as Preorder/Backorder, plus the colored
      "Sale Stock Status" badge column next to the Quantity column in the order lines list.
      Click path: Sales --> Orders --> New --> add a customer and an out-of-stock product whose
      Preorder or Backorder Policy is Disabled.
   .. out_of_stock_ordering-confirm-blocked.png — Error dialog shown after clicking Confirm on the
      quotation from the previous screenshot, displaying the "You cannot confirm this sale order due
      to out of stock status." message.
      Click path: on the quotation from the previous shot, click Confirm.

How stock status is determined
===============================

.. image:: out_of_stock_ordering/out_of_stock_ordering-product-status-auto.png
   :alt: Sale Out of Stock section on a storable product's form, in Auto mode

Every **storable** product (the *Track Inventory* product type) gets a :guilabel:`Sale Stock Status`
of :guilabel:`Order`, :guilabel:`Preorder` or :guilabel:`Backorder`. Products that are not storable
(services, non-tracked consumables) are never classified — the feature does not apply to them.

The status is calculated **live**, from the product's current forecasted quantity — it is not stored
and always reflects the latest stock position. How it is calculated depends on the company-wide
:guilabel:`Out of Stock Mode`, set in :ref:`Configuration <out-of-stock-ordering/configuration>`:

- **Auto** (the default): the status is derived automatically:

  - **forecasted quantity above zero** → :guilabel:`Order` — the product is in stock and sells
    normally;
  - **forecasted quantity at or below zero, and the product already has stock moves** →
    :guilabel:`Backorder` — a known product that is temporarily depleted;
  - **forecasted quantity at or below zero, and the product has never had any stock move** →
    :guilabel:`Preorder` — a new product that has not been received into stock yet.

- **Manual**: the automatic calculation is skipped. Each product exposes an editable
  :guilabel:`Sale Stock Status` field (:guilabel:`Order`, :guilabel:`Preorder` or
  :guilabel:`Backorder`) that a user sets directly, defaulting to :guilabel:`Order`.

.. image:: out_of_stock_ordering/out_of_stock_ordering-product-status-manual.png
   :alt: Sale Out of Stock section on a storable product's form, in Manual mode

.. note::
   :guilabel:`Out of Stock Mode` is a single, company-wide switch. It cannot be set per product —
   changing it changes how the :guilabel:`Sale Stock Status` badge behaves for **every** storable
   product at once.

Preorder and backorder policies
================================

Being classified as :guilabel:`Preorder` or :guilabel:`Backorder` does not, by itself, stop a product
from being sold. Whether it *may* be sold in that state is governed by a separate set of policies,
checked at the sales-order level:

- **Per-product policy.** Every product has a :guilabel:`Preorder Policy` and a :guilabel:`Backorder
  Policy`, each set to :guilabel:`Use default`, :guilabel:`Enabled` or :guilabel:`Disabled`.
  :guilabel:`Use default` falls back to the company-wide default below.
- **Company default policy.** :guilabel:`Preorder Default Policy` and :guilabel:`Backorder Default
  Policy` (:guilabel:`Enabled` or :guilabel:`Disabled`, both :guilabel:`Enabled` out of the box) apply
  to every product left on :guilabel:`Use default`.
- **Mixed-order policy.** :guilabel:`Preorder Mixed Policy` and :guilabel:`Backorder Mixed Policy`
  (:guilabel:`Allowed` or :guilabel:`Not Allowed`, both :guilabel:`Not Allowed` out of the box) decide
  whether a single sales order may combine an in-stock (:guilabel:`Order`) line with a preorder line,
  or an in-stock line with a backorder line, respectively.

.. important::
   The mixed-order check only looks at :guilabel:`Order` lines combined with :guilabel:`Preorder` or
   :guilabel:`Backorder` lines. Combining a :guilabel:`Preorder` line with a :guilabel:`Backorder`
   line on the same order is not restricted by this policy.

When a sales order line's product policy resolves to :guilabel:`Disabled`, or the order mixes
statuses in a way the mixed policy forbids, the order is flagged as described in
:ref:`Usage <out-of-stock-ordering/usage>`.

.. _out-of-stock-ordering/configuration:

Configuration
==============

.. image:: out_of_stock_ordering/out_of_stock_ordering-settings.png
   :alt: Sale Out of Stock Ordering settings section

#. Go to :menuselection:`Settings --> General Settings`, open the :guilabel:`eYssen ERP` app tab, and
   enable :guilabel:`Sale Out of Stock Ordering (Preorder, Backorder)` in the :guilabel:`Sale`
   section.
#. Set the company-wide :guilabel:`Out of Stock Mode` (:guilabel:`Auto` or :guilabel:`Manual`).
#. Set the default policies: :guilabel:`Preorder Default Policy`, :guilabel:`Backorder Default
   Policy`, :guilabel:`Preorder Mixed Policy` and :guilabel:`Backorder Mixed Policy`.
#. Save.

Once enabled, every storable product's form (:menuselection:`Sales --> Products --> Products`,
:guilabel:`General Information` tab) gains a :guilabel:`Sale Out of Stock` section with the
:guilabel:`Sale Stock Status` field (badge or editable selection, depending on the mode) and the
per-product :guilabel:`Preorder Policy` / :guilabel:`Backorder Policy` overrides.

.. tip::
   To set the manual :guilabel:`Sale Stock Status` on several products at once (when :guilabel:`Out
   of Stock Mode` is :guilabel:`Manual`), select the products in :menuselection:`Sales --> Products
   --> Products`, open :menuselection:`Actions --> Bulk Update`, and set :guilabel:`Sale Out of Stock
   Status` in the wizard before clicking :guilabel:`Update`.

   .. image:: out_of_stock_ordering/out_of_stock_ordering-bulk-update.png
      :alt: Bulk Update wizard with the Sale Out of Stock Status field

.. _out-of-stock-ordering/usage:

Usage
======

.. image:: out_of_stock_ordering/out_of_stock_ordering-order-warning.png
   :alt: Quotation with an out-of-stock policy warning above the order lines

On a sales order, each order line displays its product's :guilabel:`Sale Stock Status` as a colored
badge next to the :guilabel:`Quantity` column (green for :guilabel:`Order`, orange for
:guilabel:`Preorder`, red for :guilabel:`Backorder`).

If any line violates the preorder/backorder or mixed-order policy, a red warning banner appears above
the order lines, listing the specific products that cannot be sold as :guilabel:`Preorder` or
:guilabel:`Backorder`, and/or stating that mixing in-stock and preorder (or backorder) products is not
allowed by company policy.

While that warning is present:

- the :guilabel:`Send` action (quotation e-mail) is blocked; and
- the :guilabel:`Confirm` action is blocked,

both raising a validation error until the order lines no longer violate the policy — for example by
removing the offending line, changing its quantity, or adjusting the product's policy.

.. image:: out_of_stock_ordering/out_of_stock_ordering-confirm-blocked.png
   :alt: Validation error raised when confirming an order with a policy violation

.. note::
   The warning and the block are purely advisory controls on the sales flow — they do not change
   stock reservation, delivery routing or invoicing. A :guilabel:`Backorder` or :guilabel:`Preorder`
   line that passes the policy check is sold and delivered exactly like any other order line, once
   the corresponding stock becomes available.

Scope and modules
==================

- ``eyssen_sale_out_of_stock`` — the :guilabel:`Sale Stock Status` classification (auto/manual), the
  per-product and company-wide preorder/backorder policies, the mixed-order check, the order-line
  status badge, and the send/confirm blocking on sales orders.

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

How stock status is determined
===============================

.. screenshot:: inventory-out-of-stock-product-auto
   :menu: Inventory ‣ Products ‣ Products ‣ (a storable product) ‣ General Information tab
   :shows: The "Sale Out of Stock" section of a product form in Auto mode: the read-only "Sale Stock Status"
      badge (red "Backorder") next to the "Preorder Policy" and "Backorder Policy" selection fields.
   :highlight: The "Sale Stock Status" badge (red frame).
   :data: A storable product with a forecasted quantity of -3 and earlier stock moves, so the status is
      Backorder.
   :module: eyssen_sale_out_of_stock
   :notes: English UI, light theme, 1440px width, crop to the section; the badge colour must be visible.

Every **storable** product (:guilabel:`Goods` with :guilabel:`Track Inventory` enabled) gets a :guilabel:`Sale Stock Status`
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

.. screenshot:: inventory-out-of-stock-product-manual
   :menu: Inventory ‣ Products ‣ Products ‣ (a storable product) ‣ General Information tab
   :shows: The same "Sale Out of Stock" section with the company-wide "Out of Stock Mode" set to Manual, so
      "Sale Stock Status" is an editable, coloured selection field instead of a computed badge.
   :highlight: The editable "Sale Stock Status" field (red frame).
   :data: The same product with the manual status set to "Preorder".
   :module: eyssen_sale_out_of_stock
   :notes: English UI, light theme, 1440px width, crop to the section.

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

.. screenshot:: inventory-out-of-stock-settings
   :menu: Settings ‣ General Settings ‣ eYssen ERP ‣ Sale
   :shows: The "Sale" section of the eYssen ERP settings with "Sale Out of Stock Ordering (Preorder,
      Backorder)" enabled and the "Out of Stock Mode", "Preorder Default Policy", "Backorder Default
      Policy", "Preorder Mixed Policy" and "Backorder Mixed Policy" fields visible below it.
   :highlight: The five policy fields (red frame).
   :data: Mode Auto; both default policies Enabled; both mixed policies Not Allowed.
   :module: eyssen_sale_out_of_stock
   :notes: English UI, light theme, 1440px width, crop to the setting block.

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

   .. screenshot:: inventory-out-of-stock-bulk-update
      :menu: Inventory ‣ Products ‣ Products ‣ (select several) ‣ Actions ‣ Bulk Update
      :shows: The "Bulk Update" wizard with the "Sale Out of Stock Status" field set, ready to apply to the
         selected products.
      :highlight: The "Sale Out of Stock Status" field (red frame).
      :data: Four selected storable products; status set to "Preorder"; Out of Stock Mode is Manual.
      :module: eyssen_sale_out_of_stock, eyssen_product_bulk_update
      :notes: English UI, light theme, 1440px width, crop to the wizard.

.. _out-of-stock-ordering/usage:

Usage
======

.. screenshot:: inventory-out-of-stock-order-warning
   :menu: Sales ‣ Orders ‣ Quotations ‣ New
   :shows: A quotation with a red warning banner above the order lines naming the products that cannot be
      sold as Preorder or Backorder, and the coloured "Sale Stock Status" badge column next to the Quantity
      column.
   :highlight: The warning banner and the "Sale Stock Status" column (red frames).
   :data: Two lines: one in-stock product (green Order) and one backordered product whose Backorder Policy
      is Disabled.
   :module: eyssen_sale_out_of_stock
   :notes: English UI, light theme, 1440px width, crop to the banner and the order lines; the badge colours
      must be visible.

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

.. screenshot:: inventory-out-of-stock-confirm-blocked
   :menu: Sales ‣ Orders ‣ Quotations ‣ (the same quotation) ‣ Confirm
   :shows: The validation error shown when confirming the order: "You cannot confirm this sale order due to
      out of stock status."
   :highlight: The error text (red frame).
   :data: The quotation from the previous screenshot.
   :module: eyssen_sale_out_of_stock
   :notes: English UI, light theme, 1440px width, crop to the error dialog.

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

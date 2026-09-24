=============================
Stock productivity helpers
=============================

Preparing a stock transfer by hand — adding products one by one, retyping a list from a supplier
e-mail, checking totals, filing it under an internal work order or browsing the product catalog —
is repetitive and error-prone on transfers with many lines. eYssen ships a small set of independent
productivity helpers that attach directly to the :guilabel:`Transfer` (``stock.picking``) form to
speed up exactly these steps. Each helper is a separate, single-purpose module, so a warehouse can
install only the ones it needs.

Key features
============

- **Reuse a previous transfer's product lines** on a new transfer instead of re-entering them.
- **Bulk-add products** to a transfer by pasting a list, or uploading a CSV or Excel file.
- **See the total quantity** of a transfer, per unit of measure, both on the form and in the list
  view.
- **Link a transfer to an internal process number** to group related transfers under one
  reference.
- **Add products to a transfer from the product catalog**, the same kanban-based picker used
  elsewhere in Odoo for sales and purchase orders.
- **Scan a product barcode** to add it to a draft transfer.
- **See the analytic distribution** of each operation line, and find the transfer behind an
  analytic entry.

Configuration
=============

These helpers require no settings screen. Once the relevant module is installed, its button,
field or column appears automatically on the standard :guilabel:`Transfer` form and/or the
:guilabel:`Transfers` list view (:menuselection:`Inventory --> Transfers`). Every module builds on
top of the eYssen :guilabel:`Inventory` layer (``eyssen_stock`` and/or ``eyssen_base``); the
process-number helper additionally requires the ``process_number`` module, which defines the
shared :guilabel:`Process Number` record.

.. note::
   The bulk-add-products wizard reads Excel files with the ``openpyxl`` Python library, listed in
   the module's ``requirements.txt``. Make sure it is available in the Odoo environment before
   using the Excel import format.

Usage
=====

Add items from a previous transfer
-----------------------------------

.. screenshot:: inventory-stock-helpers-previous-items-button
   :menu: Inventory ‣ Transfers ‣ (a draft transfer) ‣ Operations tab
   :shows: A draft transfer form with the "Add Previous Items" button (files icon) at the top-right of the
      operations block.
   :highlight: The "Add Previous Items" button (red frame).
   :data: Draft transfer WH/INT/00001 with no lines yet.
   :module: eyssen_add_item_from_previous_stock
   :notes: English UI, light theme, 1440px width, crop to the operations block header.

On a transfer that is still in the :guilabel:`Draft` state, the :guilabel:`Add Previous Items`
button (files icon, top-right of the operations block) opens a popup where you pick a
:guilabel:`Previous Stock` transfer to copy lines from. Only transfers other than the current one
can be selected, and the picker searches by both the transfer's :guilabel:`Reference` and its
source document (:guilabel:`Origin`).

.. screenshot:: inventory-stock-helpers-previous-items-wizard
   :menu: Inventory ‣ Transfers ‣ (a draft transfer) ‣ Add Previous Items
   :shows: The "Add Previous Items" pop-up with the "Previous Stock" field set to another transfer and the
      "If Product Duplication" field showing its four choices (Stop, Skip, Replace, Increase).
   :highlight: The "Previous Stock" and "If Product Duplication" fields (red frame).
   :data: Source transfer WH/INT/00001, duplication behaviour "Increase".
   :module: eyssen_add_item_from_previous_stock
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

Every product line from the selected transfer is copied over, together with its quantity and unit
price. The :guilabel:`If Product Duplication` field controls what happens when a product from the
source transfer is already present on the current one:

- :guilabel:`Stop` — raise an error and add nothing;
- :guilabel:`Skip` — leave the existing line untouched and move to the next product;
- :guilabel:`Replace` — overwrite the existing line's quantity and unit price with the source
  values; or
- :guilabel:`Increase` (default) — add the source quantity on top of the existing quantity, and
  overwrite the unit price.

New lines are created on the destination location of the current transfer's operation type.

Bulk-add products to a transfer
--------------------------------

.. screenshot:: inventory-stock-helpers-bulk-add-button
   :menu: Inventory ‣ Transfers ‣ (a draft transfer) ‣ Operations tab
   :shows: A draft transfer form showing the "Add Bulk Products" button (cubes icon) next to the "Add
      Previous Items" button.
   :highlight: The "Add Bulk Products" button (red frame).
   :data: Draft transfer WH/INT/00002.
   :module: eyssen_product_bulk_add_stock
   :notes: English UI, light theme, 1440px width, crop to the operations block header.

The :guilabel:`Add Bulk Products` button (cubes icon), shown next to :guilabel:`Add Previous
Items` on a draft transfer, opens a wizard for entering many products at once without touching a
previous transfer.

.. screenshot:: inventory-stock-helpers-bulk-add-paste
   :menu: Inventory ‣ Transfers ‣ (a draft transfer) ‣ Add Bulk Products
   :shows: The "Add Bulk Products" wizard with Format "Copy/Paste", Based On "Default Code", "With Quantity"
      ticked, the live Example block and the multi-line paste box filled with three lines.
   :highlight: The "Format", "Based On" and "With Quantity" fields (red frame).
   :data: Three pasted lines of internal reference plus quantity.
   :module: eyssen_product_bulk_add_stock
   :notes: English UI, light theme, 1440px width, crop to the wizard.

Three input :guilabel:`Format` options are available:

- :guilabel:`Copy/Paste` — one product per line in a plain-text box;
- :guilabel:`CSV` — an uploaded, semicolon-separated CSV file, with an optional header row toggled
  with :guilabel:`Is there a header?`; or
- :guilabel:`Excel` — an uploaded ``.xlsx`` workbook (first sheet), also with the optional header
  toggle.

.. screenshot:: inventory-stock-helpers-bulk-add-csv
   :menu: Inventory ‣ Transfers ‣ (a draft transfer) ‣ Add Bulk Products
   :shows: The same wizard with Format switched to "CSV", showing the "Is there a header?" checkbox and the
      file upload field.
   :highlight: The "Is there a header?" checkbox and the upload field (red frame).
   :data: A semicolon-separated CSV file with a header row.
   :module: eyssen_product_bulk_add_stock
   :notes: English UI, light theme, 1440px width, crop to the wizard.

For every format, products are matched with the :guilabel:`Based On` field, which looks products
up by :guilabel:`Default Code` (internal reference), :guilabel:`Barcode` or :guilabel:`Product
Name`. The :guilabel:`With Quantity` and :guilabel:`With Price` toggles decide how many extra
columns (or trailing values, for copy/paste) each line carries; a live :guilabel:`Example` block
in the wizard updates to show the expected line format as these options change. When neither
toggle is enabled, every matched product is added with quantity 1 and price 0.

Matching a product that is not found, or a line that does not parse (wrong number of values, or a
quantity/price that is not numeric), stops the whole import with a validation error naming the
offending line. The same :guilabel:`If Product Duplication` choices as the previous-transfer
helper (:guilabel:`Stop` / :guilabel:`Skip` / :guilabel:`Replace` / :guilabel:`Increase`, default
:guilabel:`Stop` here) control what happens when a matched product already has a line on the
transfer.

Total quantity display
-----------------------

.. screenshot:: inventory-stock-helpers-sum-qty-detailed
   :menu: Inventory ‣ Transfers ‣ (a transfer) ‣ Operations tab
   :shows: The bottom of a transfer's Operations tab with the read-only "Sum Qty (detailed)" box below the
      lines, showing the number of distinct products and one total line per unit of measure.
   :highlight: The "Sum Qty (detailed)" box (red frame).
   :data: A transfer with three product lines in two different units of measure (e.g. 3 kg and 12 Units).
   :module: eyssen_quantity_total_stock
   :notes: English UI, light theme, 1440px width, crop to the box and the lines above it.

On the :guilabel:`Operations` tab of a transfer, below the product lines, a read-only
:guilabel:`Sum Qty (detailed)` box shows how many distinct products the transfer contains and the
total quantity per unit of measure — for example *3 kg* and *12 Units* on separate lines if the
transfer mixes UoMs. If any line already has recorded (done) quantities, those are used instead of
the planned quantities.

.. screenshot:: inventory-stock-helpers-sum-qty-column
   :menu: Inventory ‣ Transfers
   :shows: The Transfers list view with the compact "Sum Qty" column shown next to the Status column.
   :highlight: The "Sum Qty" column (red frame).
   :data: Five transfers with different numbers of lines; the column shows values like "3 P, 42 Qty".
   :module: eyssen_quantity_total_stock
   :notes: English UI, light theme, 1440px width, full list view.

The same information is available in a compact one-line form (:guilabel:`Sum Qty`, e.g. *3 P, 42
Qty*) as an optional column in the :guilabel:`Transfers` list view, next to the status column, so
totals can be scanned without opening each transfer.

Process number on a transfer
------------------------------

.. screenshot:: inventory-stock-helpers-process-number-field
   :menu: Inventory ‣ Transfers ‣ (a draft transfer)
   :shows: A draft transfer form with the "Process Number" field above the transfer name and the "Create a
      new process number" link visible because the field is still empty.
   :highlight: The "Process Number" field and the create link (red frame).
   :data: Draft transfer WH/INT/00003 with no process number yet.
   :module: process_number_stock
   :notes: English UI, light theme, 1440px width, crop to the form header.

When the ``process_number_stock`` module is installed, every transfer form shows a
:guilabel:`Process Number` field above the transfer's name. If it is empty, a :guilabel:`Create a
new process number` link creates one on the spot; an existing process number can also be selected
directly. This links the transfer to the shared eYssen :guilabel:`Process Number` record (a
trackable reference with assignees and a description, used to group related documents across
modules).

.. screenshot:: inventory-stock-helpers-process-number-form
   :menu: Inventory ‣ Process Numbers ‣ (a process number)
   :shows: A Process Number form with the "Stock Pickings" smart button (truck icon) showing a count, and
      the linked transfers listed below.
   :highlight: The "Stock Pickings" smart button (red frame).
   :data: A process number linked to three transfers.
   :module: process_number_stock
   :notes: English UI, light theme, 1440px width, crop to the button box and the linked transfers.

From the :guilabel:`Process Number` form itself, a :guilabel:`Stock Pickings` smart button shows
how many transfers are linked to it and opens their list, and the transfer list view gains a
:guilabel:`Process Number` column so linked transfers can be spotted at a glance.

.. tip::
   Changes to the :guilabel:`Process Number` field on a transfer are tracked in the chatter, which
   is useful for auditing when a transfer was reassigned to a different work order or job number.

Stock catalog
--------------

.. screenshot:: inventory-stock-helpers-catalog-button
   :menu: Inventory ‣ Transfers ‣ (a draft transfer) ‣ Operations tab
   :shows: The operations line list of a draft transfer with the "Catalog" link next to "Add a line".
   :highlight: The "Catalog" link (red frame).
   :data: Draft transfer WH/INT/00004 with one line.
   :module: eyssen_stock_catalog
   :notes: English UI, light theme, 1440px width, crop to the bottom of the operations list.

On a draft transfer's :guilabel:`Operations` tab, a :guilabel:`Catalog` link next to
:guilabel:`Add a line` opens the standard Odoo product catalog kanban view scoped to the transfer,
the same picker used on sales and purchase orders.

.. screenshot:: inventory-stock-helpers-catalog-kanban
   :menu: Inventory ‣ Transfers ‣ (a draft transfer) ‣ Operations tab ‣ Catalog
   :shows: The product catalog opened from a transfer, with product cards carrying quantity steppers but no
      unit price, and the "Back to Picking" button in the top-right.
   :highlight: The "Back to Picking" button and the absence of a price on the cards (red frames).
   :data: Six or seven products, two of them already added to the transfer.
   :module: eyssen_stock_catalog
   :notes: English UI, light theme, 1440px width, full catalog page.

Selecting a quantity for a product on a catalog tile adds or updates the matching operation line
on the transfer (removing it entirely if the quantity is set to zero); the button used to return
from the catalog reads :guilabel:`Back to Picking` instead of the generic label used on sales and
purchase catalogs. Because a transfer is not a priced document, the catalog does not show a unit
price on the product tiles, unlike the sales and purchase catalog. Once the transfer leaves the
:guilabel:`Draft` state, its lines — and therefore the catalog — become read-only.

Scan a barcode onto a transfer
------------------------------

With the ``eyssen_barcode_stock`` module installed, a draft transfer shows a barcode-scanner button
in the header of the operations block. Scanning a product's barcode adds that product to the
transfer with a quantity of one, or increases the quantity by one if the product already has a
line; the form reloads so the new quantity is visible immediately. Scanning a code that matches no
product leaves the transfer unchanged.

The button is only shown while the transfer is in the :guilabel:`Draft` state, and it requires the
eYssen barcode scanning layer (``eyssen_barcode_base``) and the eYssen
:guilabel:`Inventory` layer (``eyssen_stock``).

.. screenshot:: inventory-stock-helpers-barcode-scanner
   :menu: Inventory ‣ Transfers ‣ (a draft transfer)
   :shows: A draft transfer form with the barcode-scanner button in the header of the operations block, and
      the scanning dialog it opens.
   :highlight: The barcode-scanner button (red frame).
   :data: Draft transfer WH/INT/00005 with two scanned product lines.
   :module: eyssen_barcode_stock
   :notes: English UI, light theme, 1440px width, crop to the button and the dialog.

Analytic distribution on a transfer
-----------------------------------

The ``analytic_accounts_on_stock_picking`` module shows an :guilabel:`Analytic` column next to the
product on a transfer's operation lines, using the standard analytic-distribution widget. The value
is the analytic distribution of the purchase order line the move came from, so the cost centre a
receipt belongs to is visible without opening the purchase order.

In the other direction, an analytic item gains a :guilabel:`Transfer Reference` field naming the
transfer it relates to, which makes analytic reporting traceable back to the warehouse operation.

.. screenshot:: inventory-stock-helpers-analytic-distribution
   :menu: Inventory ‣ Receipts ‣ (a receipt from a purchase order) ‣ Operations tab
   :shows: The operations lines of a receipt with the "Analytic" column next to the product, showing the
      analytic distribution inherited from the purchase order line.
   :highlight: The "Analytic" column (red frame).
   :data: A receipt generated from a purchase order whose lines carry an analytic distribution.
   :module: analytic_accounts_on_stock_picking
   :notes: English UI, light theme, 1440px width, crop to the operation lines.

.. note::
   The column is read-only: the distribution is taken from the purchase order line and is empty for
   moves that come from a sales order or that have no source document.

Scope and modules
==================

- ``eyssen_add_item_from_previous_stock`` — :guilabel:`Add Previous Items` button and wizard to
  copy product lines from an earlier transfer.
- ``eyssen_product_bulk_add_stock`` — :guilabel:`Add Bulk Products` button and wizard to import
  product lines from pasted text, CSV or Excel.
- ``eyssen_quantity_total_stock`` — the :guilabel:`Sum Qty (detailed)` / :guilabel:`Sum Qty`
  computed totals on the transfer form and list view.
- ``process_number_stock`` — the :guilabel:`Process Number` field on transfers and the reverse
  :guilabel:`Stock Pickings` smart button (requires ``process_number``).
- ``eyssen_stock_catalog`` — the :guilabel:`Catalog` button that opens the product catalog picker
  on a transfer.
- ``eyssen_barcode_stock`` — the barcode-scanner button that adds scanned products to a draft
  transfer.
- ``analytic_accounts_on_stock_picking`` — the :guilabel:`Analytic` column on operation lines and
  the :guilabel:`Transfer Reference` field on analytic items.

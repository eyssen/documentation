=============================
Stock productivity helpers
=============================

Preparing a stock transfer by hand — adding products one by one, retyping a list from a supplier
e-mail, checking totals, filing it under an internal work order or browsing the product catalog —
is repetitive and error-prone on transfers with many lines. eYssen ships a small set of independent
productivity helpers that attach directly to the :guilabel:`Transfer` (``stock.picking``) form to
speed up exactly these steps. Each helper is a separate, single-purpose module, so a warehouse can
install only the ones it needs.

.. Screenshot plan:
.. stock_helpers-previous-item-button.png: the Transfer form in Draft state, operations tab,
..   showing the "Add Previous Items" button (files icon) at the top-right of the operations
..   block. Path: Inventory --> open any draft transfer.
.. stock_helpers-previous-item-wizard.png: the "Add Previous Items" popup wizard with the
..   "Previous Stock" field and "If Product Duplication" selection filled in. Path: on a draft
..   transfer, click the "Add Previous Items" button.
.. stock_helpers-bulk-add-button.png: the Transfer form in Draft state showing the
..   "Add Bulk Products" button (cubes icon) next to the "Add Previous Items" button. Path:
..   Inventory --> open any draft transfer.
.. stock_helpers-bulk-add-wizard.png: the "Add Bulk Products" wizard with Format set to
..   "Copy/Paste", Based On "Default Code", "With Quantity" checked, showing the live example
..   text block and the multi-line paste textarea. Path: on a draft transfer, click "Add Bulk
..   Products".
.. stock_helpers-bulk-add-wizard-csv.png: the same wizard with Format switched to "CSV",
..   showing the "Is there a header?" checkbox and the file upload field. Path: in the "Add Bulk
..   Products" wizard, change Format to CSV.
.. stock_helpers-quantity-total.png: the Transfer form, Operations tab, scrolled to the bottom
..   showing the "Sum Qty (detailed)" box below the operations lines (product type count plus one
..   line per UoM). Path: open a transfer with several product lines with different UoMs.
.. stock_helpers-quantity-total-list.png: the Transfers list view showing the compact "Sum Qty"
..   column (e.g. "3 P, 42 Qty") next to the Status column. Path: Inventory --> Transfers, default
..   list view.
.. stock_helpers-process-number-field.png: the Transfer form, Draft state, showing the Process
..   Number field above the transfer name with the "Create a new process number" link visible
..   when empty. Path: open a draft transfer that has no process number set yet.
.. stock_helpers-process-number-form.png: a Process Number form showing the "Stock Pickings"
..   smart button (truck icon) with a count, and the linked transfers listed under the Stock
..   Pickings group. Path: Inventory/Sales --> Process Numbers --> open one with linked transfers.
.. stock_helpers-catalog-button.png: the Transfer form, Operations tab, operations line list with
..   the "Add a line" control and the "Catalog" link button next to it. Path: open a draft
..   transfer, Operations tab.
.. stock_helpers-catalog-kanban.png: the product catalog kanban view opened from a transfer,
..   showing product tiles with quantity steppers and no price shown, and the "Back to Picking"
..   button in the top-right. Path: on a draft transfer, Operations tab, click "Catalog".

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

Configuration
=============

These helpers require no settings screen. Once the relevant module is installed, its button,
field or column appears automatically on the standard :guilabel:`Transfer` form and/or the
:guilabel:`Transfers` list view (:menuselection:`Inventory --> Transfers`). Every module builds on
top of the eYssen :guilabel:`Inventory` layer (``eyssen_stock`` and/or ``eyssen_base``); the
process-number helper additionally requires the ``eyssen_process_number`` module, which defines
the shared :guilabel:`Process Number` record.

.. note::
   The bulk-add-products wizard reads Excel files with the ``openpyxl`` Python library, listed in
   the module's ``requirements.txt``. Make sure it is available in the Odoo environment before
   using the Excel import format.

Usage
=====

Add items from a previous transfer
-----------------------------------

.. image:: stock_helpers/stock_helpers-previous-item-button.png
   :alt: Add Previous Items button on a draft transfer

On a transfer that is still in the :guilabel:`Draft` state, the :guilabel:`Add Previous Items`
button (files icon, top-right of the operations block) opens a popup where you pick a
:guilabel:`Previous Stock` transfer to copy lines from. Only transfers other than the current one
can be selected, and the picker searches by both the transfer's :guilabel:`Reference` and its
source document (:guilabel:`Origin`).

.. image:: stock_helpers/stock_helpers-previous-item-wizard.png
   :alt: Add Previous Items wizard with duplication behavior

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

.. image:: stock_helpers/stock_helpers-bulk-add-button.png
   :alt: Add Bulk Products button on a draft transfer

The :guilabel:`Add Bulk Products` button (cubes icon), shown next to :guilabel:`Add Previous
Items` on a draft transfer, opens a wizard for entering many products at once without touching a
previous transfer.

.. image:: stock_helpers/stock_helpers-bulk-add-wizard.png
   :alt: Add Bulk Products wizard, Copy/Paste format

Three input :guilabel:`Format` options are available:

- :guilabel:`Copy/Paste` — one product per line in a plain-text box;
- :guilabel:`CSV` — an uploaded, semicolon-separated CSV file, with an optional header row toggled
  with :guilabel:`Is there a header?`; or
- :guilabel:`Excel` — an uploaded ``.xlsx`` workbook (first sheet), also with the optional header
  toggle.

.. image:: stock_helpers/stock_helpers-bulk-add-wizard-csv.png
   :alt: Add Bulk Products wizard, CSV format with header toggle

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

.. image:: stock_helpers/stock_helpers-quantity-total.png
   :alt: Sum Qty detailed box on the transfer form

On the :guilabel:`Operations` tab of a transfer, below the product lines, a read-only
:guilabel:`Sum Qty (detailed)` box shows how many distinct products the transfer contains and the
total quantity per unit of measure — for example *3 kg* and *12 Units* on separate lines if the
transfer mixes UoMs. If any line already has recorded (done) quantities, those are used instead of
the planned quantities.

.. image:: stock_helpers/stock_helpers-quantity-total-list.png
   :alt: Compact Sum Qty column in the Transfers list view

The same information is available in a compact one-line form (:guilabel:`Sum Qty`, e.g. *3 P, 42
Qty*) as an optional column in the :guilabel:`Transfers` list view, next to the status column, so
totals can be scanned without opening each transfer.

Process number on a transfer
------------------------------

.. image:: stock_helpers/stock_helpers-process-number-field.png
   :alt: Process Number field on a draft transfer form

When the ``eyssen_process_number_stock`` module is installed, every transfer form shows a
:guilabel:`Process Number` field above the transfer's name. If it is empty, a :guilabel:`Create a
new process number` link creates one on the spot; an existing process number can also be selected
directly. This links the transfer to the shared eYssen :guilabel:`Process Number` record (a
trackable reference with assignees and a description, used to group related documents across
modules).

.. image:: stock_helpers/stock_helpers-process-number-form.png
   :alt: Stock Pickings smart button on a Process Number form

From the :guilabel:`Process Number` form itself, a :guilabel:`Stock Pickings` smart button shows
how many transfers are linked to it and opens their list, and the transfer list view gains a
:guilabel:`Process Number` column so linked transfers can be spotted at a glance.

.. tip::
   Changes to the :guilabel:`Process Number` field on a transfer are tracked in the chatter, which
   is useful for auditing when a transfer was reassigned to a different work order or job number.

Stock catalog
--------------

.. image:: stock_helpers/stock_helpers-catalog-button.png
   :alt: Catalog button in the operations line list

On a draft transfer's :guilabel:`Operations` tab, a :guilabel:`Catalog` link next to
:guilabel:`Add a line` opens the standard Odoo product catalog kanban view scoped to the transfer,
the same picker used on sales and purchase orders.

.. image:: stock_helpers/stock_helpers-catalog-kanban.png
   :alt: Product catalog kanban opened from a transfer, no price shown

Selecting a quantity for a product on a catalog tile adds or updates the matching operation line
on the transfer (removing it entirely if the quantity is set to zero); the button used to return
from the catalog reads :guilabel:`Back to Picking` instead of the generic label used on sales and
purchase catalogs. Because a transfer is not a priced document, the catalog does not show a unit
price on the product tiles, unlike the sales and purchase catalog. Once the transfer leaves the
:guilabel:`Draft` state, its lines — and therefore the catalog — become read-only.

Scope and modules
==================

- ``eyssen_add_item_from_previous_stock`` — :guilabel:`Add Previous Items` button and wizard to
  copy product lines from an earlier transfer.
- ``eyssen_product_bulk_add_stock`` — :guilabel:`Add Bulk Products` button and wizard to import
  product lines from pasted text, CSV or Excel.
- ``eyssen_quantity_total_stock`` — the :guilabel:`Sum Qty (detailed)` / :guilabel:`Sum Qty`
  computed totals on the transfer form and list view.
- ``eyssen_process_number_stock`` — the :guilabel:`Process Number` field on transfers and the
  reverse :guilabel:`Stock Pickings` smart button.
- ``eyssen_stock_catalog`` — the :guilabel:`Catalog` button that opens the product catalog picker
  on a transfer.

==========
Data audit
==========

The *Data Audit* module (`eyssen_data_audit`) provides a tool to check, and if needed repair, the
consistency of the **inventory valuation** of storable products valued at average cost (AVCO). For
every product, it compares three figures:

- the value of the *stock valuation layers* (the lines of the :guilabel:`Valuation` report of the
  Inventory app);
- the value booked on the stock valuation account by the related journal entries;
- the value of the posted vendor bills linked to the receipts through the purchase order lines;

and it recomputes, movement by movement, the value that each valuation layer *should* have if the
average cost had been applied consistently.

A typical use case is a database in which the opening stock was imported with wrong unit costs:
every delivery made afterwards was valued with a wrong average cost, and the stock account no longer
matches the inventory valuation.

.. note::
   - To install the module, go to :menuselection:`Settings --> eYssen ERP`, and, in the
     :guilabel:`General Modules` section, enable :guilabel:`Data Audit`. The *Inventory*,
     *Purchase*, and *Accounting* (automated inventory valuation) apps are required. The
     :ref:`correction <data-audit/fix>` step additionally relies on the valuation change history
     of the *Hungarian Accounting* module (`eyssen_l10n_hu_accountant`), which must be installed.
   - The tool is reserved for users with the :guilabel:`Administration: Settings` access right. Its
     menu, :menuselection:`Settings --> Technical --> Data Audit --> Stock Valuation Audit`, is
     displayed in :ref:`developer mode <developer-mode>`.
   - The titles of the audit views are displayed in Hungarian (*Készletérték Audit*), whatever the
     language of the user.

.. _data-audit/run:

Run an audit
============

#. Go to :menuselection:`Settings --> Technical --> Data Audit --> Stock Valuation Audit`, and click
   :guilabel:`New`.
#. Set the :guilabel:`Date`: only the valuation layers created up to that date and time are
   analyzed.
#. Optionally, :ref:`import reference prices <data-audit/reference-prices>`.
#. Click :guilabel:`Refresh`. The previous result of the audit, if any, is replaced.

The header of the audit then shows the :guilabel:`Error Count` (the number of products with at least
one inconsistent movement), and three totals: :guilabel:`Sum SVL Value`, :guilabel:`Sum Accounting
Value` (green when it equals the SVL value, red otherwise), and :guilabel:`Sum Bill Value`.

The :guilabel:`Products` tab contains one line per product, displayed in red when the product has an
error. Click the :icon:`fa-list-ul` (:guilabel:`Show Details`) icon of a line to open its movements.
For each valuation layer, the details show the :guilabel:`SVL Date`, :guilabel:`Quantity`,
:guilabel:`Unit Cost`, :guilabel:`SVL Value`, :guilabel:`Accounting Value`, :guilabel:`Bill Value`,
the recomputed average cost and :guilabel:`Expected Value`, and the two differences: :guilabel:`SVL
Diff` and :guilabel:`Accounting Diff`. A movement is an error when one of the two differences is
greater than 1 (in the company currency). Click the button at the end of a detail line to open the
valuation layer itself.

Click :guilabel:`View All` to open the product lines in a full list, where the :guilabel:`Errors
Only` and :guilabel:`Fixed Only` filters and the grouping by :guilabel:`Category` are available, and
:guilabel:`Print Errors` to get the *Error Report*, a PDF listing the inconsistent movements of each
product.

The expected value is computed as follows:

- **incoming** movement (positive quantity): the value of the layer is trusted, unless a
  :ref:`reference price <data-audit/reference-prices>` applies;
- **outgoing** movement (negative quantity): quantity × the average cost recomputed at that moment;
- **revaluation** (zero quantity): kept as is.

.. screenshot:: general-data-audit-form
   :menu: Settings ‣ Technical ‣ Data Audit ‣ Stock Valuation Audit ‣ (open a draft audit after Refresh)
   :shows: A draft stock valuation audit with the header buttons (Import References, Refresh, Fix Errors, View All, Print Errors), the date, the error count, the three totals with the accounting total in red, and the Products tab with two red product lines.
   :highlight: The header buttons and the "Error Count" field (red frames).
   :data: Audit dated today; 12 products, 2 of them with errors.
   :module: eyssen_data_audit
   :notes: English UI, light theme, 1440px width, developer mode enabled.

.. _data-audit/reference-prices:

Reference prices
================

A reference price is the unit cost that a product really had on a given date, typically the date
of the opening stock import. During the audit, the incoming movements of the product that are **not
linked to a purchase order** and that took place **on or before the reference date** are revalued
at the reference price; real purchases, and all later movements, keep their own value.

To load the reference prices, click :guilabel:`Import References` on a draft audit, choose how the
products are identified in the file with :guilabel:`Match By` (:guilabel:`SKU (Internal
Reference)`, :guilabel:`Product Name`, or :guilabel:`Barcode`), upload the :guilabel:`CSV File`,
and click :guilabel:`Import`.

The file must be a CSV file, separated by semicolons or commas, with a header row and three
columns: the product identifier, the reference date (`YYYY-MM-DD`), and the unit cost. A decimal
comma is accepted in the cost.

.. code-block:: text

   product_identifier;date;unit_cost
   56-0407860;2025-01-04;82.50

A notification reports the number of imported prices and the rejected lines (unknown product,
invalid date or cost). The imported prices are listed in the :guilabel:`Reference Prices` tab.
Click :guilabel:`Refresh` again to take them into account.

.. _data-audit/fix:

Fix the errors
==============

.. danger::
   :guilabel:`Fix Errors` **rewrites accounting data directly**: the value and unit cost of the
   valuation layers, and the debit and credit of the lines of **posted** journal entries, including
   in locked periods. The operation cannot be undone from the interface. Run it first on a copy of
   the database, make a backup, and involve your accountant before using it in production.

The :guilabel:`Fix Errors` button is displayed on a draft audit that has errors, and requires at
least one reference price: only the products with a reference price are corrected. After a
confirmation, the tool:

#. replays the whole movement history of each of these products: the opening movements are valued at
   the reference price, the purchases keep their original value (restored from the valuation change
   history if it had been altered), and every outgoing movement is revalued at the recomputed
   average cost. The valuation layers whose value or unit cost differs are updated;
#. for every journal entry linked to a valuation layer, aligns the line booked on the stock
   valuation account with the value of the layers, and applies the opposite correction to the
   counterpart line of the same product (e.g., the stock interim or the cost of goods sold account).

The audit then moves to the :guilabel:`Done` status and can no longer be refreshed or fixed. The
:guilabel:`Fixes` tab lists every correction with the :guilabel:`Old Value`, :guilabel:`New Value`,
:guilabel:`Old Unit Cost`, :guilabel:`New Unit Cost`, the corrections applied, and the journal entry
concerned. Click :guilabel:`Print Fixes` to get the *Fix Report*, to be kept with the accounting
records.

.. important::
   - All storable products are analyzed as if they were valued at average cost. Do not use the
     tool for products valued with the FIFO or standard price methods.
   - The stock valuation account is read from a single product category. If your product
     categories use different stock valuation accounts, the accounting comparison is not reliable.
   - After a fix, check the cost of the corrected products: the tool corrects the history, not the
     :guilabel:`Cost` field of the product.

.. seealso::
   - :doc:`../inventory_and_mrp/inventory/product_management/inventory_valuation/using_inventory_valuation`
   - :doc:`audit_log`

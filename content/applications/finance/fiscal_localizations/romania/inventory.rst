=======================
Inventory (Romania)
=======================

The `l10n_ro_stock_account` module applies the Romanian stock accounting, and `l10n_ro_stock_report`
prints the Romanian stock documents and reports. They apply to companies whose fiscal country is
Romania, that have the anglo-saxon accounting disabled and that use storable products with an
automatic (real-time) valuation.

.. seealso::
   - :doc:`invoicing`
   - :doc:`nondeductible_vat`
   - :doc:`saft_d406`

.. _localizations/romania/inventory/config:

Configuration
=============

Go to :menuselection:`Inventory --> Configuration --> Settings` and open the :guilabel:`Romanian
Stock Accounting` block.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Setting
     - Description
   * - :guilabel:`Accrue Uninvoiced Deliveries (418)`
     - Books the sales of delivered goods that are not invoiced yet (on by default).
   * - :guilabel:`Non-chargeable VAT on Accruals (4428)`
     - Books the non-chargeable VAT (4428) in the accruals of the receptions that have no vendor bill
       yet, and in the accruals of the deliveries with taxes applying VAT on payment (on by
       default). The output VAT of the other deliveries is always booked on 4427 at the delivery.
   * - :guilabel:`Goods in Transit for Bills before Reception`
     - Books the vendor bills posted before the reception on a goods-in-transit account (on by
       default).
   * - :guilabel:`Inventory Surplus Posting`
     - Surplus found at stock-taking: :guilabel:`Decrease of expense (3xx = 6xx)` (default) or
       :guilabel:`Other operating income (3xx = 7588)`.
   * - :guilabel:`Reception Committee`
     - Default members printed on the reception note.

Account managers can also set the accounts used for the accruals: :guilabel:`Invoices to Be Issued
Account (418)`, :guilabel:`Non-chargeable Output VAT Account (4428)`, :guilabel:`Non-chargeable Input
VAT Account (4428)`, :guilabel:`Inventory Surplus Income Account (7588)`, :guilabel:`Retail Markup
Account (378)`, :guilabel:`Retail Non-chargeable VAT Account (4428)` and :guilabel:`Imputed
Shortages Income Account (7581)`.

Account managers can click :guilabel:`Configure Romanian stock categories`, below these accounts, to
create, for the company, the Romanian product categories (for example goods 371, raw materials 301,
auxiliary materials 3021, finished products 345, packaging 381), each with its stock, input (4081),
output, expense and income accounts and its goods-in-transit account. The operation can be repeated
safely: only the empty values are filled. It also creates the :guilabel:`Internal Consumption`
location and one :guilabel:`Consumption Notes` operation type per warehouse.

.. note::
   When the module is updated on a database with one Romanian company, the Romanian categories are
   assigned to that company. With several Romanian companies, the shared categories stay global.

Locations (gestiuni)
--------------------

On a location, the :guilabel:`Romanian Stock Accounting` group has :guilabel:`Stock Account
(Gestiune)`, :guilabel:`Retail at Sale Price` and :guilabel:`Consumption Location`. For inventory
locations, :guilabel:`Imputed Shortages Debtor Account`, :guilabel:`Imputed To` and
:guilabel:`Imputation VAT` are also available. A transfer between locations that have different
stock accounts posts an accounting entry.

.. _localizations/romania/inventory/entries:

Accounting entries
==================

The following table shows when each entry is generated.

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Event
     - Entry
     - Comment
   * - Reception without a vendor bill
     - 371 = 408, and 4428 = 408 for the non-chargeable VAT
     - The VAT part needs the 4428 setting.
   * - Vendor bill after the reception
     - 408 = 401, 4426 = 401, 408 = 4428
     - Clears the accruals of the reception.
   * - Vendor bill before the reception
     - 32x = 408
     - Cleared at the reception.
   * - Delivery
     - 607 = 371
     - The cost of goods sold is booked at the delivery, not at the invoice. Finished products:
       711 = 345.
   * - Delivery without an invoice (*aviz*)
     - 418 = 70x and 4427
     - The VAT is declared in the month of the delivery.
   * - Posting of the invoice
     - Reverses the 418 entry
     - The invoice month only shows the difference.
   * - Surplus at stock-taking
     - 371 = 607 (or 7588)
     - Depends on :guilabel:`Inventory Surplus Posting`.
   * - Shortage at stock-taking
     - 607 = 371
     -
   * - Consumption note (*bon de consum*)
     - 601 = 301
     - The expense account of the product category.
   * - Imputed shortage
     - 607 = 371, then the debtor account of the location (for example 4282 or 461) = 7581 and 4427
     - Needs the imputation fields of the location.

Delivery without an invoice
---------------------------

When a delivery is validated, and the invoice does not exist yet, the entry 418 = 70x (the income
account of the product, 707 for goods) and 4427 is posted with real tax lines. The VAT is therefore
declared in the month of the delivery. The accrual is reversed by a separate entry, linked by
:guilabel:`Accrual Reversed by Invoice`, when the invoice is posted. If you reset the invoice to draft, the accrual is restored. No accrual is made if
the invoice is posted before the delivery, or if the option is off. For taxes with VAT on payment
(*TVA la încasare*), the VAT stays on 4428 and is not declared. The :doc:`D394 <d394>` return stays
based on invoices.

.. example::
   Delivery of 4 units at 100 with 21% VAT, cost 50: 607 +200 / 371 -200, and 418 484 / 707 -400 /
   4427 -84.

Retail locations
----------------

On a location with :guilabel:`Retail at Sale Price`, the stock account (371) holds the goods at the
sale price, including the markup (378) and the non-chargeable VAT (4428). The markup and the VAT
are discharged at the sale, in the opposite direction. For example, for goods with a cost of 100
and a sale price of 200 plus 21% VAT (242), the reception books 371 +142 on top of the cost, with
378 -100 and 4428 -42.

Romanian documents
==================

The transfers have a :guilabel:`Romanian Documents` tab. The document type is computed from the
operation: a reception is a *NIR*, a delivery is an *aviz*, an internal move to a consumption
location (or to an inventory or production location) is a consumption note, and the others are
transfers.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Group
     - Fields
   * - Reception (NIR)
     - :guilabel:`NIR Number`, supplier document number and date, customs declaration (*DVI*) number
       and date, :guilabel:`Reception Committee`.
   * - Transport
     - :guilabel:`Delegate`, ID document, means of transport, :guilabel:`Delivery Note Mention`
       (without invoice, for processing by third parties, invoice to follow, other reason) and the
       reason.

The NIR number is assigned when the reception is validated (`NIR/<year>/00001`). To make a
consumption note, tick :guilabel:`Consumption Notes (Bon de consum)` on the operation type.

Landed costs have the DVI number and date, :guilabel:`Customs Office`, :guilabel:`Customs Value` and
the import VAT, for information.

Print the documents
===================

On the transfer, click:

- :guilabel:`Print NIR` for a done reception: the *Notă de recepție și constatare de diferențe*
  (form 14-3-1A), with the reception committee, the differences, and the retail price for retail
  locations;
- :guilabel:`Print Delivery Note (Aviz)` for a delivery or an internal transfer that is ready or
  done: the *Aviz de însoțire a mărfii* (form 14-3-6A), with the shipping data and the signatures;
- :guilabel:`Print Consumption Note` for a consumption that is ready or done: the *bon de consum*
  (form 14-3-4A).

Printing is refused for non-Romanian companies, and the documents are in Romanian if the language is
installed.

Stock reports
=============

Go to :menuselection:`Inventory --> Reporting --> Romanian Stock Reports`. Each wizard has a
:guilabel:`Print` button.

:guilabel:`Stock Card (Fișa de magazie)`
   Select the location, the products (all moved products if empty) and the dates. One card per
   product with the initial stock, the in and out movements and the stock (form 14-3-8).

:guilabel:`Inventory List (Listă de inventariere)`
   Select the location and the :guilabel:`Inventory Date` (form 14-3-12). Options:
   :guilabel:`Only Counted Products`, :guilabel:`Include Zero Lines` and :guilabel:`Inventory
   Committee`. The list is grouped by stock account, with the book and counted quantities and the differences.

:guilabel:`Stock Valuation per Account (Situația stocurilor)`
   Select the date and, optionally, the location. :guilabel:`Detail per Product` is ticked by
   default; untick it to print the totals per account only. The values per account are compared with
   the general ledger balance.

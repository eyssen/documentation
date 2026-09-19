=====================
Product sales reports
=====================

The standard :guilabel:`Sales Analysis` report is based on the sales orders. Two eYssen reports
complete it with a **per-product profitability analysis based on what was actually invoiced**:
quantity, net revenue, cost of goods sold (COGS), and margin.

- :ref:`Product Sales <sales/product-sales-report>` covers the invoiced sales, split between direct
  and website sales;
- :ref:`Combined Product Sales <sales/combined-sales-report>` adds the Point of Sale orders, to get
  the total sales of a product over all channels.

Both reports are located in the :guilabel:`Reporting` menu of the Sales app, which is displayed to
the users with the :guilabel:`Sales: Administrator` access right. They respect the companies
selected in the company switcher, and their amounts are expressed in the currency of the company.

.. _sales/product-sales-report:

Product sales
=============

With the *Product Sales Report* module (`eyssen_product_sales_report`), go to
:menuselection:`Sales --> Reporting --> Product Sales`.

The report is built from the product lines of the **posted customer invoices and credit notes**
(credit notes are deducted; down payment lines are ignored). For each product, invoice date, and
sales channel, it shows:

- :guilabel:`Product Code`, and, as optional columns, the :guilabel:`Product`, the
  :guilabel:`Product Category`, the :guilabel:`Website`, and the :guilabel:`Invoice Date`;
- :guilabel:`Channel`: :guilabel:`Website` when the invoiced sales order comes from an eCommerce
  website, :guilabel:`Direct` otherwise;
- :guilabel:`Quantity`: the invoiced quantity;
- :guilabel:`Net Revenue`: the untaxed invoiced amount, converted into the company currency at the
  rate of the invoice;
- :guilabel:`COGS`: the cost of the goods sold, taken from the inventory valuation of the
  deliveries of the invoiced sales order line, in proportion to the invoiced quantity;
- :guilabel:`Net Margin` (net revenue − COGS) and :guilabel:`Margin %` (net margin ÷ net revenue).

The quantity and the three amounts are totaled at the bottom of the list and for each group.

The report opens grouped by :guilabel:`Product` and filtered on :guilabel:`This Year`. In the search
bar, the following options are available:

- filters: :guilabel:`Direct`, :guilabel:`Website`, :guilabel:`This Month`, :guilabel:`Last Month`,
  :guilabel:`This Quarter`, :guilabel:`This Year`, and :guilabel:`Last Year`;
- groupings: :guilabel:`Product`, :guilabel:`Category`, :guilabel:`Channel`, :guilabel:`Website`,
  and :guilabel:`Date` (by month).

Besides the list view, the pivot and graph views are available, and the list can be :ref:`exported
<essentials/export_import_data/export-data>`.

.. note::
   The COGS is only known for storable products delivered from a sales order with :doc:`automated
   or manual inventory valuation
   <../../inventory_and_mrp/inventory/product_management/inventory_valuation/inventory_valuation_config>`.
   Invoice lines that are not linked to a delivery (services, invoices created without a sales
   order, products not delivered yet) have a COGS of zero, and therefore a margin equal to their
   revenue.

.. screenshot:: sales-product-sales-report-list
   :menu: Sales ‣ Reporting ‣ Product Sales
   :shows: The "Product Sales Analysis" list grouped by product and filtered on "This Year", with the Channel, Quantity, Net Revenue, COGS, Net Margin and Margin % columns and their totals.
   :highlight: The COGS, Net Margin and Margin % columns (red frame).
   :data: Demo company with several months of invoiced sales orders, some of them from the website.
   :module: eyssen_product_sales_report
   :notes: English UI, light theme, 1440px width.

.. _sales/combined-sales-report:

Combined product sales
======================

With the *Combined Product Sales Report* module (`eyssen_combined_sales_report`), go to
:menuselection:`Sales --> Reporting --> Combined Product Sales`. The module requires both the
*Product Sales Report* and the :ref:`POS Product Sales Report <pos/reporting/product-sales>`
modules.

The report merges two sources:

- the invoiced sales, exactly as in the :ref:`Product Sales <sales/product-sales-report>` report
  (channels :guilabel:`Direct` and :guilabel:`Website`, dated on the invoice date);
- the lines of the Point of Sale orders that are paid, posted, or invoiced (channel :guilabel:`POS`,
  dated on the order date), with the cost recorded on the order lines as COGS.

Compared with the previous report, a :guilabel:`POS` filter is added, and the :guilabel:`Website`
column and grouping are replaced by :guilabel:`Channel Detail`, which contains the name of the
website or of the point of sale.

.. important::
   A Point of Sale order for which an **invoice** was issued is counted twice in this report: once
   in the :guilabel:`POS` channel, and once in the :guilabel:`Direct` channel through its invoice
   (without COGS). If invoices are frequently issued from the Point of Sale, filter or group by
   :guilabel:`Channel` and interpret the :guilabel:`Direct` figures accordingly.

.. screenshot:: sales-combined-sales-report-pivot
   :menu: Sales ‣ Reporting ‣ Combined Product Sales ‣ Pivot view
   :shows: The pivot view of the combined report with the product categories in rows, the three sales channels (Direct, Website, POS) in columns and the Net Revenue and Net Margin measures.
   :highlight: The three channel columns (red frame).
   :data: Demo company with sales orders, website orders and POS orders over the current year.
   :module: eyssen_combined_sales_report
   :notes: English UI, light theme, 1440px width.

.. seealso::
   - :ref:`pos/reporting/product-sales`
   - :doc:`sales_quotations/margin`

=========
Reporting
=========

All POS reports are available under :menuselection:`Point of Sale --> Reporting`. They can also be
reached from the **POS dashboard** by clicking the vertical ellipsis (:guilabel:`⋮`) button on a POS
card and selecting an entry under :guilabel:`Reporting`.

Orders
======

:menuselection:`Point of Sale --> Reporting --> Orders` opens the POS order analysis. The statistics
are available in a graph and a pivot view that can be filtered and grouped — by point of sale,
salesperson, customer, product, product category, or period — to answer questions such as which
products sell best in which shop.

.. screenshot:: pos-reporting-orders
   :menu: Point of Sale ‣ Reporting ‣ Orders
   :shows: The POS order analysis in graph view, grouped by point of sale, with the measures
      dropdown open.
   :module: point_of_sale
   :notes: English UI, light theme, 1440px width.

Sales details
=============

:menuselection:`Point of Sale --> Reporting --> Sales Details` opens a wizard in which you select a
:guilabel:`Start Date`, an :guilabel:`End Date`, and one or more points of sale, then click
:guilabel:`Print` to produce a PDF summary of the sales, the taxes, and the payments of that
period.

Session report
==============

:menuselection:`Point of Sale --> Reporting --> Session Report` opens a wizard in which you select a
session and click :guilabel:`Print` to produce its daily sales report: the opening and closing
balances, the takings per payment method, and the cash difference recorded at the :ref:`closing
control <pos/session-close>`.

.. _pos/reporting/product-sales:

Product sales
=============

The *POS Product Sales Report* module (`eyssen_pos_sales_report`) adds
:menuselection:`Point of Sale --> Reporting --> Product Sales`: a per-product profitability analysis
of the POS orders, which the standard order analysis does not provide.

Each line shows, for one product in one point of sale:

- :guilabel:`Product Code` and :guilabel:`Product`;
- :guilabel:`Quantity` sold;
- :guilabel:`Net Revenue` (the untaxed subtotal);
- :guilabel:`COGS`, the cost of the goods sold;
- :guilabel:`Net Margin` and :guilabel:`Margin %`.

The quantity and the three amount columns are summed, so the totals of any selection are displayed
at the bottom of the list.

The report opens grouped by product and filtered on the current year. Use the search panel to
change the period (:guilabel:`This Month`, :guilabel:`Last Month`, :guilabel:`This Quarter`,
:guilabel:`This Year`, :guilabel:`Last Year`), to filter by :guilabel:`Product Code`,
:guilabel:`Product`, :guilabel:`Category` or :guilabel:`Point of Sale`, and to group by product,
category, point of sale, or month. The list, pivot, and graph views are all available, and the list
view can be exported to a spreadsheet.

.. screenshot:: pos-reporting-product-sales
   :menu: Point of Sale ‣ Reporting ‣ Product Sales
   :shows: The "POS Product Sales Analysis" list grouped by product, showing the quantity, net
      revenue, COGS, net margin and margin percentage columns with their totals.
   :data: Demo company with a few weeks of POS orders across two points of sale.
   :module: eyssen_pos_sales_report
   :notes: English UI, light theme, 1440px width.

.. note::
   The margin is computed from the cost recorded on the POS order lines. Products without a cost
   price are reported with a COGS of zero and therefore with a margin equal to their revenue.

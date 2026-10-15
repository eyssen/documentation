=======
Reports
=======

Three views under :menuselection:`Competitor Prices --> Prices` show where you stand. They are
read-only; the prices are those of confirmed listings that are current and valid (suspicious and
rejected prices are left out).

Price position
==============

:menuselection:`Competitor Prices --> Prices --> Price Position` has one line per tracked product:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Column
     - Meaning
   * - :guilabel:`Our Sales Price`
     - The sales price of the product.
   * - :guilabel:`Lowest (net)`, :guilabel:`Median (net)`, :guilabel:`Highest (net)`
     - The net competitor prices per unit and their number, :guilabel:`Competitor Prices`.
   * - :guilabel:`Gap to Lowest (%)`
     - (own price − lowest competitor price) ÷ lowest × 100. Positive: you are more expensive than the
       cheapest competitor.
   * - :guilabel:`Price Index`
     - Own price ÷ median competitor price × 100. Above 100 you are above the middle of the market.
   * - :guilabel:`We Are Cheapest`
     - Your price is not above the lowest competitor price.
   * - :guilabel:`Recommended Price`
     - The open recommendation, if any.
   * - :guilabel:`Last Competitor Change`
     - When a competitor price last changed (optional column).

Filters: :guilabel:`We Are More Expensive`, :guilabel:`We Are Cheapest` and :guilabel:`New
Recommendation`; group by :guilabel:`Category`. The pivot and graph views average the price index and
the gap by category.

.. screenshot:: sales-competitor-prices-position
   :menu: Competitor Prices ‣ Prices ‣ Price Position
   :shows: The price position list with our sales price, lowest, median and highest competitor price, gap,
      price index, the "We Are Cheapest" column and the recommended price, filtered to "We Are More
      Expensive" and sorted by price index.
   :highlight: The "Price Index" column (red frame).
   :data: About 20 products in two categories.
   :notes: English UI, light theme, 1440px width.

Competitor price changes
========================

:menuselection:`Competitor Prices --> Prices --> Competitor Price Changes` lists the price history
lines of competitors where the price changed, with the :guilabel:`Change (%)`: use it to see who moved
this week. It opens in the list view; switch to the pivot or the graph. The filters and the grouping
are those of the price history (see :doc:`products`).

Price history
=============

:menuselection:`Competitor Prices --> Prices --> Price History` is the complete history, with the
graph (price per day, one line per seller) and the pivot (products by competitor). Your own price is
one of the lines (filter :guilabel:`Own Prices`), so you can see your price next to the competitors'
over time.

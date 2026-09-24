=========
Reporting
=========

You can find several reports under the :guilabel:`Reporting` menu of most apps that let you analyze
and visualize the data of your records.

.. _reporting/views:

Selecting a view
================

Depending on the report, Odoo can display the data in various ways. Sometimes, a unique view
fully tailored to the report is available, while several views are available for others. However,
two generic views are dedicated to reporting: the graph and pivot views.

.. _reporting/views/graph:

Graph view
----------

The :ref:`graph view <reporting/using-graph>` is used to visualize your records' data, helping you
identify patterns and trends. The view is often found under the :guilabel:`Reporting` menu of apps
but can be found elsewhere. Click the **graph view button** located at the top right to access
it.

.. screenshot:: essentials-reporting-graph-button
   :menu: Sales ‣ Reporting ‣ Sales
   :shows: View switcher at the top right of the control panel with the Graph view button.
   :highlight: The Graph view button.
   :module: sale
   :notes: English UI, crop tightly to the view switcher.

.. _reporting/views/pivot:

Pivot view
----------

The :ref:`pivot view <reporting/using-pivot>` is used to aggregate your records' data and break it
down for analysis. The view is often found under the :guilabel:`Reporting` menu of apps but can be
found elsewhere. Click the **pivot view button** located at the top right to access it.

.. screenshot:: essentials-reporting-pivot-button
   :menu: Sales ‣ Reporting ‣ Sales
   :shows: View switcher at the top right of the control panel with the Pivot view button.
   :highlight: The Pivot view button.
   :module: sale
   :notes: English UI, crop tightly to the view switcher.

.. _reporting/choosing-measures:

Choosing measures
=================

After selecting a view, you should ensure only the relevant records are :doc:`filtered <search>`.
Next, you should choose what is measured. By default, a measure is always selected. If you wish to
edit it, click :guilabel:`Measures` and choose one or, only for pivots, multiple measures.

.. note::
   When you select a measure, Odoo aggregates the values recorded on that field for the filtered
   records. Only numerical fields (integer, decimal, monetary) can be measured. In addition, the
   :guilabel:`Count` option is used to count the total number of filtered records.

After choosing what you want to measure, you can define how the data should be :ref:`grouped
<search/group>` depending on the dimension you want to analyze. By default, the data is often
grouped by *Date > Month*, which is used to analyze the evolution of a measure over the months.

.. tip::
   When you filter a single time period, the option to compare it against another one appears.

   .. screenshot:: essentials-reporting-comparison
      :menu: Sales ‣ Reporting ‣ Sales
      :shows: Search panel dropdown with a single period selected under Filters and the "Comparison" section offering "Previous Period" and "Previous Year".
      :highlight: The Comparison section.
      :module: sale
      :notes: English UI, crop to the relevant area.

.. example::

   .. tabs::

      .. tab:: Select measures

         Among other measures, you could add the :guilabel:`Margin` and :guilabel:`Count` measures
         to the Sales Analysis report. By default, the :guilabel:`Untaxed Amount` measure is
         selected.

         .. screenshot:: essentials-reporting-measures
            :menu: Sales ‣ Reporting ‣ Sales (Pivot view)
            :shows: The Measures dropdown open with several measures ticked (e.g., Untaxed Amount, Qty Ordered) and Count at the bottom.
            :highlight: The Measures dropdown.
            :data: Demo sales orders.
            :module: sale
            :notes: English UI, crop to the relevant area.

      .. tab:: Group measures

         You could group the measures by :guilabel:`Product Category` at the level of rows on the
         previous Sales Analysis report example.

         .. screenshot:: essentials-reporting-single-group
            :menu: Sales ‣ Reporting ‣ Sales (Pivot view)
            :shows: Pivot with rows grouped by Product Category and the measures as columns.
            :data: Demo sales orders.
            :module: sale
            :notes: English UI, crop to the relevant area.

.. _reporting/using-pivot:

Using the pivot view
====================

Grouping data is quintessential to the pivot view. It enables drilling down the data to gain deeper
insights. While you can use the :guilabel:`Group By` option to quickly add a group at the level of
rows, as shown in the example above, you can also click the plus button (:guilabel:`➕`) next to the
:guilabel:`Total` header at the level of rows *and* columns, and then select one of the
**preconfigured groups**. To remove one, click the minus button (:guilabel:`➖`).

Once you have added a group, you can add new ones on the opposite axis or the newly created
subgroups.

.. example::
   You could further divide the measures on the previous Sales Analysis report example by the
   :guilabel:`Salesperson` group at the level of columns and by the :guilabel:`Order Date > Month`
   group on the :guilabel:`All / Saleable / Office Furniture` product category.

   .. screenshot:: essentials-reporting-multiple-groups
      :menu: Sales ‣ Reporting ‣ Sales (Pivot view)
      :shows: Pivot with Salesperson groups as columns, product categories as rows, and the "All / Saleable / Office Furniture" row expanded by Order Date > Month.
      :highlight: The expanded row and the column headers.
      :data: Demo sales orders.
      :module: sale
      :notes: English UI, crop to the relevant area.

.. tip::
   - Switch the rows and columns' groups by clicking the flip axis button (:guilabel:`⇄`).
   - Click on a measure's label to sort the values by ascending (⏶) or descending (⏷) order.
   - Click the :guilabel:`Expand all` button to open all groups defined in the search. Click an
     expanded header, e.g., :guilabel:`Total`, to collapse it.
   - Click a cell to open the list of the records it aggregates.
   - Download a `.xlsx` version of the pivot by clicking the download button (:guilabel:`⭳`).

.. _reporting/using-graph:

Using the graph view
====================

Three graphs are available: the bar, line, and pie charts.

**Bar charts** are used to show the distribution or a comparison of several categories. They are
especially useful as they can deal with larger data sets.

**Line charts** are useful to show changing time series and trends over time.

**Pie charts** are used to show the distribution or a comparison of a small number of categories
when they form a meaningful whole.

.. tabs::

   .. tab:: Bar chart

      .. screenshot:: essentials-reporting-graph-bar
         :menu: Sales ‣ Reporting ‣ Sales (Graph view)
         :shows: The Sales Analysis report displayed as a bar chart, with the chart type buttons in the toolbar.
         :highlight: The bar chart button.
         :data: Demo sales orders grouped by Order Date > Month.
         :module: sale
         :notes: English UI, crop to the relevant area.

   .. tab:: Line chart

      .. screenshot:: essentials-reporting-graph-line
         :menu: Sales ‣ Reporting ‣ Sales (Graph view)
         :shows: The Sales Analysis report displayed as a line chart, with the chart type buttons in the toolbar.
         :highlight: The line chart button.
         :data: Demo sales orders grouped by Order Date > Month.
         :module: sale
         :notes: English UI, crop to the relevant area.

   .. tab:: Pie chart

      .. screenshot:: essentials-reporting-graph-pie
         :menu: Sales ‣ Reporting ‣ Sales (Graph view)
         :shows: The Sales Analysis report displayed as a pie chart, with the chart type buttons in the toolbar.
         :highlight: The pie chart button.
         :data: Demo sales orders grouped by Order Date > Month.
         :module: sale
         :notes: English UI, crop to the relevant area.

.. tip::
   For **bar** and **line** charts, you can use the stacked option when you have at least two
   groups, which then appear on top of each other instead of next to each other.

   .. tabs::

      .. tab:: Stacked bar chart

         .. screenshot:: essentials-reporting-graph-stacked-bar
            :menu: Sales ‣ Reporting ‣ Sales (Graph view)
            :shows: The Sales Analysis report as a stacked bar chart grouped by month and salesperson (Stacked option enabled).
            :highlight: The Stacked / Cumulative toggle in the toolbar.
            :data: Demo sales orders.
            :module: sale
            :notes: English UI, crop to the relevant area.

      .. tab:: Regular bar chart

         .. screenshot:: essentials-reporting-graph-non-stacked-bar
            :menu: Sales ‣ Reporting ‣ Sales (Graph view)
            :shows: The Sales Analysis report as a bar chart grouped by month and salesperson with the Stacked option disabled (bars side by side).
            :highlight: The Stacked / Cumulative toggle in the toolbar.
            :data: Demo sales orders.
            :module: sale
            :notes: English UI, crop to the relevant area.

      .. tab:: Stacked line chart

         .. screenshot:: essentials-reporting-graph-stacked-line
            :menu: Sales ‣ Reporting ‣ Sales (Graph view)
            :shows: The Sales Analysis report as a stacked line chart grouped by month and salesperson (Stacked option enabled).
            :highlight: The Stacked / Cumulative toggle in the toolbar.
            :data: Demo sales orders.
            :module: sale
            :notes: English UI, crop to the relevant area.

      .. tab:: Regular line chart

         .. screenshot:: essentials-reporting-graph-non-stacked-line
            :menu: Sales ‣ Reporting ‣ Sales (Graph view)
            :shows: The Sales Analysis report as a line chart grouped by month and salesperson with the Stacked option disabled.
            :highlight: The Stacked / Cumulative toggle in the toolbar.
            :data: Demo sales orders.
            :module: sale
            :notes: English UI, crop to the relevant area.

   For **line** charts, you can use the cumulative option to sum values, which is especially useful
   to show the change in growth over a time period.

   .. tabs::

      .. tab:: Cumulative line chart

         .. screenshot:: essentials-reporting-graph-cumulative
            :menu: Sales ‣ Reporting ‣ Sales (Graph view)
            :shows: The Sales Analysis report as a line chart with the Cumulative option enabled.
            :highlight: The Stacked / Cumulative toggle in the toolbar.
            :data: Demo sales orders.
            :module: sale
            :notes: English UI, crop to the relevant area.

      .. tab:: Regular line chart

         .. screenshot:: essentials-reporting-graph-non-cumulative
            :menu: Sales ‣ Reporting ‣ Sales (Graph view)
            :shows: The Sales Analysis report as a line chart with the Cumulative option disabled.
            :highlight: The Stacked / Cumulative toggle in the toolbar.
            :data: Demo sales orders.
            :module: sale
            :notes: English UI, crop to the relevant area.

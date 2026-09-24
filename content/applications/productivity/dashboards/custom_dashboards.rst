=================
Custom dashboards
=================

The *Dashboard* module (``dashboard``) adds a second, fully configurable dashboard application.
Unlike the standard dashboards, custom dashboards are built record by record: each dashboard (or
*board*) is a grid of *widgets* — charts, |KPIs|, tables, and shortcuts — that read live data from
the database.

.. |KPIs| replace:: :abbr:`KPIs (Key Performance Indicators)`
.. |KPI| replace:: :abbr:`KPI (Key Performance Indicator)`

.. note::
   This documentation describes the *Dashboard* (``dashboard``) module. The standard, pre-configured
   dashboards described in :doc:`../dashboards` are provided by a different application, which also
   uses the name :guilabel:`Dashboards`.

Access rights
=============

The module defines three access levels in the :guilabel:`Dashboard` category of a user's
:ref:`access rights <access-rights/users>`:

- :guilabel:`User`: can open the dashboards they have been granted access to.
- :guilabel:`Manager`: can create and configure dashboards and widgets, and manage the layout.
- :guilabel:`Technical (Python / SQL)`: can additionally create widgets whose data comes from Python
  code or an SQL query.

.. danger::
   Python and SQL widgets run with full database access, bypassing access rights and record rules.
   Grant the :guilabel:`Technical (Python / SQL)` level only to users who are trusted with reading
   the entire database.

Create a dashboard
==================

To create a dashboard, go to :menuselection:`Dashboards --> Configuration --> Boards` and click
:guilabel:`New`. Fill in:

- :guilabel:`Dashboard Name`: the name shown in the menu and at the top of the dashboard.
- :guilabel:`Menu Sequence`: the position of the dashboard's menu item.
- :guilabel:`Also show under`: optionally, another app's menu (e.g., :guilabel:`Sales`) where a menu
  item for this dashboard is created as well, in addition to the entry in the Dashboards app.
- :guilabel:`Auto Refresh`: how often the dashboard reloads its data — :guilabel:`Off`,
  :guilabel:`15 seconds`, :guilabel:`30 seconds`, :guilabel:`1 minute`, or :guilabel:`5 minutes`.
- :guilabel:`Allowed Groups` and :guilabel:`Allowed Users`: who may open the dashboard. If both are
  empty, every user with :guilabel:`Dashboard / User` rights sees it.

The :guilabel:`System` section shows the client action and the menu items Odoo created for the
dashboard; these fields are read-only.

Click :guilabel:`View Dashboard` in the header to open the dashboard itself.

.. screenshot:: productivity-custom-dashboards-board-form
   :menu: Dashboards ‣ Configuration ‣ Boards
   :shows: The dashboard form with the name, the Menu, Settings and Access groups filled in, and the Widgets tab listing four widgets with their type and data source.
   :highlight: The "Access" and "Settings" groups (red frame).
   :data: Dashboard "Sales overview" with widgets "Revenue" (KPI), "Monthly sales" (Chart), "Top customers" (Table), "New quotation" (Shortcut).
   :module: dashboard
   :notes: English UI, light theme, 1440px width.

Arrange the layout
------------------

On the dashboard itself, widgets are placed on a grid. Managers can drag a widget by its header to
move it and drag its bottom-right corner to resize it. The layout is stored per dashboard, so all
users see the same arrangement.

.. screenshot:: productivity-custom-dashboards-layout
   :menu: Dashboards ‣ <dashboard name>
   :shows: A custom dashboard with a KPI row at the top, a bar chart and a pie chart side by side, a table below, and a widget being dragged to a new grid position.
   :data: Dashboard "Sales overview" with demo sales data.
   :module: dashboard
   :notes: English UI, light theme, 1440px width.

Widgets
=======

Widgets are managed from the :guilabel:`Widgets` tab of a dashboard, or from
:menuselection:`Dashboards --> Configuration --> Widgets`. Each widget has a :guilabel:`Name`, a
:guilabel:`Type`, and — except for shortcuts — a :guilabel:`Data Source`.

Data source
-----------

- :guilabel:`ORM`: the widget reads a model through the standard database layer, so the user's
  access rights and record rules apply. Select the :guilabel:`Model`, the :guilabel:`Category /
  Group By` field and, for hierarchical charts, a :guilabel:`Sub / Secondary Group By` field. A
  :guilabel:`Domain Filter`, a :guilabel:`Date Filter Field` with a :guilabel:`Date Range`, a
  :guilabel:`Limit`, and the sorting (:guilabel:`Sort By`, :guilabel:`Sort Order`) further restrict
  the data. For records linked through a many2many or one2many field, :guilabel:`M2M / O2M
  Aggregation` decides whether a record is counted once for each related record or only once, and
  :guilabel:`Include Empty Category` adds a bucket for records with no value.
- :guilabel:`Python`: the widget is filled by a short Python snippet that populates a result
  dictionary.
- :guilabel:`SQL`: the widget is filled by a `SELECT` query. The first column provides the labels,
  the remaining columns the values. Statements that modify data are rejected.

Both :guilabel:`Python` and :guilabel:`SQL` are edited in the :guilabel:`Custom Code` tab and are
only available to users with the :guilabel:`Technical (Python / SQL)` access level.

Measures
--------

In the :guilabel:`Measures` list, add the fields to plot or aggregate. For each measure, select the
:guilabel:`Field`, the :guilabel:`Aggregation`, an optional :guilabel:`Label` and :guilabel:`Color`,
and — for dual-axis charts — the :guilabel:`Y Axis` to use.

Charts
------

Set the :guilabel:`Chart Type` to :guilabel:`Bar`, :guilabel:`Line`, :guilabel:`Area`,
:guilabel:`Pie`, :guilabel:`Radar`, :guilabel:`Funnel`, :guilabel:`Gauge`, :guilabel:`Scatter`,
:guilabel:`Heatmap`, :guilabel:`Treemap`, :guilabel:`Sunburst`, :guilabel:`Dual Sunburst`,
:guilabel:`Sankey`, :guilabel:`Stacked Bar (Hierarchical)`, or :guilabel:`Bubble / Scatter`.

Depending on the chart type, further options appear: :guilabel:`Orientation` and
:guilabel:`Stacking` for bars, :guilabel:`Smooth`, :guilabel:`Show Dots` and :guilabel:`Step` for
lines, :guilabel:`Doughnut Style`, :guilabel:`Top N (0=all)`, :guilabel:`Group Others` and
:guilabel:`Label Format` for pies, or :guilabel:`Min` and :guilabel:`Max` for gauges.
:guilabel:`Show Legend` and :guilabel:`Show Labels` control the chart decorations, and
:guilabel:`Theme` switches between the :guilabel:`Default`, :guilabel:`Dark`, and
:guilabel:`Vintage` color themes.

.. tip::
   Hierarchical chart types (treemap, sunburst, dual sunburst, sankey, hierarchical stacked bar,
   bubble) display two levels of data and therefore require a :guilabel:`Sub / Secondary Group By`
   field.

.. screenshot:: productivity-custom-dashboards-chart-widget
   :menu: Dashboards ‣ Configuration ‣ Widgets
   :shows: A chart widget form with Type "Chart", Data Source "ORM", the Data Source group (model, category group-by), the Measures list with one measure, and the Bar Options group.
   :highlight: The "Data Source" and "Measures" groups (red frame).
   :data: Widget "Monthly sales" on model "Sales Order", grouped by order date, measure "Total" summed.
   :module: dashboard
   :notes: English UI, light theme, 1440px width.

|KPIs|
------

A |KPI| widget shows a single aggregated figure. Set an :guilabel:`Icon`, an optional
:guilabel:`Target` value, and a :guilabel:`Compare Period` to display the variation against the
previous period.

Tables
------

A table widget lists records of the selected model. Choose the fields to display in
:guilabel:`Columns`; the :guilabel:`Limit` and sorting options of the data source decide how many
rows are shown and in which order.

Shortcuts
---------

A shortcut widget is a button that opens a view or a URL. Select an :guilabel:`Action` or enter a
:guilabel:`Target URL`, and choose an :guilabel:`Icon` or upload an :guilabel:`Icon Image`. To
display a counter on the button, select a :guilabel:`Badge Model` and, optionally, a
:guilabel:`Badge Domain` that restricts the records counted.

Appearance and access
---------------------

Every widget has a :guilabel:`Primary Color` and a :guilabel:`Secondary Color`, and can be
restricted to specific :guilabel:`Allowed Groups` or :guilabel:`Allowed Users`. A widget that a user
may not see is simply left out of their dashboard.

Sample dashboards
=================

To get started quickly, go to :menuselection:`Dashboards --> Configuration --> Settings`. Each card
creates a ready-made dashboard filled with widgets built on real data from the corresponding app:
:guilabel:`Sales Dashboard`, :guilabel:`Accounting Dashboard`, :guilabel:`Inventory Dashboard`,
:guilabel:`CRM Dashboard`, and :guilabel:`Purchase Dashboard`. Each sample can only be created once,
after which it can be edited like any other dashboard.

.. screenshot:: productivity-custom-dashboards-samples
   :menu: Dashboards ‣ Configuration ‣ Settings
   :shows: The Settings page with the "Sample Dashboards" cards for Sales, Accounting, Inventory, CRM and Purchase, each with its create button.
   :module: dashboard
   :notes: English UI, light theme, 1440px width.

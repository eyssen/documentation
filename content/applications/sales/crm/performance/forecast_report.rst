===============
Forecast report
===============

.. |caret| replace:: :icon:`fa-caret-down` :guilabel:`(down)` icon
.. |pivot| replace:: :icon:`oi-view-pivot` :guilabel:`(pivot)` icon
.. |list| replace:: :icon:`oi-view-list` :guilabel:`(list)` icon

The *Forecast* report in the *CRM* app allows users to view upcoming opportunities and build a
forecast of potential sales. Opportunities are grouped by the month of their expected closing date,
and can be dragged-and-dropped to adjust the deadline.

To access the *Forecast* report, navigate to :menuselection:`CRM app --> Reporting --> Forecast`.

Navigate the forecast report
============================

The default :guilabel:`Forecast` report includes opportunities assigned to the current user's
pipeline, and are expected to close within four months. It also shows opportunities without an
assigned expected closing date. The opportunities are grouped by month in a :icon:`oi-view-kanban`
:guilabel:`(Kanban)` view.

.. screenshot:: sales-crm-forecast-report
   :menu: CRM ‣ Reporting ‣ Forecast
   :shows: The Forecast report in its default graph view, with the expected revenue stacked per month and the default filters in the search bar.
   :highlight: No highlight; the report is the subject.
   :data: Demo pipeline over six months.
   :module: crm
   :notes: English UI, light theme, 1440px width, crop to the search bar and the chart.

Expected closing date
---------------------

Opportunities are grouped by the date assigned in the *Expected Closing* field on an opportunity
form. To change this date directly from the :guilabel:`Forecast` page, select the Kanban card for
the desired opportunity, then click and drag the card to the desired column.

.. note::
   The default time frame for the forecast is *month*. This can be changed by clicking the |caret|
   next to the :guilabel:`Search...` bar at the top of the report. Under the :guilabel:`Group By`
   heading in the resulting drop-down menu, click :guilabel:`Expected Closing` to expand the list of
   available options, and select a desired amount of time from the list.

After an opportunity is added to a new month, the *Expected Closing* field on the opportunity form
is updated to the *last* date of the new month.

.. tip::
   The *Expected Closing* field can also be manually updated on the opportunity card. To do that,
   click on the Kanban card for an opportunity on the :guilabel:`Forecast` page to open the
   opportunity's detail form. Click in the :guilabel:`Expected Closing` field, and use the calendar
   popover to select a new closing date.

Prorated revenue
----------------

The prorated revenue is the :guilabel:`Expected Revenue` amount that is displayed at the top of the
column for each month on the :guilabel:`Forecast` reporting page. This value is situated to the
right of the progress bar. The calculation for :guilabel:`Expected Revenue` is the total of the
prorated revenue specific to that particular time frame.

The prorated revenue is calculated using the formula below:

.. math::

   \text{Expected Revenue} \times \text{Probability} = \text{Prorated Revenue}

As opportunities are moved from one column to another, the column's revenue is automatically updated
to reflect the change.

.. example::
   A forecast report for June includes two opportunities:

   The first opportunity, `Global Solutions`, has an expected revenue of `$3,800`, and a probability
   of `90%`. This results in a prorated revenue of `$3,420`.

   The second opportunity, `Quote for 600 Chairs`, has an expected revenue of `$22,500`, and a
   probability of `20%`. This results in a prorated revenue of `$4,500`.

   The combined prorated revenue of the opportunities is `$7,920`, which is listed at the top of the
   column for the month.

   .. screenshot:: sales-crm-forecast-prorated-revenue
      :menu: CRM ‣ Reporting ‣ Forecast
      :shows: One month's column of the Forecast report with its tooltip open, showing the prorated revenue value.
      :highlight: The tooltip value (red frame).
      :data: One month with two opportunities.
      :module: crm
      :notes: English UI, light theme, 1440px width, crop to the column and tooltip.

.. seealso::
   For more information on how probability is assigned to opportunities, see
   :doc:`../track_leads/lead_scoring`

View results
============

Click the :icon:`fa-area-chart` :guilabel:`(area chart)` icon to change to graph view. Then, click
the corresponding icon at the top of the report to switch to a :icon:`fa-bar-chart` :guilabel:`(bar
chart)`, :icon:`fa-line-chart` :guilabel:`(line chart)`, or :icon:`fa-pie-chart` :guilabel:`(pie
chart)`.

.. screenshot:: sales-crm-forecast-pie-chart
   :menu: CRM ‣ Reporting ‣ Forecast
   :shows: The Forecast report displayed as a pie chart, split by sales team.
   :highlight: The pie-chart view button (red frame).
   :data: Two sales teams.
   :module: crm
   :notes: English UI, light theme, 1440px width, crop to the chart and view switcher.

Click the |pivot| to change to the pivot view, or the |list| to change to the list view.

.. tip::
   The :ref:`pivot view <reporting/using-pivot>` can be used to view and analyze data in a more
   in-depth manner. Multiple measures can be selected, and data can be viewed by month, and by
   opportunity stage.

   .. screenshot:: sales-crm-forecast-pivot
      :menu: CRM ‣ Reporting ‣ Forecast
      :shows: The Forecast report in pivot view, with months in the columns, sales teams in the rows and the expected revenue as the measure.
      :highlight: No highlight; the pivot table is the subject.
      :data: Six months, two sales teams.
      :module: crm
      :notes: English UI, light theme, 1440px width, crop to the pivot table.

.. seealso::
   To save this report as a *favorite*, see :ref:`search/favorites`.

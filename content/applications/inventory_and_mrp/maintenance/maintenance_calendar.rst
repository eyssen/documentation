====================
Maintenance calendar
====================

Avoiding equipment breakdowns requires constant equipment maintenance. Timely corrective
maintenance for machines and tools that break unexpectedly, as well as preventive maintenance to
ensure that such issues are avoided, are key to keeping operations running smoothly.

In Odoo *Maintenance*, users can access the *Maintenance Calendar* to create, schedule, and edit
both corrective and preventive maintenance requests, to stay on top of equipment maintenance.

Create maintenance request
==========================

Maintenance requests can be created directly from the *Maintenance Calendar*. To access the
calendar, navigate to :menuselection:`Maintenance app --> Maintenance --> Maintenance Calendar`.

To create a new request, click anywhere on the calendar. Doing so opens a :guilabel:`New Event`
pop-up window. In the :guilabel:`Name:` field, assign a title to the new request.

.. screenshot:: maintenance-calendar-new-event-popup
   :menu: Maintenance ‣ Maintenance Calendar ‣ (click on the calendar)
   :shows: The "New Event" quick-create pop-up window with a "Name:" field and "Create" and
     "Cancel" buttons, plus an "Edit" link.
   :module: maintenance
   :notes: English UI, light theme, 1440px width, crop to the pop-up window.

Clicking :guilabel:`Create` on the pop-up window saves the new request with no additional details.
If the request's creation should be cancelled, click :guilabel:`Cancel`.

To add more details and schedule the request for a specific date and time, click :guilabel:`Edit`.

Clicking :guilabel:`Edit` opens a blank maintenance request form, where various details about the
request can be filled out.

Edit maintenance request
------------------------

In the :guilabel:`Request` field, assign a title to the new request. In the :guilabel:`Created By`
field, from the drop-down menu, select which user the request was created by. By default, this field
populates with the user actually creating the request.

.. screenshot:: maintenance-calendar-new-request-form
   :menu: Maintenance ‣ Maintenance Calendar ‣ (click on the calendar) ‣ Edit
   :shows: A blank maintenance request form with the "Request" and "Created By" fields filled out.
   :module: maintenance
   :notes: English UI, light theme, 1440px width.

Select which machine or tool requires maintenance from the :guilabel:`Equipment` field. Once a
specific piece of equipment is selected, a greyed-out :guilabel:`Category` field appears, listing
the *Equipment Category* to which the equipment belongs.

Under the :guilabel:`Category` field, the :guilabel:`Request Date` field displays the date requested
for the maintenance to happen.

The :guilabel:`Maintenance Type` field provides two selectable radio button options:
:guilabel:`Corrective` and :guilabel:`Preventive`.

:guilabel:`Corrective` maintenance is for requests that arise for immediate needs, such as broken
equipment, while :guilabel:`Preventive` maintenance is for planned requests, to avoid breakdowns in
the future.

From the drop-down menu for the :guilabel:`Team` field, select the desired maintenance team who will
perform the maintenance. In the :guilabel:`Responsible` field, select the technician responsible for
the request.

.. screenshot:: maintenance-calendar-filled-out-form
   :menu: Maintenance ‣ Maintenance Calendar ‣ (click on the calendar) ‣ Edit
   :shows: A maintenance request form filled out with "Equipment", "Category", "Request Date",
     "Maintenance Type" set to "Corrective", "Team", and "Responsible" fields.
   :module: maintenance
   :notes: English UI, light theme, 1440px width.

In the :guilabel:`Scheduled Date` field, click the date to open a calendar popover. From this
popover, select the planned date of the maintenance, and click :guilabel:`Apply` to save the date.

In the :guilabel:`Duration` field, enter the the amount of hours (in a `00:00` format) that the
maintenance is planned to take.

.. tip::
   Ticking the :guilabel:`Recurrent` checkbox, only available for :guilabel:`Preventive`
   maintenance, reveals a :guilabel:`Repeat Every` field, and a :guilabel:`Until` field set to
   :guilabel:`Forever` by default. Use these fields to have Odoo automatically create the next
   occurrence of the request (in a new stage) once the current one is marked as done. Select
   :guilabel:`Until` and pick an :guilabel:`End Date` to stop the recurrence after a specific date.

In the :guilabel:`Priority` field, choose a priority between one and three :guilabel:`⭐⭐⭐ (stars)`.
This indicates the importance of the maintenance request.

If working in a multi-company environment, from the drop-down menu in the :guilabel:`Company` field,
select the company to which this maintenance request belongs.

At the bottom of the form, there are two tabs: :guilabel:`Notes` and :guilabel:`Instructions`.

In the :guilabel:`Notes` tab, type out any internal notes for the team or technician assigned to the
request, if necessary.

In the :guilabel:`Instructions` tab, if necessary, select one of the three radio button options to
provide maintenance instructions to the assigned team or technician. The available methods for
providing instructions are via :guilabel:`PDF`, :guilabel:`Google Slide`, or :guilabel:`Text`.

.. screenshot:: maintenance-calendar-instructions-tab
   :menu: Maintenance ‣ Maintenance Calendar ‣ (request) ‣ Instructions
   :shows: The "Instructions" tab with the "PDF", "Google Slide", and "Text" radio button options,
     and the "Text" option selected with a text-entry field below it.
   :module: maintenance
   :notes: English UI, light theme, 1440px width, crop to the tab.

Calendar elements
=================

The *Maintenance Calendar* provides various views, search functions, and filters to help keep track
of the progress of ongoing and planned maintenance requests.

The following sections describe elements found across various views of the calendar.

Filters and Favorites
---------------------

To access the maintenance calendar, navigate to :menuselection:`Maintenance app --> Maintenance -->
Maintenance Calendar`.

To add and remove filters for sorting data on the *Maintenance Calendar*, click the :guilabel:`🔻
(triangle pointed down)` icon, to the right of the search bar at the top of the page.

The left-hand side of the resulting drop-down menu lists all the different :guilabel:`Filters` users
can select. By default, :guilabel:`To Do` and :guilabel:`Active` are selected, so all open requests
are displayed.

.. tip::
   To add a custom filter to the :guilabel:`Maintenance Calendar`, click :guilabel:`Add Custom
   Filter`, under the :guilabel:`Filters` section of the drop-down menu. This opens an
   :guilabel:`Add Custom Filter` pop-up window.

   From this pop-up window, configure the properties of the new rule for the filter. Once ready,
   click :guilabel:`Add`.

The right-hand side of the drop-down menu lists the :guilabel:`Favorites`, or any searches that have
been saved as a favorite to be revisited at a later date.

.. screenshot:: maintenance-calendar-favorites-popover
   :menu: Maintenance ‣ Maintenance Calendar ‣ 🔻 (filters icon)
   :shows: The filters drop-down menu with the "Filters" column on the left ("To Do" and "Active"
     ticked) and the "Favorites" column on the right.
   :module: maintenance
   :notes: English UI, light theme, 1440px width, crop to the drop-down menu.

To save a new :guilabel:`Favorite` search, select the desired :guilabel:`Filters`. Then, click
:guilabel:`Save current search`. In the field directly below :guilabel:`Save current search`, assign
a name to the search.

Under the assigned name, there are two options, to save the current search either as the
:guilabel:`Default filter`, or as a :guilabel:`Shared` filter.

Selecting :guilabel:`Default filter` sets this filter as the default when opening this calendar
view.

Selecting the :guilabel:`Shared` filter makes this filter available to other users.

Once ready, click :guilabel:`Save`. When clicked, the new :guilabel:`Favorite` filter appears in the
:guilabel:`Favorites` column, and a :guilabel:`⭐ (gold star)` icon appears with the filter's name in
the search bar.

Views
-----

The :guilabel:`Maintenance Calendar` is available in six different views: :guilabel:`Calendar`
(default), :guilabel:`Kanban`, :guilabel:`List`, :guilabel:`Pivot`, :guilabel:`Graph`, and
:guilabel:`Activity`.

.. screenshot:: maintenance-calendar-view-type-icons
   :menu: Maintenance ‣ Maintenance Calendar
   :shows: The row of view-switcher icons in the top-right corner: Calendar, Kanban, List, Pivot,
     Graph, and Activity.
   :module: maintenance
   :notes: English UI, light theme, 1440px width, crop to the icon row.

Calendar view
~~~~~~~~~~~~~

:guilabel:`Calendar` is the default view displayed when the :guilabel:`Maintenance Calendar` is
opened. There are a number of options in this view type for sorting and grouping information about
maintenance requests.

In the top-left corner of the page, there is a drop-down menu set to :guilabel:`Week`, by default.
Clicking that drop-down menu reveals the different periods of time, in which the calendar can be
viewed: :guilabel:`Day`, :guilabel:`Month`, and :guilabel:`Year`. There is also an option to
:guilabel:`Show weekends`, selected by default. If unselected, weekends are not shown on the
calendar.

.. screenshot:: maintenance-calendar-period-dropdown
   :menu: Maintenance ‣ Maintenance Calendar ‣ Week (dropdown)
   :shows: The period drop-down menu with "Day", "Week", "Month", "Year" options, and a "Show
     weekends" checkbox, ticked.
   :module: maintenance
   :notes: English UI, light theme, 1440px width, crop to the drop-down menu.

To the left of this menu, there is a :guilabel:`⬅️ (left arrow)` icon and a :guilabel:`➡️ (right
arrow)` icon. Clicking these arrows moves the calendar backward or forward in time, respectively.

To the right of the drop-down menu set to :guilabel:`Week`, by default, is a :guilabel:`Today`
button. Clicking this button resets the calendar to view today's date, no matter which point in time
is being viewed before clicking it.

At the far-right side of the page is a sidebar column, containing a minimized calendar set to
today's date, and a :guilabel:`Technician` list, displaying all the *Technicians* with requests
currently open. Click the :guilabel:`(panel)` icon at the top of this sidebar to open or close the
sidebar.

.. note::
   The :guilabel:`Technician` list only displays if technicians are assigned to open requests, and
   individual technicians are only listed, if they are listed as :guilabel:`Responsible` on at least
   **one** maintenance request form.

Kanban view
~~~~~~~~~~~

With the :guilabel:`Kanban` view, all open maintenance requests are displayed in Kanban-style
columns, in their respective stages of the maintenance process.

Each maintenance request appears on its own task card, and each task card can be dragged-and-dropped
to a different stage of the Kanban pipeline.

Each column has a name (i.e. :guilabel:`In Progress`). Hovering at the top of a column reveals a
:guilabel:`⚙️ (gear)` icon. Clicking the :guilabel:`⚙️ (gear)` icon reveals a list of options for
that column: :guilabel:`Fold`, :guilabel:`Edit`, :guilabel:`Automations`, and :guilabel:`Delete`.

.. screenshot:: maintenance-calendar-kanban-column
   :menu: Maintenance ‣ Maintenance Calendar ‣ Kanban view
   :shows: The gear-icon menu on a Kanban column, with "Fold", "Edit", "Automations", and "Delete"
     options.
   :module: maintenance
   :notes: English UI, light theme, 1440px width, crop to the column and its menu.

Clicking :guilabel:`Fold` folds the column to hide its contents.

Clicking :guilabel:`Edit` opens an :guilabel:`Edit: (stage name)` pop-up window, with the
corresponding stage name, wherein the column's details can be edited. The following are the column
options that can be edited:

.. screenshot:: maintenance-calendar-edit-stage-popup
   :menu: Maintenance ‣ Maintenance Calendar ‣ Kanban view ‣ (column) ‣ ⚙️ ‣ Edit
   :shows: The "Edit: In Progress" pop-up window with "Name", "Folded in Maintenance Pipe",
     "Sequence", and "Request Done" fields.
   :module: maintenance
   :notes: English UI, light theme, 1440px width, crop to the pop-up window.

- :guilabel:`Name`: the name of the stage in the Kanban pipeline.
- :guilabel:`Folded in Maintenance Pipe`: when checked, this stage's column is folded by default in
  the :guilabel:`Kanban` view type.
- :guilabel:`Sequence`: the order in the maintenance process, in which this stage appears.
- :guilabel:`Request Done`: if ticked, this box indicates this stage is the final step of the
  maintenance process. Requests moved to this stage are closed.

Once ready, click :guilabel:`Save & Close`. If no changes have been made, click :guilabel:`Discard`,
or click the :guilabel:`X` icon to close the pop-up window.

List view
~~~~~~~~~

With the :guilabel:`List` view selected, all open maintenance requests are displayed in a list, with
information about each request listed in its respective row.

The columns of information displayed in this view type are the following:

- :guilabel:`Subjects`: the name assigned to the maintenance request.
- :guilabel:`Created by User`: the user who originally created the maintenance request.
- :guilabel:`Technician`: the technician responsible for the maintenance request.
- :guilabel:`Category`: the category the equipment being repaired belongs to.
- :guilabel:`Stage`: the stage of the maintenance process the request is currently in.
- :guilabel:`Company`: if in a multi-company environment, the company in the database the request is
  assigned to.

.. _maintenance/maintenance_calendar/pivot:

Pivot view
~~~~~~~~~~

With the :guilabel:`Pivot` view selected, maintenance requests are displayed in a pivot table, and
can be customized to show different data metrics.

To add more data to the pivot table, click the :guilabel:`Measures` button to reveal a drop-down
menu. By default, :guilabel:`Count` is selected. Additional options to add to the table are
:guilabel:`Duration` and :guilabel:`Repeat Every`.

.. screenshot:: maintenance-calendar-measures-menu
   :menu: Maintenance ‣ Maintenance Calendar ‣ Pivot view ‣ Measures
   :shows: The "Measures" drop-down menu, with "Count" ticked, and "Duration" and "Repeat Every"
     also listed.
   :module: maintenance
   :notes: English UI, light theme, 1440px width, crop to the drop-down menu.

To the right of the :guilabel:`Measures` button are three buttons:

- :guilabel:`Flip axis`: the x and y axis of the pivot data table flip.
- :guilabel:`Expand all`: all the available rows and columns of the pivot data table expand fully.
- :guilabel:`Download xlsx`: the pivot data table is downloaded as an .xlsx file.

.. _maintenance/maintenance_calendar/graph:

Graph view
~~~~~~~~~~

With the graph view selected, the following options appear between the search bar and visual
representation of the data. These graph-specific options are located to the right of the
:guilabel:`Measures` button.

.. screenshot:: maintenance-calendar-graph-view-icons
   :menu: Maintenance ‣ Maintenance Calendar ‣ Graph view
   :shows: The graph type icons (Bar Chart, Line Chart, Pie Chart) and formatting options (Stacked,
     Descending, Ascending) above the chart.
   :module: maintenance
   :notes: English UI, light theme, 1440px width, crop to the icon row.

There are three different types of graphs available to users to view the data:

- :guilabel:`Bar Chart`: the data is displayed in a bar chart.
- :guilabel:`Line Chart`: the data is displayed in a line chart.
- :guilabel:`Pie Chart`: the data is displayed in a pie chart.

When viewing the data as a :guilabel:`Bar Chart` graph, the data can be formatted in the following
ways:

- :guilabel:`Stacked`: the data is stacked on the graph.
- :guilabel:`Descending`: the data is displayed in descending order.
- :guilabel:`Ascending`: the data is displayed in ascending order.

When viewing the data as a :guilabel:`Line Chart` graph, the data can be formatted in the following
ways:

- :guilabel:`Stacked`: the data is stacked on the graph.
- :guilabel:`Cumulative`: the data is increasingly accumulated.
- :guilabel:`Descending`: the data is displayed in descending order.
- :guilabel:`Ascending`: the data is displayed in ascending order.

When viewing the data as a :guilabel:`Pie Chart` graph, all relevant data is displayed by default,
and no additional formatting options are available.

Activity view
~~~~~~~~~~~~~

With the :guilabel:`Activity` view selected, all open maintenance requests are listed in their own
row, with the ability to schedule activities related to those requests.

.. screenshot:: maintenance-calendar-activity-view-type
   :menu: Maintenance ‣ Maintenance Calendar ‣ Activity view
   :shows: Maintenance requests listed in rows under the Activity view, with activity columns
     across the top and a "+ Schedule an activity" icon on one row.
   :module: maintenance
   :notes: English UI, light theme, 1440px width.

Maintenance requests are listed in the :guilabel:`Maintenance Request` column as activities.
Clicking a request opens a :guilabel:`Maintenance Request` popover that indicates the status of the
request, and the responsible technician. To schedule an activity directly from the popover, click
:guilabel:`➕ Schedule an activity`. This opens a :guilabel:`Schedule Activity` pop-up window.

From the pop-up window, choose the :guilabel:`Activity Type`, provide a :guilabel:`Summary`,
schedule a :guilabel:`Due Date`, and choose the responsible user in the :guilabel:`Assigned to`
field.

.. screenshot:: maintenance-calendar-schedule-activity-popover
   :menu: Maintenance ‣ Maintenance Calendar ‣ Activity view ‣ (request) ‣ Schedule an activity
   :shows: The "Schedule Activity" pop-up window with "Activity Type", "Summary", "Due Date", and
     "Assigned to" fields.
   :module: maintenance
   :notes: English UI, light theme, 1440px width, crop to the pop-up window.

Type any additional notes for the new activity in the blank space under the greyed-out
:guilabel:`Log a note...` field. When clicked, this changes to :guilabel:`Type "/" for commands`.

Once ready, click :guilabel:`Schedule` to schedule the activity. Alternatively, click
:guilabel:`Schedule & Mark as Done` to close the activity, click :guilabel:`Done & Schedule Next` to
close the activity and open a new one, or click :guilabel:`Cancel` to cancel the activity.

With the :guilabel:`Activity` view selected, each activity type available when scheduling an
activity is listed as its own column. These columns include, by default, :guilabel:`Email`,
:guilabel:`Call`, :guilabel:`Meeting`, :guilabel:`Maintenance Request`, :guilabel:`To-Do`, and
:guilabel:`Upload Document`.

To schedule an activity with that specific activity type, click into any blank box on the
corresponding row for the desired maintenance request, and click the :guilabel:`➕ (plus)` icon. This
opens an :guilabel:`Odoo` pop-up window, wherein the activity can be scheduled.

.. screenshot:: maintenance-calendar-odoo-activity-popup
   :menu: Maintenance ‣ Maintenance Calendar ‣ Activity view ‣ (blank activity cell) ‣ ➕
   :shows: The "Odoo" pop-up window used to quickly schedule an activity of a given type from the
     Activity view.
   :module: maintenance
   :notes: English UI, light theme, 1440px width, crop to the pop-up window.

.. seealso::
   - :doc:`maintenance_requests`
   - :doc:`add_new_equipment`

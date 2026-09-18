============
Logging time
============

Besides the standard list, grid, and Kanban views, time can be recorded and reviewed in a calendar,
and it can be attached to the activities of the :doc:`Activities
</applications/essentials/activities>` app.

.. _timesheets/calendar-view:

Calendar view
=============

The timesheet lists offer a :icon:`fa-calendar` :guilabel:`Calendar` view, which opens by default
on :menuselection:`Timesheets --> Timesheets --> All Timesheets` and on the timesheets of a
project. Entries are placed on the day they were logged, sized by the time spent, and colored by
project.

Use the :guilabel:`Month`, :guilabel:`Week`, and :guilabel:`Day` scales to see a whole month at a
glance or a single day in detail, and the side panel to filter by :guilabel:`Employee`,
:guilabel:`Project`, :guilabel:`Task`, or :guilabel:`User`. The total of the displayed time is
shown with the entries, and an entry with an impossible duration — more than 24 hours, or a
negative one — is highlighted, which makes mistyped entries easy to spot.

The timesheet analysis report can be displayed in the same way, so the recorded costs and hours can
be reviewed per employee on a calendar.

.. note::
   The calendar views are provided by the *Timesheet Calendar View*
   (`timesheet_view_calendar`) module.

.. screenshot:: services-timesheets-calendar-view
   :menu: Timesheets ‣ Timesheets ‣ All Timesheets ‣ (Calendar view)
   :shows: The timesheet calendar in month mode, with entries of several projects in different colors and the filter panel open on Employee and Project.
   :highlight: The view switcher and the Month/Week/Day scales (red frame).
   :data: About fifteen timesheet entries across two projects and three employees in one month.
   :module: timesheet_view_calendar
   :notes: English UI, light theme, 1440px width, crop to the calendar and the side panel.

.. _timesheets/activities:

Time spent on activities
========================

Timesheet entries can be linked to an :guilabel:`Activity`, so that the time spent on a planned
piece of work is recorded against that activity rather than only against the task. Each entry can
additionally carry a :guilabel:`Start Date` and an :guilabel:`End Date`, which is useful when the
exact interval matters, for example for interventions billed by the hour.

The activity then shows:

- :guilabel:`Allocated Hours` – the sum of the time logged on it;
- :guilabel:`Remaining Hours` – the estimated hours of the activity minus the time already logged.

Both are kept up to date automatically as entries are added or changed, which turns the activity
list into a live comparison of the estimate against the work actually done.

.. note::
   - This feature is provided by the *Activities - Timesheets* (`activity_timesheet`) module and
     requires the *Activities* (`activity`) module.
   - Deleting an activity does not delete the time logged on it; the entries simply lose their
     link, so the recorded hours are never lost.

.. screenshot:: services-timesheets-activity-hours
   :menu: Activities ‣ (open an activity)
   :shows: An activity showing its Estimated Hours, the computed Allocated Hours and Remaining Hours, and the list of linked timesheet entries.
   :highlight: The Allocated Hours and Remaining Hours fields (red frame).
   :data: Activity "Prepare the annual audit", estimated 8 h, 5 h logged over two entries.
   :module: activity_timesheet, activity
   :notes: English UI, light theme, 1440px width, crop to the activity form.

.. seealso::
   :doc:`services`

==========
Activities
==========

The **Activities** app extends the :doc:`activities <../essentials/activities>` scheduled on records
with a dedicated board, reminders, recurring activities, and a 360° history per customer.

.. note::
   The app is provided by the *Activities* (``activity``) module, with bridge modules for the other
   apps: *Activities - CRM* (``activity_crm``), *Activities - Repair* (``activity_repair``),
   *Activities - Calendar* (``activity_calendar``).

Access rights
=============

The :guilabel:`Activities` category of the :ref:`access rights <access-rights/users>` offers three
levels:

- :guilabel:`User`: sees and manages their own activities;
- :guilabel:`Supervisor`: additionally sees the activities they supervise;
- :guilabel:`Manager`: sees all activities and configures the app.

The activity board
==================

The app groups the activities of the database in a single place:

- :menuselection:`Activities --> My Activities`: the activities assigned to the user;
- :menuselection:`Activities --> Supervised Activities`: the activities whose
  :guilabel:`Supervisor` is the user;
- :menuselection:`Activities --> All Activities`: every activity (managers only).

Besides the standard fields, an activity carries a :guilabel:`Supervisor`, :guilabel:`Tags`, a
:guilabel:`Priority`, a :guilabel:`Feedback` and, when it is cancelled, a :guilabel:`Cancel Reason`.
Its status is shown as :guilabel:`Overdue`, :guilabel:`Today`, :guilabel:`Planned`,
:guilabel:`Done`, or :guilabel:`Cancelled`.

.. screenshot:: productivity-activities-board
   :menu: Activities ‣ My Activities
   :shows: The activity board listing activities with their document, type, due date, supervisor, tags and status.
   :data: Demo company "YourCompany HU"; activities on opportunities and sales orders, one overdue.
   :module: activity
   :notes: English UI, light theme, 1440px width.

Multiple assignees
------------------

When :guilabel:`Multiple Assignees` is enabled in :menuselection:`Settings --> Activities`, an
activity can be assigned to several users at once. Each of them then gets their own copy of the
activity, so everyone can complete their part separately.

Tags
----

Tags classify activities across models. Manage them in :menuselection:`Activities --> Configuration
--> Tags`, where each tag has a :guilabel:`Name` and a :guilabel:`Color`.

Reminders
=========

A **reminder** notifies the assignee before the activity is due. Create reminders in
:menuselection:`Activities --> Configuration --> Reminders`, with a :guilabel:`Type`
(e-mail or notification), a :guilabel:`Remind Before` value and its :guilabel:`Reminder Unit`, and
optionally a :guilabel:`Custom Notification Template`. Then add the reminders to an activity in its
:guilabel:`Alarms` field.

Reminders are sent by a scheduled action, and only when :guilabel:`Activity Reminders` is enabled in
:menuselection:`Settings --> Activities`.

Due date notifications
----------------------

In :menuselection:`Settings --> Activities`, the :guilabel:`Due Activity Notifications` block sends
daily mails around the due date of the activities: on the due date, one or two notices before it,
and one or two notices after it, each with the number of days to apply. Each notice can also be
copied to the user who created the activity.

:guilabel:`Overdue Activity Escalation` notifies the supervisor when an activity stays overdue
longer than the configured number of days.

.. screenshot:: productivity-activities-settings
   :menu: Settings ‣ Activities
   :shows: The Activities settings with the "Activity Board" block (Multiple Assignees, Activity Reminders) and the "Due Date Notifications" block with its day fields.
   :highlight: The "Due Date Notifications" block (red frame).
   :module: activity
   :notes: English UI, light theme, 1440px width.

Recurring activities
====================

A recurring activity recreates itself on a schedule. Configure them in
:menuselection:`Activities --> Configuration --> Recurring Activities`:

- :guilabel:`Repeat Every`: the interval and its unit;
- the days of the week, the :guilabel:`Date of Month`, or the month, depending on the recurrence
  type chosen;
- :guilabel:`Repeat` or :guilabel:`End Date`: how the recurrence ends;
- the :guilabel:`Summary`, :guilabel:`Description`, :guilabel:`Tags`, the assignee, and the
  :guilabel:`Supervisor` given to each generated activity;
- :guilabel:`Start After Days`: the delay before the first activity is created.

Activity history
================

:menuselection:`Activities --> Activity History` gives a 360° view of every activity — open and
completed — with its :guilabel:`Customer`, :guilabel:`Company`, :guilabel:`Assigned To`,
:guilabel:`Supervisor`, :guilabel:`Activity Type`, :guilabel:`Due Date`, :guilabel:`Summary`, and
:guilabel:`Feedback`. The same history is available from a contact, in
:menuselection:`Contacts --> Activity History`.

Reporting
---------

:guilabel:`My Reporting` and :guilabel:`Reporting` analyze the activities of the user, or of
everyone, by type, assignee, supervisor, or period.

Deletion log
============

Every deleted activity leaves a trace in :menuselection:`Activities --> Configuration --> Deletion
Log`, with the document it belonged to, its summary, its assignee, its due date, who deleted it,
when, and the :guilabel:`Removal Reason`. This makes it possible to see what was planned on a record
even after the activity is gone.

.. note::
   In a multi-company database, the *Activity Multi-Company Fix* (``activity_multicompany``) module
   prevents access errors on activities belonging to another company.

.. seealso::
   :doc:`../essentials/activities`

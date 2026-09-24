==========
Activities
==========

.. |clock| replace:: :icon:`fa-clock-o` :guilabel:`(clock)` icon

*Activities* are follow-up tasks tied to a record in an Odoo database.

.. _activities/important:

The icon used to display activities varies, depending on the :ref:`activity type
<activities/types>`:

- :icon:`fa-clock-o` :guilabel:`(clock)` icon: the default activities icon.
- :icon:`fa-phone` :guilabel:`(phone)` icon: a phone call is scheduled.
- :icon:`fa-envelope` :guilabel:`(envelope)` icon: an email is scheduled.
- :icon:`fa-check` :guilabel:`(check)` icon: a "to-do" is scheduled.
- :icon:`fa-users` :guilabel:`(people)` icon: a meeting is scheduled.
- :icon:`fa-upload` :guilabel:`(upload)` icon: a document is scheduled to be uploaded.

Schedule activities
===================

Activities can be scheduled on any page of the database that contains a :ref:`chatter
<activities/chatter>` thread, :ref:`Kanban view <activities/kanban>`, :ref:`list view
<activities/list>`, or :ref:`activities view <activities/activity>` of an application.

.. _activities/chatter:

Chatter
-------

Activities can be created from the chatter on any record.

To schedule a new activity, click the :guilabel:`Activities` button, located at the top of the
chatter. In the :guilabel:`Schedule Activity` pop-up window that appears, :ref:`fill out the
Schedule Activity form <activities/form>`.

.. screenshot:: essentials-activities-chatter
   :menu: CRM ‣ (any opportunity) ‣ chatter
   :shows: Top of the chatter with the "Activities" button, and the Schedule Activity dialog opened
      from it.
   :highlight: The "Activities" button.
   :data: Demo opportunity "Office Design Project".
   :module: mail, crm
   :notes: English UI, 1440px width, crop to the chatter and the dialog.

.. _activities/kanban:

Kanban view
-----------

Activities can also be created from the :icon:`oi-view-kanban` :guilabel:`(Kanban)` view.

To do so, click on the |clock| located at the bottom of an individual record.

Click :guilabel:`+ Schedule An Activity`, then proceed to :ref:`fill out the Schedule Activity form
<activities/form>`.

.. screenshot:: essentials-activities-kanban
   :menu: CRM ‣ Sales ‣ My Pipeline (Kanban view)
   :shows: Kanban card with the clock icon clicked; the popover lists planned activities and shows
      "+ Schedule An Activity".
   :highlight: The clock icon and "+ Schedule An Activity".
   :data: Demo pipeline.
   :module: mail, crm
   :notes: English UI, crop to one column and the popover.

.. note::
   If a record already has a scheduled activity, the |clock| is replaced by the icon that represents
   the existing scheduled activity. Click on the activity type's icon to schedule another activity.

.. _activities/list:

List view
---------

Activities can also be created from a :icon:`oi-view-list` :guilabel:`(list)` view.

If the :guilabel:`Activities` column is hidden, reveal it using the :icon:`oi-settings-adjust`
:guilabel:`(settings adjust)` icon in the far-right of the top row.

Then, click on the |clock| for the record the activity is being added to, and click :guilabel:`+
Schedule an activity`. Proceed to :ref:`fill out the Schedule Activity form <activities/form>` that
appears.

.. note::
   If a record already has a scheduled activity, the |clock| is replaced by the icon that represents
   the existing scheduled activity. Click on the activity type's icon to schedule another activity.

.. screenshot:: essentials-activities-list
   :menu: CRM ‣ Sales ‣ My Pipeline (List view)
   :shows: List view with the Activities column; the clock icon of one row is clicked and the
      popover with "+ Schedule An Activity" is open.
   :highlight: The Activities column.
   :data: Demo pipeline.
   :module: mail, crm
   :notes: English UI, crop to the list and the popover.

.. _activities/activity:

Activity view
-------------

Most applications in Odoo have an *Activity* view available. If available, a |clock| is visible in
the top-right corner of the main menu bar, amongst the other view option icons.

To open the activity view, click the |clock|.

.. screenshot:: essentials-activities-view-switcher
   :menu: CRM ‣ Sales ‣ My Pipeline
   :shows: View switcher in the top-right corner of the control panel (Kanban, List, Calendar,
      Pivot, Graph, Map/other, Activity icons).
   :highlight: The Activity view (clock) icon.
   :module: mail, crm
   :notes: English UI, crop tightly to the view switcher.

In this view, all the available activities are listed in the columns, while the horizontal entries
represent all the individual records.

Activities that appear green have a due date in the future, activities that appear orange are due
today, while activities appearing red are overdue.

Color bars in each column represent records for specific activity types, and display a number
indicating how many activities are scheduled for that type.

If multiple activity types are scheduled for a record, a number appears in the box, indicating the
total number of scheduled activities.

.. note::
   Activity colors, and their relation to an activity's due date, are consistent throughout Odoo,
   regardless of the activity type, or the view.

To schedule an activity for a record, hover over the corresponding field. Click the :icon:`fa-plus`
:guilabel:`(plus)` icon that appears, and then :ref:`fill out the Schedule Activity form
<activities/form>`.

.. screenshot:: essentials-activities-activity-view
   :menu: CRM ‣ Sales ‣ My Pipeline ‣ Activity view
   :shows: Activity view grid: activity types as columns, records as rows, colored cells for late /
      today / planned activities; the mouse hovers an empty cell showing the plus icon.
   :highlight: The plus icon in the hovered cell.
   :data: Demo pipeline with several activities.
   :module: mail, crm
   :notes: English UI, 1440px width.

.. _activities/form:

Schedule Activity form
----------------------

Activities can be scheduled from many different places, such as from the :ref:`chatter
<activities/chatter>` of a record, or from one of multiple views in an application, when available:
the :ref:`Kanban view <activities/kanban>`, :ref:`list view <activities/list>`, or :ref:`activity
view <activities/activity>`.

Enter the following information on the form:

- :guilabel:`Plan`: optionally, select an :ref:`activity plan <activities/plans>` to schedule
  several predefined activities at once instead of a single activity. When a plan is selected, set
  the :guilabel:`Plan Date` the activities' deadlines are computed from and, if the plan requires
  it, the user to assign them to. This field only appears if at least one activity plan exists for
  the record's model.
- :guilabel:`Activity Type`: select the type of activity from the drop-down menu. The default
  options are: :guilabel:`Email`, :guilabel:`Call`, :guilabel:`Meeting`, or :guilabel:`To-Do`.
  Depending on what other applications are installed, additional options may be available.
- :guilabel:`Summary`: enter a short title for the activity, such as `Discuss Proposal`.
- :guilabel:`Due Date`: using the calendar popover, select the activity's deadline.
- :guilabel:`Assigned to`: by default, the current user populates this field. To assign a different
  user to the activity, select them from the drop-down menu.
- :guilabel:`Notes`: add any additional information for the activity in this field.

When the :guilabel:`Schedule Activity` pop-up window is completed, click one of the following
buttons:

- :guilabel:`Open Calendar`: opens the user's calendar to add and schedule the activity.

  Click on the desired date and time for the activity, and a :guilabel:`New Event` pop-up window
  appears. The summary from the *Schedule Activity* pop-up window populates the :guilabel:`Title`
  field.

  Enter the information in the :guilabel:`New Event` pop-up window, then click :guilabel:`Save &
  Close` to schedule it. Once scheduled, the activity is added to the chatter under the
  :guilabel:`Planned Activities` section.

  .. important::
    The :guilabel:`Open Calendar` button **only** appears if the :guilabel:`Activity Type` is set
    to either :guilabel:`Call` or :guilabel:`Meeting`.

- :guilabel:`Schedule`: schedules the activity, and adds the activity to the chatter under
  :guilabel:`Planned Activities`.
- :guilabel:`Schedule & Mark as Done`: adds the details of the activity to the chatter under
  :guilabel:`Today`. The activity is not scheduled, and is automatically marked as done.
- :guilabel:`Done & Schedule Next`: adds the details of the activity to the chatter under
  :guilabel:`Today`. The activity is not scheduled, is automatically marked as done, and a new
  :guilabel:`Schedule Activity` pop-up window appears.
- :guilabel:`Cancel`: discards any changes made on the :guilabel:`Schedule Activity` pop-up window.

.. screenshot:: essentials-activities-schedule-form
   :menu: CRM ‣ (any opportunity) ‣ Activities ‣ Schedule Activity
   :shows: Schedule Activity dialog with Plan, Activity Type, Summary, Due Date, Assigned to and
      the note editor; buttons Schedule, Schedule & Mark as Done, Done & Schedule Next, Open
      Calendar (Activity Type "Meeting"), Cancel.
   :highlight: The button row.
   :data: Activity Type "Meeting", Summary "Discuss proposal".
   :module: mail, calendar, crm
   :notes: English UI, crop to the dialog.

.. _activities/all:

All scheduled activities
========================

To view a consolidated list of activities, organized by application, click the |clock| in the header
menu, located in the top-right corner.

If any activities are scheduled, the number of activities appear in a red bubble on the
|clock|.

All activities for each application are further divided into subsections, indicating where in the
application the activity is to be completed. Each sub-section lists the number of scheduled
activities that are :guilabel:`Late`, due :guilabel:`Today`, and scheduled in the
:guilabel:`Future`.

.. example::
   In the *Time Off* application, one activity is scheduled to be done in the *All Time Off*
   requests dashboard, and six activities are scheduled to be done in the *Allocations* dashboard.

   These requests appear in two separate lists in the all activities drop-down menu: one labeled
   `Time Off` and one labeled `Time Off Allocation`.

   .. screenshot:: essentials-activities-systray
      :menu: Top menu bar ‣ clock icon
      :shows: The activities dropdown of the top menu bar, with the counters per model and the Late /
         Today / Future counts; the "Time Off" and "Time Off Allocation" entries are visible.
      :highlight: The two Time Off entries.
      :data: One time off request and six allocation requests waiting for approval.
      :module: mail, hr_holidays
      :notes: English UI, crop to the dropdown.

.. _activities/types:

Activity types
==============

To view the currently configured types of activities in the database, navigate to
:menuselection:`Settings app --> Discuss section --> Activities setting --> Activity Types`.

.. screenshot:: essentials-activities-settings
   :menu: Settings ‣ General Settings ‣ Discuss
   :shows: The Discuss section of the settings with the "Activities" setting and its "Activity
      Types" link.
   :highlight: The "Activity Types" link.
   :module: mail
   :notes: English UI, crop to the Discuss section.

Doing so reveals the :guilabel:`Activity Types` page, where the existing activity types are found.

.. tip::
   Individual applications have a list of *Activity Types* dedicated to that application. For
   example, to view and edit the activities available for the *CRM* application, go to
   :menuselection:`CRM app --> Configuration --> Activity Types`.

.. screenshot:: essentials-activities-types-list
   :menu: Settings ‣ General Settings ‣ Discuss ‣ Activity Types
   :shows: List of the existing activity types (Email, Call, Meeting, To-Do, Upload Document, …).
   :module: mail
   :notes: English UI, crop to the list.

Edit activity types
-------------------

To edit an existing :ref:`activity type <activities/types>`, click on the activity type, and the
activity type form loads.

Make any desired changes to the activity type form. The form automatically saves, but it can be
saved manually at any time by clicking the :guilabel:`Save Manually` option, represented by a
:icon:`fa-cloud-upload` :guilabel:`(cloud upload)` icon, located in the top-left corner of the page.

Create new activity types
-------------------------

To create a new :ref:`activity type <activities/types>`, click :guilabel:`New` from the
:guilabel:`Activity Types` page, and a blank activity type form loads.

Enter a :guilabel:`Name` for the activity type at the top of the form, then enter the following
information on the form.

Activity Settings section
~~~~~~~~~~~~~~~~~~~~~~~~~

- :guilabel:`Action`: Using the drop-down menu, select an action associated with this new activity
  type. Some actions trigger specific behaviors after an activity is scheduled, such as:

  - :guilabel:`Upload Document`: If selected, a link to upload a document is automatically added to
    the planned activity in the chatter. Uploading the document marks the activity as done.
  - :guilabel:`Phonecall` or :guilabel:`Meeting`: If selected, users have the option to open their
    calendar to select a date and time for the activity. The :guilabel:`Meeting` action requires
    the **Calendar** app.

  .. note::
     Available activity types vary based on the installed applications in the database.

- :guilabel:`Model`: optionally, restrict the activity type to a specific model, e.g.,
  :guilabel:`Lead/Opportunity`. If left empty, the activity type is available on all records.
- :guilabel:`Default User`: Select a user from the drop-down menu to automatically assign this
  activity to the selected user when this activity type is scheduled. If this field is left blank,
  the activity is assigned to the user who creates the activity.
- :guilabel:`Default Summary`: enter a note to include whenever this activity type is created.

  .. note::
     The information in the :guilabel:`Default User` and :guilabel:`Default Summary` fields are
     included when an activity is created. However, they can be altered before the activity is
     scheduled or saved.

- :guilabel:`Keep Done`: Tick this checkbox to keep activities that have been marked as `Done`
  visible in the :ref:`activity view <activities/activity>`.
- :guilabel:`Default Note`: enter any notes to appear with the activity.
- :guilabel:`Email templates`: select the email templates that can be used with this activity type.
  They are proposed as quick actions on the planned activity in the chatter.

Next Activity section
~~~~~~~~~~~~~~~~~~~~~

It is possible to have another activity either suggested or triggered. To do so, configure the
:guilabel:`Next Activity` section.

- :guilabel:`Chaining Type`: select either :guilabel:`Suggest Next Activity` or :guilabel:`Trigger
  Next Activity` from the drop-down menu. Depending on the selected option, either the
  :guilabel:`Suggest` or :guilabel:`Trigger` field is displayed.

  .. note::
     The :guilabel:`Chaining Type` field does **not** appear if :guilabel:`Upload Document` is
     selected for the :guilabel:`Action`.

- :guilabel:`Suggest/Trigger`: depending on what is selected for the :guilabel:`Chaining Type`, this
  field either displays :guilabel:`Suggest` or :guilabel:`Trigger`. Using the drop-down menu, select
  the activity to recommend or schedule as a follow-up task to the activity type.
- :guilabel:`Schedule`: configure when the next activity is suggested or triggered.

  First, enter a numerical value indicating when the activity is suggested or triggered.

  Next to this field, a :guilabel:`Days` field is visible. Click :guilabel:`Days`, the default
  option, to reveal a drop-down menu. Select the desired time-frame option from the list. The
  options are :guilabel:`Days`, :guilabel:`Weeks`, or :guilabel:`Months`.

  Lastly, using the drop-down menu, select whether the activity is scheduled or triggered either
  :guilabel:`after previous activity deadline` or :guilabel:`after completion date`.

.. screenshot:: essentials-activities-type-form
   :menu: Settings ‣ General Settings ‣ Discuss ‣ Activity Types ‣ New
   :shows: Completed activity type form: Name, Action, Default User, Default Summary, Keep Done,
      Default Note, and the Next Activity section with Chaining Type, Trigger and Schedule.
   :data: Activity type "Follow-up call", Action "Phonecall", triggers "Email" 2 days after
      completion date.
   :module: mail
   :notes: English UI, crop to the form sheet.

.. _activities/plans:

Activity plans
==============

*Activity plans* are predefined sets of activities that can be scheduled on a record in one go,
e.g., an onboarding checklist, or the standard follow-up steps of a new opportunity.

To manage activity plans, go to the :guilabel:`Configuration` menu of an app that supports them,
e.g., :menuselection:`CRM --> Configuration --> Activity Plans`, :menuselection:`Sales -->
Configuration --> Activity Plans`, or :menuselection:`Project --> Configuration --> Activity
Plans`. With :ref:`developer mode <developer-mode>` activated, all plans are also available under
:menuselection:`Settings --> Technical --> Activities --> Activity Plans`.

Click :guilabel:`New`, enter the :guilabel:`Plan Name`, select the :guilabel:`Model` the plan
applies to (if the field is displayed), then add one line per activity in the :guilabel:`Activities
To Create` tab:

- :guilabel:`Activity Type` and :guilabel:`Summary`: the activity to create.
- :guilabel:`Assignment`: :guilabel:`Ask at launch` to choose the responsible user when the plan is
  scheduled, or :guilabel:`Default user` to always assign the activity to the user selected in the
  :guilabel:`Assigned to` field.
- :guilabel:`Interval`, :guilabel:`Unit`, and :guilabel:`Trigger`: when the activity's deadline is
  set, relative to the plan date (:guilabel:`Before Plan Date` or :guilabel:`After Plan Date`).

To launch a plan, open the :ref:`Schedule Activity form <activities/form>` on a record, select the
plan in the :guilabel:`Plan` field, set the :guilabel:`Plan Date`, and click :guilabel:`Schedule`.
A summary of the activities to be created is displayed in the form before scheduling.

.. screenshot:: essentials-activities-plan-form
   :menu: CRM ‣ Configuration ‣ Activity Plans ‣ New
   :shows: Activity plan form with Plan Name and the "Activities To Create" tab listing three lines
      (activity type, summary, assignment, interval, unit, trigger).
   :data: Plan "New opportunity follow-up": Call after 1 day, Email after 3 days, Meeting after 7 days.
   :module: mail, crm
   :notes: English UI, crop to the form sheet.

.. seealso::
   - :doc:`../productivity/discuss`
   - :doc:`../productivity/discuss/team_communication`
   - :doc:`../sales/crm/optimize/utilize_activities`

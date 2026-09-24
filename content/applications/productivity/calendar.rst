:show-content:

========
Calendar
========

Odoo **Calendar** is a scheduling app that allows users to integrate a company's business flow into
a single management platform. By integrating with the other apps in Odoo's ecosystem, **Calendar**
allows users to schedule and organize meetings, schedule events, plan performance reviews,
coordinate projects, and more – all from the same platform.

Upon opening the :menuselection:`Calendar app`, users have an overview of their current meetings.
The selected view option appears as a :guilabel:`Day`, :guilabel:`Week`, :guilabel:`Month`, or
:guilabel:`Year` drop-down menu. Under the view options drop-down menu, users can also enable or
disable :guilabel:`Show weekends`.

.. screenshot:: productivity-calendar-overview
   :menu: Calendar
   :shows: The Calendar app in Week view with several meetings, the view selector (Day, Week, Month, Year) and the Today button.
   :data: Demo company "YourCompany HU"; a few meetings spread over the week.
   :module: calendar
   :notes: English UI, light theme, 1440px width.

.. tip::
   Depending on the selected view option, users can click the :icon:`oi-arrow-left`
   :icon:`oi-arrow-right` :guilabel:`(left or right arrow)` buttons to switch between days, weeks,
   etc., and switch back to the current day with the :guilabel:`Today` button.

Sync third-party calendars
--------------------------

Users can sync Odoo with existing :doc:`Outlook <calendar/outlook>` and/or
:doc:`Google <calendar/google>` calendars, by heading to
:menuselection:`Calendar app --> Configuration --> Settings`. From here, enter
:guilabel:`Client ID` and :guilabel:`Client Secret`. There is also an option to pause
synchronization by ticking the checkbox, or automating synchronization by keeping it blank.

Once the desired configurations are complete, be sure to click :guilabel:`Save` before moving on.

Events created in synced calendars automatically appear across the integrated platforms.

.. seealso::
   - :doc:`Synchronize Outlook calendar with Odoo <calendar/outlook>`
   - :doc:`Synchronize Google calendar with Odoo <calendar/google>`

Create activities from chatter
------------------------------

Instantly create new meetings anywhere in Odoo through an individual record's chatter, like
in a **CRM** opportunity card or task in the **Projects** app.

From the chatter, click on the :guilabel:`Activities` button. In the :guilabel:`Schedule Activity`
pop-up window, select the desired :guilabel:`Activity Type`, which populates a set of buttons,
depending on the activity.

Activities that involve other schedules, like :guilabel:`Meeting` or :guilabel:`Call for Demo`, link
to the **Calendar** app. Select one of these activities to link to the **Calendar** app, then hit
:guilabel:`Open Calendar` to navigate back to the app. Alternatively, it is also possible to
:guilabel:`Schedule & Mark as Done` to close out the activity, or select :guilabel:`Done & Schedule
Next` to keep the :guilabel:`Schedule Activity` window open to create another.

.. seealso::
   :doc:`Schedule activities in Odoo <../essentials/activities>`

Plan an event
-------------

To put an event on the calendar, open the :menuselection:`Calendar app`, and click into the target
date. On the :guilabel:`New Event` pop-up window that appears, start by adding the event title.

.. screenshot:: productivity-calendar-new-event-popup
   :menu: Calendar
   :shows: The "New Event" pop-up window opened by clicking a date, with the title, the Start field, the All Day checkbox, the Attendees field and the Videocall URL field.
   :highlight: The "Videocall URL" field and the "Odoo meeting" link (red frame).
   :data: Event "Project kick-off" on the current week.
   :module: calendar
   :notes: English UI, light theme, crop to the pop-up.

The target date auto-populates in the :guilabel:`Start` field. This can be changed by clicking
into the date section, and selecting a date from the calendar. For multi-day events, select the end
date in the second field, then click :guilabel:`Apply`.

Tick the :guilabel:`All Day` checkbox if there is no specific start or end time.

For events with specific start and stop times, ensure the :guilabel:`All Day` checkbox is unticked
to enable time selection. With the :guilabel:`All Day` checkbox unticked, time selections appear in
the :guilabel:`Start` field.

The signed-in user auto-populates as the first attendee. Additional :guilabel:`Attendees` can be
added or created from here, as well.

For virtual meetings, copy and paste the URL into the space provided in the
:guilabel:`Videocall URL` field. Or, click :icon:`fa-plus` :guilabel:`Odoo meeting` to create a
link.

Next, either create the event by clicking :guilabel:`Save & Close`, or select :guilabel:`More
Options` to further configure the event.

.. tip::
   Once the event is created, users can click into the virtual meeting directly from the calendar
   event to access more configuration options.

.. screenshot:: productivity-calendar-event-form
   :menu: Calendar
   :shows: The full meeting form opened with "More Options", showing Duration, Recurrent, Tags, Privacy, Organizer, Description and Reminders.
   :data: Meeting "Project kick-off" with two attendees and a 1-hour duration.
   :module: calendar
   :notes: English UI, light theme, 1440px width.

The :guilabel:`Description` field allows users to add additional information and details about the
meeting.

Click :guilabel:`More Options` to navigate to the meeting form, which provides additional
configurations for the event:

- :guilabel:`Duration`: Define the length of the meeting in :guilabel:`hours`, or toggle the
  :guilabel:`All Day` switch.
- :guilabel:`Recurrent`: Tick the checkbox to create a recurring meeting. Once selected, this
  opens new fields:

  - :guilabel:`Timezone`: Select the timezone for which this meeting time is specified.
  - :guilabel:`Repeat`: Select the recurring period of this meeting. Depending on what type of
    recurrence has been selected, a subsequent field appears, in which users can indicate when the
    meeting should recur. For example, if :guilabel:`Monthly` is selected as the :guilabel:`Repeat`
    option, a new field appears, in which the user decides on what :guilabel:`Day of Month` the
    meeting should recur.
  - :guilabel:`Until`: Select the limited :guilabel:`Number of repetitions` this meeting should
    recur, the :guilabel:`End date` of when the recurrences should stop, or if the meetings should
    recur :guilabel:`Forever`.
- :guilabel:`Tags`: Add tags to the event, like `Customer Meeting` or `Internal Meeting`. These can
  be searched and filtered in the **Calendar** app when organizing multiple events.
- :guilabel:`Appointment`: Link existing or new appointments. These can be configured through the
  :ref:`Share Availabilities <calendar/share-availabilities>` button from the main **Calendar**
  dashboard.
- :guilabel:`Privacy`: Toggle between visibility options to control who can view the event.
- :guilabel:`Organizer`: This is defaulted to the current Odoo user. Select a new one from
  existing users, or create and edit a new user.
- :guilabel:`Description`: Add additional information or details about the meeting.
- :guilabel:`Reminders`: Select notification options to send to attendees. Choose a default
  notification, or configure new reminders.

Coordinate with teams' availability
-----------------------------------

When scheduling an event for multiple users, on the **Calendar** app dashboard, tick the checkbox
next to :guilabel:`Attendees` to view team members' availability. Tick (or untick) the checkbox next
to listed users to show (or hide) individual calendars.

.. screenshot:: productivity-calendar-attendees
   :menu: Calendar
   :shows: The Calendar dashboard with the Attendees section in the side panel, listing team members with their checkboxes, and their events shown in the calendar.
   :highlight: The "Attendees" list (red frame).
   :data: Three internal users with meetings in the current week.
   :module: calendar
   :notes: English UI, light theme, 1440px width.

.. _calendar/share-availabilities:

Share availabilities
--------------------

To let customers or colleagues book a slot in your calendar themselves, use the
:doc:`Appointments app <appointments>`: it publishes the bookable slots, applies the booking rules,
and creates the calendar event of the provider once a booking is approved.

Automatic video call
--------------------

By default, meetings without a :guilabel:`Location` do not automatically get an online meeting link.
To change this, go to :menuselection:`Settings --> Calendar` and enable :guilabel:`Automatic Video
Call`: events without a location then get a Teams or Google Meet link, depending on the synchronized
calendar.

Each user can override the company setting in :menuselection:`Preferences --> Calendar`, by setting
:guilabel:`Automatic Video Call` to :guilabel:`Company default`, :guilabel:`Yes`, or :guilabel:`No`.

.. note::
   This behavior requires the *Calendar Auto Video Call* (``calendar_auto_videocall``) module, and
   the link itself is created by the synchronized Outlook or Google calendar.

.. toctree::
   :titlesonly:

   calendar/outlook
   calendar/google

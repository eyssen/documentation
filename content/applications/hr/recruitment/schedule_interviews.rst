===================
Schedule interviews
===================

An in-person, virtual, or phone interview is scheduled by the recruitment team from the applicant's
card. The meeting lands in the calendars of everyone invited, and can be sent to the applicant by
email or text message.

.. _recruitment/schedule_interviews/recruitment-scheduled:

Recruitment team scheduled interviews
=====================================

When an applicant reaches the interview stage, the recruitment team should schedule the interview,
by first coordinating a suitable date and time with the applicant and interviewers.

To schedule the interview, navigate to the applicant's card, by first going to the
:menuselection:`Recruitment app`, and clicking the relevant job card. This opens the
:guilabel:`Applications` page for that job position. Then, click the desired applicant's card to
view their detailed applicant form.

To schedule an phone, virtual, or in-person interview, click the :icon:`fa-calendar` :guilabel:`No
Meeting` smart button at the top of the applicant's record.

.. note::
   The :guilabel:`Meetings` smart button displays :icon:`fa-calendar` :guilabel:`No Meeting` if no
   meetings are currently scheduled. For applicants who are new to the :guilabel:`First Interview`
   stage, this is the default.

   If there is one meeting already scheduled, the smart button displays :guilabel:`1 Meeting`, with
   the date of the upcoming meeting beneath it. If more than one meeting is scheduled, the button
   displays :guilabel:`Next Meeting`, with the date of the first upcoming meeting beneath it.

Clicking the :guilabel:`Meetings` smart button loads a calendar, showing the scheduled meetings and
events for the currently signed-in user, as well as the employees who are listed under the
:guilabel:`Attendees` section, located to the right of the calendar.

To change the currently loaded meetings and events being displayed, uncheck an attendee whose
calendar events are to be hidden. Only the checked attendees are visible on the calendar.

.. screenshot:: hr-recruitment-interviews-calendar
   :menu: Recruitment ‣ Applications ‣ (calendar view)
   :shows: The interview calendar in week view, with the attendee filters on the right used to choose whose meetings are displayed.
   :highlight: The attendee filter panel (red frame).
   :data: Two recruiters with interviews across the week.
   :module: hr_recruitment, calendar
   :notes: English UI, light theme, 1440px width.

To add a meeting to the calendar when in the *Day* or *Week* view, click on the start time of the
meeting and drag down to the end time. Doing so selects the date, time, and the length of the
meeting.

A meeting can also be added in this view by clicking on the desired day *and* time slot.

Both methods cause a :ref:`New Event <recruitment/schedule_interviews/event-card>` pop-up window to
appear.

.. _recruitment/schedule_interviews/event-card:

New event pop-up window
-----------------------

Clicking a grid, corresponding with the time and date, opens the :guilabel:`New Event` pop-up window
to schedule a meeting.

Enter the information on the form. The only required fields to enter are a title for the meeting,
along with the :guilabel:`Start` (and end date/time) fields.

Once the card details are entered, click :guilabel:`Save & Close` to save the changes and create the
interview.

After entering in a required name for the meeting, the fields available to modify on the
:guilabel:`New Event` card are as follows:

- :guilabel:`Meeting Title`: Enter the subject for the meeting. This should clearly indicate the
  purpose of the meeting. The default subject is the :guilabel:`Candidate` name entered on the
  applicant's card.
- :guilabel:`Start`: Configure the start and end date and times for the meeting. Clicking either of
  these fields opens a calendar pop-up window. Click on the desired date to select it, and then
  enter the time in the corresponding field. Click :icon:`fa-check` :guilabel:`Apply` to close the
  window.
- :guilabel:`All Day`: Tick the box to schedule an all-day interview. If this box is ticked, the
  :guilabel:`Start` field changes to :guilabel:`Start Date`.
- :guilabel:`Attendees`: Select the people who should attend the meeting. The default attendees are
  the prospective candidate, and the assigned recruiter for the job position. Add as many other
  people as desired.
- :guilabel:`Videocall URL`: If the meeting is virtual, or if there is a virtual option available,
  click :icon:`fa-plus` :guilabel:`Odoo meeting`, and a URL is automatically created for the
  meeting, which populates the field.
- :guilabel:`Description`: Enter a brief description in this field. There is an option to enter
  formatted text, such as numbered lists, headings, tables, links, photos, and more. Use the
  powerbox feature, by typing a `/` to reveal a list of options.

  Scroll through the options and click on the desired item. The item appears in the field, and can
  be modified. Each command presents a different pop-up window. Follow the instructions for each
  command to complete the entry.

More options
~~~~~~~~~~~~

To add additional information to the meeting, click the :guilabel:`More Options` button in the
lower-right corner of the :ref:`New Event <recruitment/schedule_interviews/event-card>` pop-up
window. Enter any of the following additional fields:

- :guilabel:`Duration`: this field auto populates based on the :guilabel:`Start` (and end) date and
  time. If the meeting time is adjusted, this field automatically adjusts to the correct duration
  length. The default length of a meeting is one hour.
- :guilabel:`Recurrent`: if the meeting should repeat at a selected interval (not typical for a
  first interview), tick the checkbox next to :guilabel:`Recurrent`. Several additional fields
  appear when this is enabled:

  - :guilabel:`Timezone`: using the drop-down menu, select the :guilabel:`Timezone` for the
    recurrent meetings.
  - :guilabel:`Repeat`: choose :guilabel:`Daily`, :guilabel:`Weekly`, :guilabel:`Monthly`,
    :guilabel:`Yearly`, or :guilabel:`Custom` recurring meetings. If :guilabel:`Custom` is selected,
    a :guilabel:`Repeat Every` field appears beneath it, along with another time frequency parameter
    (:guilabel:`Days`, :guilabel:`Weeks`, :guilabel:`Months`, or :guilabel:`Years`). Enter a number
    in the blank field, then select the time period using the drop-down menu.
  - :guilabel:`Repeat on`: enabled when the :guilabel:`Weekly` option is selected in the
    :guilabel:`Repeat` field. Choose the day the weekly meeting falls on.
  - :guilabel:`Day of Month`: configure the two drop-down menu options to select a specific day of
    the month, irrespective of the date (e.g. the first Tuesday of every month). To set a specific
    calendar date, choose :guilabel:`Date of Month` and enter the calendar date in the field (e.g.
    `15` to set the meeting to occur on the fifteenth of every month).
  - :guilabel:`Until`: using the drop-down menu, select when the meetings stop repeating. The
    available options are :guilabel:`Number of repetitions`, :guilabel:`End date`, and
    :guilabel:`Forever`. If :guilabel:`Number of repetitions` is selected, enter the number of total
    meetings to occur in the blank field to the right. If :guilabel:`End date` is selected, specify
    the date using the calendar pop-up window, or type in a date in a MM/DD/YYYY format.
    :guilabel:`Forever` schedules meetings indefinitely.

- :guilabel:`Location`: enter the location for the meeting.
- :guilabel:`Tags`: select any tags for the meeting using the drop-down menu, or add a new tag by
  typing in the tag and clicking :guilabel:`Create "tag"`. There is no limit to the number of tags
  that can be used.
- :guilabel:`Privacy`: select if the organizer appears either :guilabel:`Available` or
  :guilabel:`Busy` for the duration of the meeting. Next, select the visibility of this meeting,
  using the drop-down menu to the right of the first selection. Options are :guilabel:`Public`,
  :guilabel:`Private`, and :guilabel:`Only internal users`. :guilabel:`Public` allows for everyone
  to see the meeting, :guilabel:`Private` allows only the attendees listed on the meeting to see the
  meeting, and :guilabel:`Only internal users` allows anyone logged into the company database to see
  the meeting.
- :guilabel:`Organizer`: the employee who created the meeting is populated in this field. Use the
  drop-down menu to change the selected employee.
- :guilabel:`Reminders`: select a reminder from the drop-down menu. Default options include
  :guilabel:`Notification`, :guilabel:`Email`, and :guilabel:`SMS Text Message`, each with a
  specific time period before the event (hours, days, etc). The chosen reminder chosen alerts the
  meeting participants of the meeting, via the selected option at the specified time. Multiple
  reminders can be selected in this field.

.. screenshot:: hr-recruitment-interview-event
   :menu: Recruitment ‣ (job position) ‣ (open an applicant) ‣ Meeting
   :shows: A meeting form for an interview with the title, the attendees, the date and time, the duration and the videocall link.
   :highlight: The attendees and the date and time (red frame).
   :data: Interview with applicant "János Tóth", 2026-04-23 10:00, 1 hour.
   :module: hr_recruitment, calendar
   :notes: English UI, light theme, 1440px width.

Send meeting to attendees
-------------------------

Once changes have been entered on the :ref:`New Event <recruitment/schedule_interviews/event-card>`
pop-up window, and the meeting details are correct, the meeting can be sent to the attendees, via
email or text message, from the expanded event form (what is seen when the :guilabel:`More Options`
button is clicked on in the :guilabel:`New Event` pop-up window).

To send the meeting via email, click the :icon:`fa-envelope` :guilabel:`EMAIL` button next to the
:guilabel:`Attendees` field on the expanded meeting form.

A :guilabel:`Contact Attendees` email configurator pop-up window appears. A pre-formatted email,
using the default :guilabel:`Calendar: Event Update` email template, populates the email body field.

The applicant, followers of the job application, as well as the user who created the meeting, are
added to the :guilabel:`To` by default. Make any desired changes to the email.

.. screenshot:: hr-recruitment-interview-email
   :menu: Recruitment ‣ (job position) ‣ (open an applicant) ‣ Meeting ‣ Email
   :shows: The email dialog for sending the meeting details to the attendees, with the recipients and the message body.
   :highlight: The recipients (red frame).
   :data: Interview with applicant "János Tóth"; use invented addresses.
   :module: calendar
   :notes: English UI, light theme, 1440px width.

To send the meeting via text message, click the :icon:`fa-mobile` :guilabel:`SMS` button next to the
:guilabel:`Attendees` field on the expanded meeting form. A :guilabel:`Send SMS` pop-up window
appears.

At the top, a blue banner appears if any attendees do not have valid mobile numbers, and lists how
many records are invalid. If a contact does not have a valid mobile number listed, click
:guilabel:`Close`, and edit the attendee's record, then redo these steps.

When no warning message appears, type in the message to be sent to the attendees in the
:guilabel:`Message` field. To add any emojis to the message, click the :icon:`oi-smile-add`
:guilabel:`(smile add)` icon on the right-side of the pop-up window.

The number of characters, and amount of text messages required to send the message (according to
GSM7 criteria) appears beneath the :guilabel:`Message` field. Click :guilabel:`Put in queue` to have
the text sent later, after any other messages are scheduled, or click :guilabel:`Send Now` to send
the message immediately.

.. screenshot:: hr-recruitment-interview-sms
   :menu: Recruitment ‣ (job position) ‣ (open an applicant) ‣ Meeting ‣ SMS
   :shows: The SMS dialog for sending the meeting details to the attendees, with the recipients, the message and the credit count.
   :highlight: The message body (red frame).
   :data: Interview with applicant "János Tóth"; use an invented phone number.
   :module: sms
   :notes: English UI, light theme, 1440px width.

.. note::
   Sending text messages is **not** a default capability with Odoo. To send text messages, credits
   are required, which need to be purchased. For more information on IAP credits and plans, refer to
   the :doc:`../../essentials/in_app_purchase` documentation.

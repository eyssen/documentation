:show-content:

============
Appointments
============

.. toctree::
   :titlesonly:

   appointments/create-opps

The **Appointments** app lets customers and colleagues book time with the company: an *appointment
type* defines who can be booked, when, for how long, and under which conditions, and each booking
creates a calendar event for the provider.

.. note::
   The app is provided by the eYssen *Appointment* module family (``appointment`` and its bridge
   modules). The optional features described below each require their own module, indicated in the
   corresponding section.

Access rights
=============

The :guilabel:`Appointments` category of the :ref:`access rights <access-rights/users>` offers:

- :guilabel:`User`: sees and manages their own bookings;
- :guilabel:`Manager`: sees all bookings, and configures appointment types and resources.

.. _appointments/types:

Appointment types
=================

Go to :menuselection:`Appointments --> Configuration --> Appointment Types` to create a type. Fill
in the :guilabel:`Name`, a :guilabel:`Description` shown to the customer, the :guilabel:`Location`,
and the :guilabel:`Time Zone` the slots are published in.

Availability
------------

The :guilabel:`Availability` tab defines when the type can be booked:

- :guilabel:`Allowed Providers`: the users who can be booked for this type. :guilabel:`Default
  Working Hours` sets the working schedule used to compute the slots, and, under
  :guilabel:`Per-provider Working Hours`, a different schedule can be set for individual providers.
- :guilabel:`Required Resources`: resources (rooms, equipment) that must be free for the booking to
  be possible.
- :guilabel:`Weekly Slots`: the recurring time ranges of the week when bookings are accepted, with
  an optional capacity or gap override per slot.
- :guilabel:`Duration`: the :guilabel:`Min Duration (min)`, :guilabel:`Max Duration (min)`,
  :guilabel:`Duration Step (min)`, and :guilabel:`Default Duration (min)` a customer can choose
  from, and the :guilabel:`Slot Increment (min)` used to generate the proposed start times.
- :guilabel:`Buffers & Gaps`: :guilabel:`Buffer Before (min)` and :guilabel:`Buffer After (min)`
  keep time free around a booking, and :guilabel:`Gap Between Meetings (min)` enforces a pause
  between two consecutive bookings.
- :guilabel:`Limits`: how far ahead bookings are possible (:guilabel:`Max Days Ahead`), the
  :guilabel:`Min Notice Hours` before the start, the :guilabel:`Cancel Notice Hours` until which a
  customer may cancel, the :guilabel:`Max Future Bookings Per Person`, and the
  :guilabel:`Capacity Per Slot` when several people may book the same slot.

Odoo computes the free slots from the working hours, the existing bookings, the providers' calendar
events, and their :ref:`leaves <appointments/leaves>`.

.. screenshot:: productivity-appointments-type-availability
   :menu: Appointments ‣ Configuration ‣ Appointment Types
   :shows: An appointment type form on the Availability tab, with the Providers & Resources, Duration, Buffers & Gaps and Limits groups filled in, and the weekly slot lines below.
   :highlight: The "Duration" and "Limits" groups (red frame).
   :data: Type "Consultation", two providers, weekly slots Monday to Friday 09:00–17:00.
   :module: appointment
   :notes: English UI, light theme, 1440px width.

Assignment and approval
-----------------------

When several providers are allowed, the :guilabel:`Assign Strategy` decides who gets the booking:
:guilabel:`Least Assigned`, :guilabel:`Round Robin`, or :guilabel:`Random`.

Enable :guilabel:`Require Approval` to hold new bookings in the :guilabel:`Requested` state until
they are approved. The approval policy is either :guilabel:`Single Approval (Manager)` or
:guilabel:`All Providers Must Approve`; in the latter case, each provider gets an approval line on
the booking, and can approve or reject it from the booking form or from the link in the approval
email.

:guilabel:`Unconfirmed Expiry (hours)` automatically cancels bookings that are never confirmed.

Questions
---------

The :guilabel:`Form` tab lists the questions asked when booking. Each question has a
:guilabel:`Name`, a :guilabel:`Type` (:guilabel:`Short Text`, :guilabel:`Long Text`,
:guilabel:`Number`, :guilabel:`Date`, :guilabel:`Select`, :guilabel:`Checkbox`, or
:guilabel:`File`), and can be marked :guilabel:`Required`. For a :guilabel:`Select` question, list
the options one per line. A question can also block the booking when a given answer is given, with
the :guilabel:`Error Message` shown to the customer.

The answers are stored on the booking, in its :guilabel:`Answers` tab.

Notifications
-------------

In the :guilabel:`Notifications` tab, select the email template used for each step:
:guilabel:`Email on Request`, :guilabel:`Email on Confirm`, :guilabel:`Email on Reject`,
:guilabel:`Email on Cancel`, :guilabel:`Email on Approval Request`, and :guilabel:`Email on Waitlist
Offer`. An :guilabel:`Additional email message` is appended to these emails.

:guilabel:`Event reminders` send a reminder to the requester a given time before the appointment
(e.g., `1` :guilabel:`Days`), while :guilabel:`Calendar alarms` are the reminders set on the
provider's calendar event.

Waitlist
--------

Enable :guilabel:`Waitlist` in the corresponding tab to let customers queue for a fully booked slot.
When a slot frees up, Odoo offers it to the first customers in the queue (:guilabel:`Waitlist Notify
Batch`), who then have :guilabel:`Waitlist Hold Minutes` to confirm before the offer expires and the
next customers are notified.

Visibility and restrictions
---------------------------

- :guilabel:`Visibility`: :guilabel:`Public`, :guilabel:`Unlisted` (only reachable with the link),
  or :guilabel:`Private`.
- In the :guilabel:`Restrictions` tab, :guilabel:`Allowed Domains` limits public booking to a
  comma-separated list of email domains.
- Click :guilabel:`Generate share link` to obtain a :guilabel:`Share URL` that can be sent to
  customers. :guilabel:`Regenerate` invalidates the previous link.

Pricing and payment
-------------------

A type can be free, or priced with a :guilabel:`Pricing Mode`:

- :guilabel:`Fixed`: the :guilabel:`Fixed Amount` is charged per booking;
- :guilabel:`Hourly`: the :guilabel:`Hourly Rate` is applied to the booked duration, rounded up to
  the :guilabel:`Billing Increment (min)`.

Enable :guilabel:`Payment Required` to make the payment part of the booking flow.
:guilabel:`Allow Refund Until Hours` defines until when a cancellation is refundable.

.. _appointments/bookings:

Bookings
========

:menuselection:`Appointments --> Bookings` lists all bookings, in list or calendar view. A booking
records:

- the :guilabel:`Appointment Type`, the :guilabel:`Providers`, and the :guilabel:`Resources`;
- the :guilabel:`Customer`, or, for a public booking, the visitor's name, email, phone, and
  language;
- the start, the end, and the :guilabel:`Duration (min)`;
- the :guilabel:`Status`: :guilabel:`Requested`, :guilabel:`Approved`, :guilabel:`Rejected`, or
  :guilabel:`Cancelled`;
- the :guilabel:`Pricing` and the payment status (:guilabel:`Pending`, :guilabel:`Authorized`,
  :guilabel:`Paid`, :guilabel:`Refunded`, or :guilabel:`Failed`).

Use the buttons in the header to :guilabel:`Approve`, :guilabel:`Reject`, or :guilabel:`Cancel` a
booking, and, after the appointment, to :guilabel:`Mark Show` or :guilabel:`Mark No-show`.
:guilabel:`Force Approve` lets a manager approve a booking that is still waiting for other
providers.

An approved booking creates the calendar event of its providers, and the customer receives the
confirmation email with a link to their booking.

.. screenshot:: productivity-appointments-booking-form
   :menu: Appointments ‣ Bookings
   :shows: A booking form with the header buttons (Approve, Reject, Cancel, Mark Show, Mark No-show), the Booking Details, Customer, Pricing and Status groups, and the Approvals tab showing two provider lines.
   :highlight: The header buttons (red frame).
   :data: Booking for "Deco Addict", type "Consultation", state "Requested", two approval lines.
   :module: appointment
   :notes: English UI, light theme, 1440px width.

.. _appointments/export:

Export bookings
---------------

With the *eYssen Appointment (Reports & Export)* module (`appointment_reports`), appointment
managers can download the bookings from the :guilabel:`Export` menu of the application:

- :menuselection:`Appointments --> Export --> Export Bookings (CSV, max 10,000)` downloads the
  `appointments.csv` file, with one row per booking: name, type, start, end, duration in minutes,
  customer (or the visitor's name for a public booking), amount, status, and attendance;
- :menuselection:`Appointments --> Export --> Export Bookings (iCal, max 10,000)` downloads the
  `appointments.ics` calendar file, which can be imported in any calendar application. Each booking
  is an event titled with the appointment type and the booking name, with its location and
  description; approved bookings are marked as confirmed, the others as tentative.

Both files contain the 10,000 most recent bookings at most, of all statuses. The dates and times
are expressed in UTC.

.. tip::
   The export can be narrowed by adding parameters to the address of the download, e.g.,
   `/appointment/export/csv?state=approved&date_from=2026-01-01&date_to=2026-03-31`. The available
   parameters are `type_id` (the ID of an appointment type), `state` (`requested`, `approved`,
   `rejected`, or `cancelled`), `date_from`, and `date_to` (`YYYY-MM-DD`).

.. note::
   To install the module, enable :guilabel:`Reports` under :guilabel:`Appointment` in
   :menuselection:`Settings --> eYssen ERP`. The menu and the downloads are reserved for the users
   with the :guilabel:`Manager` access level of the Appointments app.

.. _appointments/leaves:

Provider unavailability
=======================

Providers can be made unavailable for a period of time with an **appointment leave**, which has a
:guilabel:`User`, a start and an end, a :guilabel:`Reason`, and a state (:guilabel:`Draft`,
:guilabel:`Approved`, :guilabel:`Cancelled`). Only approved leaves block the slots.

.. note::
   With the *Appointment (HR Holidays)* (``appointment_hr``) module, validated time off of the
   employees linked to the providers also blocks the corresponding slots, so time off does not have
   to be entered twice.

Passes
======

The *Appointment (Passes)* (``appointment_pass``) module sells packages of appointments. In
:menuselection:`Appointments --> Passes --> Pass Products`, define a pass with a :guilabel:`Name`, a
:guilabel:`Mode` (a number of :guilabel:`Occurrences` or a balance of minutes), the
:guilabel:`Validity (days)`, and the :guilabel:`Price`.

:menuselection:`Appointments --> Passes --> Pass Holders` lists the passes owned by customers, with
their :guilabel:`Occurrences Remaining` or :guilabel:`Minutes Remaining` and the :guilabel:`Valid
Until` date. When a customer with a valid pass books an appointment, the booking is redeemed against
the pass instead of being paid.

Coupons and gift cards
======================

The *Appointment (Payment)* (``appointment_payment``) module adds discounts to the booking flow:

- :menuselection:`Appointments --> Configuration --> Payments & Discounts --> Coupons`: a coupon has
  a :guilabel:`Code`, a :guilabel:`Discount Type` (percentage or fixed amount), an
  :guilabel:`Amount`, a validity period, and a :guilabel:`Max Uses` limit (`0` = unlimited).
- :menuselection:`Appointments --> Configuration --> Payments & Discounts --> Gift Cards`: a gift
  card has a :guilabel:`Code`, a :guilabel:`Balance`, and an expiry date. The balance is deducted
  from the amount due of the booking.

The remaining :guilabel:`Amount Due` is then paid with one of the configured :doc:`payment providers
<../finance/payment_providers>`.

Other integrations
==================

- **Project**: with the *Appointment (Project Tasks)* (``appointment_project``) module, select a
  :guilabel:`Target Project` on the appointment type to create a task there when a booking is
  approved.
- **eLearning**: with the *Appointment (eLearning)* (``appointment_elearning``) module, select a
  :guilabel:`Course to Enroll` on the appointment type to enroll the customer in that course when
  the booking is approved.
- **CRM**: see :doc:`appointments/create-opps`.

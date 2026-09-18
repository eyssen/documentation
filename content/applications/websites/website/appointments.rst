===================
Online appointments
===================

The *eYssen Appointment (Website)* module (`appointment_website`) publishes the appointment types
configured in the **Appointments** app on the website, so that visitors can book a slot themselves.
The *eYssen Appointment (Website Payment)* module (`appointment_website_payment`) adds a payment
step for paid appointment types.

.. note::
   This page describes the public booking funnel. The appointment types, their weekly slots,
   providers, durations, questions, approval rules and pricing are configured in the back end; see
   the Appointments documentation.

The booking page
================

Public appointment types are listed at `/appointments`, and each type also has its own address
(`/appointments/<id>`). The page shows a month grid in which the available days are selectable;
picking a day reveals the free time slots of that day, computed from the type's weekly slots, the
providers' calendars, the buffers between meetings and the capacity of each slot.

Visitors choose the slot and the duration — within the minimum, maximum and step configured on the
type — enter their name, email and phone number, and answer the questions defined on the appointment
type. The booking is created when they confirm.

.. screenshot:: website-appointments-booking-page
   :menu: (website) ‣ /appointments
   :shows: The public appointment page with the appointment type selection, the month grid of available days, and the free time slots of the selected day with the duration selector.
   :highlight: The month grid and the slot list (red frame).
   :data: Two public appointment types, one selected day with four free slots.
   :module: appointment_website
   :notes: English UI, light theme, 1440px width.

.. note::
   Only appointment types whose :guilabel:`Visibility` is *public* appear at `/appointments`. Types
   that should not be listed publicly are shared through a **share link**
   (`/appointments/share/<token>`), which opens the booking page for that one type. Share links can
   be given an expiry date on the appointment type.

Managing a booking
==================

After booking, the visitor receives a link to their own booking page (`/appointment/view/<token>`).
The link is tied to the booking, so no account is needed. From that page they can:

- review the appointment (type, date and time, duration, provider, location, price);
- add the appointment to their own calendar, by downloading its calendar file;
- **reschedule** it, which reopens the booking page with the slots of the same type; and
- **cancel** it.

.. screenshot:: website-appointments-booking-view
   :menu: (booking link from the confirmation email)
   :shows: The visitor's booking page with the appointment details, its status, and the add-to-calendar, reschedule and cancel actions.
   :highlight: The reschedule and cancel actions (red frame).
   :data: One approved booking of a 60-minute appointment.
   :module: appointment_website
   :notes: English UI, light theme, 1440px width.

A booking is created as :guilabel:`Requested`. Depending on the appointment type, it is confirmed
immediately or only after approval; until it is :guilabel:`Approved`, the booking page shows that it
is still awaiting confirmation. A booking that is not confirmed within the period configured on the
type expires automatically.

.. _website/appointments/approval:

Approving a booking
-------------------

When the appointment type requires approval, the providers receive an email with an
:guilabel:`Approve` and a :guilabel:`Reject` link. The link opens a decision page where the provider
confirms the decision and can add a note, without logging in.

Depending on the type's approval policy, either a single approval is enough
(:guilabel:`Single Approval (Manager)`), or every provider must approve
(:guilabel:`All Providers Must Approve`). Once the decision is taken, the booking moves to
:guilabel:`Approved` or :guilabel:`Rejected` and the visitor is notified.

.. screenshot:: website-appointments-approval-decision
   :menu: (approval link from the notification email)
   :shows: The approval decision page with the booking summary, the note field and the confirmation button for the Approve decision.
   :highlight: The note field and the confirmation button (red frame).
   :data: One requested booking awaiting approval.
   :module: appointment_website
   :notes: English UI, light theme, 1440px width.

.. _website/appointments/waitlist:

Waiting list
------------

When a slot frees up, the visitors waiting for it receive an offer by email with a confirmation
link. The first one to confirm on that page gets the slot; the others are told that the slot is no
longer available. The offer expires if it is not confirmed in time.

.. screenshot:: website-appointments-waitlist-confirm
   :menu: (waiting list link from the offer email)
   :shows: The waiting list confirmation page with the offered slot and the confirmation button.
   :highlight: The confirmation button (red frame).
   :data: One offered slot.
   :module: appointment_website
   :notes: English UI, light theme, 1440px width.

.. _website/appointments/payment:

Paying for an appointment
=========================

With the *eYssen Appointment (Website Payment)* module (`appointment_website_payment`), a booking
made for a paid appointment type leads to a payment page (`/appointment/pay/<token>`), which shows
the amount computed from the type's pricing and the booked duration, and the available payment
methods.

On that page, the visitor can also:

- **enter a code** — a discount or prepaid code — which is applied to the amount to pay; and
- **use a pass**, if they are logged in to their customer portal and hold a valid pass that covers
  this appointment type. Passes that are expired, used up or restricted to other types are not
  offered.

.. screenshot:: website-appointments-payment-page
   :menu: (payment link after booking)
   :shows: The appointment payment page with the booking summary, the amount to pay, the code field, the "use my pass" option and the payment methods.
   :highlight: The amount and the pass option (red frame).
   :data: One 60-minute booking of EUR 60; the logged-in customer holds a valid pass.
   :module: appointment_website_payment
   :notes: English UI, light theme, 1440px width.

When there is nothing to pay — the amount is zero, or a pass or a code covers it in full — the
payment step is skipped and the booking is confirmed directly.

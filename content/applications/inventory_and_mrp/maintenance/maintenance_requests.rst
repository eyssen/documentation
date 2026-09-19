====================
Maintenance requests
====================

In order to keep equipment functioning properly, it is often necessary to perform maintenance on
it. This can include preventive maintenance, intended to prevent equipment from breaking down, or
corrective maintenance, which is used to fix equipment that is broken or otherwise unusable.

In Odoo *Maintenance*, users can create *maintenance requests* to schedule and track the progress of
equipment maintenance.

Create maintenance request
==========================

To create a new maintenance request, navigate to :menuselection:`Maintenance app --> Maintenance -->
Maintenance Requests`, and click :guilabel:`New`.

Begin filling out the form by entering a descriptive title in the :guilabel:`Request` field (e.g.,
`Drill not working`).

The :guilabel:`Created By` field auto-populates with the user creating the request, but a different
user can be selected by clicking on the drop-down menu.

Using the drop-down menu for the :guilabel:`Equipment` field, select the piece of equipment that
requires maintenance. Once a piece of equipment is selected, a greyed-out :guilabel:`Category` field
appears below it, listing the *Equipment Category* that the equipment belongs to.

The next field is titled :guilabel:`Request Date`, and is set by default to the date on which the
maintenance request is created. This date cannot be changed by the user.

In the :guilabel:`Maintenance Type` field, select the :guilabel:`Corrective` option if the request
is intended to fix an existing issue, or the :guilabel:`Preventive` option if the request is
intended to prevent issues from occurring in the future.

In the :guilabel:`Team` field, select the maintenance team that is responsible for managing the
request. If a specific team member is responsible, select them in the :guilabel:`Responsible` field.

The :guilabel:`Scheduled Date` field is used to specify the date on which maintenance should take
place, and the time it should begin. Choose a date by clicking on the field to open a calendar in a
pop-up window, and then select a day on the calendar. Enter an hour and minute in the two fields
below the calendar, and click :guilabel:`Apply` to save the date and time.

The :guilabel:`Duration` field is used to specify the time it takes to complete the maintenance
request. Use the text-entry field to enter the time in a `00:00` format.

.. tip::
   For a :guilabel:`Preventive` request, ticking the :guilabel:`Recurrent` checkbox reveals a
   :guilabel:`Repeat Every` field, and an end-date option set to :guilabel:`Forever` by default.
   Configure how often, and for how long, the request should recur: once the current occurrence is
   marked as done, Odoo automatically creates the next one on the calculated date.

The :guilabel:`Priority` field is used to communicate the importance (or urgency) of the maintenance
request. Assign the request a priority between zero and three :guilabel:`⭐⭐⭐ (stars)`, by clicking
on the desired star number. Requests assigned a higher priority appear above those with a lower
priority, on the Kanban board used to track the progression of maintenance requests.

In the :guilabel:`Notes` tab at the bottom of the form, enter any relevant details about the
maintenance request (why the maintenance issue arose, when it occurred, etc.).

The :guilabel:`Instructions` tab is used to include instructions for how maintenance should be
performed. Select one of the three options, and then include the instructions as detailed below:

- :guilabel:`PDF`: click the :guilabel:`Upload your file` button to open the device's file manager,
  and then select a file to upload.
- :guilabel:`Google Slide`: enter a :guilabel:`Google Slide link` in the text-entry field that
  appears after the option is selected.
- :guilabel:`Text`: enter the instructions in the text-entry field that appears after the option is
  selected.

.. screenshot:: maintenance-requests-request-form
   :menu: Maintenance ‣ Maintenance ‣ Maintenance Requests ‣ New
   :shows: A maintenance request form filled out for a piece of equipment, with "Request", "Created
     By", "Equipment", "Category", "Request Date", "Maintenance Type" set to "Corrective", "Team",
     "Responsible", "Scheduled Date", "Duration", and "Priority" fields.
   :module: maintenance
   :notes: English UI, light theme, 1440px width.

Process maintenance request
===========================

Once a maintenance request has been created, it appears in the :guilabel:`New Request` stage of the
*Maintenance Requests* page, which can be accessed by navigating to :menuselection:`Maintenance app
--> Maintenance --> Maintenance Requests`.

Maintenance requests can be moved to different stages by dragging and dropping them on the Kanban
board. They can also be moved by clicking on a request to open it in a new page, and then selecting
the desired stage from the stage indicator bar, located above the top-right corner of the request's
form.

A newly-created database typically has four default stages: :guilabel:`New Request`,
:guilabel:`In Progress`, :guilabel:`Repaired`, and :guilabel:`Scrap`.

Successful maintenance requests should be moved to the :guilabel:`Repaired` stage, indicating that
the specified piece of equipment is repaired.

Failed maintenance requests should be moved to the :guilabel:`Scrap` stage, indicating the specified
piece of equipment could not be repaired, and must instead be scrapped.

.. tip::
   While a request is being worked on, its :guilabel:`Kanban State` (the small circle at the top of
   the form) can be set to :guilabel:`In Progress`, :guilabel:`Blocked`, or :guilabel:`Ready for
   next stage`, to communicate the request's status independently of its stage.

   To cancel a request without deleting it, click :guilabel:`Cancel`, at the top of the request's
   form. This archives the request, and replaces the stage indicator bar with a :guilabel:`Cancelled`
   tag. Click :guilabel:`Reopen Request` to unarchive it, and put it back in its original stage.

.. seealso::
   :doc:`maintenance_calendar`

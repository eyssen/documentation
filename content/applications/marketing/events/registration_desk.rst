=================
Registration Desk
=================

Use the *Registration Desk* feature in Odoo **Events** to grant access to registered event attendees
as they arrive, and store attendee-related data in the reporting metrics.

Registration Desk page
======================

On a mobile device (on the Odoo app or in a browser), open the :menuselection:`Events app`, and
click the :guilabel:`Registration Desk` to view the :guilabel:`Registration Desk` page.

.. screenshot:: events-registration_desk-registration-desk-page
   :menu: Events ‣ Registration Desk
   :shows: The Registration Desk page with the Scan a badge and Select Attendee options.
   :data: No event-specific data needed.
   :module: event
   :notes: English UI, light theme, 1440px width.

At the bottom of the :guilabel:`Registration Desk` box, there are options to either :guilabel:`Scan
a badge` or :guilabel:`Select Attendee`.

Scan a badge
============

Scan the codes present on event attendee badges, by navigating to :menuselection:`Events app -->
Registration Desk`, and selecting the :guilabel:`Scan a badge` option.

.. important::
   Odoo **must** be granted access to the camera being used for the :guilabel:`Scan a badge` option
   to work.

Once Odoo has access to the camera, a :guilabel:`Barcode Scanner` pop-up window appears, showing the
camera's point-of-view. There is also a specified view finder box present, whose size can be
manually modified, accordingly, using the :icon:`fa-crop` :guilabel:`(crop)` icon.

.. screenshot:: events-registration_desk-barcode-scanner-window
   :menu: Events ‣ Registration Desk ‣ Scan a badge
   :shows: The barcode scanner window waiting for an attendee badge to be scanned.
   :highlight: The scanner input area (red frame).
   :data: No event-specific data needed.
   :module: event
   :notes: English UI, light theme, 1440px width.

When the badge code is in the middle of the view finder box, the code is scanned, the
:guilabel:`Barcode Scanner` pop-up window disappears, and the attendee is granted access to the
event. Once the code is scanned, their attendance is logged in the Odoo **Events** app.

If the barcode being scanned is invalid, an error pop-up message appears in the upper-right corner.

Select attendee
===============

Manually grant access to event attendees, by navigating to :menuselection:`Events app -->
Registration Desk`, and selecting the :guilabel:`Select Attendee` option.

Odoo reveals an :guilabel:`Attendees` page, with all the attendees for every event in the database,
in a default :icon:`oi-view-kanban` :guilabel:`Kanban` view.

.. screenshot:: events-registration_desk-attendees-page
   :menu: Events ‣ Registration Desk ‣ Select Attendee
   :shows: The Attendees list with the Attendee Name, Event, Ticket, Registration Date and Status columns, and the Register and Attended buttons.
   :highlight: The Register / Attended buttons (red frame).
   :data: Five registered attendees of the demo event.
   :module: event
   :notes: English UI, light theme, 1440px width.

On the :guilabel:`Attendees` page, each attendee card displays that person's name, which event they
are registered to attend, their associated company (if applicable), what ticket tier they purchased
(if applicable), along with two buttons: a :icon:`fa-check` :guilabel:`(checkmark)` and
:icon:`fa-undo` :guilabel:`(counter-clockwise arrow)`.

To grant access to a person, marking them as attended, click the :icon:`fa-check`
:guilabel:`(checkmark)` button on that attendee's card.

Click the :icon:`fa-undo` :guilabel:`(counter-clockwise arrow)` button on an attendee's card to undo
the previous action.

.. tip::
   It is recommended to use an event-specific filter on the :guilabel:`Attendees` page, via the
   search bar drop-down menu.

   To do that, click the :icon:`fa-sort-desc` :guilabel:`(down arrow)` beside the seach bar to
   reveal a drop-down menu with :guilabel:`Filters`, :guilabel:`Group By`, and :guilabel:`Favorites`
   options.

   For example, click the :guilabel:`Event` option, in the :guilabel:`Group By` column. Then, click
   away to remove the drop-down menu. Odoo reveals the :guilabel:`Attendees` page with
   event-specific columns, allowing users to locate specific event attendees.

.. seealso::
   :doc:`../../essentials/search`

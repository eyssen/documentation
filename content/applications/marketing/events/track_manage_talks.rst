============================
Talks, proposals, and agenda
============================

With Odoo *Events*, users can utilize a fully-integrated event website, where attendees can quickly
access various tracks (talks, presentations, etc.), view entire agendas, and propose talks for the
event.

Event website
=============

To access an event website, navigate to the specific event form in the Odoo *Events* app, and click
the :guilabel:`Go to Website` smart button. Or, while on the Odoo-built website for the company,
click the :guilabel:`Events` header option, and select the desired event to view that event's
website.

On the event website, there is an event-specific subheader menu with different options to choose
from.

With the *Schedule & Tracks* setting enabled in the Odoo *Events* app, the following links are
automatically added to the subheader menu, located on the event website: :guilabel:`Talks`,
:guilabel:`Talk Proposals`, and :guilabel:`Agenda`.

.. screenshot:: events-track-manage-talks-track-submenu-options
   :menu: (event website)
   :shows: The event website's top menu with the track-related submenu entries Talks, Agenda and Talk Proposals.
   :highlight: The track-related submenu entries (red frame).
   :data: Demo event with tracks enabled.
   :module: website_event_track
   :notes: English UI, light theme, 1440px width.

To enable the :guilabel:`Schedule & Tracks` setting, navigate to :menuselection:`Events app -->
Configuration --> Settings`, tick the checkbox beside :guilabel:`Schedule & Tracks`, and click
:guilabel:`Save`.

Talks page
----------

The :guilabel:`Talks` link takes the attendee to a page filled with all the planned tracks for the
event.

.. screenshot:: events-track-manage-talks-talks-page
   :menu: (event website) ‣ Talks
   :shows: The Talks page of the event website listing the published tracks with the tag and date filter menus.
   :highlight: The filter menus (red frame).
   :data: Four published talks with two tags.
   :module: website_event_track
   :notes: English UI, light theme, 1440px width.

At the top of :guilabel:`Talks` page, there are drop-down filter menus beside a :guilabel:`Search
a talk...` search bar.

The first drop-down filter menu (with the starting title: :guilabel:`Favorites`) is the only
drop-down filter menu that appears by default. When clicked, the resulting menu presents two
options: :guilabel:`Favorites` and :guilabel:`All Talks`.

Selecting :guilabel:`Favorites` shows *only* the tracks that have been favorited by the attendee.

.. note::
   If no tracks have been favorited, and the :guilabel:`Favorites` filter is selected, Odoo presents
   all the event tracks.

Selecting :guilabel:`All Talks` shows *all* the tracks, regardless if they have been favorited or
not.

The other drop-down filter menus that appear on this page are related to any configured tags (and
tag categories) created for event tracks in the backend.

.. tip::
   To add tags and tag categories to track forms, open a desired event track form, and start typing
   a new tag in the :guilabel:`Tags` field. Then, click :guilabel:`Create and edit...` from the
   resulting drop-down menu.

   Doing so reveals a :guilabel:`Create Tags` pop-up form.

   .. screenshot:: events-track-manage-talks-create-tags-popup
      :menu: Events ‣ Configuration ‣ Track Tags ‣ New
      :shows: The Create Tags pop-up window with the Tag Name, Category and Color fields used for the website filter menus.
      :highlight: The Category field (red frame).
      :data: Tag 'Beginner' in the category 'Level'.
      :module: website_event_track
      :notes: English UI, light theme, 1440px width.

   From here, users see the recently added tag in the :guilabel:`Tag Name` field. Beneath that,
   there is an option to add a specific :guilabel:`Color Index` to the tag for added organization.

   Lastly, there is the :guilabel:`Category` field, where users can either select a pre-existing
   category for this new tag, or create a new one.

   All options in the :guilabel:`Category` field for tags appear as their own drop-down filter menu
   on the :guilabel:`Talks` page, located on the event website.

Beneath the drop-down filter menus at the top of the :guilabel:`Talks` page, there is a list of
planned tracks for the specific event, organized by day.

If an attendee wishes to favorite a track, they can click the :icon:`fa-bell-o` :guilabel:`(empty
bell)` icon, located to the right of the track title. Attendees will know a track has been favorited
when they notice the icon has been changed to :icon:`fa-bell` :guilabel:`(filled bell)` icon.

Favoriting a track this way places it on the list of :guilabel:`Favorites`, which is accessible from
the default drop-down filter menu, located at the top of the :guilabel:`Talks` page.

Talk Proposals page
-------------------

The :guilabel:`Talk Proposals` link takes attendees to a page on the event website, wherein they can
formerly submit a proposal for a talk (:dfn:`track`) for the event, via a custom online form.

.. screenshot:: events-track-manage-talks-talk-proposals-page
   :menu: (event website) ‣ Talk Proposals
   :shows: The Talk Proposals page of the event website with the proposal form (title, speaker, biography, description).
   :highlight: The proposal form fields (red frame).
   :data: Empty proposal form.
   :module: website_event_track
   :notes: English UI, light theme, 1440px width.

In addition to the form, an introduction to the page, along with any other pertinent information
related to the types of talks the event will feature can be added, if needed.

The talk proposal form can be modified in a number of different ways, via the web builder tools,
accessible by clicking :guilabel:`Edit` while on the specific page.

Then, proceed to edit any of the default fields, or add new forms with the :guilabel:`Form` building
block (located in the :guilabel:`Blocks` section of the web builder tools sidebar).

Once all the necessary information is entered into the form, the attendees just need to click the
:guilabel:`Submit Proposal` button.

Then, that talk, and all the information entered on the form, can be accessed on the
:guilabel:`Event Tracks` page for that specific event in the :guilabel:`Proposal` stage, which is
accessible via the :guilabel:`Tracks` smart button on the event form.

At that point, an internal user can review the proposed talk, and choose to accept or deny the
proposal.

If accepted, the internal user can then move the track to the next appropriate stage in the Kanban
pipeline on the :guilabel:`Event Tracks` page for the event. Then, they can open that track form,
and click the :guilabel:`Go to Website` smart button to reveal that track's page on the event
website.

From there, they can toggle the :guilabel:`Unpublished` switch in the header to
:guilabel:`Published`, which allows all event attendees to view and access the talk.

Agenda page
-----------

The :guilabel:`Agenda` link takes attendees to a page on the event website, showcasing an event
calendar, depicting when (and where) events are taking place for that specific event.

.. screenshot:: events-track-manage-talks-event-agenda-page
   :menu: (event website) ‣ Agenda
   :shows: The Agenda page of the event website showing the tracks in a time grid by day and location.
   :highlight: The time grid (red frame).
   :data: Four tracks over one day and two locations.
   :module: website_event_track
   :notes: English UI, light theme, 1440px width.

Clicking any track on the calendar takes the attendee to that specific track's detail page on the
event website.

If an attendee wishes to favorite a track, they can click the :icon:`fa-bell-o` :guilabel:`(empty
bell)` icon, located to the right of the track title. Attendees will know a track has been favorited
when they notice the icon has been changed to :icon:`fa-bell` :guilabel:`(filled bell)` icon.

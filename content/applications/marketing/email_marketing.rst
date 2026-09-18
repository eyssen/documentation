:show-content:

===============
Email Marketing
===============

The Odoo *Email Marketing* app provides drag-and-drop design tools, pre-built templates, and other
interactive features to create engaging email campaigns. The *Email Marketing* app also provides
detailed reporting metrics to track the campaigns' overall effectiveness.


.. cards::

   .. card:: Mailing lists
      :target: email_marketing/mailing_lists

      Silo contacts into specific mailing lists.

   .. card:: Manage unsubscriptions (Blacklist)
      :target: email_marketing/unsubscriptions

      Allow recipients to unsubscribe and blacklist from future mailings.

   .. card:: Lost leads reactivation email
      :target: email_marketing/lost_leads_email

      Target lost leads with Email Marketing.

   .. card:: Analyze Metrics
      :target: email_marketing/analyze_metrics

      Analyzing campaign metrics.

Email marketing dashboard
=========================

After installing the application, click the :menuselection:`Email Marketing` app icon from the main
Odoo dashboard. Doing so reveals the main :guilabel:`Mailings` dashboard in the default list view.

.. screenshot:: email_marketing-email_marketing-mailings-dashboard
   :menu: Email Marketing ‣ Mailings
   :shows: The Mailings dashboard in list view with the Subject, Recipients, Sent, Delivered, Opened, Clicked, Replied and Status columns.
   :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

In the search bar, the default filter of :guilabel:`My Mailings` is present to show all the mailings
related to the current user. To remove that filter, click the :guilabel:`✖️ (remove)` icon next to
the filter in the search bar. Doing so reveals all the mailings in the database.

The information on the :guilabel:`Mailings` dashboard has four different view options, located in
the upper-right corner as individual icons.

The view options, from left-to-right, are:

- :ref:`List <email_marketing/list-view>` (default view)
- :ref:`Kanban <email_marketing/kanban-view>`
- :ref:`Calendar <email_marketing/calendar-view>`
- :ref:`Graph <email_marketing/graph-view>`

.. _email_marketing/list-view:

List view
---------

The list view, represented by the :guilabel:`☰ (horizontal lines)` icon in the upper-right corner,
is the default view of the :guilabel:`Mailings` dashboard in the :guilabel:`Email Marketing` app.

While in list view, there are columns dedicated to different aspects of information related to the
listed emails. Those columns are as follows:

- :guilabel:`Date`: the date the email was sent.
- :guilabel:`Subject`: the subject of the email.
- :guilabel:`Responsible`: the user who created the email, or the user who has been assigned to the
  email.
- :guilabel:`Sent`: how many times the email has been sent.
- :guilabel:`Delivered (%)`: percentage of sent emails that have been successfully delivered.
- :guilabel:`Opened (%)`: percentage of sent emails that have been opened by the recipients.
- :guilabel:`Clicked (%)`: percentage of sent emails that have been clicked by the recipients.
- :guilabel:`Replied (%)`: percentage of sent emails that have been replied to by the recipients.
- :guilabel:`Status`: the status of the email (:guilabel:`Draft`, :guilabel:`In Queue`, or
  :guilabel:`Sent`).

To add or remove columns, click the :guilabel:`Additional Options (two horizontal lines with dots)`
icon, located to the far-right of the column titles in list view. Doing so reveals a drop-down menu
of additional column options.

.. _email_marketing/kanban-view:

Kanban view
-----------

The Kanban view, represented by the :guilabel:`(inverted bar graph)` icon, can be accessed in the
upper-right corner of the :guilabel:`Mailings` dashboard in the :guilabel:`Email Marketing` app.

.. screenshot:: email_marketing-email_marketing-kanban-view
   :menu: Email Marketing ‣ Mailings
   :shows: The Mailings kanban grouped by status, each card showing the subject, the recipients and the result percentages.
   :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

While in Kanban view, the email information is displayed in the various stages.

The stages are: :guilabel:`Draft`, :guilabel:`In Queue`, :guilabel:`Sending`, and :guilabel:`Sent`.

- :guilabel:`Draft`: the email is still being written/created.
- :guilabel:`In Queue`: the email is scheduled to be sent at a later date.
- :guilabel:`Sending`: the email is currently being sent to its recipients.
- :guilabel:`Sent`: the email has already been sent to its recipients.

In each stage, there are drag-and-drop cards representing the emails that have been created/sent,
and the stage they are in represents the current status of that mailing.

Each card on the :guilabel:`Mailings` dashboard provides key information related to that specific
email.

When the cursor hovers over the upper-right corner of an email campaign card, a :guilabel:`⋮ (three
vertical dots)` icon appears. When clicked, a mini drop-down menu reveals the option to color-code
the email, :guilabel:`Delete` the email, or :guilabel:`Archive` the message for potential future
use.

.. screenshot:: email_marketing-email_marketing-three-dot-dropdown
   :menu: Email Marketing ‣ Mailings
   :shows: A mailing kanban card with its three-dot drop-down menu open, showing Edit, Duplicate, Send, Test and Delete.
   :highlight: The three-dot drop-down menu (red frame).
   :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

.. _email_marketing/calendar-view:

Calendar view
-------------

The calendar view, represented by a :guilabel:`📆 (calendar)` icon, can be accessed in the
upper-right corner of the :guilabel:`Mailings` dashboard in the :guilabel:`Email Marketing` app.

While in calendar view, a monthly calendar (by default), shows when the mailings have been sent or
are scheduled to be sent.

.. screenshot:: email_marketing-email_marketing-calendar-view
   :menu: Email Marketing ‣ Mailings
   :shows: The Mailings calendar view with the mailings placed on their scheduled sending date.
   :data: Two scheduled mailings in the current month.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

The current date is represented by a :guilabel:`🔴 (red circle)` icon over the date on the calendar.

To the right of the calendar, the options to filter the results by :guilabel:`Responsible` and/or
:guilabel:`Status` are available, via checkboxes.

.. tip::
   To hide the right sidebar, click the :guilabel:`(panel-right)` icon, located above the sidebar.

In the top-left corner, above the calendar, the option to change the time period being displayed is
available via a drop-down menu, which shows :guilabel:`Month`, by default. When clicked, the
drop-down menu that appears reveals the options: :guilabel:`Day`, :guilabel:`Week`,
:guilabel:`Month` (default), :guilabel:`Year`, and :guilabel:`Show weekends` (selected by default).

Clicking any of those options changes the calendar display to reflect that desired amount of time.

Clicking either :guilabel:`⬅️ (left arrow)` icon or :guilabel:`➡️ (right arrow)` icon changes the
calendar to a previous or future time, depending on what is clicked, based on the chosen amount of
time being represented.

To jump back to the current date, click the :guilabel:`Today` button.

.. _email_marketing/graph-view:

Graph view
----------

The graph view, represented by a :guilabel:`(line graph)` icon, can be accessed in the upper-right
corner of the :guilabel:`Mailings` dashboard in the :guilabel:`Email Marketing` app.

While in graph view, the status of the emails on the :guilabel:`Mailings` page is represented in a
bar graph, but other graph view options can be implemented, if needed.

.. screenshot:: email_marketing-email_marketing-graph-view
   :menu: Email Marketing ‣ Mailings
   :shows: The Mailings graph view as a bar chart with the Measures drop-down menu next to it.
   :highlight: The Measures drop-down menu (red frame).
   :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

In the upper-left corner, above the graph, there is a :guilabel:`Measures` drop-down menu. When
clicked, different filter options become available to further customize the graph views.

Those :guilabel:`Measures` options are: :guilabel:`A/B Testing percentage` and :guilabel:`Count`
(default).

Beside the :guilabel:`Measures` drop-down menu are different graph view options. From
left-to-right, those graph view options are: :guilabel:`(bar chart)` (default), :guilabel:`(line
chart)`, and :guilabel:`(pie chart)`.

.. note::
   Each graph view option provides its own series of additional view options, which appear to the
   right of the selected graph view option.

Search options
--------------

Regardless of the view chosen for the :guilabel:`Mailings` dashboard in the :guilabel:`Email
Marketing` app, the :guilabel:`Filters`, :guilabel:`Group by`, and :guilabel:`Favorites` options are
always available to further customize the information being displayed.

To access those options, click the :guilabel:`(downward arrow)` icon, located to the right of the
search bar. Doing so reveals a drop-down mega menu featuring those filtering and grouping options.

.. screenshot:: email_marketing-email_marketing-search-mega-menu
   :menu: Email Marketing ‣ Mailings
   :shows: The search bar's drop-down mega menu with the Filters, Group By and Favorites columns side by side.
   :highlight: The three columns of the mega menu (red frame).
   :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

These options provide various ways to specify and organize the information seen on the
:guilabel:`Mailings` dashboard.

.. tabs::

   .. tab:: Filters

      This section of the drop-down mega menu provides different ways to filter email results being
      shown on the :guilabel:`Mailings` dashboard in the :guilabel:`Email Marketing` app.

      .. screenshot:: email_marketing-email_marketing-filters-dropdown
         :menu: Email Marketing ‣ Mailings
         :shows: The Filters column of the search mega menu, listing My Mailings, Sent Date, Archived and Add Custom Filter.
         :highlight: The Filters column (red frame).
         :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
         :module: mass_mailing
         :notes: English UI, light theme, 1440px width.

      The options are: :guilabel:`My Mailings`, :guilabel:`Sent Date`, :guilabel:`A/B Tests`,
      :guilabel:`A/B Tests to review`, :guilabel:`Archived`, and :guilabel:`Add Custom Filter`.

      If :guilabel:`Add Custom Filter` is selected, Odoo reveals a pop-up window, with three
      customizable fields to fill in, in order to create custom filter rules for Odoo to use to
      retrieve results that fit more specific criteria.

      .. screenshot:: email_marketing-email_marketing-add-custom-filter-popup
         :menu: Email Marketing ‣ Mailings
         :shows: The Add Custom Filter pop-up window with an editable rule and the Add / Discard buttons.
         :highlight: The rule line (red frame).
         :data: One rule on the Sent Date field.
         :module: mass_mailing
         :notes: English UI, light theme, 1440px width.

   .. tab:: Group By

      This section of the drop-down mega menu provides different ways to group email results being
      shown on the :guilabel:`Mailings` dashboard in the :guilabel:`Email Marketing` app.

      .. screenshot:: email_marketing-email_marketing-group-by-dropdown
         :menu: Email Marketing ‣ Mailings
         :shows: The Group By column of the search mega menu, listing Status, Campaign, Sent Period and Add Custom Group.
         :highlight: The Group By column (red frame).
         :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
         :module: mass_mailing
         :notes: English UI, light theme, 1440px width.

      Using this section, the data can be grouped by the messages' :guilabel:`Status`, or who it was
      :guilabel:`Sent By`.

      There is also the option to group the data by :guilabel:`Sent Period`, which has its own
      sub-menu of options to choose from. The :guilabel:`Sent Period` options are :guilabel:`Year`,
      :guilabel:`Quarter`, :guilabel:`Month`, :guilabel:`Week`, and :guilabel:`Day`.

      If none of the above :guilabel:`Group By` options deliver the desired results, click
      :guilabel:`Add Custom Group` at the bottom of the :guilabel:`Group By` section. Doing so
      reveals a drop-down menu, wherein custom criteria can be selected and applied, thus delivering
      any grouping of data that may be desired.

   .. tab:: Favorites

      This section provides the opportunity to save custom filters and/or groupings for future use.
      To utilize this section, click the :guilabel:`Save current search` field, which reveals
      additional fields.

      .. screenshot:: email_marketing-email_marketing-favorites-dropdown
         :menu: Email Marketing ‣ Mailings
         :shows: The Favorites column of the search mega menu with the Save current search entry expanded.
         :highlight: The Favorites column (red frame).
         :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
         :module: mass_mailing
         :notes: English UI, light theme, 1440px width.

      Give the favorited filter/grouping a title on the blank line above the checkboxes for
      :guilabel:`Default filter` and :guilabel:`Shared`.

      Ticking the box for :guilabel:`Default filter` makes this favorited filter/grouping the
      default option. Ticking the box for :guilabel:`Shared` allows other users to see and use this
      favorited filter/grouping.

      When all desired options are configured, click :guilabel:`Save` to save the filter/grouping in
      the :guilabel:`Favorites` section of the mega drop-down menu.

Settings
========

To view and modify the *Email Marketing* settings, navigate to :menuselection:`Email Marketing app
--> Configuration --> Settings`.

.. screenshot:: email_marketing-email_marketing-configuration-settings
   :menu: Email Marketing ‣ Configuration ‣ Settings
   :shows: The Configuration menu of the Email Marketing app opened on the Settings entry.
   :highlight: The Settings menu entry (red frame).
   :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

On the :guilabel:`Settings` page, there are four features available.

.. screenshot:: email_marketing-email_marketing-settings
   :menu: Email Marketing ‣ Configuration ‣ Settings
   :shows: The Email Marketing settings page with the Mailing Campaigns, Blacklist Options when Unsubscribing and Dedicated Server options.
   :highlight: The setting checkboxes (red frame).
   :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

The features are:

- :guilabel:`Mailing Campaigns`: enables the option to manage mass mailing campaigns.
- :guilabel:`Blacklist Option when Unsubscribing`: allows recipients to blacklist themselves from
  future mailings during the unsubscribing process.
- :guilabel:`Dedicated Server`: provides the option to utilize a separate, dedicated server for
  mailings. When enabled, Odoo reveals a new field (and link), in which the specific server
  configurations must be entered, in order for it to connect properly to Odoo.
- :guilabel:`24H Stat Mailing Reports`: allows users to check how well mailings have performed a day
  after it has been sent.

.. _email_marketing/create_email:

Create an email
===============

To create an email, open the :menuselection:`Email Marketing` application, and click the
:guilabel:`New` button in the upper-left corner of the :guilabel:`Mailings` dashboard page.

Clicking :guilabel:`New` reveals a blank email form.

.. screenshot:: email_marketing-email_marketing-blank-email-detail-form
   :menu: Email Marketing ‣ Mailings ‣ New
   :shows: A new blank mailing form with the Subject field, the Recipients field, and the Mail Body, A/B Tests and Settings tabs.
   :highlight: The Subject and Recipients fields (red frame).
   :data: Empty new mailing form.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

On the email form, there are fields for the :ref:`Subject <email_marketing/subject>` and
:ref:`Recipients <email_marketing/recipients>` of the email.

Beneath that, there are three tabs: :ref:`Mail Body <email_marketing/mail_body>`, :ref:`A/B Tests
<email_marketing/ab_tests>`, and :ref:`Settings <email_marketing/settings_tab>`.

.. _email_marketing/subject:

Subject
-------

First, enter a :guilabel:`Subject` to the email. The :guilabel:`Subject` is visible in the
recipients' inbox, allowing them to quickly see what the message is about.

.. note::
   The :guilabel:`Subject` field is mandatory. An email can **not** be sent without a
   :guilabel:`Subject`.

The :guilabel:`(smiley face with a plus sign)` icon at the end of the :guilabel:`Subject` field
represents emojis that can be added to the :guilabel:`Subject` field. Clicking that icon reveals a
pop-up menu of emojis that can be used.

Beside the :guilabel:`(smiley face with a plus sign)` icon at the end of the :guilabel:`Subject`
field is an empty :guilabel:`(star)` icon. When clicked, the :guilabel:`(star)` icon turns gold, and
the email is saved as a template in the :guilabel:`Mail Body` tab, which can be used again in the
future.

.. _email_marketing/recipients:

Recipients
----------

Beneath the :guilabel:`Subject` field on the email form is the :guilabel:`Recipients` field. In this
field, select the recipients of the email. By default, the :guilabel:`Mailing List` option is
selected, but clicking the field reveals a drop-down menu of other recipient options.

With the default :guilabel:`Mailing List` option selected, a specific mailing list **must** be
chosen from the adjacent :guilabel:`Select mailing lists` field drop-down menu.

.. tip::
   More than one mailing list can be chosen from the :guilabel:`Select mailing lists` field.

Odoo then sends the email to contacts on that specific mailing list(s).

.. seealso::
   :doc:`email_marketing/mailing_lists`

When the :guilabel:`Recipients` field is clicked, a drop-down menu of other options is revealed.
Each option provides different ways Odoo can create a target audience for the email.

.. screenshot:: email_marketing-email_marketing-recipients-dropdown
   :menu: Email Marketing ‣ Mailings ‣ New
   :shows: The Recipients drop-down menu of a mailing, listing the available target models (Mailing List, Contact, Lead/Opportunity, Sales Order, Event Registration, …).
   :highlight: The Recipients drop-down menu (red frame).
   :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

Those options (excluding the default :guilabel:`Mailing List`) provide the option to create a more
specified recipient filter, in an equation-like format, which appears beneath the
:guilabel:`Recipients` field.

The :guilabel:`Recipients` field options, other than the default :guilabel:`Mailing List` option,
are as follows:

- :guilabel:`Contact`: ties specifically to the *Contacts* app, and includes all the contacts
  entered in the database.
- :guilabel:`Event Registration`: ties specifically to the *Events* app, and provides opportunities
  to interact with event registrants, in order to communicate important information about the
  event(s), or nurture other valuable actions, such as post-event surveys, purchases, etc.
- :guilabel:`Lead/Opportunity`: ties specifically to records in the *CRM* application, which opens
  up a number of opportunities to influence sales or purchase decisions.
- :guilabel:`Mailing Contact`: ties specifically to the *Email Marketing* app, and focuses on
  specific mailing contacts that have been entered in that specific application, and are related to
  a specific mailing list. These contacts are also unique because they do *not* have their own
  contact card in the *Contacts* application. This list can be accessed by navigating to
  :menuselection:`Email Marketing app --> Mailing Lists --> Mailing List Contacts`.
- :guilabel:`Sales Order`: ties specifically to the *Sales* app, and focuses on a specific sales
  orders in the database.

Add recipient filter
~~~~~~~~~~~~~~~~~~~~

To add a more specific recipient filter to any :guilabel:`Recipient` option, select any recipient
option (other than :guilabel:`Mailing List`), and click the :guilabel:`Modify filter (right-facing
arrow)` icon beneath the :guilabel:`Recipient` field to reveal three subsequent filter rule fields,
formatted like an equation.

It is highly recommended that users implement detailed targeting criteria for the
:guilabel:`Recipients` field. Typically, a single line of targeting logic is not sufficient enough
for an email campaign.

While the :guilabel:`Mailing List` option is adequate for the :guilabel:`Recipients` field, the
:guilabel:`Lead/Opportunity` and :guilabel:`Event Registration` options provide far more detailed
targeting criteria, which can be added on top of those seed sources.

.. example::
   For example, with the :guilabel:`Lead/Opportunity` option chosen in the :guilabel:`Recipients`
   field, users can add various custom criteria related to :guilabel:`Created on` dates,
   :guilabel:`Stages`, :guilabel:`Tags`, :guilabel:`Lost Reasons`, :guilabel:`Sales Teams`,
   :guilabel:`Active` statuses, :guilabel:`Country`, and so much more.

   .. screenshot:: email_marketing-email_marketing-detailed-filter-records
      :menu: Email Marketing ‣ Mailings ‣ New
      :shows: The Recipients field set to a model other than Mailing List, with the expanded rule builder showing several filter rules.
      :highlight: The rule builder (red frame).
      :data: Two rules on the Contact model.
      :module: mass_mailing
      :notes: English UI, light theme, 1440px width.

To reveal the sub-menu options within the filter rule fields, click each field, and make the desired
selections, until the preferred configuration has been achieved.

The number of :guilabel:`records` in the database that match the configured rule(s) are indicated
beneath the configured filter rule(s), in green.

.. screenshot:: email_marketing-email_marketing-filter-records
   :menu: Email Marketing ‣ Mailings ‣ New
   :shows: The Recipients field with a single filter rule and the record counter below it.
   :highlight: The record counter (red frame).
   :data: About 120 matching records.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

.. note::
   Some sub-menu options in the first rule field allow for a second choice to provide even more
   specificity.

To the right of each rule, there are three additional options, represented by :guilabel:`➕ (plus
sign)`, :guilabel:`(sitemap)`, and :guilabel:`🗑️ (trash)` icons.

- The :guilabel:`➕ (plus sign)` icon adds a new node (line) to the overall targeting logic.
- The :guilabel:`(sitemap)` icon adds a branch to the node. A branch contains two additional,
  indented sub-nodes that are related to that specific rule, providing even more specificity to the
  parent line above it.
- The :guilabel:`🗑️ (trash)` icon deletes a specific node (line) in the array of logic.

.. _email_marketing/mail_body:

Mail Body tab
-------------

In the :guilabel:`Mail Body` tab, there are a number of pre-configured message templates to choose
from.

.. screenshot:: email_marketing-email_marketing-mail-body-templates
   :menu: Email Marketing ‣ Mailings ‣ New ‣ Mail Body tab
   :shows: The Mail Body tab showing the gallery of email design templates to start from.
   :highlight: The template gallery (red frame).
   :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

Select the desired template, and proceed to modify every element of its design details with Odoo's
drag-and-drop building blocks, which appear on the right sidebar when a template is chosen.

.. screenshot:: email_marketing-email_marketing-template-building-blocks
   :menu: Email Marketing ‣ Mailings ‣ New ‣ Mail Body tab
   :shows: The Mail Body tab with a template chosen and the building-block panel open on the right.
   :highlight: The building-block panel (red frame).
   :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

The features on the sidebar used to create and customize emails are separated into three sections:
:guilabel:`Blocks`, :guilabel:`Customize`, and :guilabel:`Design`.

Each building block provides unique features and professional design elements. To use a building
block, drag-and-drop the desired block element onto the body of the email being built. Once dropped,
various aspects of the building block can be customized.

.. tip::
   To build an email from the ground up, without any building block elements, select the
   :guilabel:`Plain Text` template. When selected, Odoo provides a completely blank email canvas,
   which can be customized in a number of way using the front-end rich text editor that accepts
   forward slash `/` commands.

   When `/` is typed into the blank body of the email, while using a :guilabel:`Plain Text`
   template, a drop-down menu of various design elements appears, which can be used to create the
   desired email design.

   .. screenshot:: email_marketing-email_marketing-template-blank-slash
      :menu: Email Marketing ‣ Mailings ‣ New ‣ Mail Body tab
      :shows: The Start From Scratch template with the powerbox drop-down menu opened by typing a forward slash in the body.
      :highlight: The powerbox drop-down menu (red frame).
      :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
      :module: mass_mailing
      :notes: English UI, light theme, 1440px width.

.. _email_marketing/ab_tests:

A/B Tests tab
-------------

Initially, when the :guilabel:`A/B Tests` tab is opened on an email form, the only option available
is :guilabel:`Allow A/B Testing`. This is **not** a required option.

If this option is enabled, recipients are only mailed *once* for the entirety of the campaign.

This allows the user to send different versions of the same mailing to randomly selected recipients
to gauge the effectiveness of various designs, formats, layouts, content, and so on -- without any
duplicate messages being sent.

When the checkbox beside :guilabel:`Allow A/B Testing` is ticked, an :guilabel:`on (%)` field
appears, in which the user determines the percentage of the pre-configured recipients that are going
to be sent this current version of the mailing as part of the test.

.. note::
   The default figure in the :guilabel:`on (%)` field is `10`, but that figure can be changed at any
   time.

Beneath that, two additional fields appear:

The :guilabel:`Winner Selection` field provides a drop-down menu of options, wherein the user
decides what criteria should be used to determine the "winning" version of the email tests that are
sent.

The options in the :guilabel:`Winner Selection` field are as follows:

- :guilabel:`Manual`: allows the user to determine the "winning" version of the mailing. This option
  removes the :guilabel:`Send Final On` field.
- :guilabel:`Highest Open Rate` (default): the mailing with the highest open rate is determined to
  be the "winning" version.
- :guilabel:`Highest Click Rate`: the mailing with the highest click rate is determined to be the
  "winning" version.
- :guilabel:`Highest Reply Rate`: the mailing with the highest reply rate is determined to be the
  "winning" version.
- :guilabel:`Leads`: the mailing with the most leads generated is determined to be the "winning"
  version.
- :guilabel:`Quotations`: the mailing with the most quotations generated is determined to be the
  "winning" version.
- :guilabel:`Revenues`: the mailing with the most revenue generated is determined to be the
  "winning" version.

The :guilabel:`Send Final On` field allows users to choose a date that is used to know *when* Odoo
should determine the "winning" email, and subsequently, send that version of the email to the
remaining recipients.

.. screenshot:: email_marketing-email_marketing-ab-test-tab
   :menu: Email Marketing ‣ Mailings ‣ New ‣ A/B Tests tab
   :shows: The A/B Tests tab with Allow A/B Testing enabled, the percentage of recipients, the winner selection criteria and the Create an Alternative Version button.
   :highlight: The Allow A/B Testing checkbox and the winner criteria (red frame).
   :data: 15 % of recipients, winner selected on highest open rate.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

To the right of those fields is a :guilabel:`Create an Alternative Version` button. When clicked,
Odoo presents a new :guilabel:`Mail Body` tab for the user to create an alternate version of the
email to test.

.. _email_marketing/settings_tab:

Settings tab
------------

The options present in the :guilabel:`Settings` tab of the mail form are divided into two sections:
:guilabel:`Email Content` and :guilabel:`Tracking`.

.. note::
   The options available in the :guilabel:`Settings` tab vary depending on if the *Mailing
   Campaigns* feature is activated in :menuselection:`Email Marketing --> Configuration -->
   Settings`. See :ref:`email_marketing/mailing-campaigns` for more information.

Without the *Mailing Campaigns* feature activated, the :guilabel:`Settings` tab on the email form
only contains the :guilabel:`Preview Text`, :guilabel:`Send From`, :guilabel:`Reply To`,
:guilabel:`Attachments`, and :guilabel:`Responsible` fields.

.. screenshot:: email_marketing-email_marketing-settings-without-features
   :menu: Email Marketing ‣ Mailings ‣ New ‣ Settings tab
   :shows: The Settings tab of a mailing without the Mailing Campaigns setting enabled: Mail Subject, Preview Text, Send From, Reply To and Attach a file.
   :highlight: The Settings tab (red frame).
   :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

Email content
~~~~~~~~~~~~~

- :guilabel:`Preview Text`: allows the user to enter a preview sentence to encourage recipients to
  open the email. In most inboxes, this is displayed next to the subject. If left empty, the first
  characters of the email content appear, instead. The ability to add an emoji in this field is
  available, as well, via the :guilabel:`(smiley face with a plus sign)` icon.
- :guilabel:`Send From`: designate an email alias that displays as the sender of this particular
  email.
- :guilabel:`Reply To`: designate an email alias to whom all the replies of this particular email
  are sent.
- :guilabel:`Attach a file`: if any specific files are required (or helpful) for this email, click
  the :guilabel:`Attachments` button, and upload the desired file(s) to the email.

Tracking
~~~~~~~~

- :guilabel:`Responsible`: designate a user in the database to be responsible for this particular
  email.

.. note::
   If the *Mailing Campaign* feature *is* activated, an additional :guilabel:`Campaign` field
   appears in the :guilabel:`Tracking` section of the :guilabel:`Settings` tab.

   .. screenshot:: email_marketing-email_marketing-settings-tab-with-campaign
      :menu: Email Marketing ‣ Mailings ‣ New ‣ Settings tab
      :shows: The Settings tab of a mailing with the Mailing Campaigns setting enabled, showing the additional Campaign and Tracking (Medium, Source) fields.
      :highlight: The Campaign field (red frame).
      :data: Campaign 'Spring sale'.
      :module: mass_mailing
      :notes: English UI, light theme, 1440px width.

   The additional :guilabel:`Campaign` field allows users to attach this particular email to a
   mailing campaign, if desired.

   If the desired campaign is not available in the initial drop-down menu, select :guilabel:`Search
   More` to reveal a complete list of all mailing campaigns in the database.

   Or, type the name of the desired mailing campaign in the :guilabel:`Campaign` field, until Odoo
   reveals the desired campaign in the drop-down menu. Then, select the desired campaign.

Send, schedule, test
====================

Once the mailing is finalized, the following options can be utilized, via buttons located in the
upper-left corner of the email form: :ref:`Send <email_marketing/send>`, :ref:`Schedule
<email_marketing/schedule>`, and :ref:`Test <email_marketing/test>`.

.. _email_marketing/send:

Send
----

The :guilabel:`Send` button reveals a :guilabel:`Ready to unleash emails?` pop-up window.

.. screenshot:: email_marketing-email_marketing-send-popup
   :menu: Email Marketing ‣ Mailings ‣ New ‣ Send
   :shows: The Ready to unleash emails? confirmation pop-up window with the recipient count and the Send to all button.
   :highlight: The Send to all button (red frame).
   :data: About 120 recipients.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

When the :guilabel:`Send to all` button is clicked, Odoo sends the email to the desired recipients.
Once Odoo has sent the mailing, the status changes to :guilabel:`Sent`.

.. _email_marketing/schedule:

Schedule
--------

The :guilabel:`Schedule` button reveals a :guilabel:`When do you want to send your mailing?` pop-up
window.

.. screenshot:: email_marketing-email_marketing-schedule-popup
   :menu: Email Marketing ‣ Mailings ‣ New ‣ Schedule
   :shows: The schedule pop-up window with the date/time field for the planned sending.
   :highlight: The date/time field (red frame).
   :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

In this pop-up window, click the :guilabel:`Send on` field to reveal a calendar pop-up window.

.. screenshot:: email_marketing-email_marketing-schedule-popup-calendar
   :menu: Email Marketing ‣ Mailings ‣ New ‣ Schedule
   :shows: The schedule pop-up window with the calendar picker opened on the sending date.
   :highlight: The calendar picker (red frame).
   :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

From the calendar pop-up window, select the future date and time for Odoo to send this email. Then,
click :guilabel:`✔️ Apply`. When a date and time are chosen, click the :guilabel:`Schedule` button,
and the status of the mailing changes to :guilabel:`In Queue`.

.. _email_marketing/test:

Test
----

The :guilabel:`Test` button reveals a :guilabel:`Test Mailing` pop-up window.

.. screenshot:: email_marketing-email_marketing-test-popup
   :menu: Email Marketing ‣ Mailings ‣ New ‣ Test
   :shows: The Test Mailing pop-up window with the recipient email field and the Send Test button.
   :highlight: The recipient email field (red frame).
   :data: One test address.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

From this pop-up window, enter the email addresses of the contacts to whom Odoo should send this
test email in the :guilabel:`Recipients` field. Multiple contacts can be added in this field, if
desired.

Once all the desired email addresses have been entered in the :guilabel:`Recipients` field, click
the :guilabel:`Send Test` button.

.. warning::
   By default, there's a daily limit applied for **all emails** sent throughout **all
   applications**. So, if there are remaining emails to be sent after a limit has been reached,
   those mailings are **not** sent automatically the next day. The sending needs to be forced, by
   opening the email and clicking :guilabel:`Retry`.

.. _email_marketing/mailing-campaigns:

Mailing campaigns
=================

The *Email Marketing* application provides users with the ability to build mailing campaigns.

In order to create and customize mailing campaigns, the *Mailing Campaigns* feature **must** be
activated in the *Settings* page of the *Email Marketing* application. To do that, navigate to
:menuselection:`Email Marketing app --> Configuration --> Settings`, tick the box beside
:guilabel:`Mailing Campaigns`, and click the :guilabel:`Save` button.

.. screenshot:: email_marketing-email_marketing-campaigns-feature
   :menu: Email Marketing ‣ Configuration ‣ Settings
   :shows: The Email Marketing settings page with the Mailing Campaigns checkbox enabled.
   :highlight: The Mailing Campaigns setting (red frame).
   :data: Demo mailings 'Newsletter' and 'Product launch'; mailing lists 'Newsletter (HU)' and 'Webshop customers'.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

Once the :guilabel:`Mailing Campaigns` feature is activated, a new :guilabel:`Campaigns` menu option
appears in the header.

When that is clicked, Odoo reveals a separate :guilabel:`Campaigns` page, displaying all the mailing
campaigns in the database, and the current stage they are in, showcased in a default Kanban view.

.. screenshot:: email_marketing-email_marketing-campaigns-page
   :menu: Email Marketing ‣ Campaigns
   :shows: The Campaigns kanban grouped by stage, each card showing the campaign name, the responsible and the mailings it contains.
   :data: Three campaigns in different stages.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

.. note::
   This information can also be viewed in a list, by clicking the :guilabel:`☰ (horizontal lines)`
   icon in the upper-right corner.

Clicking any campaign from the :guilabel:`Campaigns` page reveals that campaign's form.

There are two different ways to create and customize campaigns in the *Email Marketing* application,
either directly from the :ref:`Campaigns page <email_marketing/campaign-page>` or through the
:ref:`Settings tab <email_marketing/campaign-settings>` on an email form.

.. _email_marketing/campaign-page:

Create mailing campaign (from campaigns page)
---------------------------------------------

When the *Mailing Campaigns* feature is activated, a new *Campaigns* option appears in the header of
the *Email Marketing* application. Campaigns can be created directly on the *Campaigns* page in the
*Email Marketing* app.

To do that, navigate to :menuselection:`Email Marketing app --> Campaigns --> New`.

Kanban view
~~~~~~~~~~~

When the :guilabel:`New` button is clicked in the default Kanban view on the :guilabel:`Campaigns`
page, a Kanban card appears in the :guilabel:`New` stage.

.. screenshot:: email_marketing-email_marketing-campaigns-kanban-popup
   :menu: Email Marketing ‣ Campaigns ‣ New
   :shows: The inline quick-create card on the Campaigns kanban with the Campaign Name, Responsible and Tags fields.
   :highlight: The quick-create card (red frame).
   :data: New campaign 'Spring sale'.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

New campaign cards can also be made by clicking the :guilabel:`➕ (plus sign)` at the top of any
Kanban stage on the :guilabel:`Campaigns` page.

When the new campaign Kanban card appears, the options to enter a :guilabel:`Campaign Name`, a
:guilabel:`Responsible`, and :guilabel:`Tags` become readily available.

To add the campaign to the Kanban stage, click the :guilabel:`Add` button.

To delete the campaign, click the :guilabel:`🗑️ (trash can)` icon.

To further customize the campaign, click the :guilabel:`Edit` button, which reveals the campaign
form for additional modifications.

.. note::
   A :guilabel:`Campaign Name` **must** be entered in the Kanban card, in order for the
   :guilabel:`Edit` button to reveal the campaign form for further modifications.

List view
~~~~~~~~~

To enter the list view on the :guilabel:`Campaigns` page, click the :guilabel:`☰ (horizontal lines)`
icon in the upper-right corner. Doing so reveals all campaign information in a list format.

.. screenshot:: email_marketing-email_marketing-campaign-page-list-view
   :menu: Email Marketing ‣ Campaigns
   :shows: The Campaigns list view with the Campaign Name, Responsible, Revenues, Quotations, Opportunities and Clicks columns.
   :data: Three campaigns.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

To create a campaign from the :guilabel:`Campaigns` page while in list view, click the
:guilabel:`New` button. Doing so reveals a blank campaign form.

.. screenshot:: email_marketing-email_marketing-blank-campaign-form
   :menu: Email Marketing ‣ Campaigns ‣ New
   :shows: A new blank campaign form with the Campaign Name, Responsible and Tags fields.
   :highlight: The Campaign Name field (red frame).
   :data: Empty new campaign form.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

From this campaign form, a :guilabel:`Campaign Name`, a :guilabel:`Responsible`, and
:guilabel:`Tags` can be added.

At the top of the form, various metric-related smart buttons can be seen that showcase specific
analytics related to the campaign. Those smart buttons are: :guilabel:`Revenues`,
:guilabel:`Quotations`, :guilabel:`Opportunities`, and :guilabel:`Clicks`.

.. note::
   Once a :guilabel:`Campaign Name` is entered and saved, additional buttons appear at the top of
   the campaign form.

   Those additional buttons are: :guilabel:`Send Mailing` and :guilabel:`Send SMS`.

Campaign form
-------------

On the campaign form (after clicking :guilabel:`Edit` from the Kanban card, or selecting an existing
campaign from the :guilabel:`Campaigns` page) there are additional options and metrics available.

.. screenshot:: email_marketing-email_marketing-campaign-form
   :menu: Email Marketing ‣ Campaigns ‣ (campaign)
   :shows: A saved campaign form with the Revenues, Quotations, Opportunities and Clicks smart buttons and the Send Mailing and Send SMS buttons.
   :highlight: The smart button row and the Send Mailing / Send SMS buttons (red frame).
   :data: Campaign 'Spring sale' with one mailing sent.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

At the top of the form, various smart buttons can be seen that showcase specific analytics related
to the campaign. Those smart buttons are: :guilabel:`Revenues`, :guilabel:`Quotations`,
:guilabel:`Opportunities`, and :guilabel:`Clicks`.

There are also buttons to :guilabel:`Send Mailing` and :guilabel:`Send SMS`.

.. note::
   If the :guilabel:`Send Mailing` and :guilabel:`Send SMS` buttons are not readily available, enter
   a :guilabel:`Campaign Name`, then save (either manually or automatically). Doing so reveals those
   buttons.

The status of the campaign can be viewed in the upper-right corner of the campaign form, as well.

.. _email_marketing/campaign-settings:

Create mailing campaign (from settings tab)
-------------------------------------------

To create a new campaign from the :guilabel:`Settings` tab of a mailing form, click the
:guilabel:`Campaign` field, and start typing the name of the new campaign. Then, select either
:guilabel:`Create "[Campaign Name]"` or :guilabel:`Create and edit...` from the drop-down menu that
appears.

.. screenshot:: email_marketing-email_marketing-mailing-campaign-settings
   :menu: Email Marketing ‣ Mailings ‣ New ‣ Settings tab
   :shows: The Campaign field of a mailing's Settings tab with a new campaign name typed in and the Create "…" / Create and edit… options shown.
   :highlight: The Campaign field drop-down (red frame).
   :data: New campaign name 'Spring sale' being typed.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

Select :guilabel:`Create` to add this new mailing campaign to the database, and modify its settings
in the future.

Select :guilabel:`Create and Edit...` to add this new mailing campaign to the database, and reveal a
:guilabel:`Create Campaign` pop-up window.

.. screenshot:: email_marketing-email_marketing-mailing-campaign-popup
   :menu: Email Marketing ‣ Mailings ‣ New ‣ Settings tab ‣ Create and edit…
   :shows: The Create Campaign pop-up window with the Campaign Name, Responsible, Tags and status, and the Save & Close / Discard buttons.
   :highlight: The Campaign Name and Responsible fields (red frame).
   :data: Campaign 'Spring sale', responsible 'Mitchell Admin'.
   :module: mass_mailing
   :notes: English UI, light theme, 1440px width.

Here, the new mailing campaign can be further customized. Users can adjust the :guilabel:`Campaign
Name`, assign a :guilabel:`Responsible`, and add :guilabel:`Tags`.

There is also a status located in the upper-right corner of the :guilabel:`Create Campaign` pop-up
window.

When all modifications are ready to be finalized, click :guilabel:`Save & Close`. To delete the
entire campaign, click :guilabel:`Discard`.

.. seealso::
   - :doc:`email_marketing/mailing_lists`
   - :doc:`email_marketing/unsubscriptions`
   - :doc:`email_marketing/lost_leads_email`
   - :doc:`email_marketing/analyze_metrics`

.. toctree::
   :titlesonly:

   email_marketing/mailing_lists
   email_marketing/unsubscriptions
   email_marketing/lost_leads_email
   email_marketing/analyze_metrics

=======
Chatter
=======

.. |user| replace:: :icon:`fa-user-o` :guilabel:`(user)` icon
.. |paperclip| replace:: :icon:`fa-paperclip` :guilabel:`(paperclip)` icon
.. |ve| replace:: :icon:`fa-ellipsis-v` :guilabel:`(vertical ellipsis)`

The *Chatter* feature is integrated throughout Odoo to streamline communication, maintain
traceability, and provide accountability among team members. Chatter windows, known as *composers*,
are located on almost every record within the database, and allow users to communicate with both
internal users and external contacts.

Chatter composers also enable users to log notes, upload files, and schedule activities.

Chatter thread
==============

A *chatter thread* can be found on most pages in the database, and serves as a record of the updates
and edits made to a record. A note is logged in the chatter thread when a change is made to the
record. The note includes details of the change, and a time stamp.

.. example::
   A user, Mitchell Admin, needs to update the email address of a contact. After they save the
   changes to the contact record, a note is logged in the chatter of the contact record with the
   following information:

   - The date when the change occurred.
   - The email address as it was previously listed.
   - The updated email address.

   .. screenshot:: productivity-chatter-thread-update
      :menu: (any record with a chatter)
      :shows: A chatter thread showing a logged note and a tracked field change on a contact record.
      :data: Contact "Deco Addict" with one tracked change.
      :module: mail
      :notes: English UI, light theme, crop to the chatter.

If a record was created, or edited, via an imported file, or was otherwise updated through an
intervention by the system, the chatter thread creates a log note, and credits the change to
OdooBot.

.. screenshot:: productivity-chatter-creation-message
   :menu: (any record with a chatter)
   :shows: The first chatter message of a newly created record, logged automatically.
   :data: New contact record.
   :module: mail
   :notes: English UI, light theme, crop to the chatter.

.. _discuss/add-followers:

Add followers
=============

A *follower* is a user or contact that is added to a record and is notified when the record is
updated, based on specific :ref:`follower subscription settings <discuss/edit-subscription>`.
Followers can add themselves, or can be added by another user.

.. note::
   If a user creates, or is assigned to a record, they are automatically added as a follower.

To follow a record, navigate to any record with a chatter thread. For example, to open a *CRM*
opportunity, navigate to :menuselection:`CRM app --> Sales --> My Pipeline`, and select an
opportunity from the list to open it.

At the top-right, above the chatter composer, click :guilabel:`Follow`. Doing this changes the
button to read :guilabel:`Following`. Click it again to :guilabel:`Unfollow`.

Manage followers
----------------

To add another user, or contact, as a follower, click the |user|. This opens a drop-down list of the
current followers. Click :guilabel:`Add Followers` to open an :guilabel:`Invite Follower` pop-up
window.

Select one or more contacts from the :guilabel:`Recipients` drop-down list. To notify the contacts,
tick the :guilabel:`Send Notification` checkbox. Edit the message template as desired, then click
:guilabel:`Add Followers`.

To remove followers, click the |user| to open the current followers list. Find the name of the
follower to be removed, and click the :icon:`fa-remove` :guilabel:`(remove)` icon.

.. _discuss/edit-subscription:

Edit follower subscription
--------------------------

The updates a follower receives can vary based on their subscription settings. To see the type of
updates a follower is subscribed to, and to edit the list, click the |user|. Find the appropriate
follower in the list, then click the :icon:`fa-pencil` :guilabel:`(pencil)` icon. This opens the
:guilabel:`Edit Subscription` pop-up window for the follower.

The list of available subscription settings varies depending on the record type. For example, a
follower of a *Project* task may be informed when the task's stage changes. This option would not be
available for the followers of a *CRM* opportunity.

Tick the checkbox for any updates the follower should receive, and clear the checkbox for any
updates they should **not** receive. Click :guilabel:`Apply` when finished.

.. screenshot:: productivity-chatter-edit-subscription
   :menu: (any record with a chatter)
   :shows: The "Edit Subscription" window of a follower, listing the subscription types that can be checked or unchecked.
   :highlight: The subscription checkboxes (red frame).
   :data: Follower of a sales order.
   :module: mail
   :notes: English UI, light theme, crop to the chatter.

.. _discuss/log-notes:

Log notes
=========

The chatter function includes the ability to log internal notes on individual records. These notes
are only accessible to internal users, and are available on any records that feature a chatter
thread.

To log an internal note, first navigate to a record. For example, to open a *CRM* opportunity,
navigate to :menuselection:`CRM app --> Sales --> My Pipeline`, and click on the Kanban card of an
opportunity to open it. Then, at the top-right, above the chatter composer, click :guilabel:`Log
note`.

Enter the note in the chatter composer. To tag an internal user, type `@`, and begin typing the name
of the person to tag. Then, select a name from the drop-down menu. Depending on their notification
settings, the user is notified by email, or through Odoo.

.. important::
   Outside contacts can also be tagged in an internal log note. The contact then receives an email
   with the contents of the note they were tagged in, including any attachments added directly to
   the note. If they respond to the email, their response is logged in the chatter, and they are
   added to the record as a follower.

   Outside contacts are **not** able to log in to view the entire chatter thread, and are only
   notified of specific updates, based on their :ref:`follower subscription settings
   <discuss/edit-subscription>`, or when they are tagged directly.

.. _discuss/send-messages:

Send messages
=============

Chatter composers can send messages to outside contacts, without having to leave the database, or
open a different application. This makes it easy to communicate with potential customers in the
*Sales* and *CRM* applications, or vendors in the *Purchase* app.

To send a message, first navigate to a record. For example, to send a message from a *CRM*
opportunity, navigate to :menuselection:`CRM app --> Sales --> My Pipeline`, and click on the Kanban
card of an opportunity to open it. Then, at the top-right, above the chatter composer, click
:guilabel:`Send message`.

.. tip::
   Press :command:`Ctrl + Enter` to send a message, instead of using the :guilabel:`Send` button.

If any :ref:`followers <discuss/add-followers>` have been added to the record, they are added as
recipients of the message.

.. warning::
   :ref:`Followers <discuss/add-followers>` of a record are added as recipients of a message
   automatically. If a follower should **not** receive a message, they must be removed as a follower
   before the message is sent, or a note is logged.

.. screenshot:: productivity-chatter-send-message
   :menu: CRM ‣ Sales ‣ My Pipeline
   :shows: The chatter composer of an opportunity in "Send message" mode, with the recipients (followers and the customer) listed above the composer.
   :highlight: The recipient list (red frame).
   :data: Opportunity of customer "Deco Addict".
   :module: mail
   :notes: English UI, light theme, crop to the chatter.

Expand full composer
--------------------

The chatter composer can be expanded to a larger pop-up window, allowing for additional
customizations.

To open the full composer, click the :icon:`fa-expand` :guilabel:`(expand)` icon in the bottom-right
corner of the composer window.

.. screenshot:: productivity-chatter-expand-icon
   :menu: (any record with a chatter)
   :shows: A chatter composer with the expand icon that opens the full composer.
   :highlight: The expand icon (red frame).
   :module: mail
   :notes: English UI, light theme, crop to the chatter.

Doing this opens a :guilabel:`Compose Email` pop-up window. Confirm or edit the intended
:guilabel:`Recipients` of the message, or add additional recipients. The :guilabel:`Subject` field
auto-populates based on the title of the record, though it can be edited, if desired.

To use an :doc:`email template <../../general/companies/email_template/>` for the message, click the
|ve| icon, then select a template from the list. Existing templates can also be overwritten or
deleted from this menu.

.. note::
   The number and type of templates available vary, based on the record the message is created from.

Click :icon:`fa-paperclip` :guilabel:`(paperclip)` icon to add any files to the message, then click
:guilabel:`Send`.

.. screenshot:: productivity-chatter-full-composer
   :menu: CRM ‣ Sales ‣ My Pipeline
   :shows: The expanded full composer with the subject, the rich-text body, the attachment button and the email template selector.
   :data: Opportunity of customer "Deco Addict".
   :module: mail
   :notes: English UI, light theme, crop to the chatter.

Generate text with AI
~~~~~~~~~~~~~~~~~~~~~

To generate message text using AI, click the AI icon from the expanded chatter composer. This opens
a :guilabel:`Generate Text with AI` pop-up.

Enter a prompt in the :guilabel:`Send a message` field to instruct the AI on the type of content
needed, then press enter, or click the :icon:`fa-paper-plane` :guilabel:`(paper plane)` icon.

.. screenshot:: productivity-chatter-ai-prompt
   :menu: (any record with a chatter)
   :shows: The "Generate Text with AI" pop-up with a prompt typed in the message field.
   :data: Prompt asking for a short follow-up email.
   :module: mail
   :notes: English UI, light theme, crop to the chatter.

After the text is generated, click :guilabel:`Insert` to insert the text into the message composer.

.. tip::
   Before sending the final message, be sure to edit any commentary from the AI, or any text in
   brackets.

   .. screenshot:: productivity-chatter-ai-draft
      :menu: (any record with a chatter)
      :shows: The composer filled with the text generated by the AI, before it is edited and sent.
      :module: mail
      :notes: English UI, light theme, crop to the chatter.

Edit sent messages
------------------

Messages can be edited after they are sent, to fix typos, correct mistakes, or add missing
information.

.. note::
   When messages are edited after they have been sent, an updated message is **not** sent to the
   recipient.

To edit a sent message, click the |ve| menu to the right of the message. Then, select
:guilabel:`Edit`. Make any necessary adjustments to the message.

.. screenshot:: productivity-chatter-edit-message
   :menu: (any record with a chatter)
   :shows: The dropdown menu of a sent chatter message with the "Edit" option.
   :highlight: The "Edit" option (red frame).
   :module: mail
   :notes: English UI, light theme, crop to the chatter.

To save the changes, press :command:`Ctrl + Enter`. To discard the changes, press :command:`Escape`.

.. important::
   Users with Admin-level access rights can edit any sent messages. Users without Admin rights can
   **only** edit messages they created.

.. _discuss/search-messages:

Search messages
===============

Chatter threads can become long after a while, because of all the information they contain. To make
it easier to find a specific entry, users can search the text of messages and notes for specific
keywords.

First, select a record with a chatter thread. For example, to search a *CRM* opportunity, navigate
to :menuselection:`CRM app --> Sales --> My Pipeline`, and click on the Kanban card of an
opportunity to open it. Then, at the top-right, above the chatter composer, click the
:icon:`oi-search` :guilabel:`(search)` icon to open the search bar.

Enter a keyword or phrase into the search bar, then hit :command:`Enter`, or click the
:icon:`oi-search` :guilabel:`(search)` icon to the right of the search bar. Any messages or notes
containing the keyword or phrase entered are listed below the search bar, with the keyword
highlighted.

To be taken directly to a particular message in the chatter thread, hover over the upper-right
corner of the result to reveal a :guilabel:`Jump` button. Click this button to be directed to that
message's location in the thread.

.. screenshot:: productivity-chatter-search
   :menu: (any record with a chatter)
   :shows: Search results in a chatter thread, with the search icon in the top bar and the "Jump" option on a hovered result.
   :highlight: The search icon and the "Jump" option (red frame).
   :module: mail
   :notes: English UI, light theme, crop to the chatter.

.. _discuss/schedule-activities:

Schedule activities
===================

*Activities* are follow-up tasks tied to a record in an Odoo database. Activities can be scheduled
on any database page that contains a chatter thread, Kanban view, list view, or activities view of
an application.

To schedule an activity through a chatter thread, click the :guilabel:`Activities` button, located
at the top of the chatter on any record. On the :guilabel:`Schedule Activity` pop-up window that
appears, select an :guilabel:`Activity Type` from the drop-down menu.

.. tip::
   Individual applications have a list of *Activity Types* dedicated to that application. For
   example, to view and edit the activities available for the *CRM* application, go to
   :menuselection:`CRM app --> Configuration --> Activity Types`.

Enter a title for the activity in the :guilabel:`Summary` field, located in the :guilabel:`Schedule
Activity` pop-up window.

Select a name from the :guilabel:`Assigned to` drop-down menu to assign the activity to a different
user. Otherwise, the user creating the activity is automatically assigned.

Add any additional information in the optional :guilabel:`Log a note...` field.

.. note::
   The :guilabel:`Due Date` field on the :guilabel:`Schedule Activity` pop-up window auto-populates
   based on the configuration settings for the selected :guilabel:`Activity Type`. However, this
   date can be changed by selecting a day on the calendar in the :guilabel:`Due Date` field.

Lastly, click one of the following buttons:

- :guilabel:`Schedule`: adds the activity to the chatter under :guilabel:`Planned activities`.
- :guilabel:`Schedule & Mark as Done`: adds the details of the activity to the chatter under
  :guilabel:`Today`. The activity is added to :guilabel:`Today`, and is automatically marked as
  done.
- :guilabel:`Done \& Schedule Next`: adds the task under :guilabel:`Today` marked as done, and opens
  a new activity window.
- :guilabel:`Cancel`: discards any changes made on the pop-up window.

Scheduled activities are added to the chatter for the record under :guilabel:`Planned activities`,
and are color-coded based on their due date.

- **Red** icons indicate an overdue activity.
- **Yellow** icons indicate an activity with a due date scheduled for the current date.
- **Green** icons indicate an activity with a due date scheduled in the future.

.. screenshot:: productivity-chatter-activity-icons
   :menu: CRM ‣ Sales ‣ My Pipeline
   :shows: A chatter thread with several planned activities, showing the colored due-date icons.
   :data: Three activities: overdue, due today and planned.
   :module: mail
   :notes: English UI, light theme, crop to the chatter.

.. tip::
   Click the :icon:`fa-info-circle` :guilabel:`(info)` icon next to a planned activity to see
   additional details.

   .. screenshot:: productivity-chatter-activity-details
      :menu: CRM ‣ Sales ‣ My Pipeline
      :shows: The detail popover of a planned activity with its type, due date, assignee and note.
      :data: Activity "Call" due today.
      :module: mail
      :notes: English UI, light theme, crop to the chatter.

After completing an activity, click :guilabel:`Mark Done` under the activity entry in the chatter.
This opens a :guilabel:`Mark Done` pop-up window, where additional notes about the activity can be
entered. After adding any comments to the pop-up window, click: :guilabel:`Done \& Schedule Next`,
:guilabel:`Done`, or :guilabel:`Discard`.

After the activity is marked complete, an entry with the activity type, title, and any other details
that were included in the pop-up window are listed in the chatter.

.. screenshot:: productivity-chatter-completed-activity
   :menu: CRM ‣ Sales ‣ My Pipeline
   :shows: A chatter thread with a completed activity and the feedback logged with it.
   :module: mail
   :notes: English UI, light theme, crop to the chatter.

.. _discuss/attach-files:

Attach files
============

Files can be added as attachments in the chatter, either to send with messages, or to include with a
record.

.. note::
   After a file has been added to a chatter thread, it can be downloaded by any user with access to
   the thread. Click the |paperclip| to make the files header visible, if necessary. Then, click the
   :icon:`fa-download` :guilabel:`(download)` icon the file to download it.

To attach a file, click the |paperclip| located at the top of the chatter composer of any record
that contains a chatter thread.

This opens a file explorer pop-up window. Navigate to the desired file, select it, then click
:guilabel:`Open` to add it to the record. Alternatively, files can be dragged and dropped directly
onto a chatter thread.

After files have been added, they are listed in the chatter thread, under a :guilabel:`Files`
heading.

.. note::
   After at least one file has been added to a chatter record, a new button labeled
   :guilabel:`Attach files` appears below the :guilabel:`Files` heading. To attach any additional
   files, this is the button that **must** be used, instead of the |paperclip| at the top of the
   chatter thread.

   After the :guilabel:`Files` section heading appears in the thread, clicking the |paperclip| no
   longer opens a file explorer pop-up window. Instead, clicking the |paperclip| toggles the
   :guilabel:`Files` section from visible to invisible in the chatter thread.

   .. screenshot:: productivity-chatter-attach-files
      :menu: (any record with a chatter)
      :shows: A chatter thread with the "Files" section visible, one attached file and the paperclip button in the top bar.
      :highlight: The paperclip button and the Files section (red frame).
      :module: mail
      :notes: English UI, light theme, crop to the chatter.

.. _discuss/integrations:

Integrations
============

Beyond the standard features, the *Google Translate* integration can be enabled to translate the
messages of the chatter.

.. important::
   Before it can be used, the integration **must** be configured. Step-by-step instructions can be
   found in :doc:`../../general/integrations/google_translate`.

Google Translate
----------------

*Google Translate* can be used to translate user-generated text in the Odoo chatter.

To enable *Google Translate* on a database, an *API key* must first :doc:`be created
<../../general/integrations/google_translate>` through the `Google API Console
<https://console.developers.google.com/>`_.

After creating the API key, navigate to the :menuselection:`Settings app --> Discuss section` and
paste the key in the :guilabel:`Message Translation` field. Click :guilabel:`Save` to save the
changes.

Translate a chatter message
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To translate a user's text from another language, click the |ve| menu to the right of the chatter.
Then, select :guilabel:`Translate`. The content translates to the language set in the :doc:`user's
preferences <../../general/users/language/>`.

.. screenshot:: productivity-chatter-translate
   :menu: (any record with a chatter)
   :shows: The dropdown menu of a chatter message with the "Translate" option, and the translated text below the original message.
   :highlight: The "Translate" option (red frame).
   :module: mail
   :notes: English UI, light theme, crop to the chatter.

.. important::
   Using the *Google Translate* API **requires** a current billing account with `Google
   <https://myaccount.google.com/>`_.

.. _discuss/chatter-extensions:

Chatter extensions
==================

Several modules extend the standard chatter.

Chatter position
----------------

Each user can choose where the chatter is displayed on form views. In
:menuselection:`Preferences`, set :guilabel:`Chatter Position` to :guilabel:`Side` (next to the
form) or :guilabel:`Bottom` (under the form).

.. note::
   Requires the *MuK Chatter* (``muk_web_chatter``) module.

Email delivery tracking
-----------------------

When an email is sent from the chatter, its delivery status is tracked and displayed next to the
message: :guilabel:`Sent`, :guilabel:`Delivered`, :guilabel:`Opened`, :guilabel:`Deferred`,
:guilabel:`Bounced`, :guilabel:`Soft bounced`, :guilabel:`Rejected`, :guilabel:`Spam`,
:guilabel:`Unsubscribed`, or :guilabel:`Error`. Click the status to see the tracking events of that
email, including the reported error.

The complete list is available to administrators in :menuselection:`Settings --> Technical -->
Email --> Tracking emails` and :guilabel:`Tracking events`. In :menuselection:`Settings --> General
Settings --> Discuss`, the retention of these records can be limited with the maximum age in days.

.. note::
   Requires the *Email tracking* (``mail_tracking``) module.

Reply to a specific message
---------------------------

Click :guilabel:`Reply` on a chatter message to open the composer with the original message quoted,
so that the answer keeps its context.

.. note::
   Requires the *Mail Message Reply* (``mail_quoted_reply``) module.

Preview email attachments
-------------------------

Emails attached to a record as `.eml` files open directly in the file viewer, like a PDF, instead of
being downloaded: the header block and the body are displayed, with the embedded images.

.. note::
   Requires the *Mail Attachment EML Preview* (``mail_attachment_eml_preview``) module.

Notify followers or not
-----------------------

In the full composer, the :guilabel:`Notify Followers` checkbox decides whether the message is also
sent to the followers of the record, or only to the recipients explicitly listed. The same option is
available when sending an invoice from the :guilabel:`Send` window of the Invoicing app.

.. note::
   Requires the *Mail Follower Notification* (``eyssen_mail_follower_notification``) module, and,
   for invoices, *Mail Follower Notification - Invoicing*
   (``eyssen_mail_follower_notification_account``).

.. screenshot:: productivity-chatter-notify-followers
   :menu: (any record with a chatter)
   :shows: The full composer with the "Notify Followers" checkbox next to the recipients.
   :highlight: The "Notify Followers" checkbox (red frame).
   :module: eyssen_mail_follower_notification
   :notes: English UI, light theme, crop to the composer.

.. _discuss/chatter-cc-bcc:

Cc and Bcc recipients
---------------------

In the standard full composer, all recipients are entered in a single :guilabel:`Recipients` field.
With the *Email CC and BCC* module (`mail_composer_cc_bcc`), the full composer has two additional
fields, :guilabel:`Cc` and :guilabel:`Bcc`, in which contacts can be selected (or created on the
fly from an email address):

- the :guilabel:`Recipients` and the :guilabel:`Cc` contacts appear as such, in the *To* and *Cc*
  headers, in the email received by every recipient;
- the :guilabel:`Bcc` contacts receive a copy of the email, but their address is not disclosed to
  the other recipients.

The two fields are available when sending a message from the chatter of any record, and in the
composers based on it (e.g., sending a quotation). They are not displayed when logging an internal
note.

Default values can be prepared in two places:

- on the company: go to :menuselection:`Settings --> Users & Companies --> Companies`, open the
  company, and select contacts in the :guilabel:`Default Cc` and :guilabel:`Default Bcc` fields,
  under :guilabel:`Email`. These contacts are pre-filled in every email composed for that company,
  e.g., to archive all outgoing emails in a dedicated mailbox with a default Bcc contact;
- on an :doc:`email template <../../general/companies/email_template>`: in addition to the standard
  :guilabel:`Cc` field, a :guilabel:`Bcc` field is available in the :guilabel:`Email Configuration`
  tab. When the template is selected in the composer, the addresses of these two fields are matched
  with the existing contacts, which are then added to the :guilabel:`Cc` and :guilabel:`Bcc`
  fields of the composer.

.. screenshot:: productivity-chatter-cc-bcc
   :menu: (any record with a chatter) ‣ Send message ‣ Expand full composer
   :shows: The full composer with the Recipients field followed by the "Cc" and "Bcc" tag fields, each containing one contact with its email address.
   :highlight: The "Cc" and "Bcc" fields (red frame).
   :data: Recipient "Deco Addict"; Cc "Douglas Fletcher"; Bcc "Archive mailbox <archive@yourcompany.example>".
   :module: mail_composer_cc_bcc
   :notes: English UI, light theme, crop to the composer.

Archive and restore log
-----------------------

When a record is archived or restored, the standard chatter only keeps a trace if the
:guilabel:`Active` field of the model is tracked, which is rarely the case. With the *Chatter: Log
Archive/Restore* module (`eyssen_chatter_log_all_state_chnage`), a note such as *“Deco Addict” was
archived.* or *“Deco Addict” was restored.* is logged in the chatter of every record that has one,
with the user and the date of the operation. Models that already track the field are left
unchanged, so that the operation is not logged twice.

.. note::
   To install the module, go to :menuselection:`Settings --> eYssen ERP`, and, in the
   :guilabel:`General Modules` section, enable :guilabel:`Chatter: Log Archive/Restore (no duplicate
   with tracking)`.

.. seealso::
   - :doc:`Discuss <../discuss>`
   - :doc:`Discuss Channels <../discuss/team_communication/>`
   - :doc:`Activities <../../essentials/activities>`

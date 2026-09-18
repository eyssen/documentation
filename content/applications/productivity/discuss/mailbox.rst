=======
Mailbox
=======

The **Mailbox** app gathers the internal messages of the database in a single three-pane screen —
sidebar, message list, and preview — so that messages can be processed like in an email client,
without opening each record one by one.

.. note::
   The app is provided by the *Mailbox* (``mailbox``) module. It works on the messages already
   stored in the database, so nothing has to be imported.

Navigate the mailbox
====================

Open :menuselection:`Mailbox`. The left sidebar groups the messages:

- :guilabel:`Inbox`: the messages addressed to the user;
- :guilabel:`Marked`: the messages flagged with a :ref:`mark <mailbox/marks>`;
- :guilabel:`Channels` and :guilabel:`Direct Messages`: the Discuss conversations;
- :guilabel:`Labels`: the user's own :ref:`labels <mailbox/labels>`;
- :guilabel:`Lost messages`: the messages whose record has been deleted or is no longer accessible.

Each entry shows the number of unread messages. The middle pane lists the messages of the selected
section, with their subject, author, and date; selecting one opens it in the preview pane on the
right, where the message, its attachments, and the thread it belongs to are displayed, and where it
can be answered directly.

.. screenshot:: productivity-mailbox-overview
   :menu: Mailbox
   :shows: The three-pane Mailbox screen with the sidebar (Inbox, Marked, Channels, Direct Messages, Labels, Lost messages), the message list in the middle and the selected message in the preview pane.
   :data: Demo company "YourCompany HU"; a few messages from sales orders and contacts.
   :module: mailbox
   :notes: English UI, light theme, 1440px width.

Work with messages
==================

From the message list, several messages can be selected to act on them at once with the bulk
toolbar: mark them as read or unread, apply a label, flag them with a mark, archive them, or delete
them. Deletion is a soft delete: the message is hidden but kept, together with who deleted it and
when.

The reply composer offers :guilabel:`Send as e-mail` to send the answer as an email instead of an
internal message, and supports :guilabel:`CC` and :guilabel:`BCC` recipients.

.. _mailbox/labels:

Labels
------

Labels classify messages across records. Manage them in :menuselection:`Mailbox --> Settings -->
Labels`: each label has a :guilabel:`Name`, a color, an optional :guilabel:`Description`, a
:guilabel:`Sequence`, and, in a multi-company database, a :guilabel:`Company`. The list also shows
the number of messages carrying the label.

.. _mailbox/marks:

Marks
-----

Marks are personal flags, similar to the flags of an email client. Manage them in
:menuselection:`Mailbox --> Settings --> Marks`, where each mark has a :guilabel:`Name`, a color,
and an icon. A mark is applied per user, so two users can flag the same message differently.

Audit log
---------

:menuselection:`Mailbox --> Settings --> Audit Log` records the actions performed on the messages
(edition, deletion, restoration), with their author and date.

Access rights
=============

The :guilabel:`Mailbox` category of the :ref:`access rights <access-rights/users>` gives a fine
control over what a user may do:

- :guilabel:`User: Access Mailbox`: open the app;
- :guilabel:`User: Edit Own Messages` and :guilabel:`Administrator: Edit Any Message`;
- :guilabel:`User: Delete Own Messages` and :guilabel:`Administrator: Delete Any Message`;
- :guilabel:`User: Move Messages` and :guilabel:`User: Manage Labels`;
- :guilabel:`User: Lost Messages Visibility`: see the messages whose record is gone;
- :guilabel:`User: Send as E-mail`: answer by email from the mailbox;
- :guilabel:`Administrator: Mailbox`: full access.

.. seealso::
   - :doc:`../discuss`
   - :doc:`chatter`

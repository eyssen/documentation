=============================
Commands and canned responses
=============================

In the Odoo **Live Chat** application, *commands* allow the user to perform specific actions both
inside the chat window, and through other Odoo applications. The **Live Chat** app also includes
*canned responses*. These are customized, preconfigured substitutions that allow users to replace
shortcut entries in place of longer, well-thought out responses to some of the most common questions
and comments.

Both commands and canned responses save time, and allow users to maintain a level of consistency
throughout their conversations.

Execute a command
=================

Live chat *commands* are keywords that trigger preconfigured actions. When a live chat *operator*
is participating in a conversation with a customer or website visitor, they can execute a command by
typing `/`, followed by the command.

Commands, and the resulting actions, are only visible in the conversation window for the live chat
operator. A customer does not see any commands that an operator uses in a conversation from their
view of the chat.

.. example::
   During a conversation with a customer, a live chat operator executes the command to :ref:`create
   a lead <live-chat/lead>`. After entering the command, `/lead`, followed by a title, the system
   creates a lead from the conversation and posts a link to it in the chat window, so the operator
   can go there directly to add any additional information, if necessary.

More information about each available command can be found below.

Help
----

If an operator types `/help` in the chat window, an informative message that includes the potential
entry types an operator can make is displayed.

- Type `@username` to mention a user in the conversation. A notification will be sent to that user's
  inbox or email, depending on their notification settings.
- Type `/command` to execute a command.
- Type `:shortcut` to insert a :ref:`canned response <live-chat/canned-responses>`.

.. seealso::
   - :doc:`/applications/productivity/discuss`
   - :doc:`/applications/productivity/discuss/team_communication`

History
-------

If an operator types `/history` in the chat window, it generates a list of the most recent pages the
visitor has viewed on the website (up to 15).

.. screenshot:: livechat-responses-responses-history
   :menu: Discuss
   :shows: An operator's live chat window after typing `/history`, showing the list of the visitor's recently viewed pages.
   :highlight: The generated page list (red frame).
   :data: A visitor who viewed three shop pages.
   :module: im_livechat, mail, crm_livechat
   :notes: English UI, light theme, 1440px width.

.. _live-chat/lead:

Lead
----

By typing `/lead` in the chat window, an operator can create a *lead* in the **CRM** application.

.. screenshot:: livechat-responses-responses-lead
   :menu: Discuss
   :shows: An operator's live chat window after typing `/lead` and a title, showing the link to the newly created lead.
   :highlight: The link to the new lead (red frame).
   :data: Lead 'Website inquiry'.
   :module: im_livechat, mail, crm_livechat
   :notes: English UI, light theme, 1440px width.

.. important::
   The `/lead` command can only be used if the **CRM** app has been installed.

After typing `/lead`, create a title for this new lead, then press `Enter`. A link with the lead
title appears. Click the link, or navigate to the :menuselection:`CRM` app to view the
:guilabel:`Pipeline`.

.. note::
   The link to the new lead can only be seen and accessed by the operator, not the customer.

The transcript of that specific live chat conversation (where the lead was created) is added to the
:guilabel:`Internal Notes` tab of the lead form.

On the :guilabel:`Extra Information` tab of the lead form, the :guilabel:`Source` will be listed as
:guilabel:`Livechat`.

Leave
-----

If an operator types `/leave` in the chat window, they can automatically exit the conversation. This
command does not cause the customer to be removed from the conversation, nor does it automatically
end the conversation.

.. seealso::
   - :doc:`/applications/sales/crm/acquire_leads`

.. _live-chat/canned-responses:

Canned responses
================

*Canned responses* are customizable inputs where a *shortcut* stands in for a longer response. An
operator will enter the shortcut, and it is automatically replaced by the expanded *substitution*
response in the conversation.

Create canned responses
-----------------------

To create a new canned response, go to :menuselection:`Live Chat app --> Configuration --> Canned
Responses --> New`.

Type a shortcut command in the :guilabel:`Shortcut` field. Next, click the :guilabel:`Substitution`
field, and type the message that should replace the shortcut.

.. tip::
   Try to connect the shortcut to the topic of the substitution. The easier it is for the operators
   to remember, the easier it is to use the canned responses in conversations.

Authorized groups
~~~~~~~~~~~~~~~~~

When a new canned response is created, it can **only** be utilized by the operator that created it.
To allow the response to be used by other operators, select one or more :ref:`groups
<access-rights/groups>` from the :guilabel:`Authorized Groups` drop-down list.

Use canned responses in a live chat conversation
------------------------------------------------

To use a canned response in a conversation, click the :icon:`fa-plus-circle` :guilabel:`(plus)` icon
in the message window. Then, click :guilabel:`Insert a Canned Response`. This opens a list of
available canned responses. Either select a response from the list, or type the appropriate
shortcut, then click the :icon:`fa-paper-plane` :guilabel:`(send)` icon or hit :kbd:`Enter`.

.. tip::
   Typing `::` into a chat window on its own generates a list of available canned responses.
   Responses can be manually selected from the list, in addition to the use of shortcuts.

   .. screenshot:: livechat-responses-response-list
      :menu: Discuss
      :shows: An operator's live chat window with the list of available canned responses open after typing `::`.
      :highlight: The canned response list (red frame).
      :data: Three canned responses.
      :module: im_livechat, mail, crm_livechat
      :notes: English UI, light theme, 1440px width.

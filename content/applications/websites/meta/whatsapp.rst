========
WhatsApp
========

With the **WhatsApp** feature, you talk to your customers on WhatsApp from Odoo, through the official
**WhatsApp Business Cloud API** of Meta. You can send message **templates** from contacts, quotations,
sales orders, invoices, and CRM leads, receive the answers in **Discuss**, and follow the delivery of
each message (sent, delivered, read, failed).

.. important::
   This feature is not installed automatically. Install *WhatsApp (Meta Cloud API)* from
   :menuselection:`Apps`. It needs a WhatsApp Business Account at Meta, a phone number registered in
   it, and the :ref:`Meta webhooks <meta/webhooks>`.

Connect a WhatsApp Business Account
===================================

Go to :menuselection:`Meta --> WhatsApp --> Accounts` (administrators only), and click
:guilabel:`New`:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Name`
     - For example `Customer Service`.
   * - :guilabel:`WhatsApp Business Account` group
     - The :guilabel:`WhatsApp Business Account ID` and the :guilabel:`Phone Number ID`, shown in
       the WhatsApp Manager of Meta. The display phone number, the verified name, and the quality
       rating are filled in by Odoo.
   * - :guilabel:`Authentication`
     - :guilabel:`System user access token`: paste the permanent token of a system user of your
       business. Or :guilabel:`Meta connection`: use a :doc:`Meta connection <connection>`.
   * - :guilabel:`Responsible Users`
     - The users who receive the incoming conversations.

Then use the buttons:

#. :guilabel:`Load Phone Numbers`: reads the phone numbers of the account. The :guilabel:`Phone
   Numbers` tab lists them; click :guilabel:`Use` on the one that this account uses.
#. :guilabel:`Subscribe App to WABA`: makes your Meta app receive the notifications of the account.
   In the webhooks of the Meta app, subscribe the *WhatsApp Business Account* object to the
   `messages` and `message_template_status_update` fields (see :ref:`meta/webhooks`).
#. :guilabel:`Sync Templates`: downloads the message templates.

.. screenshot:: meta-whatsapp-account
   :menu: Meta ‣ WhatsApp ‣ Accounts ‣ (an account)
   :shows: A WhatsApp account form with the Load Phone Numbers, Sync Templates, and Subscribe App to
      WABA buttons, the WhatsApp Business Account group (WABA ID, phone number ID, display number,
      verified name, quality rating), the Access group (authentication, token hidden), and the
      Responsible Users tab.
   :highlight: The three header buttons (red frame).
   :data: Throw-away account, token hidden.
   :notes: English UI, light theme, 1440px width.

Templates
=========

WhatsApp only allows to start a conversation with a **template** that Meta approved. Create and submit
your templates in the WhatsApp Manager of Meta. In Odoo, :menuselection:`Meta --> WhatsApp -->
Templates` lists the templates downloaded with :guilabel:`Sync Templates`, with their language,
category (:guilabel:`Marketing`, :guilabel:`Utility`, :guilabel:`Authentication`), and status
(:guilabel:`Approved`, :guilabel:`Pending`, :guilabel:`Rejected`, :guilabel:`Paused`, and so on).
The status is updated automatically when Meta changes it.

Open a template to configure it:

- :guilabel:`Model`: the type of document whose fields fill the variables (for example the quotation).
  The :guilabel:`Send WhatsApp` action is added to this document.
- In the :guilabel:`Variables` tab, for each variable of the template (`{{1}}`, or a name), choose the
  source: a :guilabel:`Document field` (for example the name of the customer or the reference of the
  order) or a :guilabel:`Fixed text`.
- The :guilabel:`Preview` tab shows the message with the values of the variables, and the
  :guilabel:`Content` tab the texts of the template (they can only be changed in Meta).

.. screenshot:: meta-whatsapp-template
   :menu: Meta ‣ WhatsApp ‣ Templates ‣ (a template)
   :shows: A WhatsApp template form with its status bar, the language and category, the document
      model, and the Variables tab where each variable is mapped to a document field.
   :highlight: The Variables tab (red frame).
   :data: Template "order_confirmation" with the variables customer name and order reference.
   :notes: English UI, light theme, 1440px width.

Click :guilabel:`Add "Send WhatsApp" to Documents` in :menuselection:`Meta --> Configuration -->
Settings` (:guilabel:`WhatsApp Accounts` setting) to add the action to the contacts, quotations and
sales orders, invoices, and leads.

Send a message
==============

On a contact, a quotation, a sales order, an invoice, or a lead, open the :guilabel:`Action` menu and
click :guilabel:`Send WhatsApp`:

#. Select the :guilabel:`Account` and check the :guilabel:`Phone` of the customer and its
   :guilabel:`Country`. Odoo formats the number in the international format.
#. Choose the :guilabel:`Mode`:

   - :guilabel:`Template`: select an approved template. The variables are filled in from the document;
     you can edit them. A template message can be sent at any time.
   - :guilabel:`Free text`: write your message, and attach files if needed. It is only possible while
     the **customer service window** is open: it opens when the customer writes to you, and closes 24
     hours after the last message of the customer.

#. Check the preview and click :guilabel:`Send`.

A copy of the message is logged in the chatter of the document. The status of the message (sent,
delivered, read, or failed with the error) is updated, and the list of the messages is in
:menuselection:`Meta --> WhatsApp --> Messages`.

.. warning::
   A contact who asked not to receive marketing messages (see :ref:`meta/whatsapp/opt-out`) does not
   receive templates of the :guilabel:`Marketing` category. Meta also bills each conversation
   according to its category: check the prices in your Meta account.

Conversations
=============

When a customer answers (text, images, documents, audio, video, locations, button and list replies),
the message arrives in a **Discuss** conversation of the customer's phone number, and the sender is
found by phone number or created as a contact. The conversations are listed in
:menuselection:`Meta --> WhatsApp --> Conversations`; the contact form has an :guilabel:`Open in
Discuss` button.

Answer from the conversation: your message is sent on WhatsApp while the customer service window is
open. When the window is closed, use :guilabel:`Send WhatsApp` with a template to restart the
conversation.

.. _meta/whatsapp/opt-out:

Opt-out keywords
================

In the :guilabel:`Meta` settings, enable the opt-out keywords to respect the customers who do not want
marketing messages. When a customer sends one of the :guilabel:`Opt-out Keywords` (`STOP` by default,
comma separated, not case sensitive; the whole message must be the keyword), the contact is flagged
:guilabel:`WhatsApp Opt-out` and no longer receives the marketing templates. The :guilabel:`Opt-in
Keywords` (`START` by default) remove the flag. You can also change the flag manually on the contact.

Files that the customers send are downloaded only up to the :guilabel:`Maximum Media Size (MB)` of
the :guilabel:`Received Files` setting (16 MB by default).

.. _meta/whatsapp/test:

Test WhatsApp
=============

#. Use the test number of your Meta app, or a real number, and add your own phone as a recipient in
   the WhatsApp Manager.
#. Click :guilabel:`Send WhatsApp` on a contact that has your phone number, choose a template, and send.
#. The message must arrive on your phone, and its status must become :guilabel:`Delivered` in
   :menuselection:`Meta --> WhatsApp --> Messages`.
#. Answer from your phone: the message must appear in the Discuss conversation. If it does not, check
   the :menuselection:`Meta --> Webhook Notifications` list and :ref:`meta/webhooks/troubleshooting`.
#. A message in the status :guilabel:`Failed` shows the error of Meta: a template that is not approved,
   a closed customer service window, a phone number that is not on WhatsApp, or an expired token.

.. seealso::
   - :doc:`connection`
   - :doc:`social`
   - :doc:`/applications/websites/website/tracking/privacy`

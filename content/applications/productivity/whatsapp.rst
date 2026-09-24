========
WhatsApp
========

The **Odoo WhatsApp Connector** (``whatsapp_mail_messaging``) lets users send quotations, invoices,
and portal links to customers through **WhatsApp Web** or the WhatsApp mobile app. Odoo does not
connect to the WhatsApp Business API: it prepares the message text and opens WhatsApp with the
recipient and the message already filled in, so the message is sent from the user's own WhatsApp
account.

.. note::
   The module requires the *Sales*, *Invoicing*, and *Website* apps. Every recipient must have a
   :guilabel:`Mobile` number on their contact record, in international format.

Configuration
=============

Message template
----------------

To define the text proposed by default when sending a quotation or an invoice, go to
:menuselection:`Settings --> General Settings`, scroll to the :guilabel:`Whatsapp` section, and fill
in the :guilabel:`Message Template` field. The template is stored per company; if it is left empty,
Odoo composes a default message containing the customer name, the document number, and the total
amount.

.. screenshot:: productivity-whatsapp-settings
   :menu: Settings ‣ General Settings
   :shows: General Settings scrolled to the "Whatsapp" block with the "Message Template" text field filled in with a short greeting.
   :highlight: The "Whatsapp" settings block (red frame).
   :data: Demo company "YourCompany HU"; template text "Hello, please find your document below."
   :module: whatsapp_mail_messaging
   :notes: English UI, light theme, 1440px width, crop to the settings block.

Website chat button
-------------------

The module adds a WhatsApp icon to the social media area of the website footer. Visitors can use it
to start a chat with the company. For the icon to work, enter the company's WhatsApp number in the
:guilabel:`Mobile Number` field of the website record (:menuselection:`Website --> Configuration -->
Settings`, then open the website form).

The messages offered to visitors in the chat window are managed in :menuselection:`Website -->
Configuration --> Whatsapp Messages`. Each record has a :guilabel:`Name` and a :guilabel:`Message`;
visitors can select one of them or choose :guilabel:`Custom` and type their own text.

.. screenshot:: productivity-whatsapp-message-templates
   :menu: Website ‣ Configuration ‣ Whatsapp Messages
   :shows: List view of the "Selection Message" records with two entries, and the form view of one of them showing the Name field and the Message tab.
   :data: Two templates: "Request a quote", "Opening hours".
   :module: whatsapp_mail_messaging
   :notes: English UI, light theme, 1440px width.

Send a quotation or an invoice
==============================

Open a quotation or an invoice and click the :guilabel:`Send by Whatsapp` button next to the
standard send buttons. A :guilabel:`Compose Whatsapp Message` window opens with:

- :guilabel:`Recipient`: the customer of the document;
- :guilabel:`Contact Number`: the mobile number of the recipient (editable);
- :guilabel:`Message`: the message template, or the generated default text.

Click :guilabel:`Send Message` to open WhatsApp with the message prepared. The text is also logged
in the recipient's chatter.

Several documents can be sent at once: select them in the list view and click :guilabel:`Send by
Whatsapp`. All selected documents must belong to the same customer; otherwise, Odoo raises an error.

.. screenshot:: productivity-whatsapp-compose
   :menu: Sales ‣ Orders ‣ Quotations
   :shows: A quotation form with the green "Send by Whatsapp" button, and the "Compose Whatsapp Message" dialog open with Recipient, Contact Number and Message filled in.
   :highlight: The "Send by Whatsapp" button (red frame).
   :data: Quotation S00021 for customer "Deco Addict" with a mobile number set.
   :module: whatsapp_mail_messaging
   :notes: English UI, light theme, 1440px width, use a throw-away phone number.

Share a portal link
===================

When sharing a record with a customer (the :guilabel:`Share` action that opens the portal share
window), a :guilabel:`Sharing Method` field allows :guilabel:`Whatsapp` to be selected instead of
:guilabel:`Mail`. Select the :guilabel:`Customer`, check the :guilabel:`Mobile number`, and send:
the portal link and the note are sent through WhatsApp and logged in the record's chatter.

Systray shortcuts
=================

Two icons are added to the top-right systray area: one opens the :guilabel:`Compose Whatsapp
Message` window for any number, the other opens a blank email composition form.

.. screenshot:: productivity-whatsapp-systray
   :menu: (any backend view)
   :shows: The top-right systray bar with the WhatsApp icon and the envelope icon added by the module.
   :highlight: The two added systray icons (red frame).
   :module: whatsapp_mail_messaging
   :notes: English UI, light theme, crop to the systray area.

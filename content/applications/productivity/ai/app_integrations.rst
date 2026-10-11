=======================
AI in the business apps
=======================

For many eYssen apps there is a small AI module that adds quick prompts and a
few buttons to the forms you already use. The modules install themselves when
the AI module and the matching app are both installed, so there is nothing to
set up beyond the normal AI configuration (see :doc:`getting_started`).

How they work
=============

- Quick prompts appear as chips in the AI panel when a record of the app is open
  in a form view (see :doc:`panel`). Administrators can edit or archive them
  like any other quick prompt.
- The AI reads only what you may see: your access rights, record rules and the
  AI access rules all apply (see :doc:`access_policy`). If an access rule stops
  the AI from reading what a button needs, you get a clear message instead of a
  partial result.
- Buttons that change data work as your own decision: the AI proposes values,
  you click, and the change is made with your rights and recorded in the AI
  change log (see :doc:`monitoring`). Buttons that only draft text never send or
  save anything on their own.
- Texts found in records, messages and descriptions are treated as untrusted
  content: the AI is told never to follow instructions written inside them.

CRM
===

On a lead or opportunity the quick prompts are :guilabel:`Qualify` (a short
assessment of the lead and of the information that is still missing),
:guilabel:`Next best action` and :guilabel:`Follow-up email`.

The button :guilabel:`Assign with AI` in the form header (and in the action menu
of the list, for up to 20 leads at a time) picks a salesperson and a sales team
for each lead. The AI looks at the lead, the sales teams and their members, the
open workload of each salesperson and how many leads each of them won in the
last year, in total and in the lead's country. It can only choose from the
people and teams it was offered. The assignment is written with your rights, and
a note "Assigned with AI" with the reason is added to the chatter. Leads you
cannot edit are skipped, and a summary tells you how many were assigned and why
others were not.

Sales, Purchase and Inventory
=============================

- Sales orders: :guilabel:`Summarise`, :guilabel:`Upsell ideas` (from the
  customer's order history) and :guilabel:`Follow-up`. When the margin or the
  delivery apps are installed, :guilabel:`Margin check` and :guilabel:`Delivery
  status` are added as well. If an administrator deletes one of them, it does
  not come back.
- Purchase orders: :guilabel:`Compare with previous purchases` (price, vendor
  and lead time for the same products), :guilabel:`RFQ reminder` (a reminder to
  the vendor) and :guilabel:`Summarise`.
- Transfers: :guilabel:`Explain delays` and :guilabel:`Stock risk`. Products and
  product variants also have :guilabel:`Stock risk`, which compares the stock on
  hand with the forecast and the open demand. These are shown to Inventory
  users.

Invoicing
=========

- Invoices: :guilabel:`Explain this invoice`, :guilabel:`Check for anomalies`
  (compares the invoice with the partner's previous invoices: amounts, lines,
  taxes, payment terms and possible duplicates) and :guilabel:`Payment reminder`
  (a polite reminder for the open amount).
- Contacts, for users of the billing group: :guilabel:`Payment behaviour` and
  :guilabel:`Open items`.
- In the window that sends an invoice, the button :guilabel:`Draft with AI`
  above the message writes a short, personal email in the mail language. It
  reads the invoice, its lines and the partner's other open invoices. The text
  replaces the message body so you can edit it; nothing is sent until you click
  Send.

Calendar
========

On a meeting the quick prompts are :guilabel:`Prepare agenda`, :guilabel:`Draft
minutes` (from the description and the attendees) and :guilabel:`Follow-up
email`.

Products
========

- :guilabel:`Generate description with AI` in the product form header writes the
  sales description and, when the website shop is installed, the longer website
  description. It uses the name, category, price, internal reference, current
  descriptions and attribute values of the product.
- :guilabel:`Generate image with AI` opens a small window with a prompt
  pre-filled from the product, which you can edit, and a :guilabel:`Size`. It
  needs an image model (see :doc:`models_and_providers`) and is hidden without
  one. The generated picture becomes the product image.

Email marketing
===============

- In the mailing body editor, the AI command of the editor menu is labelled
  :guilabel:`AI writer` and is answered by your configured model (see
  :doc:`writing_assistant`).
- Quick prompts on a mailing: :guilabel:`Review this mailing`,
  :guilabel:`Preview text` and :guilabel:`A/B test idea`.
- The button :guilabel:`Subject lines with AI` next to the subject reads the
  mailing and proposes three subject lines in a dialog. Click :guilabel:`Use`
  next to the one you like to set it as the subject. The button disappears once
  the mailing has been sent.

Timesheets
==========

On the timesheet list, :guilabel:`Draft with AI` opens a dialog where you pick a
day (today by default) and click :guilabel:`Propose`. For that day the AI looks
at your calendar meetings, the tasks assigned to you that changed, the messages
you wrote on tasks and the timesheets you already logged. It proposes lines with
a task, a description and the hours. Each line has a checkbox and can be edited,
and every line must name a task from the offered list. The hours are kept within
sensible bounds and the day's total never goes above 24 hours. Click
:guilabel:`Create timesheets` to create the lines you ticked. Nothing is logged
without that click.

.. note::
   The timesheet assistant has no grid view because the grid view does not exist
   in the Community edition. Only your own messages on tasks are read, in your
   own environment.

.. seealso::
   Further integrations are described in :doc:`knowledge_documents` (Knowledge,
   Documents and cloud storage), :doc:`project_sla` (projects with SLA) and
   :doc:`accounting_reports` (accounting reports).

=====================
Follow-up on invoices
=====================

Follow-up messages can be sent to customers when payments are overdue. eYssen ERP helps identify
late payments and lets you schedule and send the appropriate reminders using **follow-up levels**
according to the number of overdue days. Reminders can be sent through several channels: email,
SMS, postal letter, an online **Pay Now** link, and scheduled activities.

.. seealso::
   :doc:`/applications/finance/accounting/customer_invoices/payment_terms`

.. _accounting/follow_up/configuration:

Configuration
=============

.. _accounting/follow_up/levels:

Follow-up levels
----------------

To configure the escalation ladder, go to :menuselection:`Accounting --> Configuration -->
Follow-up Levels`. Each record is a **level** that applies once an invoice reaches a given number
of days past its due date. When several levels qualify, the **highest** one that the oldest
overdue invoice has already reached is the one that applies.

.. _accounting/follow_up/default_levels:

Default follow-up levels
~~~~~~~~~~~~~~~~~~~~~~~~

A ready-to-use ladder of seven levels is created automatically when the application is installed,
so reminders can be reviewed and sent without any configuration:

.. list-table::
   :header-rows: 1
   :widths: 28 12 60

   * - Level
     - Due Days
     - Purpose (default channel: email)
   * - :guilabel:`Payment Due Today`
     - 0
     - Friendly notice that the amount falls due today. Nothing is overdue yet.
   * - :guilabel:`Payment Overdue`
     - 1
     - The due date has passed and payment has not been received.
   * - :guilabel:`Payment Reminder`
     - 8
     - Reminder that the invoice is still unpaid.
   * - :guilabel:`Repeated Reminder`
     - 15
     - Repeated reminder, as the invoice remains unpaid.
   * - :guilabel:`Urgent Notice`
     - 30
     - More insistent notice, urging immediate payment.
   * - :guilabel:`Warning`
     - 45
     - Warning before the final step.
   * - :guilabel:`Final / Legal Notice`
     - 60
     - Last step before legal recovery, marked :guilabel:`Final / Legal Level`.

.. important::
   Every default level ships with :guilabel:`Automatic` switched **off**. Installing the
   application therefore never sends anything on its own: each reminder is only sent after someone
   reviews and sends it. Automatic sending starts only once an administrator enables
   :guilabel:`Automatic` on the individual levels that should be sent unattended (see
   :ref:`accounting/follow_up/automatic`).

.. tip::
   The default ladder is safe to edit or delete — an application upgrade will not restore it. On a
   multi-company database, add one ladder per company.

.. screenshot-pending: follow_up/levels-list.png
   :alt: List of follow-up levels in eYssen ERP.

.. Screenshot: Accounting ▸ Configuration ▸ Follow-up Levels list view, showing the seven default
   levels (Due Days 0/1/8/15/30/45/60), with the Send Email / Send SMS / Send Letter / Show Interest /
   Automatic / Final columns visible — the Automatic column unticked on every row.

To modify a level, click the record. From the form view, set the :guilabel:`Level Name` and the
number of :guilabel:`Due Days` before the reminder is sent, then choose the channels and options:

- :guilabel:`Send Email`: send the reminder by email. Select a per-level :guilabel:`Email Template`;
  when left empty, the application's default reminder template is used.
- :guilabel:`Send SMS`: send an SMS text message, using the level's :guilabel:`SMS Template`.
- :guilabel:`Send Letter (Post)`: send the reminder as a postal letter through
  :ref:`Snailmail <customer_invoices/snailmail>`.
- :guilabel:`Attach Overdue Invoices`: attach the customer's overdue invoices to the email and/or
  letter as separate PDF files.
- :guilabel:`Show Late-payment Interest`: display the informational interest and collection-fee
  block on this level's reminder (see :ref:`accounting/follow_up/interest`).
- :guilabel:`Automatic`: let the daily scheduled action send this level without manual review (see
  :ref:`accounting/follow_up/automatic`). When disabled, the level is only ever sent after a human
  reviews it.
- :guilabel:`Final / Legal Level`: flag the last, legal-notice level. This is informational and can
  be used on the reminder wording.

.. note::
   Sending SMS messages or postal letters requires :doc:`In-App Purchase (IAP)
   </applications/essentials/in_app_purchase>` credit. Email and the online **Pay Now** link do not.

.. screenshot-pending: follow_up/level-form.png
   :alt: Follow-up level form with channels and options.

.. Screenshot: a single follow-up level form (e.g. "Repeated Reminder"), left column Level Name /
   Due Days / Automatic / Final-Legal, right column Send Email + Email Template / Send SMS + SMS
   Template / Send Letter / Attach Overdue Invoices / Show Late-payment Interest.

In the :guilabel:`Activity` section, enable :guilabel:`Schedule Activity` to automatically create an
:doc:`activity </applications/essentials/activities>` when the level is triggered, then set the
activity type, responsible user, summary, and note.

.. _accounting/follow_up/interest:

Late-payment interest (informational)
-------------------------------------

To display a late-payment interest amount and, for business customers, a fixed collection fee on
reminders, go to :menuselection:`Accounting --> Configuration --> Settings` and, in the
:guilabel:`Customer Invoices` section, enable :guilabel:`Late-payment Interest on Reminders`:

- :guilabel:`Late-payment Interest on Reminders`: turn the block on and set the annual interest
  rate (in %).
- :guilabel:`Collection fee (B2B)`: optionally add a fixed collection fee, applied only to company
  (business) customers.

The block is only shown on levels whose :guilabel:`Show Late-payment Interest` option is enabled.

.. important::
   These amounts are **display-only**. They are computed and shown on the reminder for information,
   but the application **never** creates a journal entry — no interest or fee is posted to accounting.

.. screenshot-pending: follow_up/interest-settings.png
   :alt: Late-payment interest settings.

.. Screenshot: Accounting ▸ Configuration ▸ Settings, the "Late-payment Interest on Reminders"
   setting expanded, with the rate % field and the Collection fee (B2B) toggle + amount visible.

.. _accounting/follow_up/process:

Follow-up process
=================

.. note::
   Reconcile all bank transactions before starting the follow-up process to avoid sending
   reminders for invoices that have already been paid.

.. _accounting/follow_up/one-customer:

Follow-ups for one customer
---------------------------

For a detailed overview of a customer's follow-up status, go to :menuselection:`Accounting -->
Customers --> Customers`, open the customer's form, and click the :guilabel:`Payment Follow-up` tab.
The tab shows:

- :guilabel:`Follow-up Status`: :guilabel:`No Action Needed`, :guilabel:`In Need of Action`, or
  :guilabel:`With Overdue Invoices`.
- :guilabel:`Next Follow-up Date`: the throttle date before which the customer will not be dunned
  again; set automatically after a reminder is sent and manually adjustable.
- :guilabel:`Follow-up Responsible`: the user who handles the follow-up.
- :guilabel:`Total Overdue` and :guilabel:`Total Due`: the customer's overdue and total open
  receivable amounts.

.. screenshot-pending: follow_up/partner-tab.png
   :alt: Payment Follow-up tab on the customer form.

.. Screenshot: a customer form open on the "Payment Follow-up" tab, showing Follow-up Status = In
   Need of Action, Next Reminder, Responsible, Total Overdue / Total Due, the internal note, and the
   "Send Reminder" button.

Click :guilabel:`Send Reminder` to open the review window, adjust the :guilabel:`Level` if needed,
and click :guilabel:`Send`. The reminder covers the customer's **full overdue statement**.

.. note::
   - The contact information on the customer form is used to send the reminder. A customer with no
     usable contact for the chosen channel is skipped and the skip is recorded.
   - The chatter keeps a full record of every follow-up action.

.. _accounting/follow_up/all-customers:

Follow-ups for several customers
--------------------------------

To act on several customers at once, go to :menuselection:`Accounting --> Customers -->
Customers`, switch to the list view, and select the customers requiring follow-up (filter by
:guilabel:`With Overdue Invoices` to narrow the list). Then click :icon:`fa-cog` :guilabel:`(Actions)`
and select :guilabel:`Send Payment Reminder`. A review window lists one line per customer with the
resolved :guilabel:`Level`; adjust if needed and click :guilabel:`Send`. Each customer receives
their full overdue statement. Customers whose overdue balance nets zero or negative are skipped
automatically.

.. _accounting/follow_up/invoice-bulk:

Follow-ups from the overdue invoices list
-----------------------------------------

You can also start reminders from the invoices list. Go to :menuselection:`Accounting -->
Customers --> Invoices`, filter on :guilabel:`Overdue`, and select the invoices to dun. Then click
:icon:`fa-cog` :guilabel:`(Actions)` and select :guilabel:`Send Payment Reminder`. The selected
invoices are grouped by customer in the review window.

.. important::
   Unlike the customer-level entry points, a reminder started from the invoices list is **scoped**:
   it covers only the **selected** invoices (content, attachments, logged record, and interest),
   not the customer's full statement.

.. screenshot-pending: follow_up/invoice-bulk.png
   :alt: Sending reminders from the overdue invoices list.

.. Screenshot: Accounting ▸ Customers ▸ Invoices list filtered on Overdue, several rows ticked, the
   Actions (gear) menu open with "Send Payment Reminder" highlighted.

.. _accounting/follow_up/automatic:

Automatic follow-ups
--------------------

A daily scheduled action (:guilabel:`Payment Follow-up: process overdue partners`) processes
overdue customers automatically. By design it is **generate-then-review**: it only sends levels
that are explicitly flagged :guilabel:`Automatic`. Levels left non-automatic are never sent by the
cron and always require a manual review, so no reminder leaves the system unattended unless you
opt a level in.

.. _accounting/follow_up/report:

Follow-up letter
================

The reminder document is a plain A4 PDF letter listing the customer's overdue invoices, the totals,
the optional :ref:`interest and collection-fee block <accounting/follow_up/interest>`, and — in the
email — an online **Pay Now** link to the customer portal. The same content is shared between the
PDF letter and the reminder email, so both always show the customer the same figures.

.. screenshot-pending: follow_up/report.png
   :alt: Follow-up reminder letter PDF.

.. Screenshot: the generated follow-up letter PDF — header with company details, the overdue
   invoice table, totals, and (when enabled) the late-payment interest + collection-fee block.

.. _accounting/follow_up/log:

Follow-up log
=============

Every reminder that is sent — and every skipped customer — is written to an append-only audit
trail. To review it, go to :menuselection:`Accounting --> Payment Follow-up --> Follow-up Log`. Each
entry records the date, customer, level, channel (email, SMS, letter, portal, activity, or
*skipped*), the invoices covered, and a note. Log entries cannot be edited or deleted.

.. screenshot-pending: follow_up/log.png
   :alt: Follow-up log.

.. Screenshot: Accounting ▸ Payment Follow-up ▸ Follow-up Log list, several rows showing Date /
   Customer / Level / Channel / Invoices / Note.

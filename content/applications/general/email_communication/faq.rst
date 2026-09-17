====================================
Common emailing issues and solutions
====================================

This page lists the most common emailing issues and their solutions.

.. _email-issues-provider:

Odoo is not an email provider
=============================

Odoo does not function like a classic email inbox, such as Gmail, Outlook, Yahoo, etc.

While Odoo uses emails as a way to notify and communicate with users/customers, it is, by design,
not a replacement for a dedicated email server. Therefore, it might not behave in the expected way
when compared to a traditional email inbox.

The main differences are the following:

- By default, once a notification or transactional email (quote, invoice, direct message to a
  contact) is sent out successfully, the email object is deleted. The email message's content lives
  in the chatter of the related record. It prevents cluttering the database with multiple copies of
  the content of the same email (when sent to multiple recipients) if the content is already present
  in the chatter.
- There is no concept of (blind) carbon copy ([B]CC). Odoo uses the concept of *followers* added to
  a chatter to automatically decide when and how :ref:`a contact is notified
  <email-outbound-notifications>` or receives a copy of an email.
- Incoming emails are handled by checking if the *TO* email address is a valid email address in the
  Odoo database or, in case of a reply email, if there is a reference in the email header that
  matches a message sent from the Odoo database. All other emails will be bounced and **not**
  temporarily parked in a spam or quarantine folder. In other words, any email unrelated to an Odoo
  database is lost.

.. _email-issues-outgoing:

Outgoing emails
===============

.. _email-issues-outgoing-admin-address:

Changing the email address of the admin user account
----------------------------------------------------

When an Odoo database is created, the main admin account is assigned a placeholder email address. It
is recommended to **replace the admin email address** with a valid email address to prevent outgoing
email issues.

To do so, on the admin account, click the user icon, click :guilabel:`My Profile` (or
:guilabel:`Preferences`), and update the :guilabel:`Email` field found under the
:guilabel:`Preferences` tab. Use a real email address, preferably on the company's :ref:`alias
domain <email-outbound-alias-domain>` (e.g., `admin@company-name.com`).

.. _email-issues-outgoing-delivery-failure:

Delivery failure
----------------

When a message is sent, an :icon:`fa-envelope-o` :guilabel:`(envelope)` icon is displayed in the
chatter. The icon turns red when delivery has failed for at least one recipient.

.. screenshot:: general-email-faq-red-envelope
   :menu: Contacts ‣ (a contact) ‣ chatter
   :shows: A sent message in the chatter with the red envelope icon.
   :highlight: The red envelope.
   :module: mail
   :notes: English UI, crop to the relevant area.

Left-click the envelope to display information about the delivery, and, if possible, the relevant
:ref:`error messages <email-issues-outgoing-delivery-failure-messages>`.

.. screenshot:: general-email-faq-sending-failure-dialog
   :menu: Contacts ‣ (a contact) ‣ chatter ‣ red envelope
   :shows: The "Sending Failures" dialog listing the recipients with the Try Again toggles, the "See Error Details" link, and the "Send & close" / "Ignore all" buttons.
   :highlight: The Try Again column.
   :module: mail
   :notes: English UI, crop to the dialog.

Click :guilabel:`See Error Details` to get extra information for the fail reason, **if** Odoo was
able to process the original error or bounce email.

Click :guilabel:`Send & close` to retry sending the email to all **toggled-on**
(:icon:`fa-toggle-on`) recipients under the :guilabel:`Try Again` column. All **toggled-off**
(:icon:`fa-toggle-off`) recipients will be ignored.

Click :guilabel:`Ignore all` to ignore all currently failing emails and turn the envelope icon from
red to white.

Unsent emails also appear in the Odoo email queue. To access it, activate the :ref:`developer mode
<developer-mode>` and go to :menuselection:`Settings --> Technical --> Email: Emails`.

.. screenshot:: general-email-faq-email-queue
   :menu: Settings ‣ Technical ‣ Email ‣ Emails
   :shows: The email queue list filtered on failed emails, with the "Delivery Failed" status and the Retry button.
   :highlight: The status column.
   :module: mail
   :notes: English UI, developer mode active, crop to the list.

Failed emails display the :guilabel:`Delivery Failed` status. Click :guilabel:`Retry` to put a
failed email in the email queue again. It will then appear with the :guilabel:`Outgoing` status. The
email will be sent again the next time the scheduled action for the email queue runs.

Optionally, queued emails can be sent immediately by clicking :guilabel:`Send Now`. Click
:guilabel:`Cancel Email` to remove it from the email queue.

.. note::
   Sent emails are periodically cleaned from the queue. This is controlled by the *Auto-Vacuum*
   scheduled action that cleans redundant data on your Odoo database.

.. _email-issues-outgoing-delivery-failure-messages:

Common error messages
~~~~~~~~~~~~~~~~~~~~~

.. _email-issues-outgoing-delivery-failure-messages-limit:

Sending limit reached
*********************

Many mail servers and email service providers limit the number of emails that can be sent in a
given period, and block senders that send too many emails to addresses that do not exist or are no
longer valid. When the limit is reached, the emails are not sent and appear with the
:guilabel:`Delivery Failed` status.

If the sending limit is reached, you can:

- Check the limits of your outgoing mail server with its operator (the hosting provider or the
  email service provider), and ask for a higher quota if needed.
- Verify that your :ref:`email aliases are correctly set up and use the appropriate custom domains
  <email-outbound-alias-domain>`, and that :ref:`SPF <email-domain-spf>`, :ref:`DKIM
  <email-domain-dkim>`, and :ref:`DMARC <email-domain-dmarc>` are correctly configured.
- :ref:`Use a dedicated outgoing email server for mass mailings
  <email-outbound-different-servers-personalized>`.
- Retry sending the email later. To do so, activate the :ref:`developer mode <developer-mode>`, go
  to :menuselection:`Settings --> Technical --> Email: Emails`, and click :guilabel:`Retry` next to
  the unsent email.

.. important::
   Every email leaving your Odoo database counts towards the limit, whether triggered manually or
   automatically. By default, any internal message, notification, logged note, etc., counts as an
   email if it notifies someone via email. This can be mitigated by receiving :ref:`notifications in
   Odoo <discuss_app/notification_preferences>` instead of by email.

.. _email-issues-outgoing-delivery-failure-messages-smtp:

SMTP error
**********

`Simple Mail Transport Protocol (SMTP)
<https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol>`_ is a standard used to transmit
emails between email servers and/or email clients.

If you use :ref:`an external STMP server to send emails <email-outbound-custom-domain-smtp-server>`,
a standard set of `SMTP error codes exists
<https://en.wikipedia.org/wiki/List_of_SMTP_server_return_codes#Common_status_codes>`_. While the
code numbers are not specific to Odoo, the exact content of the error message might vary from email
server to email server.

.. example::
   A 550 SMTP permanent delivery error from sendgrid.com:

   .. code-block:: text

      Mail Delivery Failed
      Mail delivery failed via SMTP server 'None'.
      SMTPDataError: 550
      The from address does not match a verified Sender Identity. Mail cannot be sent until this
      error is resolved. Visit https://sendgrid.com/docs/for-developers/sending-email/sender-identity/
      to see the Sender Identity requirements

   The error message indicates that you tried sending an email from an unverified email address.
   Investigating the outgoing email server configuration or the default *FROM* address of your
   database is a good starting point to troubleshoot the issue, and verify that you whitelisted the
   email address on the side of sendgrid.com.

Usually, inputting the error message content in a Google search can yield information on what the
root cause might be and how to correct the issue.

If the issue cannot be resolved and keeps occurring, contact :ref:`your support provider
<email-issues-support>`.

.. _email-issues-outgoing-delivery-failure-messages-no-error:

No error populated
******************

Odoo is not always capable of providing information on the reason a delivery failed. The different
email providers implement their own policy on bounced emails, and it is not always possible for Odoo
to interpret it correctly.

If there is a recurring problem with the same customer or the same domain, contact :ref:`your
support provider <email-issues-support>`.

.. note::
   One of the most common reasons for an email failing to be sent with no error message is related
   to the :ref:`SPF <email-domain-spf>` or :ref:`DKIM <email-domain-dkim>` configuration. Also,
   verify that the implemented email notification setup is adapted to your business needs. See the
   :doc:`Communication in Odoo by email documentation <../email_communication>` for more
   information.

.. _email-issues-outgoing-execution-time:

Execution time
--------------

The exact time of an email is sent is handled by a system utility *cron* (scheduled action) that can
be used to schedule tasks to run automatically at predetermined intervals. Odoo uses this approach
to send emails that are considered "not urgent" (i.e., newsletters formats such as mass mailing,
and events). This avoids cluttering the mail servers and, instead, prioritizes
individual communication.

.. spoiler:: What is a cron?

   A cron is an action that Odoo runs in the background to execute particular code to complete a
   task. Odoo also creates cron triggers in certain workflows that can trigger a scheduled action
   earlier than its scheduled date. Running a scheduled action manually or changing its frequency
   is generally not recommended, as it might create errors or break specific workflows.

By default, for the normal email queue, the :guilabel:`Mail: Email Queue Manager` cron runs every 60
minutes. An interval of 15 minutes is recommended to ensure proper operation. If the interval is too
short, not all emails may be processed, which may cause the cron to timeout.

Emails that are considered urgent (from one person to another, such as sales orders, invoices,
purchase orders, etc.) are sent immediately. They do not show up under :menuselection:`Settings -->
Technical --> Email: Emails`, unless their delivery fails.

.. screenshot:: general-email-faq-mailing-queued
   :menu: Email Marketing ‣ (a mailing in queue)
   :shows: The mailing form with the blue information banner stating that the mailing is queued and will be sent as soon as possible.
   :highlight: The banner.
   :module: mass_mailing
   :notes: English UI, crop to the form header.

Email campaigns are sent as soon as possible (after clicking the :guilabel:`Send` button) or at a
scheduled time (after clicking the :guilabel:`Schedule` button).

For the email marketing queue, the :guilabel:`Mail Marketing: Process queue` cron runs once a day,
but will be **automatically triggered early** if a campaign is scheduled outside of this default
frequency. If a mailing list contains a large number of recipients, triggering the cron manually
multiple times is **not recommended**, as it will not accelerate the processing time and might
create errors.

.. tip::
   To edit crons, enable the :ref:`developer mode <developer-mode>` and go to
   :menuselection:`Settings --> Technical --> Automation: Scheduled Actions`.

.. _email-issues-outgoing-execution-time-campaigns:

Email Marketing campaigns stuck in the queue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If multiple Email Marketing campaigns are put in the queue, they are processed in chronological
order based on their creation date.

.. example::
   If there are three campaigns: Campaign_1 (created 1st of January), Campaign_2 (created 2nd of
   January), and Campaign_3 (created 3rd of January), they are put in the queue by clicking
   :guilabel:`Send` on all three of them.

   .. screenshot:: general-email-faq-mailing-queue-order
      :menu: Email Marketing ‣ Mailings (List view)
      :shows: List of three mailings Campaign_1, Campaign_2, Campaign_3 with their creation dates and the "In Queue" status.
      :module: mass_mailing
      :notes: English UI, crop to the list.

   The cron will try to process Campaign_1, then Campaign_2, and finally Campaign_3. It will not
   start processing Campaign_2 until it finishes processing Campaign_1.

   If an email campaign never leaves the queue, there might be an issue with the campaign at the top
   of the queue. To troubleshoot, we could remove Campaign_1 from the queue by clicking the
   :guilabel:`Cancel` button, and see if the two other campaigns are sent. Then we could try to fix
   Campaign_1 or contact :ref:`your support provider <email-issues-support>`.

.. _email-issues-incoming:

Incoming emails
===============

When there is an issue with incoming emails, there might not be an indication, per se, in Odoo. It
is the sending email client, who tries to contact a database, that will get a bounce message (most
of the time a :guilabel:`550: mailbox unavailable` error message).

.. _email-issues-incoming-not-received:

Email is not received
---------------------

If there is a recurring issue with the same client or domain, check the server logs and contact
:ref:`your support provider <email-issues-support>`.

Server logs are a text-only record of the actions performed by the Odoo server, with timestamps.
They can be helpful to track emails received by or leaving the database: fetching errors of
incoming mail servers, mail gateway errors, and repeated sending attempts appear in the logs. The
logs are available to the system administrator or the hosting provider.

.. seealso::
   For more information on accessing logs via the command line, refer to the :ref:`developer
   logging documentation <reference/cmdline/server/logging>`.

.. _email-issues-support:

Information for support requests
================================

Here is a list of helpful information to include when reaching out to your support provider (the
hosting provider, your Odoo partner, or your system administrator):

#. An export of the full email from the inbox. These are usually in `.eml` or `.msg` file formats
   containing technical information required for an investigation. The exact process to download the
   file depends on your third-party email provider.

   .. seealso::
      - `Gmail Help Center: Trace an email with its full header
        <https://support.google.com/mail/answer/29436>`_
      - `Microsoft Support: View internet message headers in Outlook <https://support.microsoft.com/en-us/office/view-internet-message-headers-in-outlook-cd039382-dc6e-4264-ac74-c048563d212c#tab=Web>`_

   When using a local email software (e.g., Thunderbird, Apple Mail, Outlook, etc.) to synchronize
   emails, it is usually possible to export the local copies of emails as EML/MSG files. Refer to
   the documentation of the software used for more information.

   .. tip::
      If possible, the EML/MSG file should be based on the original email that was sent and is
      failing or is causing issues.

      For **incoming emails**: if possible contact the original email sender and request an EML/MSG
      copy of the original email. Sending a copy of the original email (forwarded) only contains
      partial information related to the troubleshooting.

      For **outgoing emails**: either provide the EML/MSG of the email or specify what record in the
      database is affected (e.g., sales order number, contact name, invoice number) and the
      date/time when the email was sent (e.g., email sent on the 10th January 2024 11:45 AM Central
      European Time).

#. An explanation of the exact flow that is being followed to normally receive those emails in Odoo.
   Try to answer the following questions:

   - Is this a notification message from a reply being received in Odoo?
   - Is this a message being sent from the Odoo database?
   - Is there an incoming email server being used, or is the email being redirected/forwarded
     through a custom email server or provider?
   - Is there an example of an email that has been correctly forwarded?
   - Have you changed any email-related settings recently? Did it stop working after those changes?

#. An answer to the following questions:

   - Is it a generic issue or is it specific to a use case? If specific to a use case, which one?
   - Is it working as expected? In case the email is sent using Odoo, the bounce email should reach
     the Odoo database and display the :ref:`red envelope <email-issues-outgoing-delivery-failure>`.

=======================
Manage inbound messages
=======================

An inbound message is an email delivered to an Odoo database. Anyone can send an email to an email
alias created in the database or reply to an email that was previously sent from the database based
on the *reply-to* header.

.. _email-inbound-aliases:

Email aliases
=============

.. _email-inbound-aliases-model:

Model specific aliases
----------------------

Some applications have their specific aliases (sales teams, projects, etc.). These
aliases are used to:

- Create a record when an email is sent directly to the alias,
- Receive replies to an email initially sent from a record.

.. example::

   .. screenshot:: general-email-inbound-sales-team-alias
      :menu: CRM ‣ Configuration ‣ Sales Teams ‣ (a team)
      :shows: Sales team form with the Email Alias field set to "info" @ "company-name.com".
      :highlight: The Email Alias field.
      :data: Sales team "Europe".
      :module: crm, mail
      :notes: English UI, crop to the relevant area.

   In the example displayed above, sending an email to `info@company-name.com` will create a
   new opportunity or a new lead automatically assigned to the corresponding sales team. If an email
   is sent from the chatter of an existing opportunity, the *reply-to* will be
   `info@company-name.com`. The reply will be posted in the right chatter, according to the
   *message-id* header.

.. _email-inbound-aliases-catchall:

Catchall
--------

If an application does not have an alias, a generic fallback alias is used: the catchall. An email
sent from a chatter has a reply address set to this catchall alias. A reply sent to the catchall is
posted to the right chatter thanks to the *message-id* header.

By default, the local-part *catchall* will be used. Enable :ref:`developer-mode` and go to
:menuselection:`Settings --> Technical --> Emails: Alias Domains` to access the configuration.

An email to the catchall always needs to be a reply to a previous email sent from the database. If
an email is sent directly to the catchall, the sender will receive the following message:

.. screenshot:: general-email-inbound-catchall-bounce
   :menu: (email client)
   :shows: The automatic bounce email received after writing directly to the catchall address, explaining that the address is only for replies and giving the company email address.
   :module: mail
   :notes: Any email client; English; example domain.

.. note::
   The email address `info@company-name.com` displayed in the screenshot above is the email address
   set on the company. Upon entering the developer mode on a company profile, additional
   configuration options (such as catchall and bounce) become readable. It can be modified by
   clicking on the internal link of the Email Domain. It is generally not recommended to modify
   these options unless specific needs dictate, as it will affect all replies to previously sent
   emails.

.. example::
   An alias can be configured on a sales team in the CRM app. When a customer replies to an email
   coming from the CRM app, the *reply-to* is `info@company-name.com`.

   When an email is sent from the Contact app, the reply address is `catchall@company-name.com`
   because there is no alias on the contact model.

.. note::
   It is advised to keep the local-part of the catchall and the bounce unchanged. If this value is
   modified, previous emails sent from the database will still have the previous local-part values.
   This could lead to replies not being correctly received in the database.

.. _email-inbound-aliases-bounce:

Bounce
------

In the same way the catchall alias is used to build the reply address, the bounce alias is used to
build the *return-path* of the email. The *return-path* is used when emails cannot be delivered to
the recipient and an error is returned to the sender.

By default the name *bounce* will be used. Enable :ref:`developer-mode` and go to
:menuselection:`Settings --> Technical --> Emails: Alias Domains` to access the configuration.

When an error occurs, a notification is received and displayed in a red envelope in the chatter. In
some cases, the red envelope can just contain a `no error` message, meaning there is an error that
could not be handled by Odoo.

A notification will also be displayed in the Discuss icon on the navigation bar.

.. screenshot:: general-email-inbound-failure-navbar
   :menu: Top menu bar ‣ Discuss (messaging) icon
   :shows: The messaging dropdown with a "Delivery failure" notification for an email sent to a contact.
   :highlight: The failure notification.
   :module: mail
   :notes: English UI, crop to the relevant area.

.. example::
   If the email address of the recipient is incorrect, by clicking on the red envelope in the
   chatter an error message containing the reason for the failure will be given.

   .. screenshot:: general-email-inbound-red-envelope
      :menu: Contacts ‣ (a contact) ‣ chatter
      :shows: A sent message in the chatter with the red envelope icon clicked, showing the failure reason (e.g., invalid domain).
      :highlight: The red envelope and the error popover.
      :module: mail
      :notes: English UI, crop to the relevant area.

.. _email-inbound-default:

Receiving emails
================

Odoo does not receive emails by itself: the emails sent to the aliases, the catchall, and the bounce
address of the :ref:`alias domain <email-outbound-alias-domain>` are delivered to the mail server
of that domain, and must then be brought into the database with one of the methods described
below. On hosted databases, this is usually set up by the hosting provider.

.. _email-inbound-custom-domain:

Use a custom domain for inbound messages
========================================

The :ref:`alias domain <email-outbound-alias-domain>` must be selected in the general
settings. If you have multiple companies, each one must be configured.

.. screenshot:: general-email-inbound-alias-domain-setting
   :menu: Settings ‣ General Settings ‣ Emails
   :shows: The "Alias Domain" setting with the company's custom domain selected.
   :highlight: The Alias Domain field.
   :data: Alias domain "company-name.com".
   :module: mail
   :notes: English UI, crop to the relevant area.

All the aliases will use this custom domain. Replies on models for which an alias is configured
are done to `[alias]@my-custom-domain.com`. Replies to other models are sent to the catchall through
`catchall@my-custom-domain.com`.

.. screenshot:: general-email-inbound-custom-domain-diagram
   :menu: (diagram)
   :shows: Diagram of the inbound route with a custom domain: replies and alias emails go to [alias]@my-custom-domain.com, reach the domain's mail server (MX), and are brought into Odoo by redirection, incoming mail server, or MX record to the Odoo mail gateway.
   :module: mail
   :notes: Simple schematic drawing, not a UI screenshot.

.. important::
   If emails are sent using the default mail server while using a custom domain, follow the
   :ref:`"Using a custom domain with the default mail server" instructions
   <email-outbound-custom-domain-odoo-server>`.

Since this custom domain is used, all emails using an alias (replies, bounces and direct sends) are
sent to an address of the domain. They are thus delivered to the email server linked to the domain
(MX record). To display them in the chatter or to create new records, it is necessary to retrieve
these incoming emails in the Odoo database.

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Method
     - Benefits
     - Drawbacks
   * - :ref:`Redirections <email-inbound-custom-domain-redirections>`
     - Easy to set up, emails are directly sent to the database.
     - Each alias of a database needs to be configured.
   * - :ref:`Incoming mail servers <email-inbound-custom-domain-incoming-server>`
     - Allows to keep a copy of the email in your mailbox (with IMAP).
       Allows to create records in the chosen model.
     - Depends on a CRON, meaning emails are not retrieved immediately in the database.
       Each alias of a database needs to be configured.
   * - :ref:`MX record <email-inbound-custom-domain-mx>`
     - Only one record needs to be created to make all aliases work properly.
     - Using a subdomain is required.
       Requires advanced technical knowledge.

.. important::
   The redirection and the MX record methods require a mail server that passes the emails to the
   Odoo database through the :doc:`mail gateway script
   </administration/on_premise/email_gateway>`. Going
   through this script requires **advanced technical and infrastructure knowledge**.

.. important::
   Refer to your provider’s documentation for more detailed information on how to handle the methods
   detailed below.

.. _email-inbound-custom-domain-redirections:

Redirections
------------

Redirections allow messages to be received without delay in the database. The mailboxes of the
custom domain are redirected to the addresses on which the database receives emails through the
mail gateway (e.g., a dedicated subdomain provided by the hosting provider or the system
administrator).

It is mandatory to redirect the catchall and bounce address. Every other alias used must be
redirected as well.

.. example::
   With one sales team, and a receiving domain `odoo.company-name.com`, the following redirections
   are required:

   - `catchall@company-name.com` → `catchall@odoo.company-name.com`
   - `bounce@company-name.com` → `bounce@odoo.company-name.com`
   - `info@company-name.com` → `info@odoo.company-name.com`

.. important::
   Some providers ask to validate the redirection by sending a link to the target email address.
   This procedure is an issue for catchall and bounce since they are not used to create records.

   #. Modify the catchall value on the mail alias domain. :ref:`developer-mode` must be enabled to
      access this menu. For example, it can be changed from `catchall` to `temp-catchall`. This will
      allow to use `catchall` as the local-part of another alias.
   #. Open an app that uses an alias. For example, CRM contains aliases for each sales team. Set
      `catchall` as the local-part of the alias of a sales team.
   #. The validation email will create a record in the CRM app. The email sent will be visible in
      the chatter, allowing you to validate the redirection.
   #. Do not forget to change back the alias of the sales team and the catchall value on the mail
      alias domain, just as they were before this procedure.

.. note::
   An alternative to redirections is **forwarding**. With forwarding, **the address forwarding the
   email will be identified as the sender**, while with redirections, the original sender will
   always remain.

.. _email-inbound-custom-domain-incoming-server:

Incoming mail servers
---------------------

As mentioned earlier, using redirections is the recommended method to receive emails in Odoo.
However, it is also possible to set up incoming mail servers. Using this method means creating an
incoming email server for each mailbox on your server, catchall, bounce, and every alias of the
database, in order to fetch all incoming emails.

.. warning::
   Odoo's *Incoming Mail Servers* feature is designed for shared inboxes (e.g.,
   `sales@yourcompany.com` or `support@yourcompany.com`) to route messages to team pipelines,
   tasks, or other documents.

   Using personal email addresses (e.g., `mitchell.admin@yourcompany.com`) as incoming mail servers
   is **not** recommended. Doing so can lead to increased security risks, unintended message
   routing, privacy issues, and difficulties syncing replies correctly.

Incoming mail servers are created by going to :menuselection:`Settings --> Technical --> Emails:
Incoming Mail Servers`, or, after enabling :guilabel:`Use Custom Email Servers` in the
:guilabel:`Emails` section of the :menuselection:`Settings` app, by clicking :guilabel:`Incoming
Email Servers`.

The incoming mail server form contains the following fields:

- :guilabel:`Name` and :guilabel:`Server Type` (:guilabel:`IMAP Server`, :guilabel:`POP Server`,
  :guilabel:`Local Server`, or, depending on the installed modules, Gmail or Outlook OAuth).
- :guilabel:`Server Information`: the server name, port, and :guilabel:`SSL/TLS` option.
- :guilabel:`Login Information`: the username and password of the mailbox.
- :guilabel:`Create a New Record`: the model in which new records are created for emails that are
  not replies to an existing conversation.
- :guilabel:`Keep Attachments` and :guilabel:`Keep Original` (in the :guilabel:`Advanced` tab):
  whether attachments and a full copy of the original email are kept.

Click :guilabel:`Test & Confirm` to validate the connection, and :guilabel:`Fetch Now` to retrieve
the emails immediately.

.. important::
   We recommend using the IMAP protocol over the POP protocol, as IMAP fetches all unread emails,
   while POP fetches all the emails' history and then tags them as deleted in your mailbox.

.. tip::
   It is also possible to connect a mailbox through :doc:`Gmail with Google OAuth <google_oauth>` or
   :doc:`Outlook with Microsoft Azure OAuth <azure_oauth>`.

Regardless of the protocol chosen, emails are fetched using the *Mail: Fetchmail Service* scheduled
action.

Additionally, using an incoming mail server in Odoo gives the opportunity to create new records in a
specified model. Each incoming mail server can create records in a different model.

.. example::
   Emails received on `task@company-name.com` are fetched by the Odoo database. All fetched emails
   will create a new project task in the database.

   .. screenshot:: general-email-inbound-server-form
      :menu: Settings ‣ Technical ‣ Email ‣ Incoming Mail Servers ‣ New
      :shows: Incoming mail server form: Name, Server Type "IMAP Server", server, port, SSL/TLS, username, password, and "Create a New Record" set to Task.
      :highlight: The "Create a New Record" field.
      :data: Server "Tasks mailbox", imap.company-name.com, user task@company-name.com.
      :module: mail
      :notes: English UI, developer mode active, crop to the form; blur the password.

.. _email-inbound-custom-domain-mx:

MX record
---------

A third option is to create a MX record in your DNS zone which specifies the mail server managing
emails sent to your domain. **Advanced technical knowledge is required.**

.. important::
   This configuration requires a dedicated subdomain (e.g., `@mail.mydomain.com`) whose MX record
   points to a mail server that passes all received emails to the Odoo database through the mail
   gateway. Ask your hosting provider or system administrator for the value of the MX record.

.. _email-inbound-loops:

Infinite email loops
====================

In some cases, infinite mailing loops can be created. Odoo provides some protection against such
loops, ensuring the same sender cannot send too many emails **that would create records** to an
alias in a specific time span.

By default, an email address can send up to 20 emails in 120 minutes. If more emails are sent, they
are blocked and the sender receives the following message:

.. screenshot:: general-email-inbound-loop-bounce
   :menu: (email client)
   :shows: The automatic reply received after sending too many emails to an alias in a short time, explaining that the message was blocked.
   :module: mail
   :notes: Any email client; English; example domain.

To change the default behavior, enable :ref:`developer-mode`, then go to :menuselection:`Settings
--> Technical --> Parameters: System Parameters` to add two parameters.

- For the first parameter, enter `mail.gateway.loop.minutes` as the :guilabel:`Key` and choose a
  number of minutes as the :guilabel:`Value` (`120` is the default behavior).
- For the second parameter, enter `mail.gateway.loop.threshold` as the :guilabel:`Key` and choose a
  number of emails as the :guilabel:`Value` (`20` is the default behavior).

Allow alias domain system parameter
===================================

Incoming aliases are set in the Odoo database to create records by receiving incoming emails. To
view aliases set in the Odoo database, first activate the :ref:`developer mode <developer-mode>`.
Then, go to :menuselection:`Settings app --> Technical --> Aliases`.

The following system parameter, `mail.catchall.domain.allowed`, set with allowed alias domain
values, separated by commas, filters out correctly addressed emails to aliases. Setting the domains
for which the alias can create a task, lead, opportunity, etc., eliminates false positives where
email addresses with only the prefix alias, not the domain, are present.

In some instances, matches have been made in the Odoo database when an email is received with the
same alias prefix and a different domain on the incoming email address. This is true in the sender,
recipient, and :abbr:`CC (Carbon Copy)` email addresses of an incoming email.

.. example::
   When Odoo receives emails with the `commercial` prefix alias in the sender, recipient, or
   :abbr:`CC (Carbon Copy)` email addresses (e.g. commercial\@example.com), the database falsely
   treats the email as the full `commercial` alias, with a different domain, and therefore, creates
   a task/lead/opportunity/etc.

To add the `mail.catchall.domain.allowed` system parameter, first, activate the :ref:`developer mode
<developer-mode>`. Then, go to :menuselection:`Settings app --> Technical --> System Parameters`.
Click :guilabel:`New`. Then, type in `mail.catchall.domain.allowed` for the :guilabel:`Key` field.

Next, for the :guilabel:`Value` field, add the domains separated by commas. Manually
:icon:`fa-cloud-upload` :guilabel:`(Save)`, and the system parameter takes immediate effect.

.. screenshot:: general-email-inbound-allowed-domain
   :menu: Settings ‣ Technical ‣ Parameters ‣ System Parameters ‣ New
   :shows: System parameter form with Key "mail.catchall.domain.allowed" and Value "company-name.com,company-name.hu".
   :highlight: Key and Value.
   :module: base, mail
   :notes: English UI, developer mode active, crop to the form.

Local-part based incoming detection
===================================

When creating a new alias, there is an option to enable :guilabel:`Local-part based incoming
detection`. If enabled, Odoo only requires the local-part to match for routing an incoming email. If
this feature is turned off, Odoo requires the whole email address to match for routing an incoming
email.

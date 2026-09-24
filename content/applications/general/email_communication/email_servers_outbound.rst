========================
Manage outbound messages
========================

.. _email-outbound-default:

Sending emails with the default configuration
=============================================

If no outgoing mail server is configured in the database, Odoo sends emails through the SMTP server
defined in the server's configuration file or command-line options (`smtp_server`, `smtp_port`,
etc.). This default server is set up by the system administrator or the hosting provider.

The sender addresses are built from the company's :ref:`alias domain
<email-outbound-alias-domain>`.

.. example::
   If the alias domain is `company-name.com` and all mailing configurations are the default ones,
   all emails will be sent from `notifications@company-name.com`.

.. _email-outbound-default-from-filtering:

The addresses the default server may send from are defined by the system parameter
`mail.default.from_filter` (or, if it is not set, by the `from_filter` option of the server
configuration).
In case where the sender's domain do not match the value of this parameter, the notification address
is used instead. Multiple values can be defined in this system parameter: comma-separated, domains
or full email addresses are all allowed. Once an :ref:`outgoing mail server is configured
<email-outbound-different-servers-personalized>`, the system parameter is no longer considered
and the value used is the :ref:`FROM filtering
<email-outbound-different-servers-personalized-from-filtering>` of the mail server.

.. screenshot:: general-email-outbound-default-diagram
   :menu: (diagram)
   :shows: Diagram of the default outbound flow: Odoo sends from notifications@<alias domain> through the default SMTP server; replies go to catchall@<alias domain>; delivery errors to bounce@<alias domain>.
   :module: mail
   :notes: Simple schematic drawing, not a UI screenshot; use example.com-style domains.

Emails are sent with `catchall@company-name.com` as the *reply-to* address. In addition,
delivery errors are sent to `bounce@company-name.com`.

.. note::
   The catchall, bounce, and notification addresses do not work like other aliases. They do not have
   the vocation to create records in a database. Emails sent to an alias are automatically routed
   and will reply to an existing and linked record or will create a new one in the database.

.. _email-outbound-custom-domain:

Using a custom domain to send emails
====================================

The database can be configured to use a custom domain, in which case all default email addresses are
built using the custom domain. If the custom domain is `company-name.com`, the sender address will
be `notifications@company-name.com`, the *reply-to* address `catchall@company-name.com`, and the
*bounce* address `bounce@company-name.com`. The custom domain can be utilized when sending emails
either with the default mail server or an external one.

This section assumes ownership of a custom domain. If not, a custom domain must be purchased from a
domain registrar such as GoDaddy, Namecheap, or any alternative provider.

.. _email-outbound-custom-domain-odoo-server:

Using a custom domain with the default mail server
--------------------------------------------------

Some configurations are mandatory in the custom domain's DNS to ensure good deliverability.

.. warning::
   Most of the configuration will be done on the domain provider’s side, and it might require some
   configuration on the mail server itself. **Some technical knowledge is required.**

The first step is to configure the :ref:`SPF <email-domain-spf>` and :ref:`DKIM <email-domain-dkim>`
records so that the mail server sending the emails is authorized for the domain.

Next, the custom domain must be set as the alias domain of a company. Select the company, open the
:guilabel:`Settings`, and add the custom domain under the :guilabel:`Alias Domain` field.

After adding the alias domain, click the :icon:`oi-arrow-right` (:guilabel:`internal link`) icon to
assign more companies to the custom domain if needed. Enable the :ref:`developer-mode` mode to
modify the default aliases if desired:

- :guilabel:`Bounce Alias`: the mailbox used to catch delivery errors and populate the :ref:`red
  envelope <email-issues-outgoing-delivery-failure>` on the corresponding message.
- :guilabel:`Catchall Alias`: the default mailbox used to centralize all replies.
- :guilabel:`Default From Alias`: the default sender address.

.. note::
   At the creation of the first alias domain, all companies will use it. If you create a new
   company, the alias domain automatically set is the one with the lowest priority (ad displayed on
   the alias domain list in :ref:`developer-mode`).

All email aliases (e.g., related to CRM teams or projects) must have their corresponding mailbox in
the custom domain mail server.

.. screenshot:: general-email-outbound-custom-domain-diagram
   :menu: (diagram)
   :shows: Diagram: Odoo sends emails for company-name.com through the default mail server; the domain's DNS holds SPF/DKIM records for that server; replies arrive at the company-name.com mail server and are brought back to Odoo by redirection, incoming mail server or MX record.
   :module: mail
   :notes: Simple schematic drawing, not a UI screenshot.

To receive emails in the Odoo database within the corresponding chatter (CRM, invoices, sales
orders, etc.), one of these three methods must be used:

- :ref:`Redirections/forwarding <email-inbound-custom-domain-redirections>`,
- :ref:`Incoming mail servers <email-inbound-custom-domain-incoming-server>`,
- :ref:`MX record <email-inbound-custom-domain-mx>` (requires advanced technical knowledge)

Using a custom domain implies that specific :ref:`local-parts
<email-outbound-custom-domain-smtp-server-local-part>` might be used by Odoo to send emails.

.. _email-outbound-custom-domain-smtp-server:

Sending emails with an external SMTP server
-------------------------------------------

.. note::
   An external outgoing mail server must be paired with a domain whose DNS records you can manage.

To add an external SMTP server in Odoo, open :guilabel:`Settings`, and enable the :guilabel:`Use
Custom Email Servers` option found under the :guilabel:`Emails` section. Then, click
:guilabel:`Save` at the top of the page to save the changes.

Returning to the :guilabel:`Emails` section, click :guilabel:`Outgoing Email Servers`, then `New` to
create an outgoing mail server record. Most fields are the common parameters used to set up a
connection to an SMTP server; use the values provided by your email provider.

The main fields are:

- :guilabel:`SMTP Server` and :guilabel:`SMTP Port`: the host name (or IP address) and port of the
  SMTP server.
- :guilabel:`Connection Encryption`: :guilabel:`None`, :guilabel:`TLS (STARTTLS)`, or
  :guilabel:`SSL/TLS`, as required by the provider.
- :guilabel:`Authenticate with`: :guilabel:`Username` (with :guilabel:`Username` and
  :guilabel:`Password`), :guilabel:`SSL Certificate`, or :guilabel:`Command Line Interface` (uses
  the SMTP settings of the server configuration). Depending on the installed modules, OAuth
  options such as Gmail or Outlook are also available.
- :guilabel:`FROM Filtering`: see :ref:`email-outbound-different-servers-personalized-from-filtering`.
- :guilabel:`Priority`: the server with the lowest value is used first.

.. screenshot:: general-email-outbound-server-form
   :menu: Settings ‣ General Settings ‣ Emails ‣ Outgoing Email Servers ‣ New
   :shows: The outgoing mail server form with Name, FROM Filtering, Priority, SMTP Server, SMTP Port,
      Connection Encryption, Authenticate with, Username and Password, and the "Test Connection"
      button.
   :highlight: The "Test Connection" button.
   :data: Server "Company SMTP", smtp.example.com, port 587, TLS (STARTTLS), FROM filtering "example.com".
   :module: base, mail
   :notes: English UI, crop to the form; blur the password.

Once completed, click :guilabel:`Test Connection`. Note that a successful test connection does not
confirm that the email will go out as some restriction might remain on the provider side, thus, it
is recommended to consult your provider’s documentation.

.. _email-outbound-custom-domain-smtp-server-local-part:

Local-part values
~~~~~~~~~~~~~~~~~

Below are presented the different local-part values that can be used by Odoo to send emails. It
might be required to whitelist them in your mail server:

- The Alias Domain Bounce Alias (default value = `bounce`),
- The Alias Domain Default From (default value = `notifications`),
- The default admin address (`admin@company-name.com` or, if changed, the new value),
- The default Odoobot address (`odoobot@company-name.com` or, if changed, the new value),
- The specific FROM defined on an email marketing campaign,
- The specific FROM that can be defined in an email template.

.. seealso::
   - :doc:`google_oauth`
   - :doc:`azure_oauth`

.. _email-outbound-different-servers:

Setting up different servers for transactional and mass emails
==============================================================

.. _email-outbound-different-servers-personalized:

Personalized mail servers
-------------------------

Transactional emails and mass mailings can be sent using separate email servers in Odoo. Doing so
means day-to-day emails, quotations, or invoices sent to clients will be handled as *transactional
emails*. *Mass mailing emails*, including the sending of batches of invoices or quotations, will be
managed by the Email Marketing application.

.. example::
   You can use services like Gmail, Amazon SES, or Brevo for transactional emails, and services like
   Mailgun, Sendgrid, or Mailjet for mass mailings.

First, activate the :ref:`developer-mode` and go to :menuselection:`Settings --> Technical -->
Email: Outgoing Mail Servers`. There, add two outgoing email server records, one for the
transactional emails server and one for the mass mailings server. Enter a lower :guilabel:`Priority`
value for the transactional server (e.g., `1`) over the mass mailings server (e.g., `2`) so
transactional emails are given priority.

.. screenshot:: general-email-outbound-two-servers
   :menu: Settings ‣ Technical ‣ Email ‣ Outgoing Mail Servers
   :shows: List of two outgoing mail servers: a transactional server with priority 1 and a mass mailing server with priority 2.
   :highlight: The Priority column.
   :data: Servers "Transactional (smtp.example.com)" and "Mass mailing (smtp.mailing.example.net)".
   :module: base
   :notes: English UI, developer mode active, crop to the list.

Now, go to :menuselection:`Email Marketing --> Configuration --> Settings`, enable
:guilabel:`Dedicated Server`, and select the appropriate email server. Odoo uses the server with the
lowest priority value for transactional emails, and the server selected here for mass mailings.

.. screenshot:: general-email-outbound-dedicated-server
   :menu: Email Marketing ‣ Configuration ‣ Settings
   :shows: The "Dedicated Server" setting enabled with the mass mailing server selected.
   :highlight: The Dedicated Server setting.
   :module: mass_mailing
   :notes: English UI, crop to the setting.

.. _email-outbound-different-servers-personalized-from-filtering:

FROM filtering
~~~~~~~~~~~~~~

.. important::
   It’s **highly recommended** to configure the FROM Filtering on the outgoing mail servers as per
   the instructions of your provider.

The :guilabel:`FROM Filtering` field allows for the use of a specific outgoing email server
depending on the *From* email address or domain that Odoo is sending on behalf of. The **value must
be a domain or a complete address** that matches the sender’s email address and is trusted on the
outgoing mail server provider's side.

If FROM filtering is not used, emails will go out using the notification address.

.. warning::
   Some outgoing mail servers require a specific configuration of the FROM filter.

When an email is sent from Odoo, the following sequence is used to choose the outgoing email server:

- First, Odoo searches for a server that has the same FROM filtering value as the From value (i.e.,
  email address) defined in the outgoing email. This configuration is ideal if all users of a
  company share the same domain but have different local-parts.

.. example::
   If the sender's email address is `test@example.com`, only an email server having a FROM filtering
   value equal to `test@example.com` or `example.com` can be used.

- If no server is found based on the first criteria, Odoo looks for the first server without a FROM
  filtering value set. The email will be overridden with the notification address.

- If no server is found based on the second criteria, Odoo uses the first server, and the email will
  be overridden with the notification address.

.. note::
   To determine which server is first, Odoo uses the priority value (the lower the value is, the
   higher the priority is). Failing to do so, the first server is determined by the servers' names,
   using alphabetical order.

- If there is no mail server, Odoo relies on the :ref:`system parameter
  <email-outbound-default-from-filtering>` value.

It is also possible to combine an outgoing mail server record with the default mail server of the
server configuration.

.. _email-outbound-different-servers-external-odoo:

Using an external email server and the default server
-----------------------------------------------------

If no outgoing mail server is set in the database, the default SMTP server of the server
configuration is used. The same server can also be added as an outgoing mail server record, by
selecting :guilabel:`Command Line Interface` in the :guilabel:`Authenticate with` field, e.g., to
give it a priority and a FROM filter.

.. screenshot:: general-email-outbound-cli-server
   :menu: Settings ‣ Technical ‣ Email ‣ Outgoing Mail Servers ‣ New
   :shows: Outgoing mail server form with "Authenticate with" set to "Command Line Interface" and the
      information text explaining that the server configuration's SMTP settings are used.
   :highlight: The "Authenticate with" field.
   :module: base
   :notes: English UI, developer mode active, crop to the form.

.. example::
   If an outgoing mail server is used simultaneously with the default server (CLI), the FROM
   filter of each server must contain the domain (or addresses) that server is allowed to send
   from. If there is no FROM filtering, the email will go out using the notification address.

.. screenshot:: general-email-outbound-split-servers
   :menu: Settings ‣ Technical ‣ Email ‣ Outgoing Mail Servers
   :shows: List with a "Command Line Interface" server used for transactional emails and an
      external SMTP server used for mass mailing, each with its own FROM filtering and priority.
   :module: base
   :notes: English UI, developer mode active, crop to the list.

.. _email-outbound-custom-domain-external-server:

Using a custom domain with an external email server
===================================================

Similar to the :ref:`previous chapter <email-outbound-different-servers-external-odoo>`, proper
configuration might be needed to ensure that the external email server is allowed to send emails
using your custom domain. Refer to your provider’s documentation to properly set up the relevant
records (SPF, DKIM, and DMARC). A list of the :ref:`most common providers is available
<email-domain-providers-documentation>`.

.. note::
   DNS configuration is required when you use your own domain. The SPF and DKIM records must
   authorize the mail server that actually sends the emails; see :doc:`email_domain`.

.. _email-outbound-port-restriction:

Port restriction
================

Port 25 is often blocked by hosting and cloud providers for security reasons. If the connection
fails on port 25, try using port 465, 587, or 2525 instead.

.. _email-outbound-alias-domain:

Alias domain
============

The catchall domain is company-specific. By default, all companies share the same alias domain, but
each company may have its own custom email domain, selected in the :guilabel:`Alias Domain` field
of the :menuselection:`Settings` app.

When the :ref:`developer-mode` is activated, the alias domain options are available by going to
:menuselection:`Settings --> Technical --> Email: Alias Domains`.

.. warning::
   Any modification of the alias domain must be done very carefully. If one of the aliases (bounce,
   catchall, default from) is changed, all previous emails that are not properly redirected to the
   new aliases will be lost.

The :guilabel:`Default From Alias` field can be filled with a local-part of the email address (by
default `notifications`) or a full email address. Configure it to determine the `FROM` header of
your emails. If a full email address is used, all outgoing emails will be overwritten with this
address.

.. _email-outbound-notifications:

Notification system
===================

When an email is sent from the chatter, customers can reply directly to it. If a customer replies
directly to an email, the answer is logged in the same chatter, thus functioning as a message thread
related to the record.

Upon receiving the reply, Odoo then uses the subscribed followers (based on the subscribed subtypes)
to send them a notification by email, or in the Odoo inbox, depending on the user’s preferences.

.. example::
   If a customer with the email address `“Mary” <mary@customer.example.com>` makes a direct reply to
   an email coming from the Odoo database, Odoo's default behavior is to redistribute the email's
   content to all other followers within the thread.

   As Mary’s domain does not belong to the alias domain, Odoo overrides the email address and uses
   the notification email address to notify the followers. This override depends on the
   configuration done in the database. By default, the email `FROM` address will be overridden with
   the value `notifications@company-name.com` instead of `mary@customer.example.com`.

   The address is constructed using the name of the sender and
   `{alias domain, default from alias}`@`{alias domain, domain name}`, by default,
   `notifications@company-name.com`.

.. _email-outbound-unique-address:

Using a unique email address for all outgoing emails
====================================================

To force the email address from which emails are sent, activate the :ref:`developer-mode`, and go to
:menuselection:`Settings --> Technical --> Email: Alias Domains`. On the :guilabel:`Default From
Alias`, use the local-part or a complete email address as the value.

.. warning::
   If a **complete address** is used as the :guilabel:`Default From Alias` value, **all** outgoing
   emails will be overwritten by this address.

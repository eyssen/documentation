============================================
Configure DNS records to send emails in Odoo
============================================

This documentation presents three complementary authentication protocols (SPF, DKIM, and DMARC) used
to prove the legitimacy of an email sender. Not complying with these protocols will greatly reduce
chances of your emails to reach their destination.

When emails are sent from a **custom domain**, **configuring SPF and DKIM records correctly is
essential** to prevent emails from being quarantined as spam or not being delivered to recipients.

The records must authorize the mail server that actually sends the emails: the :ref:`default mail
server <email-outbound-custom-domain-odoo-server>` of the Odoo server configuration, or the
:ref:`external outgoing mail server <email-outbound-custom-domain-smtp-server>` configured in the
database. The exact values (SPF `include` or IP addresses, DKIM selector and key) are provided by
the operator of that mail server, e.g., the hosting provider or the email service.

.. note::
   Email service providers apply different rules to incoming emails. An email may be classified as
   spam even if it passes the SPF and DKIM checks.

.. _email-domain-spf:

SPF (Sender Policy Framework)
=============================

The Sender Policy Framework (SPF) protocol allows the owner of a domain name to specify which
servers are allowed to send emails from that domain. When a server receives an incoming email, it
checks whether the IP address of the sending server is on the list of allowed IPs according to the
sender's :abbr:`SPF (Sender Policy Framework)` record.

In Odoo, the **SPF test is performed on the bounce address** defined under the :guilabel:`Alias
Domain` field found under the database's :guilabel:`General Settings`. If using a custom domain as
:guilabel:`Alias Domain`, it is necessary to configure it to be SPF-compliant.

The SPF policy of a domain is set using a TXT record. The way to create or modify this record
depends on the provider hosting the :abbr:`DNS (Domain Name System)` zone of the domain name.

If the domain name does not yet have an SPF record, create one using the value given by the mail
server operator, for example:

.. code-block:: bash

   v=spf1 include:_spf.mail-provider.example ~all

If the domain name **already has an SPF record, the record must be updated**. Do not create a new
one, as a domain must have only one SPF record.

.. example::
   If the TXT record is `v=spf1 include:_spf.google.com ~all`, edit it to add
   `include:_spf.mail-provider.example`: `v=spf1 include:_spf.mail-provider.example
   include:_spf.google.com ~all`

Check the SPF record using a tool like `MXToolbox SPF Record Check
<https://mxtoolbox.com/spf.aspx>`_. The process to create or modify an SPF record depends on the
provider hosting the DNS zone of the domain name. The :ref:`most common providers
<email-domain-providers-documentation>` and their documentation are listed below.

.. _email-domain-dkim:

DKIM (DomainKeys Identified Mail)
=================================

The DomainKeys Identified Mail (DKIM) allows a user to authenticate emails with a digital signature.

When sending an email, the outgoing mail server includes a unique :abbr:`DKIM (DomainKeys Identified
Mail)` signature in the headers. The recipient's server decrypts this signature using the DKIM
record in the database's domain name. If the signature and the key contained in the record match, it
proves the message is authentic and has not been altered during transport.

DKIM signing is performed by the mail server, not by Odoo itself. Enabling DKIM is **strongly
recommended** when sending emails **from a custom domain**.

To enable DKIM, add the record provided by the mail server operator to the :abbr:`DNS (Domain Name
System)` zone of the domain name. Depending on the operator, it is a TXT record containing the
public key, or a :abbr:`CNAME (Canonical Name)` record pointing to the operator's key, published
under a *selector*, for example:

.. code-block:: bash

   selector1._domainkey IN TXT "v=DKIM1; k=rsa; p=<public key>"

The way to create or modify a CNAME record depends on the provider hosting the DNS zone of the
domain name. The :ref:`most common providers <email-domain-providers-documentation>` and their
documentation are listed below.

Check if the DKIM record is valid using a tool like `MXToolbox DKIM Record Lookup
<https://mxtoolbox.com/dkim.aspx>`_. Enter `example.com:selector1` in the DKIM lookup tool,
specifying that the selector being tested is `selector1` for the custom domain `example.com`.

.. _email-domain-dmarc:

DMARC (Domain-based Message Authentication, Reporting and Conformance)
======================================================================

The :abbr:`DMARC (Domain-based Message Authentication, Reporting, & Conformance)` record is a
protocol that unifies :abbr:`SPF (Sender Policy Framework)` and :abbr:`DKIM (DomainKeys Identified
Mail)`. The instructions contained in the DMARC record of a domain name tell the destination server
what to do with an incoming email that fails the SPF and/or DKIM check.

.. note::
   The aim of this documentation is to help **understand the impact DMARC has on the deliverability
   of emails**, rather than give precise instructions for creating a DMARC record. Refer to a
   resource like `DMARC.org <https://dmarc.org/>`_ to set the DMARC record.

There are three DMARC policies:

- `p=none`
- `p=quarantine`
- `p=reject`

`p=quarantine` and `p=reject` instruct the server that receives an email to quarantine that email or
ignore it if the SPF or DKIM check fails.

.. note::
   **For the DMARC to pass, the DKIM or SPF check needs to pass** and the domains must be in
   alignment. Configuring DKIM on the sending domain is the most reliable way to pass the DMARC.

Passing DMARC generally means that the email will be successfully delivered. However, it's important
to note that **other factors like spam filters can still reject or quarantine a message**.

`p=none` is used for the domain owner to receive reports about entities using their domain. It
should not impact the deliverability.

.. example::
   :literal:`_dmarc IN TXT “v=DMARC1; p=none; rua=mailto:postmaster@example.com”` means that
   aggregate DMARC reports will be sent to `postmaster\@example.com`.

.. _email_domain/mail_config_common_providers:
.. _email-domain-providers-documentation:

SPF, DKIM and DMARC documentation of common providers
=====================================================

- `OVH DNS <https://docs.ovh.com/us/en/domains/web_hosting_how_to_edit_my_dns_zone/>`_
- `GoDaddy TXT record <https://www.godaddy.com/help/add-a-txt-record-19232>`_
- `GoDaddy SPF, DKIM, or DMARC records <https://www.godaddy.com/help/set-up-spf-dkim-or-dmarc-records-for-my-hosting-email-40810>`_
- `NameCheap <https://www.namecheap.com/support/knowledgebase/article.aspx/317/2237/how-do-i-add-txtspfdkimdmarc-records-for-my-domain/>`_
- `CloudFlare DNS <https://support.cloudflare.com/hc/en-us/articles/360019093151>`_
- `Squarespace DNS records <https://support.squarespace.com/hc/en-us/articles/360002101888-Adding-custom-DNS-records-to-your-Squarespace-managed-domain>`_
- `Azure DNS <https://docs.microsoft.com/en-us/azure/dns/dns-getstarted-portal>`_

To fully test the configuration, use the `Mail-Tester <https://www.mail-tester.com/>`_ tool, which
gives a full overview of the content and configuration in one sent email. Mail-Tester can also be
used to configure records for other, lesser-known providers.

.. seealso::
   - `Using Mail-Tester to set SPF Records for specific carriers
     <https://www.mail-tester.com/spf/>`_


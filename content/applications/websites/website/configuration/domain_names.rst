============
Domain names
============

Domain names are text-based addresses identifying online locations, such as websites. They provide a
more memorable and recognizable way for people to navigate the internet than numerical IP addresses.

A newly installed database is usually reachable through the address assigned by your hosting
provider (e.g., `mycompany.example-hosting.com`). To let visitors reach your website through your
own address (e.g., `www.yourdomain.com`), :ref:`configure a domain name you own
<domain-name/existing>`.

.. note::
   Registering a domain name and managing its :abbr:`DNS (domain name system)` records is done at
   your domain registrar, not in Odoo. If you are unsure which registrar or :abbr:`DNS (domain name
   system)` service hosts your domain, contact your hosting provider or system administrator.

.. _domain-name/dns-records:

DNS records
===========

The following :abbr:`DNS (domain name system)` record types are relevant when connecting a domain
name to a database:

- :guilabel:`A`: an A record holds the IP address a domain points to.
- :guilabel:`CNAME`: CNAME records forward one domain or subdomain to another domain. This is the
  record type used to point the `www.` subdomain to the database.
- :guilabel:`MX`: MX records instruct servers on where to deliver emails sent to the domain.
- :guilabel:`TXT`: TXT records are used for different purposes (e.g., to verify domain name
  ownership, or to publish the SPF and DKIM records used for outgoing emails).

Any modification to the :abbr:`DNS (domain name system)` records can take up to **72 hours** to
propagate worldwide on all servers.

.. seealso::
   :doc:`../../../general/email_communication`

Mailbox
-------

Connecting a domain name to a database does **not** create mailboxes for that domain. To receive
emails at addresses such as `info@yourdomain.com`, either use a subdomain as an alias domain for the
database, or set up an external email provider.

Use a subdomain
~~~~~~~~~~~~~~~

You can create a subdomain (e.g., `subdomain.yourdomain.com`) to use as an alias domain for the
database. It allows users to create records in the database from emails received on their
`email@subdomain.yourdomain.com` alias.

To do so, add a CNAME record at your :abbr:`DNS (domain name system)` provider with the desired
subdomain as the name (e.g., `subdomain`) and the database's original address with a period at the
end as the target (e.g., `mycompany.example-hosting.com.`). Then, ask your hosting provider to
declare the subdomain as an additional domain of the database.

Finally, go to your database and open :menuselection:`Settings`. Under the :guilabel:`Alias Domain`
field, enter the alias domain (e.g., `subdomain.yourdomain.com`), click :guilabel:`Create`, and then
:guilabel:`Save`.

Use an external email provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use an external email provider, configure an MX record at your :abbr:`DNS (domain name system)`
provider. The values to enter for the :guilabel:`Name`, :guilabel:`Content`, and
:guilabel:`Priority` fields depend on the external email provider.

.. seealso::
   - `Google Workspace: MX record values <https://support.google.com/a/answer/174125?hl=en>`_
   - `Outlook and Exchange Online: Add an MX record for email <https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider?view=o365-worldwide#add-an-mx-record-for-email-outlook-exchange-online>`_

.. _domain-name/existing:

Configure an existing domain name
=================================

If you already have a domain name, you can use it for your Odoo website.

.. warning::
   It is strongly recommended to follow **in order** these steps to avoid any :ref:`SSL certificate
   validation <domain-name/ssl>` issues:

   #. :ref:`Add a CNAME record <domain-name/cname>`
   #. :ref:`Redirect your naked domain name <domain-name/naked>` (optional, but recommended)
   #. :ref:`Map your domain name to your Odoo database <domain-name/db-map>`
   #. :ref:`Map your domain name to your Odoo website <domain-name/website-map>`

.. _domain-name/cname:

Add a CNAME record
------------------

Adding a CNAME record to forward your domain name to the address of your Odoo database is required.
The CNAME record's target address is the database's address as provided by your hosting provider
(e.g., `mycompany.example-hosting.com`).

The specific instructions depend on your DNS hosting service.

.. seealso::
   - `GoDaddy: Add a CNAME record <https://www.godaddy.com/help/add-a-cname-record-19236>`_
   - `Namecheap: How to create a CNAME record for your domain <https://www.namecheap.com/support/knowledgebase/article.aspx/9646/2237/how-to-create-a-cname-record-for-your-domain>`_
   - `OVHcloud: Add a new DNS record <https://docs.ovh.com/us/en/domains/web_hosting_how_to_edit_my_dns_zone/#add-a-new-dns-record>`_
   - `Cloudflare: Manage DNS records
     <https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/>`_

.. _domain-name/naked:

Redirect a naked domain
-----------------------

.. note::
   Although optional, completing this step is advised.

To let visitors use your naked domain name :dfn:`(a domain name without any subdomains or prefixes)`
(`yourdomain.com`), creating a 301 redirect :dfn:`(a permanent redirect from one URL to another)`
to `www.yourdomain.com` is required:

- from `http://yourdomain.com` to `https://www.yourdomain.com`, and
- from `https://yourdomain.com` to `https://www.yourdomain.com`.

The specific instructions depend on your DNS hosting service. However, not all of them offer to
redirect a naked domain with a secure HTTPS connection. If you encounter any issue, we recommend
:ref:`using Cloudflare <domain-name/naked/cloudflare>`.

.. _domain-name/naked/cloudflare:

Using Cloudflare to secure and redirect a naked domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. `Sign up and log in to Cloudflare <https://dash.cloudflare.com/sign-up>`_.
#. Enter your domain name on `Cloudflare's dashboard <https://dash.cloudflare.com/login>`_ and
   select :guilabel:`Quick scan for DNS records`.
#. Choose a plan (the free plan is sufficient).
#. Follow Cloudflare's instructions and recommendations to complete the activation.
#. Add a CNAME record to redirect your naked domain (`yourdomain.com`) to the `www` subdomain
   (e.g., `www.yourdomain.com`) by clicking :guilabel:`DNS` in the navigation menu, then clicking
   the :guilabel:`Add record` button, and using the following configuration:

   - :guilabel:`Type`: CNAME
   - :guilabel:`Name`: `@` (or `yourdomain.com`)
   - :guilabel:`Target`: e.g., `www.yourdomain.com`
   - :guilabel:`Proxy status`: Proxied

   .. screenshot:: websites-domain-names-cloudflare-cname-www
      :menu: (Cloudflare dashboard) ‣ DNS ‣ Records ‣ Add record
      :shows: The Cloudflare "Add record" form filled in with Type CNAME, Name "@", Target
         "www.yourdomain.com" and Proxy status "Proxied".
      :highlight: The Type, Name, Target and Proxy status fields (red frame).
      :data: Example domain "yourdomain.com".
      :module: (external website)
      :notes: English UI, light theme, 1440px width, crop to the record form.

#. Add another second CNAME record to redirect the `www` subdomain (e.g., `www.yourdomain.com`) to
   your database address (e.g., `mycompany.example-hosting.com`) using the following configuration:

   - :guilabel:`Type`: CNAME
   - :guilabel:`Name`: e.g., `www.yourdomain.com`
   - :guilabel:`Target`: e.g., `mycompany.example-hosting.com`
   - :guilabel:`Proxy status`: DNS only

   .. screenshot:: websites-domain-names-cloudflare-cname-db
      :menu: (Cloudflare dashboard) ‣ DNS ‣ Records ‣ Add record
      :shows: The Cloudflare "Add record" form filled in with Type CNAME, Name "www", Target the
         database address, and Proxy status "DNS only".
      :highlight: The Proxy status toggle set to "DNS only" (red frame).
      :data: Example domain "yourdomain.com", database address "mycompany.example-hosting.com".
      :module: (external website)
      :notes: English UI, light theme, 1440px width, crop to the record form.

#. Define a redirect rule to permanently redirect (301) your naked domain (e.g., `yourdomain.com`)
   to both `http://` and `https://` by going to :menuselection:`Rules --> Create rule --> Products`,
   and clicking :guilabel:`Create a Rule` under :guilabel:`Redirect Rules`:

   - Enter any :guilabel:`Rule name`.
   - Under the :guilabel:`If incoming requests match...` section, select :guilabel:`Custom filter
     expression` and use the following configuration:

     - :guilabel:`Field`: Hostname
     - :guilabel:`Operator`: equals
     - :guilabel:`Value`: e.g., `yourdomain.com`

   - Under the :guilabel:`Then...` section, use the following configuration:

     - :guilabel:`Type`: Dynamic
     - :guilabel:`Expression`: e.g., `concat("https://www.yourdomain.com", http.request.uri.path)`
     - :guilabel:`Status code`: 301
     - :guilabel:`Preserve query string`: enabled

   .. screenshot:: websites-domain-names-cloudflare-redirect-rule
      :menu: (Cloudflare dashboard) ‣ Rules ‣ Redirect Rules ‣ Create a Rule
      :shows: The Cloudflare redirect rule form with a custom filter expression on Hostname equals
         "yourdomain.com" and a dynamic expression producing "https://www.yourdomain.com" with
         status code 301 and "Preserve query string" enabled.
      :highlight: The "Then..." section with the dynamic expression and the 301 status code
         (red frame).
      :data: Example domain "yourdomain.com".
      :module: (external website)
      :notes: English UI, light theme, 1440px width, full rule form.

#. Go to :guilabel:`SSL/TLS` and set the encryption mode to :guilabel:`Full`.

   .. screenshot:: websites-domain-names-cloudflare-encryption
      :menu: (Cloudflare dashboard) ‣ SSL/TLS ‣ Overview
      :shows: The Cloudflare SSL/TLS encryption mode page with "Full" selected.
      :highlight: The "Full" encryption mode option (red frame).
      :data: Example domain "yourdomain.com".
      :module: (external website)
      :notes: English UI, light theme, 1440px width, crop to the encryption mode selector.

.. _domain-name/db-map:

Map a domain name to an Odoo database
-------------------------------------

.. warning::
   Ensure you have :ref:`added a CNAME record <domain-name/cname>` to your domain name's DNS
   **before** mapping your domain name to your Odoo database.

   Failing to do so may prevent the validation of the :ref:`SSL certificate <domain-name/ssl>` and
   could result in a *certificate name mismatch* error. Web browsers often display this as a
   warning, such as *"Your connection is not private"*.

Once the CNAME record points to the database, ask your hosting provider or system administrator to
declare the domain name (e.g., `www.yourdomain.com`) as a domain served by the database, so that the
web server answers requests sent to that address and issues a certificate for it.

.. _domain-name/ssl:

SSL encryption (HTTPS protocol)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**SSL encryption** allows visitors to navigate a website through a secure connection, which appears
as the *https://* protocol at the beginning of a web address rather than the non-secure *http://*
protocol.

A separate SSL certificate is generated for each domain name mapped to the database, usually through
`Let's Encrypt's certificate authority and ACME protocol <https://letsencrypt.org/how-it-works/>`_.

.. note::
   - Certificate generation may take a few minutes to several hours, depending on the hosting
     setup.
   - Certificates are renewed automatically. If a browser reports an expired or mismatching
     certificate, contact your hosting provider or system administrator.

.. important::
   No SSL certificate is generated for naked domains :dfn:`(domain names without any subdomains
   or prefixes)`.

.. _domain-name/web-base-url:

Web base URL of a database
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
   If the Website app is installed on your database, skip this section and continue from the
   :ref:`Map a domain name to a website <domain-name/website-map>` section.

The *web base URL* or root URL of a database affects your main website address and all the
links sent to your customers (e.g., quotations, portal links, etc.).

To make your custom domain name the *web base URL* of your database, access your database using your
custom domain name and log in as an administrator :dfn:`(a user part of the Settings access right
group under Administration)`.

.. important::
   If you access your database with its original address (e.g., `mycompany.example-hosting.com`),
   the *web base URL* of your database is updated accordingly. To prevent the automatic update of
   the *web base URL* when an administrator logs in to the database, activate the :ref:`developer
   mode <developer-mode>`, go to :menuselection:`Settings --> Technical --> System Parameters -->
   New`, and enter `web.base.url.freeze` as the :guilabel:`Key` and `True` as the
   :guilabel:`Value`.

.. note::
   You can also set the web base URL manually. To do so, activate the :ref:`developer mode
   <developer-mode>`, go to :menuselection:`Settings --> Technical --> System Parameters`, and
   search for the `web.base.url` key (create it if necessary) and enter the full address of your
   website as the value (e.g., `https://www.yourdomain.com`). The URL must include the protocol
   `https://` (or `http://`) and *not* end with a slash (`/`).

.. _domain-name/website-map:

Map a domain name to an Odoo website
------------------------------------

Mapping your domain name to your website is different than mapping it to your database:

- It defines your domain name as the main one for your website, helping search engines to index your
  website correctly.
- It defines your domain name as the base URL for your database, including portal links sent by
  email to your customers.
- If you have multiple websites, it maps your domain name to the appropriate website.

Go to :menuselection:`Website --> Configuration --> Settings`. If you have multiple websites, select
the one you want to configure. In the :guilabel:`Domain` field, enter the address of your website
(e.g., `https://www.yourdomain.com`) and :guilabel:`Save`.

.. screenshot:: websites-domain-names-website-domain-setting
   :menu: Website ‣ Configuration ‣ Settings
   :shows: The Website settings page scrolled to the "Website Info" block, with the "Domain" field
      filled in with "https://www.yourdomain.com".
   :highlight: The "Domain" field (red frame).
   :data: Demo company "YourCompany"; a single website named "My Website".
   :module: website
   :notes: English UI, light theme, 1440px width, crop to the Website Info block.

.. warning::
   Mapping your domain name to your Odoo website prevents search engines from indexing the
   database's original address (e.g., `mycompany.example-hosting.com`).

   If both addresses are already indexed, it may take some time before the indexation of the second
   address is removed. You can use the `Google Search Console
   <https://search.google.com/search-console/welcome>`_ to fix the issue.

.. note::
   If you have multiple websites and companies on your database, make sure to select the right
   :guilabel:`Company` under :menuselection:`Website --> Configuration --> Settings`. Doing so
   indicates Odoo which URL to use as the :ref:`base URL <domain-name/web-base-url>` according to
   the company in use.

.. tip::
   When migrating from an existing website, make sure to set up the necessary :ref:`redirects
   <website/pages/url-redirection>` before adding your domain name. For example, if a previous URL
   like `/path/about/something` existed, redirect it to the new corresponding page on your Odoo
   website, such as `/something`.

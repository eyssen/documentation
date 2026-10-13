==================================
Tracking overview: Google and Meta
==================================

The **Google** and **Meta** (Facebook & Instagram) apps connect your website, your eCommerce store,
your CRM and your point of sale to the advertising and analytics platforms of Google and Meta. They
measure what visitors do on the website, report purchases and leads back to your ad accounts, publish
your product catalog, import the leads of lead ad forms into the CRM, and, for Meta, answer Messenger,
Instagram, and WhatsApp messages from Odoo.

Both apps are built on a **shared base** that handles everything that must be identical for every
platform: the visitor's consent, the queue of events sent from the server, the hashing of personal
data, and the connections to the platform accounts. Small **add-ons** that install by themselves
connect the apps to eCommerce, CRM, and Point of Sale.

.. _tracking/overview/apps:

The two apps
============

.. list-table::
   :header-rows: 1
   :widths: 18 82

   * - App
     - What it does
   * - :doc:`Google </applications/websites/google>`
     - Google Tag Manager, Google tag (Google Analytics 4), Consent Mode v2, Google Ads
       conversions, GA4 Measurement Protocol, Search Console statistics, Business Profile reviews,
       Merchant Center product feeds and synchronization, Google Customer Reviews, offline
       conversions, Customer Match audiences, and Google Ads lead forms.
   * - :doc:`Meta </applications/websites/meta>`
     - Meta Pixel, domain verification, Conversions API, product catalog, Lead Ads and Conversion
       Leads, Facebook and Instagram inbox and posts, and WhatsApp.

Install an app from :menuselection:`Apps`. Installing one of them also installs the shared base. You
can install only the Google app, only the Meta app, or both.

.. _tracking/overview/addons:

Add-ons that install automatically
==================================

The add-ons below are installed automatically as soon as everything they connect is installed. You
do not need to install them yourself. Their names appear in the :menuselection:`Apps` list.

.. list-table::
   :header-rows: 1
   :widths: 26 34 40

   * - Add-on
     - Installs automatically when…
     - What it adds
   * - *Website Tracking & Consent*
     - the Google or the Meta app is installed
     - The shared base: the cookie consent banner that replaces the cookies bar, the
       :guilabel:`Tracking` block of the Website settings, the :guilabel:`Tracking & Consent` menu
       (server events, consent log, cookies, connections), and the click identifiers stored on
       orders and leads.
   * - *Website Tracking for eCommerce*
     - the shared base and eCommerce are installed
     - The eCommerce events (product views, cart, checkout, purchase, refund) and the
       :ref:`eCommerce tracking settings <ecommerce/tracking>`.
   * - *Website Tracking for CRM*
     - the shared base and the Website CRM forms are installed
     - The lead events of website forms and the :doc:`lead stage rules
       </applications/sales/crm/optimize/lead_tracking>` (offline conversions).
   * - *Website Tracking for Point of Sale*
     - the shared base and Point of Sale are installed
     - The :doc:`Report Store Sales </applications/sales/point_of_sale/store_sales_tracking>`
       setting.
   * - *eCommerce Product Feeds*
     - Google for eCommerce or Meta Catalog for eCommerce is installed
     - The :doc:`product feeds </applications/websites/ecommerce/product_feeds>` and the :guilabel:`Marketing` tab of
       the products.
   * - *eCommerce Product Feeds - Stock*
     - product feeds and eCommerce stock management are installed
     - The stock quantities and the availability in the product feeds.
   * - *Google for eCommerce*
     - the Google app and the eCommerce tracking are installed
     - :doc:`Merchant Center </applications/websites/google/merchant_center>`, Google Customer Reviews,
       :doc:`offline purchase conversions and Customer Match </applications/websites/google/offline_conversions>`.
   * - *Google for CRM*
     - the Google app and the CRM tracking are installed
     - The :doc:`Google Ads lead form webhook </applications/websites/google/lead_forms>` and the Google Ads
       conversion action on the lead stage rules.
   * - *Meta Catalog for eCommerce*
     - the Meta app and the eCommerce tracking are installed
     - The :doc:`Meta catalog </applications/websites/meta/catalog>` feed and real-time updates.
   * - *Meta Lead Ads and Conversion Leads for CRM*
     - the Meta app and the CRM tracking are installed
     - :doc:`Lead Ads and Conversion Leads </applications/websites/meta/lead_ads>`.

Two further modules are **not** installed automatically because they change how your company works
every day. Install them from :menuselection:`Apps` if you need them:

- *Meta Social: Facebook & Instagram Inbox and Posts*: :doc:`Messenger and Instagram messages and
  posts </applications/websites/meta/social>`.
- *WhatsApp (Meta Cloud API)*: :doc:`WhatsApp messages and templates </applications/websites/meta/whatsapp>`.

.. note::
   The *Tracking Broker* is a different kind of module: it is installed only on the **central**
   database of a company that offers the connection to Google and Meta as a service to several
   databases. See :doc:`/applications/general/tracking_broker`.

.. _tracking/overview/where:

Where to find the settings
==========================

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Menu
     - Content
   * - :menuselection:`Website --> Configuration --> Settings`
     - :guilabel:`Cookie Consent` (privacy section) and the :guilabel:`Tracking` block: debug
       mode, retention, :guilabel:`Connection Broker`, :guilabel:`eCommerce Tracking`,
       :guilabel:`Lead Tracking`.
   * - :menuselection:`Website --> Configuration --> Tracking & Consent`
     - :guilabel:`Server Events`, :guilabel:`Consent Log`, and :guilabel:`Connections`.
   * - :menuselection:`Google --> Configuration --> Settings`
     - All the settings of the Google app.
   * - :menuselection:`Meta --> Configuration --> Settings`
     - All the settings of the Meta app.
   * - :menuselection:`Website --> eCommerce --> Product Feeds`
     - The product feeds.
   * - :menuselection:`CRM --> Configuration --> Lead Tracking Rules`
     - The lead stage rules.
   * - :menuselection:`Point of Sale --> Configuration --> Settings`
     - :guilabel:`Report Store Sales`.

The settings of the Google and Meta apps apply to **one website**. If your database has several
websites, select the website in the :guilabel:`Settings of Website` field at the top of the settings
page before changing anything.

.. important::
   The menus of the Google and Meta apps are available to the users of the *Website* application who
   have the *Designer* access right. The connections, the secrets, and the webhooks can only be
   changed by an administrator (*Settings* access right).

Getting started
===============

#. Enable :guilabel:`Cookie Consent` in :menuselection:`Website --> Configuration --> Settings`
   and choose how the consent is collected, as described in :doc:`cookie_consent`.
#. Install the Google app, the Meta app, or both.
#. Enter the identifiers of your accounts (measurement ID, container ID, pixel ID…) in the settings
   of the app. These identifiers only make the browser tags work: no connection is needed.
#. For the features that use the platform APIs (Merchant Center, offline conversions, Lead Ads,
   catalog, Search Console, Business Profile, WhatsApp), :doc:`connect your account <connections>`.
#. :doc:`Test <troubleshooting>` that the events arrive.

.. seealso::
   - :doc:`privacy`
   - :doc:`server_events`

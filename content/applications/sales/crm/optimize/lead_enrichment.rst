===============
Lead enrichment
===============

*Lead enrichment* is a service that provides business information for a contact attached to a lead.
Lead enrichment is an In-App Purchase (IAP) that requires credits to use, and is available for
existing leads in an Odoo database.

The information provided by lead enrichment can include general information about the business
(including full business name and logo), social media accounts, :guilabel:`Company type`,
:guilabel:`Founded` information, :guilabel:`Sectors` information, the number of
:guilabel:`Employees`, :guilabel:`Estimated revenue`, :guilabel:`Phone` number,
:guilabel:`Timezone`, and :guilabel:`Technologies Used`.

.. important::
   The *leads* feature **must** be activated in the *CRM* settings page in order to use lead
   enrichment. To access the *CRM* settings, navigate to :menuselection:`CRM app --> Configuration
   --> Settings`. Under the :guilabel:`CRM` section activate the :guilabel:`Leads` option and click
   :guilabel:`Save`.

Lead enrichment set up
======================

To set up lead enrichment in the *CRM* application, navigate to :menuselection:`CRM app -->
Configuration --> Settings`. Then, under the :guilabel:`Lead Generation` section, tick the checkbox
next to :guilabel:`Lead Enrichment`, and select either :guilabel:`Enrich leads on demand only` or
:guilabel:`Enrich all leads automatically`. Click the :guilabel:`Save` button to activate the
changes.

.. screenshot:: sales-crm-lead-enrichment-setting
   :menu: CRM ‣ Configuration ‣ Settings
   :shows: The CRM settings with the "Lead Enrichment" checkbox enabled and the "Enrich leads on demand only" option selected.
   :highlight: The Lead Enrichment setting and its options (red frame).
   :data: Demo company.
   :module: crm_iap_enrich
   :notes: English UI, light theme, 1440px width, crop to the setting block.

Enrich leads
============

Enrichment of leads is based on the domain of the email address of the customer set on the lead.
There are two different ways that a lead can be enriched: *automatically* or *manually*.

Automatically enrich leads
--------------------------

During set up, if :guilabel:`Enrich all leads automatically` was selected on the *CRM*
:guilabel:`Settings` page, then no action needs to be taken by the user to enrich the lead. A
scheduled action runs automatically, every sixty minutes, and enrichment occurs on leads, after a
remote database is contacted.

.. tip::
   To access the cron that runs for the automatic lead enrichment, activate :ref:`developer mode
   <developer-mode>`, and navigate to :menuselection:`Settings app --> Technical menu --> Automation
   section --> Scheduled Actions`. In the :guilabel:`Search...` bar, type in `CRM`. Click into the
   result labeled :guilabel:`CRM: enrich leads (IAP)`, and make any necessary adjustments. In the
   :guilabel:`Execute Every` field, enter a value greater than, or equal to, five minutes.

.. example::
   The following is an example of lead enrichment data that has been autocompleted successfully:

   .. screenshot:: sales-crm-lead-enrichment-chatter
      :menu: CRM ‣ Leads ‣ Leads ‣ (an enriched lead)
      :shows: The chatter of an enriched lead with the note listing the data found (sector, employees, estimated revenue, phone, timezone, technologies used).
      :highlight: The enrichment note (red frame).
      :data: A lead enriched from its email domain.
      :module: crm_iap_enrich
      :notes: English UI, light theme, 1440px width, crop to the chatter.

Manually enrich leads
---------------------

If the :guilabel:`Enrich leads on demand only` option was selected on the *CRM* :guilabel:`Settings`
page, when activating :guilabel:`Lead Enrichment`, each lead that a user wishes to enrich **must**
be manually enriched. This is achieved by clicking the :guilabel:`Enrich` button in the top menu of
the lead.

The same information will be retrieved at the same :abbr:`IAP (In-App Puchase)` credit cost (one per
enrichment). This method of enrichment is useful when every lead does not need to be enriched, or
cost is an issue.

.. screenshot:: sales-crm-lead-enrichment-manual-button
   :menu: CRM ‣ Leads ‣ Leads ‣ (a lead)
   :shows: A lead form with the "Enrich" button next to the email field.
   :highlight: The "Enrich" button (red frame).
   :data: A lead with a company email address.
   :module: crm_iap_enrich
   :notes: English UI, light theme, 1440px width, crop to the field group.

.. tip::
   Manually enrich leads in bulk using the *list* view. First, navigate to :menuselection:`CRM app
   --> Leads`, and click the list view button (:guilabel:`☰ (three horizontal lines)` icon). Next,
   tick the checkboxes for the leads that should be manually enriched. Finally, click the
   :guilabel:`⚙️ Action` icon, and select :guilabel:`Enrich` from the resulting drop-down menu. This
   can also be achieved from the *My Pipeline* page. To do so, simply open the *CRM* app, or
   navigate to :menuselection:`CRM app --> Sales --> My Pipeline`. Either route reveals leads and
   opportunities on the :guilabel:`Pipeline` page.

Pricing
=======

Lead enrichment is an In-App Purchase (IAP) feature, and each enriched lead costs one credit.

.. note::
   See here for full pricing information: `Lead Generation by Odoo IAP
   <https://iap.odoo.com/iap/in-app-services/273>`_.

To buy credits, navigate to :menuselection:`CRM app --> Configuration --> Settings`. In the
:guilabel:`Lead Generation` section, under the :guilabel:`Lead Enrichment` feature, click on
:guilabel:`Buy Credits`.

.. screenshot:: sales-crm-lead-enrichment-buy-credits
   :menu: CRM ‣ Configuration ‣ Settings
   :shows: The Lead Enrichment setting block with the "Buy credits" link beneath it.
   :highlight: The "Buy credits" link (red frame).
   :data: Demo company.
   :module: crm_iap_enrich
   :notes: English UI, light theme, 1440px width, crop to the setting block.

Credits and balances may also be purchased by navigating to the :menuselection:`Settings app`. In
the :guilabel:`Contacts` section, under the :guilabel:`Odoo IAP` feature, click on :guilabel:`View
My Services`.

.. screenshot:: sales-crm-lead-enrichment-iap-services
   :menu: Settings ‣ General Settings ‣ Odoo IAP ‣ View My Services
   :shows: The In-App Purchase services page listing the Lead Enrichment service with its remaining credit balance.
   :highlight: The Lead Enrichment credit balance (red frame).
   :data: A throw-away account with a small balance.
   :module: iap
   :notes: English UI, light theme, 1440px width, crop to the service row.

.. seealso::
   :doc:`../../../essentials/in_app_purchase`

.. important::
   When collecting a company's contact information, make sure to be aware of the latest EU
   regulations. For more information about General Data Protection Regulation, refer to: `Odoo GDPR
   <http://odoo.com/gdpr>`__.

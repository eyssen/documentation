=============================
Lead Ads and Conversion Leads
=============================

With **Lead Ads**, people fill in a form inside the Facebook or Instagram ad, without visiting your
website. Odoo receives each lead **in real time** in the CRM, with its ad and its campaign. Then,
with **Conversion Leads**, Odoo reports to Meta what happens to these leads (qualified, won, lost),
so that Meta shows your ads to the people who are most likely to become customers.

Prerequisites
=============

- A :doc:`Meta connection <connection>` with the *leads retrieval* and *pages* permissions.
- The :ref:`Meta webhooks <meta/webhooks>` enabled and subscribed to the leads of your pages.
- Administrator access for the first setup. The people with the *Sales: Administrator* access right
  manage the forms afterwards.

Receive the leads
=================

Go to :menuselection:`Meta --> Configuration --> Settings`. In the :guilabel:`Lead Ads` block:

#. Enable :guilabel:`Lead Ads`. This setting applies to the whole company.
#. Click :guilabel:`Load Pages`. Odoo reads the Facebook pages that the Meta connection can manage
   and saves their access.
#. Open the :guilabel:`Pages` (also in :menuselection:`Meta --> Lead Ads --> Pages`). For each page
   whose leads you want, click :guilabel:`Subscribe to Leads`. The :guilabel:`Subscribed to Leads`
   box is checked when Meta confirms.
#. Click :guilabel:`Sync Forms` on the page to load its lead forms.

.. screenshot:: meta-settings-lead-ads
   :menu: Meta ‣ Configuration ‣ Settings
   :shows: The Lead Ads block of the Meta settings with the Lead Ads setting enabled: the Load Pages,
      Pages, and Lead Forms links, then the Lead Ads Leads setting with the Lead Tracking Rules link.
   :highlight: The Lead Ads setting and its Load Pages link (red frame).
   :data: Throw-away page.
   :notes: English UI, light theme, 1440px width, crop to the block.

From then on, every lead sent through a form of a subscribed page creates a lead in the CRM within a
few minutes. A form that Odoo does not know yet is added automatically, with the default settings.

Lead forms
----------

The lead forms are in :menuselection:`Meta --> Lead Ads --> Lead Forms` (and in
:menuselection:`CRM --> Configuration --> Meta Lead Forms`). Open a form to set what happens to its
leads:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Import Leads`
     - Creates a CRM lead for each lead of the form. Uncheck it to ignore the form.
   * - :guilabel:`Create As`
     - :guilabel:`Lead` or :guilabel:`Opportunity`.
   * - :guilabel:`Sales Team`, :guilabel:`Salesperson`, :guilabel:`Tags`
     - Applied to the new leads.
   * - :guilabel:`Default Campaign`
     - The campaign of the leads when Meta gives none (organic leads).
   * - :guilabel:`Website`
     - The website whose Meta settings apply to the lead events (Conversion Leads).

In the :guilabel:`Field Mapping` tab, choose for each question of the form the field of the lead that
receives the answer (email, phone, mobile, contact name, company name, job position, street, city,
ZIP, state, country, website, lead title, or notes). The answers that you do not map (:guilabel:`Ignore`
excluded) are added to the **notes** of the lead. Click :guilabel:`Sync Questions` if you changed the
questions in Meta.

.. screenshot:: meta-lead-form
   :menu: Meta ‣ Lead Ads ‣ Lead Forms ‣ (a form)
   :shows: A Meta lead form with the Sync Questions button, the Meta group (page, form ID, language,
      Import Leads), the Leads group (Create As, sales team, salesperson, tags, default campaign),
      the Leads smart button, and the Field Mapping tab with questions mapped to lead fields.
   :highlight: The Field Mapping tab (red frame).
   :data: Form "Free quote" with email, phone, and company questions.
   :notes: English UI, light theme, 1440px width.

Import past leads
-----------------

In the :guilabel:`Import Past Leads` tab of a form, choose a date and click :guilabel:`Import
Leads`. Odoo imports the leads received since this date and tells how many are new. Meta keeps the
leads for **90 days**. Leads already imported are not duplicated.

The leads in the CRM
--------------------

Each lead is created once (a notification repeated by Meta is ignored). It contains:

- the contact details from the form, and the other answers in its notes;
- the source :guilabel:`Facebook` or :guilabel:`Instagram`, the medium `Lead Ads`, and the
  campaign of the ad;
- the :guilabel:`Meta Lead Ads` group with the Meta lead ID, the form, the platform, the ad, and the
  campaign.

Filter the leads with :guilabel:`Meta Lead Ads` in the search bar of the CRM.

.. note::
   The person gave their data to you in the Meta form, with the consent screen of Meta: no cookie consent
   is needed for these leads.

.. _meta/lead-ads/conversion-leads:

Conversion Leads
================

Conversion Leads tell Meta which leads become customers. Enable :guilabel:`CRM Lead Events` in the
:doc:`Conversions API <conversions_api>` block, then manage the events in the :doc:`lead
tracking rules </applications/sales/crm/optimize/lead_tracking>`
(:menuselection:`CRM --> Configuration --> Lead Tracking Rules`). Each rule has a :guilabel:`Meta`
group:

- :guilabel:`Send to Meta`: reports the stage to Meta (enabled by default).
- :guilabel:`Meta Event Name`: the name of the stage as it is configured in Meta Events Manager (for
  example `Qualified` or `Converted`). If empty, the name of the rule is used.

The :guilabel:`Lead Ads Leads` setting (enabled by default) sends the events of the leads that come
from Lead Ads **without cookie consent** (they gave their consent in the Meta form), with their Meta
lead ID. This is what lets Meta optimize the campaigns for the leads that convert. Uncheck it if you
prefer to send only the leads whose consent you collected yourself.

.. _meta/lead-ads/test:

Test Lead Ads
=============

#. In the *Lead Ads Testing Tool* of Meta (*Tools > Lead Ads Testing*), select your page and your form,
   and click *Create lead*.
#. In Odoo, open the CRM. The test lead appears within a few minutes, with the source Facebook.
#. If it does not appear, open :menuselection:`Meta --> Webhook Notifications`: the notification
   should be there, in the status :guilabel:`Processed`. See
   :ref:`meta/webhooks/troubleshooting`.
#. Change the stage of the lead to a stage that has a rule, and check in :menuselection:`Meta -->
   Server Events` that the event is sent.

The most frequent problems are a page that is not subscribed, the :guilabel:`Lead Ads` setting
disabled, a form with :guilabel:`Import Leads` unchecked, and an expired Meta connection.

.. seealso::
   - :doc:`/applications/sales/crm/optimize/lead_tracking`
   - :doc:`connection`
   - :doc:`conversions_api`

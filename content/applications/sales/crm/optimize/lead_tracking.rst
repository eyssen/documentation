=============
Lead tracking
=============

When the Google app or the Meta app is installed, the CRM reports the progress of your leads to the
advertising platforms. Google Ads and Meta then know which clicks and which ads produce real customers,
not only form submissions, and can optimize your campaigns for them.

Two kinds of events are sent:

- the **new lead** event, when a visitor submits a website form that creates a lead;
- the **stage events**, when a lead reaches a stage, is won, or is lost. They are defined by *lead
  stage rules*.

All events respect the cookie consent that the visitor gave when the lead was created, except the
leads that come from a lead form of Google or Meta, who gave their consent in the ad. See
:doc:`/applications/websites/website/tracking/privacy`.

Website form leads
==================

When a website form creates a lead, the lead stores the **click identifiers** of the visit (Google Ads
click IDs and Meta click and browser IDs) and the consent of the visitor. A `generate_lead` event is
sent by the browser and by the server, with the same event ID so that the platforms count it once.

To give a value to this event, go to :menuselection:`Website --> Configuration --> Settings`, and in
the :guilabel:`Tracking` block, fill in the :guilabel:`Lead Value` of the :guilabel:`Lead Tracking`
setting. `0` means that the event has no value.

.. note::
   In developer mode, the :guilabel:`Ad Tracking` tab of the lead shows the stored identifiers and
   consent.

.. _crm/lead-tracking/rules:

Lead stage rules
================

Go to :menuselection:`CRM --> Configuration --> Lead Tracking Rules`, and click :guilabel:`New`. A
rule says: *when this happens to a lead, send this event*.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Name`
     - The name of the rule.
   * - :guilabel:`Trigger`
     - :guilabel:`Lead is created`, :guilabel:`Lead reaches a stage`, :guilabel:`Lead is won`, or
       :guilabel:`Lead is lost`.
   * - :guilabel:`Stage`
     - The stage, for the trigger :guilabel:`Lead reaches a stage`.
   * - :guilabel:`Sales Teams`
     - Restricts the rule to some teams. Empty: all the teams.
   * - :guilabel:`Only Tracked Leads`
     - Enabled by default. The rule only applies to the leads that carry an ad click identifier, or the
       ID of a Meta lead. The other leads cannot be attributed to a campaign.
   * - :guilabel:`Event`
     - The event sent: :guilabel:`New lead`, :guilabel:`Working on the lead`, :guilabel:`Qualified
       lead`, :guilabel:`Disqualified lead`, :guilabel:`Won (converted)`, or :guilabel:`Lost (not
       converted)`.
   * - :guilabel:`Value`
     - :guilabel:`Expected revenue` of the lead (default), a :guilabel:`Fixed value`, or
       :guilabel:`No value`.

.. screenshot:: crm-lead-tracking-rule
   :menu: CRM ‣ Configuration ‣ Lead Tracking Rules ‣ (a rule)
   :shows: A lead tracking rule form with the When group (trigger, stage, sales teams, only tracked
      leads), the Send group (event, value), and the destination fields of Google (Google Ads
      Conversion Action ID) and Meta (Send to Meta, Meta Event Name).
   :highlight: The destination fields (red frame).
   :data: Rule "Qualified" on the stage Qualified, event Qualified lead, expected revenue.
   :notes: English UI, light theme, 1440px width, developer mode off.

Destinations
------------

Each platform adds its fields to the rule:

- **Google Ads**: the :guilabel:`Google Ads Conversion Action ID` of the conversion action of type
  *Import from clicks* that receives this stage. Without an ID, the rule is not uploaded to Google Ads.
  See :doc:`/applications/websites/google/lead_forms` and
  :doc:`/applications/websites/google/offline_conversions`.
- **Meta**: :guilabel:`Send to Meta` (enabled by default), and the :guilabel:`Meta Event Name`, which
  is the name of the stage in Meta Events Manager. If empty, the name of the rule is used. See
  :ref:`meta/lead-ads/conversion-leads`.
- **Google Analytics 4**: when the :doc:`Measurement Protocol
  </applications/websites/google/measurement_protocol>` and its lead events are enabled, the events
  are also sent to GA4, whatever the destination fields.

Each destination has its own switch in the settings of the Google or the Meta app
(:guilabel:`CRM Offline Conversions`, :guilabel:`CRM Lead Events`). A rule is sent only to the
destinations that are enabled for the website of the lead.

Behavior
--------

- A rule sends its event **once** per lead and per rule. When a lead goes back to a previous stage and
  reaches the stage again, nothing is sent twice.
- A lead is linked to the website where it was created. A lead created in the CRM without a website
  uses the first website of its company.
- The events are put in the queue of the :doc:`server events
  </applications/websites/website/tracking/server_events>`, and sent every few minutes. You can follow
  them there.

.. tip::
   For a good optimization, report few and clear stages: for example *Qualified* and *Won*. Keep the
   *Expected revenue* up to date: it is the value that Google and Meta learn from.

.. seealso::
   - :doc:`/applications/websites/google/lead_forms`
   - :doc:`/applications/websites/meta/lead_ads`
   - :doc:`/applications/websites/website/tracking/privacy`

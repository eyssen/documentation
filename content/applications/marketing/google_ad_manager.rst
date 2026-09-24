:show-content:

=================
Google Ad Manager
=================

The *Google Ad Manager* module (`google_ad_manager`) brings the ad trafficking objects of a Google
Ad Manager network into Odoo and keeps them in sync in both directions. Sales orders, line items,
creatives and the ad inventory can be reviewed — and, where Google allows it, maintained — from
Odoo, next to the advertisers that are already contacts in the database.

Configuration
=============

Connection
----------

Go to :menuselection:`Ad Manager --> Configuration --> Connections` and create a connection:

- :guilabel:`Name`: a name for this connection.
- :guilabel:`Company`: the Odoo company the connection belongs to.
- :guilabel:`Network Code`: the code of the Google Ad Manager network.
- the **service account key** of the Google service account authorized on that network.
- :guilabel:`Application Name`: the name reported to Google, `eYssen Odoo` by default.
- :guilabel:`Synchronization enabled` and :guilabel:`Sync Interval (min)`: whether the scheduled
  synchronization runs for this connection, and how often.

:guilabel:`Test Connection` verifies the credentials and fills in the network's display name,
currency, time zone and root ad unit, which are read from Google and cannot be edited in Odoo.
:guilabel:`Sync Now` starts a synchronization immediately.

.. screenshot:: marketing-google-ad-manager-connection
   :menu: Ad Manager ‣ Configuration ‣ Connections ‣ New
   :shows: A Google Ad Manager connection form with the name, company, network code, service account key and application name fields, the synchronization options, the read-only network information, and the Test Connection and Sync Now buttons.
   :highlight: The Network Code field and the Test Connection button (red frame).
   :data: Network code 123456789; use a throw-away service account key.
   :module: google_ad_manager
   :notes: English UI, light theme, 1440px width.

.. warning::
   The service account key gives full access to the ad network. Treat it as a password: only users
   who administer the connection should be allowed to open it.

Synchronization
---------------

Each synchronization is recorded under :menuselection:`Ad Manager --> Reporting --> Sync Runs`, with
its start and end time, its status, the number of records pulled from Google, pushed to Google,
skipped, and in error, and the full log. This is the place to look when a record does not appear, or
when a change made in Odoo did not reach Google.

.. screenshot:: marketing-google-ad-manager-sync-runs
   :menu: Ad Manager ‣ Reporting ‣ Sync Runs
   :shows: The Sync Runs list with the connection, start and end time, status and the pulled, pushed, skipped and error counters.
   :highlight: The status and counter columns (red frame).
   :data: About ten synchronization runs, one of them with errors.
   :module: google_ad_manager
   :notes: English UI, light theme, 1440px width.

Every synchronized record carries its own state, shown on the record itself:

- :guilabel:`New local`: created in Odoo, not sent to Google yet;
- :guilabel:`Dirty local`: changed in Odoo since the last synchronization;
- :guilabel:`Synced`: identical on both sides;
- :guilabel:`Error`: the last synchronization of this record failed; the reason is shown on the
  record;
- :guilabel:`Pending archive` and :guilabel:`Archived`: the record is being, or has been, archived.

A single record can be synchronized on its own with the :guilabel:`Sync` button on its form, which
is useful after fixing the cause of an error.

Advertisers and agencies
========================

:menuselection:`Ad Manager --> Companies` lists the advertisers and agencies of the network, with
their :guilabel:`Type` and contact email. Each of them can be linked to an Odoo :guilabel:`Contact`,
so that the ad orders of a customer can be related to the rest of their file.

Orders and line items
=====================

:menuselection:`Ad Manager --> Orders` lists the ad orders, each with its
:guilabel:`Advertiser`, :guilabel:`Agency`, :guilabel:`Status`, :guilabel:`Trafficker`,
:guilabel:`Salesperson`, the period it runs, and its currency and notes.

An order's :guilabel:`Line Items` (:menuselection:`Ad Manager --> Line Items`) describe what is
actually delivered:

- :guilabel:`Type` and :guilabel:`Priority`: the kind of line item and its priority in ad serving;
- :guilabel:`Cost Type` and :guilabel:`Rate`: how the line item is charged (e.g., CPM) and at which
  rate, in the order's currency;
- :guilabel:`Start` and :guilabel:`Target End`: the booked period, the effective end date coming
  back from Google;
- :guilabel:`Environment`: where the ad is served, for example in a browser.

.. screenshot:: marketing-google-ad-manager-line-item
   :menu: Ad Manager ‣ Line Items ‣ (line item)
   :shows: A line item form with its order, type, status, cost type and rate, the start and end dates, the environment, the inventory targeting and the associated creatives.
   :highlight: The cost type and rate fields (red frame).
   :data: A CPM line item of EUR 4.50 on a two-month order.
   :module: google_ad_manager
   :notes: English UI, light theme, 1440px width.

Inventory
=========

:menuselection:`Ad Manager --> Inventory` holds the ad space of the network:

- :guilabel:`Ad Units`: the ad slots, organized as a tree under the network's root ad unit, with
  their code, status and the accepted sizes;
- :guilabel:`Placements`: named groups of ad units that can be targeted as one.

Line items are targeted at ad units and placements, so the inventory determines where each line item
can be served.

Creatives
=========

:menuselection:`Ad Manager --> Creatives` lists the creatives with their type, size, advertiser,
destination URL and — depending on the creative — the uploaded asset or the code snippet. A preview
link opens the creative as Google renders it.

A creative is shown for a line item through a **creative association**
(:menuselection:`Ad Manager --> Creatives --> Creative Associations`), which links one creative to
one line item for a given period and set of sizes.

.. seealso::
   `Google Ad Manager help <https://support.google.com/admanager>`_

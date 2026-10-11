=====================================
Offline conversions and audiences
=====================================

Many sales are completed after the click: a bank transfer paid three days later, an order confirmed
by a salesperson, a quote that becomes a deal. The app uploads these results to Google Ads, with the
**Data Manager API**, and feeds **Customer Match** lists with your customers. Both require the
:doc:`Google connection <connection>` and the Google Ads account.

Go to :menuselection:`Google --> Configuration --> Settings`. These settings are in the
:guilabel:`Google Ads Offline Conversions` block, which requires eCommerce (for purchases and
audiences) and CRM (for leads).

.. _google/offline/account:

Google Ads account
==================

In the :guilabel:`Google Ads Account` setting (administrators only):

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Customer ID`
     - The 10-digit Google Ads account that receives the conversions and the audiences, like
       `123-456-7890`.
   * - :guilabel:`Manager Account ID`
     - The manager account (MCC) through which the connected Google user accesses the account.
       Leave empty if the user has direct access.
   * - :guilabel:`Validation Mode`
     - Sends the conversions and the audience members with the "validate only" option: Google checks
       the requests and records nothing. Use it for the first tests.

.. _google/offline/purchases:

Offline purchase conversions
============================

With :guilabel:`Offline Purchase Conversions`, the website orders that carry a **Google click
identifier** (`gclid`, `gbraid`, `wbraid`) or customer data are uploaded to the Google Ads conversion
actions that you marked. The click identifiers are stored on the order when the visitor arrives from a
Google ad (with marketing consent).

#. In Google Ads, create a conversion action of type **Import > Track conversions from clicks**
   (or use the conversion action of the website itself to complete its conversions). Copy its
   numeric ID: it is the `ctId` in the address of the conversion action.
#. Open the :ref:`conversion action <google/ads/conversion-actions>` of the *Purchase* event
   (:menuselection:`Google --> Configuration --> Conversion Actions`), enable :guilabel:`Upload
   Offline`, and paste the number in :guilabel:`Conversion Action ID`. These two fields only appear on
   the lines of the :guilabel:`Purchase` event.
#. In the settings, enable :guilabel:`Offline Purchase Conversions`.

With :guilabel:`Restate Refunded Orders` (enabled by default), when a credit note of an uploaded
order is posted, Odoo sends the remaining value of the order: Google Ads replaces the conversion value
(conversion adjustment). Click :guilabel:`Conversion Actions` to open the list.

The conversion is queued as a :doc:`server event </applications/websites/website/tracking/server_events>`,
and Google accepts clicks of the last 90 days: the identifiers are kept in Odoo for the same time
(see :ref:`tracking/consent/retention`).

.. _google/offline/customer-match:

Customer Match audiences
========================

*Customer Match* lets you show ads to your own customers or to look-alike audiences. Enable
:guilabel:`Customer Match` in the settings, then click :guilabel:`Audiences` (or go to
:menuselection:`Google --> Configuration --> Customer Match Audiences`).

.. warning::
   Only customers who **agreed to receive marketing and personalized advertising** may be part of a
   Customer Match audience (Google's Customer Match policy and the EU user consent policy).
   Keep the filter limited to them, for example the contacts subscribed to a mailing list that are
   not blacklisted.

#. In the Google Ads audience manager (*Tools > Shared library > Audience manager*), create a
   **customer list** with the option *Upload emails, phones and/or mailing addresses*, and copy its ID.
#. In Odoo, create an audience:

   .. list-table::
      :header-rows: 1
      :widths: 30 70

      * - Field
        - Description
      * - :guilabel:`Name`
        - For example `Newsletter subscribers`.
      * - :guilabel:`User List ID`
        - The ID of the customer list in Google Ads.
      * - :guilabel:`Customers Consented`
        - You confirm that the customers of the audience agreed. Required: the
          :guilabel:`Synchronise Now` button is hidden without it.
      * - :guilabel:`Customers`
        - The filter on the contacts to send.

#. Click :guilabel:`Synchronise Now`, or wait for the daily scheduled action.

The members are sent with hashed identifiers (email, phone, address). Every day, the contacts that
entered the filter are added, the ones whose data changed are updated, and the ones that left (or were
deleted) are removed. After a synchronization, :guilabel:`Members` shows the number of customers
sent, and the :guilabel:`State` is :guilabel:`Synchronised` or :guilabel:`Error` (with the reason in
:guilabel:`Last Error`).

.. screenshot:: google-customer-match-audience
   :menu: Google ‣ Configuration ‣ Customer Match Audiences ‣ (an audience)
   :shows: A Customer Match audience form with the consent warning at the top, the user list ID, the
      Customers Consented checkbox ticked, the customers domain filter, and the synchronization
      group (members, last synchronization).
   :highlight: The Customers Consented checkbox (red frame).
   :data: Audience "Newsletter subscribers", filter on contacts subscribed to a mailing list.
   :notes: English UI, light theme, 1440px width.

.. seealso::
   - :doc:`lead_forms`
   - :doc:`/applications/websites/website/tracking/privacy`

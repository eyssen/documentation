==========
Google Ads
==========

The Google app reports the actions of the website to Google Ads as **conversions**, so that your
campaigns optimize for sales and leads, and sends the products viewed and bought for **dynamic
remarketing**. Conversions are sent by the Google tag when the visitor accepted the marketing cookies.

.. note::
   Google Ads conversions need the :ref:`Google tag <google/tags/google-tag>`: the setting displays a
   reminder if it is disabled.

Enable Google Ads conversions
=============================

Go to :menuselection:`Google --> Configuration --> Settings`. In the :guilabel:`Google Ads` block,
enable :guilabel:`Google Ads Conversions` and enter the :guilabel:`Conversion ID` of your account,
like `AW-123456789` (*Goals > Conversions > Settings* in Google Ads, in the tag setup).

.. screenshot:: google-settings-ads
   :menu: Google ‣ Configuration ‣ Settings
   :shows: The Google Ads block of the Google settings: Google Ads Conversions enabled with the
      Conversion ID and the Conversion Actions link, then Enhanced Conversions, Dynamic Remarketing,
      New Customers, and Conversions with Cart Data.
   :highlight: The whole Google Ads block (red frame).
   :data: Conversion ID "AW-123456789" (throw-away).
   :notes: English UI, light theme, 1440px width, crop to the Google Ads block.

.. _google/ads/conversion-actions:

Conversion actions
==================

A conversion action ties an event of the website to a conversion action of Google Ads. In Google
Ads, create the action under *Goals > Conversions > New conversion action*, choose **Website**, and
set it up **manually** with the Google tag. Copy its **conversion label**: it is the part after the
slash in the `send_to` value of the event snippet (`AW-123456789/AbC-D_efG-h12_34-567`).

In Odoo, click :guilabel:`Conversion Actions` (or go to :menuselection:`Google --> Configuration -->
Conversion Actions`) and create a line:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Field
     - Description
   * - :guilabel:`Name`
     - A label, for example `Online purchase`.
   * - :guilabel:`Website`
     - With several websites.
   * - :guilabel:`Event`
     - The event that triggers the conversion: a site event such as :guilabel:`Purchase`,
       :guilabel:`Lead`, :guilabel:`Sign up`, :guilabel:`Add to cart`, :guilabel:`Begin checkout`,
       :guilabel:`Contact`, or :guilabel:`Newsletter subscription`, or a CRM stage event such as
       :guilabel:`Qualified lead` or :guilabel:`Won lead (converted)`.
   * - :guilabel:`Conversion Label`
     - The label copied from Google Ads.
   * - :guilabel:`Send Value`
     - Sends the value and the currency of the event with the conversion. Enabled by default.
   * - :guilabel:`Upload Offline`, :guilabel:`Conversion Action ID`
     - For purchases, see :doc:`offline_conversions`.

The conversion value of a purchase follows the :ref:`eCommerce tracking settings
<ecommerce/tracking>` (untaxed amount or total, excluded lines). The lead value is set in the
:doc:`CRM lead tracking </applications/sales/crm/optimize/lead_tracking>`.

Enhanced conversions
====================

Enable :guilabel:`Enhanced Conversions` to improve the matching of the conversions with Google
accounts. For customers known at the time of the event (logged-in customers and the customer of the
order confirmation page), the email address, phone number, name, and address are **hashed with
SHA-256** and sent with the conversion, and added to the Google Tag Manager data layer. It only
happens when the visitor accepted the **marketing** cookies. Enable *Enhanced conversions for web*
in Google Ads as well.

Dynamic remarketing
===================

With :guilabel:`Dynamic Remarketing`, the products viewed, added to the cart, and purchased are
sent to Google Ads (retail vertical) to build remarketing lists and ads with the products the
visitor looked at. The product identifier of the events must be the one of your product feed: see
:ref:`ecommerce/tracking/identifier`.

Conversions with cart data
==========================

Enable :guilabel:`Conversions with Cart Data` to send the purchased items with the purchase
conversion, so that Google Ads can report the product-level performance and the cost of goods.
Fill in:

- :guilabel:`Merchant Center ID`: the number of your Merchant Center account.
- :guilabel:`Feed Country` and :guilabel:`Feed Language`: the country (for example `ES`) and the
  language (for example `es`) of the product feed registered in Merchant Center.

The items sent use the same identifier as your Merchant Center feed.

New customers
=============

Enable :guilabel:`New Customers` to tell Google Ads whether a purchase is the **first one of the
customer**: the *customer acquisition* goals of Google Ads can then give more value to new customers.
An order is the first one when the same customer (the commercial contact) has no earlier confirmed order, whatever the sales channel.

.. seealso::
   - :doc:`consent_mode`
   - :doc:`offline_conversions`
   - :doc:`/applications/websites/website/tracking/privacy`

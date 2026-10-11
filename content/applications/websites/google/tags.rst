=====================
Tags and Analytics
=====================

The Google app loads the Google tag (`gtag.js`, for Google Analytics 4 and Google Ads), Google Tag
Manager, or both, only after the :doc:`visitor's consent
</applications/websites/website/tracking/cookie_consent>`, with the :doc:`Consent Mode <consent_mode>`
signals already set.

Go to :menuselection:`Google --> Configuration --> Settings`. Select the website in the
:guilabel:`Settings of Website` field first if you have several websites.

.. note::
   When the Google app is installed, the :guilabel:`Google Analytics` setting of the Website settings
   only contains a :guilabel:`Google Settings` button that opens this page. The :guilabel:`Measurement
   ID` that you entered there is kept.

.. _google/tags/google-tag:

Google tag (Google Analytics 4)
===============================

In the :guilabel:`Tags` block, enable :guilabel:`Google Tag (GA4)` and fill in:

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Field
     - Description
   * - :guilabel:`Measurement ID`
     - The ID of your GA4 web stream, like `G-XXXXXXXXXX` (*Admin > Data streams* in Google
       Analytics).
   * - :guilabel:`Additional Tag IDs`
     - Other destinations of the Google tag, separated by commas: `G-…`, `GT-…`, `DC-…`
       (for example a second GA4 property or a Floodlight tag). The IDs are checked when you save.
   * - :guilabel:`Google Tag Server URL`
     - Optional. To serve `gtag.js` from your own domain (Google tag gateway) or a server-side
       container, enter its address, for example `https://www.example.com/metrics`. The script is
       loaded from `{URL}/gtag/js`. Leave empty to use Google's servers.

.. screenshot:: google-settings-tags
   :menu: Google ‣ Configuration ‣ Settings
   :shows: The Tags block of the Google settings: the Google Tag (GA4) setting enabled with the
      Measurement ID, Additional Tag IDs, and Google Tag Server URL fields, and below it the
      Google Tag Manager setting.
   :highlight: The Google Tag (GA4) setting (red frame).
   :data: Demo website, Measurement ID "G-ABCDE12345" (throw-away).
   :notes: English UI, light theme, 1440px width, crop to the Tags block.

The Google tag also carries the :doc:`Google Ads <ads>` conversions: with the Google tag disabled,
the Google Ads conversions are not sent.

Page views, e-commerce events (product views, cart, checkout, purchase), and lead events are sent
to every GA4 destination automatically, in the GA4 recommended event format.

.. important::
   The GA4 events carry the consent signals of the visitor. If analytics is refused, Google receives
   cookieless pings in *Advanced* mode and nothing in *Basic* mode. See :doc:`consent_mode`.

.. _google/tags/gtm:

Google Tag Manager
==================

Google Tag Manager (GTM) lets you manage your own tags in a container. The app inserts the
container on every page and pushes the website events to its **data layer**, in the format of GA4
e-commerce, so you do not need to edit the code of the website.

Enable :guilabel:`Google Tag Manager (GTM)` in the :guilabel:`Tags` block and fill in:

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Field
     - Description
   * - :guilabel:`Container ID`
     - Required: the ID of the container, like `GTM-ABC1234`.
   * - :guilabel:`Server URL`
     - Optional: the address of a server-side GTM container or of a tag gateway path, for example
       `https://sgtm.example.com`. Leave empty to use `www.googletagmanager.com`.
   * - :guilabel:`Environment Auth` and :guilabel:`Environment Preview`
     - Optional: the `gtm_auth` and `gtm_preview` values of a GTM environment (for example `env-5`),
       to load a draft environment on this website.

The data layer receives, with an `event_id` for deduplication: `view_item`, `view_item_list`,
`add_to_cart`, `remove_from_cart`, `view_cart`, `add_to_wishlist`, `begin_checkout`,
`add_shipping_info`, `add_payment_info`, `purchase`, and `refund` (with an `ecommerce` object), and
the other events (`generate_lead`, `sign_up`, `login`, `search`, `contact`, `subscribe`) with their
parameters at the top level. The page view is left to the own trigger of GTM. If
:guilabel:`Enhanced Conversions` are enabled, a `user_data` object with hashed customer data is added
when the visitor accepted marketing cookies.

.. note::
   If purchases are :ref:`sent from the server <google/mp/purchases>`, the `purchase` event of the
   data layer is flagged `ga4_sent_by_server: true`. Exclude it in the trigger of your GA4 event tag
   (condition *ga4_sent_by_server does not equal true*) to avoid counting it twice; the Google Ads
   tags can still use it.

.. tip::
   You can use the Google tag and Google Tag Manager together, but do not send the same event
   to GA4 from both. A common choice is to keep GA4 in the Google tag and to use GTM for the other
   marketing tags.

.. _google/tags/analytics-options:

Google Analytics options
========================

In the :guilabel:`Google Analytics` block of the settings:

- :guilabel:`GA4 User ID`: sends a pseudonymous user ID (a **keyed hash** of the customer, never the
  email address) for logged-in customers, so that GA4 can join the visits of the same customer on
  several devices. Enable *Google signals* in GA4 to use it.
- :guilabel:`GA4 Debug Mode`: shows the events of the website in the GA4 *DebugView*. See
  :doc:`/applications/websites/website/tracking/troubleshooting`. Disable it in production.

.. seealso::
   - :doc:`consent_mode`
   - :doc:`/applications/websites/website/reporting/analytics`

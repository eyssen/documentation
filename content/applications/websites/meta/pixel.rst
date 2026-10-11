==========
Meta Pixel
==========

The **Meta Pixel** measures what your visitors do on the website (page views, product views,
searches, carts, checkouts, purchases, leads) in Meta Ads Manager. It lets you build audiences,
optimize campaigns for conversions, and measure their results.

The pixel is loaded only when the visitor accepts the **marketing** cookies. See :doc:`/applications/websites/website/tracking/cookie_consent`.

Set up the pixel
================

Go to :menuselection:`Meta --> Configuration --> Settings`. Select the website at the top, then, in
the :guilabel:`Meta Pixel` block, enable :guilabel:`Meta Pixel` and fill in:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Pixel ID`
     - The main pixel (dataset) ID, shown in Meta Events Manager. It only contains digits.
   * - :guilabel:`Additional Pixel IDs`
     - Other pixels that receive the same events, separated by commas.

.. screenshot:: meta-settings-pixel
   :menu: Meta ‣ Configuration ‣ Settings
   :shows: The Meta Pixel block of the Meta settings with the Meta Pixel setting enabled: the Pixel
      ID and Additional Pixel IDs fields, then the Load Before Consent, Advanced Matching, Custom
      Events, and Domain Verification settings.
   :highlight: The Meta Pixel setting and the Pixel ID field (red frame).
   :data: Pixel ID "1234567890123456".
   :notes: English UI, light theme, 1440px width, crop to the block.

Each website has its own settings. The pixel is only loaded on the pages of the website, outside the
backend, and never for the visitors who refuse the marketing cookies.

Options
=======

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Setting
     - Description
   * - :guilabel:`Load Before Consent`
     - Loads the pixel when the page opens, **with its consent revoked**: Meta receives no event
       until the visitor grants the marketing consent, and the events of the page are then sent.
       Enable it only if your legal basis allows loading the Meta script before consent, because
       the visitor's browser contacts Meta at once.
   * - :guilabel:`Advanced Matching`
     - Sends the **hashed** email, phone, name, and address of the logged-in customer, or of the
       customer of the order on the confirmation page, with the pixel events, to improve the
       matching with Meta accounts. The data is hashed with SHA-256 in Odoo before it leaves the
       server.
   * - :guilabel:`Custom Events`
     - Also sends the events that Meta has no standard event for, as custom events: *ViewCart*,
       *RemoveFromCart*, *ViewItemList*, *AddShippingInfo*, and *Login*.
   * - :guilabel:`Domain Verification`
     - Adds the verification meta tag of your Meta Business Manager to the pages. Paste the content
       of the `facebook-domain-verification` tag in the :guilabel:`Verification Code` field.

.. _meta/pixel/events:

Events sent
===========

The events of the website are translated to the standard Meta events:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Visitor action
     - Meta event
   * - Page view
     - *PageView*
   * - Product view
     - *ViewContent*
   * - Search
     - *Search*
   * - Add to cart
     - *AddToCart*
   * - Add to wishlist
     - *AddToWishlist*
   * - Begin checkout
     - *InitiateCheckout*
   * - Payment information
     - *AddPaymentInfo*
   * - Order confirmed
     - *Purchase*
   * - Form submission (lead)
     - *Lead*
   * - Sign up
     - *CompleteRegistration*
   * - Contact request
     - *Contact*
   * - Newsletter subscription
     - *Subscribe*

The product events carry the product IDs, the quantities, the prices, and the currency. The product
IDs are the same as the ones of the :doc:`product catalog </applications/websites/meta/catalog>`, so
that Meta can link the events to the catalog items (dynamic ads). The eCommerce events come from the
:doc:`eCommerce tracking </applications/websites/ecommerce/tracking>`.

Every event has a unique ID. When the :doc:`Conversions API <conversions_api>` sends the same event
from the server, Meta uses this ID to count it once.

.. tip::
   Check the events with the **Meta Pixel Helper** browser extension, or in the *Test events* tab of
   Events Manager. See :ref:`meta/capi/test` and :doc:`/applications/websites/website/tracking/troubleshooting`.

.. seealso::
   - :doc:`conversions_api`
   - :doc:`/applications/websites/website/tracking/cookie_consent`
   - :doc:`/applications/websites/website/tracking/privacy`

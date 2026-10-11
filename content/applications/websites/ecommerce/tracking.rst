.. _ecommerce/tracking:

==================
eCommerce tracking
==================

When the Google app or the Meta app is installed, the eCommerce store reports what happens in the
shop to the advertising and analytics platforms: which products are viewed, added to the cart, bought
or refunded. These events feed the e-commerce reports of Google Analytics 4, the conversions of
Google Ads, the dynamic remarketing audiences, and the Meta pixel and Conversions API.

Everything respects the :doc:`cookie consent </applications/websites/website/tracking/cookie_consent>`
of the visitor. Nothing is sent for a visitor who refused the cookies of the corresponding category.

Events
======

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Event
     - When it is sent
   * - Product list and search
     - A visitor opens a category page of the shop, or searches for products.
   * - Product view
     - A visitor opens a product page.
   * - Add to cart, remove from cart
     - A visitor changes the cart.
   * - Wishlist
     - A visitor adds a product to the wishlist.
   * - View cart
     - A visitor opens the cart page.
   * - Begin checkout, shipping and payment information
     - A visitor goes through the steps of the checkout.
   * - Purchase
     - An order is placed or confirmed (see :ref:`ecommerce/tracking/purchase`). It is sent by the
       browser **and** by the server with the same event ID, so the platforms count it once.
   * - Refund
     - A credit note of an eCommerce order is posted. It is sent from the server to Google Analytics 4
       (see :doc:`/applications/websites/google/measurement_protocol`).

The products of the events carry their identifier, name, brand, category, variant, price, quantity, and
discount.

.. _ecommerce/tracking/settings:

eCommerce Tracking settings
===========================

Go to :menuselection:`Website --> Configuration --> Settings` and scroll down to the :guilabel:`Tracking`
block. The :guilabel:`eCommerce Tracking` setting contains:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Product Identifier`
     - The identifier of the products in the events **and** in the :doc:`product feeds
       <product_feeds>`. See :ref:`ecommerce/tracking/identifier`.
   * - :guilabel:`Conversion Value`
     - The value reported for a purchase: the :guilabel:`Untaxed amount` (default) or the
       :guilabel:`Total amount (taxes included)`.
   * - :guilabel:`Report Purchases`
     - When the purchase is reported. See :ref:`ecommerce/tracking/purchase`.
   * - :guilabel:`Exclude Shipping Lines`
     - Enabled by default. The delivery lines are not sent as purchased items. The shipping amount
       is sent separately.
   * - :guilabel:`Exclude Discount Lines`
     - Enabled by default. The discount and gift card lines are not sent as purchased items.

.. screenshot:: ecommerce-tracking-settings
   :menu: Website ‣ Configuration ‣ Settings
   :shows: The Tracking block of the Website settings with the eCommerce Tracking setting: the
      Product Identifier, Conversion Value, and Report Purchases fields, and the Exclude Shipping
      Lines and Exclude Discount Lines checkboxes.
   :highlight: The eCommerce Tracking setting (red frame).
   :data: Default values.
   :notes: English UI, light theme, 1440px width, crop to the block.

.. note::
   These settings apply to one website. Select the website in the :guilabel:`Settings of Website`
   field at the top of the page.

.. _ecommerce/tracking/identifier:

Product identifier
------------------

Dynamic remarketing (Google) and catalog ads (Meta) work only if the product IDs of the events are
**identical** to the IDs of the product feed. Both use the same setting, so they always match as long
as you do not change it by hand in a feed column. Choose:

- :guilabel:`Product variant ID`: the technical ID of the variant (default). Always unique.
- :guilabel:`Internal reference (variant ID when empty)`: the internal reference of the variant,
  or its ID when it has none. Use it if the platform already knows your references.
- :guilabel:`Product template ID`: one identifier per product, whatever the variant. Use it with
  the feeds at product level.

.. warning::
   If you change the identifier, update the product feeds in Merchant Center and in the Meta catalog.
   The products registered with the previous identifiers are not matched anymore.

.. _ecommerce/tracking/purchase:

When is a purchase reported?
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Value
     - Behavior
   * - :guilabel:`When the order is placed`
     - As soon as the customer reaches the confirmation page, even if the payment is pending (for
       example a wire transfer). Choose it if you want to measure all the orders, including those
       paid later.
   * - :guilabel:`When the order is confirmed`
     - Once the payment is received or the order is confirmed manually. Choose it if you only want to
       report the real sales.

Each order is reported **once**, whatever the number of times the customer reloads the page. The
click identifiers (Google Ads, Meta) and the consent of the visitor are stored on the order at the
time of the visit, so the later server events and the :doc:`offline conversions
</applications/websites/google/offline_conversions>` can use them.

.. tip::
   In developer mode, the :guilabel:`Ad Tracking` section of the :guilabel:`Other Info` tab of the
   order shows the stored identifiers (GCLID, GBRAID, WBRAID, GA client ID, Meta browser and click
   IDs), the consent, and whether the purchase was already sent.

.. seealso::
   - :doc:`product_feeds`
   - :doc:`/applications/websites/google/ads`
   - :doc:`/applications/websites/meta/pixel`
   - :doc:`/applications/websites/website/tracking/troubleshooting`

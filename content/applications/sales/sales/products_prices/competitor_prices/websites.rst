=============================
Competitor websites and fetch
=============================

A **competitor website** is one shop whose prices you follow. It holds the rules of how politely and
how often its pages are read. Go to :menuselection:`Competitor Prices --> Configuration --> Competitor
Websites` and click :guilabel:`New`.

The website form
================

:guilabel:`Website`
   - :guilabel:`Website`: the address of the shop, for example ``https://www.example.com``.
   - :guilabel:`Other Domains`: further domains of the same shop (``example.de, example-shop.com``).
     A product address on one of them belongs to this website.
   - :guilabel:`Partner`, :guilabel:`Country` and :guilabel:`Platform` (Shopify, WooCommerce,
     PrestaShop, Magento, Shoprenter, UNAS, Shopware, Odoo or other) describe the shop.

:guilabel:`Prices`
   - :guilabel:`Currency`: the currency of the shop, with several currencies.
   - :guilabel:`Number Format`: how the shop writes numbers. :guilabel:`Automatic` works for most
     shops; set a decimal comma or point when a price such as 1.299 is read wrongly.
   - :guilabel:`Prices Include Tax`: tick it for consumer shops that show gross prices. The prices are
     converted to net with the taxes of your own product before they are compared.
   - :guilabel:`Key Competitor`: the :guilabel:`Lowest of the key competitors` pricing strategy looks
     only at these websites.

The :guilabel:`Listings` button lists the product addresses of the website.

.. screenshot:: sales-competitor-prices-website-form
   :menu: Competitor Prices ‣ Configuration ‣ Competitor Websites ‣ (a website)
   :shows: A competitor website form with the Website and Prices groups, the "Terms of Use Reviewed" and
      "Fetch Prices Now" buttons in the header and the Fetching tab open.
   :highlight: The "Terms of Use Reviewed" button and the Fetching tab (red frames).
   :data: Demo website "Example Shop" with 120 listings, 2 of them broken.
   :notes: English UI, light theme, 1440px width.

Terms of use review
-------------------

A new website is fetched only after a manager has read its terms of use and pressed :guilabel:`Terms
of Use Reviewed`. The form then shows who confirmed it and when (:guilabel:`Terms of Use` tab), where
you can note where the terms are and what they say about automated access. The review is required
unless :guilabel:`Require Terms of Use Review` is switched off in the settings. In the website list,
websites without a review are highlighted; the :guilabel:`Terms Not Reviewed` filter shows them.

How the prices are fetched
==========================

The :guilabel:`Fetching` tab sets the pace:

- :guilabel:`Fetching Active` switches the website on or off. A website with fetching off keeps its
  history but is not read.
- :guilabel:`Refresh Prices Every`: how often the price of a product is read again, in hours or days.
- :guilabel:`At Most … pages per … minutes`: the request limit of the website.
- :guilabel:`Min. Seconds Between Requests`: the minimum time between two pages. A longer *Crawl-delay* in the
  website's *robots.txt* wins.
- :guilabel:`Respect robots.txt`: pages that *robots.txt* disallows are not read.
- :guilabel:`User Agent`: leave empty to use the one from the settings.

A scheduled job (*Competitor Prices: fetch due prices*, every 5 minutes) reads the prices that are
due, within these limits. Only public product pages are read, and a website that is being read is
never read in parallel.

.. important::
   The app never tries to get around a block. When a website answers with a block, a *Too many
   requests* error or a bot-protection page (a CAPTCHA or a challenge), fetching of that website
   pauses and the form shows *Fetching is paused until …* with the reason. Click
   :guilabel:`Resume Fetching` to end the pause early, only when you know the reason is gone. If a
   website keeps blocking you, switch its fetching off and ask the shop's owner for permission, or
   get its prices from another source (for example the :doc:`Priceva import <priceva_import>`).

:guilabel:`Fetch Prices Now` on the form reads the due prices of the website at once, still within
its limits. The :guilabel:`Fetch Log` (:menuselection:`Competitor Prices --> Configuration --> Fetch
Log`) lists every run with its start, duration, trigger (scheduled or manual) and the number of
changed, unchanged, suspicious, failed and skipped prices.

How a price is read
===================

The app reads a product page in this order and stops at the first source that gives a price:

#. The **structured product data** of the page (JSON-LD or microdata) and its meta tags.
#. The **extraction rule** of the listing or of the website, for pages without usable structured data.

The :guilabel:`Extraction Rule` tab of the website holds a rule that applies to all its listings. It
is a short text in JSON: for each field (``price``, ``regular_price``, ``currency``,
``availability``, ``shipping``, ``gtin``, ``mpn``, ``sku``, ``title``) an ``xpath`` or ``css``
selector, and optionally ``attr`` (read an attribute), ``regex``, ``map`` (translate a text to a
value) or ``fixed`` (a constant). For example:

.. code-block:: json

   {"price": {"css": "span.price"}, "currency": {"fixed": "EUR"}}

:guilabel:`Site Rule State` shows whether the rule is :guilabel:`None`, :guilabel:`Proposed`,
:guilabel:`Validated` or :guilabel:`Broken`; :guilabel:`Site Rule Validated On` tells when it last worked.

:guilabel:`Use the Rule First`
   For shops whose structured data holds a coupon, member or other conditional price instead of the
   shelf price, tick this: the rule is then read *before* the structured data.

A single listing can have its own rule (see :doc:`products`).

Finding products
================

The :guilabel:`Finding Products` tab holds the :guilabel:`Search URL` of the shop, for
example ``https://www.example.com/search?q={query}``, and its :guilabel:`Sitemap URL`. They are used
when the AI looks for your products on the website (see
:doc:`/applications/productivity/ai/competitor_prices`).

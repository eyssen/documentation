:nosearch:

=================
Competitor prices
=================

Know what your competitors charge, keep the history, and get a sales price recommendation that never
goes below your cost and margin. The **Competitor Prices** app reads the public prices of your
products from the websites of your competitors, stores every price change, and compares them with
your own sales prices.

.. note::
   The app only *recommends* prices. A sales price changes only when a manager presses
   :guilabel:`Accept` on a recommendation; nothing changes by itself.

What you can do
===============

- Follow the prices of a product on any number of competitor websites, each with its own refresh
  interval and request limit (see :doc:`competitor_prices/websites`).
- Keep an append-only price history, with a suspicious-change check that holds back a price that
  jumped by too much (see :doc:`competitor_prices/products`).
- Define pricing rules and receive sales price recommendations that respect the cost, the fees and
  the minimum margin, optionally on the :ref:`expected purchase cost
  <inventory/supplier-products/expected-cost>` (see :doc:`competitor_prices/recommendations`).
- See where you stand on a product or a category, and which competitor prices changed (see
  :doc:`competitor_prices/reports`).
- Load the product addresses and the price history from a Priceva export (see
  :doc:`competitor_prices/priceva_import`).
- Let the AI find your products on the competitor websites, build the extraction rules and repair
  them when a website changes (see :doc:`/applications/productivity/ai/competitor_prices`).

.. _sales/competitor-prices/modules:

Modules
=======

The functions are split into four modules; install the ones you need.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Module
     - What it adds
   * - *Competitor Prices*
     - The app: websites, listings, price history, recommendations, pricing rules, reports.
   * - *Competitor Prices - Expected Purchase Cost*
     - Lets a pricing rule use the expected purchase cost of the vendor pricelist instead of the
       product cost. Requires *Supplier Product Management*.
   * - *AI for Competitor Prices*
     - Website analysis, product finding, AI-built extraction rules and automatic repair. Requires
       the *AI* application.
   * - *Competitor Prices - Priceva Import*
     - Import of Priceva Excel reports.

Lawful use
==========

The app reads prices from other companies' websites. That can be lawful, but only when it is done
with care. The same rules are shown at the top of :menuselection:`Competitor Prices --> Configuration
--> Settings`, in the :guilabel:`Lawful Use` section.

- **Terms of use.** Read the terms of use of a website before you add it. Under EU case law (CJEU
  C-30/14, *Ryanair v PR Aviation*) a website may forbid the automated reading of its data by
  contract. If the terms forbid it, do not track that website, or ask the owner for permission.
- **Public prices only.** Read only pages anyone can see without signing in. Never get around
  CAPTCHAs, bot protection, IP blocks or paywalls. The app stops by itself when a website blocks it
  and does not try again until the pause is over.
- **Be gentle.** Keep *robots.txt* respected, the refresh interval long and the request limit low.
  Use an honest user agent: it needs no contact address, but it must not pose as a web browser.
- **Only what you need.** Store prices, availability and product identifiers. Do not copy product
  descriptions, photos, reviews or large parts of a catalogue (copyright, database rights), and do
  not collect personal data such as reviewer names (GDPR).
- **Set your prices independently.** Watching public prices is allowed. Agreeing on prices with
  competitors, or using price data to coordinate with them, is forbidden by competition law
  (Article 101 TFEU).
- **Price reductions.** When you announce a price reduction, show your own lowest price of the
  previous 30 days as the earlier price (EU Omnibus Directive, Article 6a). Every recommendation
  shows that price.

.. warning::
   The app is a tool and not legal advice. The rules differ by country and by website; every company
   and user that runs it is responsible for using it lawfully. When in doubt, ask a lawyer first.

Access rights
=============

Two groups are listed under :guilabel:`Competitor Prices` on the user form:

- :guilabel:`User` sees the competitor prices, adds and confirms listings and fetches prices.
- :guilabel:`Manager` also sets up the competitor websites and the pricing rules, and accepts or
  rejects price recommendations. Only an administrator opens the app settings.

The administrator and the root user are managers when the app is installed. The records belong to a
company: with several companies, each company sees its own websites, listings and recommendations.

Settings
========

Go to :menuselection:`Competitor Prices --> Configuration --> Settings`.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Setting
     - Meaning
   * - :guilabel:`Require Terms of Use Review`
     - A website is fetched only after someone confirmed on its form that its terms of use were
       reviewed. On by default.
   * - :guilabel:`User Agent`
     - How the price reader introduces itself. The default is ``PriceCheck/1.0``.
   * - :guilabel:`Refresh Prices Every`
     - Default interval, in hours, for new websites (24 by default).
   * - :guilabel:`Request Limit`
     - Default number of pages per number of minutes for new websites (120 pages per 60 minutes).
   * - :guilabel:`Pause Between Requests`
     - Default minimum time, in seconds, between two pages of one website (10). A longer
       *Crawl-delay* in *robots.txt* wins.
   * - :guilabel:`Suspicious Price Change`
     - A competitor price that moves by more than this percentage (40 by default) is held back; 0
       switches the check off.
   * - :guilabel:`Broken Listing`
     - A listing is marked broken after this many failed reads in a row (3).

The defaults are copied to a website when it is created; change them per website on its form.

.. screenshot:: sales-competitor-prices-settings
   :menu: Competitor Prices ‣ Configuration ‣ Settings
   :shows: The Competitor Prices settings page: the "Lawful Use" warning box with the six rules and the
      "Require Terms of Use Review" and "User Agent" settings, then "Defaults for New Websites" and
      "Data Quality".
   :highlight: The "Lawful Use" block (red frame).
   :data: Default values.
   :notes: English UI, light theme, 1440px width, crop to the first two blocks.

.. toctree::
   :titlesonly:

   competitor_prices/websites
   competitor_prices/products
   competitor_prices/recommendations
   competitor_prices/reports
   competitor_prices/priceva_import

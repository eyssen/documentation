========================
AI for competitor prices
========================

The *AI for Competitor Prices* module adds the AI to the :doc:`Competitor Prices
</applications/sales/sales/products_prices/competitor_prices>` app. The AI does the slow parts of
setting up price tracking:

- it **analyses a competitor website**: shop engine, search page, sitemap;
- it **finds your products** on the competitor websites and proposes the matching pages;
- it **builds an extraction rule** for pages whose price cannot be read from the structured data;
- it **repairs a broken listing** by writing a new rule when a website changes;
- optionally, it **reads the price itself** when no rule works.

The AI never sets a price and never confirms a doubtful match: a person confirms every proposed
listing, and sales prices change only when a manager accepts a recommendation.

.. note::
   The module requires the *AI* application with at least one chat model set up (see
   :doc:`models_and_providers`) and the *Competitor Prices* app. The AI calls run with the access
   rights and limits of the user who clicks, or, in the background, of the user chosen in the
   settings.

.. warning::
   To judge a page, the AI provider receives the text of the competitor's product page and the name,
   codes and brand of your product. Every call uses your AI quota. Content of a web page is treated as untrusted data: instructions written in a
   page are not followed.

Settings
========

Go to :menuselection:`Competitor Prices --> Configuration --> Settings`, section :guilabel:`AI`.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Setting
     - Meaning
   * - :guilabel:`AI Models`
     - One model per task. :guilabel:`Rules and finding` writes and repairs extraction rules, picks
       links from search results and finds a shop's search page. :guilabel:`Product matching` decides
       whether a competitor page sells the same product (model, variant, pack size) and reads prices
       when no rule works: use the most careful model here. Empty: the main AI model.
   * - :guilabel:`Scheduled AI Work Runs As`
     - The user whose AI rights and limits are used for the background work (product finding and
       repair). Empty: the AI does no background work.
   * - :guilabel:`Confirm Matches with the Same GTIN`
     - A found page whose GTIN (EAN) equals the barcode of the product is confirmed without review.
       Every other match waits for a person. On by default.
   * - :guilabel:`Repair Broken Listings with AI`
     - When a listing becomes broken, the AI writes a new rule and checks it before use, at most
       :guilabel:`AI Repairs per Website per Day` (5) times per website.
   * - :guilabel:`AI Reads the Price When No Rule Works`
     - Costly: one AI call per page that no rule can read. The price is marked as read by AI
       (method :guilabel:`AI reading`).

.. screenshot:: ai-competitor-prices-settings
   :menu: Competitor Prices ‣ Configuration ‣ Settings
   :shows: The "AI" block of the Competitor Prices settings with the two model fields, the "Scheduled AI
      Work Runs As" user, the GTIN and repair options and the "AI Reads the Price When No Rule Works"
      option.
   :highlight: The "AI Models" setting (red frame).
   :data: A cheap model for rules and finding, a careful model for matching, an AI user selected.
   :notes: English UI, light theme, 1440px width, crop to the AI block.

Analyse a website
=================

On the form of a competitor website click :guilabel:`Analyse Website` (managers). The app reads the
home page and reports in a notification and in the chatter: the shop engine (:guilabel:`Platform`),
the search page, the sitemap listed in *robots.txt*, whether *robots.txt* allows reading, and whether
the home page carries structured product data. The search page and the platform are saved on the
website (:guilabel:`Search URL`, :guilabel:`Finding Products` tab).

The :guilabel:`Finding Products` tab also shows the state of the sitemap (:guilabel:`Sitemap`:
:guilabel:`Not loaded`, :guilabel:`Loading`, :guilabel:`Loaded` or :guilabel:`Not available`), the
:guilabel:`Addresses in Sitemap` and :guilabel:`Sitemap Loaded`. The sitemap is loaded the first
time it is needed and refreshed from time to time. On the :guilabel:`Fetching` tab,
:guilabel:`Render JavaScript With` selects a web provider that draws the page for shops that show
their prices only after a script ran.

Find products on competitor websites
====================================

Select products in the product list (or open one), then choose :menuselection:`Action --> Find on
Competitor Websites`. On the product form the button is also on the :guilabel:`Competitor Prices`
tab.

.. screenshot:: ai-competitor-prices-discovery-wizard
   :menu: Sales ‣ Products ‣ Products ‣ Action ‣ Find on Competitor Websites
   :shows: The Find on Competitor Websites window with the explanation, the products, the competitor
      websites, "Skip Products Already Listed" and "Start Now", and the Find Products button.
   :highlight: The "Skip Products Already Listed" and "Start Now" options (red frame).
   :data: Five selected products, three competitor websites.
   :notes: English UI, light theme, dialog only.

:guilabel:`Products` and :guilabel:`Competitor Websites`
   The products to look up and the websites to search (the websites with fetching on are preselected).

:guilabel:`Skip Products Already Listed`
   Skips a product that already has a listing on the website.

:guilabel:`Start Now`
   Processes as many as the request limits of the websites allow at once (about 40 seconds); the
   scheduled job (*Competitor Prices: find products on competitor websites (AI)*, every 10 minutes)
   finishes the rest.

Click :guilabel:`Find Products`. For each product and website a search task is created. A task looks
for the product with its GTIN (barcode), manufacturer part number, internal reference and name:

#. on the **search page** of the website;
#. if nothing fits, in the website's **sitemap**;
#. if nothing fits, with a **web search engine**, when one is configured in the AI settings and
   allowed.

Candidate pages are downloaded politely, within the limits of the website, and the page's identity is
compared with your product. A page with the **same GTIN** is confirmed at once (if
:guilabel:`Confirm Matches with the Same GTIN` is on). A page with the same manufacturer part number
and brand, or one the AI judges to be the same product (also checking the model, variant and pack
size, which sets :guilabel:`Units per Listing`), is **proposed**: it becomes a listing
:guilabel:`To Review`.

The tasks are in :menuselection:`Competitor Prices --> Listings --> Product Finding`:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Status
     - Meaning
   * - :guilabel:`Waiting`
     - The task is queued or in progress.
   * - :guilabel:`Found (same GTIN)`
     - A listing was created and confirmed.
   * - :guilabel:`Found, to review`
     - A listing was proposed; confirm or reject it in :menuselection:`Competitor Prices --> Listings
       --> To Review`.
   * - :guilabel:`Not found`
     - No matching page; the notes say what was tried.
   * - :guilabel:`Error`
     - For example the website blocks automated access.

The filters :guilabel:`Waiting`, :guilabel:`Found` and :guilabel:`Not Found` narrow the list;
:guilabel:`Retry` (on a not found or failed task) searches again, and the list action :guilabel:`Process
Now` runs the selected tasks at once. If a website blocks the search, its fetching pauses as usual
(see :doc:`/applications/sales/sales/products_prices/competitor_prices/websites`).

.. screenshot:: ai-competitor-prices-product-finding
   :menu: Competitor Prices ‣ Listings ‣ Product Finding
   :shows: The Product Finding list with products, websites, statuses Found (same GTIN), Found, to
      review and Not found, the listing and the notes.
   :highlight: The status column (red frame).
   :data: About 15 tasks with all statuses.
   :notes: English UI, light theme, 1440px width.

Build a rule with AI
====================

For a listing whose price cannot be read from the structured data of the page, click :guilabel:`Build
Rule with AI` on the listing form. The AI:

#. checks whether the page has structured product data (then no rule is needed);
#. checks whether the website's rule already works on the page;
#. otherwise asks the model for a rule, **audits** it (the selector must match, point to a number and
   read the price the page shows), and, when other confirmed pages of the website exist, checks that
   the rule also works there.

A rule that works on several pages is saved as the **website's rule** (:guilabel:`Validated`); otherwise
it is saved as the listing's :guilabel:`Own rule`, with :guilabel:`Rule Source` :guilabel:`AI` and a
note. The price read is recorded at once. A rule that cannot be checked is not saved, and the message
says why. You can read and edit the rule on the website or listing form, and :guilabel:`Test Read`
shows what it reads.

Repair broken listings
======================

When a listing becomes broken and :guilabel:`Repair Broken Listings with AI` is on, the listing is
queued (:guilabel:`AI Repair Queued`). A scheduled job (*Competitor Prices: repair broken listings
(AI)*, hourly) builds and audits a new rule as above and, if it works, confirms the listing again.
A failed repair is noted on the listing (:guilabel:`AI Notes`) and not repeated. The number of repairs
a website had today is shown as :guilabel:`AI Repairs Today` on its :guilabel:`Extraction Rule` tab;
the daily cap keeps the cost and the load on the website in check.

.. tip::
   Start with a few products and one website, check the proposed listings and the rules, and only
   then run large batches.

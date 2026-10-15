=========================================
Competitor listings and the price history
=========================================

A **listing** tells where the price of one of your products is on a competitor website: the product
and the address of the page. One product can have a listing on every competitor website.

Follow a product
================

Open the product form and tick :guilabel:`Track Competitor Prices` among the product options. A
:guilabel:`Competitor Prices` tab appears. Adding a listing ticks the box by itself. Only tracked
products are fetched and get recommendations; clear the box to stop following a product, and its open
recommendations are closed.

.. screenshot:: sales-competitor-prices-product-tab
   :menu: Sales ‣ Products ‣ Products ‣ (a product) ‣ Competitor Prices
   :shows: The Competitor Prices tab of a product: a "New sales price recommendation" box with
      Accept and Reject buttons, the Market block with lowest, median and highest competitor price and the
      price index, the Check Now, Recompute Recommendation and Price History buttons, and the listing
      table.
   :highlight: The recommendation box and the "Check Now" button (red frames).
   :data: A product with listings on three competitor websites and one open recommendation.
   :notes: English UI, light theme, 1440px width, crop to the tab.

The tab shows:

- The **recommendation** box, when a new sales price is recommended (see :doc:`recommendations`).
- The **market**, net and per unit: :guilabel:`Lowest Competitor Price`, :guilabel:`Median
  Competitor Price`, :guilabel:`Highest Competitor Price` and the :guilabel:`Price Index`, which is
  your net price divided by the median competitor price, times 100. Above 100 you are more expensive
  than the middle of the market.
- Three buttons: :guilabel:`Check Now`, :guilabel:`Recompute Recommendation` and :guilabel:`Price
  History`.
- The **listings** of the product and its latest **recommendations**.

Add a listing
=============

In the listing table of the product click :guilabel:`Add a line`, choose the
:guilabel:`Competitor`, paste the :guilabel:`URL` of the product page on that website and save. The
competitor is filled in when the address belongs to a website that is already set up. The listing is
read at once and then according to the website's refresh interval. All listings are also in
:menuselection:`Competitor Prices --> Listings --> All Listings`.

The listing columns are:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Column
     - Meaning
   * - :guilabel:`Units per Listing`
     - How many of your units the competitor sells for the listed price (6 for a six-pack). The
       price is divided by it.
   * - :guilabel:`Status`
     - :guilabel:`To Review`, :guilabel:`Confirmed`, :guilabel:`Broken` or :guilabel:`Rejected`; see
       below.
   * - :guilabel:`Price`, :guilabel:`Currency`, :guilabel:`Regular Price`
     - The current price, its currency and the price before a discount, when the page shows it.
   * - :guilabel:`Availability`
     - :guilabel:`In Stock`, :guilabel:`Out of Stock`, :guilabel:`Pre-order` or :guilabel:`Unknown`.
   * - :guilabel:`Unit Price (net)`
     - The price per unit of your product without tax: divided by the units per listing, and, for a
       website with prices including tax, converted to net.
   * - :guilabel:`Last Successful Fetch`
     - When the price was last read.

With product variants, a listing can be tied to one :guilabel:`Variant`.

Status of a listing
-------------------

:guilabel:`To Review`
   A listing proposed by the AI (see :doc:`/applications/productivity/ai/competitor_prices`) that nobody
   checked yet. It is not fetched and not used in recommendations. Use :guilabel:`Confirm Same
   Product` (check icon) when the page sells the same product, or :guilabel:`Not the Same Product`
   (ban icon) and choose the reason: different product, bundle or multipack, different variant, used
   or refurbished, or other. :menuselection:`Competitor Prices --> Listings --> To Review` lists them.

:guilabel:`Confirmed`
   Fetched on schedule and used in recommendations.

:guilabel:`Broken`
   After the number of failed reads in a row set in the settings (:guilabel:`Broken Listing`, 3 by
   default) the listing is marked broken and the error is shown on the form. It is still tried again.
   Open the listing, correct the address or the rule, and press :guilabel:`Fetch Now`.

:guilabel:`Rejected`
   Not the same product. It is not fetched and not used in recommendations. A rejected listing can be
   confirmed later.

The :guilabel:`Listings` search filters :guilabel:`To Review`, :guilabel:`Confirmed`,
:guilabel:`Broken`, :guilabel:`Rejected`, :guilabel:`Competitor Out of Stock` and :guilabel:`With
Error` find the listings that need attention.

Check now
=========

:guilabel:`Check Now` on the product tab records your current sales price, reads all the listings of the
product immediately (whether or not the product is ticked for tracking), within the request limits of
their websites, and recomputes the recommendation. A message tells how many prices changed. The :guilabel:`Fetch Now` button on a listing does the same for one listing. :guilabel:`Test
Read` on the listing form shows the price, the regular price, the availability and the source the app reads from the page,
without saving anything; use it to try an extraction rule.

The listing form
================

Besides the data above, the form of a listing has these tabs:

:guilabel:`Identity`
   How the page was matched to the product (:guilabel:`Manual`, :guilabel:`Same GTIN`, :guilabel:`Same
   MPN and brand` or :guilabel:`AI judgement`), the confidence, and what the page says: title, brand,
   GTIN, manufacturer part number and SKU. A note tells why the page is or is not the same product.

:guilabel:`Extraction Rule`
   :guilabel:`Website's rule` uses the rule of the website; :guilabel:`Own rule` shows a rule field
   for this page only (same format as the website rule, see :doc:`websites`). The rule is checked when
   you save it.

:guilabel:`Price History`
   The price changes of this listing.

The :guilabel:`Price History` button on the form and on the product opens the same history as a list,
graph and pivot.

Price history
=============

Every price is stored; nothing is overwritten. A new line is added only when the price, the regular
price, the availability or the shipping cost changes; while it stays the same, :guilabel:`Last Seen`
moves forward. Open :menuselection:`Competitor Prices --> Prices --> Price History`:

- :guilabel:`From`, :guilabel:`Last Seen` and :guilabel:`Until` give the period the price was valid;
  :guilabel:`Current` marks the latest line.
- :guilabel:`Unit Price (net)` and :guilabel:`Unit Price (gross)` make the prices of different shops
  comparable; :guilabel:`Change (%)` shows the step from the previous price.
- The :guilabel:`Method` (optional column) tells how the price was obtained: structured data,
  meta tags, extraction rule, AI reading, manual entry, import or own price.
- The filters :guilabel:`Valid Prices`, :guilabel:`Suspicious`, :guilabel:`Current`, :guilabel:`Own
  Prices`, :guilabel:`Competitor Prices` and :guilabel:`Price Changes` narrow the list; group by
  product, competitor or day, and switch to the graph or the pivot view.

.. screenshot:: sales-competitor-prices-history
   :menu: Competitor Prices ‣ Prices ‣ Price History
   :shows: The price history as a line graph, one line per competitor, with the Competitor Prices
      filter on and the product filtered to one product.
   :highlight: The lines of two competitors that differ (red frame).
   :data: One product, three competitors, two months of data.
   :notes: English UI, light theme, 1440px width, graph view.

Suspicious price changes
------------------------

A price that moves by more than :guilabel:`Suspicious Price Change` (40 % by default) is marked
:guilabel:`Suspicious` and left out of the recommendations. This protects you from a misread price,
for example a price of a different pack size, or 12 instead of 1 200. The mark clears by itself when
the next read gives the same value. A manager can also decide on the history line: :guilabel:`Accept`
makes the price valid, :guilabel:`Reject` throws it away.

Your own price and the Omnibus rule
-----------------------------------

The history also records **your own sales price** of tracked products (:guilabel:`Own Prices`
filter): every change of the sales price is stored. This is the source of the lowest price of the
last 30 days that every recommendation shows, for the price reduction rule of the EU Omnibus
Directive (see :doc:`recommendations`).

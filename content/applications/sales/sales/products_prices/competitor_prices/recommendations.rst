===================================
Pricing rules and recommendations
===================================

From the competitor prices, your cost and a **pricing rule**, the app computes a **recommended sales
price**. The rule decides which competitor prices count, how to react to them, and how low or high
the price may go. A manager looks at the recommendation and accepts or rejects it.

.. important::
   A recommendation never changes a price by itself. The sales price (or the pricelist price) is
   written only when a manager presses :guilabel:`Accept`. Computing, recomputing and fetching only
   create recommendations.

.. _sales/competitor-prices/pricing-rules:

Pricing rules
=============

Go to :menuselection:`Competitor Prices --> Configuration --> Pricing Rules`. A rule named *Match the
lowest price, keep 20% margin* is installed. Rules are checked in the order of the list (drag the
handle to reorder); the **first rule that matches a product** is used for it. A product that no rule
matches gets no recommendation.

.. screenshot:: sales-competitor-prices-pricing-rule
   :menu: Competitor Prices ‣ Configuration ‣ Pricing Rules ‣ (a rule)
   :shows: A pricing rule form with the groups Applies To, Competitor Prices Used, Strategy, Never Below
      (Floor), Limits and When Accepted.
   :highlight: The "Never Below (Floor)" group (red frame).
   :data: The installed rule "Match the lowest price, keep 20% margin".
   :notes: English UI, light theme, 1440px width.

:guilabel:`Applies To`
   :guilabel:`Product Categories` (with their subcategories) and :guilabel:`Products`; empty means all.

:guilabel:`Competitor Prices Used`
   - :guilabel:`Competitors`: only these websites; empty means all.
   - :guilabel:`Only Competitors in Stock` (on by default): a competitor that is out of stock is not a
     reference. Prices with unknown availability count.
   - :guilabel:`Max. Price Age (days)` (3): older prices are ignored.
   - :guilabel:`Min. Competitor Prices` (1): with fewer usable prices there is no recommendation (see
     :guilabel:`Raise When No Competitor` below).
   - :guilabel:`Ignore Outliers`: leaves out prices far from the others; it applies with at least four
     prices.
   - :guilabel:`Compare Prices`: :guilabel:`Net (without tax)` or :guilabel:`Gross (with tax)`.
   - :guilabel:`Add Competitor Shipping Cost`: adds the shipping cost the competitor charges to its
     price before comparing.

:guilabel:`Strategy`
   - :guilabel:`Match the lowest price`, :guilabel:`Beat the lowest price` (by a percentage or an
     amount, :guilabel:`Beat By`), :guilabel:`Median of the market`, :guilabel:`Average of the
     market`, or :guilabel:`Lowest of the key competitors` (the websites marked :guilabel:`Key
     Competitor`).
   - :guilabel:`Raise When No Competitor` and :guilabel:`Raise By (%)`: when no usable competitor
     price remains (for example all are out of stock), recommend a higher price.

:guilabel:`Never Below (Floor)`
   The lowest price the rule may recommend. It is computed from the **cost** of the product:

   | floor = (cost + :guilabel:`Extra Cost per Unit`) ÷ (1 − :guilabel:`Fees (% of price)` − :guilabel:`Min. Margin (%)`)

   and never less than cost + extra cost + :guilabel:`Min. Margin per Unit`. The minimum margin is a
   gross margin on the net sales price: (price − cost) ÷ price. Margin and fees together must stay
   below 95 %. The :guilabel:`Cost Basis` is the :guilabel:`Product cost`; with the *Competitor
   Prices - Expected Purchase Cost* module there are two more choices (see below).

:guilabel:`Limits`
   - :guilabel:`Ceiling`: none, a maximum markup on the cost, or a maximum raise on the current price
     (:guilabel:`Ceiling (%)`).
   - :guilabel:`Max. Change per Step (%)` (15): a recommendation moves the price by at most this much;
     0 means no limit. The floor wins over this limit: the app never recommends selling below the
     floor.
   - :guilabel:`Ignore Changes Below (%)` (1): smaller differences are not recommended.
   - :guilabel:`Rounding`: currency precision, whole number, ending in .99 or .90, or a multiple of 5,
     10 or 100.
   - :guilabel:`Do Not Repeat Rejected for (days)` (7): a rejected recommendation is not proposed again
     with the same price for this long.

:guilabel:`When Accepted`
   :guilabel:`Accepting Writes To`: :guilabel:`Sales price of the product`, or :guilabel:`Fixed price
   on a pricelist`, with the :guilabel:`Pricelist` to write to. With the pricelist choice, the sales
   price of the product stays as it is and a fixed-price line for the product is added or updated on
   that pricelist.

Cost from the expected purchase cost
------------------------------------

With the *Competitor Prices - Expected Purchase Cost* module (it needs *Supplier Product Management*)
the :guilabel:`Cost Basis` of a rule has two more choices:

- :guilabel:`Expected purchase cost`: the :ref:`expected cost <inventory/supplier-products/expected-cost>`
  of the preferred vendor pricelist line: price after discount, plus shipping, import duty and EPR
  fee, minus rebate, plus the safety margin, converted to the company currency and to the unit of
  the product.
- :guilabel:`Higher of product cost and expected purchase cost`: the more careful of the two.

A product without a vendor pricelist line falls back to the product cost. The recommendation form
lists the parts of the cost.

Recommendations
===============

A recommendation is created when the competitor prices of a product are fetched, when you press
:guilabel:`Recompute Recommendation` or :guilabel:`Check Now` on the product, and by a daily scheduled
job (*Competitor Prices: recompute price recommendations*). When the situation changes, the open
recommendation of the product is replaced (status :guilabel:`Superseded`); when the product no longer
needs a change it becomes :guilabel:`Outdated`.

Three places show them:

- :menuselection:`Competitor Prices --> Prices --> Price Recommendations`: the new recommendations,
  with :guilabel:`Accept` and :guilabel:`Reject` icons on each line. Filters: :guilabel:`New`,
  :guilabel:`Accepted`, :guilabel:`Rejected`, :guilabel:`Price Decrease`, :guilabel:`Price Increase`
  and :guilabel:`Cannot Match Profitably`; group by reason, category or status.
- :menuselection:`Competitor Prices --> Prices --> Products with New Price`: the products that have
  one. The :guilabel:`New Price Recommendation` filter is also on the product list, with a
  :guilabel:`New price` badge in the kanban view and an optional :guilabel:`Recommended Price`
  column in the list.
- The :guilabel:`Competitor Prices` tab of the product, with the recommendation in a box on top.

.. screenshot:: sales-competitor-prices-recommendation
   :menu: Competitor Prices ‣ Prices ‣ Price Recommendations ‣ (a recommendation)
   :shows: A recommendation form with the explanation text on top, the Price, Market, Cost and Margin and
      Decision groups, and the competitor price lines below.
   :highlight: The explanation text and the "Own Lowest Price, Last 30 Days" field (red frames).
   :data: A product with three competitor prices, a cost breakdown from the expected purchase cost and
      the reason "Competitors are cheaper".
   :notes: English UI, light theme, 1440px width.

The form explains the recommendation in words and shows:

:guilabel:`Price`
   The current and the recommended price, the change in percent, the :guilabel:`Reason`
   (:guilabel:`Competitors are cheaper`, :guilabel:`Room to raise the price`, :guilabel:`Cannot match
   profitably: minimum margin price`, :guilabel:`Limited by the ceiling`, :guilabel:`Limited by the
   max. change per step` or :guilabel:`No competitor available`), and :guilabel:`Own Lowest Price, Last
   30 Days`.

:guilabel:`Market`
   Lowest, median, average and highest competitor price and their number, on the net or gross basis
   of the rule. The competitor prices used are listed at the bottom.

:guilabel:`Cost and Margin`
   The cost with its breakdown, the floor and the ceiling, and the margin before and after.

:guilabel:`Decision`
   The rule, who decided and when, and a note for a rejection.

Accept or reject
----------------

Only a **Competitor Prices manager** can :guilabel:`Accept` or :guilabel:`Reject`. Accepting writes
the recommended price as set in :guilabel:`When Accepted`, marks the recommendation
:guilabel:`Accepted` and posts a note in the chatter of the product with the old and the new price.
Rejecting keeps the price and keeps the rejection for the number of days of the rule.

.. warning::
   Accepting changes a real price. Look at the market, the cost and the margin first, and accept in
   bulk only when you have checked the rule that created the recommendations.

Lowest price of the last 30 days
--------------------------------

When you announce a price reduction in the EU, the earlier price you show must be the lowest price of
the previous 30 days (Omnibus Directive, Article 6a). Every recommendation shows your own lowest
price of the last 30 days, taken from the recorded own prices (see :doc:`products`), so you can
quote the right reference price.

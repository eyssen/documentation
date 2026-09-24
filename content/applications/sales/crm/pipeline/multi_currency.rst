=================================
Opportunities in other currencies
=================================

By default, the expected revenue of a lead or an opportunity is expressed in the company currency.
The *CRM - Multi Currency* module (``eyssen_crm_multi_currency``) lets each opportunity be quoted in
the customer's own currency while the pipeline figures stay comparable.

Sales team default currency
===========================

Each sales team gets a :guilabel:`Default Currency` field, in
:menuselection:`CRM app --> Configuration --> Sales Teams`. New leads and opportunities of the team
start in that currency, so an export team can work in EUR while the domestic team works in the
company currency.

Currency on the opportunity
===========================

The lead and opportunity form gains two fields:

- :guilabel:`Currency`: the currency this deal is quoted in. It defaults to the sales team's
  :guilabel:`Default Currency`.
- :guilabel:`Expected Revenue in Currency`: the amount as the customer sees it.

The standard :guilabel:`Expected Revenue` field is then computed from it, converted to the company
currency at the current rate. Every pipeline figure — the Kanban totals, the Pipeline Analysis and
the Forecast reports — therefore keeps working on comparable amounts.

.. important::
   Enter the deal amount in :guilabel:`Expected Revenue in Currency`. :guilabel:`Expected Revenue`
   is the converted value and is recomputed from it.

.. screenshot:: sales-crm-multi-currency-opportunity
   :menu: CRM ‣ Sales ‣ My Pipeline ‣ (an opportunity)
   :shows: An opportunity form with the Currency field, the "Expected Revenue in Currency" amount in that currency and the converted Expected Revenue in the company currency.
   :highlight: The Currency and "Expected Revenue in Currency" fields (red frame).
   :data: Opportunity for a foreign customer; 12 000 in a foreign currency, converted to the company currency.
   :module: eyssen_crm_multi_currency
   :notes: English UI, light theme, 1440px width, crop to the field group.

.. seealso::
   :doc:`../../sales/products_prices/prices/currencies`

===================
Pricing extensions
===================

Pricing in Odoo is driven by a product's :guilabel:`Sales Price` and by
:doc:`pricelists <../../../sales/sales/products_prices/prices/pricing>`. The eYssen modules on this
page extend that machinery with pricelist **tags**, an explicit **rule order**, a second price
**currency**, a table of fixed **currency pairs**, pricelist prices shown **on the product**,
spreadsheet **imports** and a full **price history**.

.. _inventory/pricing/pricelist-tags:

Pricelist tags
==============

``eyssen_product_pricelist_tag`` lets a pricelist rule apply to a **tag** instead of to one
product, one variant or a whole product category — so a discount can follow a freely chosen group
of products that crosses category boundaries.

Tags are maintained under :menuselection:`Sales --> Configuration --> Pricelist Tags`; each has
a translatable :guilabel:`Tag` name and a :guilabel:`Color`. Products carry their
:guilabel:`Pricelist Tags` on the product form, and a pricelist rule gains :guilabel:`Tag` as an
extra choice in its :guilabel:`Apply On` field, with a :guilabel:`Tag` field to pick the tag. The
rule is then named after the tag (`Tag: Winter sale`) in the pricelist's rule list.

.. screenshot:: inventory-pricing-pricelist-tag-rule
   :menu: Sales ‣ Products ‣ Pricelists ‣ (a pricelist)
   :shows: A pricelist rule whose "Apply On" is set to "Tag", with the "Tag" field filled in, listed among
      the pricelist's other rules where its name reads "Tag: <tag name>".
   :highlight: The "Apply On" and "Tag" cells (red frame).
   :data: Pricelist "Public (HUF)"; rule applying a 20% discount to the tag "Winter sale".
   :module: eyssen_product_pricelist_tag
   :notes: English UI, light theme, 1440px width, crop to the rule lines.

.. screenshot:: inventory-pricing-pricelist-tags-on-product
   :menu: Inventory ‣ Products ‣ Products ‣ (a product)
   :shows: The "Pricelist Tags" field of a product form holding two coloured tags.
   :highlight: The "Pricelist Tags" field (red frame).
   :data: Tags "Winter sale" and "Clearance".
   :module: eyssen_product_pricelist_tag
   :notes: English UI, light theme, 1440px width, crop to the field.

.. important::
   When a product carries several tags that each have a rule, the rule giving the **smallest**
   discount currently wins. Assign overlapping tags deliberately, or keep one tag per product per
   pricelist.

Webshop ribbon from a tag
-------------------------

``eyssen_product_pricelist_tag_ribbon`` links a pricelist tag to a webshop **ribbon**: a
:guilabel:`Ribbon` field on the tag names the ribbon to show, and assigning the tag to a product
sets that product's website ribbon automatically. Two settings buttons keep existing products in
sync — :guilabel:`Update All` re-applies the ribbon of each product's first tag, and
:guilabel:`Clean All` removes the ribbon from every product.

.. screenshot:: inventory-pricing-tag-ribbon
   :menu: Sales ‣ Configuration ‣ Pricelist Tags ‣ (a tag)
   :shows: A pricelist tag form with the "Ribbon" field selected.
   :highlight: The "Ribbon" field (red frame).
   :data: Tag "Winter sale" linked to the ribbon "Sale".
   :module: eyssen_product_pricelist_tag_ribbon
   :notes: English UI, light theme, 1440px width, crop to the form.

Ordering pricelist rules
========================

``eyssen_product_pricelist_sequence`` adds a :guilabel:`Sequence` to pricelist rules, so the order
in which they are evaluated can be set explicitly by dragging the handle on the rule list, instead
of depending on the rules' natural ordering. This matters as soon as several rules can match the
same product — for example a tag rule and a category rule.

Pricelist prices on the product
===============================

``eyssen_product_show_pricelist_price`` brings pricelist prices onto the product itself, so a
salesperson does not have to open each pricelist to compare them.

On a pricelist (:menuselection:`Sales --> Products --> Pricelists`), three switches decide where
that pricelist's price is shown:

- :guilabel:`Display on Product Form`;
- :guilabel:`Display on Product List`; and
- :guilabel:`Display on Product Kanban`.

Enabling :guilabel:`Display on Product List` or :guilabel:`Display on Product Kanban` creates a
per-pricelist price column for that pricelist, available from the optional-column selector. The
product form additionally shows an :guilabel:`All Prices` summary listing every pricelist's current
price for the product, computed for today's date.

.. screenshot:: inventory-pricing-show-pricelist-price-settings
   :menu: Sales ‣ Products ‣ Pricelists ‣ (a pricelist)
   :shows: A pricelist form with the "Display on Product Form", "Display on Product List" and "Display on
      Product Kanban" switches.
   :highlight: The three switches (red frame).
   :data: Pricelist "Public (HUF)" with all three enabled.
   :module: eyssen_product_show_pricelist_price
   :notes: English UI, light theme, 1440px width, crop to the switches.

.. screenshot:: inventory-pricing-all-prices-on-product
   :menu: Inventory ‣ Products ‣ Products ‣ (a product)
   :shows: The "All Prices" summary on a product form, listing each pricelist with the price it currently
      gives for this product.
   :highlight: The "All Prices" block (red frame).
   :data: Three pricelists with different prices for the same product.
   :module: eyssen_product_show_pricelist_price
   :notes: English UI, light theme, 1440px width, crop to the block.

Sales price in a foreign currency
=================================

``product_currency_price`` lets a product's sales price be maintained in a **supplier or list
currency** while the company-currency price is derived from it, which keeps an imported catalog in
step with the exchange rate.

First, flag the currencies to offer (:menuselection:`Accounting --> Configuration --> Currencies`):

- :guilabel:`Show on Product` — a sales price in this currency can be entered on a product.
- :guilabel:`Sales Price Markup (%)` — the percentage added to the converted amount. A markup of
  `2.5` means the company-currency sales price is the converted amount multiplied by 1.025.

.. screenshot:: inventory-pricing-currency-settings
   :menu: Accounting ‣ Configuration ‣ Currencies ‣ (a currency)
   :shows: A currency form with the "Show on Product" checkbox enabled and the "Sales Price Markup (%)"
      field filled in.
   :highlight: The two fields (red frame).
   :data: Currency EUR, markup 2.5%.
   :module: product_currency_price
   :notes: English UI, light theme, 1440px width, crop to the fields.

On the product form, pick the :guilabel:`Foreign Price Currency` and enter the
:guilabel:`Foreign Sales Price`. The company-currency :guilabel:`Sales Price` is then computed from
it with the current rate and the currency's markup, and is recomputed automatically whenever an
exchange rate for that currency is added, changed or removed, or the markup is edited.

.. screenshot:: inventory-pricing-foreign-price
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ General Information tab
   :shows: A product form with the "Foreign Price Currency" set to EUR, the "Foreign Sales Price" entered,
      and the company-currency "Sales Price" computed from it.
   :highlight: The "Foreign Price Currency" and "Foreign Sales Price" fields (red frame).
   :data: Foreign price 100.00 EUR, markup 2.5%, resulting HUF sales price computed from the current rate.
   :module: product_currency_price
   :notes: English UI, light theme, 1440px width, crop to the price fields.

.. note::
   Only **one** foreign currency price can be set per product, and the company currency is never
   offered as a foreign currency.

.. note::
   Requires the eYssen live exchange-rate module (``eyssen_currency_rate_live_community``) to keep
   the rates up to date; without current rates the derived price does not change.

Fixed price pairs
=================

Converting with the daily exchange rate is not always wanted: a price list agreed with a customer
often maps a **fixed** base price to a **fixed** price per currency (for example 100 EUR always
being 39 900 HUF, regardless of today's rate). ``eyssen_pricelist_price_pair`` implements exactly
that as a new :guilabel:`Price Pair` computation on a pricelist rule.

A rule set to :guilabel:`Price Pair` holds a table of :guilabel:`Price Pairs`: each pair has a
:guilabel:`Base Price` in the company currency and, below it, one line per
:guilabel:`Currency` with the :guilabel:`Price` to use in that currency.

Three options control what happens when no pair matches:

- :guilabel:`Missing Pair` — :guilabel:`Use Currency Rate` falls back to the normal conversion,
  :guilabel:`Use Zero` yields a zero price.
- :guilabel:`Use Global Pair` — when the rule has no matching pair of its own, a global pair (one
  not attached to any rule) with the same base price and a line in the target currency is used.
- :guilabel:`Reuse Pairs From` — use another rule's pair table instead of copying it onto every
  rule, which keeps one shared table for many tag rules.

.. screenshot:: inventory-pricing-price-pair-rule
   :menu: Sales ‣ Products ‣ Pricelists ‣ (a pricelist) ‣ (a rule)
   :shows: A pricelist rule whose "Price Computation" is "Price Pair", showing the "Missing Pair", "Use Global
      Pair" and "Reuse Pairs From" options and the "Price Pairs" table with one base price and its per-currency
      lines.
   :highlight: The "Price Pairs" table (red frame).
   :data: Base price 100.00 EUR with lines for HUF and RON.
   :module: eyssen_pricelist_price_pair
   :notes: English UI, light theme, 1440px width, full form.

Pairs can also be loaded in bulk: an import wizard either reads a CSV :guilabel:`File` or copies
every pair and currency line from a :guilabel:`Source Pricelist Rule`, optionally replacing the
pairs already on the target rule.

.. screenshot:: inventory-pricing-price-pair-import
   :menu: Sales ‣ Products ‣ Pricelists ‣ (a rule) ‣ (import price pairs)
   :shows: The "Import Price Pairs" wizard with "Mode" set to "Import from file", the File field, the target
      rule and the "Replace existing pairs on target" checkbox.
   :highlight: The "Mode" field (red frame).
   :data: A CSV file of base prices and per-currency prices.
   :module: eyssen_pricelist_price_pair
   :notes: English UI, light theme, 1440px width, crop to the wizard.

Importing pricelist items
=========================

``eyssen_pricelist_import`` fills a pricelist from a spreadsheet. On the pricelist form,
:guilabel:`Import Items` opens a wizard that takes a :guilabel:`Data file` — an Excel workbook whose
first sheet lists the product's internal reference in the first column and the fixed price in the
second — and creates or updates one fixed-price rule per product. :guilabel:`Delete Items` empties
the pricelist's rule list in one step.

.. screenshot:: inventory-pricing-pricelist-import
   :menu: Sales ‣ Products ‣ Pricelists ‣ (a pricelist) ‣ Import Items
   :shows: The "Import Items" wizard with the target pricelist and the "Data file" upload field, and the
      "Import Items" and "Delete Items" buttons visible on the pricelist form behind it.
   :highlight: The "Data file" field and the two buttons (red frames).
   :data: An .xlsx file with internal references and fixed prices.
   :module: eyssen_pricelist_import
   :notes: English UI, light theme, 1440px width, crop to the wizard and the buttons.

.. important::
   :guilabel:`Delete Items` removes **every** rule of the pricelist without asking for
   confirmation. Export the pricelist first if the rules may be needed again.

.. note::
   The Excel import needs the ``openpyxl`` Python library in the Odoo environment.

Price history
=============

``product_price_history`` records every price change, so it can be answered later what a product
cost at a given moment and why it changed.

Each change is stored as one event with the :guilabel:`Price Type` — :guilabel:`Sales Price`,
:guilabel:`Cost Price` or :guilabel:`Pricelist Price` — the :guilabel:`Pricelist` it belongs to (for
a pricelist price), the :guilabel:`Old Price` and :guilabel:`New Price`, the
:guilabel:`Effective Date` on which the new price applies, the date it was
recorded, the user who made the change, and a description of what caused it.

A :guilabel:`Price History` tab on the product form lists the product's own events, and
:menuselection:`Sales --> Configuration --> Price History` opens the same records with the full
search and grouping options.

.. screenshot:: inventory-pricing-price-history
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ Price History tab
   :shows: The "Price History" tab of a product form, listing the price events with their Effective Date,
      Price Type, Pricelist, Old Price, New Price, source description and user.
   :highlight: The "Old Price" and "New Price" columns (red frame).
   :data: Five events: two sales-price changes, one cost change and two pricelist-rule changes.
   :module: product_price_history
   :notes: English UI, light theme, 1440px width, crop to the tab.

Events with an effective date in the future are recorded as **projected** and become effective
automatically when their date arrives; two scheduled actions do this work, one processing the
event queue every few minutes and one materialising the projected events. A one-off
:guilabel:`Seed Missing Price Baselines` action, available to system administrators from the
:guilabel:`Price History` list, creates the initial events for a catalog that already has prices
when the module is installed.

.. note::
   Because the events are recorded from the price changes themselves, the history only covers what
   happened after the module was installed, plus whatever the bootstrap action created.

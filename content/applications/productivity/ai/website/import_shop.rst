====================================
Blog posts and products in an import
====================================

Two bridge modules extend the :doc:`website import <import>`. They install themselves when the
matching app is installed:

- **AI Website Import - Blog** (``ai_website_import_blog``), with the Blog app;
- **AI Website Import - eCommerce** (``ai_website_import_sale``), with the eCommerce app.

Blog posts
==========

The import recognises the articles of the source: pages marked as articles, pages under addresses
such as ``/blog/…`` or ``/news/…`` and, on WordPress, the posts of its public list of posts. When it
finds some, it asks "Import the 34 blog posts too?" (field :guilabel:`Import the blog posts`).

The posts are created in the first blog of the target website, or in a new blog named "Blog". Each
post gets its title, its date, its text (headings, paragraphs, lists, quotes, links, bold and
italic, pictures), its cover picture and its SEO texts. They are unpublished unless
:guilabel:`Publish the pages` is on. A 301 redirect is created from each old address to the new
post.

At most 200 posts are imported, with 30 pictures per post.

Products
========

The import reads products from the public product list of the shop (Shopify, WooCommerce) or from
the product data written in its pages (schema.org). No password or key is asked or stored. When it
finds products, it asks "Import the 12 products too (unpublished)?" (field :guilabel:`Import the
products`).

The products are created unpublished (unless :guilabel:`Publish the pages` is on) with their name,
price, description, pictures and a 301 redirect from their old address. Stock
quantities are not imported. At most 250 products are imported.

The :guilabel:`Products` tab of the review lists every product with :guilabel:`Include`, the number
of :guilabel:`Variants`, the :guilabel:`Price` and the :guilabel:`Warnings`.

Variants
--------

The options of a product (size, colour…) become product attributes. An attribute or value with the
same name that already exists in the database is reused; missing ones are created.

- When the variants have their own price, reference, barcode or picture, or when the shop sells only
  some combinations, Odoo variants are created (the combinations that are not sold are archived).
  Otherwise the options are kept as attributes that do not create variants, and the product stays
  one product.
- The lowest variant price becomes the product price; the differences become extra prices per value
  when they add up for every variant. When they do not, every variant keeps the product price and
  the review and the log list the variants to price by hand.
- References, valid barcodes that are not used yet and pictures per variant are set.
- A product with more than 100 variants (or more than Odoo's own variant limit, when that is lower)
  is imported without variants, and the review says so.

Prices in another currency
--------------------------

The import finds the currency of the source prices in the shop data or in the pages. When it differs
from the currency of the website's company, the import asks what to do (field :guilabel:`Prices in
another currency`):

- :guilabel:`Convert with Odoo's exchange rate`: the prices are converted with the current rate of
  Odoo (its date is shown) and rounded. This is the default when Odoo has a rate.
- :guilabel:`Keep the source prices in a pricelist in their currency`: a pricelist of the website in
  the source currency gets the source prices as fixed prices. The currency is activated if needed.
  The pricelist can be chosen on the website; it is not made the default anywhere else.
- :guilabel:`Same numbers, not converted`: the numbers are kept as they are. This is the default
  when Odoo has no rate; check the prices afterwards.

The :guilabel:`Products` tab shows the decision with the rate, and you can change it until you
import.

Undo
====

:guilabel:`Undo import` also removes the posts, a blog the import created, the products with their
variants, and the pricelist. Attributes and values created by the import are deleted only when no
product uses them any more, and a currency the import activated is deactivated only when no company
or pricelist uses it.

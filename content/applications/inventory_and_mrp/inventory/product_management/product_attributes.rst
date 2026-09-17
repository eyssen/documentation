=============================
Product attribute extensions
=============================

Odoo's product attributes exist to generate variants. The eYssen modules on this page reuse the
same attributes as **structured product data**: an attribute can become a field of its own on the
product form, several attributes can be combined into one displayed value, the selectable values of
one attribute can be narrowed by another, and a reusable collection of attributes can be applied to
a product in one step.

.. seealso::
   :doc:`Product variants <../../manufacturing/advanced_configuration/product_variants>`

Attribute options
=================

``eyssen_product_attribute`` adds the following options to every attribute
(:menuselection:`Products --> Configuration --> Attributes`):

- :guilabel:`Direct Field` — the attribute also becomes a **field of its own** on the product form,
  holding the values assigned to that product. This makes the attribute available as a column, a
  filter and a group-by, and keeps a product's attribute data readable without opening the variant
  matrix. Ticking or unticking the option creates or removes that field and the view extensions
  that show it.
- :guilabel:`Mixed Field` and its :guilabel:`Mixed Fields` lines — the attribute's displayed value
  is **assembled from other attributes**. Each line names a :guilabel:`Sub Attribute` and,
  optionally, a :guilabel:`Prefix` and a :guilabel:`Suffix`, and the lines are concatenated in
  their :guilabel:`Sequence` order. A typical use is a single *Size* attribute built from a width
  and a length attribute, displayed as `40/32`.
- :guilabel:`Can be only one variant` — the attribute may contribute at most one value per product,
  so it cannot multiply the number of variants.
- :guilabel:`Show One Value Variant` — the attribute is shown on a product even when it has only a
  single value, which would otherwise be hidden.

.. screenshot:: inventory-product-attributes-options
   :menu: Products ‣ Configuration ‣ Attributes ‣ (an attribute)
   :shows: An attribute form with the eYssen options "Direct Field", "Mixed Field", "Can be only one
      variant" and "Show One Value Variant", and the "Mixed Fields" lines below with their Prefix, Sub
      Attribute and Suffix.
   :highlight: The four option checkboxes (red frame).
   :data: Attribute "Size" as a mixed field built from "Width" and "Length" with a "/" separator.
   :module: eyssen_product_attribute
   :notes: English UI, light theme, 1440px width, full form.

Value filters
=============

A **value filter** limits which values of one attribute may be chosen, depending on the value
selected for another attribute — so impossible combinations never appear.

A filter is defined on the attribute whose values it restricts, and names:

- the :guilabel:`Attribute Values` it applies to;
- the :guilabel:`Filter Attribute` whose selection drives the restriction; and
- the :guilabel:`Filter Values` of that attribute for which the restriction holds.

An attribute with at least one filter is marked with the read-only :guilabel:`Value Filter`
indicator. The filters apply both in the back office and in the webshop's product configurator, so
a customer is never offered a combination that cannot be produced.

.. screenshot:: inventory-product-attributes-value-filter
   :menu: Products ‣ Configuration ‣ Attributes ‣ (an attribute) ‣ (a value filter)
   :shows: A value filter form naming the Attribute Values it restricts, the Filter Attribute and the Filter
      Values, with its computed display name at the top.
   :highlight: The "Filter Attribute" and "Filter Values" fields (red frame).
   :data: The sizes 44-48 of the "Size" attribute restricted to the "Material: Leather" value.
   :module: eyssen_product_attribute
   :notes: English UI, light theme, 1440px width, full form.

Attribute collections
=====================

``eyssen_product_attribute_collection`` stores reusable sets of attributes, so a new product of a
known kind gets all of its attributes in one step instead of line by line.

A collection (:menuselection:`Sales --> Configuration --> Attribute Collections`) has an
:guilabel:`Attribute Collection Name`, a :guilabel:`Company`, the list of
:guilabel:`Attributes` it contains and a free-text :guilabel:`Comment`.

On a product form, a wizard asks for the :guilabel:`Attribute Collection` and then lists its
attributes with a :guilabel:`Values` field each, so the values can be picked before the attribute
lines are created on the product in one go.

.. screenshot:: inventory-product-attributes-collection-wizard
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ (attribute collection wizard)
   :shows: The attribute-collection wizard with the "Attribute Collection" field selected and one line per
      attribute of that collection, each with its "Values" field filled in.
   :highlight: The "Attribute Collection" field (red frame).
   :data: Collection "Footwear" with the attributes Size, Colour and Width.
   :module: eyssen_product_attribute_collection
   :notes: English UI, light theme, 1440px width, crop to the wizard.

Webshop behaviour of attributes
===============================

``eyssen_product_attribute_ws`` adds three webshop-specific options to an attribute:

- :guilabel:`Show variants as separate products on website` — each variant of this attribute is
  listed as its own product in the shop, instead of one product with a variant selector.
- :guilabel:`Show One Value Variant on Webshop` — the attribute is shown in the shop even when it
  has only one value.
- :guilabel:`Product Page Visibility` — :guilabel:`Visible` or :guilabel:`Hidden`; a hidden
  attribute is not displayed on the product detail page of the website.

.. screenshot:: inventory-product-attributes-website-options
   :menu: Products ‣ Configuration ‣ Attributes ‣ (an attribute)
   :shows: The website options of an attribute: "Show variants as separate products on website", "Show One
      Value Variant on Webshop" and the "Product Page Visibility" selection.
   :highlight: The three options (red frame).
   :data: Attribute "Colour" with variants shown as separate products and visibility "Visible".
   :module: eyssen_product_attribute_ws
   :notes: English UI, light theme, 1440px width, crop to the options.

.. note::
   The webshop-side presentation of these options is documented with the **Website** application.
   This page only covers where they are configured on the attribute.

Supplier colour codes
=====================

``supplier_color_code`` records, per attribute value and per supplier, the code that supplier uses
for that value — so a purchase order carries the vendor's own colour code instead of the internal
name. On an attribute value, a :guilabel:`Supplier Colour Codes` list holds one line per
:guilabel:`Supplier` with its :guilabel:`Colour Code`, and the matching code is printed on the
purchase order report for the order's vendor.

.. note::
   The labels of this module are currently Hungarian in the source code (*Szállítói színkódok*,
   *Színkód*, *Beszéllító*), so they appear in Hungarian regardless of the interface language.

.. screenshot:: inventory-product-attributes-supplier-color-code
   :menu: Products ‣ Configuration ‣ Attributes ‣ (an attribute) ‣ (a value) ‣ Supplier Colour Codes
   :shows: The supplier colour code list of an attribute value, with one line per supplier and the code that
      supplier uses for the value.
   :highlight: The colour-code lines (red frame).
   :data: The colour "Black" with the codes "099" for one supplier and "BK" for another.
   :module: supplier_color_code
   :notes: English UI, light theme, 1440px width, crop to the list. The field labels appear in Hungarian.

Automatic website categories
============================

``product_public_category_rule`` assigns products to webshop categories automatically, from rules
instead of by hand. A rule (:menuselection:`Website --> eCommerce --> Category Rules`) has a
:guilabel:`Name`, an :guilabel:`Active` flag, a :guilabel:`Sequence`, the
:guilabel:`Category` (or categories) it assigns, and the conditions that select the products:
:guilabel:`Attribute Values`, :doc:`Pricelist Tags <pricing_extensions>` and product tags. An
:guilabel:`Apply Rules` action re-evaluates every rule and updates the products' website
categories.

.. note::
   The webshop-side effect of these categories is documented with the **Website** application.

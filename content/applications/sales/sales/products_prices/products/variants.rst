================
Product variants
================

Product variants are used to give single products a variety of different characteristics and options
for customers to choose from, such as size, style, or color, just to name a few.

Products variants can be managed via their individual product template, or by navigating to either
the :guilabel:`Product Variants` or :guilabel:`Attributes` page. All of these options are located
within the Odoo *Sales* application.

.. example::
   An apparel company has the following variant breakdown for one their best-selling t-shirts:

   - Unisex Classic Tee

     - Color: Blue, Red, White, Black
     - Size: S, M, L, XL, XXL

   Here, the **T-shirt** is the product template, and **T-shirt: Blue, S** is a specific product
   variant.

   **Color** and **Size** are *attributes*, and the corresponding options (like **Blue** and **S**)
   are *values*.

   In this instance, there is a total of twenty different product variants: four **Color** options
   multiplied by five **Size** options. Each variant has its own inventory count, sales totals, and
   other similar records in Odoo.

.. seealso::
   :ref:`ecommerce/products/product-variants`

Configuration
=============

To use product variants, the *Variants* setting **must** be activated in the Odoo *Sales*
application.

To do that, go to :menuselection:`Sales app --> Configuration --> Settings`, and locate the
:guilabel:`Product Catalog` section at the top of the page.

In that section, check the box to enable the :guilabel:`Variants` feature.

.. screenshot:: sales-variants-setting
   :menu: Sales ‣ Configuration ‣ Settings
   :shows: The Settings page scrolled to the "Product Catalog" section with the "Variants" checkbox enabled and the "Attributes" link beside it.
   :highlight: The "Variants" setting (red frame).
   :data: Demo company.
   :module: product
   :notes: English UI, light theme, 1440px width, crop to the setting block.

Then, click :guilabel:`Save` at the top of the :guilabel:`Settings` page.

Attributes
==========

Before product variants can be set up, attributes **must** be created. To create, manage, and modify
attributes, navigate to :menuselection:`Sales app --> Configuration --> Attributes`.

.. note::
   The order of attributes on the :guilabel:`Attributes` page dictates how they appear on the
   *Product Configurator*, *Point of Sale* dashboard, and *eCommerce* pages.

To create a new attribute from the :guilabel:`Attributes` page, click :guilabel:`New`. Doing so
reveals a blank attributes form that can be customized and configured in a number of ways.

.. screenshot:: sales-variants-attribute-form
   :menu: Sales ‣ Configuration ‣ Attributes ‣ New
   :shows: A blank attribute form with the Attribute Name, Display Type, Variant Creation Mode, eCommerce Filter Visibility and Category fields, and the empty values list.
   :highlight: No highlight; the empty form is the subject.
   :data: New, unsaved attribute.
   :module: product
   :notes: English UI, light theme, 1440px width, full form.

First, create an :guilabel:`Attribute Name`, such as `Color` or `Size`.

Next, select one of the options from the :guilabel:`Display Type` field. The :guilabel:`Display
Type` determines how this product is shown on the online store, *Point of Sale* dashboard, and
*Product Configurator*.

The :guilabel:`Display Type` options are:

- :guilabel:`Pills`: options appear as selectable buttons on the product page of the online store.
- :guilabel:`Color`: options appear as small, colored squares, which reflect any HTML color codes
- :guilabel:`Radio`: options appear in a bullet-style list on the product page of the online store.
- :guilabel:`Select`: options appear in a drop-down menu on the product page of the online store.
  set, on the product page of the online store.
- :guilabel:`Multi-checkbox (option)`: options appear as selectable checkboxes on the product page
  of the online store.

.. screenshot:: sales-variants-display-types
   :menu: (eCommerce product page)
   :shows: The same attribute rendered on the online store with each Display Type: Radio, Pills, Select, Color and Multi-checkbox.
   :highlight: Each display type labelled (red frames).
   :data: Attribute "Size" with three values.
   :module: website_sale
   :notes: English UI, light theme, crop to the product-configurator block.

The :guilabel:`Variant Creation Mode` field informs Odoo when to automatically create a new variant
once an attribute is added to a product.

.. note::
   The :guilabel:`Variant Creation Mode` field **must** be set to :guilabel:`Never (option)` in
   order for the :guilabel:`Multi-checkbox (option)` to work properly as the :guilabel:`Display
   Type`.

- :guilabel:`Instantly`: creates all possible variants as soon as attributes and values are added
  to a product template.
- :guilabel:`Dynamically`: creates variants **only** when corresponding attributes and values are
  added to a sales order.
- :guilabel:`Never (option)`: never automatically creates variants.

.. warning::
   Once added to a product, an attribute's :guilabel:`Variants Creation Mode` cannot be edited.

The :guilabel:`eCommerce Filter Visibility` field determines whether or not these attribute options
are visible to the customer on the front-end, as they shop on the online store.

- :guilabel:`Visible`: the attribute values are visible to customers on the front-end.
- :guilabel:`Hidden`: the attribute values are hidden from customers on the front-end.

Lastly, in the optional :guilabel:`eCommerce Category` field, select a category from a drop-down
menu to group similar attributes under the same section for added specificity and organization.

.. note::
   To view the details related to the attribute category selected, click the internal link
   :icon:`fa-arrow-right` :guilabel:`(right arrow)` icon to the far-right of the
   :guilabel:`eCommerce Category` field, once an option has been selected. Doing so reveals that
   attribute category's detail form.

   .. screenshot:: sales-variants-attribute-category
      :menu: Sales ‣ Configuration ‣ Attributes ‣ (an attribute) ‣ Category
      :shows: An attribute-category form opened from the internal-link arrow next to the Category field, listing the attributes it groups.
      :highlight: The Category name field (red frame).
      :data: Category "Dimensions".
      :module: product
      :notes: English UI, light theme, 1440px width, full form.

   Here, the :guilabel:`Category Name` and :guilabel:`Sequence` is displayed at the top. Followed by
   :guilabel:`Related Attributes` associated with the category. These attributes can be
   dragged-and-dropped into a desirable order of priority.

   Attributes can be directly added to the category, as well, by clicking :guilabel:`Add a line`.

.. tip::
   To create an attribute category directly from this field, start typing the name of the new
   category, then select either :guilabel:`Create` or :guilabel:`Create and edit...` from the
   drop-down menu that appears.

   Clicking :guilabel:`Create` creates the category, which can be modified later. Clicking
   :guilabel:`Create and edit...` creates the category and reveals a :guilabel:`Create Category`
   pop-up window, in which the new attribute category can be configured and customized.

Attribute values
----------------

Attribute values should be added to the :guilabel:`Attribute Values` tab. Values can be added to an
attribute at any time, if needed.

To add a value, click :guilabel:`Add a line` in the :guilabel:`Attribute Values` tab.

Then, enter the name of the value in the :guilabel:`Value` column. Next, check the box in the
:guilabel:`Is custom value` column, if the value is custom (i.e. the customer gets to provide unique
specifications that are specific to this particular value).

Colors
~~~~~~

Next to :guilabel:`Display Type`, select the :guilabel:`Color` option. Go to the
:guilabel:`Attribute Values` tab to modify the value settings.

.. screenshot:: sales-variants-value-image
   :menu: Sales ‣ Configuration ‣ Attributes ‣ (a color attribute) ‣ (a value)
   :shows: An attribute-value form where an image is uploaded to represent a pattern instead of a plain color.
   :highlight: The uploaded image (red frame).
   :data: Attribute "Color", value "Pattern".
   :module: product
   :notes: English UI, light theme, 1440px width, crop to the value form.

To choose a color, click the blank circle in the :guilabel:`Color` column, which reveals an HTML
color selector pop-up window.

.. screenshot:: sales-variants-color-picker
   :menu: Sales ‣ Configuration ‣ Attributes ‣ (a color attribute) ‣ (a value) ‣ Color
   :shows: The colour-picker pop-up used to set the colour of an attribute value.
   :highlight: The selected colour swatch (red frame).
   :data: Attribute "Color", value "White".
   :module: product
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

In this pop-up window, select a specific color by dragging the color slider to a particular hue,
and clicking on the color portion directly on the color gradient window.

Or, choose a specific color by clicking the *dropper* icon, and selecting a desired color that's
currently clickable on the screen.

If you sell products with specific patterns, you can also add an image to display the
pattern of the product. To do so, click the :icon:`fa-camera` :guilabel:`(camera)` icon,
then click the :icon:`fa-pencil` :guilabel:`(pencil)` icon and select an image from your local
drive. This pattern will appear as a color option on the ecommerce product page.

.. screenshot:: sales-variants-pattern-on-shop
   :menu: (eCommerce product page)
   :shows: The online store product page where the pattern image is shown as one of the selectable colour options.
   :highlight: The pattern swatch (red frame).
   :data: Product "Conference Chair" with a pattern colour value.
   :module: website_sale
   :notes: English UI, light theme, crop to the colour selector.

.. tip::
   Attributes can also be created directly from the product template by adding a new line and
   typing the name into the :guilabel:`Variants` tab.

Once an attribute is added to a product, that product is listed and accessible, via the attribute's
:guilabel:`Related Products` smart button. That button lists every product in the database currently
using that attribute.

Product variants
================

Once an attribute is created, use the attribute (and its values) to create a product variant. To do
that, go to :menuselection:`Sales app --> Products --> Products`, and select an existing product to
view that desired product's form. Or, click :guilabel:`Create` to create a new product, to which a
product variant can be added.

On the product form, click the :guilabel:`Attributes \& Variants` tab to view, manage, and modify
attributes and values for the product.

.. screenshot:: sales-variants-product-attributes-tab
   :menu: Sales ‣ Products ‣ Products ‣ (a product) ‣ Attributes & Variants
   :shows: The "Attributes & Variants" tab of a product form with two attributes and their selected values.
   :highlight: The attribute rows (red frame).
   :data: Product "Conference Chair"; Legs and Color.
   :module: product
   :notes: English UI, light theme, 1440px width, crop to the notebook.

To add an attribute to a product, and subsequent attribute values, click :guilabel:`Add a line` in
the :guilabel:`Attributes \& Variants` tab. Then, choose the desired attribute from the drop-down
menu that appears.

.. tip::
   Attributes can be created directly from the :guilabel:`Attributes \& Variants` tab of a product
   form. To do that, start typing the name of the new attribute in the blank field, and select
   either :guilabel:`Create` or :guilabel:`Create and edit...` from the mini drop-down menu that
   appears.

   Clicking :guilabel:`Create` creates the attribute, which can be customized later. Clicking
   :guilabel:`Create and edit...` creates the attribute, and a :guilabel:`Create Attribute` pop-up
   form appears. In the pop-up form, proceed to modify the attribute in a number of ways.

Once an attribute is selected in the :guilabel:`Attribute` column, proceed to select the specific
attribute values to apply to the product, via the drop-down menu available in the :guilabel:`Values`
column.

.. note::
   There is no limit to how many values can be added.

.. tip::
   Similar product variant creation processes are accessible through the Purchase, Inventory, and
   eCommerce applications.

.. _products/variants/configure-variants:

Configure variants
------------------

To the far-right of the attribute line is a :guilabel:`Configure` button. When clicked, Odoo reveals
a separate page showcasing those specific :guilabel:`Product Variant Values`.

.. screenshot:: sales-variants-configure-page
   :menu: Sales ‣ Products ‣ Products ‣ (a product) ‣ Attributes & Variants ‣ Configure
   :shows: The "Product Variant Values" page listing every value of the product's attributes with its extra price.
   :highlight: The "Value Price Extra" column (red frame).
   :data: Values of Legs and Color, one with an extra price.
   :module: product
   :notes: English UI, light theme, 1440px width, crop to the list.

Here, the specific :guilabel:`Value` name, :guilabel:`HTML Color Index` (if applicable), and
:guilabel:`Value Price Extra` are viewable.

.. note::
   The :guilabel:`Value Price Extra` represents the increase in the sales price if the attribute is
   selected.

When a value is clicked on the :guilabel:`Product Variant Values` page, Odoo reveals a separate
page, detailing that value's related details.

.. screenshot:: sales-variants-value-detail
   :menu: Sales ‣ Products ‣ Products ‣ (a product) ‣ Attributes & Variants ‣ Configure ‣ (a value)
   :shows: A single product-variant-value form with the Value, Attribute, Product and "Value Price Extra" fields.
   :highlight: The "Value Price Extra" field (red frame).
   :data: Value "Aluminium", extra price 50.00.
   :module: product
   :notes: English UI, light theme, 1440px width, full form.

On the specific product variant detail page, the :guilabel:`Value` and :guilabel:`Value Price Extra`
fields can be found, along with an :guilabel:`Exclude for` field.

In the :guilabel:`Exclude for` field, different :guilabel:`Product Templates` and specific
:guilabel:`Attribute Values` can be added. When added, this specific attribute value will be
excluded from those specific products.

Variants smart button
---------------------

When a product has attributes and variants configured in its :guilabel:`Attributes \& Variants` tab,
a :guilabel:`Variants` smart button appears at the top of the product form. The :guilabel:`Variants`
smart button indicates how many variants are currently configured for that specific product.

.. screenshot:: sales-variants-smart-button
   :menu: Sales ‣ Products ‣ Products ‣ (a product)
   :shows: The button box of a product form with the Variants smart button showing the number of generated variants.
   :highlight: The Variants smart button (red frame).
   :data: Product "Conference Chair", 4 variants.
   :module: product
   :notes: English UI, light theme, 1440px width, crop to the button box.

When the :guilabel:`Variants` smart button is clicked, Odoo reveals a separate page showcasing all
the specific product variant combinations configured for that specific product.

.. screenshot:: sales-variants-list
   :menu: Sales ‣ Products ‣ Products ‣ (a product) ‣ Variants
   :shows: The product-variants list of one product, showing each attribute combination with its internal reference and sales price.
   :highlight: No highlight; the variant list is the subject.
   :data: Four "Conference Chair" variants.
   :module: product
   :notes: English UI, light theme, 1440px width, crop to the list.

Impact of variants
==================

In addition to offering more detailed product options to customers, product variants have their own
impacts that can be taken advantage of throughout the Odoo database.

- :guilabel:`Barcode`: barcodes are associated with each variant, instead of the product template.
  Each individual variant can have its own unique barcode/SKU.
- :guilabel:`Price`: every product variant has its own public price, which is the sum of the
  product template price *and* any extra charges for particular attributes.

  .. example::
   A red shirt's sales price is $23 -- because the shirt's template price is $20, plus an additional
   $3 for the red color variant. Pricelist rules can be configured to apply to the product template,
   or to the variant.

- :guilabel:`Inventory`: inventory is counted for each individual product variant. On the product
  template form, the inventory reflects the sum of all variants, but the actual inventory is
  computed by individual variants.
- :guilabel:`Picture`: each product variant can have its own specific picture.

.. note::
   Changes to the product template automatically apply to every variant of that product.

.. seealso::
   :doc:`import`

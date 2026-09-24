=========
Discounts
=========

By offering discounts, you can entice your customers and drastically
increase your revenue. It is vital to offer discounts, whether they are
time-limited, seasonal or manually given.

To manage discounts, Odoo has powerful features that help set up a
pricing strategy tailored to every business.

Apply manual discounts
======================

If you seldom use discounts, applying manual ones might be the easiest
solution for your point of sale.

You can either apply a discount on the whole order or on specific
products inside an order.

Apply a discount on a product
-----------------------------

From your PoS session interface, use the *Disc* button.

.. screenshot:: pos-discounts-manual-disc-button
   :menu: (POS interface) ‣ Register screen
   :shows: The POS cart with a product line selected and the "Disc" button in the numpad used to enter a per-line discount.
   :highlight: The "Disc" button (red frame).
   :module: point_of_sale
   :notes: English UI, light theme, 1440px width, centered, crop to the cart and numpad.

Then, you can input a discount over the product that is currently
selected.

Apply a global discount
-----------------------

To apply a discount on the whole order, go to :menuselection:`Point of
Sale --> Configuration --> Point of Sale` and select your PoS.

Once on your PoS form, select *Global Discounts*, under the *Pricing* category.

.. screenshot:: pos-discounts-global-setting
   :menu: Point of Sale ‣ Configuration ‣ Settings
   :shows: The "Pricing" section of the POS settings with the global discount setting enabled.
   :highlight: The global discount setting (red frame).
   :module: point_of_sale, pos_discount
   :notes: English UI, light theme, 1440px width, centered, crop to the settings block.

Now, you have a new *Discount* button appearing on your PoS interface.

.. screenshot:: pos-discounts-global-button
   :menu: (POS interface) ‣ Register screen
   :shows: The POS register screen with the "Discount" button added to the button bar.
   :highlight: The "Discount" button (red frame).
   :module: point_of_sale, pos_discount
   :notes: English UI, light theme, 1440px width, centered.

Click on it and enter the wanted discount.

.. screenshot:: pos-discounts-global-in-cart
   :menu: (POS interface) ‣ Register screen
   :shows: The cart after applying a global discount, with a separate discount line and the reduced total.
   :module: point_of_sale, pos_discount
   :notes: English UI, light theme, 1440px width, centered, crop to the cart pane.

.. note::
   On this example, there is a global discount of 50% as well as a specific
   50% discount on oranges.

Apply time-limited discounts
============================

To activate time-limited discounts, you must activate the *Pricelists*
feature. To do so, go to :menuselection:`Point of Sale -->
Configuration --> Point of Sale` and open your PoS. Then, enable the
pricelist feature.

.. screenshot:: pos-discounts-pricelists-setting
   :menu: Point of Sale ‣ Configuration ‣ Settings
   :shows: The "Pricing" section of the POS settings with the "Pricelists" option enabled and the available pricelists listed below it.
   :highlight: The "Pricelists" setting block (red frame).
   :module: point_of_sale, product
   :notes: English UI, light theme, 1440px width, centered, crop to the settings block.

Once activated, you must choose the pricelists you want to make
available in the PoS and define a default one.

Create a pricelist
------------------

By default, Odoo has a *Public Pricelist* configured. To create more,
go to :menuselection:`Point of Sale --> Products --> Pricelists`. Then
click on create.

When creating a pricelist, you can set several criteria to use a
specific price: period, min. quantity, etc. You can also decide to apply
that pricelist on specific products or on the whole range.

.. screenshot:: pos-discounts-time-limited-pricelist
   :menu: Point of Sale ‣ Products ‣ Pricelists ‣ (a pricelist)
   :shows: A pricelist form with two price rules that each carry a validity start and end date.
   :data: Pricelist "Weekend promo" with two products discounted for one weekend.
   :module: product
   :notes: English UI, light theme, 1440px width, centered.

Using a pricelist with the PoS interface
----------------------------------------

On the PoS interface, a new button appears. Use it to select a
pricelist.

.. screenshot:: pos-discounts-pricelist-button
   :menu: (POS interface) ‣ Register screen
   :shows: The POS register screen with the pricelist button in the button bar and the list of available pricelists open.
   :highlight: The pricelist button (red frame).
   :module: point_of_sale, product
   :notes: English UI, light theme, 1440px width, centered.

Click on it to instantly update the prices with the selected pricelist. Then, you can finalize the
order.

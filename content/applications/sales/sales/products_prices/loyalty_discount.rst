=============================
Discount and loyalty programs
=============================

The Odoo *Sales*, *eCommerce*, and *Point of Sale* applications allow users to create discount and
loyalty programs that customers can use for online and in-store shopping. These programs offer more
varied, public, and time-sensitive pricing options than :doc:`pricelists
</applications/sales/sales/products_prices/prices/pricing>`.

Configure the settings
======================

To begin using discount and loyalty programs, navigate to :menuselection:`Sales --> Configuration
--> Settings`. Under the :guilabel:`Pricing` heading, activate the :guilabel:`Discounts, Loyalty &
Gift Card` setting by checking the box next to the feature. Finally, click :guilabel:`Save` to save
the changes.

.. _sales/products/loyalty-programs:

Configure discount and loyalty programs
=======================================

To create discount and loyalty programs, go to :menuselection:`Sales --> Products --> Discount &
Loyalty`.

If no discount or loyalty programs have been created yet, Odoo provides a choice of templates to
help create the first program. Choose one of the template cards, or click :guilabel:`New` to create
a new program from scratch.

Or, if there are already existing programs, select an existing program to edit it.

.. screenshot:: sales-loyalty-program-templates
   :menu: Sales ‣ Products ‣ Discount & Loyalty ‣ New
   :shows: The program template cards shown on a new discount & loyalty program: Coupons, Next Order Coupons, Loyalty Cards, Promotions, Discount Code, Buy X Get Y.
   :highlight: The template cards row (red frame).
   :data: Demo database, no program created yet.
   :module: loyalty
   :notes: English UI, light theme, 1440px width, crop to the template cards.

.. note::
   Templates **only** appear when no programs have been created, and they disappear once the first
   program is created.

Creating or editing a program opens the program form.

.. screenshot:: sales-loyalty-program-form
   :menu: Sales ‣ Products ‣ Discount & Loyalty ‣ (a program)
   :shows: A loyalty program form with the Program Name, Program Type, Currency, Points Unit, Validity, Limit Usage and Company fields.
   :highlight: The Program Type field (red frame).
   :data: Program "Loyalty Cards", points unit "Loyalty Points".
   :module: loyalty
   :notes: English UI, light theme, 1440px width, crop to the field group.

The program form contains the following fields:

- :guilabel:`Program Name`: Enter the name of the program in this field. The program name is **not**
  visible to the customer.
- :guilabel:`Program Type`: Select the desired :ref:`program type
  <sales/pricing_management/program-types>` from the drop-down menu.
- :guilabel:`Currency`: Select the currency used for the program.
- :guilabel:`Pricelist`: If desired, select a pricelist from the drop-down menu to have this loyalty
  program applied to a specific pricelist (and customers attached to the pricelist). More than one
  pricelist can be selected in this field. When a single loyalty program is linked to several
  pricelists, it makes it viable for different customer segments to have different pricelists, but
  the *same* loyalty programs. If this field is left blank, the program applies to everyone,
  regardless of pricelist.
- :guilabel:`Points Unit`: Enter the name of the points used for the :guilabel:`Loyalty Cards`
  program (e.g. `Loyalty Points`). The points unit name *is* visible to the customer. This field is
  **only** available when the :guilabel:`Program Type` is set to :guilabel:`Loyalty Cards`.
- :guilabel:`Start Date`: Select the date on which the program becomes valid. Leave this field blank
  if the program should always be valid and not expire.
- :guilabel:`End Date`: Select the date on which the program stops being valid. Leave this field
  blank if the program should always be valid and not expire.
- :guilabel:`Limit Usage`: If desired, tick this checkbox, and enter a number of :guilabel:`usages`
  to limit the number of times the program can be used during the validity period.
- :guilabel:`Company`: If working in a multi-company database, choose the one company for which the
  program is available. If left blank, the program is available to all companies in the database.
- :guilabel:`Available On`: Select the apps on which the program is available.
- :guilabel:`Website`: Select a website on which the program is available. Leave this field blank to
  make it available on all websites.
- :guilabel:`Point of Sale`: Select the point(s) of sale at which the program is available. Leave
  this field blank to make it available at all :abbr:`PoS (Point of Sale)`.

.. note::
   The options available on the program form vary depending on the :ref:`Program Type
   <sales/pricing_management/program-types>` selected.

All of the existing cards, codes, coupons, etc. that have been generated for the program are
accessible through the smart button located at the top of the form.

.. screenshot:: sales-loyalty-program-items-button
   :menu: Sales ‣ Products ‣ Discount & Loyalty ‣ (a program)
   :shows: The button box of a loyalty program with the Items smart button showing the number of generated coupons or cards.
   :highlight: The Items smart button (red frame).
   :data: Program "Loyalty Cards", 12 items.
   :module: loyalty
   :notes: English UI, light theme, 1440px width, crop to the button box.

.. note::
   In Odoo 17 (and later), when a loyalty card or coupon is associated with a contact in the
   database, a :guilabel:`Loyalty Cards` smart button conditionally appears on the contact form.

   .. screenshot:: sales-loyalty-contact-cards-button
      :menu: Sales ‣ Orders ‣ Customers ‣ (a customer)
      :shows: The button box of a contact form with the "Loyalty Cards" smart button.
      :highlight: The "Loyalty Cards" smart button (red frame).
      :data: Customer "Deco Addict", 1 loyalty card.
      :module: loyalty
      :notes: English UI, light theme, 1440px width, crop to the button box.

   This smart button **only** appears if a loyalty card or coupon is associated with the contact.

.. _sales/pricing_management/program-types:

Program types
-------------

The different :guilabel:`Program Types` available on the program form are:

- :guilabel:`Coupons`: Generate and share single-use coupon codes that grant immediate access to
  rewards.
- :guilabel:`Loyalty Cards`: When making purchases, the customer accumulates points to exchange for
  rewards on current and/or future orders.
- :guilabel:`Promotions`: Set conditional rules for ordering products, which, when fulfilled, grant
  access to rewards for the customer.
- :guilabel:`Discount Code`: Set codes which, when entered upon checkout, grant discounts to the
  customer.
- :guilabel:`Buy X Get Y`: for every (X) item bought, the customer is granted 1 credit. After
  accumulating a specified amount of credits, the customer can trade them in to receive (Y) item.
- :guilabel:`Next Order Coupons`: Generate and share single-use coupon codes that grant access to
  rewards on the customer's next order.

Conditional rules
-----------------

Next, configure the :guilabel:`Conditional rules` that determine when the program applies to a
customer's order.

In the :guilabel:`Rules & Rewards` tab, click :guilabel:`Add` next to :guilabel:`Conditional rules`
to add *conditions* to the program. This reveals a :guilabel:`Create Conditional rules` pop-up
window.

.. screenshot:: sales-loyalty-rules-rewards-tab
   :menu: Sales ‣ Products ‣ Discount & Loyalty ‣ (a program) ‣ Rules & Rewards
   :shows: The "Rules & Rewards" tab of a loyalty program with one conditional rule and one reward listed.
   :highlight: The "Add" links for rules and rewards (red frame).
   :data: Rule: 1 point per 1.00 spent; reward: 10% discount for 50 points.
   :module: loyalty
   :notes: English UI, light theme, 1440px width, crop to the notebook.

.. note::
   The options for :guilabel:`Conditional rules` vary depending on the selected :ref:`Program Type
   <sales/pricing_management/program-types>`.

The following options are available for configuring conditional rules:

- :guilabel:`Discount Code`: Enter a custom code to be used for the :guilabel:`Discount Code`
  program, or use the default one generated by Odoo. This field is only available when the
  :guilabel:`Program Type` is set to :guilabel:`Discount Code`.
- :guilabel:`Minimum Quantity`: Enter the minimum number of products that must be purchased in order
  to access the reward. Set the minimum quantity to at least `1` to ensure that the customer must
  make a purchase in order to access the reward.
- :guilabel:`Minimum Purchase`: Enter the minimum amount (in currency), with :guilabel:`tax
  Included` or :guilabel:`tax Excluded`, that must be spent in order to access the reward. If both a
  minimum quantity *and* minimum purchase amount are entered, then the customer's order must meet
  both conditions.
- :guilabel:`Products`: Select the specific product(s) for which the program applies. Leave this
  field blank to apply it to all products.
- :guilabel:`Categories`: Select the category of products for which the program applies. Choose
  :guilabel:`All` to apply it to all product categories.
- :guilabel:`Product Tag:` Select a tag to apply the program to products with that specific tag.
- :guilabel:`Grant`: Enter the number of points the customer earns :guilabel:`per order`,
  :guilabel:`per currency spent`, or :guilabel:`per unit paid` (for the :guilabel:`Loyalty Cards`
  and :guilabel:`Buy X Get Y` programs).

.. screenshot:: sales-loyalty-rule-popup
   :menu: Sales ‣ Products ‣ Discount & Loyalty ‣ (a program) ‣ Rules & Rewards ‣ (a rule)
   :shows: The conditional-rule pop-up with the Discount Code, Minimum Quantity, Minimum Purchase, Products/Categories and "Grant" fields.
   :highlight: The Grant fields (red frame).
   :data: Minimum purchase 100.00, grant 1 point per 1.00.
   :module: loyalty
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

Click :guilabel:`Save & Close` to save the rule and close the pop-up window, or click
:guilabel:`Save & New` to save the rule and immediately create a new one.

Rewards
-------

In the :guilabel:`Rules & Rewards` tab of the program form, click :guilabel:`Add` next to
:guilabel:`Rewards` to add *rewards* to the program. This reveals a :guilabel:`Create Rewards`
pop-up window.

.. note::
   The options for :guilabel:`Rewards` vary depending on the selected :ref:`Program Type
   <sales/pricing_management/program-types>`.

The following options are available for configuring rewards:

- :guilabel:`Reward Type`: Select the reward type among :guilabel:`Free Product`,
  :guilabel:`Discount`, and :guilabel:`Free Shipping`. The other options for reward configuration
  depend on the :guilabel:`Reward Type` selected.

  - :guilabel:`Free Product`:

    - :guilabel:`Quantity Rewarded`: Select the number of free products rewarded to the customer.
    - :guilabel:`Product`: Select the product given for free as a reward. Only one product can be
      selected.
    - :guilabel:`Product Tag`: Select a tag to further specify the free product eligible for the
      reward.

  - :guilabel:`Discount`:

    - :guilabel:`Discount`: Enter the discounted amount in either :guilabel:`percentage`,
      :guilabel:`currency per point`, or :guilabel:`currency per order`. Then, select whether the
      discount applies to the entire :guilabel:`Order`, only the :guilabel:`Cheapest Product` on the
      order, or only :guilabel:`Specific Products`.
    - :guilabel:`Max Discount`: Enter the maximum amount (in currency) that this reward may grant as
      a discount. Leave this field at `0` for no limit.

  - :guilabel:`Free Shipping`:

    - :guilabel:`Max Discount`: Enter the maximum amount (in currency) that this reward may grant as
      a discount. Leave this field at `0` for no limit.

- :guilabel:`In exchange of`: Enter the number of points required to exchange for the reward (for
  the :guilabel:`Loyalty Cards` and :guilabel:`Buy X Get Y` programs).
- :guilabel:`Description on order`: Enter the description of the reward, which is displayed to the
  customer upon checkout.

.. screenshot:: sales-loyalty-reward-popup
   :menu: Sales ‣ Products ‣ Discount & Loyalty ‣ (a program) ‣ Rules & Rewards ‣ (a reward)
   :shows: The reward pop-up with the Reward Type (Free Product, Discount, Free Shipping), the discount value and the cost in points.
   :highlight: The Reward Type field (red frame).
   :data: Discount of 10% on the order, 50 points.
   :module: loyalty
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

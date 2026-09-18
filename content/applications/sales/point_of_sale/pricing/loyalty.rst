================
Loyalty programs
================

Encourage your customers to keep shopping at your point of sale with **loyalty and promotion
programs**. Odoo supports several program types, all of them usable directly from the POS
interface.

Configuration
=============

#. Go to the :ref:`POS settings <configuration/settings>` and scroll down to the
   :guilabel:`Pricing` section.
#. Enable :guilabel:`Promotions, Coupons, Gift Card & Loyalty Program`.
#. Click :guilabel:`Save`.

.. screenshot:: pos-loyalty-setting
   :menu: Point of Sale ‣ Configuration ‣ Settings
   :shows: The "Pricing" section of the POS settings with the "Promotions, Coupons, Gift Card &
      Loyalty Program" option enabled.
   :highlight: The "Promotions, Coupons, Gift Card & Loyalty Program" setting (red frame).
   :module: point_of_sale, loyalty, pos_loyalty
   :notes: English UI, light theme, 1440px width, crop to the settings block.

Two menus are then available under :menuselection:`Point of Sale --> Products`:

- :guilabel:`Discount & Loyalty` for :guilabel:`Coupons`, :guilabel:`Promotions`,
  :guilabel:`Loyalty Cards`, :guilabel:`Discount Code`, :guilabel:`Buy X Get Y`, and
  :guilabel:`Next Order Coupons` programs;
- :guilabel:`Gift cards & eWallet` for :guilabel:`Gift Card` and :guilabel:`eWallet` programs.

.. note::
   Both menus are only visible to users with the :guilabel:`Point of Sale` access right set to
   :guilabel:`Administrator`.

Create a program
================

#. Go to :menuselection:`Point of Sale --> Products --> Discount & Loyalty` and click
   :guilabel:`New`.
#. Name the program and select its :guilabel:`Program Type`.
#. Restrict the program with the :guilabel:`Start Date`, :guilabel:`End date`, and
   :guilabel:`Limit Usage` fields, and select the points of sale it applies to in the
   :guilabel:`Point of Sale` field. Leave that field empty to make the program available in every
   POS.
#. On the :guilabel:`Rules & Rewards` tab, define the conditions to earn points
   (:guilabel:`Rules`) and what customers get in exchange (:guilabel:`Rewards`): a discount in
   percent or in currency, or a free product.

.. screenshot:: pos-loyalty-program-form
   :menu: Point of Sale ‣ Products ‣ Discount & Loyalty ‣ New
   :shows: A loyalty program form with "Program Type" set to "Loyalty Cards", a validity period,
      and the "Rules & Rewards" tab showing one rule and one reward.
   :data: Program "Loyalty Card", rule "1 point per 1 EUR spent", reward "10 % discount for 100
      points".
   :module: loyalty, pos_loyalty
   :notes: English UI, light theme, 1440px width.

.. seealso::
   :doc:`../../sales/products_prices/loyalty_discount`

Use a program in the POS
========================

Once a customer is set on the order, the points they earn with the transaction are displayed in the
cart and accumulate until they are spent. To redeem them, click the :guilabel:`Reward` button and
select one of the rewards the customer is entitled to according to the program's rules.

.. screenshot:: pos-loyalty-reward-in-pos
   :menu: (POS interface) ‣ Register screen
   :shows: The POS cart with a customer selected, the loyalty points earned shown below the
      customer, and the "Reward" button in the button bar.
   :highlight: The loyalty points counter and the "Reward" button (red frame).
   :module: point_of_sale, pos_loyalty
   :notes: English UI, light theme, 1440px width, crop to the cart pane.

The order total is updated instantly to reflect the reward, and the order can be paid as usual.

.. note::
   Gift cards and eWallets are used as :doc:`payment methods <../payment_methods>` on the payment
   screen, not as rewards.

=====================
Ordering and checkout
=====================

Odoo eCommerce provides several options to organize the ordering and checkout process. It offers
different :ref:`order button <ecommerce/checkout/order-buttons>` options and sequential
:ref:`checkout steps <ecommerce/checkout/steps>`, some of which support additional features. The
related buttons and checkout pages can be customized using the website editor.

.. _ecommerce/checkout/order-buttons:

Order buttons
=============

To customize the ordering process in Odoo eCommerce, you can:

- change the :ref:`Add to Cart <ecommerce/checkout/add-to-cart>` button's behavior,
- replace it with a :ref:`customized <ecommerce/checkout/prevent-sale>` button,
- add a :ref:`Buy now <ecommerce/checkout/buy-now>` button, and
- add an :ref:`Order again <ecommerce/checkout/re-order>` button to the customer portal.

.. _ecommerce/checkout/add-to-cart:

Add to cart options
-------------------

Default add to cart behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When clicking the :guilabel:`Add to cart` button, different actions can be triggered. To configure
them, go to :menuselection:`Website --> Configuration --> Settings`, scroll down to the
:guilabel:`Shop - Checkout Process` section, and select one of the following options:

- :guilabel:`Stay on Product Page`: The customer remains on the product's page.
- :guilabel:`Go to cart`: The customer is immediately redirected to the cart.
- :guilabel:`Let the user decide (dialog)`: The customer can choose if they want to go to the cart
  (:guilabel:`Proceed to Checkout`) or if they prefer to stay on the product page
  (:guilabel:`Continue Shopping`).

.. note::
   This dialog box always appears regardless of the configuration to suggest :doc:`optional products
   <products/cross_upselling>`, if any.

.. _ecommerce/checkout/prevent-sale:

Button customization
~~~~~~~~~~~~~~~~~~~~

You can replace the :guilabel:`Add to Cart` button with a :guilabel:`Contact Us` button, which
redirects users to the default contact form.

.. note::
   Removing the ability to add products to the cart is often used by businesses that want to display
   an online catalog but cannot share prices publicly (e.g., to offer custom or variable pricing).

To display the :guilabel:`Contact Us` button and a note saying `Not Available For Sale` , you need
to :ref:`hide your prices <ecommerce/prices/hide-prices>` on your product page.

.. screenshot:: ecommerce-checkout-cart-contact-us
   :menu: (website) ‣ Shop ‣ (product)
   :shows: A product page where the Add to Cart button is replaced by a Contact Us button.
   :highlight: The Contact Us button (red frame).
   :data: Demo website 'My Website' with the eCommerce demo products.
   :module: website_sale
   :notes: English UI, light theme, 1440px width.

.. note::
   The :guilabel:`Contact Us` button label, URL, and the *Not Available For Sale* text beneath the
   product title and description can be modified on the product's page while in :guilabel:`Edit`
   mode.

Additional add to cart buttons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add additional :guilabel:`Add to Cart` buttons and link them to specific products on any
website page.

To add them, open the website editor and place the :guilabel:`Add to Cart Button` inner content
building block. Once placed, click the button, scroll to the :guilabel:`Add to Cart Button`
section, and configure the following:

- :guilabel:`Product`: Select the product to link the button with.
- :guilabel:`Action`: Choose if it should be an :guilabel:`Add to Cart` or :ref:`Buy Now
  <ecommerce/checkout/buy-now>` button.

.. note::
   - If the product has variants, either choose one or leave the option on :guilabel:`Visitor's
     Choice`, which prompts the customer to select a variant and then to :guilabel:`Proceed to
     Checkout` or :guilabel:`Continue Shopping`.
   - The default :guilabel:`Add to Cart` button does not offer those options, but its label can be
     changed.

.. tip::
   While in :guilabel:`Edit` mode, it is also possible to show or hide the :icon:`fa-shopping-cart`
   (:guilabel:`cart`) icon in the page's header. Click the header and then the
   :icon:`fa-shopping-cart` (:guilabel:`cart`) button next to the :guilabel:`Show Empty` option
   under the :guilabel:`Customize` tab.

.. _ecommerce/checkout/buy-now:

Buy now
-------

To let customers choose to go to the :ref:`review order <ecommerce/checkout/review_order>` step
directly, you can add an additional :guilabel:`Buy now` button. To do so, go to
:menuselection:`Website --> Configuration --> Settings`. Under the :guilabel:`Shop - Checkout
Process` section, tick the :guilabel:`Buy Now` feature.

.. tip::
   Alternatively, enable the feature by going to any product's page while in :guilabel:`Edit` mode
   and, in the :guilabel:`Customize` tab, clicking the :icon:`fa-bolt` :guilabel:`Buy Now` button
   next to the :guilabel:`Cart` options.

.. screenshot:: ecommerce-checkout-cart-buy-now
   :menu: (website) ‣ Shop ‣ (product)
   :shows: A product page with both the Add to Cart and the Buy Now buttons.
   :highlight: The Buy Now button (red frame).
   :data: Demo website 'My Website' with the eCommerce demo products.
   :module: website_sale
   :notes: English UI, light theme, 1440px width.

.. _ecommerce/checkout/re-order:

Re-order from portal
--------------------

You can let customers re-order items from previous sales orders from their customer portal using the
:guilabel:`Order Again` button. To add it, go to :menuselection:`Website --> Configuration -->
Settings`. Under the :guilabel:`Shop - Checkout Process` section, tick the :guilabel:`Re-order From
Portal` feature.

.. screenshot:: ecommerce-checkout-order-again-button
   :menu: (website) ‣ My Account ‣ Orders ‣ (order)
   :shows: A confirmed order in the customer portal with the Order Again button.
   :highlight: The Order Again button (red frame).
   :data: One confirmed order with three lines.
   :module: website_sale
   :notes: English UI, light theme, 1440px width.

.. _ecommerce/checkout/steps:

Checkout steps
==============

During the checkout process, customers are taken through the following steps:

- :ref:`Review order <ecommerce/checkout/review_order>`
- :ref:`Delivery <ecommerce/checkout/delivery>`
- :ref:`Extra info (if enabled) <ecommerce/checkout/extra_step>`
- :ref:`Payment <ecommerce/checkout/payment>`
- :ref:`Order confirmation <ecommerce/checkout/order_confirmation>`

.. _ecommerce/checkout/customize_steps:

Each step can be customized using the website editor by adding :doc:`building blocks
<../website/web_design/building_blocks>` or opening the :guilabel:`Customize` tab to enable various
checkout options.

.. note::
   Content added through building blocks is **specific** to each step.

.. tip::
   Restrict access to the :ref:`shop <ecommerce/customer_accounts/shop-access>` and :ref:`checkout
   <ecommerce/customer_accounts/checkout-access>` for specific customers, e.g., in a :doc:`B2B
   <b2b_b2c>` business setup.

.. _ecommerce/checkout/review_order:

Review order
------------

The :guilabel:`Review Order` step allows customers to see the items they added to their cart, adjust
quantities, or :guilabel:`Remove` products. Information related to the product prices and taxes
applied are also displayed. Customers can then click the :guilabel:`Checkout` button to continue to
the :ref:`Delivery <ecommerce/checkout/delivery>` step.

Open the website editor to :ref:`enable <ecommerce/checkout/customize_steps>` checkout options such
as:

- :guilabel:`Suggested Accessories`: to showcase :ref:`accessory products
  <ecommerce/cross_upselling/accessory>`;
- :guilabel:`Promo Code`: to allow customers to redeem :ref:`gift cards <ewallet_gift/gift-cards>`
  or apply :doc:`discount codes <../../sales/sales/products_prices/loyalty_discount>`;
- :guilabel:`Add to Wishlist`: :ref:`Enable wishlists <ecommerce/products/wishlists>` to allow
  signed-in users to remove a product from their cart and add it to their wishlist using the
  :guilabel:`Save for later` option.

.. note::
   - If a :doc:`fiscal position <../../finance/accounting/taxes/fiscal_positions>` is detected
     automatically, the product tax is determined based on the customer's IP address.
   - If the installed :doc:`payment provider <../../finance/payment_providers>` supports
     :ref:`express checkout <payment_providers/express_checkout>`, a dedicated button is displayed,
     allowing customers to go straight from the cart to the confirmation page without filling out
     the contact form.

.. _ecommerce/checkout/delivery:

Delivery
--------

Once they have reviewed their order:

- Unsigned-in customers are prompted to :guilabel:`Sign in` or enter their :guilabel:`Email
  address`, along with their delivery address and phone details;
- Signed-in customers can select the appropriate :guilabel:`Delivery address`.

They can then :doc:`choose a delivery method <shipping>`, select or enter their :guilabel:`Billing
Address` (or toggle the :guilabel:`Same as delivery address` switch if the billing and delivery
addresses are identical), and click :guilabel:`Confirm` to proceed to the next step.

.. tip::
   - For B2B customers, you can also :ref:`enable <ecommerce/checkout/customize_steps>` optional
     :ref:`B2B fields <ecommerce/b2b_b2c/b2b-fields>` in the website editor.
   - You can add a checkbox for users without an account to sign up for a newsletter. To do so, go
     to :menuselection:`Website --> Configuration --> Settings`. Under the :guilabel:`Shop -
     Checkout Process` section, enable the :guilabel:`Newsletter` feature and select a
     :guilabel:`Newsletter List`.

.. _ecommerce/checkout/extra_step:

Extra info
----------

You can add an :guilabel:`Extra Info` step in the checkout process to collect additional customer
information through an online form, which is then included in the :ref:`sales order
<handling/sales>`. To do so, :ref:`enable <ecommerce/checkout/customize_steps>` the :guilabel:`Extra
Step` option in the website editor. The form can be :ref:`customized <website/building_blocks/form>`
as needed.

.. tip::
   Alternatively, go to :menuselection:`Website --> Configuration --> Settings`, scroll to the
   :guilabel:`Shop - Checkout Process` section, enable :guilabel:`Extra Step During Checkout`, and
   click :guilabel:`Save`. Click :icon:`fa-arrow-right` :guilabel:`Configure Form` to customize it.

.. _ecommerce/checkout/payment:

Payment
-------

At the :guilabel:`Payment` step, customers :guilabel:`Choose a payment method`, enter their payment
details, and click :guilabel:`Pay now`.

You can require customers to agree to your :doc:`terms and conditions
<../../finance/accounting/customer_invoices/terms_conditions>` before payment. To :ref:`enable
<ecommerce/checkout/customize_steps>` this option, go to the website editor and toggle the
:guilabel:`Accept Terms & Conditions` feature.

.. tip::
   Enable the :ref:`developer mode <developer-mode>` and click the :icon:`fa-bug` (:guilabel:`bug`)
   icon to display an :ref:`availability <payment_providers/availability>` report for payment
   providers and payment methods, which helps diagnose potential availability issues on the payment
   form.

.. _ecommerce/checkout/customer-type:

Private person or company
-------------------------

The *Website Sale Partner Type* module (`website_sale_partner_type`) adds a :guilabel:`Private
Person` / :guilabel:`Company` choice at the top of the address step for visitors who are not logged
in. The choice sets the contact's :guilabel:`Company Type`, and the address form adapts to it: the
company name and tax ID fields are only required for companies.

Together with the Hungarian localization, the form also switches between the international
:guilabel:`VAT` field and the Hungarian tax number field depending on the selected
:guilabel:`Country`, and the B2B fields are always shown.

.. screenshot:: ecommerce-checkout-customer-type
   :menu: (website) ‣ Checkout ‣ Address
   :shows: The checkout address form of an anonymous visitor with the Private Person / Company radio buttons above the name field, and the company and tax number fields shown for the Company choice.
   :highlight: The Private Person / Company radio buttons (red frame).
   :data: Company selected, country Hungary, Hungarian tax number field visible.
   :module: website_sale_partner_type
   :notes: English UI, light theme, 1440px width, crop to the top of the address form.

When the visitor fills in a company name, the *Website Sale Company* module
(`website_sale_company`) automatically creates the company contact and links the ordering person to
it as a child contact, so that the order is placed on behalf of the company.

.. _ecommerce/checkout/order-signature:

Signing the order
-----------------

The *Website Sale Order Sign* module (`website_sale_order_sign`) requires customers to accept and
sign the order before they can pay. At the :guilabel:`Payment` step, an :guilabel:`Accept & Sign`
button is displayed instead of the payment button; clicking it opens a dialog with the order summary
and the signature field. Once the order is signed, the payment button appears and the signature and
signing date are stored on the sales order.

.. screenshot:: ecommerce-checkout-accept-and-sign
   :menu: (website) ‣ Checkout ‣ Payment
   :shows: The payment step of the checkout with the Accept & Sign button in place of the payment button, and the signature dialog opened over it.
   :highlight: The Accept & Sign button and the signature field (red frame).
   :data: One cart of about EUR 150.
   :module: website_sale_order_sign
   :notes: English UI, light theme, 1440px width.

.. _ecommerce/checkout/order_confirmation:

Order confirmation
------------------

The final step of the checkout process is the :guilabel:`Order confirmation`, which provides a
summary of the customer's purchase details.

.. seealso::
   :doc:`Order handling documentation <order_handling>`

=================
Payment providers
=================

Odoo supports a multitude of online
:doc:`payment providers </applications/finance/payment_providers>` for your website, allowing your
customers to pay with their preferred payment methods.

.. seealso::
   - :doc:`/applications/sales/sales/products_prices/ewallets_giftcards`
   - :doc:`checkout`

Configuration
=============

To set up payment providers on the eCommerce app, go to :menuselection:`Website --> Configuration
--> Payment Providers`. From here, :guilabel:`Activate` the payment providers you wish to have
available on your shop, and configure them according to your needs.

Alternatively, you can access **payment providers** via :menuselection:`Website --> Configuration
--> Settings`. In the :guilabel:`Shop - Payment` section, you can :guilabel:`Configure SEPA Direct
Debit` if you wish to use it, as well as :guilabel:`View other providers`. If you use the
:guilabel:`Authorize.net` payment provider, the
:ref:`Payment Capture Method <payment_providers/manual_capture>` can be configured in that same menu.

If you are using :doc:`/applications/finance/payment_providers/paypal`, you can also enable and
configure it here.

Checkout payment options
------------------------

Once activated, customers can choose the payment provider of their choice during the **checkout
process**, at the :guilabel:`Confirm Order` step.

.. screenshot:: ecommerce-payments-payments-checkout
   :menu: (website) ‣ Checkout ‣ Payment
   :shows: The payment step of the checkout with the enabled payment providers and payment methods listed as options.
   :highlight: The provider list (red frame).
   :data: Two enabled providers.
   :module: website_sale, payment
   :notes: English UI, light theme, 1440px width.

eWallets and gift cards
=======================

When checking out, customers can pay with an eWallet or gift cards. To enable these, go to
:menuselection:`Website --> Configuration --> Settings`, and in the :guilabel:`Shop-Products`
section, enable :menuselection:`Discounts, Loyalty & Gift Card`.

Once enabled, customers can enter their gift card **code** or pay with their eWallet at the checkout
step.

.. screenshot:: ecommerce-payments-payments-ewallets-giftcards
   :menu: (website) ‣ Checkout ‣ Payment
   :shows: The payment step of the checkout with the gift card / promo code field where the code is entered.
   :highlight: The gift card code field (red frame).
   :data: One gift card of EUR 50.
   :module: website_sale_loyalty
   :notes: English UI, light theme, 1440px width.

.. seealso::
   :doc:`/applications/sales/sales/products_prices/ewallets_giftcards`

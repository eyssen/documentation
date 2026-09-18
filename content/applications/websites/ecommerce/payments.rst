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

.. _ecommerce/payments/fees:

Payment fees
============

The *eCommerce: charge payment fee* module (`website_sale_charge_payment_fee`) makes it possible to
charge the customer a handling fee depending on the payment provider they choose (e.g., a
cash-on-delivery surcharge).

To configure a fee, go to :menuselection:`Website --> Configuration --> Payment Providers`, open a
provider, and use the :guilabel:`Charge payment fee` tab:

- :guilabel:`Charge payment fee`: enables the fee for this provider.
- :guilabel:`Product`: the service product used for the fee line added to the order. Its name is
  shown to the customer, and its taxes and accounts are used for invoicing.
- :guilabel:`Computation type`: :guilabel:`Fixed` or :guilabel:`Percentage`.
- :guilabel:`Fixed Price` and :guilabel:`Fee Currency`: the amount charged for a fixed fee. If the
  fee currency differs from the order's pricelist currency, the amount is converted automatically.
- :guilabel:`Percentage`: the percentage of the order total charged as a fee.

When the customer selects the provider at checkout, a fee line is added to the order and shown in
the order total. Selecting another provider replaces or removes the line.

.. screenshot:: ecommerce-payments-charge-payment-fee
   :menu: Website ‣ Configuration ‣ Payment Providers ‣ (provider) ‣ Charge payment fee tab
   :shows: The Charge payment fee tab of a payment provider with Charge payment fee enabled, a fee product selected, the Computation type set to Fixed and a fixed price entered.
   :highlight: The Charge payment fee checkbox and the Computation type field (red frame).
   :data: Provider "Wire Transfer", fee product "Cash on delivery fee", fixed price EUR 2.
   :module: website_sale_charge_payment_fee
   :notes: English UI, light theme, 1440px width, crop to the tab.

.. note::
   The tab is hidden on providers that allow :guilabel:`express checkout`, because the fee cannot be
   added to the order after the express payment has started.

.. _ecommerce/payments/payment-terms:

Payment terms per payment provider
==================================

The *Website Sale Payment Term* module (`website_sale_payment_term`) links each payment provider to
a payment term. When a payment transaction is created for a sales order — at website checkout or
from the customer portal — the order's :guilabel:`Payment Terms` are set from the selected provider,
and the invoice created from the order inherits the term through the standard flow.

Set the term on the provider itself (:menuselection:`Website --> Configuration --> Payment
Providers`), or review the assignment from the other side: open a payment term under
:menuselection:`Accounting --> Configuration --> Payment Terms`, where the :guilabel:`Payment
Providers` section lists the providers using it.

.. screenshot:: ecommerce-payments-payment-term-providers
   :menu: Accounting ‣ Configuration ‣ Payment Terms ‣ (term)
   :shows: A payment term form with the Payment Providers section listing the providers that use this term, with their Name and State columns.
   :highlight: The Payment Providers section (red frame).
   :data: Payment term "Immediate Payment" used by two providers.
   :module: website_sale_payment_term
   :notes: English UI, light theme, 1440px width, crop to the section.

.. important::
   Every payment provider must have a payment term set. Providers cannot be removed from the list on
   the payment term: change the term on the provider itself instead.

.. _ecommerce/payments/order-payments:

Payments on the sales order
===========================

The *Manage Website Sale Payment* module (`eyssen_website_sale_payment`) adds two read-only fields
below :guilabel:`Payment Terms` on the sales order, so that the payments received for a webshop
order are visible without opening the accounting entries:

- :guilabel:`Payment Transactions`: the payments linked to the order, as tags.
- :guilabel:`Payment Transaction Methods`: the payment methods used, as text.

Both fields are hidden when the order has no payment yet.


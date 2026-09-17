=================================================
B2B (tax excluded) and B2C (tax included) pricing
=================================================

When working with consumers, prices are usually expressed with taxes included in the price (e.g., in
most eCommerce). But, when you work in a B2B environment, companies usually negotiate prices with
taxes excluded.

Odoo manages both use cases easily, as long as you register your prices on the product with taxes
excluded or included, but not both together. If you manage all your prices with tax included (or
excluded) only, you can still easily do sales order with a price having taxes excluded (or included)
: that's easy.

This documentation is only for the specific use case where you need to have two references for the
price (tax included or excluded), for the same product. The reason of the complexity is that there
is not a symmetrical relationship with prices included and prices excluded, as shown in this use
case, in Belgium with a tax of 21%:

-  Your eCommerce has a product at **10€ (taxes included)**

-  This would do **8.26€ (taxes excluded)** and a **tax of 1.74€**

But for the same use case, if you register the price without taxes on the product form (8.26€), you
get a price with tax included at 9.99€, because:

-  **8.26€ \* 1.21 = 9.99€**

So, depending on how you register your prices on the product form, you will have different results
for the price including taxes and the price excluding taxes:

-  Taxes Excluded: **8.26€ & 10.00€**

-  Taxes Included: **8.26€ & 9.99€**

.. note::
  If you buy 100 pieces at 10€ taxes included, it gets even more tricky. You will get: **1000€
  (taxes included) = 826.45€ (price) + 173.55€ (taxes)** Which is very different from a price per
  piece at 8.26€ tax excluded.

This documentation explains how to handle the very specific use case where you need to handle the
two prices (tax excluded and included) on the product form within the same company.

.. note::
  In terms of finance, you have no more revenues selling your product at 10€ instead of 9.99€ (for a
  21% tax), because your revenue will be exactly the same at 9.99€, only the tax is 0.01€ higher.
  So, if you run an eCommerce in Belgium, make your customer a favor and set your price at 9.99€
  instead of 10€. Please note that this does not apply to 20€ or 30€, or other tax rates, or a
  quantity >1. You will also make you a favor since you can manage everything tax excluded, which is
  less error prone and easier for your salespeople.

Configuration
=============

Introduction
------------

The best way to avoid this complexity is to choose only one way of managing your prices and stick to
it: price without taxes or price with taxes included. Define which one is the default stored on the
product form (on the default tax related to the product), and let Odoo compute the other one
automatically, based on the pricelist and fiscal position. Negotiate your contracts with customers
accordingly. This perfectly works out-of-the-box and you have no specific configuration to do.

If you can not do that and if you really negotiate some prices with tax excluded and, for other
customers, others prices with tax included, you must:

#.  always store the default price **tax excluded** on the product form, and apply a tax (price
    excluded on the product form)

#.  create a pricelist with prices in **tax included**, for specific customers

#.  create a fiscal position that switches the tax excluded to a tax included

#.  assign both the pricelist and the fiscal position to customers who want to benefit to this
    pricelist and fiscal position

For the purpose of this documentation, we will use the above use case:

-   your product default sale price is 8.26€ tax excluded

-   but we want to sell it at 10€, tax included, in our shops or eCommerce website

Setting your products
---------------------

Your company must be configured with tax excluded by default. This is usually the default
configuration, but you can check it in :menuselection:`Accounting --> Configuration --> Settings`,
in the :guilabel:`Default Taxes` setting of the :guilabel:`Taxes` section: the :guilabel:`Prices`
field must be set to :guilabel:`Tax Excluded`.

.. screenshot:: accounting-taxes-b2b-b2c-settings
   :menu: Accounting ‣ Configuration ‣ Settings
   :shows: "Taxes" section; "Default Taxes" setting with Sales Tax "21%" and Prices "Tax Excluded".
   :highlight: The "Prices" field (red frame).
   :data: Belgian demo company; default sales tax "21%".
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the Taxes section.

Once done, you can create a **B2C** pricelist. To activate pricelists, go to
:menuselection:`Sales --> Configuration --> Settings`, and enable :guilabel:`Pricelists` in the
:guilabel:`Pricing` section.

Then, create a B2C pricelist from the menu :menuselection:`Sales --> Products --> Pricelists`. It's
also good to rename the default pricelist into B2B to avoid confusion.

Then, create a product at 8.26€, with a tax of 21% (defined as tax not included in price) and set a
price on this product for B2C customers at 10€ in the B2C pricelist, from the
:menuselection:`Sales --> Products --> Products` menu of the Sales application:

.. screenshot:: accounting-taxes-b2b-b2c-pricelist
   :menu: Sales ‣ Products ‣ Pricelists ‣ B2C
   :shows: B2C pricelist form, "Price Rules" tab with one rule: the product at a fixed price of 10.00 €.
   :highlight: The price rule line (red frame).
   :data: Belgian demo company; pricelist "B2C" (EUR); product "Chair" (sales price 8.26 €, tax 21% excluded).
   :module: product, sale
   :notes: English UI, light theme, 1440px width.

Setting the B2C fiscal position
-------------------------------

From the accounting application, create a B2C fiscal position from this menu:
:menuselection:`Accounting --> Configuration --> Fiscal Positions`. This fiscal position should map the VAT 21%
(tax excluded of price) with a VAT 21% (tax included in price)

.. screenshot:: accounting-taxes-b2b-b2c-fiscal-position
   :menu: Accounting ‣ Configuration ‣ Fiscal Positions ‣ B2C
   :shows: B2C fiscal position form, "Tax Mapping" tab: "21%" (tax excluded) mapped to "21% (included)".
   :highlight: The tax mapping line (red frame).
   :data: Belgian demo company; taxes "21%" and "21% (included)".
   :module: account
   :notes: English UI, light theme, 1440px width.

Test by creating a quotation
============================

Create a quotation from the Sale application, using the :menuselection:`Sales --> Quotations` menu.
You should have the following result: 8.26€ + 1.73€ = 9.99€.

.. screenshot:: accounting-taxes-b2b-b2c-quotation-b2b
   :menu: Sales ‣ Orders ‣ Quotations ‣ New
   :shows: Quotation with the default (B2B) pricelist and no fiscal position; one line of the product at 8.26 € + 21% tax; totals 8.26 + 1.73 = 9.99 €.
   :highlight: The totals block (red frame).
   :data: Belgian demo company; product "Chair".
   :module: sale
   :notes: English UI, light theme, 1440px width.

Then, create a quotation but **change the pricelist to B2C and the fiscal position to B2C** on the
quotation, before adding your product. You should have the expected result, which is a total price
of 10€ for the customer: 8.26€ + 1.74€ = 10.00€.

.. screenshot:: accounting-taxes-b2b-b2c-quotation-b2c
   :menu: Sales ‣ Orders ‣ Quotations ‣ New
   :shows: Quotation with the "B2C" pricelist and the "B2C" fiscal position; one line of the product at 10.00 € with tax "21% (included)"; totals 8.26 + 1.74 = 10.00 €.
   :highlight: The Pricelist and Fiscal Position fields and the totals block (red frames).
   :data: Belgian demo company; product "Chair".
   :module: sale
   :notes: English UI, light theme, 1440px width.

This is the expected behavior for a customer of your shop.

Avoid changing every sale order
===============================

If you negotiate a contract with a customer, whether you negotiate tax included or tax excluded, you
can set the pricelist and the fiscal position on the customer form so that it will be applied
automatically at every sale of this customer.

The pricelist (:guilabel:`Pricelist` field) is in the :guilabel:`Sales & Purchase` tab of the
customer form, and the fiscal position (:guilabel:`Fiscal Position` field) is in the same tab, in
the :guilabel:`Fiscal Information` section.

Note that this is error prone: if you set a fiscal position with tax included in prices but use a
pricelist that is not included, you might have wrong prices calculated for you. That's why we
usually recommend companies to only work with one price reference.

==============
Order handling
==============

When a customer orders on your eCommerce, there are **three** record types required to be handle in
Odoo:

- :ref:`Sales orders <handling/sales>`;
- :ref:`Delivery orders <handling/delivery>`;
- :ref:`Invoices & legal requirements <handling/legal>`.

.. _handling/sales:

Sales orders
============

Order and payment status
------------------------

The first step when a customer adds a product to his cart is the creation of a quotation. Orders can
be managed either from the **Website** or :doc:`Sales </applications/sales/sales>` app. eCommerce
orders can automatically be assigned to a specific sales team by going to :menuselection:`Website
--> Configuration --> Settings`. In the **Shop - Checkout Process** section, select a
:guilabel:`Sales Team` or :guilabel:`Salesperson` to handle eCommerce orders.

.. screenshot:: ecommerce-order_handling-handling-salesteam
   :menu: Website ‣ Configuration ‣ Settings
   :shows: The Website settings page with the Sales Team and Salesperson fields of the website filled in.
   :highlight: The Sales Team and Salesperson fields (red frame).
   :data: Demo website 'My Website' with the eCommerce demo products.
   :module: website_sale
   :notes: English UI, light theme, 1440px width.

Orders can be found under :menuselection:`Website --> eCommerce --> Orders/Unpaid Orders`. Each
order goes through a different status:

- **Quotation**: a new product is added to the cart, but the customer has *not* gone through the
  checkout process yet;
- **Quotation sent**: the customer has gone through the checkout process and confirmed the order,
  but the payment is not yet confirmed;
- **Order**: the customer has gone through the checkout process, confirmed the order, and the
  payment is received.

.. screenshot:: ecommerce-order_handling-handling-status
   :menu: Website ‣ eCommerce ‣ Orders
   :shows: The eCommerce orders list with the Order, Customer, Date, Total and Status columns, showing both quotations (abandoned carts) and confirmed orders.
   :highlight: The Status column (red frame).
   :data: Five orders in different statuses.
   :module: website_sale
   :notes: English UI, light theme, 1440px width.

.. _handling/manual-confirmation:

Manual confirmation of paid orders
----------------------------------

By default, a webshop order is confirmed automatically as soon as the online payment succeeds. The
*Disable auto confirm for payed orders* module (`eyssen_website_sale_disable_auto_confirm`) keeps
paid webshop orders in the **Quotation sent** status instead, so that a salesperson reviews them —
stock, delivery date, customer data — before the order is confirmed and the delivery order is
created.

.. warning::
   While this module is installed, webshop orders cannot be confirmed with the
   :guilabel:`Confirm` button either: the button only moves the order to **Quotation sent**. See
   the open questions in the project notes.

Abandoned cart
--------------

An **abandoned cart** represents an order for which the customer did **not finish** the checkout
confirmation process. For these orders, it is possible to send an **email reminder** to the
customer automatically. To enable that feature, go to :menuselection:`Website --> Configuration -->
Settings` and in the :guilabel:`Email & Marketing` section, enable :guilabel:`Automatically send
abandoned checkout emails`. Once enabled, you can set the **time-lapse** after which the email is
sent and customize the **email template** used.

.. note::
   For abandoned cart emails, the customer must either have entered their contact details during the
   checkout process; or be logged-in when they added the product to their cart.

.. _handling/delivery:

Delivery orders
===============

Delivery flow
-------------

Once a quotation has been confirmed, a delivery order is automatically created. The next step is to
process this delivery.

Packing eCommerce orders usually requires picking the product, preparing the packaging, printing the
shipping label(s) and shipping to the customer. Depending on the number of orders, strategy, or
resources, those steps can be considered as one or multiple actions in Odoo.

An automatic email can be sent to the customer when the transfer status in Odoo is “done”. To do so,
enable the feature in the settings of the
:doc:`Inventory </applications/inventory_and_mrp/inventory>` app.

.. note::
   If customers are allowed to pay when picking up their order in stores or by wire transfer, the
   quotation is **not** be confirmed and the stock is **not** be reserved. Orders must be confirmed
   manually to reserve products in stock.

.. seealso::
   - :doc:`../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/invoicing`
   - :doc:`../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/labels`
   - :doc:`../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/multipack`

Returns and refunds
-------------------

Full refunds can be directly sent to customers from within the order interface. A refund-compatible
payment provider needs to be enabled first.

.. _handling/portal-rma:

Return requests from the portal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The *RMA - Website Portal* module (`eyssen_rma_website_sale`) lets customers request a return
themselves from their customer portal, without contacting the sales team.

On a confirmed order in :menuselection:`My Account --> Orders`, a :guilabel:`Request RMA` button
opens the return request form, which lists the order lines that can still be returned. For each
line, the customer selects the quantity, picks a :guilabel:`Reason` from the reasons published for
the portal, and — for tracked products — selects the serial or lot numbers actually delivered to
them. Only the delivered quantity that has not been returned or requested yet can be selected.

.. screenshot:: ecommerce-order_handling-portal-request-rma
   :menu: (website) ‣ My Account ‣ Orders ‣ (order) ‣ Request RMA
   :shows: The portal return request form with the returnable order lines, the quantity selectors, the Reason drop-down menus and the serial/lot selection on a tracked line.
   :highlight: The Reason column and the quantity selectors (red frame).
   :data: One confirmed order with three delivered lines, one of them serial-tracked.
   :module: eyssen_rma_website_sale
   :notes: English UI, light theme, 1440px width.

Once submitted, the request creates an RMA in the back end, where the sales team processes it. The
customer follows its status under :menuselection:`My Account --> Returns (RMA)`, which lists the
return requests together with the :doc:`withdrawal declarations
</applications/sales/withdrawal/consumer_portal>`.

.. screenshot:: ecommerce-order_handling-portal-rma-list
   :menu: (website) ‣ My Account ‣ Returns (RMA)
   :shows: The portal list of return requests with their reference, date, status and the related order.
   :highlight: The status column (red frame).
   :data: Two return requests in different statuses.
   :module: eyssen_rma_website_sale
   :notes: English UI, light theme, 1440px width.

.. note::
   The reasons offered on the portal are the RMA reasons published for the portal. Configure them
   in :menuselection:`Sales --> Configuration --> RMA --> Reasons`.

.. seealso::
   - :doc:`/applications/sales/sales/products_prices/returns`
   - :doc:`/applications/sales/withdrawal`
   - :doc:`/applications/finance/payment_providers`

.. _handling/legal:

Invoice and legal requirements
==============================

The final step of an ecommerce order is to generate the invoice and send it to the customer.
Depending on your needs, an invoice can either be generated automatically or on demand of the
customer. This process can be automated if (and when) the online payment is :ref:`confirmed
<handling/sales>`.

To automate invoicing, go to :menuselection:`Website --> Configuration --> Settings` and in the
:guilabel:`Invoicing` section, enable :guilabel:`Automatic Invoice`.

.. _handling/invoicing-journal:

Invoicing journal per website
-----------------------------

With several webshops in the same database, each website can invoice in its own sales journal. The
*Website Sale Invoicing Journal* module (`eyssen_website_sale_journal`) adds an
:guilabel:`Invoicing Journal` field to the website configuration
(:menuselection:`Website --> Configuration --> Settings`). Orders placed on that website get the
journal filled in automatically, and their invoices inherit it through the standard flow.

.. screenshot:: ecommerce-order_handling-website-invoicing-journal
   :menu: Website ‣ Configuration ‣ Settings
   :shows: The Website settings page with the Invoicing Journal field of the website set to a sales journal.
   :highlight: The Invoicing Journal field (red frame).
   :data: Website "My Website" with the journal "Webshop sales".
   :module: eyssen_website_sale_journal
   :notes: English UI, light theme, 1440px width, crop to the Invoicing section.

======================
Marketplace connectors
======================

Besides the Odoo webshop, products can also be sold on an external webshop platform. The eYssen
connectors keep such a platform and Odoo in sync, so that the catalog, the stock and the orders stay
in one place — Odoo — while the storefront runs elsewhere.

Two connectors are available:

- :ref:`Shopify <ecommerce/connectors/shopify>` (`shopify`)
- :ref:`Unas <ecommerce/connectors/unas>` (`unas`)

.. note::
   Both connectors run their synchronization in the background. If a synchronization seems stuck,
   check the job queue with your system administrator before re-running it manually.

.. _ecommerce/connectors/shopify:

Shopify
=======

The *eYssen Shopify Connector* module (`shopify`) synchronizes products, stock, orders and
fulfillments with a Shopify shop:

- **Products**: Odoo → Shopify;
- **Stock**: Odoo → Shopify;
- **Orders**: Shopify → Odoo, through webhooks, so that new orders arrive immediately;
- **Fulfillments**: Odoo → Shopify, when the delivery is validated in Odoo;
- **Static objects**: shipping methods, payment methods, warehouses/locations and tax rates, so
  that the Shopify values are mapped to the matching Odoo records.

Configuration
-------------

The connection is configured per company. Go to :menuselection:`Settings --> Users & Companies -->
Companies`, open the company, and fill in the Shopify section:

- :guilabel:`Enable Shopify`: activates the integration for this company.
- :guilabel:`Shopify Shop URL`: the shop's address, e.g., `myshop.myshopify.com`.
- :guilabel:`Client ID` and :guilabel:`Client Secret`: the credentials of the custom app created in
  the Shopify admin.
- :guilabel:`Webhook Signing Secret`: the API secret key used to verify incoming webhooks.
- :guilabel:`API Version`: the Shopify API version used.

The :guilabel:`Admin API Access Token` and its expiry date are filled in and refreshed
automatically; the :guilabel:`Last ... Sync Date` fields show when each synchronization last ran.

.. screenshot:: ecommerce-connectors-shopify-company-settings
   :menu: Settings ‣ Users & Companies ‣ Companies ‣ (company)
   :shows: The Shopify section of a company form with Enable Shopify checked, the shop URL, the client ID and secret, the webhook signing secret, the API version and the last synchronization dates.
   :highlight: The Enable Shopify checkbox and the shop URL (red frame).
   :data: Shop "myshop.myshopify.com"; use throw-away credentials.
   :module: shopify
   :notes: English UI, light theme, 1440px width, crop to the Shopify section.

Mapping
-------

Before the first synchronization, map the Shopify values to the Odoo records under
:menuselection:`Shopify --> Configuration`:

- :guilabel:`Shipping Methods`: each Shopify shipping option to an Odoo delivery method;
- :guilabel:`Payment Methods`: each Shopify payment gateway to an Odoo payment method;
- :guilabel:`Warehouses/Locations`: each Shopify location to an Odoo warehouse, so that the stock
  published to Shopify comes from the right warehouse;
- :guilabel:`Tax Rates`: each Shopify tax rate to an Odoo tax.

.. screenshot:: ecommerce-connectors-shopify-configuration-menu
   :menu: Shopify ‣ Configuration
   :shows: The Shopify Configuration menu opened, showing the Shipping Methods, Payment Methods, Warehouses/Locations and Tax Rates entries.
   :highlight: The Configuration menu entries (red frame).
   :data: Demo company "YourCompany".
   :module: shopify
   :notes: English UI, light theme, 1440px width.

Products
--------

Products are published to Shopify from Odoo. On the product form, the connector adds:

- :guilabel:`Sync to Shopify`: whether this product is published;
- :guilabel:`Shopify Status`: the state of the product on Shopify;
- :guilabel:`Shopify ID` and :guilabel:`Shopify Variant ID`: the identifiers on the Shopify side,
  filled in automatically;
- :guilabel:`Last Sync Date`.

Pricelists can also be marked for Shopify, so that the prices published to the shop come from a
dedicated pricelist.

Orders
------

Incoming orders are listed under :menuselection:`Shopify --> Orders --> Orders`, together with the
sales order created for each of them. :menuselection:`Shopify --> Orders --> Sync Orders from
Shopify` fetches the orders manually, which is useful after a connection problem: normally, orders
arrive through webhooks without any action.

.. screenshot:: ecommerce-connectors-shopify-orders
   :menu: Shopify ‣ Orders ‣ Orders
   :shows: The list of Shopify orders with the Shopify order number, the date, the customer, the amount, the status and the related Odoo sales order.
   :highlight: The related sales order column (red frame).
   :data: Five imported Shopify orders.
   :module: shopify
   :notes: English UI, light theme, 1440px width.

.. _ecommerce/connectors/unas:

Unas
====

The *eYssen Unas Connector* module (`unas`) synchronizes an Unas webshop with Odoo: products,
customers and orders, together with the shipping and payment method mapping.

Configuration
-------------

Go to :menuselection:`Settings --> General Settings`, in the :guilabel:`Unas` section:

- :guilabel:`Unas Enable`: activates the integration for the current company;
- :guilabel:`Unas API Key`: the API key of the Unas shop.

The access token and its expiry are obtained and refreshed automatically from the API key, and the
last synchronization dates of the products, the partners and the orders are stored on the company.

.. screenshot:: ecommerce-connectors-unas-settings
   :menu: Settings ‣ General Settings
   :shows: The Unas section of the general settings with Unas Enable checked and the API key filled in.
   :highlight: The Unas Enable checkbox and the API key field (red frame).
   :data: Use a throw-away API key.
   :module: unas
   :notes: English UI, light theme, 1440px width, crop to the Unas section.

Mapping
-------

Unas identifies its records by its own IDs, which the connector stores on the matching Odoo records
as :guilabel:`Unas ID`: on products, on contacts, on sales orders, on delivery methods and on
payment terms. Fill in the :guilabel:`Unas ID` of the delivery methods and the payment terms once,
so that imported orders get the right shipping and payment conditions.

Synchronization queue
---------------------

Every exchange goes through a queue, visible under :menuselection:`Unas Connector --> Sync Queue`.
Each job shows:

- :guilabel:`Type`: :guilabel:`Product`, :guilabel:`Partner`, :guilabel:`Order`,
  :guilabel:`Payment Method` or :guilabel:`Shipping Method`;
- :guilabel:`State`: :guilabel:`Draft`, :guilabel:`Done` or :guilabel:`Error`;
- the :guilabel:`Payload` sent, the :guilabel:`Response` received and, on failure, the
  :guilabel:`Error Message`.

A failed job can be retried from the job itself, once the cause of the error is fixed.

.. screenshot:: ecommerce-connectors-unas-queue
   :menu: Unas Connector ‣ Sync Queue
   :shows: The Unas synchronization queue with the reference, type, state and Unas ID columns, including one job in the Error state.
   :highlight: The State column with the Error job (red frame).
   :data: About ten jobs, one of them failed.
   :module: unas
   :notes: English UI, light theme, 1440px width.

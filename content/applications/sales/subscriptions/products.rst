=====================
Subscription products
=====================

Only products flagged as subscription products can be used on a subscription line.

Flag a product
==============

Open a product in :menuselection:`Sales app --> Products --> Products` (or in
:menuselection:`Inventory app --> Products --> Products`) and tick the :guilabel:`Subscription`
checkbox in the :guilabel:`General Information` tab. A :guilabel:`Subscription` tab then appears on
the product form, and two smart buttons show how many subscription lines use the product: the
active ones and the total.

.. note::
   The :guilabel:`Product` field of a subscription line only offers products with the
   :guilabel:`Subscription` checkbox ticked.

.. screenshot:: sales-subscriptions-product-flag
   :menu: Sales ‣ Products ‣ Products ‣ (a product) ‣ General Information
   :shows: A product form with the "Subscription" checkbox ticked and the two subscription smart buttons in the button box.
   :highlight: The "Subscription" checkbox (red frame).
   :data: Product "Hosting – Standard plan", 12 active subscriptions.
   :module: subscription
   :notes: English UI, light theme, 1440px width, crop to the button box and the checkbox.

The Subscription tab
====================

The :guilabel:`Subscription` tab holds:

- :guilabel:`Subscription Type`: classifies the recurring service. The standard value is
  :guilabel:`General`; additional types are added by the modules that extend the application.
- :guilabel:`Recurring Prices`: the default price per :doc:`billing period <configuration>`. Add one
  line per period — for example a monthly and a yearly price for the same product — with the
  :guilabel:`Period`, the optional :guilabel:`Product Variants` it applies to, the
  :guilabel:`Price` and its :guilabel:`Currency`.

.. example::
   A hosting plan sold both monthly and yearly has two recurring price lines: `Monthly` = `29.00`
   and `Yearly` = `290.00`. When a subscription line for this product is set to the yearly period,
   the yearly price is proposed.

.. screenshot:: sales-subscriptions-product-recurring-prices
   :menu: Sales ‣ Products ‣ Products ‣ (a product) ‣ Subscription
   :shows: The Subscription tab of a product with the Subscription Type field and the Recurring Prices list containing a monthly and a yearly price line.
   :highlight: The Recurring Prices list (red frame).
   :data: Product "Hosting – Standard plan"; Monthly 29.00, Yearly 290.00.
   :module: subscription
   :notes: English UI, light theme, 1440px width, crop to the notebook.

.. seealso::
   - :doc:`lines`
   - :doc:`configuration`

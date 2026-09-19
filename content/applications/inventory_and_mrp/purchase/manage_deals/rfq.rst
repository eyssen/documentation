======================
Requests for quotation
======================

.. |PO| replace:: :abbr:`PO (Purchase Order)`
.. |POs| replace:: :abbr:`POs (Purchase Orders)`
.. |RFQ| replace:: :abbr:`RFQ (Request for Quotation)`
.. |RFQs| replace:: :abbr:`RFQs (Requests for Quotation)`

Odoo's requests for quotation (RFQs) feature in the **Purchase** app standardizes ordering products
from multiple vendors with varying prices and delivery times.

|RFQs| are documents companies send to vendors requesting product pricing. In Odoo, once the vendor
approves the |RFQ|, the purchase order (PO) is confirmed to align on lead times and pricing.

Configuration
=============

Product
-------

To auto-populate product information and prices on an |RFQ|, configure products by going to
:menuselection:`Purchase app --> Products --> Products`. Select an existing product, or create a new
one by selecting :guilabel:`New`. Doing so opens the product form, where sales and purchasing data
can be configured.

To configure purchasable products, tick the :guilabel:`Purchase` checkbox, under the product name.
Next, go to the :guilabel:`Inventory` tab, and enable the :guilabel:`Buy` route.

.. important::
   The :guilabel:`Inventory` tab and routes are only visible if using the :doc:`Inventory app
   <../../inventory>`.

.. seealso::
   :doc:`Configure product types and track quantities
   <../../../inventory_and_mrp/inventory/product_management/configure>`

.. screenshot:: purchase-rfq-product-purchase-config
   :menu: Purchase ‣ Products ‣ Products ‣ (open a product)
   :shows: Product form with the "Purchase" checkbox ticked below the product name, the Inventory
           tab open, and the "Buy" route enabled.
   :highlight: The "Purchase" checkbox and the "Buy" route (red frame).
   :data: Demo company "YourCompany"; product "Office Chair Black".
   :module: purchase
   :notes: English UI, light theme, 1440px width.

.. _purchase/manage_deals/vendor-pricelist:

Vendor pricelist
----------------

In the :guilabel:`Purchase` tab of the product form, click :guilabel:`Add a line` to input the
vendor and their price, to have this information auto-populate on an |RFQ| each time the product is
listed.

.. seealso::
   :doc:`../products/pricelist`

Default columns include :guilabel:`Quantity`, :guilabel:`Unit Price`, and :guilabel:`Delivery Lead
Time`, but other columns like, :guilabel:`Vendor Product Code` or :guilabel:`Discount (%)`, can also
be enabled.

To enable or disable columns, click the :icon:`oi-settings-adjust` :guilabel:`(additional options)`
icon on the right side of the header row to reveal a drop-down menu of additional columns that can
be added (or removed) from the :guilabel:`Purchase` tab.

Additional columns worth enabling on a vendor pricelist line:

- :guilabel:`Company`: restricts the price to a single company, in a multi-company database. Leave
  it empty to make the price available to every company.
- :guilabel:`Variant`: restricts the price to a single product variant. Leave it empty to apply the
  price to every variant of the product.
- :guilabel:`Validity`: two dates (:guilabel:`Start Date` and :guilabel:`End Date`) after which the
  vendor price is no longer used to auto-populate |RFQs|. Leave them empty for a price that never
  expires.

.. note::
   Alternatively, prices and delivery lead times for existing products can be added by going to
   :menuselection:`Purchase app --> Configuration --> Vendor Pricelists`. Click :guilabel:`New` in
   the top-left corner. In the :guilabel:`Vendor` section of the pricelist form that appears, add
   the product information as it pertains to the vendor.

   .. note::
      This list can also show a :guilabel:`Created on` column (enable it via the
      :icon:`oi-settings-adjust` :guilabel:`(additional options)` icon), which is useful for
      auditing when a vendor price was entered.

Vendors column on the product list
-----------------------------------

The :guilabel:`Products` list, under :menuselection:`Purchase app --> Products --> Products`, shows
a :guilabel:`Vendors` column listing every vendor with a price on that product's vendor pricelist.
Products can also be grouped by :guilabel:`Vendor`, via :menuselection:`Group By --> Vendor` in the
search bar.

.. note::
   This column and grouping option are provided by the *eYssen Purchase* module
   (`eyssen_purchase`).

Warnings
--------

To display a custom message, or block the order, whenever a specific vendor or product is added to
a purchase order, first navigate to :menuselection:`Purchase app --> Configuration --> Settings`,
and under the :guilabel:`Orders` section, tick the :guilabel:`Warnings` checkbox. Then click
:guilabel:`Save`.

Next, set the warning on a vendor by going to their contact form, and, in the :guilabel:`Sales &
Purchase` tab, under the :guilabel:`Purchase` section, select :guilabel:`Warning` or
:guilabel:`Blocking Message` in the :guilabel:`Purchase Order Warning` field, and enter the message
to display.

To set a warning on a product instead, go to the product form, click the :guilabel:`Purchase` tab,
and configure the same way in the :guilabel:`Purchase Order Line Warning` field.

- :guilabel:`Warning`: a pop-up notifies the user of the message, but the order can still proceed.
- :guilabel:`Blocking Message`: a pop-up displays the message, and the vendor (or product) is
  removed from the order.

Order products
==============

With products and prices configured, follow these steps to create and send |RFQs| to make purchases
for the company.

|RFQ| dashboard
---------------

To get started, navigate to :menuselection:`Purchase app --> Orders --> Requests for Quotation`.

The :guilabel:`Requests for Quotation` dashboard displays an overview of the company's |RFQs|,
|POs|, and their status. The top of the screen breaks down all |RFQs| in the company, as well as
individual ones (where the user is the buyer) with a summary of their status.

The top-right corner also provides a report of the company's recent purchases by total value, lead
times, and number of |RFQs| sent.

Additionally, the dashboard includes buttons for:

- :guilabel:`To Send`: orders in the |RFQ| stage that have not been sent to the vendor.
- :guilabel:`Waiting`: |RFQs| that have been sent by email, and are waiting on vendor confirmation.
- :guilabel:`Late`: |RFQs| or |POs| where the :guilabel:`Order Deadline` has passed.

.. screenshot:: purchase-rfq-dashboard
   :menu: Purchase ‣ Orders ‣ Requests for Quotation
   :shows: The Requests for Quotation list with the To Send/Waiting/Late buttons and the recent
           purchases report at the top-right.
   :highlight: The To Send, Waiting, and Late buttons.
   :data: Demo company "YourCompany"; a handful of RFQs and POs in different states.
   :module: purchase
   :notes: English UI, light theme, 1440px width.

In addition to view options, the :guilabel:`Requests for Quotation` dashboard provides
:guilabel:`Filters` and :guilabel:`Group By` options, accessible via the search bar drop-down menu.

.. seealso::
   :doc:`../../../essentials/search`

.. _purchase/manage_deals/create-new-rfq:

Create a new |RFQ|
------------------

To create a new |RFQ|, click the :guilabel:`New` button on the top-left corner of the
:guilabel:`Requests for Quotation` dashboard to reveal a new |PO| form.

.. note::
   With the *Process Number - Purchase* module (`process_number_purchase`) installed, a
   :guilabel:`Process Number` field appears above the |RFQ| form, with a :guilabel:`Create a new
   process number` link. See :doc:`../../../services/project/process_numbers` for the concept of a
   process number. To have a process number created automatically for every new |RFQ|, enable
   :guilabel:`Create Automatically` under :menuselection:`Settings --> eYssen --> Process Number`.

Start by assigning a :guilabel:`Vendor`.

The :guilabel:`Vendor Reference` field points to the sales and delivery order numbers sent by the
vendor. This comes in handy once products are received, and the |PO| needs to be matched to the
delivery order.

With the :doc:`Purchase Agreements feature <blanket_orders>` activated, the :guilabel:`Blanket
Order` field appears, referring to long-term purchase agreements on recurring orders with set
pricing. To view and configure blanket orders, head to :menuselection:`Purchase app --> Orders -->
Purchase agreements`.

.. important::
   The :guilabel:`Purchase agreements` view only appears if the :guilabel:`Blanket Order` setting is
   enabled. To do so, navigate to :menuselection:`Purchase app --> Configuration --> Settings`, then
   tick the :guilabel:`Blanket Orders` checkbox.

Next, configure an :guilabel:`Order Deadline`, which is the date by which the vendor must confirm
their agreement to supply the products.

.. note::
   After the :guilabel:`Order Deadline` is exceeded, the |RFQ| is marked as late, but the products
   can still be ordered.

:guilabel:`Expected Arrival` is automatically calculated based on the :guilabel:`Order Deadline` and
vendor lead time. Tick the checkbox for :guilabel:`Ask confirmation` to ask the vendor to confirm
the shipping date by email.

.. note::
   :guilabel:`Ask confirmation` only appears if the :guilabel:`Receipt Reminder` setting is enabled,
   under :menuselection:`Purchase app --> Configuration --> Settings`. When enabled, Odoo
   automatically emails a reminder to the vendor a set number of days before the expected receipt,
   for any |PO| where :guilabel:`Ask confirmation` was ticked and the vendor has not yet confirmed.
   The number of days is set per vendor, on the :guilabel:`Sales & Purchase` tab of their contact
   form, in the :guilabel:`Days Before Receipt` field.

With the :doc:`Storage Locations feature
<../../inventory/warehouses_storage/inventory_management/use_locations>` activated, the
:guilabel:`Deliver to` field appears, which specifies which warehouse operation (set in the
**Inventory** app) is used to receive the shipment.

Select the receiving warehouse address here, or select :guilabel:`Dropship` to indicate that this
order is to be shipped directly to the end customer. When :guilabel:`Dropship` is selected, the
:guilabel:`Dropship address` field is enabled. Contact names auto-populate here from the
**Contacts** app.

.. important::
   The :guilabel:`Dropship` options only appear if the :guilabel:`Dropshipping` setting is enabled
   in the **Inventory** app. To do so, navigate to :menuselection:`Inventory app --> Configuration
   --> Settings`, then tick the :guilabel:`Dropshipping` checkbox.

.. tip::
   To create |RFQs| using different currencies, each currency needs to be enabled in the
   **Invoicing** app settings. See :doc:`../../../sales/sales/products_prices/prices/currencies` to
   learn more.

Products tab
~~~~~~~~~~~~

In the :guilabel:`Products` tab, add the products to be ordered. Click :guilabel:`Add a product`,
and type in the product name, or select the item from the drop-down menu.

To create a new product and add it, type the new product name in the :guilabel:`Product` column,
select :guilabel:`Create [product name]` from the resulting drop-down menu and manually add the unit
price. Alternatively, select :guilabel:`Create and edit...` to be taken to the product form for that
new item.

:guilabel:`Catalog` can also be selected to navigate to a product menu from the chosen vendor. From
here, products can be added to the cart.

.. note::
   To make adjustments to products and prices, access the product form by clicking the
   :icon:`oi-arrow-right` :guilabel:`(right arrow)` icon that becomes available upon hovering over
   the :guilabel:`Product` name.

.. tip::
   With the :guilabel:`Variant Grid Entry` setting enabled, under :menuselection:`Purchase app -->
   Configuration --> Settings`, in the :guilabel:`Products` section, products with several variants
   (size, color, etc.) can be added to the |RFQ| through a grid, instead of one variant at a time.
   This mirrors the *Sales* app feature described in :doc:`the Sales documentation
   <../../../sales/sales/sales_quotations/orders_and_variants>`; on a purchase order the setting is
   named :guilabel:`Variant Grid Entry` rather than :guilabel:`Order Grid Entry`.

Add items from a previous purchase order
++++++++++++++++++++++++++++++++++++++++

On a draft |RFQ|, click the :icon:`fa-files-o` :guilabel:`(add previous items)` button, above the
:guilabel:`Products` tab, to copy the product lines of an earlier purchase order into the current
one.

In the :guilabel:`Add Previous Items` pop-up window, select the :guilabel:`Previous Purchase` to
copy lines from, and choose what should happen :guilabel:`If Product Duplication` occurs (i.e., the
current |RFQ| already has a line for one of the copied products):

- :guilabel:`Stop`: cancels the whole operation with an error message.
- :guilabel:`Skip`: leaves the existing line untouched, and copies over the remaining lines.
- :guilabel:`Replace`: overwrites the existing line's quantity and price with the copied values.
- :guilabel:`Increase`: adds the copied quantity to the existing line's quantity, and applies the
  copied price.

Click :guilabel:`Add` to copy the lines onto the current |RFQ|.

.. note::
   This feature is provided by the *Add Items from Previous Purchase* module
   (`eyssen_add_item_from_previous_purchase`), and is only available while the |RFQ| is in the
   :guilabel:`RFQ` (draft) stage.

Send the |RFQ|
--------------

Clicking :guilabel:`Send by Email` reveals a :guilabel:`Compose Email` pop-up window, with a
:guilabel:`Purchase: Request for Quotation` template loaded, ready to send to the vendor's email
address (configured in the **Contacts** app).

After crafting the desired message, click :guilabel:`Send`. Once sent, the |RFQ| moves to the
:guilabel:`RFQ Sent` stage.

Clicking :guilabel:`Print RFQ` downloads a PDF of the |RFQ|.

.. seealso::
   :doc:`../../../essentials/contacts`

.. _purchase/manage_deals/confirm-order:

Confirm order
-------------

Clicking :guilabel:`Confirm Order` directly transforms the |RFQ| into an active |PO|.

.. tip::
   Odoo tracks communications on each order through the chatter of the |PO| form. This shows the
   emails sent between the user and the contact, as well as any internal notes and activities.
   Messages, notes, and activities can also be logged on the chatter.

Once an |RFQ| is confirmed, it creates a |PO|.

On the new |PO|, the :guilabel:`Order Deadline` field changes to :guilabel:`Confirmation Date`,
which displays the date and time the user confirmed the order.

Depending on the user's chosen configuration in the **Purchase** app settings, a *vendor bill* is
created once products have been ordered or received. For more information, refer to the
documentation on :doc:`managing vendor bills <manage>`.

.. note::
   After an order is placed, clicking :guilabel:`Receive Products` records the reception of new
   products into the database.

.. note::
   With the **Inventory** app installed, confirming a |PO| automatically creates a receipt document,
   with the product information and expected arrival dates automatically populated.

.. seealso::
   :doc:`manage`

.. _purchase/manage_deals/po-approval:

Purchase order approval
------------------------

To require a manager's approval before a purchase order over a certain amount can be confirmed,
navigate to :menuselection:`Purchase app --> Configuration --> Settings`, and under the
:guilabel:`Orders` section, tick the :guilabel:`Purchase Order Approval` checkbox. Then, in the
:guilabel:`Minimum Amount` field that appears, enter the threshold amount, and click
:guilabel:`Save`.

Once this setting is enabled, confirming an |RFQ| whose total is above the minimum amount moves it
to the :guilabel:`To Approve` stage, instead of directly to :guilabel:`Purchase Order`. A user with
the *Purchase Manager* role can then click :guilabel:`Approve Order` to confirm it.

Lock confirmed orders
-----------------------

To prevent confirmed purchase orders from being edited, navigate to :menuselection:`Purchase app -->
Configuration --> Settings`, and under the :guilabel:`Orders` section, tick the :guilabel:`Lock
Confirmed Orders` checkbox, then click :guilabel:`Save`.

With this setting enabled, every |PO| is automatically set to the :guilabel:`Locked` status once
confirmed. To manually lock (or unlock) an individual order regardless of the setting, click the
:guilabel:`Lock` (or :guilabel:`Unlock`) button on the |PO| form; unlocking requires the *Purchase
Manager* role.

Purchase order status
-----------------------

Throughout its lifecycle, a purchase order moves through the following statuses, shown at the top of
the form:

- :guilabel:`RFQ`: the initial, unconfirmed, draft state.
- :guilabel:`RFQ Sent`: the request for quotation has been emailed to the vendor.
- :guilabel:`To Approve`: the order total is above the :ref:`approval threshold
  <purchase/manage_deals/po-approval>`, and is waiting for a manager to approve it.
- :guilabel:`Purchase Order`: the order has been confirmed (or approved).
- :guilabel:`Locked`: the confirmed order can no longer be edited.
- :guilabel:`Cancelled`: the order was cancelled.

Order quantity totals
-----------------------

On the |PO| form, next to the tax totals under the :guilabel:`Products` tab, a :guilabel:`Sum Qty`
block lists the total ordered quantity of each unit of measure used on the order (for example, `12
Units` and `3 kg`), together with the number of distinct storable products and services on the
order. A shorter version of this total, such as `2 P, 15 Qty`, is also available as an optional
column (:guilabel:`Sum Qty`) on the :guilabel:`Requests for Quotation` and purchase order lists.

.. note::
   This feature is provided by the *Add Quantity Total for Purchase* module
   (`eyssen_quantity_total_purchase`).

============
Dropshipping
============

.. |RfQ| replace:: :abbr:`RfQ (request for quotation)`

Dropshipping is an order fulfillment strategy that allows sellers to have items shipped directly
from suppliers to customers. Normally, a seller purchases a product from a supplier, stores it in
their inventory, and ships it to the end customer once an order is placed. With dropshipping, the
supplier is responsible for storing and shipping the item. This benefits the seller by reducing
inventory costs, including the price of operating warehouses.

Configure products to be dropshipped
====================================

To use dropshipping as a fulfillment strategy, navigate to the :menuselection:`Purchase` app and
select :menuselection:`Configuration --> Settings`. Under the :guilabel:`Logistics` heading, click
the :guilabel:`Dropshipping` checkbox, and :guilabel:`Save` to finish.

Next, go to the :menuselection:`Sales` app, click :menuselection:`Products --> Products` and choose
an existing product or select :guilabel:`Create` to configure a new one. On the :guilabel:`Product`
page, make sure that the :guilabel:`Can be Sold` and :guilabel:`Can be Purchased` checkboxes are
enabled.

.. screenshot:: daily-operations-dropshipping-sold-purchased-checkboxes
   :menu: Inventory ‣ Products ‣ Products
   :shows: A product form with the "Can be Sold" and "Can be Purchased" checkboxes both ticked.
   :highlight: Both checkboxes (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

Click on the :guilabel:`Purchase` tab and specify a vendor and the price that they sell the product
for. Multiple vendors can be added, but the vendor at the top of the list will be the one
automatically selected for purchase orders.

.. screenshot:: daily-operations-dropshipping-product-vendor-config
   :menu: Inventory ‣ Products ‣ Products
   :shows: The Purchase tab of a product form with a vendor and a purchase price added to the vendor pricelist.
   :highlight: The vendor line (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

Finally, select the :guilabel:`Inventory` tab and enable the :guilabel:`Dropship` checkbox in the
:guilabel:`Routes` section.

.. screenshot:: daily-operations-dropshipping-enable-dropship-route
   :menu: Inventory ‣ Products ‣ Products
   :shows: The Inventory tab of a product form with the "Dropship" route ticked in the Operations section.
   :highlight: The "Dropship" checkbox (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

.. note::
   While it is not necessary to enable the :guilabel:`Buy` route in addition to the
   :guilabel:`Dropship` route, enabling both provides the option of dropshipping the product or
   purchasing it directly.

Fulfill orders using dropshipping
=================================

When a sales order is created for a dropshipped product, an associated request for quotation (RfQ)
is automatically generated to purchase the product from the vendor. Sales orders can be viewed in
the :menuselection:`Sales` app by selecting :menuselection:`Orders --> Orders`. Click the
:guilabel:`Purchase` smart button at the top right of a sales order to view the associated
:abbr:`RFQ (Request for Quotation)`.

.. screenshot:: daily-operations-dropshipping-dropship-sales-order
   :menu: Sales ‣ Orders ‣ Orders
   :shows: A confirmed sales order for a dropshipped product, with the Purchase smart button in the top-right corner.
   :highlight: The Purchase smart button (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

Once the :abbr:`RFQ (Request for Quotation)` is confirmed, it becomes a purchase order, and a
dropship receipt is created and linked to it. The receipt can be viewed by clicking the
:guilabel:`Dropship` smart button in the top-right corner of the purchase order form.

.. screenshot:: daily-operations-dropshipping-dropship-purchase-order
   :menu: Purchase ‣ Orders ‣ Purchase Orders
   :shows: The dropship purchase order created from the sales order, with the Receipt smart button in the top-right corner.
   :highlight: The Receipt smart button (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

The dropship receipt displays :guilabel:`Partners/Vendors` in the :guilabel:`Source Location` field,
and :guilabel:`Partners/Customers` in the :guilabel:`Destination Location` field. Upon delivery of
the product to the customer, click on the :guilabel:`Validate` button at the top-left of the
dropship receipt to confirm the delivered quantity.

.. screenshot:: daily-operations-dropshipping-validate-dropship-receipt
   :menu: Inventory ‣ Operations ‣ Transfers
   :shows: The dropship transfer, moving goods from the vendor location straight to the customer location, with the Validate button visible.
   :highlight: The Validate button (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

To view all dropship orders, simply navigate to the :menuselection:`Inventory` :guilabel:`Overview`
dashboard and click the teal :guilabel:`# TO PROCESS` button on the :guilabel:`Dropship` card.

.. screenshot:: daily-operations-dropshipping-view-all-dropship-orders
   :menu: Inventory
   :shows: The Inventory overview with the "Dropship" operation-type card and its count of orders to process.
   :highlight: The "Dropship" card (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

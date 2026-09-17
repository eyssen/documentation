==============
Blanket orders
==============

A **blanket order** is a framework agreement: the customer commits to a total quantity of one or
more products at an agreed price, and calls that quantity off over time in several ordinary sales
orders.

The *Sale Blanket Orders* module (``sale_blanket_order``) adds two menus under
:menuselection:`Sales app --> Orders`: :guilabel:`Blanket Orders` and :guilabel:`Blanket Order
Lines`.

Create a blanket order
======================

Go to :menuselection:`Sales app --> Orders --> Blanket Orders` and click :guilabel:`New`.

- :guilabel:`Partner`: the customer who commits to the quantities.
- :guilabel:`Validity Date`: the day the agreement expires. After it, the blanket order becomes
  :guilabel:`Expired` and no more sales orders can be called off.
- :guilabel:`Pricelist`, :guilabel:`Payment Terms`, :guilabel:`Fiscal Position`,
  :guilabel:`Salesperson`, :guilabel:`Sales Team`, :guilabel:`Customer Reference` and
  :guilabel:`Tags`: as on a sales order.
- :guilabel:`Order Lines`: one line per product, with the :guilabel:`Original Qty` committed, the
  :guilabel:`Price`, the taxes and an optional :guilabel:`Scheduled Date`.

Click :guilabel:`Confirm` to move the agreement from :guilabel:`Draft` to :guilabel:`Open`. The
totals (:guilabel:`Untaxed Amount`, :guilabel:`Taxes`, :guilabel:`Total`) are computed like on a
sales order.

.. screenshot:: sales-blanket-orders-form
   :menu: Sales ‣ Orders ‣ Blanket Orders ‣ (a blanket order)
   :shows: A confirmed blanket order in the Open state with the partner, validity date and pricelist, the order lines with their original, ordered, delivered, invoiced and remaining quantities, and the "Create Sale Order" button.
   :highlight: The "Create Sale Order" button and the Remaining Qty column (red frames).
   :data: Blanket order BO00003 for "Deco Addict", 1 000 units committed, 300 already ordered.
   :module: sale_blanket_order
   :notes: English UI, light theme, 1440px width, full form.

Quantity tracking
=================

Each blanket order line tracks five quantities, so it is always visible how much of the commitment
is left:

- :guilabel:`Original Qty`: the committed quantity.
- :guilabel:`Ordered Qty`: already called off on sales orders.
- :guilabel:`Delivered Qty` and :guilabel:`Invoiced Qty`: the progress of those sales orders.
- :guilabel:`Remaining Qty`: what may still be called off.

A blanket order becomes :guilabel:`Done` when nothing remains, and :guilabel:`Expired` when the
validity date passes with a remainder.

The :menuselection:`Sales app --> Orders --> Blanket Order Lines` list shows the lines of every
blanket order together, which is the quickest way to see what is still open across customers.

Call off a sales order
======================

Click :guilabel:`Create Sale Order` on the blanket order (or select lines in the
:guilabel:`Blanket Order Lines` list and use the same action). In the pop-up, enter the
:guilabel:`Quantity to Order` for each line — the :guilabel:`Remaining quantity` is shown next to it
— and click :guilabel:`Create and View Order`.

The generated sales order takes the blanket order's price, taxes, payment terms and pricelist, and
each of its lines keeps a :guilabel:`Blanket Order line` link. Confirming that sales order increases
the :guilabel:`Ordered Qty` of the blanket order line.

.. screenshot:: sales-blanket-orders-create-so
   :menu: Sales ‣ Orders ‣ Blanket Orders ‣ (a blanket order) ‣ Create Sale Order
   :shows: The call-off pop-up listing the blanket order lines with their remaining quantity and the "Quantity to Order" input, and the "Create and View Order" button.
   :highlight: The "Quantity to Order" column (red frame).
   :data: Two lines with 700 remaining; 100 entered on the first line.
   :module: sale_blanket_order
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

The :guilabel:`Sale Orders` smart button on the blanket order opens every order called off from it.

Restricting the called-off orders
=================================

By default a salesperson can still add other products to an order created from a blanket order. To
prevent that, enable :guilabel:`Disable adding more lines to SOs` in
:menuselection:`Sales app --> Configuration --> Settings`. Orders that originate from a blanket
order then only accept the lines that came from it.

.. note::
   The :guilabel:`Blanket Orders` menu is visible to sales administrators; salespeople see the
   :guilabel:`Blanket Order Lines` list.

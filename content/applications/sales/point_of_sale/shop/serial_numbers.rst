=======================
Serial numbers and lots
=======================

Working with **serial numbers** and **lots** allows tracking your products' movements. When products
are tracked, the system identifies their location based on their last movement.

To enable traceability, go to :menuselection:`Point of Sale --> Products --> Products`. Then,
select a product and check the :guilabel:`Tracking By Unique Serial Number` or the
:guilabel:`Tracking By Lots` box in the :guilabel:`Inventory` tab.

.. screenshot:: pos-serial-numbers-product-tracking
   :menu: Point of Sale ‣ Products ‣ Products ‣ (a product) ‣ Inventory
   :shows: The "Inventory" tab of a product form with "Track Inventory" enabled and tracking set to "By Unique Serial Number".
   :highlight: The tracking selection (red frame).
   :module: point_of_sale, stock
   :notes: English UI, light theme, 1440px width, centered, crop to the traceability block.

Serial numbers and lots importation
===================================

You can import serial numbers in Point of Sale. To do so, select a **sales order** or a
**quotation** containing tracked products. Then, agree to load the **Lots or Serial Numbers** linked
to the :abbr:`SO (sales order)`.

.. screenshot:: pos-serial-numbers-import-popup
   :menu: (POS interface) ‣ Quotations/Orders ‣ (a sales order)
   :shows: The popup asking whether to import the serial or lot numbers recorded on the sales order into the POS order.
   :module: point_of_sale, pos_sale
   :notes: English UI, light theme, centered, 480px wide.

The imported tracking numbers appear below the tracked products. You can modify them by clicking on
the list-view button next to the products.

.. screenshot:: pos-serial-numbers-imported-cart
   :menu: (POS interface) ‣ Register screen
   :shows: The cart after importing a sales order, with the serial numbers listed under the tracked products.
   :module: point_of_sale, pos_sale
   :notes: English UI, light theme, centered, 480px wide.

.. seealso::
   - :doc:`../shop/sales_order`

Serial numbers and lots creation
================================

If a tracked product is available in your POS, adding the product to the cart opens a pop-up window
where you can type or scan the product's serial or lot numbers. To add more than one of the same
tracked products, click on **enter** to validate and start a new line.

.. screenshot:: pos-serial-numbers-edit-popup
   :menu: (POS interface) ‣ Register screen ‣ (list-view button on a tracked product)
   :shows: The popup used to enter or edit serial and lot numbers, with one number per line.
   :module: point_of_sale, pos_sale
   :notes: English UI, light theme, centered, 480px wide.

.. note::
   - Changing a tracked product's quantity using the numpad turns the list-view button red. Click on
     it to add the missing lot and serial numbers.
   - :guilabel:`Lot & Serial Number(s)` are :guilabel:`required` on tracked products but not
     mandatory. Meaning that not attributing some or any does **not** prevent from completing the
     sale.

.. seealso::
   - :doc:`/applications/inventory_and_mrp/inventory/product_management/product_tracking/serial_numbers`
   - :doc:`/applications/inventory_and_mrp/inventory/product_management/product_tracking/lots`

=================================
Scan products onto an order
=================================

The ``eyssen_barcode_purchase`` and ``eyssen_barcode_sale`` modules add a barcode-scan button
directly to request-for-quotation and quotation forms, so that order lines can be built by
scanning products instead of searching for them one by one.

Purchase orders
================

On a request for quotation (RFQ) still in the :guilabel:`Draft` state, a :guilabel:`(barcode-scan)`
button appears next to the order lines. Click it to reveal a scan field: type into it, scan with a
USB/Bluetooth/keyboard-wedge scanner, or use the :guilabel:`(camera)` button to scan with the
device's camera.

.. screenshot:: barcode-scan-orders-purchase-button
   :menu: Purchase ‣ Orders ‣ Requests for Quotation ‣ (a draft RFQ)
   :shows: A draft request for quotation with the barcode-scan button next to the order lines, and
      the scan field it opens.
   :highlight: The barcode-scan button and the scan field (red frame).
   :data: Draft RFQ for vendor "Azure Interior" with one product line already added.
   :module: eyssen_barcode_purchase
   :notes: English UI, light theme, 1440px width, crop to the order-lines header.

Scanning a product's barcode adds it as a new order line with a quantity of one; scanning the same
barcode again increases the quantity of the existing line by one instead of adding a duplicate.
Scanning a code that matches no product's :guilabel:`Barcode` field leaves the order unchanged.

.. note::
   The button is shown regardless of the order's state; scanning still only makes sense while the
   :abbr:`RFQ (request for quotation)` is in :guilabel:`Draft`, since a confirmed purchase order's
   lines are no longer meant to be edited this way.

Sales orders and quotations
=============================

The same behavior is available on quotations: on a sales order still in the :guilabel:`Quotation`
(draft) state, a :guilabel:`(barcode-scan)` button next to the order lines opens the same scan
field.

.. screenshot:: barcode-scan-orders-sale-button
   :menu: Sales ‣ Orders ‣ Quotations ‣ (a draft quotation)
   :shows: A draft quotation with the barcode-scan button next to the order lines, and the scan
      field it opens.
   :highlight: The barcode-scan button and the scan field (red frame).
   :data: Draft quotation for customer "Deco Addict" with one product line already added.
   :module: eyssen_barcode_sale
   :notes: English UI, light theme, 1440px width, crop to the order-lines header.

Scanning a product's barcode adds it to the quotation with a quantity of one, or increases the
quantity of an existing line for that product by one. As on purchase orders, a barcode that does
not match a product's :guilabel:`Barcode` field is ignored.

.. seealso::
   :doc:`../../inventory/product_management/configure` for setting a product's barcode.

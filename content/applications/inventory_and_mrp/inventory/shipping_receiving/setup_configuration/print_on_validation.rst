=======================
Printable delivery PDFs
=======================

Automatically print delivery-related PDFs documents and labels in Odoo, containing package recipient
details, contents, or handling instructions.

The following PDFs can be configured to print upon validating an *Inventory* operation (e.g.
receipt, picking, delivery orders, quality checks):

#. :ref:`Delivery slip <inventory/shipping_receiving/delivery-slip>`
#. :ref:`Return slip <inventory/shipping_receiving/return-slip>`
#. :ref:`Product labels of items in the order <inventory/shipping_receiving/product-labels>`
#. :ref:`Lot and serial number labels <inventory/shipping_receiving/lot-sn-labels>`
#. :ref:`Reception report and its labels <inventory/shipping_receiving/reception-report>`
#. :ref:`Package content <inventory/shipping_receiving/package-content>`
#. :ref:`Package label <inventory/shipping_receiving/package-label>`

.. _inventory/shipping_receiving/print_setup:

To automatically print these forms, navigate to :menuselection:`Inventory app --> Configuration -->
Operations Types`, and select the desired operation type.

In the :guilabel:`Hardware` tab, tick each of the desired options available in the :guilabel:`Print
on Validation` section to download the PDF of those selected documents automatically after
validating the :guilabel:`Operation Type`. For details on what each of the checkbox options do, jump
to the related section.

.. screenshot:: setup-configuration-print-on-validation
   :menu: Inventory ‣ Configuration ‣ Operations Types
   :shows: The Hardware tab of an operation type, showing the "Print on Validation" checkboxes: Delivery Slip, Return Slip, Product Labels, Lot/SN Labels, Reception Report, Package Content.
   :highlight: The "Print on Validation" group (red frame).
   :data: Operation type "Pick" of the main warehouse.
   :module: stock
   :notes: English UI, light theme, 1440px width.

.. _inventory/shipping_receiving/delivery-slip:

Delivery slip
=============

A *delivery slip* contains recipient and package details, usually placed inside (or attached to) the
package.

.. seealso::
   - :doc:`Tracking label <../setup_configuration/labels>`

After :ref:`enabling the Delivery Slip setting <inventory/shipping_receiving/print_setup>` in the
:guilabel:`Hardware` tab configuration options, clicking :guilabel:`Validate` on the desired
operation type downloads a PDF of the delivery slip.

The delivery slip shows products, quantities, the delivery order reference number, and the total
order weight.

.. screenshot:: setup-configuration-print-on-validation-delivery-slip
   :menu: (document)
   :shows: A printed delivery slip PDF listing the products, quantities, the delivery order reference and the total order weight.
   :module: stock
   :notes: PDF document, use demo data.

.. _inventory/shipping_receiving/return-slip:

Return slip
===========

Print a *return slip* to include in a delivery for customer return packages. It identifies the
return, links to the sales order, and includes item details and customer information. It can also
include specific return instructions for the customer.

After :ref:`enabling the Return Slip setting <inventory/shipping_receiving/print_setup>` in the
:guilabel:`Hardware` tab configuration options, clicking :guilabel:`Validate` on the desired
operation type downloads a PDF of the return slip.

The return slip displays the company's return address, along with barcodes for both the order and
the return operation.

.. screenshot:: setup-configuration-print-on-validation-return-slip
   :menu: (document)
   :shows: A printed return slip PDF with the company return address and the barcodes of the order and the return operation.
   :module: stock
   :notes: PDF document, use demo data.

.. _inventory/shipping_receiving/product-labels:

Product labels
==============

Print *product labels* to affix to items in an order, providing essential information, such as
product name, barcode, and price.

After navigating to the intended operation type (:menuselection:`Inventory app --> Configuration -->
Operations Types`), in the :guilabel:`Hardware` tab, tick the :guilabel:`Product Labels` option.

Doing so makes the :guilabel:`Print label as:` drop-down menu visible, where each product label can
be printed as:

- :guilabel:`2 x 7 with price`: PDF displays product name, barcode, and price, fitting two rows and
  seven columns of product labels per page.

  .. spoiler:: Example 2 x 7

     .. screenshot:: setup-configuration-print-on-validation-two-seven
        :menu: (document)
        :shows: A sheet of 2 x 7 product labels with the product name, barcode and price.
        :module: stock
        :notes: PDF document, use demo data.

- :guilabel:`4 x 7 with price`: displays product name, barcode, and price, fitting four rows and
  seven columns of product labels per page.

  .. spoiler:: Example 4 x 7

     .. screenshot:: setup-configuration-print-on-validation-four-seven
        :menu: (document)
        :shows: A sheet of 4 x 7 product labels with the product name, barcode and price.
        :module: stock
        :notes: PDF document, use demo data.

- :guilabel:`4 x 12`: displays product name and barcode. Fits four rows and twelve columns of
  product labels per page.

  .. spoiler:: Example 4 x 12

     .. screenshot:: setup-configuration-print-on-validation-four-twelve
        :menu: (document)
        :shows: A sheet of 4 x 12 product labels with the product name and barcode, without price.
        :module: stock
        :notes: PDF document, use demo data.

- :guilabel:`4 x 12 with price`: displays product name, barcode, and price. Fits four rows and
  twelve columns of product labels per page.
- :guilabel:`ZPL Labels`: prints labels in the Zebra Programming Language (ZPL) containing the
  product name and barcode. Readable for Zebra printers to automatically print labels.
- :guilabel:`ZPL Labels with price`: prints labels in the :abbr:`ZPL (Zebra Programming Language)`
  containing the product name, barcode, and price.

.. note::
   Product labels can be manually printed from any delivery order, by clicking the :guilabel:`Print
   Labels` button.

.. _inventory/shipping_receiving/lot-sn-labels:

Lot/SN Labels
=============

Print *lot/SN labels* to affix to items in an order, providing essential information, such as
product name, lot or serial number, and the barcode.

To automatically print this PDF, navigate to the intended operation type's options page
(:menuselection:`Inventory app --> Configuration --> Operations Types`). Then, in the
:guilabel:`Hardware` tab, tick the :guilabel:`Lot/SN Labels` option.

Doing so makes the :guilabel:`Print label as:` drop-down menu visible, where each product label can
be printed as:

- :guilabel:`4 x 12 - One per lot/SN`: PDF with labels for unique lot/serial numbers in the order,
  including product name, lot/serial number, and barcode. Fits four rows and twelve columns per
  page.

  .. spoiler:: Example 4 x 12 - One per lot/SN

     .. screenshot:: setup-configuration-print-on-validation-four-twelve-lots
        :menu: (document)
        :shows: A sheet of lot/serial number labels for an order that contains a single set of lot numbers, showing the product name, lot number and barcode.
        :module: stock
        :notes: PDF document, use demo data.

     Labels for an order with only one unique set of lot/serial numbers.

- :guilabel:`4 x 12 - One per unit`: PDF with labels matching the quantity of items, displaying the
  product name, lot/serial number, and barcode. Fits four rows and twelve columns per page.
- :guilabel:`ZPL Labels - One per lot/SN`: prints labels in :abbr:`ZPL (Zebra Programming
  Language)`, containing the product name, lot/serial number, and barcode.
- :guilabel:`ZPL Labels - One per unit`: prints labels with the quantity of items in :abbr:`ZPL
  (Zebra Programming Language)`, containing the product name, lot/serial number, and barcode.

.. _inventory/shipping_receiving/reception-report:

Reception report
================

The *reception report* shows, for a validated receipt, which incoming quantities can be allocated to
the sales orders, manufacturing orders, or transfers that are waiting for them. Its labels can be
printed and attached to the goods so that warehouse staff know where each item is headed.

To make the report available, go to :menuselection:`Inventory app --> Configuration --> Settings`,
tick the :guilabel:`Reception Report` checkbox in the :guilabel:`Operations` section, and click
:guilabel:`Save`.

Then, go to :menuselection:`Inventory app --> Configuration --> Operations Types`, select a receipt
or internal operation type, and in the :guilabel:`Hardware` tab tick:

- :guilabel:`Reception Report`: prints the report of the picking on validation, provided the picking
  has assigned moves.
- :guilabel:`Reception Report Labels`: prints one label per allocated line.

.. note::
   Both options are only available on incoming and internal operation types, not on delivery orders.

.. screenshot:: setup-configuration-print-on-validation-reception-report
   :menu: Inventory ‣ Configuration ‣ Operations Types
   :shows: The Hardware tab of a receipt operation type, with the "Reception Report" and "Reception Report Labels" checkboxes ticked in the "Print on Validation" section.
   :highlight: The two reception report checkboxes (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

.. _inventory/shipping_receiving/package-content:

Package content
===============

A *package content* PDF includes the package's barcode, packed date, along with a list of contained
products and quantities.

To print this form automatically, go to :menuselection:`Inventory app --> Configuration -->
Operation Types`, and select the desired operation type. Then, go to the :guilabel:`Hardware` tab,
and tick the :guilabel:`Package Contents` checkbox.

.. important::
   If the option is not available, enable the :doc:`Packages
   <../../product_management/configure/package>` feature, by going to :menuselection:`Inventory app
   --> Configuration --> Settings`, ticking the :guilabel:`Packages` checkbox, and clicking
   :guilabel:`Save`.

After enabling the feature in the :guilabel:`Hardware` tab, validating the operation prints a PDF of
the package contents.

.. spoiler:: Example package content PDF

   .. screenshot:: setup-configuration-print-on-validation-package-content
      :menu: (document)
      :shows: A printed package content PDF with the package barcode, the packed date and the list of products and quantities inside.
      :module: stock
      :notes: PDF document, use demo data.

   Package contents showing the package contents, barcode, and pack date.

.. _inventory/shipping_receiving/package-label:

Package label
=============

A *package label* that shows the package's barcode and pack date can be configured to print upon
clicking the *Put in Pack* button.

.. important::
   The :guilabel:`Put in Pack` button is available **only** when the :doc:`Packages
   <../../product_management/configure/package>` feature is enabled in
   :menuselection:`Inventory app --> Configuration --> Settings`.

   After it is enabled, the :guilabel:`Put in Pack` button is available on all inventory operations
   (e.g. receipt, pickings, internal transfers, delivery orders, etc.).

To automatically print the package label when the :guilabel:`Put in Pack` button is clicked, go to
:menuselection:`Inventory app --> Configuration --> Operation Types`. Select the desired operation
type, and tick the :guilabel:`Package Label` checkbox in the :guilabel:`Hardware` tab. Labels can be
printed in :guilabel:`PDF` or :guilabel:`ZPL` file formats, as defined in the :guilabel:`Print label
as` field.

.. spoiler:: Example of package barcode

   .. screenshot:: setup-configuration-print-on-validation-package-barcode
      :menu: (document)
      :shows: A printed package label PDF with the package barcode and the packed date.
      :module: stock
      :notes: PDF document, use demo data.


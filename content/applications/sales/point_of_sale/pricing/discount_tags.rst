===============================
Discount tags (barcode scanner)
===============================

To sell a product at a reduced price — for example, an item close to its expiration date — you can
print and scan **discount tags**. A discount tag is a barcode that encodes both the discount
percentage and the product's own barcode.

.. note::
   Using discount tags requires a :doc:`barcode scanner <../shop/barcode>`.

Barcode nomenclature
====================

Discount tags rely on the *Discounted Product* rule of the barcode nomenclature. In the
:guilabel:`Default Nomenclature`, that rule matches barcodes that start with `22`, followed by two
digits for the discount percentage, followed by the product's barcode.

To review the rule, :doc:`enable the developer mode </applications/general/developer_mode>`, go to
:menuselection:`Inventory --> Configuration --> Barcode Nomenclatures`, open
:guilabel:`Default Nomenclature`, and look up the :guilabel:`Discounted Product` line.

.. screenshot:: pos-discount-tags-nomenclature
   :menu: Inventory ‣ Configuration ‣ Barcode Nomenclatures ‣ Default Nomenclature
   :shows: The "Default Nomenclature" form with the barcode rules list, the "Discounted Product"
      rule visible with its barcode pattern.
   :highlight: The "Discounted Product" rule line (red frame).
   :module: barcodes, point_of_sale
   :notes: English UI, light theme, 1440px width, developer mode on, crop to the rules list.

.. example::
   To grant a 50 % discount on a product whose barcode is `2100002000003`, the discount tag's
   barcode is `22` (discount rule) + `50` (percentage) + `2100002000003` (product barcode).

Scan the product and the tag
============================

#. :ref:`Open a POS session <pos/session-start>`.
#. Scan the product's own barcode to add it to the cart.
#. Scan the discount tag. The discount is applied to that order line, and the transaction can be
   finished as usual.

.. screenshot:: pos-discount-tags-applied
   :menu: (POS interface) ‣ Register screen
   :shows: The POS cart with one product line showing the original price struck through and the
      discounted price, after scanning a 50 % discount tag.
   :highlight: The discounted order line (red frame).
   :data: Product "Lemon" with a 50 % discount tag.
   :module: point_of_sale, barcodes
   :notes: English UI, light theme, 1440px width, crop to the cart pane.

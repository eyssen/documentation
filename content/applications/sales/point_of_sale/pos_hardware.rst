========
Hardware
========

Odoo Point of Sale supports integration with a variety of hardware, including :doc:`payment
terminals <payment_methods/terminals>`, :ref:`customer displays <pos/display>`, :doc:`barcode
scanners <shop/barcode>`, and :doc:`ePOS printers <configuration/epos_printers>`.

.. _pos/display:

Customer display
================

The **customer display** feature provides real-time updates on a secondary screen for customers
during the checkout process. This screen shows the :ref:`items in the cart <pos/sell>`, the subtotal
as items are added, and details throughout the payment process. It also displays the total amount,
the selected :doc:`payment method <payment_methods>`, and any change to be returned.

.. screenshot:: pos-hardware-customer-display
   :menu: (POS interface) ‣ Customer Display window
   :shows: The customer-facing display window during checkout, listing two order lines with
      quantities and prices, the subtotal and the total amount.
   :module: point_of_sale
   :notes: English UI, light theme, 1440px width; scale down to about 50 % of the page width.

.. note::
   Both the customer and POS displays must have a minimum diagonal size of 6 inches. For optimal
   readability, larger screens are recommended.

Configuration
-------------

Depending on the POS setup, the feature can be displayed directly on a secondary screen connected
via USB-C or HDMI, or on another device connected to the same database.

To activate the feature, follow these steps:

#. Navigate to the :ref:`POS settings <configuration/settings>` and scroll down to the
   :guilabel:`Connected Devices` section.
#. Open the dropdown menu under the :guilabel:`Customer Display` section and select one of the
   following options:

   - :guilabel:`None`: To disable the feature.
   - :ref:`The same device <pos/display-same-device>`: To use a secondary screen connected
     with an HDMI or USB-C cable.
   - :ref:`Another device <pos_hardware/display_another_device>`: To use a remote device connected
     to the database.
#. Optionally, upload an image in the :guilabel:`Background Image` field. It is displayed on the
   customer display while no order is in progress.
#. Click :guilabel:`Save`.

Opening the customer display
----------------------------

.. _pos/display-same-device:

Same device
~~~~~~~~~~~

To open the customer display on a second screen connected to a POS system using an HDMI or USB-C
cable, follow these steps:

#. :ref:`Open a POS session <pos/session-start>`.
#. Click the :icon:`fa-bars` (:guilabel:`hamburger menu`) icon.
#. Click the :icon:`fa-desktop` (:guilabel:`Customer Display`) icon, which opens a new window to
   drag onto the second screen.

.. _pos_hardware/display_another_device:

Another device
~~~~~~~~~~~~~~

To open the customer display on a remote device (any computer, tablet, or smartphone), follow these
steps:

#. Access your database from the other device and navigate to :menuselection:`Point of Sale -->
   Dashboard`.
#. Click the :icon:`fa-ellipsis-v` (:guilabel:`Dropdown menu`) icon on a POS card.
#. Click :guilabel:`Customer Display` to open the display remotely.

.. note::
   The two devices are not required to share the same network as long as they are connected to the
   same database.

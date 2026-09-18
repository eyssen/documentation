===
SIX
===

Connecting a SIX payment terminal allows you to offer a fluid payment flow to your customers and
ease the work of your cashiers.

.. warning::
   Although Worldline has acquired SIX Payment Services and both entities utilize Yomani payment
   terminals, their firmware differs. Terminals supplied by Worldline are, therefore, incompatible
   with this integration.

Configuration
=============

.. _six/configure:

Configure the payment method
----------------------------

#. Go to the :ref:`POS settings <configuration/settings>`, scroll down to the :guilabel:`Payment
   Terminals` section, enable :guilabel:`Six`, and click :guilabel:`Save`. This installs the
   **POS Six** module.
#. :doc:`Create a payment method <../../payment_methods>` for the SIX terminal.
#. Set the journal type as :guilabel:`Bank`.
#. Fill in the :guilabel:`Outstanding Account` field.
#. Select :guilabel:`Terminal` in the :guilabel:`Integration` field.
#. Select :guilabel:`SIX` in the :guilabel:`Use a Payment Terminal` field.
#. Enter the terminal's IP address in the :guilabel:`Six Terminal IP` field.
#. Click :guilabel:`Save`.

.. screenshot:: pos-six-payment-method
   :menu: Point of Sale ‣ Configuration ‣ Payment Methods ‣ New
   :shows: A payment method form with "Integration" set to "Terminal", "Use a Payment Terminal" set to
      "SIX", and the "Six Terminal IP" field filled in with a local IP address.
   :highlight: The "Use a Payment Terminal" and "Six Terminal IP" fields (red frame).
   :data: Payment method named "SIX", bank journal "Bank", Six Terminal IP 192.168.1.42.
   :module: point_of_sale, pos_six
   :notes: English UI, light theme, 1440px width; scale down to about 45 % of the page width.

.. note::
   Ensure the SIX terminal is switched on and connected to the same local network as the POS
   device.

Link the payment method to a POS
--------------------------------

Once the payment method is created, it can be selected in the POS settings. To do so,

#. Go to the :ref:`POS' settings <configuration/settings>`.
#. Add the payment method under the :guilabel:`Payment methods` field within the :guilabel:`Payment`
   section.

=====
PayTM
=====

Connecting a `PayTM <https://business.paytm.com/>`_ payment terminal allows customers to pay by card
or by QR code directly from the POS.

.. important::
   PayTM payment terminals are only available in **India**.

Configuration
=============

Collect the PayTM credentials
-----------------------------

Log in to the `PayTM for Business portal <https://business.paytm.com/>`_ and collect:

- the **Merchant ID** (MID) of the merchant account;
- the **Merchant API key** (AES key);
- the **Terminal ID** (TID) of the device, or its activation code.

.. _paytm/configure:

Configure the payment method
----------------------------

#. Go to the :ref:`POS settings <configuration/settings>`, scroll down to the :guilabel:`Payment
   Terminals` section, enable :guilabel:`PayTM`, and click :guilabel:`Save`. This installs the
   **POS PayTM** module.
#. :doc:`Create a payment method <../../payment_methods>` for the PayTM terminal.
#. Set the journal type as :guilabel:`Bank`.
#. Select :guilabel:`Terminal` in the :guilabel:`Integration` field, then :guilabel:`PayTM` in the
   :guilabel:`Use a Payment Terminal` field.
#. Fill in the :guilabel:`PayTM Merchant ID`, :guilabel:`PayTM Terminal ID`, and
   :guilabel:`PayTM Merchant API Key` fields.
#. Set :guilabel:`Accept Payment` to :guilabel:`Automatically` for the payment to be validated in
   Odoo as soon as the terminal reports it, or to :guilabel:`Manually` for the cashier to confirm
   it.
#. Set :guilabel:`Allowed Payment Modes` to :guilabel:`All`, :guilabel:`Card`, or :guilabel:`QR`.
#. Click :guilabel:`Save`.

.. screenshot:: pos-paytm-payment-method
   :menu: Point of Sale ‣ Configuration ‣ Payment Methods ‣ New
   :shows: A payment method form with "Integration" set to "Terminal", "Use a Payment Terminal" set to
      "PayTM", and the merchant ID, terminal ID, API key, "Accept Payment" and "Allowed Payment
      Modes" fields filled in.
   :highlight: The PayTM-specific fields (red frame).
   :module: point_of_sale, pos_paytm
   :notes: English UI, light theme, 1440px width; use throw-away credentials and mask the API key.

.. note::
   The :guilabel:`PayTM Merchant API Key` is only visible to users with the :guilabel:`Point of
   Sale` access right set to :guilabel:`Administrator`.

.. tip::
   Enable :guilabel:`PayTM Test Mode` to send the transactions to the PayTM staging environment
   while testing the setup. Disable it before going live.

Link the payment method to a POS
--------------------------------

Go to the :ref:`POS settings <configuration/settings>` and add the payment method under the
:guilabel:`Payment methods` field within the :guilabel:`Payment` section.

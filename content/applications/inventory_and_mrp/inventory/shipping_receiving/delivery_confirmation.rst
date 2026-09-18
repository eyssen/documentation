=====================================
Delivery confirmation: signature, SMS
=====================================

Beyond the printed documents, Odoo can collect a **signature** from the person receiving the goods
and send the customer an **SMS** the moment a delivery is validated. Both are optional features of
the *Inventory* app and are configured independently of the delivery method.

.. _inventory/shipping_receiving/signature:

Signature on delivery orders
============================

Turn the feature on from :menuselection:`Inventory app --> Configuration --> Settings`. In the
:guilabel:`Shipping` section, tick :guilabel:`Signature`, and click :guilabel:`Save`.

.. note::
   The setting adds the *Sign Delivery Orders* access right to the current user. Other users need
   that right as well before the signature button appears for them.

.. screenshot:: shipping-receiving-delivery-confirmation-signature-setting
   :menu: Inventory ‣ Configuration ‣ Settings
   :shows: The Inventory settings page scrolled to "Shipping", with the "Signature" checkbox enabled.
   :highlight: The "Signature" checkbox (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

Once enabled, a :guilabel:`Sign` button appears in the header of every **delivery order** (it is not
shown on receipts or internal transfers). Click it to open the signature pad: the recipient's name
is pre-filled from the delivery address, and the signature can be drawn, typed, or uploaded as an
image. Confirming stores the signature on the transfer, the :guilabel:`Sign` button disappears, and
the signature is printed on the :ref:`delivery slip <inventory/shipping_receiving/delivery-slip>`
together with the recipient's name.

The signature can be collected either before validating the transfer or after it is
:guilabel:`Done`, so a driver can have the delivery signed on the spot from a portable device.

.. screenshot:: shipping-receiving-delivery-confirmation-sign-button
   :menu: Inventory ‣ Delivery Orders
   :shows: A delivery order header with the "Sign" button next to Validate, and the signature pad dialog open with the recipient's name pre-filled.
   :highlight: The "Sign" button (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

.. _inventory/shipping_receiving/sms-confirmation:

SMS confirmation
================

Odoo can text the customer when the last goods movement of their order is validated, so they know
the parcel is on its way.

To set it up, go to :menuselection:`Inventory app --> Configuration --> Settings`, and in the
:guilabel:`Shipping` section, tick :guilabel:`SMS Confirmation`. Doing so installs the *Stock - SMS*
module and reveals the :guilabel:`SMS Template` field, where the message sent to the customer is
selected. Click :guilabel:`Save`.

Sending text messages is an :doc:`In-App Purchase </applications/essentials/in_app_purchase>`
service, so the database needs SMS credits.

.. note::
   The setting is stored per company, and the message is only sent for **outgoing** transfers whose
   customer has a valid mobile number. The first time a delivery would trigger an SMS, Odoo shows a
   confirmation dialog so the message is never sent by accident.

.. screenshot:: shipping-receiving-delivery-confirmation-sms-setting
   :menu: Inventory ‣ Configuration ‣ Settings
   :shows: The Inventory settings page scrolled to "Shipping", with "SMS Confirmation" enabled and the "SMS Template" field visible below it.
   :highlight: The "SMS Confirmation" setting and its "SMS Template" field (red frame).
   :module: stock_sms
   :notes: English UI, light theme, 1440px width.

.. seealso::
   - :doc:`setup_configuration/print_on_validation`
   - :doc:`delivery_status_and_dates`

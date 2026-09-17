=========================================
Online signatures for order confirmations
=========================================

The Odoo **Sales** application provides customers with the ability to confirm orders, via an online
signature, directly on the sales order. Once the sales order is electronically signed by the
customer, the salesperson attached to the sales order is instantly notified that the order is
confirmed.

Activate online signatures
==========================

In order to have customers confirm orders with an online signature, the *Online Signature* feature
**must** be activated.

To activate the *Online Signature* feature, go to :menuselection:`Sales app --> Configuration -->
Settings`, scroll to the :guilabel:`Quotations \& Orders` heading, and activate the
:guilabel:`Online Signature` feature by checking the box beside it.

.. screenshot:: sales-get-signature-setting
   :menu: Sales ‣ Configuration ‣ Settings
   :shows: The Settings page scrolled to the "Quotations & Orders" section with the "Online Signature" checkbox enabled.
   :highlight: The "Online Signature" setting (red frame).
   :data: Demo company.
   :module: sale
   :notes: English UI, light theme, 1440px width, crop to the setting block.

Then, click the :guilabel:`Save` button in the top-left corner.

.. note::
   When making a quotation template, the online signature feature is the :guilabel:`Signature`
   option, located in the :guilabel:`Online confirmation` field of the quotation template form.

   .. screenshot:: sales-get-signature-template-option
      :menu: Sales ‣ Configuration ‣ Quotation Templates ‣ (a template)
      :shows: A quotation template form with the "Online signature" confirmation option ticked.
      :highlight: The "Online signature" option (red frame).
      :data: Template "Basic Furniture".
      :module: sale_management
      :notes: English UI, light theme, 1440px width, crop to the confirmation options.

   On standard quotations, the online signature feature is the :guilabel:`Signature` option, located
   under the :guilabel:`Other Info` tab of the quotation form.

   .. screenshot:: sales-get-signature-quotation-option
      :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation) ‣ Other Info
      :shows: The Sales section of the Other Info tab of a quotation, with the "Online signature" option ticked.
      :highlight: The "Online signature" option (red frame).
      :data: Quotation S00021.
      :module: sale
      :notes: English UI, light theme, 1440px width, crop to the Sales group.

Order confirmations with online signatures
==========================================

When clients access quotations online through their customer portal, there's a :guilabel:`Sign \&
Pay` button directly on the quotation.

.. screenshot:: sales-get-signature-portal-button
   :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation) ‣ Preview
   :shows: The customer portal view of a quotation with the "Sign & Pay" button at the top of the order.
   :highlight: The "Sign & Pay" button (red frame).
   :data: Quotation S00021.
   :module: sale
   :notes: English UI, light theme, 1440px width, crop to the portal header.

When clicked, a :guilabel:`Validate Order` pop-up window appears. In this pop-up window, the
:guilabel:`Full Name` field is auto-populated, based on the contact information in the database.

.. screenshot:: sales-get-signature-validate-popup
   :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation) ‣ Preview ‣ Sign & Pay
   :shows: The "Validate Order" pop-up window with the drawn signature, the Auto and Load options, and the Accept & Sign button.
   :highlight: The signature area (red frame).
   :data: A throw-away signature drawn in the field.
   :module: sale
   :notes: English UI, light theme, 1440px width, crop to the pop-up. Use a throw-away signature.

Then, customers have the option to enter an online signature with any of the following options:
:guilabel:`Auto`, :guilabel:`Draw`, or :guilabel:`Load`.

:guilabel:`Auto` lets Odoo automatically generate an online signature based on the information in
the :guilabel:`Full Name` field. :guilabel:`Draw` lets the customer use the cursor to create a
custom signature directly on the pop-up window. And :guilabel:`Load` lets the customer upload a
previously-created signature file from their computer.

After the customer has chosen any of the three previously mentioned signature options
(:guilabel:`Auto`, :guilabel:`Draw`, or :guilabel:`Load`), they will click the :guilabel:`Accept \&
Sign` button.

When :guilabel:`Accept \& Sign` is clicked, the various payment method options become available for
them to choose from (if the *online payment* option applies to this quotation).

Then, when the quotation is paid and confirmed, a delivery order is automatically created (if the
Odoo **Inventory** app is installed).

View online signatures in Developer Mode
----------------------------------------

Clients can view the online signature in :ref:`developer mode <developer-mode>`.

To view a online signature from a paid invoice, go to :menuselection:`Sales app --> Orders -->
Orders` and select the desired sales order. A new tab, :guilabel:`Customer Signature`, is available.
Click the tab to view the electronic signature as well as the :guilabel:`Signed By` and
:guilabel:`Signed On` information.

.. screenshot:: sales-get-signature-customer-signature-tab
   :menu: Sales ‣ Orders ‣ Orders ‣ (a confirmed order) ‣ Customer Signature
   :shows: The "Customer Signature" tab of a confirmed sales order, showing the stored signature image and the signer's name.
   :highlight: The stored signature (red frame).
   :data: Order S00021, signed by "Deco Addict". Developer mode is active.
   :module: sale
   :notes: English UI, light theme, 1440px width, crop to the notebook. Use a throw-away signature.

.. seealso::
   - :doc:`quote_template`
   - :doc:`get_paid_to_validate`


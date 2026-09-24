=================================
Online payment order confirmation
=================================

The Odoo *Sales* application provides customers with the ability to confirm orders, via an online
payment, directly on a sales order. Once the sales order is electronically paid for by the customer,
the salesperson attached to the sales order is instantly notified that the order is confirmed.

Activate online payments
========================

In order to have customers confirm orders with an online payment, the *Online Payment* setting
**must** be activated.

To activate the *Online Payment* feature, go to :menuselection:`Sales app --> Configuration -->
Settings`, scroll to the :guilabel:`Quotations \& Orders` heading, check the box next to the
:guilabel:`Online Payment` feature, and click :guilabel:`Save`.

.. screenshot:: sales-get-paid-setting
   :menu: Sales ‣ Configuration ‣ Settings
   :shows: The Settings page scrolled to the "Quotations & Orders" section with the "Online Payment" checkbox enabled and the prepayment-percentage field next to it.
   :highlight: The "Online Payment" setting (red frame).
   :data: Demo company; prepayment 100%.
   :module: sale
   :notes: English UI, light theme, 1440px width, crop to the setting block.

Beneath the :guilabel:`Online Payment` option on the *Sales* :guilabel:`Settings` page, there's a
:guilabel:`Default Quotation Validity` field. In this field, there's the option to add a specific
number of days for quotations to remain valid by default.

To enable this feature on a standard quotation, click the checkbox for the :guilabel:`Payment`
feature option, located in the :guilabel:`Online confirmation` field, on the :guilabel:`Other Info`
tab.

.. screenshot:: sales-get-paid-quotation-option
   :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation) ‣ Other Info
   :shows: The Sales section of the Other Info tab of a quotation, with the "Online payment" option ticked.
   :highlight: The "Online payment" option (red frame).
   :data: Quotation S00021.
   :module: sale
   :notes: English UI, light theme, 1440px width, crop to the Sales group.

To enable this feature on a quotation template, click the checkbox for the :guilabel:`Payment`
feature option, located in the :guilabel:`Online confirmation` field of the quotation template form.

.. screenshot:: sales-get-paid-template-option
   :menu: Sales ‣ Configuration ‣ Quotation Templates ‣ (a template)
   :shows: A quotation template form with the "Online payment" confirmation option ticked and its prepayment percentage.
   :highlight: The "Online payment" option (red frame).
   :data: Template "Basic Furniture".
   :module: sale_management
   :notes: English UI, light theme, 1440px width, crop to the confirmation options.

Payment providers
=================

After activating the :guilabel:`Online Payment` feature, a link to configure :guilabel:`Payment
Providers` appears beneath it.

Clicking that link reveals a separate :guilabel:`Payment Providers` page, in which a large variety
of payment providers can be enabled, customized, and published.

.. screenshot:: sales-get-paid-providers-list
   :menu: Sales ‣ Configuration ‣ Online Payment: Payment Providers
   :shows: The payment-providers kanban with the available providers and their enabled/disabled state.
   :highlight: No highlight; the list of providers is the subject.
   :data: Demo database; "Wire Transfer" enabled, the rest disabled.
   :module: payment
   :notes: English UI, light theme, 1440px width, crop to the kanban.

.. seealso::
   :doc:`../../../finance/payment_providers`

Register a payment
==================

After opening quotations in their customer portal, customers can click :guilabel:`Accept \& Pay` to
confirm their order with an online payment.

.. screenshot:: sales-get-paid-portal-button
   :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation) ‣ Preview
   :shows: The customer portal view of a quotation with the "Accept & Pay" button at the top of the order.
   :highlight: The "Accept & Pay" button (red frame).
   :data: Quotation S00021.
   :module: sale
   :notes: English UI, light theme, 1440px width, crop to the portal header.

After clicking :guilabel:`Accept \& Pay`, customers are presented with :guilabel:`Validate Order`
pop-up window containing different options for them to make online payments, in the :guilabel:`Pay
with` section.

.. screenshot:: sales-get-paid-validate-popup
   :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation) ‣ Preview ‣ Accept & Pay
   :shows: The "Validate Order" pop-up window with the signature field and the "Pay with" list of enabled payment providers.
   :highlight: The "Pay with" provider list (red frame).
   :data: One enabled provider, "Wire Transfer".
   :module: sale
   :notes: English UI, light theme, 1440px width, crop to the pop-up. Use a throw-away signature.

.. note::
   Odoo will **only** offer payment options on the :guilabel:`Validate Order` pop-up window that
   have been published and configured on the :guilabel:`Payment Providers` page.

Once the customer selects their desired method of payment, they will click the :guilabel:`Pay`
button on the pop-up window to confirm the order. Odoo instantly notifies the assigned salesperson
upon order confirmation with an online payment.

.. screenshot:: sales-get-paid-chatter-confirmation
   :menu: Sales ‣ Orders ‣ Orders ‣ (a confirmed order)
   :shows: The chatter of the confirmed sales order with the automatic message logged after the online payment.
   :highlight: The payment-confirmation message (red frame).
   :data: Order S00021, amount paid in full.
   :module: sale
   :notes: English UI, light theme, 1440px width, crop to the chatter.

.. seealso::
   - :doc:`quote_template`
   - :doc:`get_signature_to_validate`
   - :doc:`../../../finance/payment_providers`

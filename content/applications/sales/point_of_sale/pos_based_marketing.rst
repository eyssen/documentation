==================
Marketing features
==================

Use your POS system to engage with customers directly by sending them promotional offers by email.

Storing contact details
=======================

This feature requires your customer's contact details, either their email address or phone number.

- **Email addresses**: automatically collected and saved in POS orders when sending a receipt by
  email.
- **Phone numbers**: to store phone numbers when sending receipts by SMS,

  #. Go to :menuselection:`Point of Sale --> Configuration --> Settings` and scroll to the
     :guilabel:`Bills & Receipts` section;
  #. Activate the :guilabel:`SMS Enabled` option, click :guilabel:`Save`, then return to the setting
     and select the :guilabel:`Receipt template` to use.

.. screenshot:: pos-marketing-sms-enabled
   :menu: Point of Sale ‣ Configuration ‣ Settings
   :shows: The "Bills & Receipts" section of the POS settings with the "SMS Enabled" checkbox ticked
      and the "Receipt template" field visible below it.
   :highlight: The "SMS Enabled" setting (red frame).
   :module: point_of_sale, pos_sms
   :notes: English UI, light theme, 1440px width, crop to the setting block.

If a customer's contact information is missing, it is automatically saved in the POS order when the
receipt is sent by email or SMS.

.. tip::
   From a POS order form, navigate to the :guilabel:`Contact Info` group under the
   :guilabel:`Extra Info` tab, then click the :icon:`fa-envelope` (:guilabel:`email`) icon next to
   the :guilabel:`Email` field to send a standalone message to that customer.

   .. screenshot:: pos-marketing-standalone-message
      :menu: Point of Sale ‣ Orders ‣ Orders ‣ (an order) ‣ Extra Info
      :shows: The "Extra Info" tab of a POS order form, with the "Contact Info" group showing the
         "Email" field and the envelope button next to it.
      :highlight: The envelope button next to the "Email" field (red frame).
      :module: point_of_sale
      :notes: English UI, light theme, 1440px width, crop to the "Contact Info" group.

Email marketing
===============

To send marketing emails to your customers from POS orders,

#. Go to :menuselection:`Point of Sale --> Orders --> Orders`;
#. Select the orders;
#. Click :guilabel:`Actions`, then :guilabel:`Send Email` from the dropdown menu.

Doing so opens an email composing form. Fill it in and hit :guilabel:`Send`.

.. screenshot:: pos-marketing-mail-composer
   :menu: Point of Sale ‣ Orders ‣ Orders ‣ Actions ‣ Send Email
   :shows: The email composer dialog opened from a selection of POS orders, with the recipients,
      subject, and body filled in and the "Send" button at the bottom.
   :module: point_of_sale, mail
   :notes: English UI, light theme, 1440px width; scale down to about 50 % of the page width.

.. tip::
   - Save some time by saving your content as a template. Click the vertical ellipsis button and
     select your template under the :guilabel:`Insert Template` section.
   - You can also save your content as template for later use. Click the vertical ellipsis button
     and select :guilabel:`Save as Template`.
   - The :doc:`Email CC and BCC </applications/general/companies/email_cc_bcc>` module adds
     :guilabel:`CC` and :guilabel:`BCC` fields to this composer, so a copy of the message can be
     sent to additional recipients.

.. note::
   - Fill in the :guilabel:`Mass Mailing Name` field to create a mass mailing and track its results
     in the :doc:`Email Marketing app <../../marketing/email_marketing>`.
   - If an email address is not related to an existing customer, a new customer is automatically
     created when sending marketing emails.

.. seealso::
   :doc:`Use the email marketing app for more advanced marketing features
   <../../marketing/email_marketing>`.

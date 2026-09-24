==============================================
Deliveries and invoices to different addresses
==============================================

People and businesses often use separate addresses for billing (invoicing) and shipping (delivery)
purposes. With the Odoo *Sales* app, contacts can have different specified addresses for delivery
and invoicing.

Settings
========

To properly utilize multiple addresses in Odoo, go to :menuselection:`Accounting app -->
Configuration --> Settings`, and scroll down to the :guilabel:`Customer Invoices` heading. Then,
tick the checkbox.

.. screenshot:: sales-different-addresses-setting
   :menu: Sales ‣ Configuration ‣ Settings
   :shows: The Settings page scrolled to the "Quotations & Orders" section with the "Customer Addresses" checkbox enabled.
   :highlight: The "Customer Addresses" setting (red frame).
   :data: Demo company.
   :module: sale
   :notes: English UI, light theme, 1440px width, crop to the setting block.

.. _sales/send_quotations/contact-form-config:

Contact form configuration
==========================

To add multiple addresses to a contact, go to :menuselection:`Sales app --> Orders --> Customers`,
and clear any default filters from the search bar. Then, click on the desired customer to open their
contact form.

.. tip::
   Contact forms can be accessed in the *Contacts* application, as well.

From the contact form, click :guilabel:`Edit`, and then select :guilabel:`Add`, which is located
under the :guilabel:`Contacts & Addresses` tab. Doing so reveals a :guilabel:`Create Contact` pop-up
form, in which additional addresses can be configured.

.. screenshot:: sales-different-addresses-contact-tab
   :menu: Sales ‣ Orders ‣ Customers ‣ (a customer) ‣ Contacts & Addresses
   :shows: The "Contacts & Addresses" tab of a contact form with the "Add" link visible and one existing address card.
   :highlight: The "Add" link in the Contacts & Addresses tab (red frame).
   :data: Customer "Deco Addict" with one existing delivery address.
   :module: base
   :notes: English UI, light theme, 1440px width, crop to the notebook.

On the :guilabel:`Create Contact` pop-up form, start by clicking the default :guilabel:`Other
Address` field to reveal a drop-down menu of address-related options.

Select any of the following options:

- :guilabel:`Contact`: adds another contact to the existing contact form.
- :guilabel:`Invoice Address`: adds a specific invoice address to the existing contact form.
- :guilabel:`Delivery Address`: adds a specific delivery address to the existing contact form.
- :guilabel:`Other Address`: adds an alternate address to the existing contact form.
- :guilabel:`Private Address`: adds a private address to the existing contact form.

Once an option is selected, proceed to enter the corresponding contact information that should be
used for the specified address type.

.. screenshot:: sales-different-addresses-create-contact-popup
   :menu: Sales ‣ Orders ‣ Customers ‣ (a customer) ‣ Contacts & Addresses ‣ Add
   :shows: The "Create Contact" pop-up window with the address-type radio buttons (Contact, Invoice Address, Delivery Address, Other Address) and the address fields.
   :highlight: The address-type radio buttons (red frame).
   :data: "Delivery Address" selected; name and street filled in.
   :module: base
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

Then, click :guilabel:`Save & Close` to save the address and close the :guilabel:`Create Contact`
window. Or, click :guilabel:`Save & New` to save the address and immediately input another one.

Address added to quotations
===========================

When a customer is added to a quotation, the :guilabel:`Invoice Address` and :guilabel:`Delivery
Address` fields autopopulate with the corresponding addresses specified on the customer's contact
form.

.. screenshot:: sales-different-addresses-quotation-fields
   :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation)
   :shows: The top of a quotation form where the Invoice Address and Delivery Address fields are filled automatically after selecting the customer.
   :highlight: The Invoice Address and Delivery Address fields (red frame).
   :data: Customer "Deco Addict" with different invoice and delivery addresses.
   :module: sale
   :notes: English UI, light theme, 1440px width, crop to the customer block.

The :guilabel:`Invoice Address` and :guilabel:`Delivery Address` can also be edited directly from
the quotation by clicking the :guilabel:`Edit` button, and then clicking the :guilabel:`➡️ (right
arrow)` internal link buttons next to each address line.

These addresses can be updated at any time to ensure accurate invoicing and delivery.

.. tip::
   If any changes are made on a form in Odoo, include *Contacts* forms, remember to click
   :guilabel:`Save` to save the changes to the database.

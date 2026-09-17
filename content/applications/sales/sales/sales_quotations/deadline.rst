===================
Quotation deadlines
===================

In the Odoo *Sales* application, it is possible to set deadlines on sales quotations. Doing so
encourages customers to act quickly during sales negotiations, for they might fear for missing out
on a good deal. As well, deadlines also can also act as protection for a company in case an order
has to be fulfilled at a price that is no longer profitable for the business.

Quotation expiration
====================

In Odoo *Sales*, there's the option to add an expiration date to a quotation.

To add an expiration date to a quotation, navigate to :menuselection:`Sales app`, and select a
desired quotation, or create a new one by clicking :guilabel:`New`.

On the quotation form, click the :guilabel:`Expiration` field to reveal a pop-up calendar. From this
pop-up calendar, select the desired month and date as the expiration date for the quotation.

.. screenshot:: sales-deadline-expiration-field
   :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation)
   :shows: A quotation form with the Expiration field filled in and its date picker open.
   :highlight: The Expiration field and the open calendar pop-up (red frame).
   :data: Demo quotation S00021 for "Deco Addict"; expiration one month ahead.
   :module: sale
   :notes: English UI, light theme, 1440px width, crop to the top of the quotation form.

.. tip::
   By clicking the :guilabel:`Preview` button on a quotation, Odoo clearly displays when that
   specific offer expires.

   .. screenshot:: sales-deadline-customer-preview
      :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation) ‣ Preview
      :shows: The customer portal preview of a quotation, showing the "Expires" date next to the quotation number.
      :highlight: The expiration date shown to the customer (red frame).
      :data: Same demo quotation S00021.
      :module: sale
      :notes: English UI, light theme, 1440px width, crop to the portal header.

Quotation template expiration
=============================

The Odoo *Sales* application also makes it possible to add a deadline expiration date to quotation
templates.

To add a deadline expiration date to a quotation template, navigate to :menuselection:`Sales app -->
Configuration --> Quotation Templates`, and either select the desired quotation template to which a
deadline should be added, or click :guilabel:`New` to build a new quotation template from scratch.

On the quotation template form, add a specific number of days to the :guilabel:`Quotation expires
after` field, located beneath the quotation template name. The number of days represents how long
the quotation will be valid for, before it expires.

.. screenshot:: sales-deadline-template-expires-after
   :menu: Sales ‣ Configuration ‣ Quotation Templates ‣ (a template)
   :shows: A quotation template form with the "Quotation expires after" field set to a number of days.
   :highlight: The "Quotation expires after" field (red frame).
   :data: Template "Basic Furniture", 30 days.
   :module: sale_management
   :notes: English UI, light theme, 1440px width, crop to the top of the template form.

Then, whenever that specific quotation template is used in a quote, an expiration date is
automatically calculated, based on the number of days designated above. However, this date can be
overwritten before sending the quotation to the customer.

.. seealso::
   :doc:`quote_template`

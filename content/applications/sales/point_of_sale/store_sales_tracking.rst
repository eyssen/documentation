====================
Store sales tracking
====================

If you advertise on Google or Meta, you also want to know which ads lead to purchases **in your
shops**. Odoo can report the paid orders of the :abbr:`PoS (Point of Sale)` as **offline store sales**
to the advertising platforms, so that they can measure the effect of the ads on your physical stores
and optimize the campaigns.

This feature is installed automatically when the Point of Sale and the Google or Meta app are
installed.

.. important::
   No cookie consent can be collected at the counter. Only the customers you identified are reported,
   and only if the settings of the platform allow store sales. Enable this feature only if your legal
   basis allows it, and mention it in your privacy policy. See
   :doc:`/applications/websites/website/tracking/privacy`.

Set up the store sales
======================

#. In the settings of the platform, enable the store sales:

   - Meta: go to :menuselection:`Meta --> Configuration --> Settings` and enable :guilabel:`Store
     Sales` in the :guilabel:`Conversions API` block (see :ref:`meta/capi/store-sales`).
   - Google Analytics 4: go to :menuselection:`Google --> Configuration --> Settings` and enable
     :guilabel:`Store Purchases` in the :doc:`Measurement Protocol
     </applications/websites/google/measurement_protocol>` options.

#. Go to :menuselection:`Point of Sale --> Configuration --> Settings`, select the point of sale in
   the :guilabel:`Point of Sale` field if needed, and in the :guilabel:`Report Store Sales` setting,
   select the :guilabel:`Report Sales to Ads` website. It is the website whose Google and Meta settings
   (pixel, dataset, tokens) apply to this point of sale.
#. Click :guilabel:`Save`.

.. screenshot:: pos-settings-store-sales
   :menu: Point of Sale ‣ Configuration ‣ Settings
   :shows: The Report Store Sales setting of the Point of Sale settings, with the Report Sales to Ads
      field set to a website.
   :highlight: The Report Sales to Ads field (red frame).
   :data: Website "My Website".
   :notes: English UI, light theme, 1440px width, crop to the setting.

Leave the field empty to report nothing for this point of sale. Each point of sale has its own
setting, so you can report some shops and not others.

Which orders are reported?
==========================

When a PoS order is **paid**, Odoo reports it as a purchase if:

- a website is selected for the point of sale;
- the order has a **customer** with an email address or a phone number (the platforms use them to
  match the sale with a person, after hashing);
- the total of the order is positive;
- the platform has the store sales enabled.

The order is sent once, with its date and time, its currency, its untaxed amount, its reference, and the
products (identifier, name, unit price, and quantity). The product identifier is the same as in the
:doc:`product feeds and the website events </applications/websites/ecommerce/tracking>`.

The customer's email, phone, name, and address are **hashed** with SHA-256 before being sent. The sales
without an identified customer are never reported.

.. tip::
   Ask your cashiers to identify the customer (a loyalty card or a customer account) so that the sale
   can be matched. The unidentified sales cannot be attributed to an ad.

The reports are put in the queue of the :doc:`server events
</applications/websites/website/tracking/server_events>` (:menuselection:`Website --> Configuration -->
Tracking & Consent --> Server Events`), where you can see whether they were sent.

.. seealso::
   - :doc:`/applications/websites/meta/conversions_api`
   - :doc:`/applications/websites/google/measurement_protocol`

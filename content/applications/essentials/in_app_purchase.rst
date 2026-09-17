======================
In-app purchases (IAP)
======================

.. |IAP| replace:: :abbr:`IAP (In-app purchases)`

In-app purchases (IAP) are optional services that enhance Odoo databases. Each service provides its
own specific features and functionality. A full list of services is available on the `Odoo IAP
Catalog <https://iap.odoo.com/iap/all-in-app-services>`_.

.. screenshot:: essentials-iap-catalog
   :menu: (Odoo IAP Catalog website) iap.odoo.com
   :shows: The IAP catalog page listing the available in-app services.
   :module: iap
   :notes: Odoo SA website; crop to the service list.

.. example::
   The :guilabel:`SMS` service sends text messages to contacts directly from the database, and the
   :guilabel:`Snailmail` service sends invoices by post.

|IAP| services do **not** need to be configured or set up before use. Odoo users can click on
the service in the app to activate it. However, each service requires its own prepaid credits, and
when they run out, users **must** :ref:`buy more <iap/buying_credits>` in order to keep using it.

.. note::
   IAP services are provided by Odoo SA (or third parties) and are paid separately from the
   database: the credits are bought on Odoo SA's IAP platform, independently of the hosting of the
   database.

.. _in_app_purchase/portal:

IAP services
============

|IAP| services are provided by Odoo, as well as third-parties, and have a wide range of uses.

The following |IAP| services are used by Community modules:

- :guilabel:`Partner Autocomplete`: automatically populates contact records with corporate data.
- :guilabel:`SMS`: sends SMS text messages to contacts directly from the database.
- :guilabel:`Lead Generation`: generates leads based on a set of criteria, and converts web visitors
  into quality leads and opportunities.
- :guilabel:`Snailmail`: sends customer invoices and follow-up reports by post, worldwide.

.. note::
   Some |IAP| services, such as document digitization (OCR), are only used by Enterprise modules and
   are therefore not available in this edition.

For more information on every service currently available (offered from developers other than Odoo),
visit the `Odoo IAP Catalog <https://iap.odoo.com/iap/all-in-app-services>`_.

Use IAP services
----------------

|IAP| services are automatically integrated with Odoo, and do **not** require users to configure any
settings. To use a service, interact with it wherever it appears in the database.

.. example::
   The following flow focuses on the *SMS* |IAP| service being used from a contact's record.

   This can be done by clicking the :icon:`fa-mobile` :guilabel:`SMS` icon within the database.

   .. screenshot:: essentials-iap-sms-icon
      :menu: Contacts ‣ (a contact)
      :shows: Contact form with the mouse over the Mobile field, showing the SMS icon next to the number.
      :highlight: The SMS icon.
      :data: Demo contact with a mobile number.
      :module: sms, contacts
      :notes: English UI, crop to the phone fields.

   One way to utilize the *SMS* |IAP| service with Odoo is showcased in the following steps:

   First, navigate to the :menuselection:`Contacts application`, and click on a contact with a
   mobile phone number entered in either the :guilabel:`Phone` or :guilabel:`Mobile` field of the
   contact form.

   Next, find the :icon:`fa-mobile` :guilabel:`SMS` icon that appears to the right of the
   :guilabel:`Phone` or :guilabel:`Mobile` fields. Click the :icon:`fa-mobile` :guilabel:`SMS` icon,
   and a :guilabel:`Send SMS Text Message` pop-up window appears.

   Type a message in the :guilabel:`Message` field of the pop-up window. Then, click the
   :guilabel:`Send SMS` button. Odoo then sends the message, via SMS, to the contact, and logs what
   was sent in the *chatter* of the contact's form.

   Upon sending the SMS message, the prepaid credits for the *SMS* |IAP| service are automatically
   deducted from the existing credits. If there are not enough credits to send the message, Odoo
   prompts the user to purchase more.

.. seealso::
   For more information on how to use various |IAP| services, and for more in-depth instructions
   related to SMS functionality in Odoo, review the documentation below:

   - :doc:`Lead mining <../sales/crm/acquire_leads/lead_mining>`
   - :doc:`Enrich your contacts base with Partner Autocomplete
     <../sales/crm/optimize/partner_autocomplete>`
   - :doc:`SMS Marketing <../marketing/sms_marketing>`

.. _in_app_purchase/credits:

IAP credits
===========

Every time an |IAP| service is used, the prepaid credits for that service are spent. Odoo prompts
the purchase of more credits when there are not enough credits left to continue using a service.
Email alerts can also be set up for when :ref:`credits are low <in_app_purchase/low-credits>`.

Credits are purchased in *Packs* from the `Odoo IAP Catalog
<https://iap.odoo.com/iap/all-in-app-services>`_, and pricing is specific to each service.

.. example::
   The `SMS service <https://iap.odoo.com/iap/in-app-services/1>`_ has four packs available, in
   denominations of:

   - :guilabel:`Starter Pack`: 10 credits
   - :guilabel:`Standard Pack`: 100 credits
   - :guilabel:`Advanced Pack`: 500 credits
   - :guilabel:`Expert Pack`: 1,000 credits

   .. screenshot:: essentials-iap-sms-packs
      :menu: (Odoo IAP website) SMS service page
      :shows: The four credit packs of the SMS service (Starter, Standard, Advanced, Expert).
      :module: sms
      :notes: Odoo SA website; crop to the packs.

   The number of credits consumed depends on the length of the SMS and the country of destination.

   For more information, refer to the :doc:`SMS Pricing and FAQ
   <../marketing/sms_marketing/pricing_and_faq>` documentation.

.. _iap/buying_credits:

Buy credits
-----------

If there are not enough credits to perform a task, the database automatically prompts the purchase
of more credits.

Users can check the current balance of credits for each service, and manually purchase more credits,
by navigating to the :menuselection:`Settings app --> Contacts section`, and beneath the
:guilabel:`Odoo IAP` setting, click :guilabel:`View My Services`.

Doing so reveals an :guilabel:`IAP Service` page, listing the various |IAP| services in the
database. From here, click an |IAP| service to open its :guilabel:`Account Information` page, where
additional credits can be purchased.

Manually buy credits
~~~~~~~~~~~~~~~~~~~~

To manually buy credits in Odoo, follow these steps:

First, go to the :menuselection:`Settings application` and type `IAP` in the search bar.
Alternatively users can scroll down to the :guilabel:`Contacts` section. Under the
:guilabel:`Contacts` section, where it says :guilabel:`Odoo IAP`, click :guilabel:`View My
Services`.

.. screenshot:: essentials-iap-view-services
   :menu: Settings ‣ General Settings ‣ Contacts
   :shows: The Contacts section with the "Odoo IAP" setting and its "View My Services" link.
   :highlight: "View My Services".
   :module: iap
   :notes: English UI, crop to the section.

Doing so reveals an :guilabel:`IAP Account` page, listing the various |IAP| services in the
database. From here, click an |IAP| service to open its :guilabel:`Account Information` page, where
additional credits can be purchased.

On the :guilabel:`Account Information` page, click the :guilabel:`Buy Credit` button. Doing so loads
a :guilabel:`Buy Credits for (IAP Account)` page in a new tab. From here, click :guilabel:`Buy` on
the desired pack of credits. Then, follow the prompts to enter payment details, and confirm the
order.

.. screenshot:: essentials-iap-buy-pack
   :menu: (Odoo IAP website) Buy Credits page
   :shows: The "Buy Credits" page of the SMS service with the four packs and their Buy buttons.
   :module: iap, sms
   :notes: Odoo SA website; crop to the packs.

Once the transaction is complete, the credits are available for use in the database.

.. _in_app_purchase/low-credits:

Low-credit notification
~~~~~~~~~~~~~~~~~~~~~~~

It is possible to be notified when credits are low, in order to avoid running out of credits, while
using an |IAP| service. To do that, follow this process:

Go to the :menuselection:`Settings application`, and type `IAP` in the search bar.
Under the :guilabel:`Contacts` section, where it says :guilabel:`Odoo IAP`, click :guilabel:`View My
Services`.

The available |IAP| accounts appear in a list view on the :guilabel:`IAP Account` page. From here,
click on the desired |IAP| account to view that service's :guilabel:`Account Information` page.

Set the :guilabel:`Email Alert Threshold` to the credit amount that should trigger a low-credit
alert when the balance falls below it. Next, select which user(s) should receive the email
notification using the :guilabel:`Email Alert Recipients` field.

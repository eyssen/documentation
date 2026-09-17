=================================
Product images with Google Images
=================================

Having appropriate product images in Odoo is useful for a number of reasons. However, if a lot of
products need images, assigning them can become incredibly time-consuming.

Fortunately, by configuring the *Google Custom Search* API within an Odoo database, finding product
images for products (based on their barcode) is extremely efficient.

.. _product_images/configuration:

Configuration
=============

In order to utilize *Google Custom Search* within an Odoo database, both the database and the Google
API must be properly configured.

.. note::
   Free Google accounts allow users to select up to 100 free images per day. If a higher amount is
   needed, a billing upgrade is required.

.. _product_images/google-api-dashboard:

Google API dashboard
--------------------

#. Go to the `Google Cloud Platform API & Services <https://console.developers.google.com/>`_ page
   to generate Google Custom Search API credentials. Then, log in with a Google account. Next, agree
   to their :guilabel:`Terms of Service` by checking the box, and clicking :guilabel:`Agree and
   Continue`.
#. From here, select (or create) an API project to store the credentials. Start by giving it a
   memorable :guilabel:`Project Name`, select a :guilabel:`Location` (if any), then click
   :guilabel:`Create`.
#. With the :guilabel:`Credentials` option selected in the left sidebar, click :guilabel:`Create
   Credentials`, and select :guilabel:`API key` from the drop-down menu.

   .. screenshot:: sales-product-images-gcp-credentials
      :menu: (Google Cloud console) ‣ APIs & Services ‣ Credentials
      :shows: The Credentials page of a Google Cloud project with the "Create credentials" menu open on "API key".
      :highlight: The "API key" menu item (red frame).
      :data: A throw-away Google Cloud project.
      :module: product_images
      :notes: English UI, light theme, crop to the header and menu.

#. Doing so reveals an :guilabel:`API key created` pop-up window, containing a custom :guilabel:`API
   key`. Copy and save :guilabel:`Your API key` in the pop-up window -- it will be used later. Once
   the key is copied (and saved for later use), click :guilabel:`Close` to remove the pop-up window.

   .. screenshot:: sales-product-images-gcp-api-key
      :menu: (Google Cloud console) ‣ APIs & Services ‣ Credentials ‣ Create credentials ‣ API key
      :shows: The "API key created" dialog showing the generated key and the copy button.
      :highlight: The copy button (red frame).
      :data: A throw-away key; blur or replace the key value.
      :module: product_images
      :notes: English UI, light theme, crop to the dialog. Use a throw-away secret and mask it.

#. On this page, search for `Custom Search API`, and select it.

   .. screenshot:: sales-product-images-gcp-search-api
      :menu: (Google Cloud console) ‣ API Library
      :shows: The API library search box with "Custom Search API" typed in and the matching result listed.
      :highlight: The "Custom Search API" result (red frame).
      :data: A throw-away Google Cloud project.
      :module: product_images
      :notes: English UI, light theme, crop to the search box and result.

#. From the :guilabel:`Custom Search API` page, enable the API by clicking :guilabel:`Enable`.

   .. screenshot:: sales-product-images-gcp-enable-api
      :menu: (Google Cloud console) ‣ API Library ‣ Custom Search API
      :shows: The Custom Search API page with the Enable button.
      :highlight: The Enable button (red frame).
      :data: A throw-away Google Cloud project.
      :module: product_images
      :notes: English UI, light theme, crop to the header.

.. _product_images/google-pse-dashboard:

Google Programmable Search dashboard
------------------------------------

#. Next, go to `Google Programmable Search Engine <https://programmablesearchengine.google.com/>`_,
   and click either of the :guilabel:`Get started` buttons. Log in with a Google account, if not
   already logged in.

   .. screenshot:: sales-product-images-pse-start
      :menu: (Google Programmable Search Engine)
      :shows: The Programmable Search Engine landing page with the "Get started" button.
      :highlight: The "Get started" button (red frame).
      :data: Signed in with a throw-away account.
      :module: product_images
      :notes: English UI, light theme, crop to the header.

#. On the :guilabel:`Create a new search engine` form, fill out the name of the search engine, along
   with what the engine should search, and be sure to enable :guilabel:`Image Search` and
   :guilabel:`SafeSearch`.

   .. screenshot:: sales-product-images-pse-create
      :menu: (Google Programmable Search Engine) ‣ Add
      :shows: The "Create a new search engine" form with the name, the "Search the entire web" option and the "Image search" toggle enabled.
      :highlight: The "Image search" toggle (red frame).
      :data: Search engine name "Odoo product images".
      :module: product_images
      :notes: English UI, light theme, crop to the form.

#. Validate the form by clicking :guilabel:`Create`.
#. Doing so reveals a new page with the heading: :guilabel:`Your new search engine has been
   created`.

   .. screenshot:: sales-product-images-pse-created
      :menu: (Google Programmable Search Engine) ‣ Add ‣ Create
      :shows: The confirmation page shown after the search engine is created, with the embed code containing the search engine ID.
      :highlight: The search engine ID inside the code snippet (red frame).
      :data: A throw-away search engine; mask the ID.
      :module: product_images
      :notes: English UI, light theme, crop to the code block. Use a throw-away secret and mask it.

#. From this page, click :guilabel:`Customize` to open the :menuselection:`Overview --> Basic` page.
   Then, copy the ID in the :guilabel:`Search engine ID` field. This ID is needed for the Odoo
   configuration.

   .. screenshot:: sales-product-images-pse-id
      :menu: (Google Programmable Search Engine) ‣ Overview ‣ Basic
      :shows: The Basic section of the search engine overview, showing the "Search engine ID" field with its copy button.
      :highlight: The "Search engine ID" field (red frame).
      :data: A throw-away search engine; mask the ID.
      :module: product_images
      :notes: English UI, light theme, crop to the field. Use a throw-away secret and mask it.

.. _product_images/setup-in-odoo:

Odoo
----

#. In the Odoo database, go to the :menuselection:`Settings app` and scroll to the
   :guilabel:`Integrations` section. From here, check the box beside :guilabel:`Google Images`.
   Then, click :guilabel:`Save`.

   .. screenshot:: sales-product-images-odoo-setting
      :menu: Settings ‣ General Settings
      :shows: The Integrations section of the general settings with the "Google Images" checkbox enabled and the API Key and Search Engine ID fields beneath it.
      :highlight: The API Key and Search Engine ID fields (red frame).
      :data: Throw-away credentials; mask both values.
      :module: product_images
      :notes: English UI, light theme, 1440px width, crop to the setting block. Use throw-away secrets and mask them.

#. Next, return to the :menuselection:`Settings app`, and scroll to the :guilabel:`Integrations`
   section. Then, enter the :guilabel:`API Key` and :guilabel:`Search Engine ID` in the fields
   beneath the :guilabel:`Google Images` feature.
#. Click :guilabel:`Save`.

.. _product_images/get-product-images:

Product images in Odoo with Google Custom Search API
====================================================

Adding images to products in Odoo can be done on any product or product variant. This process can be
completed in any Odoo application that provides access to product pages (e.g. *Sales* app,
*Inventory* app, etc.).

Below is a step-by-step guide detailing how to utilize the *Google Custom Search API* to assign
images to products in Odoo using the Odoo *Sales* application:

#. Navigate to the :guilabel:`Products` page in the *Sales* app (:menuselection:`Sales app -->
   Products --> Products`). Or, navigate to the :guilabel:`Product Variants` page in the *Sales* app
   (:menuselection:`Sales app --> Products --> Product Variants`).
#. Select the desired product that needs an image.

   .. note::
      Only products (or product variants) that have a barcode, but **not** an image, are processed.

      If a product with one or more variants is selected, each variant that matches the
      aforementioned criteria is processed.

#. Click the :guilabel:`Action ⚙️ (gear)` icon on the product page, and select :guilabel:`Get
   Pictures from Google Images` from the menu that pops up.

   .. screenshot:: sales-product-images-action-menu
      :menu: Sales ‣ Products ‣ Product Variants
      :shows: The product-variants list with several records selected and the gear (Actions) menu open on "Get Pictures from Google Images".
      :highlight: The "Get Pictures from Google Images" item (red frame).
      :data: Three product variants selected.
      :module: product_images
      :notes: English UI, light theme, 1440px width, crop to the open menu.

#. On the pop-up window that appears, click :guilabel:`Get Pictures`.

   .. screenshot:: sales-product-images-confirm-popup
      :menu: Sales ‣ Products ‣ Product Variants ‣ Get Pictures from Google Images
      :shows: The confirmation pop-up with the "Get Pictures" button.
      :highlight: The "Get Pictures" button (red frame).
      :data: Three variants selected.
      :module: product_images
      :notes: English UI, light theme, 1440px width, crop to the pop-up.

#. Once clicked, the image(s) will appear incrementally.

   .. note::
      Only the first 10 images are fetched immediately. If you selected more than 10, the rest are
      fetched as a background job.

      The background job processes about 100 images in a minute. If the quota authorized by Google
      (either with a free or a paid plan) is reached, the background job puts itself on hold for 24
      hours. Then, it will continue where it stopped the day before.

.. seealso::
   `Create, modify, or close your Google Cloud Billing account
   <https://cloud.google.com/billing/docs/how-to/manage-billing-account>`_

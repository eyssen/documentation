=================
Website analytics
=================

Website analytics helps website owners monitor how people use their site. It provides data on
visitor demographics, behavior, and interactions, helping improve websites and marketing strategies.

You can track your Odoo website's traffic using :ref:`analytics/plausible` or
:ref:`analytics/google-analytics`. We recommend using Plausible.io as it is privacy-friendly,
lightweight, and easy to use.

The Plausible Analytics dashboard is also integrated into Odoo and can be accessed
via :menuselection:`Website --> Reporting --> Analytics`.

.. _analytics/plausible:

Plausible.io
============

To use Plausible.io, create your own Plausible.io account (or use an existing one), then connect it
to the database as follows:

#. Create or sign in to a Plausible.io account using the following link: `<https://plausible.io/register>`_.
#. If you are creating a new account, go through the registration and activation steps.
   On the :guilabel:`Add website info` page, add the :guilabel:`Domain` of your website without
   including `www` (e.g., `example.com`) and change the :guilabel:`Reporting Timezone`,
   if necessary. Click :guilabel:`Install Plausible` to proceed to the next step. Ignore the
   :guilabel:`Manual installation` instructions and click :guilabel:`Start collecting data`.
#. Once done, click the Plausible.io logo in the upper-left part of the page to access your `list of
   websites <https://plausible.io/sites>`_, then click the :icon:`fa-ellipsis-v`
   (:guilabel:`ellipsis`) icon next to the website and select :icon:`fa-cog` :guilabel:`Settings`
   from the drop-down menu.

   .. screenshot:: website-analytics-plausible-gear-icon-settings
      :menu: (Plausible.io) ‣ Sites
      :shows: The Plausible.io site list with the three-dot menu of a site open on the Settings entry.
      :highlight: The Settings entry (red frame).
      :data: Site `example.com`.
      :module: website
      :notes: English UI, light theme, 1440px width.

#. In the sidebar, select :guilabel:`Visibility`, then click :guilabel:`Add Shared link`.
#. Enter a :guilabel:`Name`, leave the :guilabel:`Password (optional)` field empty, as the Plausible
   analytics dashboard integration in Odoo does not support it, then click :guilabel:`Create
   shared link`.

#. Copy the shared link.

   .. screenshot:: website-analytics-plausible-copy-shared-link
      :menu: (Plausible.io) ‣ Site settings ‣ Visibility
      :shows: The Plausible.io Visibility settings with the created shared link and its copy button.
      :highlight: The shared link (red frame).
      :data: Use a throw-away shared link.
      :module: website
      :notes: English UI, light theme, 1440px width.

#. In Odoo, go to :menuselection:`Website --> Configuration --> Settings`.
#. In the :guilabel:`SEO` section, enable :guilabel:`Plausible Analytics`, then paste the
   :guilabel:`Shared Link Auth` and click :guilabel:`Save`.

.. tip::
   If you have :doc:`multiple websites <../configuration/multi_website>`, add your websites to your
   Plausible.io account by going to `<https://plausible.io/sites>`_ and clicking :guilabel:`+ Add
   Website`. In Odoo, in the **Website settings**, make sure to select the website in the
   :guilabel:`Settings of Website` field at the top of the page before pasting the
   :guilabel:`Shared link`.

.. note::
   Odoo automatically pushes two custom goals: `Lead Generation` and `Shop`.

.. seealso::
   `Plausible Analytics documentation <https://plausible.io/docs>`_

.. _analytics/google-analytics:

Google Analytics
================

To follow your Odoo website's traffic with Google Analytics:

#. Create or sign in to a Google account using the following link: `<https://analytics.google.com>`_.
#. - If you are setting up Google Analytics for the first time, click :guilabel:`Start measuring`
     and go through the account creation step.
   - If you already have a Google Analytics account, sign in and click the :icon:`fa-cog` icon
     in the bottom-left corner of the page to access the **Admin** page. Then, click
     :guilabel:`+ Create` and select :guilabel:`Property` from the drop-down menu.

#. Complete the next steps: `property creation <https://support.google.com/analytics/answer/9304153?hl=en/&visit_id=638278591144564289-3612494643&rd=2#property>`_,
   business details and business objectives.
#. When you reach the **Data collection** step, choose the :guilabel:`Web` platform.

   .. screenshot:: website-analytics-ga-platform
      :menu: (Google Analytics) ‣ Admin ‣ Data streams
      :shows: The Google Analytics platform selection when creating a data stream, with the Web option.
      :highlight: The Web option (red frame).
      :data: Domain `example.com`.
      :module: website_google_analytics
      :notes: English UI, light theme, 1440px width.

#. Set up your data stream: Specify your :guilabel:`Website URL` and a :guilabel:`Stream name`, then
   click :guilabel:`Create & continue`.
#. Copy the :guilabel:`Measurement ID`.

   .. screenshot:: website-analytics-ga-measurement-id
      :menu: (Google Analytics) ‣ Admin ‣ Data streams ‣ (stream)
      :shows: The Google Analytics web stream details showing the Measurement ID to copy.
      :highlight: The Measurement ID (red frame).
      :data: Use a throw-away measurement ID.
      :module: website_google_analytics
      :notes: English UI, light theme, 1440px width.

#. In Odoo, go to :menuselection:`Website --> Configuration --> Settings`.
#. In the :guilabel:`SEO` section, enable :guilabel:`Google Analytics`, then paste the
   :guilabel:`Measurement ID` and click :guilabel:`Save`.

.. tip::
   If you have :doc:`multiple websites <../configuration/multi_website>` with separate domains, it
   is recommended to create `one property <https://support.google.com/analytics/answer/9304153?hl=en/&visit_id=638278591144564289-3612494643&rd=2#property>`_
   per domain. In Odoo, in the **Website settings**, make sure to select the website in the
   :guilabel:`Settings of Website` field at the top of the page before pasting the
   :guilabel:`Measurement ID`.

.. seealso::
   `Google documentation on setting up Analytics for a website
   <https://support.google.com/analytics/answer/1008015?hl=en/>`_

.. _analytics/google-tag-manager:

Google Tag Manager
==================

Google Tag Manager is a tag management system that allows you to easily update
measurement codes and related code fragments, collectively known as tags on your website or mobile
app, directly through the code injector.

.. note::
   :abbr:`GTM (Google Tag Manager)` is not an analytics tool and does not offer reporting features;
   it is used to collect data and works alongside Google Analytics to provide more detailed
   insights. In order to use GTM properly, it is recommended to configure Google Analytics as well.

   For more information refer to the `documentation on linking Google Analytics and
   Google Tag Manager <https://support.google.com/tagmanager/answer/9442095?hl=en>`_.

.. warning::
   - Some GTM tags use data layers (e.g., advanced eCommerce tracking data layers) to retrieve
     variables and send them to Google Analytics. Data layers are currently not managed in Odoo.
   - Google Tag Manager may not be compliant with local data protection regulations.

To configure GTM, proceed as follows:

#. Create or sign in to a Google account by going to https://tagmanager.google.com/.

#. In the :guilabel:`Accounts` tab, click :guilabel:`Create Account`.

#. Enter an :guilabel:`Account Name` and select the account's :guilabel:`Country`.

#. Enter your website's URL in the :guilabel:`Container name` field and select the :guilabel:`Target
   platform`.

#. Click :guilabel:`Create` and agree to the Terms of Service.

#. Copy the `<head>` and `<body>` codes from the popup window. Then, go to your website, click
   :guilabel:`Edit`, go to the :guilabel:`Theme` tab, scroll down to the
   :guilabel:`Advanced` section, then click :guilabel:`<head>` and :guilabel:`</body>` next to
   :guilabel:`Code Injection` to paste the codes.

   .. screenshot:: website-analytics-gtm-codes
      :menu: (Google Tag Manager)
      :shows: The Google Tag Manager install instructions showing the two code snippets to copy into the website's <head> and <body>.
      :highlight: The two code snippets (red frame).
      :data: Use a throw-away container ID.
      :module: website_google_analytics
      :notes: English UI, light theme, 1440px width.

.. tip::
   With the *Odoo Google Tag Manager* module (`website_google_tag`) installed, the container script
   does not have to be injected by hand. Go to :menuselection:`Website --> Configuration -->
   Settings`, enable :guilabel:`Google Tag Manager` under the Google Analytics setting, and enter
   the :guilabel:`Container ID` (e.g., `GTM-XXXXXXX`). The tag is then inserted on every page of
   that website, and the setting is per website, so each website can use its own container.

   .. screenshot:: website-analytics-gtm-container-id
      :menu: Website ‣ Configuration ‣ Settings
      :shows: The Website settings page with the Google Tag Manager setting enabled and the Container ID field filled in, right below the Google Analytics setting.
      :highlight: The Google Tag Manager setting and its Container ID field (red frame).
      :data: Use a throw-away container ID.
      :module: website_google_tag
      :notes: English UI, light theme, 1440px width, crop to the setting.

.. note::
   The data is collected in the marketing tools used to monitor the website (e.g., Google Analytics,
   Plausible, Facebook Pixel), not in Odoo.

.. seealso::
   `Setting up click triggers on Google
   <https://support.google.com/tagmanager/answer/7679320?hl=en&ref_topic=7679108&sjid=17684856364781654579-EU>`_

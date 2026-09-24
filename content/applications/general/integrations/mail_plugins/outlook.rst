==============
Outlook Plugin
==============

Outlook allows for third-party applications to connect in order to execute database actions from
emails. Odoo has a plugin for Outlook that allows for the creation of an opportunity from the email
panel.

Configuration
=============

The Outlook :doc:`Mail Plugin <../mail_plugins>` needs to be configured both on Odoo and Outlook.

.. _mail-plugin/outlook/enable-mail-plugin:

Enable Mail Plugin
------------------

First, enable the *Mail Plugin* feature in the database. Go to :menuselection:`Settings --> General
Settings --> Integrations`, enable :guilabel:`Mail Plugin`, and :guilabel:`Save` the configuration.

.. _mail-plugin/outlook/install-plugin:

Install the Outlook Plugin
--------------------------

Download (:menuselection:`Save Page As --> Web Page XML only`) the following XML file to upload
later: `https://download.odoocdn.com/plugins/outlook/manifest.xml
<https://download.odoocdn.com/plugins/outlook/manifest.xml>`_.

Next, open the Outlook mailbox, and select any email. After completing this, click on the
:guilabel:`More actions` button in the upper right-side and select :guilabel:`Get Add-ins`.

.. screenshot:: general-outlook-plugin-more-actions
   :menu: (Outlook on the web) ‣ (an email)
   :shows: The "More actions" (…) menu of an opened email with "Get Add-ins".
   :module: mail_plugin
   :notes: Outlook web interface; demo mailbox; example database URL.

.. tip::
   For locally installed versions of Microsoft Outlook, access the :guilabel:`Get Add-ins` menu item
   while in preview mode (**not** with a message open). First, click on the :guilabel:`...
   (ellipsis)` icon in the upper right of the previewed message, then scroll down, and click on
   :guilabel:`Get Add-ins`.

Following this step, select the :guilabel:`My add-ins` tab on the left-side.

.. screenshot:: general-outlook-plugin-my-add-ins
   :menu: (Outlook on the web) ‣ Get Add-ins
   :shows: The add-ins dialog with the "My add-ins" tab selected on the left.
   :module: mail_plugin
   :notes: Outlook web interface; demo mailbox; example database URL.

Under :guilabel:`Custom add-ins` towards the bottom, click on :guilabel:`+ Add a custom add-in`, and
then on :guilabel:`Add from file...`

.. screenshot:: general-outlook-plugin-custom-add-ins
   :menu: (Outlook on the web) ‣ Get Add-ins ‣ My add-ins
   :shows: The "Custom add-ins" section with "+ Add a custom add-in" ‣ "Add from file…".
   :module: mail_plugin
   :notes: Outlook web interface; demo mailbox; example database URL.

For the next step, attach the `manifest.xml` file downloaded above, and press :guilabel:`OK`. Next,
read the warning and click on :guilabel:`Install`.

.. screenshot:: general-outlook-plugin-add-in-warning
   :menu: (Outlook on the web) ‣ Add from file
   :shows: The custom add-in installation warning with the Install button.
   :module: mail_plugin
   :notes: Outlook web interface; demo mailbox; example database URL.

.. _mail-plugin/outlook/connect-database:

Connect the database
--------------------

Now, Outlook will be connected to the Odoo database. First, open any email in the Outlook mailbox,
click on the :guilabel:`More actions` button in the upper right-side, and select :guilabel:`Odoo for
Outlook`.

.. screenshot:: general-outlook-plugin-odoo-for-outlook
   :menu: (Outlook on the web) ‣ (an email) ‣ More actions
   :shows: The "More actions" menu with the "Odoo for Outlook" add-in entry.
   :module: mail_plugin
   :notes: Outlook web interface; demo mailbox; example database URL.

The right-side panel can now display **Company Insights**. At the bottom, click on
:guilabel:`Login`.

.. screenshot:: general-outlook-plugin-panel-login
   :menu: (Outlook on the web) ‣ Odoo for Outlook
   :shows: The Odoo side panel with the Login button at the bottom.
   :module: mail_plugin
   :notes: Outlook web interface; demo mailbox; example database URL.

.. note::
   Only a limited amount of **Company Insights** (*Lead Enrichment*) requests are available for
   free. This feature requires :ref:`prepaid credits <mail_plugins/pricing>`.

.. tip::
   If, after a short while, the panel is still empty, it is possible that the browser cookie
   settings prevented it from loading. Note that these settings also change if the browser is in
   "Incognito" mode.

   To fix this issue, configure the browser to always allow cookies on Odoo's plugin page.

   For Google Chrome, change the browser cookie settings by following the guide at:
   `https://support.google.com/chrome/answer/95647
   <https://support.google.com/chrome/answer/95647>`_
   and adding `download.odoo.com` to the list of :guilabel:`Sites that can always use cookies`.

   Once this is complete, the Outlook panel needs to be opened again.

Now, enter the Odoo database URL and click on :guilabel:`Login`.

.. screenshot:: general-outlook-plugin-database-url
   :menu: (Outlook on the web) ‣ Odoo for Outlook ‣ Login
   :shows: The side panel asking for the Odoo database URL, with the Login button.
   :module: mail_plugin
   :notes: Outlook web interface; demo mailbox; example database URL.

Next, click on :guilabel:`Allow` to open the pop-up window.

.. screenshot:: general-outlook-plugin-new-window-warning
   :menu: (Outlook on the web) ‣ Odoo for Outlook
   :shows: The pop-up asking to allow opening a new window, with the Allow button.
   :module: mail_plugin
   :notes: Outlook web interface; demo mailbox; example database URL.

If the user isn't logged into the database, enter the credentials. Click on :guilabel:`Allow` to let
the Outlook Plugin connect to the database.

.. screenshot:: general-outlook-plugin-odoo-permission
   :menu: (Odoo) plugin authorization page
   :shows: The Odoo page asking to allow the Outlook plugin to access the database, with the Allow button.
   :module: mail_plugin
   :notes: Outlook web interface; demo mailbox; example database URL.

.. _mail-plugin/outlook/add-shortcut:

Add a shortcut to the plugin
----------------------------

By default, the Outlook Plugin can be opened from the *More actions* menu. However, to save time,
it's possible to add it next to the other default actions.

In the Outlook mailbox, click on :guilabel:`Settings`, then on :guilabel:`View all Outlook
settings`.

.. screenshot:: general-outlook-plugin-all-settings
   :menu: (Outlook on the web) ‣ Settings
   :shows: The settings panel with "View all Outlook settings".
   :module: mail_plugin
   :notes: Outlook web interface; demo mailbox; example database URL.

Now, select :guilabel:`Customize actions` under :guilabel:`Mail`, click on :guilabel:`Odoo for
Outlook`, and then :guilabel:`Save`.

.. screenshot:: general-outlook-plugin-customize-actions
   :menu: (Outlook on the web) ‣ Settings ‣ Mail ‣ Customize actions
   :shows: The Customize actions page with "Odoo for Outlook" ticked.
   :module: mail_plugin
   :notes: Outlook web interface; demo mailbox; example database URL.

Following this step, open any email; the shortcut should be displayed.

.. screenshot:: general-outlook-plugin-shortcut
   :menu: (Outlook on the web) ‣ (an email)
   :shows: An opened email with the Odoo "O" shortcut icon in the action bar.
   :module: mail_plugin
   :notes: Outlook web interface; demo mailbox; example database URL.

Using the plugin
----------------

Now that the plug-in is installed and operational, all that needs to be done to create a lead is to
click on the `O` [Odoo icon] or navigate to :guilabel:`More actions` and click on :guilabel:`Odoo
for Outlook`. The side panel will appear on the right-side, and under :guilabel:`Opportunities`
click on :guilabel:`New`. A new window with the created opportunity in the Odoo database will
populate.

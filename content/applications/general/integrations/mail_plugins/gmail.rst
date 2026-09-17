============
Gmail Plugin
============

The *Gmail Plugin* integrates an Odoo database with a Gmail inbox, so users can keep track of all
their work between Gmail and Odoo, without losing any information.

Installation and configuration
==============================

Follow the steps below to configure the Gmail Plugin for a database hosted on your own domain.

.. note::
   As part of their security guidelines, Google requires add-on creators to provide a list of URLs
   that can be used in actions and redirections launched by the add-on. This protects users by
   ensuring, for example, that no add-on redirects users toward a malicious website. (Read more on
   `Google Apps Script <https://developers.google.com/apps-script/manifest/allowlist-url>`_.)

   The Gmail Plugin published on the Google Workspace Marketplace only allows the domains listed by
   its publisher (`odoo.com`). Databases hosted on other domains therefore need their own copy of
   the plugin, as described below.

Install the Gmail Plugin
------------------------

First, access the `GitHub repository <https://github.com/odoo/mail-client-extensions>`_ for the
Odoo Mail Plugins. Next, click on the green :guilabel:`Code` button. Then, click
:guilabel:`Download ZIP` to download the Mail Plugin files onto the user's computer.

.. screenshot:: general-gmail-plugin-download-zip
   :menu: (GitHub) odoo/mail-client-extensions
   :shows: The GitHub repository page with the green "Code" button open and "Download ZIP" highlighted.
   :highlight: "Download ZIP".
   :module: mail_plugin
   :notes: GitHub website.

Open the ZIP file on the computer. Then, go to :menuselection:`mail-client-extensions-master -->
gmail --> src --> views`, and open the :file:`login.ts` file using any text editor software,
such as Notepad (Windows), TextEdit (Mac), or Visual Studio Code.

Delete the following three lines of text from the :file:`login.ts` file:

.. code-block::

   if (!/^https:\/\/([^\/?]*\.)?odoo\.com(\/|$)/.test(validatedUrl)) {
        return notify("The URL must be a subdomain of odoo.com");
   }

This removes the `odoo.com` domain constraint from the Gmail Plugin program.

Next, in the ZIP file, go to :menuselection:`mail-client-extensions-master --> gmail`, and open the
file called :guilabel:`appsscript.json`. In the :guilabel:`urlFetchWhitelist` section, replace all
the references to `odoo.com` with the domain of the Odoo database.

Then, in the same :guilabel:`gmail` folder, open the file called :guilabel:`README.md`. Follow the
instructions in the :guilabel:`README.md` file to push the Gmail Plugin files as a Google Project.

.. note::
   The computer must be able to run Linux commands in order to follow the instructions on the
   :guilabel:`README.md` file.

After that, share the Google Project with the Gmail account that the user wishes to connect to Odoo.
Then, click :guilabel:`Publish` and :guilabel:`Deploy from manifest`. Lastly, click
:guilabel:`Install the add-on` to install the Gmail Plugin.

Configure the Odoo database
---------------------------

The :guilabel:`Mail Plugin` feature must be enabled in the Odoo database in order to use the Gmail
Plugin. To enable the feature, go to :menuselection:`Settings --> General Settings`. Under the
:guilabel:`Integrations` section, activate :guilabel:`Mail Plugin`, and then click :guilabel:`Save`.

.. screenshot:: general-gmail-plugin-setting
   :menu: Settings ‣ General Settings ‣ Integrations
   :shows: The "Mail Plugin" setting enabled.
   :highlight: The Mail Plugin setting.
   :module: mail_plugin
   :notes: English UI, crop to the setting.

Configure the Gmail inbox
-------------------------

In the Gmail inbox, a purple Odoo icon is now visible on the right side panel. Click on the Odoo
icon to open up the Odoo plugin window. Then, click on any email in the inbox. Click
:guilabel:`Authorize Access` in the plugin window to grant Odoo access to the Gmail inbox.

.. screenshot:: general-gmail-plugin-authorize
   :menu: (Gmail) side panel ‣ Odoo
   :shows: The Odoo plugin panel in Gmail with the "Authorize Access" button.
   :highlight: The button.
   :module: mail_plugin
   :notes: Gmail web interface; demo mailbox.

Next, click :guilabel:`Login`. Then, enter the URL of the Odoo database that the user wishes to
connect to the Gmail inbox, and log in to the database.

.. note::
   Use the general URL for the database, not the URL of a specific page in the database. For
   example, use `https://erp.mycompany.com`, not
   `https://erp.mycompany.com/odoo/action-menu`.

Finally, click :guilabel:`Allow` to let Gmail access the Odoo database. The browser will then show
a :guilabel:`Success!` message. After that, close the window. The Gmail inbox and Odoo database are
now connected.

================
Apps and modules
================

:ref:`Install <general/install>`, :ref:`upgrade <general/upgrade>` and :ref:`uninstall
<general/uninstall>` any needed apps and modules from the :menuselection:`Apps` dashboard.

By default, an :guilabel:`Apps` filter is applied. To search for modules too, select
:guilabel:`Extra` from the :icon:`fa-filter` :guilabel:`Filters`.

.. screenshot:: general-apps-search-filter
   :menu: Apps
   :shows: The Apps dashboard with the search dropdown open: Filters "Apps", "Extra", "Installed",
      "Not Installed"; "Extra" is ticked.
   :highlight: The "Extra" filter.
   :module: base
   :notes: English UI, crop to the search bar and dropdown.

.. warning::
   Adding or removing apps can significantly affect other apps in the database. Consider carefully
   or test the changes in a staging environment before proceeding.

   - **Administrators manage the database**: The administrator of the database is responsible for
     its usage, as they know best how their organization works.
   - **Odoo apps can have dependencies**: Installing some apps and features with dependencies may
     also install additional apps and modules that are technically required, even if database users
     do not actively use them.
   - **Duplicate the database to test apps**: Testing on a duplicate database reveals what app
     dependencies may be required or what data may be erased. Ask your hosting provider or system
     administrator for a test copy of the database, or see :doc:`on-premise database management
     <../../administration/on_premise>`.

.. _general/install:

Install apps and modules
========================

From the main Odoo dashboard, open the :menuselection:`Apps` app, then click on the search bar to
find the app to be installed or scroll to find it. From here, click :guilabel:`Activate` on the
app's card.

.. note::
   If the app or module to be installed is not listed, update the app list by activating
   :ref:`developer mode <developer-mode>`, and then go to :menuselection:`Apps --> Update Apps
   List`, and then click :guilabel:`Update`. Modules that are not present on the server (e.g.,
   custom or third-party modules) must first be deployed by the system administrator or the hosting
   provider.

.. tip::
   With :ref:`developer mode <developer-mode>` activated, :menuselection:`Apps --> Import Module`
   allows installing a *data module* from a `.zip` file (views, data, and static files only, without
   Python code). Tick :guilabel:`Load demo data` if needed, then click :guilabel:`Install`.

.. _general/upgrade:

Upgrade apps and modules
========================

With each :doc:`new Odoo release </administration/supported_versions>`, new improvements or app
features are added. Upgrade the app to use these new improvements and features.

Go to :menuselection:`Apps` and then on the app to upgrade, click the :icon:`fa-ellipsis-v`
:guilabel:`(vertical ellipsis)` icon and select :guilabel:`Upgrade`.

.. _general/uninstall:

Uninstall apps and modules
==========================

.. danger::
   Uninstalling apps also deletes their database records. Test uninstalling apps on a duplicated
   database before removing apps on a production database.

.. note::
   Some apps have dependencies, meaning that one app requires another. Therefore, uninstalling one
   app may uninstall multiple apps and modules.

Go to :menuselection:`Apps` and then on the app to uninstall, click the :icon:`fa-ellipsis-v`
:guilabel:`(vertical ellipsis)` icon and select :guilabel:`Uninstall` to open the
:guilabel:`Uninstall module` pop-up window.

The :guilabel:`Apps to Uninstall` section lists the applications to be uninstalled.

.. tip::
   Select the :guilabel:`Show All` checkbox to display all module dependencies.

The :guilabel:`Documents to Delete` section lists the database records to be deleted.

To proceed with uninstalling the app, its dependencies, and all related database records, click
:guilabel:`Uninstall`.

.. screenshot:: general-apps-uninstall-menu
   :menu: Apps (filter: Installed)
   :shows: An installed app's card with its vertical ellipsis menu open: "Module Info", "Upgrade",
      "Uninstall".
   :highlight: The "Uninstall" entry.
   :module: base
   :notes: English UI, crop to the card and menu.

.. example::
   The **Restaurant** app requires the **Point of Sale** app to function, so uninstalling the
   **Point of Sale** app will also uninstall the **Restaurant** app, and any related records.

   .. screenshot:: general-apps-uninstall-dependencies
      :menu: Apps ‣ Point of Sale ‣ ⋮ ‣ Uninstall
      :shows: The uninstall confirmation dialog listing the apps/modules that will also be uninstalled
         (e.g., Restaurant) and the records that will be deleted, with the Uninstall and Discard
         buttons.
      :highlight: The list of dependent apps.
      :module: base, point_of_sale, pos_restaurant
      :notes: English UI, crop to the dialog.

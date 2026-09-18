:show-content:

==========
Dashboards
==========

.. toctree::
   :titlesonly:

   dashboards/my_dashboard
   dashboards/custom_dashboards

The **Dashboards** app centralizes pre-configured dashboards that display real-time data from the
database, giving an overview of key business metrics without having to open each app's reporting
views.

Depending on their :ref:`access rights <dashboards/access-and-sharing>`, users can:

- :ref:`consult dashboards <dashboards/consult-dashboards>`, including :ref:`standard,
  pre-configured dashboards <dashboards/consult-dashboards/standard>`;
- :ref:`interact with dashboards <dashboards/use-dashboards/interact>` using filters and by
  accessing underlying data;
- :ref:`share a snapshot of a dashboard <dashboards/access-and-sharing/sharing>` with internal users
  who do not have the appropriate access rights, or with external users;
- centralize frequently consulted views on a personal :doc:`dashboards/my_dashboard` page;
- build fully configurable dashboards with charts, |KPIs|, tables, and shortcuts using the
  :doc:`dashboards/custom_dashboards`.

.. |KPIs| replace:: :abbr:`KPIs (Key Performance Indicators)`

.. _dashboards/consult-dashboards:

Consult dashboards
==================

On the main Dashboards page, the left panel lists all :ref:`dashboards a user has access to
<dashboards/access-and-sharing>`, grouped by section. Clicking on a dashboard name opens that
dashboard in the main part of the page.

.. tip::
   Clicking the :icon:`fa-angle-double-left` :guilabel:`(double chevron)` icon at the top of the
   left panel collapses the panel, maximizing the space available for dashboards.

.. _dashboards/consult-dashboards/standard:

Standard dashboards
-------------------

Depending on which apps are installed, a series of standard dashboards is available by default,
e.g., for Sales, Invoicing, Inventory, Expenses, or Point of Sale. These pre-configured dashboards
present data on specific aspects of the topic in tables and charts, while dashboard-specific filters
allow users to tailor the view to their needs.

.. example::
   Within the :guilabel:`Sales` section in the Dashboards app, the :guilabel:`Sales` dashboard gives
   an overview of the number of quotations and orders, the revenue, and the average order value, as
   well as a chart showing monthly sales. It also includes tables listing top quotations and sales
   orders, top-performing products and salespeople, and top countries served.

   A series of pre-configured global filters at the top of the dashboard allows the entire dashboard
   to be filtered by, e.g., product or sales team. A default value of `Last 90 days` in the period
   filter means data from the previous 90 days is automatically retrieved every time the dashboard
   is opened or refreshed.

   .. screenshot:: productivity-dashboards-sales
      :menu: Dashboards ‣ Dashboards
      :shows: The Sales dashboard open in the Dashboards app, with the section list in the left panel, the KPI row at the top, the monthly sales chart and the global filters.
      :data: Demo company "YourCompany HU" with sales data over the last 12 months.
      :module: spreadsheet_dashboard, spreadsheet_dashboard_sale
      :notes: English UI, light theme, 1440px width.

.. note::
   Standard dashboards are read-only. Their underlying spreadsheets cannot be edited in this
   database; to build your own dashboards, use the :doc:`dashboards/custom_dashboards`.

.. _dashboards/use-dashboards/interact:

Interact with dashboards
------------------------

In addition to consulting a dashboard for a high-level overview of key business data, it is also
possible to interact with the dashboard for a more detailed analysis:

- **Filter data**: Most standard dashboards have one or more global filters, shown as dropdown
  menus, at the top of the dashboard. These filters apply to all the data on the dashboard at the
  same time, for example, to show data only for a specific period of time, or for one or more
  salespeople or customers.

- **Open underlying database records**: To access database records referenced by a dashboard, click
  on the relevant value in a table or on a data point on a chart. Doing so opens either the
  individual record, or, in the case of charts or tables displaying consolidated data, a list of the
  referenced records.

- **Open underlying database views**: To access the view from which the data for a specific chart
  or table is retrieved, click on the title of the chart or table. Doing so opens the corresponding
  list view, pivot view, or graph view.

.. tip::
   To return to a dashboard after drilling down to underlying records or views, click the
   :guilabel:`Dashboards` breadcrumb at the upper left of the page.

.. _dashboards/configuration:

Configuration
=============

.. note::
   Only a user with the appropriate :ref:`access rights <access-rights/groups>` can configure
   dashboards and dashboard sections.

To manage dashboard sections, go to :menuselection:`Dashboards --> Configuration --> Dashboards`.
The following actions are possible at the level of dashboard sections:

- **Change the order of dashboard sections** by using the :icon:`oi-draggable` :guilabel:`(drag
  handle)` icon to move a section to a new position.

- **Duplicate a dashboard section** by selecting the relevant section name, clicking the
  :icon:`fa-cog` :guilabel:`Actions` button, and then :icon:`fa-clone` :guilabel:`Duplicate`. The
  dashboards within the section are not duplicated.

- **Delete a dashboard section** by selecting the relevant section name, clicking the :icon:`fa-cog`
  :guilabel:`Actions` button, then :icon:`fa-trash-o` :guilabel:`Delete`.

   .. tip::
      Standard, pre-installed dashboard sections cannot be deleted; custom dashboard sections, on
      the other hand, can be deleted.

- **Create a new dashboard section** by clicking :guilabel:`New`, then entering the section name.

Clicking on an individual dashboard section lists all dashboards within that section. The following
actions are possible:

- **Change the order of a dashboard within its section** by using the :icon:`oi-draggable`
  :guilabel:`(drag handle)` icon to move the dashboard to a new position.

- **Edit the name of a dashboard section or dashboard** by clicking the name and modifying it.

- **Add or remove user groups** to :ref:`control access to the dashboard
  <dashboards/access-and-sharing>`.

- **Select a company** if, in a :doc:`multi-company <../general/companies/multi_company>` database,
  the dashboard should only be visible to users of one company. If this field is left blank, the
  dashboard is visible to all users with the appropriate access rights, regardless of which company
  is currently selected in the database.

- **Unpublish a dashboard** by disabling the :guilabel:`Is Published` toggle. Unpublished dashboards
  are no longer listed in the left panel of the Dashboards app.

- **Delete a dashboard** by clicking the :icon:`fa-trash` :guilabel:`(trash)` icon.

  .. tip::
     A standard dashboard that is deleted is reinstalled when the corresponding app is updated.

.. screenshot:: productivity-dashboards-configuration
   :menu: Dashboards ‣ Configuration ‣ Dashboards
   :shows: A dashboard section opened in Configuration, listing its dashboards with the drag handle, the Group column, the Company column and the "Is Published" toggle.
   :highlight: The "Group" and "Is Published" columns (red frame).
   :data: Section "Sales" with the standard Sales dashboard.
   :module: spreadsheet_dashboard
   :notes: English UI, light theme, 1440px width.

.. _dashboards/access-and-sharing:

Access rights and sharing
=========================

.. _dashboards/access-and-sharing/viewing:

Consulting dashboards
---------------------

The *right to view and interact with a dashboard* is based on :ref:`user groups
<access-rights/groups>`, and is managed in the :ref:`Configuration settings
<dashboards/configuration>` of the Dashboards app. Only users who are part of a group that has been
granted access to a specific dashboard see that dashboard in the left-hand panel on the main
Dashboards page.

However, the *visibility of dynamic data within a dashboard* is handled separately. This is based on
a user's :ref:`access rights <access-rights/users>` to the model from which the data has been
retrieved, and takes into account any record rules that may restrict access.

.. important::
   User permissions are taken into account when a user opens a dashboard, with the dashboard only
   being populated with data the user is authorized to see. This means that a user could in theory
   be able to view a dashboard but, due to a lack of appropriate permissions, not be able to see the
   data the dashboard's creator intended to be displayed.

   Therefore, it is crucial to take user permissions into consideration when granting dashboard
   access to groups.

.. example::
   Granting the user group `Sales / User: Own Documents Only` access to the :guilabel:`Sales`
   dashboard would serve little purpose. While users belonging to that group would be able to view
   and interact with the dashboard, they would only see data related to their own sales, rendering
   the overall dashboard misleading.

To manage users' rights to view and interact with a dashboard:

#. In the Dashboards app, go to :menuselection:`Configuration --> Dashboards`.
#. From the list of dashboard sections, open the relevant section.
#. On the line of the relevant dashboard, in the :guilabel:`Group` column:

   - add a user group by clicking the field until a dropdown with user groups appears, then
     selecting the appropriate user group. In the dropdown, click :guilabel:`Search More` to access
     the full list of user groups;
   - remove a user group by clicking the relevant group name, then clicking :icon:`fa-times`
     :guilabel:`(Delete)`.

.. _dashboards/access-and-sharing/sharing:

Share dashboard snapshot
------------------------

To share a frozen version of a dashboard with an internal user who does not have the appropriate
access, or with an external party, click :icon:`fa-share-alt` :guilabel:`Share` at the top-right of
the page, then click the :icon:`fa-clone` :guilabel:`(copy)` icon to copy a shareable link to the
clipboard. Anyone with the link can open the read-only snapshot without logging in.

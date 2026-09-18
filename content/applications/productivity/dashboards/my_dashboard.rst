============
My Dashboard
============

**My Dashboard** allows you to centralize the views you consult most regularly, making it possible
to see critical tasks at a glance without having to first navigate through multiple apps. Unlike the
other dashboards of the Dashboards app, My Dashboard is built directly from database views.

Views inserted in My Dashboard are fully dynamic and retain many features of the source view, e.g.,
sorting of lists, changing the measures used for a pivot table, changing the chart type, or clicking
on a value or data point to view the underlying record(s).

.. tip::
   It is not possible to change the domain, i.e., the filtering or grouping, of a view that has been
   added to My Dashboard. To change the domain, make the necessary changes in the original view,
   then re-insert the view in My Dashboard and delete the originally inserted view.

Add views
=========

Most Odoo views can be added to My Dashboard, including:

- multiple record views like list and kanban
- timeline views like calendar and :ref:`gantt <dashboards/my-dashboard/gantt>`
- reporting views like pivot and graph

To add a view to My Dashboard:

#. With the relevant view open in your database, click the :icon:`fa-cog` :guilabel:`(Actions)` icon
   beside the name of the view, then :menuselection:`Dashboard`.
#. Under :guilabel:`Add to my Dashboard`, rename the view if desired, then click :guilabel:`Add`.

   .. screenshot:: productivity-my-dashboard-add-view
      :menu: Sales ‣ Orders ‣ Quotations
      :shows: The "Actions" cog menu open on a list view with the "Dashboard" entry expanded, showing the "Add to my Dashboard" field with a name and the "Add" button.
      :highlight: The "Add to my Dashboard" block (red frame).
      :data: Demo company "YourCompany HU"; view renamed to "My quotations".
      :module: board
      :notes: English UI, light theme, 1440px width, crop to the dropdown.

#. Refresh the page.

The added view is now visible as a widget in My Dashboard in the Dashboards app.

.. tip::
   If added views are not showing in My Dashboard, refresh the browser page.

Customize layout
================

When at least one view has been added to My Dashboard, the page can be customized as follows:

- **Change the layout of the page**: Click :guilabel:`Change Layout` in the top-right corner and
  select the desired layout.

  .. tip::
     For multi-column layouts, the column limits are identified by :icon:`fa-caret-left`
     :guilabel:`(left caret)` and :icon:`fa-caret-right` :guilabel:`(right caret)` icons at the
     bottom of the page. If needed, scroll to the bottom of the page to see the column limits.

     .. screenshot:: productivity-my-dashboard-column-limits
        :menu: Dashboards ‣ My Dashboard
        :shows: The bottom of My Dashboard with the left and right caret icons that mark the column limits of a two-column layout.
        :highlight: The caret icons marking the column limits (red frame).
        :module: board
        :notes: English UI, light theme, crop to the bottom of the page.

- **Collapse and expand widgets**: By default, an inserted widget is shown fully expanded. To
  collapse, or minimize, a widget, and show only the title, click the :icon:`fa-window-minimize`
  :guilabel:`(minimize)` icon at the top right of the widget. To expand a widget, click the
  :icon:`fa-window-maximize` :guilabel:`(maximize)` icon.
- **Move widgets**: Drag and drop widgets to the desired location in the same column or a different
  column.
- **Remove widgets**: To remove a widget from the page, click the :icon:`fa-times`
  :guilabel:`(remove)` icon.

.. _dashboards/my-dashboard/gantt:

Gantt views
===========

Gantt views are provided by the *Web Gantt* module, which adds a timeline view type to models that
have a start and a stop date, e.g., project tasks or manufacturing orders. When a model offers a
Gantt view, it can be added to My Dashboard like any other view.

.. note::
   Gantt views require the *Web Gantt* (``web_gantt``) module.

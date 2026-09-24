=======================
Work order dependencies
=======================

.. |BOM| replace:: :abbr:`BoM (Bill of Materials)`

When manufacturing certain products, specific operations may need to be completed before others can
begin. In order to ensure operations are carried out in the correct order, Odoo *Manufacturing*
features a *work order dependencies* setting. Enabling this setting allows for operations on a Bill
of Materials (BoM) to be *blocked* by other operations that should occur first.

Configuration
=============

The *work order dependencies* setting is not enabled by default. To enable it, begin by navigating
to :menuselection:`Manufacturing --> Configuration --> Settings`. Then, enable the :guilabel:`Work
Orders` setting, if it is not already active.

After enabling the :guilabel:`Work Orders` setting, the :guilabel:`Work Order Dependencies` setting
appears below it. Enable :guilabel:`Work Order Dependencies`, then click :guilabel:`Save` to confirm
the changes.

Add dependencies to BoM
=======================

Work order dependencies are configured on a product's |BOM|. To do so, navigate to
:menuselection:`Manufacturing --> Products --> Bills of Materials`, then select a |BOM|, or create a
new one by clicking :guilabel:`New`.

.. admonition:: Learn more

   For a complete guide on how to properly configure a new |BOM|, see the documentation on
   :doc:`creating a bill of materials <../basic_setup/bill_configuration>`.

On the |BOM|, click on the :guilabel:`Miscellaneous` tab, then enable the :guilabel:`Operation
Dependencies` checkbox. This makes a new :guilabel:`Blocked By` option available in the settings of
the :guilabel:`Operations` tab.

.. screenshot:: manufacturing-work-order-deps-operation-dependencies
   :menu: Manufacturing ‣ Products ‣ Bills of Materials ‣ (BoM) ‣ Miscellaneous tab
   :shows: The Miscellaneous tab of a BoM with the "Operation Dependencies" checkbox ticked.
   :highlight: The "Operation Dependencies" checkbox.
   :data: BoM for product "Product A".
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the tab.

Next, click on the :guilabel:`Operations` tab. On the top-right of the tab, click on the tab's
:guilabel:`settings` button, then enable the :guilabel:`Blocked By` checkbox. This makes a
:guilabel:`Blocked By` field appear for each operation on the :guilabel:`Operations` tab.

.. screenshot:: manufacturing-work-order-deps-operations-settings
   :menu: Manufacturing ‣ Products ‣ Bills of Materials ‣ (BoM) ‣ Operations tab ‣ settings
   :shows: The optional-columns menu of the Operations tab list with the "Blocked By" checkbox ticked.
   :highlight: The "Blocked By" checkbox.
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the dropdown.

In the line of the operation that should be blocked by another operation, click the
:guilabel:`Blocked By` field, and an :guilabel:`Open: Operations` pop-up window appears. In the
:guilabel:`Blocked By` drop-down field on the pop-up window, select the blocking operation that must
be completed *before* the operation that is blocked.

.. screenshot:: manufacturing-work-order-deps-blocked-by
   :menu: Manufacturing ‣ Products ‣ Bills of Materials ‣ (BoM) ‣ Operations tab ‣ Blocked By
   :shows: The "Open: Operations" pop-up window with the "Blocked By" drop-down field open, listing the other operations of the BoM.
   :data: BoM operations "Cut" and "Assemble"; "Assemble" blocked by "Cut".
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the dialog.

Finally, save the |BOM| by clicking :guilabel:`Save`.

Plan work orders using dependencies
===================================

Once work order dependencies have been configured on a |BOM|, Odoo *Manufacturing* is able to plan
when work orders are scheduled, based on their dependencies. To plan the work orders for a
manufacturing order, begin by navigating to :menuselection:`Manufacturing --> Operations -->
Manufacturing Orders`.

Next, select a manufacturing order for a product with work order dependencies set on its |BOM|, or
create a new manufacturing order by clicking :guilabel:`New`. If a new manufacturing order is
created, select a |BOM| configured with work order dependencies from the :guilabel:`Bill of
Material` drop-down field, then click :guilabel:`Confirm`.

After confirming the manufacturing order, select the :guilabel:`Work Orders` tab to view the work
orders required to complete it. Any work orders that are *not* blocked by a different work order
display a `Ready` tag in the :guilabel:`Status` section.

Work orders that are blocked by one or more work orders display a `Waiting for another WO` tag
instead. Once the blocking work order(s) are completed, the tag updates to `Ready`.

.. screenshot:: manufacturing-work-order-deps-status-tags
   :menu: Manufacturing ‣ Operations ‣ Manufacturing Orders ‣ (MO) ‣ Work Orders tab
   :shows: The Work Orders tab with a "Ready" tag on the "Cut" operation and a "Waiting for another WO" tag on the "Assemble" operation.
   :data: MO for product "Product A"; operations "Cut" and "Assemble".
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the tab.

To schedule the manufacturing order's work orders, click the :guilabel:`Plan` button at the top of
the page. After doing so, the :guilabel:`Start` field for each work order on the :guilabel:`Work
Orders` tab auto-fills with the scheduled start date and time (enable the column from the
:icon:`oi-settings-adjust` :guilabel:`(settings adjust)` icon if it is not shown). A blocked work
order is scheduled at the end of the time period specified in the :guilabel:`Expected Duration`
field of the work order that precedes it.

.. screenshot:: manufacturing-work-order-deps-start-field
   :menu: Manufacturing ‣ Operations ‣ Manufacturing Orders ‣ (MO) ‣ Work Orders tab
   :shows: The Work Orders tab, "Start" column enabled, showing the scheduled start date and time for both operations.
   :data: MO for product "Product A"; "Cut" starting at 1:30 PM, "Assemble" starting at 2:30 PM.
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the tab.

.. example::
   A manufacturing order is created for Product A. The manufacturing order has two operations: Cut
   and Assemble. Each operation has an expected duration of 60 minutes, and the Assemble operation
   is blocked by the Cut operation.

   The :guilabel:`Plan` button for the manufacturing order is clicked at 1:30 pm, and the Cut
   operation is scheduled to begin immediately. Since the Cut operation has an expected duration of
   60 minutes, the Assemble operation is scheduled to begin at 2:30 pm.


.. _manufacturing/workflows/work-orders:

===================
Process work orders
===================

.. |MO| replace:: :abbr:`MO (Manufacturing Order)`
.. |BoM| replace:: :abbr:`BoM (Bill of Materials)`

When a product's |BoM| includes one or more operations (via a routing), confirming a manufacturing
order (|MO|) for that product generates a *work order* for each operation. Work orders let
employees track, at each work center, exactly how much time is spent working on a specific step of
the manufacturing process.

.. important::
   Work orders require the :guilabel:`Work Orders` setting to be enabled. To do so, navigate to
   :menuselection:`Manufacturing app --> Configuration --> Settings`, tick the checkbox next to
   :guilabel:`Work Orders`, under the :guilabel:`Operations` heading, and click :guilabel:`Save`.

   .. seealso::
      :doc:`Work centers <../advanced_configuration/using_work_centers>`

Work orders overview
====================

To view every work order in the database, navigate to :menuselection:`Manufacturing app -->
Operations --> Work Orders`. The page can be displayed as a list, a kanban board (grouped by work
center), a calendar, or a pivot/graph, using the view switcher icons at the top-right of the page.

.. screenshot:: manufacturing-work-orders-list
   :menu: Manufacturing app --> Operations --> Work Orders
   :shows: The list view of work orders, "Operation", "Work Center", "Product", "Quantity
      Remaining", "Expected Duration", "Real Duration" and "Status" columns, with the Start/Pause/
      Done buttons and the status dropdown visible on each row.
   :highlight: The Start/Pause/Done buttons and the status dropdown of one row.
   :data: Demo company "YourCompany"; a mix of ready, in-progress, and done work orders.
   :module: mrp
   :notes: English UI, light theme, 1440px width.

Each work order can be in one of the following states:

- :guilabel:`Waiting for another WO`: a preceding work order, on which this one depends, has not
  been completed yet.
- :guilabel:`Waiting for components`: the components required for the operation are not yet
  available.
- :guilabel:`Ready`: the work order can be started.
- :guilabel:`In Progress`: work is currently being done on the work order.
- :guilabel:`Finished`: the work order has been completed.
- :guilabel:`Cancelled`: the work order was cancelled, typically because its |MO| was cancelled.

.. note::
   By default, work orders are only sequenced according to their operation's order on the |BoM|. To
   have Odoo enforce that a work order cannot start before another, specific one is finished (e.g.,
   *paint* cannot start before *sand* is done, even on a different work center), enable the
   :guilabel:`Work Order Dependencies` checkbox, located below the :guilabel:`Work Orders` setting.
   Doing so adds a :guilabel:`Blocked By` tab to each work order, used to select its dependencies.

Start, pause, and complete a work order
=======================================

From the :guilabel:`Work Orders` list or kanban view, each work order that is not yet done displays
buttons to process it directly, without opening its form:

- :icon:`fa-play` :guilabel:`Start`: begins the timer for the work order, and switches its status to
  :guilabel:`In Progress`. Starting a work order for a product tracked by serial numbers
  automatically sets its :guilabel:`Quantity Producing` to `1`.
- :icon:`fa-pause` :guilabel:`Pause`: stops the timer without marking the work order as done. It can
  be resumed later by clicking :icon:`fa-play` :guilabel:`Start` again.
- :icon:`fa-check` :guilabel:`Done`: stops the timer, consumes the components required for the
  operation, and marks the work order as :guilabel:`Finished`.

.. note::
   The :icon:`fa-play` :guilabel:`Start`, :icon:`fa-pause` :guilabel:`Pause`, and :icon:`fa-check`
   :guilabel:`Done` buttons are hidden whenever the work order's work center is blocked (see below).

Alternatively, click the colored status dot at the right of a work order's row to open its
:guilabel:`(status)` drop-down menu, which contains:

- :guilabel:`Done`: marks the work order as finished, equivalent to the :icon:`fa-check`
  :guilabel:`Done` button.
- :guilabel:`Block`/:guilabel:`Unblock`: blocks or unblocks the work order's work center (see
  below).
- :guilabel:`Print Work Order`: downloads a PDF work order sheet for the selected work order(s).

.. screenshot:: manufacturing-work-orders-status-dropdown
   :menu: Manufacturing app --> Operations --> Work Orders
   :shows: The status drop-down menu open on a work order row, with "Done", "Block", and "Print
      Work Order" options.
   :highlight: The "Block" option.
   :data: Demo company "YourCompany"; an in-progress work order.
   :module: mrp
   :notes: English UI, light theme, 1440px width.

On the kanban view, work orders that are :guilabel:`In Progress` display a :icon:`fa-play` (run),
:icon:`fa-pause` (paused), or :icon:`fa-stop` (blocked) icon on their card, depending on whether an
employee is actively working on them.

Block a work center
===================

If a work center becomes temporarily unusable, for example due to a mechanical breakdown or a
missing component, it can be *blocked*. While blocked, none of its pending work orders can be
started, paused, or finished, until it is unblocked again.

To block a work center from the :guilabel:`Work Orders` page, click the status drop-down menu on one
of its work orders, and select :guilabel:`Block`. Alternatively, navigate to
:menuselection:`Manufacturing app --> Configuration --> Work Centers`, and click the colored status
indicator on the work center's kanban card.

In the :guilabel:`Block Workcenter` pop-up window that appears, select a :guilabel:`Reason` for the
blockage, from options including :guilabel:`Material Availability`, :guilabel:`Equipment Failure`,
:guilabel:`Setup and Adjustments`, :guilabel:`Process Defect`, and :guilabel:`Reduced Yield`.
Optionally, enter additional details in the :guilabel:`Description` field. Then, click
:guilabel:`Block` to confirm.

.. screenshot:: manufacturing-work-orders-block-workcenter
   :menu: Manufacturing app --> Operations --> Work Orders (status dropdown --> Block)
   :shows: The "Block Workcenter" pop-up window, "Reason" field open showing the list of loss
      reasons, "Description" field.
   :highlight: The "Reason" field.
   :data: Demo company "YourCompany"; work center "Assembly Line 1", reason "Equipment Failure".
   :module: mrp
   :notes: English UI, light theme, 1440px width.

These blocking reasons are also used to compute the :doc:`Overall Equipment Effectiveness (OEE)
<../reporting/oee>` of each work center. To unblock a work center, select :guilabel:`Unblock` from
the same status drop-down menu, or click its status indicator again on the :guilabel:`Work Centers`
kanban view.

Work order details
==================

Click on a work order's :guilabel:`Operation` name to open its form and access additional
information:

- :guilabel:`Time Tracking` tab: lists every time entry logged against the work order, one per
  employee and work session, along with an optional :guilabel:`Productivity` loss reason for each
  entry. The total :guilabel:`Real Duration`, in minutes, is displayed below the list.
- :guilabel:`Components` tab: lists the components required for the operation, along with the
  quantity to consume, the quantity already consumed, and the on-hand and forecasted quantities.
- :guilabel:`Work Instruction` tab: displayed only if the operation's routing step includes a PDF
  file, a Google Slides link, or a text note, configured as instructions for how to carry out the
  operation.

.. screenshot:: manufacturing-work-orders-time-tracking
   :menu: Manufacturing app --> Operations --> Work Orders (open a work order) --> Time Tracking
      tab
   :shows: The Time Tracking tab of a work order form, with two time entries listed (different
      users, start/end times, and one with a "Productivity" loss reason set).
   :highlight: The "Productivity" column.
   :data: Demo company "YourCompany"; work order with 2 logged time entries.
   :module: mrp
   :notes: English UI, light theme, 1440px width.

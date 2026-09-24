====================
Replenishment report
====================

.. |SO| replace:: :abbr:`SO (Sales Order)`
.. |SOs| replace:: :abbr:`SOs (Sales Orders)`

The *replenishment report* is an interactive dashboard that uses :doc:`manual reordering rules
<reordering_rules>`, lead times, and upcoming demands to forecast quantities of products that need
restocking.

Reordering rules used on this dashboard are normal reordering rules, but the user benefits from a
monitoring menu with extra options to manage suggestions for replenishment.

This enables users to anticipate future needs, keep less products on hand without the risk of
running out, plan and consolidate orders.

Navigate the replenishment report
=================================

To access the replenishment report, go to :menuselection:`Inventory app --> Operations -->
Replenishment.`

.. note::
   Automatic reordering rules are available on this menu as well, but are hidden by default.

The fields and features unique to the replenishment dashboard are displayed below. For definitions
of the other fields, go to the :ref:`Create reordering rules section
<inventory/warehouses_storage/rr-fields>`.

By default, the quantity in the :guilabel:`To Order` field is the quantity required to reach the set
:guilabel:`Max Quantity`. However, the :guilabel:`To Order` quantity can be adjusted by clicking on
the field and changing the value. To replenish a product manually, click :icon:`fa-truck`
:guilabel:`Order`.

Click :icon:`fa-bell-slash` :guilabel:`Snooze` to temporarily deactivate the reordering rule for
the set period, hiding the entry from the replenishment dashboard, when it is supposed to appear.

.. tip::
   Defining a :guilabel:`Vendor` allows filtering or grouping demands by the vendor. This simplifies
   the process of identifying products to order and can reduce shipment costs. Click the
   :icon:`oi-settings-adjust` :guilabel:`(adjust settings)` icon and select :guilabel:`Vendor` from
   the drop-down list to view the field on the report.

.. screenshot:: inventory-replenishment-dashboard
   :menu: Inventory ‣ Operations ‣ Replenishment
   :shows: The replenishment report listing products that need restocking, with the Product, Location, On
      Hand, Forecast, Min, Max and "To Order" columns and the "Order" and "Snooze" buttons on the lines.
   :highlight: The "To Order" column and the "Order" button (red frames).
   :data: Three or four manual reordering rules whose forecast is below the minimum.
   :module: stock
   :notes: English UI, light theme, 1440px width, full list view including the left search panel.

Order to max
------------

If a reordering rule does not forecast the product to arrive below the minimum, the replenishment
cannot be triggered, because it is seen as *unnecessary*. However, there can be instances where a
product needs to be replenished even if it is not deemed *necessary*, such as when an order needs to
be maximized to obtain better discounts, or to save on delivery costs.

First, select one or more products by ticking the appropriate checkbox. Then, click the
:guilabel:`Replenish` button and select :guilabel:`Order To Max`. Doing so creates a request for
quotation (RFQ) for the first possible replenishment date for each product for the maximum specified
in the reordering rule.

.. screenshot:: inventory-replenishment-order-to-max
   :menu: Inventory ‣ Operations ‣ Replenishment
   :shows: The replenishment report with one line selected and the "Replenish" drop-down open, showing the
      "Order" and "Order To Max" entries.
   :highlight: The "Order To Max" entry (red frame).
   :data: One selected reordering rule whose forecast is above its minimum.
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the selection bar and the open drop-down.


Replenishment information
=========================

In each line of the replenishment report, clicking the :icon:`fa-info-circle` :guilabel:`(info)`
icon opens the :guilabel:`Replenishment Information` pop-up window, which displays the *lead times*
and *forecasted date*.

For detailed information on how to use this feature for replenishment, go to the :ref:`Just in time
logic <inventory/warehouses_storage/just-in-time>` section.

Select a warehouse
------------------

If a warehouse's replenishment method is :doc:`resupply from another warehouse
<resupply_warehouses>`, check for available product quantities in other warehouses by opening the
:guilabel:`Replenishment Information` pop-up window. Warehouses that can replenish the stock are
listed under the :guilabel:`Warehouses` tab, and the :guilabel:`Available Quantity` shows the
on-hand stock in each warehouse.

After selecting a sourcing warehouse, click :guilabel:`Select Route` to use that warehouse for this
replenishment. If the :guilabel:`Order` button is clicked without selecting a route, the reordering
rule reverts to its preferred route (*Buy* or *Manufacture*).

.. screenshot:: inventory-replenishment-select-warehouse
   :menu: Inventory ‣ Operations ‣ Replenishment ‣ (info icon on a line)
   :shows: The "Replenishment Information" pop-up with the "Warehouses" tab selected, listing the warehouses
      that can resupply the stock with their "Available Quantity" and the "Select Route" button.
   :highlight: The "Available Quantity" column and the "Select Route" button (red frames).
   :data: Two warehouses, one of which holds stock of the product.
   :module: stock
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

.. seealso::
   :ref:`Temporary Reordering Rules <purchase/check-replenishment>`

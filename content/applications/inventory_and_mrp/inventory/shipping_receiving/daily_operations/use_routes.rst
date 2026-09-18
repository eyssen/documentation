==========================
Routes and push/pull rules
==========================

*Routes* in Odoo control the movement of products between different locations, whether internal or
external, using push and pull rules. Once set up, these rules help automate the logistics of product
movement based on specific conditions.

.. seealso::
   :doc:`Standard routes in Odoo <../daily_operations>`

.. note::
   Routes are applicable on products, product categories, shipping methods, :ref:`packagings
   <inventory/product_management/route-on-packaging>`, and on the sales order line.

About routes and terminology
============================

In a generic warehouse, there are receiving docks, a quality control area, storage locations,
picking and packing areas, and shipping docks. All products go through all these locations. As the
products move through the locations, each location triggers the products' specified route and
rules.

.. screenshot:: daily-operations-use-routes-stock-example
   :menu: (diagram)
   :shows: A schematic drawing of a warehouse with an input area, a quality control area, a stock area and an output area.
   :module: stock
   :notes: Simple schematic drawing, no Odoo UI.

In this example, vendor trucks unload pallets of ordered products at the receiving docks. Operators
then scan the products in the receiving area. Depending on the product's route and rules, some of
these products are sent to a quality control area (for example, products that are components used
in the manufacturing process), while others are directly stored in their respective locations.

.. screenshot:: daily-operations-use-routes-push-to-rule-example
   :menu: (diagram)
   :shows: A schematic drawing of a push rule: goods arriving at the input location are automatically moved on to quality control.
   :module: stock
   :notes: Simple schematic drawing, no Odoo UI.

Here is an example of a fulfillment route. In the morning, items are picked for all the orders that
need to be prepared during the day. These items are picked from storage locations and moved to the
picking area, close to where the orders are packed. Then, the orders are packed in their respective
boxes, and conveyor belts bring them to the shipping docks, ready to be delivered to customers.

.. screenshot:: daily-operations-use-routes-pull-from-rule-example
   :menu: (diagram)
   :shows: A schematic drawing of a pull rule: a customer demand at the output location triggers a move out of stock.
   :module: stock
   :notes: Simple schematic drawing, no Odoo UI.

Push rules
----------

Push rules are used to *supply products into a storage locations* as soon as they arrive at a
specific receiving location.

.. note::
   Push rules can only be triggered if there are no pull rules that have already generated the
   product transfers.

In a :doc:`one-step receipt route <receipts_delivery_one_step>`, which uses one push rule, when a
product arrives in the warehouse, a push rule can automatically transfer it to the *Storage
Location*. Different push rules can be applied to different products, allowing for customized
storage locations.

.. screenshot:: daily-operations-use-routes-push-rule
   :menu: Inventory ‣ Configuration ‣ Routes
   :shows: A rule form of the "Receive in one step" route, with Action set to "Push To" and the source and destination locations filled in.
   :highlight: The "Action" field (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

For more information about configuring rules, skip to the :ref:`Configure rules section
<inventory/shipping_receiving/configure-rules>`.

Pull rules
----------

Pull rules trigger product moves on demand, such as a sales order or a :doc:`need to restock
<../../warehouses_storage/replenishment/reordering_rules>`.

Pull rules work backward from the demand location. For example, in a :ref:`two-step delivery
<inventory/shipping_receiving/two-step-delivery>` route, where items move from *Stock* to *Output*
before being delivered to the *Customer Location*, the pull rule first creates a transfer from
*Output* to the customer. If the product is not at *Output*, another pull rule creates a transfer
from *Stock* to *Output*. The warehouse workers then process these transfers in the reverse order:
picking, then shipping.

.. screenshot:: daily-operations-use-routes-pull-rule
   :menu: Inventory ‣ Configuration ‣ Routes
   :shows: A rule form of the "Deliver in two steps" route, with Action set to "Pull From" and the operation type shown.
   :highlight: The "Action" field (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

For more information about configuring rules, skip to the :ref:`Configure rules section
<inventory/shipping_receiving/configure-rules>`.

.. _use-routes/routes-rules:

Configuration
=============

Since *Routes* are a collection of *Push and Pull Rules*, Odoo helps you manage advanced route
configurations such as:

- Manage product manufacturing chains.
- Manage default locations per product.
- Define routes within the stock warehouse according to business needs, such as quality control,
  after-sales services, or supplier returns.
- Help rental management by generating automated return moves for rented products.

To configure a route for a product, first, open the :guilabel:`Inventory` application and go to
:menuselection:`Configuration --> Settings`. Then, in the :guilabel:`Warehouse` section, enable the
:guilabel:`Multi-Step Routes` feature and click :guilabel:`Save`.

.. screenshot:: daily-operations-use-routes-multi-steps-feature
   :menu: Inventory ‣ Configuration ‣ Settings
   :shows: The Inventory settings page scrolled to "Warehouse", with the "Multi-Step Routes" checkbox enabled.
   :highlight: The "Multi-Step Routes" checkbox (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

.. note::
   The :guilabel:`Storage Locations` feature is automatically activated with the
   :guilabel:`Multi-Step Routes` feature.

Once this first step is completed, the user can use pre-configured routes that come with Odoo, or
they can create custom routes.

Pre-configured routes
---------------------

To access Odoo's pre-configured routes, go to :menuselection:`Inventory --> Configuration -->
Warehouses`. Then, open a warehouse form. In the :guilabel:`Warehouse Configuration` tab, the user
can view the warehouse's pre-configured routes for :guilabel:`Incoming Shipments` and
:guilabel:`Outgoing Shipments`.

.. screenshot:: daily-operations-use-routes-example-preconfigured-warehouse
   :menu: Inventory ‣ Configuration ‣ Warehouses
   :shows: A warehouse form showing the Incoming and Outgoing Shipments step options.
   :highlight: The shipment step options (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

Some more advanced routes, such as pick-pack-ship, are also available. The user can select the
route that best fits their business needs. Once the :guilabel:`Incoming Shipments` and
:guilabel:`Outgoing Shipments` routes are set, head to :menuselection:`Inventory --> Configuration
--> Routes` to see the specific routes that Odoo generated.

.. screenshot:: daily-operations-use-routes-preconfigured
   :menu: Inventory ‣ Configuration ‣ Routes
   :shows: The routes list showing the pre-configured routes: Receive in one/two/three steps, Deliver in one/two/three steps, Buy and Replenish on Order (MTO).
   :module: stock
   :notes: English UI, light theme, 1440px width.

On the :guilabel:`Routes` page, click on a route to open the route form. In the route form, the
user can view which places the route is :guilabel:`Applicable On`. The user can also set the route
to only apply on a specific :guilabel:`Company`. This is useful for multi-company environments; for
example, a user can have a company and warehouse in Country A and a second company and warehouse in
Country B.

.. seealso::
   :ref:`Applicable on packagings <inventory/product_management/packaging-route>`

.. screenshot:: daily-operations-use-routes-example
   :menu: Inventory ‣ Configuration ‣ Routes
   :shows: A route form with the "Applicable On" checkboxes, showing the route applied to product categories and to a warehouse.
   :highlight: The "Applicable On" block (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

At the bottom of the route form, the user can view the specific :guilabel:`Rules` for the route.
Each :guilabel:`Rule` has an :guilabel:`Action`, a :guilabel:`Source Location`, and a
:guilabel:`Destination Location`.

.. screenshot:: daily-operations-use-routes-rules-example
   :menu: Inventory ‣ Configuration ‣ Routes
   :shows: The Rules tab of a route, listing rules with both "Push To" and "Pull From" actions and their locations.
   :module: stock
   :notes: English UI, light theme, 1440px width.

Custom Routes
-------------

To create a custom route, go to :menuselection:`Inventory --> Configuration --> Routes`, and click
on :guilabel:`Create`. Next, choose the places where this route can be selected. A route can be
applicable on a combination of places.

.. screenshot:: daily-operations-use-routes-advanced-custom-route
   :menu: Inventory ‣ Configuration ‣ Routes
   :shows: A custom route form named "Pick - Pack - Ship" with its three rules in the Rules tab.
   :module: stock
   :notes: English UI, light theme, 1440px width.

Each place has a different behavior, so it is important to tick only the useful ones and adapt each
route accordingly. Then, configure the :guilabel:`Rules` of the route.

If the route is applicable on a product category, the route still needs to be manually set on the
product category form by going to :menuselection:`Inventory --> Configuration --> Product
Categories`. Then, select the product category and open the form. Next, click :guilabel:`Edit` and
under the :guilabel:`Logistics` section, set the :guilabel:`Routes`.

When applying the route on a product category, all the rules configured in the route are applied to
**every** product in the category. This can be helpful if the business uses the dropshipping
process for all the products from the same category.

.. screenshot:: daily-operations-use-routes-logistic-section
   :menu: Inventory ‣ Configuration ‣ Routes
   :shows: A route form with "Product Categories" ticked under "Applicable On", and the "All" category selected below.
   :highlight: The "Product Categories" checkbox and the selected category (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

The same behavior applies to the warehouses. If the route can apply to :guilabel:`Warehouses`, all
the transfers occurring inside the chosen warehouse that meet the conditions of the route's rules
will then follow that route.

.. screenshot:: daily-operations-use-routes-applicable-on-warehouse
   :menu: Inventory ‣ Configuration ‣ Routes
   :shows: A route form with "Warehouses" ticked under "Applicable On" and the warehouse drop-down open.
   :highlight: The warehouse drop-down (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

If the route is applicable on :guilabel:`Sales Order Lines`, it is more or less the opposite. The
route must be manually chosen when creating a quotation. This is useful if some products go through
different routes.

Remember to toggle the visibility of the :guilabel:`Route` column on the quotation/sales order.
Then, the route can be chosen on each line of the quotation/sales order.

.. screenshot:: daily-operations-use-routes-add-to-sales-lines
   :menu: Inventory ‣ Configuration ‣ Routes
   :shows: A route form with "Sales Order Lines" ticked under "Applicable On".
   :highlight: The "Sales Order Lines" checkbox (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

Finally, there are routes that can be applied to products. Those work more or less like the product
categories: once selected, the route must be manually set on the product form.

To set a route on a product, go to :menuselection:`Inventory --> Products --> Products` and select
the desired product. Then, go to the :guilabel:`Inventory` tab and under the :guilabel:`Operations`
section, select the :guilabel:`Routes`.

.. screenshot:: daily-operations-use-routes-on-product-route
   :menu: Inventory ‣ Products ‣ Products
   :shows: A product form with the Inventory tab open, showing the Routes checkboxes in the Operations section with a custom route ticked.
   :highlight: The selected route (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

.. important::
   Rules must be set on the route in order for the route to work.

.. _inventory/shipping_receiving/configure-rules:

Rules
~~~~~

The rules are defined on the route form. First, go to :menuselection:`Inventory --> Configuration
--> Routes` and open the desired route form. Next, click :guilabel:`Edit` and in the
:guilabel:`Rules` section, click on :guilabel:`Add a line`.

.. screenshot:: daily-operations-use-routes-add-new-rules
   :menu: Inventory ‣ Configuration ‣ Routes
   :shows: The Rules tab of a route with the "Add a line" link, used to add a new rule.
   :module: stock
   :notes: English UI, light theme, 1440px width.

The available rules trigger various actions. If Odoo offers *Push* and *Pull* rules, others are
also available. Each rule has an :guilabel:`Action`:

- :guilabel:`Pull From`: this rule is triggered by a need for the product in a specific location.
  The need can come from a sales order being validated or from a manufacturing order requiring a
  specific component. When the need appears in the destination location, Odoo generates a picking to
  fulfill this need.
- :guilabel:`Push To`: this rule is triggered by the arrival of some products in the defined source
  location. In the case of the user moving products to the source location, Odoo generates a picking
  to move those products to the destination location.
- :guilabel:`Pull & Push`: this rule allows the generation of pickings in the two situations
  explained above. This means that when products are required at a specific location, a transfer is
  created from the previous location to fulfill that need. This creates a need in the previous
  location and a rule is triggered to fulfill it. Once the second need is fulfilled, the products
  are pushed to the destination location and all the needs are fulfilled.
- :guilabel:`Buy`: when products are needed at the destination location, a request for quotation is
  created to fulfill the need.
- :guilabel:`Manufacture`: when products are needed in the source location, a manufacturing order
  is created to fulfill the need.

.. screenshot:: daily-operations-use-routes-pull-from-rule-stock-to-packing
   :menu: Inventory ‣ Configuration ‣ Routes
   :shows: A "Pull From" rule form moving goods from WH/Stock to WH/Packing Zone, with the operation type set to Internal Transfer.
   :data: Rule of the "Pick - Pack - Ship" route.
   :module: stock
   :notes: English UI, light theme, 1440px width.

The :guilabel:`Operation Type` must also be defined on the rule. This defines which kind of picking
is created from the rule.

If the rule's :guilabel:`Action` is set to :guilabel:`Pull From` or :guilabel:`Pull & Push`, a
:guilabel:`Supply Method` must be set. The :guilabel:`Supply Method` defines what happens at the
source location:

- :guilabel:`Take From Stock`: the products are taken from the available stock of the source
  location.
- :guilabel:`Trigger Another Rule`: the system tries to find a stock rule to bring the products to
  the source location. The available stock is ignored.
- :guilabel:`Take From Stock, if Unavailable, Trigger Another Rule`: the products are taken from
  the available stock of the source location. If there is no stock available, the system tries to
  find a rule to bring the products to the source location.

Example flow
============

In this example, let's use a custom *Pick - Pack - Ship* route to try a full flow with an advanced
custom route.

First, a quick look at the route's rules and their supply methods. There are three rules, all
:guilabel:`Pull From` rules. The :guilabel:`Supply Methods` for each rule are the following:

- :guilabel:`Take From Stock`: When products are needed in the :guilabel:`WH/Packing Zone`, *picks*
  (internal transfers from :guilabel:`WH/Stock` to :guilabel:`WH/Packing Zone`) are created from
  :guilabel:`WH/Stock` to fulfill the need.
- :guilabel:`Trigger Another Rule`: When products are needed in :guilabel:`WH/Output`, *packs*
  (internal transfers from :guilabel:`WH/Packing Zone` to :guilabel:`WH/Output`) are created from
  :guilabel:`WH/Packing Zone` to fulfill the need.
- :guilabel:`Trigger Another Rule`: When products are needed in :guilabel:`Partner
  Locations/Customers`, *delivery orders* are created from :guilabel:`WH/Output` to fulfill the
  need.

.. screenshot:: daily-operations-use-routes-transfers-overview
   :menu: Inventory ‣ Operations ‣ Transfers
   :shows: The transfers list showing the three transfers created by a pick-pack-ship route for one sales order.
   :data: Pick, Pack and Delivery Order of the same sales order.
   :module: stock
   :notes: English UI, light theme, 1440px width.

This means that, when a customer orders products that have a *pick - pack - ship* route set on it,
a delivery order is created to fulfill the order.

.. screenshot:: daily-operations-use-routes-on-transfers
   :menu: Inventory ‣ Operations ‣ Transfers
   :shows: The Operations tab of the pick transfer created by the pull rule, showing the source and destination locations.
   :module: stock
   :notes: English UI, light theme, 1440px width.

.. note::
   If the source document for multiple tranfers is the same sales order, the status is not the same.
   The status will be :guilabel:`Waiting Another Operation` if the previous transfer in the list is
   not done yet.

.. screenshot:: daily-operations-use-routes-waiting-status
   :menu: Inventory ‣ Operations ‣ Transfers
   :shows: The three chained transfers at the start of the flow: the first is Ready, the other two are "Waiting Another Operation".
   :highlight: The status column (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

To prepare the delivery order, packed products are needed at the output area, so an internal
transfer is requested from the packing zone.

.. screenshot:: daily-operations-use-routes-detailed-2
   :menu: Inventory ‣ Operations ‣ Transfers
   :shows: The detailed operations of the transfer between the packing zone and the output location.
   :data: Transfer WH/PACK/00001.
   :module: stock
   :notes: English UI, light theme, 1440px width.

Obviously, the packing zone needs products ready to be packed. So, an internal transfer is
requested to the stock and employees can gather the required products from the warehouse.

.. screenshot:: daily-operations-use-routes-detailed-transfer
   :menu: Inventory ‣ Operations ‣ Transfers
   :shows: The detailed operations of the transfer between stock and the packing zone.
   :data: Transfer WH/PICK/00001.
   :module: stock
   :notes: English UI, light theme, 1440px width.

As explained in the introduction of the documentation, the last step in the process (for this
route, the delivery order) is the first to be triggered, which then triggers other rules until we
reach the first step in the process (here, the internal transfer from the stock to the packing
area). Now, everything is ready to be processed so the customer can get the ordered items.

In this example, the product is delivered to the customer when all the rules have been triggered and
the transfers are done.

.. screenshot:: daily-operations-use-routes-transfers-status
   :menu: Inventory ‣ Operations ‣ Transfers
   :shows: The same three transfers once the route is completed, all in "Done" status.
   :highlight: The status column (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

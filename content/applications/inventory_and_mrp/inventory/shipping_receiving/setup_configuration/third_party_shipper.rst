===========================
Shipping carrier connectors
===========================

.. |SO| replace:: :abbr:`SO (Sales Order)`
.. |DO| replace:: :abbr:`DO (Delivery Order)`

.. _inventory/shipping/third_party:

A *shipping carrier connector* links Odoo to a carrier's own system, so that Odoo can verify whether
the carrier delivers to a given address, :doc:`automatically calculate shipping costs
<../setup_configuration>`, :doc:`generate shipping labels <labels>`, and receive tracking numbers.

Carrier connectors can be applied to a sales order (SO), invoice, or delivery order. For tips on
resolving common issues when configuring a connector, skip to the :ref:`Troubleshooting
<inventory/shipping_receiving/third-party-troubles>` section.

The following carrier connectors are available:

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Carrier
     - Module
     - Region availability
   * - :doc:`GLS <gls>`
     - *Delivery GLS* (`eyssen_delivery_gls`)
     - Hungary and GLS parcel-shop countries
   * - :doc:`MPL <mpl>` (Magyar Posta)
     - *Delivery MPL* (`eyssen_delivery_mpl`)
     - Hungary
   * - :doc:`Foxpost <foxpost>`
     - *Delivery Foxpost* (`eyssen_delivery_foxpost`)
     - Hungary
   * - :doc:`Custom carrier <custom>`
     - *Delivery Custom* (`eyssen_delivery_custom`)
     - Any carrier that accepts a printed label
   * - Mondial Relay
     - *Mondial Relay* (`delivery_mondialrelay`)
     - France and neighboring countries

.. note::
   Carriers without a connector are still usable: configure them as a :ref:`Fixed Price
   <inventory/shipping/fixed>` or :ref:`Based on Rules <inventory/shipping/rules>` delivery method,
   or use the :doc:`custom carrier <custom>` module to print a label with the carrier's own layout.

Configuration
=============

To set up a carrier connector, follow these steps:

#. :ref:`Install the shipping connector <inventory/shipping_receiving/shipping-connector>`.
#. :ref:`Set up delivery method <inventory/shipping_receiving/configure-delivery-method>`.
#. :ref:`Activate production environment <inventory/shipping_receiving/production-env>`.
#. :ref:`Configure warehouse <inventory/shipping_receiving/configure-source-address>`.
#. :ref:`Specify weight of products <inventory/shipping_receiving/configure-weight>`.

.. _inventory/shipping_receiving/shipping-connector:

Install shipping connector
--------------------------

Each carrier connector is a separate module. To install one, :ref:`install the module
<general/install>` listed in the table above from the :menuselection:`Apps` application (for example,
`Delivery GLS`). Installing a connector also installs the *Delivery Costs* module it depends on.

.. note::
   The :guilabel:`Shipping Connectors` block on the :menuselection:`Inventory app --> Configuration
   --> Settings` page lists connectors that are not part of this database; install the connector
   modules from :menuselection:`Apps` instead.

.. note::
   :doc:`Delivery methods <../setup_configuration>` are also used by the *Sales*, *eCommerce*, and
   *Website* apps.

.. _inventory/shipping_receiving/configure-delivery-method:

Delivery method
---------------

To configure the API credentials, and activate the shipping carrier, begin by going to
:menuselection:`Inventory app --> Configuration --> Shipping Methods`, and select the desired
delivery method.

.. note::
   The list often includes **two** delivery methods from the same :guilabel:`Provider`: one for
   international shipping and one for domestic shipping.

   Additional delivery methods can be created for specific purposes, such as :doc:`packaging
   <../../product_management/configure/packaging>`.

.. seealso::
   :doc:`Configure delivery methods <../setup_configuration>`

.. note::
   Ensure the delivery method is published when it should be available on the *Website* app. To
   publish a delivery method on the website, click the desired delivery method, then click the
   :guilabel:`Unpublished` smart button. Doing so changes that smart button to read:
   :guilabel:`Published`.

.. _inventory/shipping_receiving/shipping-methods-details:

The :guilabel:`Shipping Method` page contains details about the provider, including:

- :guilabel:`Shipping Method` (*Required field*): the name of the delivery method (e.g. `GLS Home
  Delivery`, `GLS ParcelShop`, etc.).
- :guilabel:`Website`: configure shipping methods for an *eCommerce* page that is connected to a
  specific website in the database. Select the applicable website from the drop-down menu, or leave
  it blank to apply the method to all web pages.
- :guilabel:`Provider` (*Required field*): choose the delivery service, like GLS. Upon choosing a
  provider, the :guilabel:`Integration Level`, :guilabel:`Invoicing Policy` and
  :guilabel:`Insurance Percentage` fields become available.
- :guilabel:`Integration Level`: choose :guilabel:`Get Rate` to simply get an :ref:`estimated
  shipment cost <inventory/shipping_receiving/third-party-so>` on an |SO| or invoice.

  .. important::
     Select :guilabel:`Get Rate and Create Shipment` to also :doc:`generate shipping labels
     <labels>`.

- :guilabel:`Company`: if the shipping method should apply to a specific company, select it from the
  drop-down menu. Leave the field blank to apply the method to all companies.
- :guilabel:`Delivery Product` (*Required field*): the delivery charge name that is added to the
  |SO| or invoice.
- :guilabel:`Invoicing Policy`: select and calculate an :guilabel:`Estimated cost` of shipping
  directly from the shipping carrier. If the :guilabel:`Real cost` of shipping is wanted instead,
  refer to :doc:`Invoice real shipping costs <invoicing>` document.
- :guilabel:`Margin on Rate`: specify an additional percentage amount added to the base shipping
  rate to cover extra costs, such as handling fees, packaging materials, exchange rates, etc.
- :guilabel:`Free if order amount is above`: enables free shipping for orders surpassing a specified
  amount entered in the corresponding :guilabel:`Amount` field.
- :guilabel:`Insurance Percentage`: specify a percentage amount of the shipping costs reimbursed to
  the senders if the package is lost or stolen in transit. The field is only shown for connectors
  that support shipping insurance.

.. screenshot:: setup-configuration-third-party-shipper-carrier-form
   :menu: Inventory ‣ Configuration ‣ Shipping Methods
   :shows: A delivery method form of a carrier connector, showing the Provider, Integration Level, Delivery Product, Invoicing Policy and Margin on Rate fields.
   :data: Delivery method "GLS Home Delivery", provider GLS.
   :module: eyssen_delivery_gls
   :notes: English UI, light theme, 1440px width.

**Shipping Method** configuration page for `GLS Home Delivery`.

In the :guilabel:`Configuration` tab, fill out the API credential fields (e.g. API key, password,
account number, etc.). Depending on the carrier chosen in the :guilabel:`Provider` field, the
:guilabel:`Configuration` tab contains different required fields. For details about configuring a
specific carrier's credentials, refer to the following documents:

.. seealso::
   - :doc:`GLS configuration <gls>`
   - :doc:`MPL configuration <mpl>`
   - :doc:`Foxpost configuration <foxpost>`
   - :doc:`Custom carrier <custom>`

.. _inventory/shipping_receiving/production-env:

Production environment
----------------------

With the delivery method details configured, click the :guilabel:`Test Environment` smart button to
set it to :guilabel:`Production Environment`.

.. warning::
   Setting the delivery method to :guilabel:`Production` creates **real** shipping labels, and the
   carrier account may be charged **before** the customer is charged for shipping. Verify all
   configurations are correct before switching the delivery method to :guilabel:`Production`.

.. screenshot:: setup-configuration-third-party-shipper-production
   :menu: Inventory app ‣ Configuration ‣ Shipping Methods
   :shows: A delivery method form with the "Test Environment" smart button at the top, used to switch to the production environment.
   :highlight: The "Test Environment" smart button (red frame).
   :module: delivery
   :notes: English UI, light theme, 1440px width.

.. _inventory/shipping_receiving/configure-source-address:

Warehouse configuration
-----------------------

Ensure the warehouse's :guilabel:`Address` (including ZIP code) and :guilabel:`Phone` number are
entered accurately. To do that, go to :menuselection:`Inventory app --> Configuration -->
Warehouses`, and select the desired warehouse.

On the warehouse configuration page, open the warehouse contact page by clicking the
:guilabel:`Company` field.

.. screenshot:: setup-configuration-third-party-shipper-internal-link
   :menu: Inventory ‣ Configuration ‣ Warehouses
   :shows: A warehouse form with the "Company" field and its internal-link arrow, which opens the company contact.
   :highlight: The "Company" field (red frame).
   :module: delivery
   :notes: English UI, light theme, 1440px width.

Verify that the :guilabel:`Address` and :guilabel:`Phone` number are correct, as they are required
for the shipping connector to work properly.

.. screenshot:: setup-configuration-third-party-shipper-company
   :menu: Settings ‣ Users & Companies ‣ Companies
   :shows: A company form showing the full Address (with ZIP code) and the Phone number filled in.
   :highlight: The Address and Phone fields (red frame).
   :module: delivery
   :notes: English UI, light theme, 1440px width.

.. _inventory/shipping_receiving/configure-weight:

Product weight
--------------

For the carrier integration to work properly, specify the weight of products by going to
:menuselection:`Inventory app --> Products --> Products`, and selecting the desired product.

Then, switch to the :guilabel:`Inventory` tab, and define the :guilabel:`Weight` of the product in
the :guilabel:`Logistics` section.

.. screenshot:: setup-configuration-third-party-shipper-product-weight
   :menu: Inventory app ‣ Products ‣ Products
   :shows: The Inventory tab of a product form, with the "Weight" field filled in under Logistics.
   :highlight: The "Weight" field (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

.. _inventory/shipping_receiving/apply-third-party-carrier:

Apply a shipping carrier
========================

Shipping carriers can be applied on a :abbr:`SO (Sales Order)`, invoice, or delivery order.

After configuring the carrier's :ref:`delivery method
<inventory/shipping_receiving/configure-delivery-method>` in Odoo, create or navigate to a quotation
by going to :menuselection:`Sales app --> Orders --> Quotations`.

.. _inventory/shipping_receiving/third-party-so:

Sales order
-----------

To assign a shipping carrier, and get an estimated cost of shipping, begin by going to
:menuselection:`Sales app --> Orders --> Quotations`. Create or select an existing quotation, and
add the cost of shipping through a carrier connector to a quotation, by clicking the
:guilabel:`Add Shipping` button in the bottom-right corner of the :guilabel:`Order Lines` tab.

.. screenshot:: setup-configuration-third-party-shipper-add-shipping
   :menu: Sales app ‣ Orders ‣ Quotations
   :shows: A quotation with the "Add Shipping" button in the bottom-right corner of the Order Lines tab.
   :highlight: The "Add Shipping" button (red frame).
   :module: delivery
   :notes: English UI, light theme, 1440px width.

In the resulting :guilabel:`Add a shipping method` pop-up window, select the intended carrier from
the :guilabel:`Shipping Method` drop-down menu. The :guilabel:`Cost` field is automatically filled
based on:

- the amount specified in the :guilabel:`Total Order Weight` field (if it is not provided, the sum
  of :ref:`product weights <inventory/shipping_receiving/configure-weight>` in the order is used)
- the distance between the warehouse's :ref:`source address
  <inventory/shipping_receiving/configure-source-address>` and the customer's address.

.. _inventory/shipping_receiving/third-party-rate:

After selecting a connected provider in the :guilabel:`Shipping Method` field, click
:guilabel:`Get Rate` in the :guilabel:`Add a shipping method` pop-up window to get the estimated
cost through the shipping connector. Then, click the :guilabel:`Add` button to add the delivery
charge to the |SO| or invoice.

.. seealso::
   :doc:`Charge customers for shipping after product delivery <invoicing>`

.. _inventory/shipping_receiving/third-party-do:

Delivery order
--------------

For users making shipments without installing the *Sales* app, assign the shipping carrier to the
delivery order, by first going to the :menuselection:`Inventory` app. Then, from the
:guilabel:`Inventory Overview` dashboard, select the :guilabel:`Delivery Orders` operation type, and
choose the desired delivery order that is not already marked as :guilabel:`Done` or
:guilabel:`Cancelled`.

In the :guilabel:`Additional info` tab, set the :guilabel:`Carrier` field to the desired shipping
carrier. When the delivery method is set to :ref:`production mode
<inventory/shipping_receiving/configure-delivery-method>`, a :guilabel:`Tracking Reference` is
provided.

.. seealso::
   :doc:`Generate shipping labels <labels>`

.. screenshot:: setup-configuration-third-party-shipper-delivery-info
   :menu: Inventory ‣ Delivery Orders
   :shows: The "Additional info" tab of a delivery order, with the Carrier and Tracking Reference fields filled in.
   :highlight: The "Carrier" and "Tracking Reference" fields (red frame).
   :module: delivery
   :notes: English UI, light theme, 1440px width.

.. _inventory/shipping_receiving/third-party-troubles:

Troubleshooting
===============

Since shipping connectors can sometimes be complex to set up, here are some checks to try when
things are not working as expected:

#. Ensure the :ref:`warehouse information <inventory/shipping_receiving/configure-source-address>`
   (e.g., address and phone number) in Odoo is correct **and** matches the records saved in the
   shipping provider's website.
#. Verify that the :ref:`package type <inventory/warehouses_storage/package-type>` and parameters
   are valid for the shipping carrier. To check, ensure the shipment can be directly created on the
   shipping carrier's website.
#. When encountering a price mismatch between Odoo's estimated cost and the provider's charge, first
   ensure the delivery method is set to :ref:`production environment
   <inventory/shipping_receiving/production-env>`.

   Then, create the shipment in both the carrier's website and Odoo, and verify the prices are the
   same across Odoo, the shipping provider, and in the *debug logs*.

   .. example::
      When checking for a price mismatch in the debug logs, if the request says the package weighs
      six kilograms, but the carrier's response says the package weighs seven kilograms, the issue
      is on the carrier's side.

Debug log
---------

Track shipping data inconsistencies by activating debug logging. To do that, go to the delivery
method's configuration page (:menuselection:`Inventory app --> Configuration --> Shipping
Method`), and select the desired shipping method. Click the :guilabel:`No Debugging` smart button to
activate :guilabel:`Debug Requests`.

.. screenshot:: setup-configuration-third-party-shipper-no-debug
   :menu: Inventory ‣ Configuration ‣ Shipping Methods
   :shows: A delivery method form with the "No Debugging" smart button at the top.
   :highlight: The "No Debugging" smart button (red frame).
   :module: delivery
   :notes: English UI, light theme, 1440px width.

With :guilabel:`Debug Requests` activated, each time the shipping connector is used to estimate the
cost of shipping, records are saved in the :guilabel:`Logging` report. To access the report, turn on
:ref:`developer mode <developer-mode>`, and go to :menuselection:`Settings app --> Technical -->
Database Structure section --> Logging`.

.. note::
   Logs are created for a shipping method each time the :ref:`Get Rate
   <inventory/shipping_receiving/third-party-rate>` button is clicked on :abbr:`SOs (Sales Orders)`
   and invoices, **and** when a customer adds the shipping carrier to their order through the
   *Website* app.

.. screenshot:: setup-configuration-third-party-shipper-log
   :menu: Settings ‣ Technical
   :shows: The Settings Technical menu opened, with the "Logging" item under Database Structure.
   :highlight: The "Logging" menu item (red frame).
   :module: delivery
   :notes: English UI, light theme, 1440px width, developer mode on.

Click the *HTTP request* line item to open a detailed page, and verify the correct information is
sent from Odoo to the shipping carrier. In the *HTTP response*, verify that the same information is
received.

.. screenshot:: setup-configuration-third-party-shipper-logging
   :menu: Settings ‣ Technical ‣ Logging
   :shows: The Logging list showing HTTP request and response records created by the carrier connector.
   :module: delivery
   :notes: English UI, light theme, 1440px width, developer mode on.

================
Expiration dates
================

.. |RFQ| replace:: :abbr:`RFQ (request for quotation)`

.. _inventory/product_management/product_tracking/expiration_dates:

In Odoo, *expiration dates* can be used to manage and track the lifecycles of perishable products,
from purchase to sale. Using expiration dates reduces product loss due to unexpected expiry, and
helps to avoid sending expired products to customers.

In Odoo, only products that are tracked using *lots* and *serial numbers* can be assigned expiration
information. Once a lot or serial number has been assigned, an expiration date can be set. This is
especially helpful for companies (such as food manufacturers) that consistently, or exclusively, buy
and sell perishable products.

.. seealso::
   - :doc:`../product_tracking/lots`
   - :doc:`../product_tracking/serial_numbers`

Enable expiration dates
=======================

To enable the use of *expiration dates*, go to :menuselection:`Inventory app --> Configuration -->
Settings`, and scroll down to the :guilabel:`Traceability` section. Then, click the checkbox to
enable the :guilabel:`Lots & Serial Numbers` feature.

Once that feature is activated, a new option will appear to enable :guilabel:`Expiration Dates`.
Click that checkbox to enable the feature, and be sure to :guilabel:`Save` changes.

.. screenshot:: inventory-expiration-dates-enable
   :menu: Inventory ‣ Configuration ‣ Settings
   :shows: The Inventory settings page scrolled to the "Traceability" section with both the "Lots & Serial
      Numbers" and the "Expiration Dates" checkboxes enabled.
   :highlight: The "Expiration Dates" checkbox (red frame).
   :data: Demo company "YourCompany".
   :module: stock, product_expiry
   :notes: English UI, light theme, 1440px width, crop to the "Traceability" settings block.

.. tip::
   Once the :guilabel:`Lots & Serial Numbers` feature is activated, an additional feature appears to
   :guilabel:`Display Lots & Serial Numbers on Delivery Slips`. Activating these features helps with
   end-to-end traceability, making it easier to manage product recalls, identify batches of faulty
   products, and more.

Configure expiration dates on products
======================================

Once the :guilabel:`Lots & Serial Numbers` and :guilabel:`Expiration Dates` features have been
enabled in the **Inventory** app settings, expiration information can be configured on individual
products.

To do so, go to :menuselection:`Inventory app --> Products --> Products`, and select a product to
edit. Selecting a product reveals the product form for that particular item.

.. important::
   To be tracked using lots or serial numbers, or to configure expiration information, products
   *must* have their :guilabel:`Product Type` set as :guilabel:`Goods` under the :guilabel:`General
   Information` tab. Then, in the :guilabel:`Track Inventory` field, select either :guilabel:`By
   Unique Serial Number` or :guilabel:`By Lots`.

Then, click the :guilabel:`Inventory` tab, and scroll down to the :guilabel:`Traceability` section.
Tick the :guilabel:`Expiration Date` checkbox. Doing so reveals a :guilabel:`Dates` group below it.

.. note::
   If a product has stock on-hand prior to activating tracking by lots or serial numbers, an
   inventory adjustment might need to be performed in order to assign lot numbers to the existing
   stock.

.. tip::
   For processing large quantities of products on receipts or deliveries, it is recommended to track
   using lots, so multiple products can be traced back to the same lot, if any issues arise.

.. screenshot:: inventory-expiration-dates-product-form
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ Inventory tab
   :shows: The "Traceability" section of a product form with the "Expiration Date" checkbox ticked, and the
      "Dates" section below showing the "Expiration Date", "Best Before Date", "Removal Date" and "Alert
      Date" fields filled in.
   :highlight: The "Expiration Date" checkbox and the four "Dates" fields (red frames).
   :data: A perishable lot-tracked product, e.g. expiration 30 days, best before 20, removal 25, alert 15.
   :module: product_expiry
   :notes: English UI, light theme, 1440px width, crop to the Traceability and Dates sections.

The :guilabel:`Dates` group holds four durations, each expressed as a number of days:

- :guilabel:`Expiration Date`: the number of days after receiving products (either from a vendor or
  in stock after production) in which goods may become dangerous and should not be used or consumed.
- :guilabel:`Best Before Date`: the number of days before the expiration date in which the goods
  start deteriorating, **without** being dangerous yet.
- :guilabel:`Removal Date`: the number of days before the expiration date in which the goods should
  be removed from stock.
- :guilabel:`Alert Date`: the number of days before the expiration date in which an alert should be
  raised on goods in a particular lot or containing a particular serial number.

.. note::
   These four fields hold a **number of days**, while the fields of the same name on a lot or serial
   number hold the resulting **dates**, computed from them.

.. note::
   The values entered into these fields automatically compute the expiration date for goods entered
   into stock, whether purchased from a vendor or manufactured in-house.

.. tip::
   If the :guilabel:`Dates` group is left empty, dates (and lots) can still be assigned manually on
   receipts and deliveries in and out of the warehouse.
   Even when assigned, they can still be overwritten and changed manually if needed, as well.

Set expiration dates on receipts with lots & serial numbers
===========================================================

Generating expiration dates for *incoming* goods can be done directly on the :guilabel:`Receipt`.
Navigate to :menuselection:`Inventory app --> Operations --> Receipts`, then click on a line to
open the :guilabel:`Receipt` record.

.. important::
   Clicking :guilabel:`Validate` before assigning a serial number to the ordered product quantities
   causes a :guilabel:`User Error` popup to appear. The popup requires entry of a lot or serial
   number for the ordered products. The receipt cannot be validated without an assigned lot or
   serial number.

   .. screenshot:: inventory-expiration-dates-validate-error
      :menu: Inventory ‣ Receipts ‣ (a receipt) ‣ Validate
      :shows: The user-error pop-up shown when a receipt for a lot- or serial-tracked product is validated
         before any lot or serial number was entered.
      :highlight: The error text (red frame).
      :data: Receipt WH/IN/00001 for a perishable lot-tracked product.
      :module: stock
      :notes: English UI, light theme, 1440px width, crop to the pop-up.

From here, click the :icon:`fa-list` :guilabel:`(Details)` icon located on the of the product line.
When clicked, a :guilabel:`Detailed Operations` pop-up will appear.

In the pop-up, the :guilabel:`Expiration Date` automatically populates, based on the configuration
on the product form. Click the :guilabel:`Lot/Serial Number` field on the appropriate line, then
enter the lot or serial number.

.. tip::
   If the :guilabel:`Dates` group on the product form has not been filled in, the
   :guilabel:`Expiration Date` can be entered by hand.

Click :guilabel:`Save` when finished to close the pop-up. Finally, click :guilabel:`Validate`.

.. screenshot:: inventory-expiration-dates-on-receipt
   :menu: Inventory ‣ Receipts ‣ (a receipt) ‣ Operations tab ‣ (details icon)
   :shows: The detailed-operations pop-up of a receipt line, with the "Lot/Serial Number" entered and the
      "Expiration Date" column pre-filled from the product's date settings.
   :highlight: The "Expiration Date" cell (red frame).
   :data: Lot "LOT0001" of a perishable product with a 30-day expiration time.
   :module: product_expiry
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

A :guilabel:`Traceability` smart button will appear upon validating the receipt. Click the
:guilabel:`Traceability` smart button to see the updated :guilabel:`Traceability Report`, which
includes: a :guilabel:`Reference` document; the :guilabel:`Product` being traced; the
:guilabel:`Lot/Serial #`; and more.

Set expiration dates on manufactured products
=============================================

Expiration dates can also be generated for products manufactured in-house. To assign expiration
dates to manufactured products, a manufacturing order (MO) needs to be completed.

To create a :abbr:`MO (manufacturing order)`, go to :menuselection:`Manufacturing app --> Operations
--> Manufacturing Orders`, and click :guilabel:`New`. Choose a product to manufacture from the
:guilabel:`Product` field drop-down menu, then select the :guilabel:`Quantity` to produce.

.. screenshot:: inventory-expiration-dates-manufacturing-order
   :menu: Manufacturing ‣ Operations ‣ Manufacturing Orders ‣ New
   :shows: A manufacturing order for a perishable, lot-tracked product, with the product, the quantity to
      produce and the component lines to consume.
   :highlight: The "Product" and "Quantity" fields (red frame).
   :data: One manufactured perishable product with two components.
   :module: mrp, product_expiry
   :notes: English UI, light theme, 1440px width, crop to the top of the manufacturing order form.

.. note::
   To manufacture a product, there must be materials to consume in the lines in the
   :guilabel:`Product` column. This can be achieved either by creating a :guilabel:`Bill of
   Material` for the :guilabel:`Product`, or manually adding materials to consume by clicking
   :guilabel:`Add a line`.

Once ready, click :guilabel:`Confirm`.

The appropriate number of :guilabel:`Lots/Serial Numbers` automatically populated in the field.
Click the :icon:`fa-list` :guilabel:`(Details)` icon to reveal additional information for those
specific numbers. On that pop-up, all expiration information that was previously configured for the
product is displayed.

.. screenshot:: inventory-expiration-dates-mo-lot-details
   :menu: Manufacturing ‣ Operations ‣ Manufacturing Orders ‣ (a confirmed order) ‣ (details icon next to
      Lot/Serial Number)
   :shows: The pop-up opened from the "Lot/Serial Number" field of a confirmed manufacturing order, listing
      the generated lot number with all its expiration information (expiration, best before, removal and
      alert date).
   :highlight: The date columns (red frame).
   :data: The lot generated for the manufactured perishable product.
   :module: mrp, product_expiry
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

Sell products with expiration dates
===================================

Selling perishable products with expiration dates is done the same as any other type of product. The
first step in selling perishable products is to create a sales order.

To do that, go to :menuselection:`Sales app --> New` to create a new quotation, and fill out the
information on the sales order form.

Add a :guilabel:`Customer`, then click :guilabel:`Add a product` to add the desired products to the
:guilabel:`Product` lines, and set a :guilabel:`Quantity` for the products.

Then, click the :guilabel:`Other Info` tab. Under the :guilabel:`Delivery` section, change the
:guilabel:`Delivery Date` to a date after the expected date, and click :guilabel:`Apply` to confirm
the date. Finally, click :guilabel:`Confirm` to confirm the sales order.

.. important::
   If the products are delivered before the alert date computed for the lot, then no alerts are
   created.

Next, click the :guilabel:`Delivery` smart button at the top of the sales order to see the warehouse
receipt form.

On the warehouse receipt form, click :guilabel:`Validate`, and then :guilabel:`Apply` in the
accompanying pop-up window, to automatically process all :guilabel:`Done` quantities, and deliver
the products to the customer.

.. important::
   To sell perishable products with expiration dates, the :guilabel:`Removal Strategy` for the
   :guilabel:`Location` the products are stored in must be set to :abbr:`FEFO (First Expiry, First
   Out)`. If there is not enough stock of perishable products in one lot, Odoo will automatically
   take the remaining quantity required from a second lot with the next-soonest expiration date.
   Removal strategies can also be set on :guilabel:`Product Categories`.

.. seealso::
   :doc:`../../shipping_receiving/removal_strategies`

View expiration dates for lots & serial numbers
===============================================

To view (and/or group) all products with expiration dates by lot number, go to
:menuselection:`Inventory app --> Products --> Lots/Serial Numbers`.

Once there, remove any default search filters from the search bar. Then, click :guilabel:`Group By`,
choose :guilabel:`Add Custom Group`, and select the :guilabel:`Expiration Date` parameter from the
drop-down menu. Doing so breaks down all perishable products, their expiration dates, and the
assigned lot number.

.. screenshot:: inventory-expiration-dates-group-by
   :menu: Inventory ‣ Products ‣ Lots/Serial Numbers
   :shows: The Lots/Serial Numbers list with the default filters removed and a custom group by "Expiration
      Date" applied, so perishable products are listed per expiration date with their lot numbers.
   :highlight: The applied "Expiration Date" group in the search bar (red frame).
   :data: Several lots of perishable products with different expiration dates.
   :module: product_expiry
   :notes: English UI, light theme, 1440px width, show the search bar and the grouped list.

.. tip::
   Customers can also view the expiration date alert in their customer portal.

.. _inventory/product_management/expiration-alerts:

Expiration alerts
-----------------

To see expiration alerts, go to :menuselection:`Inventory app --> Products --> Lots/Serial Numbers`.

Then, click into a :guilabel:`Lot/Serial Number` with perishable products. Doing so reveals the
serial number detail form.

.. tip::
   To view expiration date information in the list view, click the :icon:`oi-settings-adjust`
   :guilabel:`(adjust settings)` icon at the top of the list of records, then tick the
   :guilabel:`Expiration Date` checkbox.

On the :guilabel:`Lot/Serial Number` detail form, the :guilabel:`Dates` tab lists all expiration
information of that lot or serial number.

If the expiration date for a lot/serial number has passed, the form displays a red
:guilabel:`Expiration Alert` at the top of the page to indicate that the products in this lot are
either expired or expiring soon.

From here, click back to the :guilabel:`Lots/Serial Numbers` page (via the breadcrumbs).

To see the new expiration alert, or any expiration alerts for products that are expired (or will
expire soon), click back to the :guilabel:`Lots/Serial Numbers` page via the breadcrumbs. Remove
all of the search filters from the search bar on the :guilabel:`Lots/Serial Numbers` dashboard.

Then, click :guilabel:`Filters`, and choose :guilabel:`Expiration Alerts`.

.. screenshot:: inventory-expiration-dates-alert-filter
   :menu: Inventory ‣ Products ‣ Lots/Serial Numbers ‣ Filters ‣ Expiration Alerts
   :shows: The Lots/Serial Numbers list filtered with "Expiration Alerts", listing the lots whose expiration
      date has passed or is close, with their expiration date column shown.
   :highlight: The "Expiration Alerts" filter facet in the search bar (red frame).
   :data: At least one expired lot and one lot inside its alert period.
   :module: product_expiry
   :notes: English UI, light theme, 1440px width, show the search bar and the list.

Expiration notifications
------------------------

Users can be notified when the expiration date for a product has passed. This can help keep specific
employees up to date on the status of items under their purview.

To configure a notification, navigate to :menuselection:`Inventory app --> Products --> Products`.
Select a product configured with lot/serial numbers and expiration date tracking. Navigate to the
:guilabel:`Inventory` tab. Under the :guilabel:`Logistics` section, select a user in the
:guilabel:`Responsible` field.

When the expiration date passes for a lot/serial number for this product, a notification is sent to
the user in this field.

.. note::
   Once the expiration date is due, expiration alerts are created on the form view of the lot/serial
   number of the product.

   To customize these alerts, turn on :ref:`developer mode <developer-mode>`, go to
   :menuselection:`Settings app --> Technical --> Activity Types`, and select the :guilabel:`Alert
   Date Reached` activity type.

   The :guilabel:`Default User` assigned will be notified once the expiration date is reached. If no
   default user is configured, the activity will be assigned to the :guilabel:`Responsible` user
   selected on the product's :guilabel:`Inventory` tab.

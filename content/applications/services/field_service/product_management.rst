==================
Product management
==================

Technicians usually consume materials during an intervention. The :guilabel:`Products` tab of the
task records what was used, at which price, and at which cost, so that the intervention can be
billed and its profitability measured.

Configuration
=============

The tab is displayed on the tasks of every project whose :ref:`category <field_service/category>`
has the :guilabel:`Product` option enabled.

.. _field_service/products-tab:

Recording the products used
===========================

Open the task and go to the :guilabel:`Products` tab. Each line holds:

- :guilabel:`Product` – the product or material used.
- :guilabel:`Quantity` and :guilabel:`UoM` – the unit of measure defaults to the product's own unit.
- :guilabel:`Unit Price` and :guilabel:`Subtotal` – computed from the :guilabel:`Pricelist` of the
  task (see below).
- :guilabel:`Unit Cost` and :guilabel:`Subtotal Cost` – the product's cost, converted into the
  task's currency. These two columns are only visible to users with purchase access rights.

The :guilabel:`Quantity`, :guilabel:`Subtotal`, and :guilabel:`Subtotal Cost` columns are totaled at
the bottom of the list, giving the material value and the material cost of the intervention at a
glance.

.. note::
   The tab becomes read-only once the task is set to :guilabel:`Done` or :guilabel:`Canceled`, so a
   closed intervention can no longer be modified.

.. screenshot:: services-field-service-products-tab
   :menu: Project ‣ (field service project) ‣ (open a task) ‣ Products
   :shows: The Products tab of a task with three product lines; the Quantity, Subtotal and Subtotal Cost columns show their sums in the footer.
   :highlight: The Products tab and its totals row (red frame).
   :data: Products "Copper pipe 15 mm" 4 m, "Gasket set" 1 unit, "Circulation pump" 1 unit; pricelist "Public Pricelist (HUF)".
   :module: eyssen_project_product
   :notes: English UI, light theme, 1440px width, crop to the tab.

.. _field_service/pricelist:

Pricelist and currency
======================

Field service tasks carry a :guilabel:`Pricelist` field. When a :guilabel:`Customer` is set, the
pricelist of that customer is proposed automatically; it can be changed manually as long as the
task is not done or canceled. The prices in the :guilabel:`Products` tab, and the currency in which
they are expressed, follow this pricelist.

.. seealso::
   - :doc:`../../sales/sales/products_prices/prices/pricing`
   - :doc:`worksheets`

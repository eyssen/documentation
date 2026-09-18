==========
Pricelists
==========

Pricelists allow you to adjust product prices depending on various criteria automatically. For
example, you can set POS-specific prices, create temporary discount periods, reward specific
customers, or offer discounts when set quantities are ordered.

.. _pricelists/configuration:

Configuration
=============

Navigate to the :ref:`general POS app settings <configuration/settings>` and ensure
:guilabel:`Flexible Pricelists` are enabled under the :guilabel:`Pricing` section.

Once enabled, select the pricelists that the cashiers may pick from in the :guilabel:`Available`
field, and the one applied by default in the :guilabel:`Default` field.

.. screenshot:: pos-pricelists-setting
   :menu: Point of Sale ‣ Configuration ‣ Settings
   :shows: The "Pricing" section of the POS settings with the "Flexible Pricelists" option
      enabled, two pricelists in the "Available" field and one in the "Default" field.
   :highlight: The "Pricelists" setting block (red frame).
   :module: point_of_sale, product
   :notes: English UI, light theme, 1440px width, crop to the settings block.

.. note::
   Pricelists are shared with the rest of the database, including the :doc:`Sales
   <../../sales/products_prices/prices/pricing>` and :ref:`eCommerce <ecommerce/prices/pricelists>`
   apps.

.. _pricelists/create:

Create pricelists
-----------------

Go to :menuselection:`Point of Sale --> Products --> Pricelists` and click :guilabel:`New` or
select an existing pricelist. Name the pricelist, set its :guilabel:`Currency` and, if the pricelist
is reserved for one company, its :guilabel:`Company`. Then add the price rules on the
:guilabel:`Price Rules` tab.

.. _pricelists/simple:

Fixed prices
~~~~~~~~~~~~

The simplest rule sets a fixed price for a product or one of its variants, optionally under
conditions. To add one:

#. Click :guilabel:`Add a line`, and select a **product** and its **variant** if needed.
#. Add the condition(s):

   - a product quantity to be reached by using the :guilabel:`Min. Quantity` column;
   - a determined period during which the pricelist is applied by using the :guilabel:`Start Date`
     and :guilabel:`End Date` columns.

#. Add the :guilabel:`Price` to be applied when the conditions are met (if any).

.. screenshot:: pos-pricelists-multiple-prices
   :menu: Point of Sale ‣ Products ‣ Pricelists ‣ New
   :shows: A pricelist form with three fixed-price rules applied to two products and a product
      category.
   :data: Pricelist "Wholesale" with rules on "Desk Organizer", "Cabinet with Doors" and the "Office Furniture" category.
   :module: product
   :notes: English UI, light theme, 1440px width.

.. _pricelists/advanced:

Advanced price rules
~~~~~~~~~~~~~~~~~~~~

Beside fixed prices, a price rule can compute the price with a percentage discount or mark-up, or
with a formula. Open a price rule (or click :guilabel:`Add a line` and then the rule's internal
link) to reach the full rule form:

#. Select a :guilabel:`Compute Price` method:

   - :guilabel:`Fixed Price` to set a new fixed price.
   - :guilabel:`Discount` to compute a percentage discount (e.g., `10.00` %) or mark-up (e.g.,
     `-10.00` %).
   - :guilabel:`Formula` to compute the price according to a formula. It is required to define what
     the calculation is **based on** (:guilabel:`Sales Price`, :guilabel:`Cost`, or :guilabel:`Other
     Pricelist`). You can then:

     - Apply a percentage :guilabel:`Discount` or mark-up.
     - Add an :guilabel:`Extra Fee` (e.g., $ `5.00`) or subtract a fixed amount (e.g., $ `-5.00`).
     - Define a :doc:`Rounding Method <cash_rounding>` by forcing the price after
       :guilabel:`Discount` to be a multiple of the value set. The :guilabel:`Extra Fee` is applied
       afterward.

       .. example::
          To have the final price end with `.99`, set the :guilabel:`Rounding Method` to `1.00` and
          the :guilabel:`Extra Fee` to `-0.01`.

     - Specify the minimum (e.g., $ `20.00` ) and maximum (e.g., $ `50.00` ) profit
       :guilabel:`Margins` for computations based on :guilabel:`Cost`.

#. Select on which product(s) the price rule should be **applied**:

   - :guilabel:`All Products`
   - a :guilabel:`Product Category`
   - a :guilabel:`Product`
   - a :guilabel:`Product Variant`

#. Add conditions, such as a specific quantity to reach for the price to change by using the
   :guilabel:`Min. Quantity` field or a specific period during which the pricelist should be
   applied by using the :guilabel:`Validity` fields.

.. screenshot:: pos-pricelists-advanced-rule
   :menu: Point of Sale ‣ Products ‣ Pricelists ‣ (a pricelist) ‣ (a price rule)
   :shows: An advanced price rule form with the computation set to a percentage discount, a minimum quantity, rounding and margin fields, and the validity dates.
   :module: product
   :notes: English UI, light theme, 1440px width.

Select pricelists
-----------------

Go to the :ref:`specific POS settings <configuration/settings>` and add all the available
pricelists in the :guilabel:`Available` field. Then, set its **default pricelist** in the
:guilabel:`Default` field.

When you :ref:`open a POS session <pos/session-start>`, click the **pricelists** button, and select
the desired pricelist from the list.

.. screenshot:: pos-pricelists-frontend-button
   :menu: (POS interface) ‣ Register screen
   :shows: The POS register screen with the pricelist button in the button bar and the list of available pricelists open.
   :highlight: The pricelist button (red frame).
   :module: point_of_sale, product
   :notes: English UI, light theme, 1440px width.

.. note::
   - Multiple pricelists must be selected for the **pricelist button** to be displayed.
   - If a pricelist is selected on a POS order while its conditions are **not** met, the price will
     **not** be adjusted.

.. tip::
   You can also set a pricelist to be selected automatically once a specific :ref:`customer is set
   <pos/customers>`. To do so, go to the customer form and switch to the preferred pricelist in the
   :guilabel:`Pricelist` field of the :guilabel:`Sales & Purchase` tab.

.. seealso::
   - :doc:`../../sales/products_prices/prices/pricing`
   - :ref:`How to use pricelists in an ecommerce environment <ecommerce/prices/pricelists>`

.. _pos/pricelists/tags:

Pricelist rules based on product tags
=====================================

The *Price List Validation by Tags for POS* module (`eyssen_pos_product_pricelist_tag`) makes the
pricelist rules that are :doc:`applied on a pricelist tag
<../../../inventory_and_mrp/inventory/product_management/pricing_extensions>` work in the POS as
well: the tags of the products and the tag of each price rule are loaded into the session, so the
discount is computed on the register exactly as it is in the back end.

No POS-side configuration is needed beyond selecting the pricelist as usual; the tags and the rules
are maintained on the products and the pricelists.

.. note::
   This module requires the *Price List Validation by Tags* module
   (`eyssen_product_pricelist_tag`).

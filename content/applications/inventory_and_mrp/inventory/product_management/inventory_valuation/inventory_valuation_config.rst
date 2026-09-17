=============================
Automatic inventory valuation
=============================

.. |right arrow| replace:: :icon:`fa-arrow-right` :guilabel:`(right arrow)`

All of a company's stock on-hand contributes to the valuation of its inventory. That value should
be reflected in the company's accounting records to accurately show the value of the company and
all of its assets.

By default, Odoo uses a periodic inventory valuation (also known as manual inventory valuation).
This method implies that the accounting team manually posts journal entries, based on the physical
inventory of the company, and warehouse employees take the time to count the stock. In Odoo, each
product category reflects this, with the :guilabel:`Costing Method` set to :guilabel:`Standard
Price`, and the :guilabel:`Inventory Valuation` (not visible by default) set to :guilabel:`Manual`.

.. screenshot:: inventory-valuation-config-costing-method
   :menu: Inventory ‣ Configuration ‣ Product Categories ‣ (a category)
   :shows: A product category form, "Inventory Valuation" section, with the "Costing Method" field set to
      "Standard Price" and the "Inventory Valuation" field set to "Manual".
   :highlight: The "Costing Method" field (red frame).
   :data: Product category "All / Saleable".
   :module: stock_account
   :notes: English UI, light theme, 1440px width, crop to the "Inventory Valuation" section. The "Inventory
      Valuation" field is only visible once automatic stock accounting is enabled.

Alternatively, perpetual (automatic) inventory valuation creates real-time *journal entries* in the
*Accounting* app whenever stock enters or leaves the company's warehouse.

This document is focused on the proper setup of automatic inventory valuation, which is an
integrated valuation method that ensures journal entries in the *Accounting* app match stock
valuation updates in the *Inventory* app. For an introduction of inventory valuation in Odoo, refer
to the :doc:`using_inventory_valuation` documentation.

.. warning::
   Switching from manual to automatic inventory valuation may cause discrepancies between stock
   valuation and accounting journals.

   One successful strategy for switching to automated valuation:

   #. Clear existing stock (possibly with an :doc:`inventory adjustment
      <../../warehouses_storage/inventory_management/count_products>`)
   #. Change the inventory valuation method to *Automatic*
   #. Return the existing stock, with the original monetary value (using an inventory adjustment)

   Once the existing stock is recovered, the Odoo *Accounting* app automatically generates the
   journal entries to corresponding stock valuation records.

Configuration
=============

To properly set up automatic inventory valuation, follow these steps in Odoo:

#. :ref:`Install Accounting app and enable specific settings
   <inventory/warehouses_storage/accounting-setup>`
#. :ref:`Set Automatic inventory valuation on product categories
   <inventory/warehouses_storage/valuation-on-product-category>`
#. :ref:`Set costing method <inventory/warehouses_storage/costing_methods>`

.. _inventory/warehouses_storage/accounting-setup:

Accounting setup
----------------

To use automatic inventory valuation, install the *Accounting* app. Next, go to
:menuselection:`Accounting app --> Configuration --> Settings`, and in the :guilabel:`Inventory
Valuation` section, tick the :guilabel:`Automatic Stock Accounting` checkbox. Then, click
:guilabel:`Save`.

Once the checkbox is ticked, the company-wide default accounts used by inventory valuation appear
right below it: :guilabel:`Stock Valuation Account`, :guilabel:`Stock Journal`, :guilabel:`Stock
Input Account` and :guilabel:`Stock Output Account`. A separate :guilabel:`Inventory Ledger
Accounts` setting in the same block holds the default :guilabel:`Income Account` and
:guilabel:`Expense Account`. Every value set here is the company default; each product category can
still override it on its own form.

.. note::
   - Enabling :guilabel:`Automatic Stock Accounting` shows the previously invisible *Inventory
     Valuation* field on a product category.
   - Turning the setting **off** again resets every product category that was set to *Automated*
     back to *Manual*.

.. note::
   The :guilabel:`Inventory Valuation` block in the accounting settings is provided by the
   ``eyssen_stock_accountant`` module. Without it, the same accounts are still available, but only
   on each product category's form.

.. screenshot:: inventory-valuation-config-automatic-accounting
   :menu: Accounting ‣ Configuration ‣ Settings
   :shows: The Accounting settings page scrolled to the "Inventory Valuation" block, with "Automatic Stock
      Accounting" enabled and the Stock Valuation Account, Stock Journal, Stock Input Account and Stock
      Output Account fields visible below it.
   :highlight: The "Automatic Stock Accounting" checkbox (red frame).
   :data: Demo company "YourCompany HU" with a Hungarian chart of accounts.
   :module: stock_account, eyssen_stock_accountant
   :notes: English UI, light theme, 1440px width, crop to the "Inventory Valuation" settings block.

Refer to the :ref:`Expense <inventory/warehouses_storage/expense-account>` and :ref:`Stock
input/output <inventory/warehouses_storage/stock-account>` sections of documentation for details on
configuring the accounting journals shown.

.. _inventory/warehouses_storage/valuation-on-product-category:

Product category setup
----------------------

After :ref:`enabling inventory valuation <inventory/warehouses_storage/accounting-setup>`, the next
step is to set the product category to use automatic inventory valuation.

Go to :menuselection:`Inventory app --> Configuration --> Product Categories`, and select the
desired product category. In the :guilabel:`Inventory Valuation` section, set the
:guilabel:`Inventory Valuation` field to :guilabel:`Automated`. Repeat this step for every product
category intending to use automatic inventory valuation.

.. note::
   After enabling automatic accounting, each new stock move layer (SVL), that is created during
   inventory valuation updates, generates a journal entry.

.. screenshot:: inventory-valuation-config-category-automated
   :menu: Inventory ‣ Configuration ‣ Product Categories ‣ (a category)
   :shows: A product category form with "Inventory Valuation" set to "Automated", so the "Account Stock
      Properties" section with the stock accounts and the stock journal appears.
   :highlight: The "Inventory Valuation" field and the "Account Stock Properties" section (red frames).
   :data: Product category "All / Saleable", costing method FIFO.
   :module: stock_account
   :notes: English UI, light theme, 1440px width, crop to the two sections.

.. _inventory/warehouses_storage/costing_methods:

Costing method
==============

After :ref:`enabling inventory valuation <inventory/warehouses_storage/accounting-setup>`, the
*costing method* for calculating and recording inventory costs is defined on the product category in
Odoo.

Go to :menuselection:`Inventory app --> Configuration --> Product Categories` and select the desired
product category. In the :guilabel:`Inventory Valuation` section, select the appropriate
:guilabel:`Costing Method`:


.. tabs::

   .. tab:: Standard Price

      The default costing method in Odoo. The cost of the product is manually defined on the product
      form, and this cost is used to compute the valuation. Even if the purchase price on a purchase
      order differs, the valuation is the cost defined on the product form.

      .. list-table::
         :header-rows: 1
         :stub-columns: 1

         * - Operation
           - Unit Cost
           - Qty On Hand
           - Incoming Value
           - Inventory Value
         * -
           - $10
           - 0
           -
           - $0
         * - Receive 8 products for $10/unit
           - $10
           - 8
           - 8 * $10
           - $80
         * - Receive 4 products for $16/unit
           - $10
           - 12
           - 4 * $10
           - $120
         * - Deliver 10 products
           - $10
           - 2
           - -10 * $10
           - $20
         * - Receive 2 products for $9/unit
           - $10
           - 4
           - 2 * $10
           - $40

   .. tab:: Average Cost (AVCO)

      Calculates the valuation of a product based on the average cost of that product, divided by
      the total number of available stock on-hand. With this costing method, inventory valuation is
      *dynamic*, and constantly adjusts based on the purchase price of products.

      .. list-table::
         :header-rows: 1
         :stub-columns: 1

         * - Operation
           - Unit Cost
           - Qty On Hand
           - Incoming Value
           - Inventory Value
         * -
           - $0
           - 0
           -
           - $0
         * - Receive 8 products for $10/unit
           - $10
           - 8
           - 8 * $10
           - $80
         * - Receive 4 products for $16/unit
           - $12
           - 12
           - 4 * $16
           - $144
         * - Deliver 10 products
           - $12
           - 2
           - -10 * $12
           - $24
         * - Receive 2 products for $6/unit
           - $9
           - 4
           - 2 * $6
           - $36

      How are unit cost and inventory value calculated at each step?

      - When receiving four products for $16 each:

        - Inventory value is calculated by adding the previous inventory value with the incoming
          value: :math:`$80 + (4 * $16) = $144`.
        - Unit cost is calculated by dividing the inventory value by the quantity on-hand:
          :math:`$144 / 12 = $12`.

      - When delivering ten products, the average unit cost is used to calculate the inventory
        value, regardless of the purchase price of the product. Therefore, inventory value is
        :math:`$144 + (-10 * $12) = $24`.

      - Receive two products for $6 each:

        - Inventory value: :math:`$24 + (2 * $6) = $36`
        - Unit cost: :math:`$36 / 4 = $9`

      .. note::
         When choosing :guilabel:`Average Cost (AVCO)` as the :guilabel:`Costing Method`, changing
         the numerical value in the *Cost* field for products in the respective product category
         creates a new record in the *Inventory Valuation* report to adjust the value of the
         product. The *Cost* amount is then automatically updated, based on the average purchase
         price of both the inventory on-hand and the costs accumulated from validated purchase
         orders.

   .. tab:: First In First Out (FIFO)

      Tracks the costs of incoming and outgoing items in real-time, and uses the real price of the
      products to change the valuation. The oldest purchase price is used as the cost for the next
      good sold, until an entire lot of that product is sold. When the next inventory lot moves up
      in the queue, an updated product cost is used based on the valuation of that specific lot.

      This method is arguably the most accurate inventory valuation method for a variety of reasons,
      but it is highly sensitive to input data and human error.

      .. list-table::
         :header-rows: 1
         :stub-columns: 1

         * - Operation
           - Unit Cost
           - Qty On Hand
           - Incoming Value
           - Inventory Value
         * -
           - $0
           - 0
           -
           - $0
         * - Receive 8 products for $10/unit
           - $10
           - 8
           - 8 * $10
           - $80
         * - Receive 4 products for $16/unit
           - $12
           - 12
           - 4 * $16
           - $144
         * - Deliver 10 products
           - $16
           - 2
           - | -8 * $10
             | -2 * $16
           - $32
         * - Receive 2 products for $6/unit
           - $11
           - 4
           - 2 * $6
           - $44

      How are unit cost and inventory value calculated at each step?

      - When receiving four products for $16 each:

        - Inventory value is calculated by adding the previous inventory value to the incoming
          value: :math:`$80 + (4 * $16) = $144`.
        - Unit cost is calculated by dividing the inventory value by the quantity on-hand:
          :math:`$144 / 12 = $12`.

         - When delivering ten products, eight units were purchased for $10, and two units were
           purchased for $16.

        - First, the incoming value is calculated by multiplying the on-hand quantity by the
          purchased price: :math:`(-8 * $10) + (-2 * $16) = -112`.
        - The inventory value is calculated by subtracting the incoming value from the previous
          inventory value: :math:`$144 - $112 = $32`.
        - Unit cost is calculated by dividing the inventory value by the remaining quantity:
          :math:`$32 / 2 = $16`.

      - When receiving two products for $6, inventory value is :math:`$32 + $12 = $44`. Unit cost is
        :math:`$44 / 4 = $11`.

.. warning::
   Changing the costing method greatly impacts inventory valuation. It is highly recommended to
   consult an accountant first before making any adjustments here.

.. seealso::
   :doc:`using_inventory_valuation`

When the :guilabel:`Costing Method` is changed, products already in stock that were using the
:guilabel:`Standard` costing method **do not** change value; rather, the existing units keep their
value, and any product moves from then on affect the average cost, and the cost of the product will
change. If the value in the :guilabel:`Cost` field on a product form is changed manually, Odoo
generates a corresponding record in the *Inventory Valuation* report.

.. note::
   It is possible to use different valuation settings for different product categories.

.. _inventory/warehouses_storage/accounting-types:

Types of accounting
===================

With automated inventory valuation set up, the generated journal entries depend on the chosen
accounting mode: *Continental* or *Anglo-Saxon*.

.. tip::
   Verify the accounting mode by activating the :ref:`developer-mode`, and navigating to
   :menuselection:`Accounting app --> Configuration --> Settings`.

   Then, in the :guilabel:`Search...` bar, look for `Anglo-Saxon Accounting`, to see if the feature
   is enabled. If it is **not** enabled, *Continental* accounting mode is in use.

   .. screenshot:: inventory-valuation-config-anglo-saxon
      :menu: Accounting ‣ Configuration ‣ Settings
      :shows: The Accounting settings page with "Anglo-Saxon Accounting" found through the settings search
         box, showing whether the checkbox is enabled.
      :highlight: The "Anglo-Saxon Accounting" checkbox (red frame).
      :data: Demo company "YourCompany HU".
      :module: om_account_accountant
      :notes: English UI, light theme, 1440px width, crop to the setting. Requires developer mode.

In *Anglo-Saxon* accounting, the costs of goods sold (COGS) are reported when products are sold or
delivered. This means the cost of a good is only recorded as an expense when a customer is invoiced
for a product.

So, for **manual** valuation method, set the *Expense Account* to *Stock Valuation* for the current
asset type; for **automatic** valuation method, set the *Expense Account* to an *Expenses* or a
*Cost of Revenue* type (e.g. *Cost of Production*, *Cost of Goods Sold*, etc.).

In *Continental* accounting, the cost of a good is reported as soon as a product is received into
stock. Because of this, the *Expense Account* can be set to **either** *Expenses* or a *Cost of
Revenue* type, however, it is more commonly set to an *Expenses* account.

Refer to the :ref:`Expense <inventory/warehouses_storage/expense-account>` and :ref:`Stock
input/output <inventory/warehouses_storage/stock-account>` sections for details on configuring each
account type.

.. _inventory/warehouses_storage/expense-account:

Expense account
---------------

To configure the *expense account*, which is used in both manual and automatic inventory valuation,
go to the :guilabel:`Account Properties` section of the intended product category
(:menuselection:`Inventory app --> Configuration --> Product Categories`). Then, choose an existing
account from the :guilabel:`Expense Account` drop-down menu.

To ensure the chosen account is the correct :guilabel:`Type,` click the |right arrow| icon to the
right of the account. Then, set the account type based on the information below.

.. tabs::

   .. group-tab:: Anglo-Saxon

      .. tabs::

         .. group-tab:: Automated

            In Anglo-Saxon accounting for automated inventory valuation, set the :guilabel:`Expense
            Account` to the `Expenses` account. Then, click the |right arrow| icon to the right of
            the account.

            In the pop-up window, choose :guilabel:`Expenses` or :guilabel:`Cost of Revenue` from
            the :guilabel:`Type` drop-down menu.

            .. screenshot:: inventory-valuation-config-expense-account-link
               :menu: Inventory ‣ Configuration ‣ Product Categories ‣ (a category)
               :shows: The "Account Properties" section of a product category with the "Expense Account"
                  field filled in and the internal-link (right arrow) icon next to it.
               :highlight: The "Expense Account" field and the internal-link icon (red frame).
               :data: Expense account of the "Expenses" type.
               :module: stock_account
               :notes: English UI, light theme, 1440px width, crop to the field.

         .. group-tab:: Manual

            To configure the :guilabel:`Expense Account`, choose :guilabel:`Stock Valuation` from
            the field's drop-down menu. Verify the account's type by clicking the |right arrow|
            icon, and then ensure the :guilabel:`Type` is :guilabel:`Current Assets`.

            .. screenshot:: inventory-valuation-config-expense-account-manual
               :menu: Inventory ‣ Configuration ‣ Product Categories ‣ (a category)
               :shows: The "Expense Account" field of a product category set to a "Stock Valuation" account,
                  used for manual (periodic) valuation under Anglo-Saxon accounting.
               :highlight: The "Expense Account" field (red frame).
               :data: Expense account of the "Current Assets" type named "Stock Valuation".
               :module: stock_account
               :notes: English UI, light theme, 1440px width, crop to the field.

   .. group-tab:: Continental

      .. tabs::

         .. group-tab:: Automated

            Set the :guilabel:`Expense Account` to the :guilabel:`Expenses` or :guilabel:`Cost of
            Revenue` account type.

         .. group-tab:: Manual

            Set the :guilabel:`Expense Account` to the :guilabel:`Expenses` or :guilabel:`Cost of
            Revenue` account type.

.. _inventory/warehouses_storage/stock-account:

Stock input/output (automated only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To configure the :guilabel:`Stock Input Account` and :guilabel:`Stock Output Account`, go to
:menuselection:`Inventory app --> Configuration --> Product Categories` and select the desired
product category.

In the :guilabel:`Inventory Valuation` field, select :guilabel:`Automated`. Doing so makes the
:guilabel:`Account Stock Properties` section appear. These accounts are defined as follows:

- :guilabel:`Stock Valuation Account`: when automated inventory valuation is enabled on a product,
  this account will hold the current value of the products.
- :guilabel:`Stock Journal`: accounting journal where entries are automatically posted when a
  product's inventory valuation changes.
- :guilabel:`Stock Input Account`: counterpart journal items for all incoming stock moves will be
  posted in this account, unless there is a specific valuation account set on the source location.
  This is the default value for all products in a given category, and can also be set directly on
  each product.
- :guilabel:`Stock Output Account`: counterpart journal items for all outgoing stock moves will be
  posted in this account, unless there is a specific valuation account set on the destination
  location. This is the default value for all products in a given category, and can also be set
  directly on each product.

.. tabs::

   .. group-tab:: Anglo-Saxon

      In Anglo-Saxon accounting, the :guilabel:`Stock Input Account` and :guilabel:`Stock Output
      Account` are set to *different* :guilabel:`Current Assets` accounts. This way, delivering
      products and invoicing the customer balance the *Stock Output* account, while receiving
      products and billing vendors balance the *Stock Input* account.

      To modify the account type, go to the click the |right arrow| icon to the right of the stock
      input/output account. In the pop-up window, choose :guilabel:`Current Assets` from the
      :guilabel:`Type` drop-down menu.

      .. screenshot:: inventory-valuation-config-account-type
         :menu: Inventory ‣ Configuration ‣ Product Categories ‣ (a category) ‣ Stock Input Account ‣
            (internal link)
         :shows: The account form opened from the "Stock Input Account" field, with the "Type" field set to
            "Current Assets".
         :highlight: The "Type" field (red frame).
         :data: Account "Stock Interim (Received)".
         :module: account
         :notes: English UI, light theme, 1440px width, crop to the pop-up. Caption to convey: the Stock
            Input account is set to Stock Interim (Received), a Current Asset account type.

   .. group-tab:: Continental

      In Continental accounting, the :guilabel:`Stock Input Account` and :guilabel:`Stock Output
      Account` are set to **the same** :guilabel:`Current Assets` account. That way, one account can
      be balanced when items are bought and sold.

      .. example::
         The stock input and output accounts are both set to `Stock Interim (Received)`, a
         :guilabel:`Current Assets` account type. They can also be set to the `Stock Interim
         (Delivered)`, as long as the input and output accounts are assigned to the **same**
         account.

         .. screenshot:: inventory-valuation-config-continental-accounts
            :menu: Inventory ‣ Configuration ‣ Product Categories ‣ (a category)
            :shows: The "Account Stock Properties" section of a product category where the "Stock Input
               Account" and the "Stock Output Account" are set to the same account.
            :highlight: The two account fields holding the same value (red frame).
            :data: Both fields set to "Stock Interim (Received)", a Current Assets account.
            :module: stock_account
            :notes: English UI, light theme, 1440px width, crop to the section.

Inventory valuation reporting
=============================

To start, go to :menuselection:`Accounting app --> Dynamic Reports --> Balance Sheet`. Click the
:guilabel:`Current Assets` line item to unfold it, and look for the nested :guilabel:`Stock
Valuation`, :guilabel:`Stock Interim (Received)` and :guilabel:`Stock Interim (Delivered)` lines.

.. tip::
   Set the date range at the top of the report to show accounting records up to a chosen date.

.. seealso::
   - :ref:`Stock accounts and what they do <inventory/warehouses_storage/stock-account>`
   - :doc:`../../../../finance/accounting/get_started/cheat_sheet`
   - :doc:`Stock valuation dashboard <../../warehouses_storage/reporting/aging>`

.. screenshot:: inventory-valuation-config-balance-sheet
   :menu: Accounting ‣ Dynamic Reports ‣ Balance Sheet
   :shows: The Balance Sheet report with the "Current Assets" line unfolded, showing the nested "Stock
      Valuation", "Stock Interim (Received)" and "Stock Interim (Delivered)" lines with their balances.
   :highlight: The three stock account lines (red frame).
   :data: Demo company "YourCompany HU" with automatic stock accounting and a few validated receipts and
      deliveries.
   :module: account_dynamic_reports
   :notes: English UI, light theme, 1440px width, crop to the Current Assets block.

For the individual entries behind a stock account, open :menuselection:`Accounting app --> Dynamic
Reports --> General Ledger` and filter on that account. Every journal item generated by a validated
stock move is listed there with the warehouse operation as its reference (e.g. `WH/IN/00014`), and
the item can be opened to inspect the full journal entry.

.. screenshot:: inventory-valuation-config-stock-journal-items
   :menu: Accounting ‣ Dynamic Reports ‣ General Ledger
   :shows: The General Ledger report filtered on the stock valuation account, listing the journal items
      generated by the validated stock moves with their reference and amount.
   :highlight: The account filter and the listed journal items (red frames).
   :data: Journal items whose reference matches warehouse operations such as WH/IN/00014.
   :module: account_dynamic_reports
   :notes: English UI, light theme, 1440px width, full report view.

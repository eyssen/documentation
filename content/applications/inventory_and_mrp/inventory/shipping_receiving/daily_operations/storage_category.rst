==================
Storage categories
==================

A *storage category* is used with :doc:`putaway rules <putaway>` to assign a storage location to
incoming products while accounting for the capacity of that location.

Follow these steps to complete the setup:

#. :ref:`Enable features in the settings <inventory/routes/enable-storage-categories>`
#. :ref:`Define capacity limitations <inventory/routes/define-storage>`
#. Assign a :ref:`category to storage locations <inventory/routes/assign-location>`
#. Add the storage category as an attribute to a :ref:`putaway rule
   <inventory/routes/set-putaway-attribute>`

.. seealso::
   :doc:`putaway`

.. note::
   Assigning categories to storage locations tells Odoo these locations meet specific requirements,
   such as temperature or accessibility. Odoo then evaluates these locations, based on defined
   capacity, and recommends the best one on the warehouse transfer form.

.. _inventory/routes/enable-storage-categories:

Configuration
=============

To enable storage categories, go to :menuselection:`Inventory app --> Configuration --> Settings`.
Then, in the :guilabel:`Warehouse` section, ensure the :guilabel:`Storage Locations` and
:guilabel:`Multi-Step Routes` features are enabled.

If intending to set capacities by :ref:`package type <inventory/routes/set-capacity-package>`, also
make sure :guilabel:`Packages` is enabled. Click :guilabel:`Save`.

.. screenshot:: daily-operations-storage-category-enable-categories
   :menu: Inventory app ‣ Configuration ‣ Settings
   :shows: The Inventory settings page scrolled to "Warehouse", with "Storage Locations", "Multi-Step Routes" and "Storage Categories" enabled.
   :highlight: The "Storage Categories" checkbox (red frame).
   :module: stock
   :notes: English UI, light theme, 1440px width.

.. _inventory/routes/define-storage:

Define storage category
=======================

A storage category with specific limitations **must** be created first, before it is applied to
locations, in order to decide the optimal storage location.

To create a storage category, go to :menuselection:`Inventory app --> Configuration --> Storage
Categories`, and click :guilabel:`New`.

On the storage category form, type a name for the category in the :guilabel:`Storage Category`
field.

Options are available to limit capacity by weight, product, and package type.

.. note::
   Weight limits can be combined with capacity by package or product (e.g. a maximum of one hundred
   products with a total weight of two hundred kilograms).

   While it is possible to limit capacity by product and package type at the same location, it may
   be more practical to store items in different amounts across various locations, as shown in this
   example of :ref:`capacity by package <inventory/routes/set-capacity-package>`.

The :guilabel:`Allow New Product` field defines when the location is considered available to store a
product:

- :guilabel:`If location is empty`: a product can be added there only if the location is empty.
- :guilabel:`If products are the same`: a product can be added there only if the same product is
  already there.
- :guilabel:`Allow mixed products`: several different products can be stored in this location at the
  same time.

.. tip::
   When clicked, the :icon:`oi-arrows-v` :guilabel:`Locations` smart button shows which storage
   locations the category has been assigned to.

.. important::
   Odoo does **not** automatically split quantities across multiple storage locations. If an
   incoming receipt contains several units or packages and the first recommended location exceeds
   its capacity, Odoo still routes all items to that same location instead of selecting another one
   with available space.

   *(Example: If a location can hold 10 units and 12 units arrive, all 12 are still assigned to that
   location.)*

Capacity by weight
------------------

On a storage category form (:menuselection:`Inventory app --> Configuration --> Storage
Categories`), set a maximum product weight in the :guilabel:`Max Weight` field. This limit applies
to each location assigned this storage category.

Capacity by product
-------------------

In the :guilabel:`Capacity by Product` tab, click :guilabel:`Add a Line` to input items, and enter
their capacities in the :guilabel:`Quantity` field.

.. example::
   Ensure only a maximum of five `Large Cabinets` and two `Corner Desk Right Sit` are stored at a
   single storage location, by specifying those amounts in the :guilabel:`Capacity by Product` tab
   of a storage category form.

   .. screenshot:: daily-operations-storage-category-capacity-by-product
      :menu: Inventory ‣ Configuration ‣ Storage Categories
      :shows: A storage category form with the "Capacity by Product" table filled in, limiting how many units of a product a location may hold.
      :data: Category "Pallet zone": 10 units of "Large Cabinet".
      :module: stock
      :notes: English UI, light theme, 1440px width.

.. _inventory/routes/set-capacity-package:

Capacity by package
-------------------

For companies using :doc:`packages <../../product_management/configure/package>`, it becomes
possible to ensure real-time storage capacity checks, based on package types (e.g., crates, bins,
boxes, etc.).

Create the :ref:`package type <inventory/warehouses_storage/package-type>` before assigning it to a
storage category. Create it on the :guilabel:`Inventory` tab of the product form (in the
:guilabel:`Packaging` section), or create it from the :guilabel:`Product Packagings` page. Be sure
to set the :guilabel:`Package Type`.

.. example::
   Create putaway rules for pallet-stored items, by creating the `High frequency pallets` storage
   category.

   In the :guilabel:`Capacity by Package` tab, specify the number of packages for the designated
   :guilabel:`Package Type`, and set a maximum of `2.00` `Pallets` for a specific location.

   .. screenshot:: daily-operations-storage-category
      :menu: Inventory ‣ Configuration ‣ Storage Categories
      :shows: A new storage category form with the "Capacity by Package" table and the "Allow New Product" option.
      :highlight: The "Allow New Product" field (red frame).
      :module: stock
      :notes: English UI, light theme, 1440px width.

.. important::
   Odoo does **not** automatically split quantities across multiple storage locations. If an
   incoming receipt contains several units or packages and the first recommended location exceeds
   its capacity, Odoo still routes all items to that same location instead of selecting another one
   with available space.

   *(Example: If a location can hold 10 units and 12 units arrive, all 12 are still assigned to that
   location.)*

.. _inventory/routes/assign-location:

Assign to location
==================

Once the storage category is created, assign it to a location. Navigate to the location by going to
:menuselection:`Inventory app --> Configuration --> Locations`, and select the desired location.
Then, select the created category in the :guilabel:`Storage Category` field.

.. example::
   Assign the `High frequency pallets` storage category (which limits pallets stored at any location
   to two pallets) to the `WH/Stock/Pallets/PAL1` sub-location.

   .. screenshot:: daily-operations-storage-category-location
      :menu: Inventory app ‣ Configuration ‣ Locations
      :shows: A location form with the "Storage Category" field set to a storage category.
      :highlight: The "Storage Category" field (red frame).
      :module: stock
      :notes: English UI, light theme, 1440px width.

.. _inventory/routes/set-putaway-attribute:

Putaway rule
============

With the :ref:`storage category <inventory/routes/define-storage>` and :ref:`location
<inventory/routes/assign-location>` set up, create the :doc:`putaway rule <putaway>` by navigating
to :menuselection:`Inventory app --> Configuration --> Putaway Rules`.

Click the :guilabel:`New` button to create the putaway rule. Specify a location to store to in the
:guilabel:`Store to` field.

Use the :guilabel:`Sublocation` field to specify that you want to use a sublocation with the storage
category:

- :guilabel:`Last Used`: The last location that had a move associated with it for that product or
  product category is used. If there is no last location used, the destination is whatever is
  specified in the :guilabel:`Store to` field.
- :guilabel:`Closest Location`: The locations specified as part of the storage category are used. A
  storage category is mandatory in the :guilabel:`Having Category` field.

If using multiple storage locations for a single storage category, create putaway rules for each
location to ensure that if one storage location is in use, the secondary locations must be used.

.. example::
   Continuing the example from above, the `High frequency pallets` storage category is assigned to
   the putaway rule directing pallets of lemonade to locations with the `High frequency pallets`
   storage category :ref:`assigned to them <inventory/routes/assign-location>`.

   .. screenshot:: daily-operations-storage-category-smart-putaways
      :menu: Inventory app ‣ Configuration ‣ Putaway Rules
      :shows: The putaway rules list, with the "Having Category" column showing rules restricted to different storage categories.
      :module: stock
      :notes: English UI, light theme, 1440px width.

Use case: limit capacity by package
===================================

To limit the capacity of a storage location by a specific number of packages, :ref:`create a storage
category with a Capacity By Package <inventory/routes/set-capacity-package>`.

Continuing the example from above, the `High frequency pallets` storage category is assigned to the
`PAL1` and `PAL2` locations.

Then, :ref:`putaway rules <inventory/routes/putaway-rule>` are set, so that any pallets received in
the warehouse are directed to be stored in `PAL1` and `PAL2` locations.

Depending on the number of pallets on-hand at each of the storage locations, when two pallets of
lemonade cans is received, the following scenarios happen:

- If `PAL1` and `PAL2` are empty, the pallet is redirected to `WH/Stock/Pallets/PAL1`.
- If `PAL1` is full, the pallet is redirected to `WH/Stock/Pallets/PAL2`.
- If `PAL1` and `PAL2` are full, the pallet is redirected to `WH/Stock/Pallets`.
- If `PAL1` is partially full (for example, with one pallet), Odoo treats more than one received
  pallet as a single pallet on the receipt. You must manually separate the two pallets into separate
  storage locations. Click the :guilabel:`Open Move` icon to the right of the :guilabel:`Units`
  field, and then in the :guilabel:`Open: Stock move` box, click :guilabel:`Add a line`. Finally,
  split the receipt by quantity into separate locations, then click :guilabel:`Save`.

     .. screenshot:: daily-operations-storage-category-package-stock-move
        :menu: Inventory ‣ Receipts
        :shows: The detailed operations of a receipt, where pallets are routed to different destination locations by the storage-category putaway rule.
        :highlight: The "Destination Location" column (red frame).
        :module: stock
        :notes: English UI, light theme, 1440px width.

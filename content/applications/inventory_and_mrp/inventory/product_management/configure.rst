:show-content:

.. |UoM| replace:: :abbr:`UoM (Unit of Measure)`
.. |UoMs| replace:: :abbr:`UoMs (Units of Measure)`


=================
Configure product
=================

A group of products in Odoo can be further defined using:

- :doc:`Units of measure (UoM) <configure/uom>`: a standard quantity for specifying product amounts
  (e.g., meters, yards, kilograms). Enables automatic conversion between measurement systems in
  Odoo, such as centimeters to feet.

  - *Ex: Purchasing fabric measured in meters but receiving it in yards from a vendor.*

- :doc:`configure/package`: A physical container used to group products together, regardless of
  whether they are the same or different.

  - *Ex: A box containing assorted items for delivery, or a storage box of two hundred buttons on a
    shelf.*

- :doc:`configure/packaging`: groups the *same* products together to receive or sell them in
  specified quantities.

  - *Ex: Cans of soda sold in packs of six, twelve, or twenty-four.*

Comparison
==========

This table provides a detailed comparison of units of measure, packages, and packaging to help
businesses evaluate which best suits their requirements.

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Feature
     - Unit of measure
     - Packages
     - Packaging
   * - Purpose
     - Standardized measurement for product units (e.g., cm, lb, L)
     - Tracks the specific physical container and its contents
     - Groups a fixed number of items together for easier management (e.g., packs of 6, 12 or 24)
   * - Product uniformity
     - Defined per product; saved as one |UoM| in the database
     - Allows mixed products
     - Same products only
   * - Flexible
     - Converts between vendor/customer |UoMs| and database |UoM|
     - Items can be added or removed from the container
     - Quantities are fixed (e.g., always packs of 6, 12 or 24)
   * - Complexity
     - Simplest for unit conversions
     - More complex due to container-level inventory tracking
     - Simpler; suitable for uniform product groupings
   * - Inventory tracking
     - Tracks product quantities within the warehouse in the specific |UoM| defined in the product
       form
     - Tracks package location and contents within the warehouse
     - Tracks grouped quantities but not individual items' locations
   * - Barcode operations
     - Not available
     - Both the package and the individual items are scanned on reception (even if there are thirty
       items in the package). The :ref:`Move Entire Packages
       <inventory/product_management/move-entire-pack>` feature updates the locations of the items a
       package contains when the package itself is moved
     - A barcode can be stored on the packaging line, but scanning it does **not** record the
       contained units automatically
   * - Product lookup
     - Not available
     - The :ref:`Product Information <inventory/product_management/product-lookup>` screen of the
       eYssen *Barcode* app lists every internal location and package where the scanned product is
       stored, with the stored, reserved and available quantity per line
     - Not available: a packaging barcode identifies a grouped quantity, not a storage location
   * - Unique references
     - Not available
     - Every package has its own unique reference (e.g. `PACK0000012`), which doubles as its barcode
     - The barcode is set on the packaging line of one product (e.g. for a pack of six), so it is
       shared by every pack of that kind
   * - Reusability
     - Not applicable
     - Can be disposable or reusable, configured via the :ref:`Package Use
       <inventory/warehouses_storage/cluster-pack>` field
     - Disposable only
   * - Container weight
     - Not applicable
     - Weight of the container itself is included in the *Shipping Weight* field of a package
       (:menuselection:`Inventory app --> Products --> Packages`)
     - Weight of the container is defined in the *Package Type* settings
   * - Lot/serial number tracking
     - Requires manual adjustments to track |UoMs| via lots (See :ref:`use case
       <inventory/product_management/lots-uom>` for details)
     - Applies only to contained products
     - Applies to both contained products and the container
   * - Custom routes
     - Cannot be set
     - Cannot be set
     - Routes can define specific warehouse paths for a particular packaging type

Use cases
=========

After comparing the various features, consider how these businesses, with various inventory
management and logistics workflows, came to their decision.

Pallets of items using packaging
--------------------------------

A warehouse receives shipments of soap organized on physical pallets, each containing 96 bars. These
pallets are used for internal transfers and are also sold as standalone units. For logistical
purposes, the pallet's weight must be included in the total shipping weight for certain deliveries.
Additionally, the pallet requires a barcode to facilitate tracking, and the number of individual
bars of soap must be included in the stock count when the pallet is received.

After evaluating various options, *product packaging* was the most suitable solution. Packaging
enables assigning a barcode to a pallet, identifying it as a "pallet type" containing 96 soap bars.
This barcode streamlines operations by automatically registering the grouped quantity. Key
distinctions include:

- **Warehouse tracking limitations**: Odoo tracks only the total quantity, not the number of
  packagings. For instance, if a pallet with 12 and 24 quantities is received, Odoo records 36
  quantities, not the pallet details.
- **Packaging barcodes are type-specific, not unique**: Barcodes represent packaging types (e.g.,
  "pallet of 96 soap bars") but do not uniquely identify individual pallets, such as Pallet #1 or
  Pallet #2.

.. _inventory/product_management/product-lookup:

Look up where a product is stored
---------------------------------

A warehouse operator needs to know, from the shop floor, where a product is currently stored and how
much of it is available.

*Packages* was the most suitable. Because a package is a physical container whose contents are
tracked individually, the quantity of each product is recorded together with the location and the
package holding it.

In the eYssen *Barcode* app, the :guilabel:`Product Information` screen searches by barcode,
internal reference or product name, and lists every internal location where the product is stored,
the package on that location (if any), and the stored, reserved and available quantity for each
line. Product labels can also be printed straight from that screen.

.. seealso::
   :doc:`../../barcode`

.. _inventory/product_management/lots-uom:

Track different units of measure in storage
-------------------------------------------

A fruit juice distributor tracks multiple |UoMs| for their operations:

- Fruits are purchased in tons.
- Juice is produced and stored in kilograms.
- Small samples are stored in grams for recipe testing.

*Unit of Measure* was most suitable. Odoo automatically converts tons to kilograms during
receipts. However, since Odoo tracks only one |UoM| per product in the database, the company uses
lot numbers to differentiate |UoMs|:

- LOT1: Grams (g)
- LOT2: Kilograms (kg)

Manual inventory adjustments are required to convert between lots, such as subtracting 1 kg from
LOT2 to add 1,000 g to LOT1. While functional, this workaround can be time-consuming and prone to
errors.

.. toctree::
   :titlesonly:

   configure/type
   configure/uom
   configure/package
   configure/packaging


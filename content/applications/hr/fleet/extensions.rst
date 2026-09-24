=================================
Vehicle data, vignettes and parts
=================================

Three eYssen modules extend the **Fleet** application with the vehicle data a workshop actually
needs, with vignette tracking, and with a link between vehicles and the stock of spare parts.

.. _fleet/extra-vehicle-data:

Additional vehicle data
=======================

The *Fleet More Features* (`fleet_extra`) module adds the technical data that the standard vehicle
form does not carry. Open a vehicle in :menuselection:`Fleet app --> Fleet --> Fleet` and fill in:

- :guilabel:`Engine Number` and :guilabel:`Registration Certificate Number`, next to the chassis
  number.
- :guilabel:`Engine Displacement`, in the engine data.
- :guilabel:`Vehicle Dimensions`.
- :guilabel:`Tire Size (summer)` and :guilabel:`Tire Size (winter)`.
- :guilabel:`Service Interval (time)` and :guilabel:`Service Interval (distance)`: the intervals at
  which the vehicle is due for service.

.. note::
   The module also makes the :guilabel:`Driver` field of an odometer reading optional, so that a
   reading can be recorded without naming who was driving.

.. _fleet/vignettes:

Vignettes
=========

A :guilabel:`Vignettes` smart button at the top of the vehicle form lists the road-use vignettes
bought for that vehicle. Click it, then :guilabel:`New`, and fill in:

- :guilabel:`Vignette (Location)`: what the vignette is for, typically the country or the motorway
  section. This field is **required**.
- :guilabel:`Expiration Date`: the last day the vignette is valid. This field is **required**.
- :guilabel:`Attached Image`: a picture or scan of the vignette.

.. screenshot:: hr-fleet-vignettes
   :menu: Fleet ‣ Fleet ‣ Fleet ‣ (open a vehicle) ‣ Vignettes
   :shows: The vignette list of one vehicle, with the vignette location, the expiration date and the attached image column.
   :highlight: The Expiration Date column (red frame).
   :data: Vehicle "Skoda Octavia / ABC-123" with a Hungarian yearly and an Austrian ten-day vignette.
   :module: fleet_extra
   :notes: English UI, light theme, 1440px width.

.. _fleet/stock-location:

Stock location per vehicle
==========================

The *Fleet Stock Management* (`fleet_stock`) module gives every vehicle its own stock location, so
that the parts and tyres held for a vehicle are visible in the **Inventory** application.

Configure it in :menuselection:`Fleet app --> Configuration --> Settings`, in the
:guilabel:`Stock Management` block:

- :guilabel:`Stocking Method`: :guilabel:`Location` creates one internal stock location per
  vehicle.
- :guilabel:`Stocking Location`: the parent location the per-vehicle locations are created under.
  This field is **required**.

Once configured, the :guilabel:`Stock` tab of a vehicle shows its :guilabel:`Stock Location`. The
location is named after the licence plate and the model, and is renamed automatically when either
changes.

.. note::
   As long as the stocking location is not set, no per-vehicle location is created and the
   :guilabel:`Stock Location` of the existing vehicles is left as it is.

.. _fleet/parts:

Spare parts and tyres
=====================

The *Fleet Parts Management* (`fleet_parts`) module identifies which products are fleet parts and
which vehicle each individual part is currently fitted to.

.. note::
   This module requires the *Fleet Stock Management* and *Fleet More Features* modules, and the
   **Inventory** application with lot and serial number tracking.

Mark a product as a fleet part
------------------------------

Open a storable product in :menuselection:`Inventory app --> Products --> Products` and tick
:guilabel:`Fleet Parts`. Then select the :guilabel:`Fleet Parts Type`:

- :guilabel:`Tire`: a :guilabel:`Season` (:guilabel:`Summer`, :guilabel:`Summer (M+S)`,
  :guilabel:`Winter`, :guilabel:`Winter (M+S)`, :guilabel:`Winter (Studded)`,
  :guilabel:`All-Season`, :guilabel:`Space-saver Spare Wheel` or :guilabel:`Other`) and a
  :guilabel:`Wheel Size` can be entered.
- :guilabel:`Rim`: a :guilabel:`Material` (:guilabel:`Steel`, :guilabel:`Aluminium` or
  :guilabel:`Other`), a :guilabel:`Wheel Size`, a :guilabel:`Bolt Pattern`, a
  :guilabel:`Wheel Hub Diameter` and a :guilabel:`TPMS Sensor` indication.
- :guilabel:`Other`: any other part.

.. screenshot:: hr-fleet-parts-product
   :menu: Inventory ‣ Products ‣ Products ‣ (open a product)
   :shows: A product form with the Fleet Parts checkbox ticked, the Fleet Parts Type set to Tire and the tyre season and wheel size fields filled in.
   :highlight: The Fleet Parts checkbox and the Fleet Parts Type selector (red frame).
   :data: Product "205/55 R16 winter tyre", type Tire, season Winter, wheel size 16".
   :module: fleet_parts
   :notes: English UI, light theme, 1440px width.

Assign a part to a vehicle
--------------------------

Each physical part is a lot or serial number. Open it in :menuselection:`Inventory app --> Products
--> Lots/Serial Numbers` and set the :guilabel:`Vehicle` it is fitted to. For tyres, record the
:guilabel:`DOT` code and the :guilabel:`Quality` as well.

The :guilabel:`All Parts` group in the :guilabel:`Stock` tab of a vehicle then lists every part
assigned to it, with its location, lot number, product, quantity, DOT code, quality and part type.

.. screenshot:: hr-fleet-parts-vehicle
   :menu: Fleet ‣ Fleet ‣ Fleet ‣ (open a vehicle) ‣ Stock
   :shows: The Stock tab of a vehicle with its stock location and the All Parts list showing four tyres with their DOT codes.
   :highlight: The All Parts list (red frame).
   :data: Vehicle "Skoda Octavia / ABC-123" with a set of four winter tyres assigned.
   :module: fleet_parts, fleet_stock
   :notes: English UI, light theme, 1440px width.

.. seealso::
   - :doc:`new_vehicle`
   - :doc:`service`

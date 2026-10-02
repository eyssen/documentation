=================
Measuring Devices
=================

The **Measuring Devices** sub-module extends Equipment Management with features specific to
measuring instruments such as coordinate measuring machines (CMMs), optical measurement systems, and
other precision devices. It adds calibration tracking, software and hardware information, sensor
management, and the :guilabel:`Etalon` category for your company's own reference standards (see
:ref:`equipment/etalons`). Measuring devices and etalons are named automatically after their serial
number and model (see :ref:`equipment/derived-name`).

.. screenshot:: services-equipment-measuring-list
   :menu: Equipment Management ‣ Measuring Devices ‣ Measuring Devices
   :shows: The Measuring Devices list without a name column: Manufacturer, Product Family, Model, Serial Number, Customer, Product, Calibration, Next Calibration Date, Software Serial Number, Assignees, Activities, Tags and State.
   :highlight: The Calibration column (red frame).
   :data: Four measuring devices with mixed calibration statuses (valid, expiring, expired).
   :module: equipment_measuring
   :notes: English UI, light theme, 1440px width, crop to the list.

Installation
============

Enable the Measuring Devices module from :menuselection:`Equipment Management --> Settings -->
Configuration`, by ticking :guilabel:`Measuring Devices` in the :guilabel:`Equipment Types` section,
or install *Equipment Management - Measuring Devices* from the :menuselection:`Apps` menu (remove
the :guilabel:`Apps` filter to find it). The module requires the *Repairs* app, which is installed
along with it: calibrations are recorded as :ref:`repair orders
<repairs/repair_orders/calibration>`.

Dedicated measuring views
=========================

Once installed, the **Measuring Devices** and **Etalons** menus appear in the Equipment Management
navigation:

- :menuselection:`Equipment Management --> Measuring Devices --> Measuring Devices`: shows only the
  equipment of the :guilabel:`Measuring Device` category. The list has no name column: each device
  is identified by its :guilabel:`Manufacturer`, :guilabel:`Product Family`, :guilabel:`Model`, and
  :guilabel:`Serial Number`, followed by the :guilabel:`Customer`, :guilabel:`Product`,
  :guilabel:`Calibration`, :guilabel:`Next Calibration Date`, :guilabel:`Software Serial Number`,
  :guilabel:`Assignees`, :guilabel:`Activities`, :guilabel:`Tags`, and :guilabel:`State` columns.
  :guilabel:`Internal ID`, :guilabel:`Software Version`, and :guilabel:`Sensors` are optional
  columns, hidden by default.
- :menuselection:`Equipment Management --> Measuring Devices --> Calibrations`: lists all the
  calibrations of all measuring devices.
- :menuselection:`Equipment Management --> Etalons`: your company's own reference standards (see
  :ref:`equipment/etalons`).

Creating an equipment from the Measuring Devices menu sets its :guilabel:`Category` to
:guilabel:`Measuring Device`, and its name is built automatically (see
:ref:`equipment/derived-name`). The :guilabel:`Measuring Device` and :guilabel:`Etalon` categories
are also available on the equipment models, in :menuselection:`Equipment Management --> Settings -->
Models` (see :ref:`equipment/models`): the :guilabel:`Model` field of a device only offers the
models of its category.

.. _equipment/derived-name:

Names of measuring devices and etalons
======================================

For the :guilabel:`Measuring Device` and :guilabel:`Etalon` categories, the name at the top of the
form cannot be typed: it is built from the :guilabel:`Serial Number`, the :guilabel:`Model`, the
:guilabel:`Manufacturer`, and the :guilabel:`Product Family`, and it is updated automatically when
one of them changes, also when a model, a manufacturer, or a product family is renamed.

The name is built as follows, for example with the manufacturer *Zeiss*, the product family *CMM*,
the model *Contura*, and the serial number *CT-2019-0043*:

- with a serial number and a model: *<Serial Number> - <Model>*, e.g., ``CT-2019-0043 - Contura``;
- with a serial number but no model: *<Serial Number> - <Manufacturer> <Product Family>*, e.g.,
  ``CT-2019-0043 - Zeiss CMM``, or the serial number alone if these are empty as well;
- without a serial number: *<Manufacturer> <Model>*, e.g., ``Zeiss Contura``, or, without a model
  either, *<Manufacturer> <Product Family>*, e.g., ``Zeiss CMM``;
- with none of these: the :guilabel:`Equipment ID`, e.g., ``EQ/0042``.

A name supplied in another way, for example in an import file, is replaced by the built name as
well.

The equipment of the other categories, such as :guilabel:`General` or :guilabel:`Printer`, keeps a
typed name. When an equipment is switched to :guilabel:`Measuring Device` or :guilabel:`Etalon`, its
name is replaced by the built one; when it is switched back to another category, it keeps its last
name, which can then be edited again.

As the name repeats the serial number and the model, the Measuring Devices and Etalons lists have no
name column.

Measuring tab
=============

.. screenshot:: services-equipment-measuring-tab
   :menu: Equipment Management ‣ Measuring Devices ‣ (open a device) ‣ Measuring
   :shows: The Measuring tab of an equipment with the calibration section, the software and hardware information, and the technical description.
   :highlight: The Calibration section (red frame).
   :data: Measuring device "CT-2019-0043 - Contura" (manufacturer "Zeiss", model "Contura", serial number "CT-2019-0043") with a valid calibration.
   :module: equipment_measuring
   :notes: English UI, light theme, 1440px width, crop to the tab.

When the :guilabel:`Category` of an equipment is :guilabel:`Measuring Device`, a dedicated
:guilabel:`Measuring` tab appears on the form (etalons do not have it), with the following sections:

Calibration
-----------

- :guilabel:`Last Calibration Date`: the calibration date of the most recent **finished**
  calibration of the equipment (repair order in the :guilabel:`Repaired` status). Cannot be edited
  directly.
- :guilabel:`Last Calibration Date (Manual)`: only displayed as long as the equipment has no
  calibration. Enter here the date of the last calibration performed before the equipment was
  recorded in the database; it is used as last calibration date until a first calibration is
  finished.
- :guilabel:`Next Calibration Date`: computed as the last calibration date plus the calibration
  period. Read-only, and empty as long as one of the two is missing.
- :guilabel:`Calibration Period (months)`: how often the equipment must be calibrated. Set manually.
- :guilabel:`Calibration Status`: a badge computed from the next calibration date every time the
  equipment is displayed:

  - :guilabel:`OK` (green): the next calibration is more than 30 days away.
  - :guilabel:`Warning` (yellow): the next calibration is within 30 days.
  - :guilabel:`Overdue` (red): the calibration date has passed, or there is no next calibration
    date.

  Only measuring devices have a calibration status: it stays empty for every other category, etalons
  included.

Software
--------

- :guilabel:`Software Modules`: free-text description of the installed software modules.
- :guilabel:`Software Serial Number`: the license serial number.
- :guilabel:`Software Version`: the current software version.

Hardware
--------

- :guilabel:`Hardware Keylock`: the hardware keylock number (dongle/license key).

Characteristics
---------------

A rich text field for technical specifications, measurement ranges, accuracy specifications, and
other characteristics of the measuring device.

Sensors
-------

.. screenshot:: services-equipment-measuring-sensors
   :menu: Equipment Management ‣ Measuring Devices ‣ (open a device) ‣ Measuring
   :shows: The Sensors inline list of the Measuring tab with three sensor lines showing name and serial number.
   :highlight: None.
   :data: Sensors "Touch Probe SP25M", "Optical Sensor", "Chromatic Focus Point".
   :module: equipment_measuring
   :notes: English UI, light theme, 1440px width, crop to the sensor list.

An inline editable list of sensors attached to the measuring device:

- :guilabel:`Name`: sensor name (e.g., "Optical Sensor", "Touch Probe SP25M").
- :guilabel:`Serial Number`: the sensor's serial number for tracking and warranty purposes.
- :guilabel:`Type`: sensor type (free text, e.g., "Optical", "Tactile", "Chromatic Focus Point");
  optional column, hidden by default.
- :guilabel:`Notes`: additional notes; optional column, hidden by default.

To show an optional column, click the :icon:`oi-settings-adjust` :guilabel:`(settings adjust)` icon
at the far-right of the column titles.

Click the :guilabel:`Sensors` stat button to view sensors in a dedicated list view, with the same
optional columns.

Calibration management
======================

.. screenshot:: services-equipment-calibration-list
   :menu: Equipment Management ‣ Measuring Devices ‣ Calibrations
   :shows: The list of calibrations with the reference of the repair order, the certificate number, the equipment, the calibration date, the quality, the result, the customer and the status.
   :highlight: The "Certificate Number" column (red frame).
   :data: Six calibrations across three measuring devices, one of them cancelled (greyed out).
   :module: equipment_measuring
   :notes: English UI, light theme, 1440px width, crop to the list.

A calibration is a **repair order** of the *Repairs* app on which the :guilabel:`Calibration`
checkbox is ticked. It therefore follows the usual repair workflow (parts, operations, invoicing),
and additionally carries the calibration data and a certificate number. The complete calibration
history of each measuring device is made of its calibration repair orders.

Creating a calibration
----------------------

.. screenshot:: services-equipment-calibration-form
   :menu: Equipment Management ‣ Measuring Devices ‣ (open a device) ‣ Create Calibration
   :shows: A repair order form with the Calibration checkbox ticked and the Calibration group: equipment, calibration date, quality and result badges, performed by, certificate number, certificate file, signature fields, work performed and notes.
   :highlight: The "Calibration" group (red frame).
   :data: Measuring device "CT-2019-0043 - Contura"; quality "Accredited"; result "Pass"; certificate number "4382".
   :module: equipment_measuring
   :notes: English UI, light theme, 1440px width, crop to the form sheet.

#. Open the measuring device, and click :guilabel:`Create Calibration` in the header. The button is
   available on :guilabel:`Active` and :guilabel:`Inactive` equipment. A new repair order opens,
   with :guilabel:`Calibration` ticked, and the equipment, its product, and its customer filled in.

   Alternatively, click :guilabel:`New` in :menuselection:`Equipment Management --> Measuring
   Devices --> Calibrations`, or tick :guilabel:`Calibration` on any repair order, and select the
   :guilabel:`Equipment` (only measuring devices can be selected, not etalons; type the device's
   name, serial number, internal ID, or equipment ID to find it).

#. Fill in the :guilabel:`Calibration` group:

   - :guilabel:`Calibration Date`: the date the calibration is performed (defaults to today);
   - :guilabel:`Calibration Quality`: :guilabel:`Accredited` or :guilabel:`Werks` (required);
   - :guilabel:`Result`: :guilabel:`Pass`, :guilabel:`Fail`, :guilabel:`Conditional Pass`, or
     :guilabel:`Conditional Fail`;
   - :guilabel:`Performed By`: the person or organization performing the calibration;
   - :guilabel:`Certificate`: the calibration certificate file (PDF, etc.);
   - :guilabel:`Signed By`, :guilabel:`Customer Signature`, and :guilabel:`Sign Date`: the
     acknowledgment of the customer;
   - :guilabel:`Work Performed` and :guilabel:`Calibration Notes`.

#. Click :guilabel:`Confirm Repair`, and then :guilabel:`Start Repair`. At that moment, the
   :guilabel:`Certificate Number` is issued from the *Calibration Certificate* sequence, so that it
   can be printed on the worksheet before the calibration is finished.
#. Click :guilabel:`Print Worksheet` to print the *Calibration Worksheet*.
#. When the calibration is finished, click :guilabel:`End Repair`. The equipment's :guilabel:`Last
   Calibration Date`, :guilabel:`Next Calibration Date`, and :guilabel:`Calibration Status` are
   updated.

See :ref:`repairs/repair_orders/calibration` for the details of the calibration fields on the repair
order.

.. important::
   The certificate number is a regulatory, gap-less numbering:

   - it is issued automatically, and can neither be entered nor modified manually;
   - a calibration with a certificate number cannot be deleted, reset to draft, or turned back into
     a regular repair. It can only be cancelled; cancelled calibrations keep their number and can be
     found with the :guilabel:`Voided Certificate` filter of the repair orders.

.. tip::
   The starting number of the certificates can be adapted in :ref:`developer mode <developer-mode>`
   on the *Calibration Certificate* sequence (:menuselection:`Settings --> Technical --> Sequences &
   Identifiers --> Sequences`) **before** the first certificate is issued.

Search and filtering
--------------------

In the repair order search, calibrations can be found by :guilabel:`Calibration Quality`,
:guilabel:`Certificate Number`, and :guilabel:`Equipment`, filtered with :guilabel:`Accredited`,
:guilabel:`Werks`, and :guilabel:`Voided Certificate`, and grouped by :guilabel:`Calibration
Quality`.

Searching by :guilabel:`Equipment` also finds a device by its serial number, internal ID, or
equipment ID.

Stat buttons
============

Measuring devices show additional stat buttons (etalons do not):

- :guilabel:`Calibrations`: the number of calibration repair orders of the equipment. Click to open
  the calibrations of the device in the calibration list, with the same columns as
  :menuselection:`Equipment Management --> Measuring Devices --> Calibrations`; :guilabel:`New`
  there creates a calibration for this device.
- :guilabel:`Sensors`: the number of attached sensors. Only visible when sensors exist.

Dedicated search filters
========================

The equipment and measuring devices list views include specific search capabilities:

- :guilabel:`Calibration Due` filter: measuring devices whose next calibration is within 30 days.
- :guilabel:`Calibration Overdue` filter: measuring devices past their calibration date. Devices
  without a next calibration date are not included, although their status is :guilabel:`Overdue`.
- :guilabel:`Product Family` grouping.
- :guilabel:`Software Serial Number` search field, in the Measuring Devices list.

.. note::
   There is no automatic reminder when a calibration becomes due: use the :guilabel:`Calibration
   Due` and :guilabel:`Calibration Overdue` filters, e.g., saved as a favorite, or schedule an
   activity on the equipment.

.. _equipment/etalons:

Etalons
=======

The Measuring Devices sub-module also adds the :guilabel:`Etalon` category, for your company's own
reference standards, such as gauge block sets or setting rings. The category also exists on the
equipment models (see :ref:`equipment/models`).

.. screenshot:: services-equipment-etalon-list
   :menu: Equipment Management ‣ Etalons
   :shows: The Etalons list without a name column, showing the Manufacturer, Product Family, Model, Serial Number, Internal ID, Owner, Assignees, Activities and State columns.
   :highlight: The Owner column (red frame).
   :data: Demo company "YourCompany HU"; three etalons owned by the company (e.g., a gauge block set and a setting ring), one of them Scrapped.
   :module: equipment_measuring
   :notes: English UI, light theme, 1440px width, crop to the list.

:menuselection:`Equipment Management --> Etalons` lists the etalons only; they also appear in
:menuselection:`Equipment Management --> All Equipment`. As for measuring devices, the list has no
name column: the etalons are identified by the :guilabel:`Manufacturer`, :guilabel:`Product Family`,
:guilabel:`Model`, and :guilabel:`Serial Number` columns, followed by :guilabel:`Internal ID`,
:guilabel:`Owner`, :guilabel:`Assignees`, :guilabel:`Activities`, and :guilabel:`State`. The
:guilabel:`Customer` and :guilabel:`Tags` columns are optional, hidden by default.

The etalons can be searched by :guilabel:`Name`, :guilabel:`Equipment ID`, :guilabel:`Serial
Number`, :guilabel:`Internal ID`, :guilabel:`Owner`, :guilabel:`Customer`, :guilabel:`Manufacturer`,
:guilabel:`Model`, :guilabel:`Product Family`, and :guilabel:`Tags`, filtered by state
(:guilabel:`Draft`, :guilabel:`Active`, :guilabel:`Inactive`, :guilabel:`Scrapped`) or with
:guilabel:`Archived`, and grouped by :guilabel:`State`, :guilabel:`Owner`, :guilabel:`Brand`,
:guilabel:`Model`, :guilabel:`Product Family`, or :guilabel:`Tag`.

An equipment created with :guilabel:`New` in this menu gets the :guilabel:`Etalon` category. For
etalons:

- :guilabel:`Customer` and :guilabel:`Owner` default to your company, also when :guilabel:`Etalon`
  is selected on a new equipment created from another menu, and when an import gives no customer or
  owner for an etalon. Both fields can be changed. If a new equipment is switched from
  :guilabel:`Etalon` to another category before it is saved, your company is removed from both
  fields again; a saved equipment keeps its customer and owner when its category changes.
- The name is built automatically and cannot be typed, as for measuring devices (see
  :ref:`equipment/derived-name`).
- The :guilabel:`Model` field only offers the models of the :guilabel:`Etalon` category.
- There are no calibration features: no :guilabel:`Measuring` tab, no :guilabel:`Create Calibration`
  button, no :guilabel:`Calibrations` or :guilabel:`Sensors` stat button, and no calibration status.
  An etalon cannot be selected on a calibration repair order.

.. tip::
   To keep track of the certificates of an etalon, attach them in its :guilabel:`Documents` tab, for
   example with the :guilabel:`Calibration` type and an :guilabel:`Expiry Date`: for an active
   etalon, a warning activity is created when the expiry date approaches (see :doc:`documents`).

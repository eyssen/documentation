=================
Measuring Devices
=================

The **Measuring Devices** sub-module (``equipment_measuring``) extends Equipment Management with
features specific to measuring instruments such as coordinate measuring machines (CMMs), optical
measurement systems, and other precision devices. It adds calibration tracking, software and
hardware information, and sensor management.

.. screenshot:: services-equipment-measuring-list
   :menu: Equipment Management ‣ Measuring Devices ‣ Measuring Devices
   :shows: The list of measuring devices with their serial numbers, customers and calibration status column.
   :highlight: The Calibration Status column (red frame).
   :data: Four measuring devices with mixed calibration statuses (valid, expiring, expired).
   :module: equipment_measuring
   :notes: English UI, light theme, 1440px width, crop to the list.

Installation
============

Enable the Measuring Devices module from :menuselection:`Equipment Management --> Settings -->
Configuration`, by ticking :guilabel:`Measuring Devices` in the equipment types section, or install
``equipment_measuring`` from the Apps menu. The module requires the *Repairs* app, which is
installed along with it: calibrations are recorded as :ref:`repair orders
<repairs/repair_orders/calibration>`.

Dedicated measuring views
=========================

Once installed, a **Measuring Devices** menu appears in the Equipment Management navigation:

- :menuselection:`Equipment Management --> Measuring Devices --> Measuring Devices`: shows only
  measuring-type equipment with specific columns (calibration status, next calibration date,
  product family, serial number).
- :menuselection:`Equipment Management --> Measuring Devices --> Calibrations`: lists all the
  calibrations of all measuring devices.

Creating an equipment from the Measuring Devices menu automatically sets the type to
*Measuring Device*. The *Measuring Device* type is also available on the equipment models
(:menuselection:`Equipment Management --> Settings --> Models`).

Measuring tab
=============

.. screenshot:: services-equipment-measuring-tab
   :menu: Equipment Management ‣ Measuring Devices ‣ (open a device) ‣ Measuring
   :shows: The Measuring tab of an equipment with the calibration section, the software and hardware information, and the technical description.
   :highlight: The Calibration section (red frame).
   :data: Equipment "Zeiss Contura CMM" with a valid calibration.
   :module: equipment_measuring
   :notes: English UI, light theme, 1440px width, crop to the tab.

When an equipment has type *Measuring Device*, a dedicated :guilabel:`Measuring` tab appears on
the form with the following sections:

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
   :shows: The Sensors inline list of the Measuring tab with three sensor lines showing name, serial number and type.
   :highlight: None.
   :data: Sensors "Touch Probe SP25M", "Optical Sensor", "Chromatic Focus Point".
   :module: equipment_measuring
   :notes: English UI, light theme, 1440px width, crop to the sensor list.

An inline editable list of sensors attached to the measuring device:

- :guilabel:`Name`: sensor name (e.g., "Optical Sensor", "Touch Probe SP25M").
- :guilabel:`Serial Number`: the sensor's serial number for tracking and warranty purposes.
- :guilabel:`Type`: sensor type (free text, e.g., "Optical", "Tactile", "Chromatic Focus Point").
- :guilabel:`Notes`: additional notes (optional column).

Click the :guilabel:`Sensors` stat button to view sensors in a dedicated list view.

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
   :data: Equipment "Zeiss Contura CMM"; quality "Accredited"; result "Pass"; certificate number "4382".
   :module: equipment_measuring
   :notes: English UI, light theme, 1440px width, crop to the form sheet.

#. Open the measuring device, and click :guilabel:`Create Calibration` in the header. The button is
   available on :guilabel:`Active` and :guilabel:`Inactive` equipment. A new repair order opens,
   with :guilabel:`Calibration` ticked, and the equipment, its product, and its customer filled in.

   Alternatively, click :guilabel:`New` in :menuselection:`Equipment Management --> Measuring
   Devices --> Calibrations`, or tick :guilabel:`Calibration` on any repair order, and select the
   :guilabel:`Equipment` (only measuring devices can be selected).

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

Stat buttons
============

Measuring-type equipment shows additional stat buttons:

- :guilabel:`Calibrations`: the number of calibration repair orders of the equipment. Click to view
  the full calibration history.
- :guilabel:`Sensors`: the number of attached sensors. Only visible when sensors exist.

Dedicated search filters
========================

The equipment and measuring devices list views include specific search capabilities:

- :guilabel:`Calibration Due` filter: measuring devices whose next calibration is within 30 days.
- :guilabel:`Calibration Overdue` filter: measuring devices past their calibration date.
- :guilabel:`Product Family` grouping.
- :guilabel:`Calibration Status` grouping (:guilabel:`OK`, :guilabel:`Warning`,
  :guilabel:`Overdue`).

.. note::
   There is no automatic reminder when a calibration becomes due: use the :guilabel:`Calibration
   Due` and :guilabel:`Calibration Overdue` filters, e.g., saved as a favorite, or schedule an
   activity on the equipment.

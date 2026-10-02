========
Settings
========

Equipment settings are accessible from :menuselection:`Equipment Management --> Settings -->
Configuration` or from :menuselection:`Settings --> Equipment`.

.. screenshot:: services-equipment-settings
   :menu: Equipment Management ‣ Settings ‣ Configuration
   :shows: The Equipment settings page with the Equipment Types blocks (Printers, Measuring Devices) and the other configuration options.
   :highlight: The Equipment Types block (red frame).
   :data: Both equipment type sub-modules enabled.
   :module: equipment, equipment_printer, equipment_measuring
   :notes: English UI, light theme, 1440px width, crop to the settings blocks.

Equipment Types
===============

Enable or disable equipment type sub-modules:

- **Printers**: Adds the :guilabel:`Printer` category, with counter tracking, cartridge management,
  and paper format support. See :doc:`equipment_printer`.
- **Measuring Devices**: Adds the :guilabel:`Measuring Device` category, with calibration tracking,
  sensor management, and software and hardware information. It also adds the :guilabel:`Etalon`
  category, with its own :guilabel:`Etalons` menu, for your company's own reference standards. See
  :doc:`equipment_measuring`.

.. note::
   Enabling a sub-module will install the corresponding Odoo module.

.. warning::
   Disabling a sub-module uninstalls the module: the data it adds, such as printer counters,
   calibration data, or sensors, is deleted, and its equipment and models (printers, or measuring
   devices and etalons) get the :guilabel:`General` category.

Automation
==========

Auto-create Analytic Account
----------------------------

When enabled, activating an equipment (changing state from *Draft* to *Active*) automatically
creates a dedicated analytic account for that equipment.

- **Analytic Plan**: Select which analytic plan the auto-created accounts should belong to. The
  default is the *Equipment* plan created during module installation.

This is useful for tracking revenue and costs per equipment without manual setup.

Auto-create Maintenance Equipment
---------------------------------

When enabled, activating an equipment also creates a corresponding ``maintenance.equipment`` record
automatically. If a maintenance equipment with the same serial number already exists, it will be
linked instead of creating a duplicate.

The :guilabel:`Create Maintenance Equipment` button on the form remains available as a manual
alternative when this setting is disabled.

Document Expiry Warning
-----------------------

Configure how many days before a document's expiry date the system should create a warning
activity. The default is **30 days**.

The daily scheduled job checks all active equipment's documents and creates activities for those
within the warning period.

Defaults
========

Default Project
---------------

Set a default project that is automatically assigned to new equipment records. This is useful when
all equipment should be linked to the same ticket/project management system.

Equipment ID Prefix
-------------------

Customize the prefix used for auto-generated Equipment IDs. The default is ``EQ/``, producing
IDs like ``EQ/0001``, ``EQ/0002``, etc.

Changing the prefix affects only newly created equipment — existing IDs are not modified.

.. tip::
   Each company can have its own sequence and prefix. In multi-company setups, configure the
   prefix separately for each company.

.. _equipment/models:

Manufacturers and models
========================

Manufacturers and their models are managed in :menuselection:`Equipment Management --> Settings
--> Manufacturers` and :menuselection:`Equipment Management --> Settings --> Models`. Each model has
a :guilabel:`Manufacturer` (required), a :guilabel:`Category`, and optionally a :guilabel:`Product`,
which is then shown on the equipment of this model.

The :guilabel:`Model` field of an equipment only offers the models of the equipment's category, and
of its manufacturer if one is set. A missing model can also be created directly from that field:
select :guilabel:`Create` or :guilabel:`Create and edit...` in its drop-down menu. The new model
gets the equipment's category and manufacturer.

The :guilabel:`Models` list shows the :guilabel:`Manufacturer`, :guilabel:`Name`,
:guilabel:`Category`, and :guilabel:`Product` columns. It can be searched by :guilabel:`Name`,
:guilabel:`Manufacturer`, and :guilabel:`Product`, filtered with :guilabel:`Archived`, and grouped
by :guilabel:`Category`, :guilabel:`Brand`, or :guilabel:`Product`.

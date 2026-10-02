===============
Getting Started
===============

Installation
============

Navigate to :menuselection:`Apps` and search for **Equipment Management**. Click
:guilabel:`Activate`.

The module installs as a standalone application with its own top-level menu item in the main
navigation bar.

.. tip::
   Sub-modules for specific equipment types (Printers, Measuring Devices) can be enabled in
   :menuselection:`Equipment Management --> Settings --> Configuration` or installed separately
   from the Apps menu.

   The Measuring Devices sub-module also adds the :guilabel:`Etalon` category, with its own
   :guilabel:`Etalons` menu, for your company's own reference standards (see
   :ref:`equipment/etalons`).

Creating your first equipment
=============================

#. Navigate to :menuselection:`Equipment Management --> All Equipment`.
#. Click :guilabel:`New`.
#. Select the :guilabel:`Category` first: it decides which models can be selected, and whether the
   name is typed or built automatically. The default is :guilabel:`General`; the Printers sub-module
   adds :guilabel:`Printer`, and the Measuring Devices sub-module adds :guilabel:`Measuring Device`
   and :guilabel:`Etalon`. When you start from :menuselection:`Equipment Management --> Measuring
   Devices --> Measuring Devices` or :menuselection:`Equipment Management --> Etalons` instead, the
   category is already set.
#. Fill in the required fields:

   - **Name**: A descriptive name for the equipment (e.g., "Warehouse forklift H25"). For measuring
     devices and etalons, the name cannot be typed: it is built automatically from the serial number
     and the model (see :ref:`equipment/derived-name`).
   - **Equipment ID**: Auto-generated from the configured sequence (e.g., ``EQ/0001``). You can
     override this value manually if needed.
   - **Customer**: The customer who owns or uses the equipment.
   - **Owner**: The legal owner of the equipment.

   For an etalon, the customer and the owner both default to your own company (see
   :ref:`equipment/etalons`).

#. Optionally fill in:

   - **Serial Number**: The manufacturer's serial number. If a matching :doc:`stock lot
     </applications/inventory_and_mrp/inventory/product_management/product_tracking/lots>` exists,
     it will be automatically suggested.
   - **Manufacturer** and **Model**: The :guilabel:`Model` field only offers the models of the
     selected category and, if one is selected, of the manufacturer. A missing model can be created
     directly from the :guilabel:`Model` field; it gets the equipment's category and manufacturer
     (see :ref:`equipment/models`).
   - **Product Family**: The product family this equipment belongs to.
   - **Production Year**: The year the equipment was manufactured.
   - **Warranty Expiration**: The date when the manufacturer's warranty expires.
   - **MAC Address**: For network-connected equipment.
   - **Sales Team**: The responsible sales team.

   For a measuring device or an etalon, fill in at least the :guilabel:`Serial Number` and the
   :guilabel:`Model`: its name is built from them.

#. Click the :guilabel:`Draft` status bar to change the state to :guilabel:`Active`.

.. screenshot:: services-equipment-new-form
   :menu: Equipment Management ‣ All Equipment ‣ New
   :shows: A newly filled equipment form with the name, serial number, category (Printer), customer, product family, production year and warranty expiration, with the status bar switched from Draft to Active.
   :highlight: The Draft/Active status bar (red frame).
   :data: Equipment "Canon iR-ADV C5535", serial "CN-2024-0187", customer "Deco Addict".
   :module: equipment, equipment_printer
   :notes: English UI, light theme, 1440px width, crop to the form sheet.

Equipment states
================

Each equipment record goes through four lifecycle states:

- **Draft**: Initial state when created. Equipment is being set up.
- **Active**: Equipment is in service. Activating an equipment can automatically create an analytic
  account and/or a maintenance equipment record (if configured in Settings).
- **Inactive**: Equipment is no longer in service but kept for historical reference.
- **Scrapped**: Equipment that has been scrapped. Scrapped equipment cannot be archived, so that its
  record remains accessible.

Equipment ID sequence
=====================

By default, new equipment records receive an auto-generated ID using the format ``EQ/0001``,
``EQ/0002``, etc. The prefix can be customized in
:menuselection:`Equipment Management --> Settings --> Configuration --> Defaults --> Equipment ID Prefix`.

The ID field remains editable — you can override the auto-generated value at any time, for example
to match an existing internal numbering system.

=================
Add new equipment
=================

.. _maintenance/equipment_management/add_new_equipment:

In Odoo, *equipment* refers to any item that is used in everyday operations, including the
manufacturing of products. This can mean a piece of machinery on a production line, a tool that is
used in different locations, or a computer in an office space. Equipment registered in Odoo can be
owned by the company that uses the Odoo database, or by a third party, such as a vendor in the case
of equipment rentals.

Using Odoo *Maintenance*, it is possible to track individual pieces of equipment, along with
information about their maintenance requirements. To add a new piece of equipment, navigate to
:menuselection:`Maintenance app --> Equipment`, click :guilabel:`New`, and configure the equipment
as follows:

- :guilabel:`Equipment Name`: the product name of the piece of equipment
- :guilabel:`Equipment Category`: the category that the equipment belongs to; for example,
  computers, machinery, tools, etc.; new categories can be created by navigating to
  :menuselection:`Configuration --> Equipment Categories` and clicking :guilabel:`New`
- :guilabel:`Company`: the company that owns the equipment; again, this can be the company that uses
  the Odoo database, or a third-party company
- :guilabel:`Owner`: the user considered responsible for the equipment; this field is set
  automatically once :guilabel:`Used By` is filled out below
- :guilabel:`Used By`: specify if the equipment is used by a specific :guilabel:`Employee`,
  :guilabel:`Department`, or :guilabel:`Other`; select :guilabel:`Other` to specify both an employee
  and a department
- :guilabel:`Maintenance Team`: the team responsible for servicing the equipment; new teams can be
  created by navigating to :menuselection:`Configuration --> Maintenance Teams` and
  selecting :guilabel:`New`; the members of each team can also be assigned from this page
- :guilabel:`Technician`: the person responsible for servicing the equipment; this can be used to
  assign a specific individual in the event that no maintenance team is assigned or when a specific
  member of the assigned team should always be responsible for the equipment; any internal user can
  be assigned as a technician
- :guilabel:`Used in location`: the location where the equipment is used; this is a simple text
  field, useful for equipment that is not tied to a specific piece of machinery, like a laptop or an
  office

.. screenshot:: maintenance-add-equipment-form
   :menu: Maintenance ‣ Equipment ‣ (equipment)
   :shows: The top part of an equipment form filled out with an "Equipment Name", "Equipment
     Category", "Company", "Owner", "Used By" set to "Employee" with an "Employee" field shown,
     "Maintenance Team", "Technician", and "Used in location".
   :highlight: The "Used By" radio buttons and the "Employee" field that appears below them (red
     frame).
   :data: Demo company "YourCompany"; equipment "Full-size vans" in category "Vans", used by
     employee "Mitchell Admin".
   :module: maintenance, hr_maintenance
   :notes: English UI, light theme, 1440px width.

.. tip::
   Custom fields can be added to an equipment category via the :guilabel:`Properties` widget at the
   top of the equipment form. Properties are defined per category, from the category form, and only
   appear on equipment that belongs to that category.

If a serial number is entered on the equipment (see below) that matches an existing lot or serial
number in the *Inventory* app, a smart button showing that serial number appears at the top of the
equipment form. Clicking it opens the corresponding lot/serial number record.

Include additional product information
--------------------------------------

The :guilabel:`Product Information` tab at the bottom of the page can be used to provide further
details about the piece of equipment:

- :guilabel:`Vendor`: the vendor that the equipment was purchased from
- :guilabel:`Vendor Reference`: the reference code assigned to the vendor
- :guilabel:`Model`: the specific model of the piece of equipment
- :guilabel:`Serial Number`: the unique serial number of the equipment
- :guilabel:`Effective Date`: the date that the equipment became available for use; this is used to
  calculate the :abbr:`MTBF (Mean Time Between Failures)`
- :guilabel:`Cost`: the amount the equipment was purchased for
- :guilabel:`Warranty Expiration Date`: the date on which the equipment's warranty will expire

.. screenshot:: maintenance-add-equipment-product-info
   :menu: Maintenance ‣ Equipment ‣ (equipment) ‣ Product Information
   :shows: The "Product Information" tab with "Vendor", "Vendor Reference", "Model", "Serial
     Number", "Effective Date", "Cost", and "Warranty Expiration Date" fields filled out.
   :module: maintenance
   :notes: English UI, light theme, 1440px width, crop to the tab.

Add maintenance details
-----------------------

The :guilabel:`Maintenance` tab at the bottom of the page provides information about the failure
frequency of the piece of equipment:

- :guilabel:`Expected Mean Time Between Failure`: the average number of days the equipment is
  expected to operate between failures. This number can be configured manually.
- :guilabel:`Mean Time Between Failure`: the average number of days the equipment operates between
  failures. This number is calculated automatically based on previous failures, and cannot
  be configured manually.
- :guilabel:`Estimated Next Failure`: the estimated date the equipment may experience its next
  failure.
  This date is calculated automatically based on the data in the :guilabel:`Mean Time Between
  Failure` and :guilabel:`Latest Failure` fields, and cannot be configured manually.
- :guilabel:`Latest Failure`: the most recent date on which the equipment failed. This date is based
  on the creation date of the equipment's most recent maintenance request, and cannot be configured
  manually.
- :guilabel:`Mean Time To Repair`: the average number of days needed to repair the equipment. This
  number is calculated automatically based on the duration of previous maintenance requests, and
  cannot be configured manually.

.. screenshot:: maintenance-add-equipment-metrics
   :menu: Maintenance ‣ Equipment ‣ (equipment) ‣ Maintenance
   :shows: The "Maintenance" tab of an equipment form, with the "Expected Mean Time Between
     Failure", "Mean Time Between Failure", "Estimated Next Failure", "Latest Failure", and "Mean
     Time To Repair" fields; only "Expected Mean Time Between Failure" is editable, the rest are
     greyed out.
   :module: maintenance
   :notes: English UI, light theme, 1440px width, crop to the tab.

.. tip::
   To see any open maintenance requests for a piece of equipment, go to the page for the equipment,
   and click the :guilabel:`Maintenance` smart button at the top of the page.

.. seealso::
   - :doc:`../../services/equipment`
     for the eYssen *Equipment Management* app (product-facing equipment, measuring devices and
     printers), which can be linked to a maintenance equipment record from this module: see
     :doc:`../../services/equipment/integrations`.

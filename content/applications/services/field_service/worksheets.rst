==========
Worksheets
==========

The **worksheet** is the report of an intervention: what was done, how long it took, and which
materials were used. It can be printed, signed by the customer from the portal, and used as the
basis of a quotation.

Configuration
=============

Worksheets are available on the tasks of every project whose :ref:`category
<field_service/category>` has the :guilabel:`Worksheet` option enabled. To have the time spent
appear on the worksheet, the project must also allow :doc:`timesheets <../timesheets>`.

.. _field_service/worksheet-content:

What the worksheet contains
===========================

The worksheet is generated from the task itself, so there is no separate form to fill in. It
consists of:

- the customer and, in the header, the task :guilabel:`Name`, the :guilabel:`Deadline`, and the
  :guilabel:`Allocated Hours`;
- the :guilabel:`Description` of the task;
- a :guilabel:`Services` table listing every timesheet entry (date, employee, description, time
  spent), followed by the total time spent;
- a :guilabel:`Products` table listing the materials recorded in the :ref:`Products tab
  <field_service/products-tab>` with their quantities.

Sections that have no data are left out: a task without timesheet entries produces a worksheet
without the :guilabel:`Services` table.

.. screenshot:: services-field-service-worksheet-pdf
   :menu: (PDF report) Project ‣ (field service project) ‣ (open a task) ‣ Print
   :shows: The printed Worksheet PDF of an intervention, showing the header information, the Services table with two timesheet lines and total time spent, and the Products table.
   :highlight: None.
   :data: Task "Annual boiler service"; two timesheet lines; two product lines.
   :module: eyssen_project_worksheet
   :notes: English UI, light theme, full page of the PDF, cropped to the page content.

.. _field_service/worksheet-print:

Printing and signing the worksheet
==================================

Two buttons are available in the header of the task:

- :guilabel:`Print` generates the **Worksheet** PDF. The report is rendered in the customer's
  language. It is also available from the :icon:`fa-cog` :guilabel:`Actions` menu of the task list,
  so several worksheets can be printed at once.
- :guilabel:`Sign Report` opens the task in the customer portal, where the customer can review the
  intervention and sign it off on the technician's device.

Customers who open the task in their portal see a :guilabel:`View Timesheet` button that downloads
the same worksheet as a PDF.

.. screenshot:: services-field-service-worksheet-buttons
   :menu: Project ‣ (field service project) ‣ (open a task)
   :shows: The header of a field service task with the Sign Report, Print and Create Quotation buttons, and the Quotations/Orders smart button in the button box.
   :highlight: The Sign Report and Print buttons (red frame).
   :data: Task "Annual boiler service" in stage "In Progress".
   :module: eyssen_project_worksheet, eyssen_project_product
   :notes: English UI, light theme, 1440px width, crop to the task header and button box.

.. _field_service/worksheet-quotation:

Creating a quotation from the intervention
==========================================

Click :guilabel:`Create Quotation` in the header of the task to turn the recorded work into a
quotation. The button is available to users with sales rights on tasks that have the
:guilabel:`Products` tab.

The quotation is created for the task's customer, with the task's :ref:`pricelist
<field_service/pricelist>`, and the task name as source document. Its lines are built as follows:

- a :guilabel:`Services` section containing the timesheet entries of the task, each with the time
  spent expressed in hours;
- if the task has no timesheet entries but has :guilabel:`Allocated Hours`, a single
  :guilabel:`Service Fee` line of that many hours instead;
- a :guilabel:`Products` section containing the lines of the :guilabel:`Products` tab.

The quotation opens directly for review. The number of quotations and orders linked to the task is
shown on the :guilabel:`Quotations/Orders` smart button, which opens them.

.. important::
   The service lines are created with a quantity and a unit of measure but **without a product**.
   Pick the service product on each line before confirming the quotation, so that the correct price
   and income account are applied.

.. seealso::
   - :doc:`product_management`
   - :doc:`../timesheets`

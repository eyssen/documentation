============================
Creating field service tasks
============================

An intervention is an ordinary :doc:`project task <../project/tasks/task_creation>` that belongs to
a project with a :ref:`field service category <field_service/category>`. It can be created manually
or automatically from a sales order.

Manual task creation
====================

#. Open the **Project** app and go to the field service project.
#. Click :guilabel:`New`, or use the list view of :menuselection:`Project --> My Tasks`.
#. Fill in the task title, the :guilabel:`Customer`, and the :guilabel:`Location`.
#. Add the planned date, the assignees, and the :guilabel:`Allocated Hours`, then save.

.. _field_service/location:

Intervention location
=====================

The :guilabel:`Location` field holds the address where the work is performed. It is **required** on
tasks of a field service project.

The selectable values are the customer chosen in the :guilabel:`Customer` field and that customer's
child contacts. This makes it possible to keep the invoicing partner in :guilabel:`Customer` and
still point the technician at the right site, shop, or building of that customer.

.. tip::
   Create the sites of a customer as child contacts of type :guilabel:`Address` on the customer
   form. They then become available in the :guilabel:`Location` field of every intervention for
   that customer.

.. screenshot:: services-field-service-task-location
   :menu: Project ‣ (field service project) ‣ (open a task)
   :shows: A field service task form; the Customer field holds a company and the Location field one of its child addresses.
   :highlight: The Location field (red frame).
   :data: Customer "Deco Addict" with child address "Deco Addict, Warehouse Budapest".
   :module: eyssen_project_fsm
   :notes: English UI, light theme, 1440px width, crop to the task header fields.

Task creation from a sales order
================================

When a quotation containing a :ref:`service product <sales/invoicing/configured-service-product>`
configured to create a task is confirmed, the task is created in the project set on the product.
Point that product at your field service project to have interventions created directly by the
sales team. Click the :guilabel:`Tasks` smart button on the sales order to open them.

.. seealso::
   - :doc:`../project/tasks/task_creation`
   - :doc:`worksheets`

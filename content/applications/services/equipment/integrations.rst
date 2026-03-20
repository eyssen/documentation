============
Integrations
============

Equipment Management integrates with several Odoo modules to provide a complete view of each
equipment's lifecycle.

Maintenance
===========

Each equipment can be linked to a **maintenance equipment** record from the Maintenance module.
This enables:

- Viewing maintenance requests directly on the equipment form.
- MTBF/MTTR statistics computed from maintenance history.
- Preventive maintenance scheduling through the Maintenance module.

**Linking maintenance equipment:**

#. Open the equipment form.
#. Go to the :guilabel:`Maintenance` tab.
#. Click :guilabel:`Create Maintenance Equipment`.
#. If a maintenance equipment with the same serial number already exists, it will be linked
   automatically instead of creating a duplicate.

When the maintenance equipment link is established, data is synced automatically:

- Serial number, customer, and assignees are kept in sync.
- Changes on the equipment form propagate to the maintenance record.

Analytic Accounting
===================

Each equipment can have a dedicated **analytic account** that tracks all financial transactions
related to that specific piece of equipment.

The analytic account is used to:

- Link customer invoices to the equipment (visible in the Finance tab).
- Link purchase orders to the equipment.
- Calculate revenue, cost, and margin per equipment.

When setting the analytic distribution on invoice lines or purchase order lines, select the
equipment's analytic account to associate the transaction with the equipment.

.. tip::
   Enable **Auto-create Analytic Account** in Settings to have analytic accounts created
   automatically when equipment is activated.

Stock / Inventory
=================

Equipment can be linked to a **stock lot** (serial number tracking in Inventory). When you enter
a serial number on the equipment form, the system automatically searches for a matching stock lot:

- **One match found**: The lot is auto-linked.
- **Multiple or no matches**: The lot field remains empty for manual selection.

This link allows you to trace the equipment's inventory history, warehouse location, and stock
movements.

Fleet
=====

For vehicle-type equipment (company cars, delivery trucks, forklifts), a **fleet vehicle** can be
linked. The Fleet tab shows:

- License plate, odometer, last service date, and contract state.
- Direct link to the fleet vehicle form for full details.

.. note::
   Fleet vehicles must be created manually in the Fleet module first, then linked from the
   equipment form. This is because fleet vehicles have many required fields that cannot be
   auto-populated.

Project / Tickets
=================

Equipment can be linked to one or more **projects** for ticket management. The :guilabel:`Create
Ticket` button on the form creates a project task linked to the equipment.

If the equipment has exactly one project, the task is created directly. If multiple projects are
linked, a wizard appears to select the target project.

Subscription
============

Equipment can be linked to a **subscription service** for recurring billing. When a subscription
is linked, the Subscription tab shows pricing details and the invoicing period.

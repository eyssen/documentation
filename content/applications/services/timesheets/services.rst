==================
Timesheet services
==================

**Timesheet services** classify the work logged on a timesheet line — for example *Consulting*,
*Development*, or *On-site support* — and decide two things about it: which product the work is
billed with, and at what rate the hours are charged against the customer's service credit.

.. note::
   This feature is provided by the *eYssen Invoice from Timesheet*
   (`eyssen_invoice_from_timesheet`) module.

.. _timesheets/services-config:

Configuring the services
========================

Go to :menuselection:`Project --> Configuration --> Timesheet Services`. Each service has:

- :guilabel:`Service Name` – the label chosen on the timesheet line.
- :guilabel:`Product` – the service product used to price the work. Only products of type
  *Service* can be selected.
- :guilabel:`Billing Rate (%)` – the percentage of the logged hours charged against the customer's
  credit. Use it to weight the work by seniority: for instance 70% for junior work, 100% for
  standard work, 150% for senior work.

.. screenshot:: services-timesheets-services-list
   :menu: Project ‣ Configuration ‣ Timesheet Services
   :shows: The Timesheet Services list in edit mode with three services, each with a service product and a billing rate.
   :highlight: The Billing Rate (%) column (red frame).
   :data: Services "Junior consulting" 70%, "Consulting" 100%, "Senior consulting" 150%.
   :module: eyssen_invoice_from_timesheet
   :notes: English UI, light theme, 1440px width, crop to the list.

.. _timesheets/services-project:

Billing a project from timesheet services
=========================================

Open the project's settings and enable :guilabel:`Billable from Timesheet Services` to invoice time
and material from the services instead of the standard billing setup. The option replaces the
standard :guilabel:`Billable` setting; only one of the two applies to a project.

A :guilabel:`Contains Services` tab then appears on the project, listing the service credit agreed
with the customer. Each line holds the :guilabel:`Timesheet Service`, the :guilabel:`Quantity` of
hours included, and the :guilabel:`Start Date` and :guilabel:`End Date` of the period in which they
can be consumed.

.. screenshot:: services-timesheets-contains-services
   :menu: Project ‣ Projects ‣ (open a project) ‣ Contains Services
   :shows: The Contains Services tab of a project with two credit lines, each with a service, a quantity of hours and a validity period.
   :highlight: The Contains Services tab (red frame).
   :data: Project "Support contract 2026"; lines "Consulting 100 h" and "Senior consulting 20 h" for 2026.
   :module: eyssen_invoice_from_timesheet
   :notes: English UI, light theme, 1440px width, crop to the tab.

.. _timesheets/services-logging:

Logging time on a service
=========================

The :guilabel:`Service` is **required** on every timesheet line, and is available both in the quick
entry form of :guilabel:`My Timesheets` and on the full timesheet line form. When the line is
saved, the database fills in, from the service and the customer's pricelist:

- :guilabel:`Billing Rate (%)` – copied from the service;
- :guilabel:`Billed Hours` – the logged hours multiplied by the billing rate;
- :guilabel:`Service Unit Price` – the price of the service product for the project's customer on
  the date of the line, taken from that customer's pricelist (or the product's sales price when the
  customer has none);
- :guilabel:`Service Amount` – the unit price multiplied by the logged hours.

The rate and the price are stored on the line, so later changes to the service or the pricelist do
not rewrite the history of the work already logged.

.. important::
   The price is looked up **when the line is saved**. Correct the service on the line before the
   period is invoiced, not afterwards.

Tasks show the resulting :guilabel:`Billed Time Spent` next to the hours actually spent, so the
difference between the time worked and the time charged stays visible.

.. seealso::
   - :doc:`../project/categories`
   - :doc:`/applications/sales/sales/invoicing/time_materials`

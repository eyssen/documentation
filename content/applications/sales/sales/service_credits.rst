===============
Service credits
===============

A **service credit** is a prepaid package of hours: the customer buys, say, 40 support hours in
advance, and the timesheets recorded on their projects draw the hours down from that balance instead
of being invoiced one by one.

The feature comes from the *Service Credit Management* module (``service_credit``).

Selling a credit package
========================

Flag the product that represents the package in :menuselection:`Sales app --> Products -->
Products`, on the :guilabel:`Sales` tab:

- :guilabel:`Creates Service Credit`: when this product is invoiced, a service credit is created
  automatically.
- :guilabel:`Credit Hours`: how many hours one unit of the product contains.
- :guilabel:`Warning Threshold (hours)`: the default remaining-hours level at which the projects
  start warning.

Sell the product on an ordinary quotation. When the customer invoice is posted, a service credit is
created in the :guilabel:`Draft` state for the number of hours (credit hours × invoiced quantity)
and linked to the invoice. When that invoice is **paid**, the credit becomes :guilabel:`Active` and
can be consumed.

.. screenshot:: sales-service-credits-product
   :menu: Sales ‣ Products ‣ Products ‣ (a product) ‣ Sales
   :shows: A service product's Sales tab with the "Creates Service Credit" checkbox ticked and the Credit Hours and Warning Threshold fields filled in.
   :highlight: The service-credit fields (red frame).
   :data: Product "Support package 40 h"; 40 credit hours, warning at 5 hours.
   :module: service_credit
   :notes: English UI, light theme, 1440px width, crop to the field group.

Managing credits
================

Credits are listed in :menuselection:`Project app --> Configuration --> Service Credits`. A credit
holds:

- :guilabel:`Customer` and :guilabel:`Name`.
- :guilabel:`Credit Hours`, :guilabel:`Hours Used` and :guilabel:`Hours Remaining`.
- :guilabel:`Projects`: the projects whose timesheets consume it.
- :guilabel:`Invoice`: the customer invoice the credit was sold on.
- :guilabel:`Start Date` and :guilabel:`End Date`: its validity.
- :guilabel:`Warning Threshold (hours)`.
- :guilabel:`Notes`.

The states are :guilabel:`Draft`, :guilabel:`Active`, :guilabel:`Depleted` (no hours left) and
:guilabel:`Closed`. The header buttons are :guilabel:`Activate` and :guilabel:`Close`; a credit can
also be activated by hand when it was not sold through an invoice.

:guilabel:`Print Detail` produces a statement of the credit with the consumption behind it.

.. screenshot:: sales-service-credits-form
   :menu: Project ‣ Configuration ‣ Service Credits ‣ (a credit)
   :shows: An active service credit with the customer, the credit hours, hours used and hours remaining, the linked projects and the source invoice.
   :highlight: The Hours Used and Hours Remaining fields (red frame).
   :data: Credit "INV/2026/0031 - Support package 40 h" for "Deco Addict"; 40 hours, 12 used, 28 remaining.
   :module: service_credit
   :notes: English UI, light theme, 1440px width, full form.

Consumption and warnings
========================

Every timesheet entry recorded on a project linked to a credit reduces the remaining hours. The
project itself shows :guilabel:`Total Credit Hours`, :guilabel:`Credit Hours Used` and
:guilabel:`Credit Hours Remaining`, plus a traffic-light :guilabel:`Credit Status`:

- green: enough hours left;
- yellow: the remaining hours have fallen under the warning threshold;
- red: the credit is depleted.

A warning message is shown on the project when the status is yellow or red, so the team notices
before working unpaid hours.

The customer contact also carries the totals: a :guilabel:`Service Credits` smart button, the
:guilabel:`Credit Hours Remaining` and the same traffic-light status. The :guilabel:`Has Service
Credits` filter on the contact list finds the customers who have any.

.. note::
   Consuming credits requires the timesheet-invoicing module the service credit builds on
   (``eyssen_invoice_from_timesheet``).

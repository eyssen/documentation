=============================
Invoicing from delivery notes
=============================

The *Invoicing from Stock Picking* (`eyssen_stock_picking_invoice`) module allows invoicing
validated delivery orders (and billing validated receipts) directly, and keeps track of the
invoiced quantities of each transfer.

.. note::
   The module requires the Hungarian localization and delivery note modules (e.g.,
   `eyssen_l10n_hu`, `eyssen_stock_deliveryslip`, `eyssen_stock_priced_delivery_note`). Some
   labels of this feature are currently displayed in Hungarian (e.g., :guilabel:`Számlázás`,
   meaning *Invoicing*).

.. _accounting/invoice-from-delivery/status:

Invoice status of transfers
===========================

Validated transfers have an :guilabel:`Invoice Status`, computed from the quantities of the
transfer and the quantities already invoiced:

- :guilabel:`Not invoiced`: nothing has been invoiced yet.
- :guilabel:`To Invoice`: the transfer is partially invoiced.
- :guilabel:`Fully Invoiced`: all the quantities are invoiced.
- :guilabel:`Over Invoiced`: more than the transferred quantities are invoiced.
- :guilabel:`No need to invoice`: the transfer must not be invoiced.

The :guilabel:`Invoice Status` is displayed on the transfer form and in the list of transfers. Use
the :guilabel:`To be Invoice` filter to list the transfers still to invoice, or group the transfers
by :guilabel:`Invoice State`. On the transfer form, the :guilabel:`Invoiced` column of the
operations shows the invoiced quantity of each product (green: fully invoiced, orange: not invoiced,
blue: partially invoiced, red: over invoiced).

To exclude a transfer from invoicing, open its :guilabel:`Additional Info` tab and, in the
:guilabel:`Számlázás` section, tick :guilabel:`No need to invoice` and enter the
:guilabel:`Reason`. Only users with the :guilabel:`Advisor` accounting access right can change this
option.

For receipts, the vendor's delivery note number can be recorded in the :guilabel:`Partner Delivery
Note Number` field.

.. screenshot:: accounting-invoice-from-delivery-picking
   :menu: Inventory ‣ Operations ‣ Deliveries ‣ (open a validated delivery order)
   :shows: Validated delivery order with the "Számlázás" button in the header, the "Invoice Status" field ("Not invoiced"), and the "Invoiced" column in the Operations tab.
   :highlight: The "Számlázás" button, the "Invoice Status" field and the "Invoiced" column (red frames).
   :data: Demo company "YourCompany HU"; delivery order WH/OUT/00012 of 10 units, validated.
   :module: eyssen_stock_picking_invoice
   :notes: English UI, light theme, 1440px width.

.. _accounting/invoice-from-delivery/from-transfer:

Invoicing from the transfers
============================

To create an invoice (or a vendor bill for receipts) from transfers:

- open a validated transfer and click :guilabel:`Számlázás`; or
- select several validated transfers in the list view, and click :menuselection:`Actions -->
  Számlázás`.

A draft invoice is created with the not yet invoiced quantities. The invoice date and delivery date
are set to the latest delivery date of the transfers (the validation date for deliveries, the
recorded delivery date for receipts), and each line keeps its own delivery date. The unit prices
come from the stock moves or, if not set, from the sales order lines.

The following conditions must be met to invoice several transfers together:

- the transfers belong to the same partner and use the same currency;
- the transfers are validated (:guilabel:`Done`);
- the delivery dates are in the same month;
- if the delivery dates are different, the partner must have an **aggregate invoice agreement**
  (:guilabel:`Aggregate Invoice Agreement`); the invoice is then marked as an aggregate invoice.

.. _accounting/invoice-from-delivery/from-invoice:

Adding delivery notes to an invoice
===================================

On a draft invoice or bill with a selected partner, click :guilabel:`Add Products from Delivery
Notes` above the invoice lines. In the :guilabel:`Selection of Delivery Notes` window, select the
validated transfers that are not yet fully invoiced, and click :guilabel:`Loading Items`. The not yet
invoiced quantities are added to the invoice lines. Quantities of transfers in the opposite
direction (e.g., a customer return on a customer invoice) are added with a negative sign.

The invoice lines display the related :guilabel:`Delivery Note` and an indicator showing whether the
line is fully delivered.

.. screenshot:: accounting-invoice-from-delivery-wizard
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (open a draft invoice) ‣ Add Products from Delivery Notes
   :shows: "Selection of Delivery Notes" dialog listing two validated delivery orders of the customer (Reference, Source and Destination Location, Contact, Source Document), with the "Loading Items" button.
   :highlight: The "Loading Items" button (red frame).
   :data: Demo customer with two validated, not invoiced delivery orders.
   :module: eyssen_stock_picking_invoice
   :notes: English UI, light theme, crop to the dialog.

.. seealso::
   :doc:`../customer_invoices`

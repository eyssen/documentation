=============
Cash rounding
=============

**Cash rounding** is required when the lowest physical denomination
of currency, or the smallest coin, is higher than the minimum unit
of account.

For example, some countries require their companies to round up or
down the total amount of an invoice to the nearest five cents, when
the payment is made in cash.

Configuration
=============

Go to :menuselection:`Accounting --> Configuration --> Settings`, enable :guilabel:`Cash Rounding`
in the :guilabel:`Customer Invoices` section, then click :guilabel:`Save`.

.. screenshot:: accounting-cash-rounding-setting
   :menu: Accounting ‣ Configuration ‣ Settings
   :shows: "Customer Invoices" section with the "Cash Rounding" setting enabled and its "Cash Roundings" link button.
   :highlight: The setting block (red frame).
   :data: Demo company "YourCompany HU".
   :module: account
   :notes: English UI, light theme, 1440px width. Crop to the setting.

Go to :menuselection:`Accounting --> Configuration --> Management --> Cash Roundings`, and click
:guilabel:`New`.

Define here your :guilabel:`Rounding Precision`, :guilabel:`Rounding Strategy`, and
:guilabel:`Rounding Method` (:guilabel:`Up`, :guilabel:`Down`, or :guilabel:`Nearest`).

Odoo supports two **rounding strategies**:

1. :guilabel:`Add a rounding line`: a *rounding* line is added on the invoice. You have to define
   which accounts record the cash rounding profits and losses.

2. :guilabel:`Modify tax amount`: the rounding is applied in the taxes section.

Apply roundings
===============

When editing a draft invoice, open the :guilabel:`Other Info` tab and select the appropriate
:guilabel:`Cash Rounding Method`.

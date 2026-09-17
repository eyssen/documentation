================
Cash basis taxes
================

Cash basis taxes are due when the payment is made, as opposed to standard taxes that are due when
the invoice is confirmed. Reporting your income and expenses to the government based on the cash
basis method is mandatory in some countries and under some conditions.

.. example::
   You sell a product in the 1st quarter of your fiscal year, and the payment is received in the 2nd
   quarter. Based on the cash basis method, the tax you must pay is for the 2nd quarter.

Configuration
-------------

Go to :menuselection:`Accounting --> Configuration --> Settings` and under the :guilabel:`Taxes`
section, enable :guilabel:`Cash Basis`.

Then, define the :guilabel:`Tax Cash Basis Journal`. To update the journal's default properties
such as the :guilabel:`Journal Name`, :guilabel:`Type` or :guilabel:`Short Code`, open the journal
from :menuselection:`Accounting --> Configuration --> Journals`.

.. screenshot:: accounting-taxes-cash-basis-settings
   :menu: Accounting ‣ Configuration ‣ Settings
   :shows: "Taxes" section; "Cash Basis" setting enabled, with the "Tax Cash Basis Journal" (Cash Basis Taxes) and "Base Tax Received Account" fields.
   :highlight: The "Cash Basis" setting block (red frame).
   :data: Demo company "YourCompany HU".
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the setting.

.. note::
   By default, the journal entries of the :guilabel:`Cash Basis Taxes` journal are named using the
   :guilabel:`CABA` short code.

Once this is done, go to :menuselection:`Accounting --> Configuration --> Taxes` to configure your
taxes. You can either create a :guilabel:`New` tax or update an existing one by clicking on it.

The :guilabel:`Account` column reflects the proper transitional accounts to post taxes until the
payment is registered.

.. screenshot:: accounting-taxes-cash-basis-account-column
   :menu: Accounting ‣ Configuration ‣ Taxes ‣ (open a cash basis tax) ‣ Definition tab
   :shows: "Distribution for Invoices" and "Distribution for Refunds" tables; the "of tax" lines use a transitional tax account.
   :highlight: The "Account" column (red frame).
   :data: Tax "15% cash basis" with a temporary tax account.
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the tab.

In the :guilabel:`Advanced Options` tab, decide of the :guilabel:`Tax Exigibility`. Select
:guilabel:`Based on Payment`, so the tax is due when the payment of the invoice is received. You can
then also define the :guilabel:`Cash Basis Transition Account` where the tax amount is recorded as
long as the original invoice has not been reconciled.

.. screenshot:: accounting-taxes-cash-basis-advanced-options
   :menu: Accounting ‣ Configuration ‣ Taxes ‣ (open a cash basis tax) ‣ Advanced Options tab
   :shows: "Tax Exigibility" set to "Based on Payment" and the "Cash Basis Transition Account" field filled in.
   :highlight: The "Tax Exigibility" and "Cash Basis Transition Account" fields (red frame).
   :data: Tax "15% cash basis".
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the tab.

Impact of cash basis taxes on accounting
----------------------------------------

To illustrate the impact of cash basis taxes on accounting transactions, let's take an example with
the sales of a product that costs 1,000$, with a cash basis tax of 15%.

.. screenshot:: accounting-taxes-cash-basis-invoice
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (open a posted invoice)
   :shows: Posted customer invoice with one line of 1,000.00 and the "15% cash basis" tax; total 1,150.00.
   :highlight: The invoice line and the totals block (red frame).
   :data: Demo customer; tax "15% cash basis".
   :module: account
   :notes: English UI, light theme, 1440px width.

The following entries are created in your accounting, and the tax report is currently empty.

+----------------------------+----------------------------+
|**Customer journal (INV)**                               |
+============================+============================+
| **Debit**                  |**Credit**                  |
+----------------------------+----------------------------+
| Receivable $1,150          |                            |
+----------------------------+----------------------------+
|                            |Income $1,000               |
+----------------------------+----------------------------+
|                            |Temporary tax account $150  |
+----------------------------+----------------------------+

When the payment is then received, it is registered as below :

+----------------------------+----------------------------+
| **Bank journal (BANK)**                                 |
+============================+============================+
| **Debit**                  |**Credit**                  |
+----------------------------+----------------------------+
| Bank $1,150                |                            |
+----------------------------+----------------------------+
|                            |Receivable $1,150           |
+----------------------------+----------------------------+

.. note::
    Once the payment is registered, you can use the :guilabel:`Cash Basis Entries` smart button on
    the invoice to access them directly.

Finally, upon reconciliation of the invoice with the payment, the below entry is automatically
created:

+----------------------------+----------------------------+
| **Tax Cash Basis Journal (Caba)**                       |
+============================+============================+
| **Debit**                  |**Credit**                  |
+----------------------------+----------------------------+
| Income account $1,000      |                            |
+----------------------------+----------------------------+
| Temporary tax account $150 |                            |
+----------------------------+----------------------------+
|                            |  Income account $1,000     |
+----------------------------+----------------------------+
|                            | Tax Received $150          |
+----------------------------+----------------------------+

The journal items :guilabel:`Income account` vs. :guilabel:`Income account` are neutral, but they
are needed to ensure correct tax reports in Odoo with accurate base tax amounts.

Using a default :guilabel:`Base Tax Received Account` is recommended so your balance is at zero and
your income account is not polluted by unnecessary accounting movements. To do so, go to
:menuselection:`Accounting --> Configuration --> Settings`, and select a :guilabel:`Base Tax Received
Account` under the :guilabel:`Cash Basis` setting of the :guilabel:`Taxes` section.

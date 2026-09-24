================
Year-end closing
================

Year-end closing is vital for maintaining financial accuracy, complying with regulations, making
informed decisions, and ensuring transparency in reporting.

.. seealso::
   :doc:`Tax return <tax_returns>`

.. _year-end/fiscal-years:

Fiscal years
============

By default, the fiscal year is set to last 12 months and ends on December 31st. However, its
duration and end date can vary due to cultural, administrative, and economic considerations.

To modify these values, go to :menuselection:`Accounting --> Configuration --> Settings`. Under the
:guilabel:`Fiscal Year` section, change the :guilabel:`Last Day` field if necessary.

If the period lasts *more* than or *less* than 12 months, enable :guilabel:`Fiscal Years` and
:guilabel:`Save`. Then click :icon:`oi-arrow-right` :guilabel:`Fiscal Years`, click
:guilabel:`New`, and give it a :guilabel:`Name` and both a :guilabel:`Start Date` and
:guilabel:`End Date`.

Fiscal years can also be managed from :menuselection:`Accounting --> Configuration --> Accounting
--> Fiscal Year`.

.. note::
   Once the set fiscal period is over, Odoo automatically reverts to the default periodicity,
   considering the value specified in the :guilabel:`Last Day` field.

.. _year-end/checklist:

Year-end checklist
==================

.. _year-end/before-closure:

Before closure
--------------

Before closing a fiscal year, ensure that everything is accurate and up-to-date:

- Make sure all bank accounts are fully :doc:`reconciled <../bank/reconciliation>` up to year-end,
  and confirm that the ending book balances match the bank statement balances.
- Verify that all :doc:`customer invoices <../customer_invoices>` have been created and
  confirmed and that there are no draft invoices.
- Confirm that all :doc:`vendor bills  <../vendor_bills>` have been created and confirmed.
- Ensure the accuracy of all :doc:`expenses <../../expenses>` and validate them.
- Check that all :doc:`received payments <../payments>` have been encoded and confirmed.
- Close all :ref:`suspense accounts <accounting/journals/bank-cash-cc>`.
- Book all :doc:`depreciation <../vendor_bills/assets>` and :doc:`deferred revenue
  <../customer_invoices/deferred_revenues>` entries.

.. _year-end/closing-a-fiscal-year:

Closing a fiscal year
---------------------

Then, to close the fiscal year:

- Run a :ref:`tax report <accounting/reporting/tax-report>`, and verify that all tax information is
  correct.
- Reconcile all accounts on the :ref:`balance sheet <accounting/reporting/balance-sheet>`:

  - Update the bank balances in Odoo according to the actual balances found on the bank statements.
  - Reconcile all transactions in the cash and bank accounts by running the :ref:`aged receivables
    <accounting/reporting/aged-receivable>` and :ref:`aged payables
    <accounting/reporting/aged-payable>` reports.
  - Audit all accounts, fully understanding all transactions and their nature, including loans and
    :doc:`fixed assets <../vendor_bills/assets>`.
  - Optionally, :ref:`match payments <accounting/payments/payments-matching>` to validate any open
    vendor bills and customer invoices with their payments. While this step is optional, it could
    assist the year-end closing process if all outstanding payments and invoices are reconciled,
    potentially finding errors or mistakes in the system.

Next, the accountant likely verifies balance sheet items and book entries for:

  - year-end manual adjustments,
  - work in progress,
  - depreciation journal entries,
  - loans,
  - tax adjustments,
  - etc.

During the year-end audit, the accountant may print paper copies of all balance sheet items (e.g.,
loans, bank accounts, prepayments, sales tax statements) to compare them against the balances
recorded in Odoo.

.. tip::
   As part of this process, setting a :ref:`lock date <year-end/lock-dates>` to the last day
   (inclusive) of the preceding fiscal year is good practice. This ensures that journal entries with
   an accounting date on or before the lock date cannot be created or modified during the audit.

.. _year-end/lock-dates:

Lock dates
~~~~~~~~~~

Setting a lock date prevents modifications to any posted journal entries with an accounting date on
or before the lock date. It also prevents posting new entries with an accounting date on or before
the lock date; in such cases, the entry is postponed to a later date in accordance with its
journal's sequence.

To set the lock dates, go to :menuselection:`Accounting --> Accounting --> Lock Dates`. The
:guilabel:`Lock your Fiscal Period` window groups them in two:

:guilabel:`Management Closing`
   - :guilabel:`Sales Lock Date` — blocks customer entries only.
   - :guilabel:`Purchase Lock Date` — blocks vendor entries only.
   - :guilabel:`Tax Return Lock Date` — blocks entries with taxes, see :ref:`tax lock date
     <tax-returns/lock-date>`.

:guilabel:`Account Period Closing`
   - :guilabel:`Lock Date for All Users` — blocks every entry up to and including that date. It is
     the field shown as :guilabel:`Global Lock Date` in the settings.
   - :guilabel:`Hard Lock Date` — same effect, but irreversible and without any possible exception.

Click :guilabel:`Save` to apply them.

The same fields are also available under :menuselection:`Accounting --> Configuration --> Settings`,
in the :guilabel:`Fiscal Period Closing` section.

.. warning::
   The :guilabel:`Hard Lock Date` is irreversible and is intended to ensure the data inalterability
   required to comply with accounting regulations in certain countries. It **cannot be changed or
   overridden**, regardless of access rights, so set it only once the period is confirmed correct.

.. screenshot:: accounting-year-end-lock-dates
   :menu: Accounting ‣ Accounting ‣ Lock Dates
   :shows: The "Lock your Fiscal Period" dialog with the "Management Closing" group (Sales Lock
      Date, Purchase Lock date, Tax Return Lock Date) and the "Account Period Closing" group (Lock
      Date for All Users, Hard Lock Date), and the Save button.
   :highlight: The "Account Period Closing" group (red frame).
   :data: Lock Date for All Users set to 12/31/2025, Hard Lock Date empty.
   :module: om_fiscal_year
   :notes: English UI, light theme, dialog only.

.. _year-end/current-year-earnings:

Current year's earnings
~~~~~~~~~~~~~~~~~~~~~~~

Odoo uses a unique account type called **current year's earnings** to display the difference
between the **income** and **expense** accounts.

.. note::
   The chart of accounts can only contain one account of this type. By default, it is a 999999
   account named :guilabel:`Undistributed Profits/Losses`.

To allocate the current year's earnings, create a new miscellaneous entry with a date set to the end
of the fiscal year to book them to any equity account.

Then, verify whether the current year's earnings on the **balance sheet** correctly show a zero
balance. If so, a :guilabel:`Hard Lock Date` can be set to the last day of the fiscal year in
:menuselection:`Accounting --> Accounting --> Lock Dates`.

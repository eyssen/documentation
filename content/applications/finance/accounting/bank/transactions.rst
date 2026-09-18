============
Transactions
============

Importing transactions from your bank statements allows keeping track of bank account transactions
and reconciling them with the ones recorded in your accounting.

:doc:`Bank synchronization <bank_synchronization>` automates the process. However, if you do not
want to use it or if your bank is not supported by a synchronization provider, other options exist:

- :doc:`Import the statement files <statement_import>` your bank delivers;
- :ref:`Import bank transactions <transactions/import>` from a spreadsheet;
- :ref:`Register bank transactions <transactions/register>` manually.

.. note::
   :ref:`Grouping transactions by statement <transactions/statements>` is optional.

.. _transactions/import:

Import transactions from a file
===============================

Transactions can be loaded from a comma-separated (CSV) or a spreadsheet (XLSX) file with the
standard import tool. Go to the :guilabel:`Accounting Dashboard`, click the :icon:`fa-ellipsis-v`
:guilabel:`(ellipsis)` icon on the :guilabel:`Bank` journal and select :guilabel:`Transactions`,
then click the :icon:`fa-cog` :guilabel:`(gear)` icon and select :guilabel:`Import records`.

After setting the necessary formatting options and mapping the file columns with their related Odoo
fields, you can run a :guilabel:`Test` and :guilabel:`Import` your bank transactions.

.. tip::
   For the banks covered by a dedicated importer (OTP, K&H, CIB, Raiffeisen, Wise), use the
   :doc:`bank statement importers <statement_import>` instead: they read the bank's own export
   format directly, find the journal from the account number, and skip transactions that are
   already in the database.

.. seealso::
   :doc:`/applications/essentials/export_import_data`

.. _transactions/register:

Register bank transactions manually
===================================

You can also record your bank transactions manually. To do so, go to :guilabel:`Accounting
Dashboard`, click on the :guilabel:`Bank` journal, and then on :guilabel:`New`. Make sure to fill
out the :guilabel:`Partner` and :guilabel:`Label` fields to ease the reconciliation process.

.. _transactions/statements:

Statements
==========

A **bank statement** is a document provided by a bank or financial institution that lists the
transactions that have occurred in a particular bank account over a specified period of time.

In Odoo Accounting, it is optional to group transactions by their related statement, but depending
on your business flow, you may want to record them for control purposes.

.. important::
   If you want to compare the ending balances of your bank statements with the ending balances of
   your financial records, *don't forget to create an opening transaction* to record the bank
   account balance as of the date you begin synchronizing or importing transactions. This is
   necessary to ensure the accuracy of your accounting.

To access a list of existing statements, go to the :guilabel:`Accounting Dashboard`, click the
:icon:`fa-ellipsis-v` :guilabel:`(ellipsis)` icon next to the bank or cash journal you want to
check, then click :guilabel:`Statements`.

.. _transactions/statement-list:

Create a statement
------------------

Open the list of transactions by clicking the :icon:`fa-ellipsis-v` :guilabel:`(ellipsis)` icon on
the bank or cash journal and selecting :guilabel:`Transactions`. Select all the transactions
belonging to the bank statement and, in the :guilabel:`Statement` column, either pick an existing
statement or type a reference and click :guilabel:`Create and edit...` to open the statement form.

A statement can also be created directly from :guilabel:`Statements`: click :guilabel:`New`, and
Odoo proposes a :guilabel:`Reference` built from the journal code and the date, and carries the
:guilabel:`Starting Balance` over from the journal's previous statement.

On the statement form, fill out the :guilabel:`Reference`, the :guilabel:`Date`, the
:guilabel:`Starting Balance` and the :guilabel:`Ending Balance`, add the transactions, and save.

.. screenshot:: accounting-bank-statement-form
   :menu: Accounting ‣ Dashboard ‣ (bank journal ellipsis) ‣ Statements ‣ (open a statement)
   :shows: A bank statement form with the Reference, Date, Starting Balance and Ending Balance
      fields, the list of statement lines, the computed balance in the footer, and the
      "Transactions" and "Journal Items" smart buttons.
   :highlight: The Starting Balance / Ending Balance fields (red frame).
   :data: Statement "BNK1 Statement 09/30/2026" with five lines.
   :module: account_statement_base, eyssen_accountant
   :notes: English UI, light theme, 1440px width.

.. _transactions/view-edit-print:

Statement viewing, editing, and printing
----------------------------------------

To view an existing statement, click on the statement name in the bank transaction list view, or
open it from :guilabel:`Statements`. From here, you can edit the :guilabel:`Reference`,
:guilabel:`Starting Balance`, or :guilabel:`Ending Balance`.

.. note::
   Manually updating the :guilabel:`Starting Balance` automatically updates the :guilabel:`Ending
   Balance` based on the new value of the :guilabel:`Starting Balance` and the value of the
   statement's transactions.

.. warning::
   If the :guilabel:`Starting Balance` doesn't equal the previous statement's :guilabel:`Ending
   Balance`, or if the :guilabel:`Ending Balance` doesn't equal the running balance
   (:guilabel:`Starting Balance` plus the statement's transactions), a warning banner appears at the
   top of the statement explaining the issue. To maintain flexibility, it is still possible to save without first resolving the
   issue.

To attach a digital copy (i.e., JPEG, PNG, or PDF) of the bank statement for enhanced recordkeeping,
click the :icon:`fa-paperclip` :guilabel:`Attachments` button and select the file to attach.

To generate and print a PDF of the bank statement, open the statement list, select the statement,
click the :icon:`fa-cog` :guilabel:`(gear)` icon and select :icon:`fa-print` :guilabel:`Statement`.

.. note::
   When a bank statement is generated to be printed, it is automatically added to the
   :guilabel:`Attachments`.

.. seealso::
   - :doc:`statement_import`
   - :doc:`reconciliation`

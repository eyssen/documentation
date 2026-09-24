===================
Bank reconciliation
===================

**Bank reconciliation** is the process of matching your :doc:`bank transactions <transactions>` with
your business records, such as :doc:`customer invoices <../customer_invoices>`, :doc:`vendor bills
<../vendor_bills>`, and :doc:`payments <../payments>`. Not only is this compulsory for most
businesses, but it also offers several benefits, such as reduced risk of errors in financial
reports, detection of fraudulent activities, and improved cash flow management.

Thanks to the bank :doc:`reconciliation models <reconciliation_models>`, Odoo pre-selects the
matching entries automatically.

.. seealso::
   - :doc:`bank_synchronization`
   - :doc:`statement_import`
   - :doc:`transactions`

.. _accounting/reconciliation/access:

Bank reconciliation view
========================

To access a bank journal's **reconciliation view**, go to your :guilabel:`Accounting Dashboard` and
either:

- click the journal name (e.g., :guilabel:`Bank`) to display all transactions, including those
  previously reconciled, or
- click the :guilabel:`Reconcile <N> Items` button to display only the transactions that are not
  reconciled yet. Remove the :guilabel:`Not Reconciled` filter from the search bar to include
  previously reconciled transactions.

The card also shows a :guilabel:`<N> to check` link, which opens the transactions someone marked as
:guilabel:`To Check`, and a circular indicator of how much of the journal is already reconciled.

.. screenshot:: accounting-reconciliation-entry-points
   :menu: Accounting ‣ Dashboard
   :shows: A bank journal card with the "Transactions" and "Reconcile 12 Items" buttons on the left
      and the "5 to check" link and the reconciliation-progress ring on the right.
   :highlight: The "Reconcile 12 Items" button (red frame).
   :data: Demo company "YourCompany HU"; bank journal with 12 unreconciled and 5 to-check lines.
   :module: account, account_reconcile_oca, eyssen_accountant
   :notes: English UI, light theme, 1440px width, crop to the card.

The reconciliation view is split in two: the list of bank transactions on the left, and the
reconciliation of the selected transaction on the right.

Transactions
   The left pane shows the bank transactions of the journal as cards with the date, the amount, the
   partner, and the label. A :guilabel:`To check` badge marks the transactions someone flagged, and
   a :guilabel:`Reconciled` badge marks the ones already done. The badge also tells you whether the
   line was reconciled :guilabel:`Automatically` by a rule or :guilabel:`Manually`. Click a
   transaction to open it on the right.

   A :guilabel:`Statement` button appears on the separator above the first transaction that does not
   belong to a statement yet; use it to :ref:`create a statement <transactions/statement-list>` from
   that transaction down.

Reconciliation
   The right pane shows the resulting journal entry: the bank transaction, the counterpart lines
   proposed or chosen, and the remaining open amount. A banner above it states how the line was
   matched and by which rule. Below, the tabs let you pick the counterpart:
   :ref:`reconciliation/existing-entries`, :ref:`reconciliation/manual-operations`,
   :guilabel:`Other Info` (the label and the internal note), and :guilabel:`Chatter`.
   :ref:`Reconciliation model buttons <reconciliation/button>` are displayed above the tabs.

.. screenshot:: accounting-reconciliation-view
   :menu: Accounting ‣ Dashboard ‣ (click the bank journal name)
   :shows: The reconciliation screen: the transaction cards on the left with one selected, and on
      the right the status bar (Validate, Reset reconciliation, To Check, View move), the resulting
      entry, the reconciliation-model buttons and the "Reconcile" tab with the matching invoices.
   :highlight: The resulting entry block and the "Validate" button.
   :data: A 1,200.00 HUF incoming transaction from "Deco Addict" matching invoice INV/2026/0031.
   :module: account_reconcile_oca, eyssen_accountant
   :notes: English UI, light theme, 1440px width.

.. _accounting/reconciliation/reconcile:

Reconcile transactions
======================

Transactions can be matched automatically with the use of :doc:`reconciliation models
<reconciliation_models>`, or they can be matched with :ref:`existing entries
<reconciliation/existing-entries>`, :ref:`manual operations <reconciliation/manual-operations>`, and
:ref:`reconciliation model buttons <reconciliation/button>`.

#. Select a transaction among the unreconciled bank transactions.
#. Define the counterpart, either by selecting existing journal items in the :guilabel:`Reconcile`
   tab, by filling out the :guilabel:`Manual operation` tab, or by clicking a reconciliation model
   button.
#. If the resulting entry is not fully balanced, balance it by adding another existing counterpart
   entry or writing it off with a :ref:`manual operation <reconciliation/manual-operations>`.
#. Click the :guilabel:`Validate` button to confirm the reconciliation and move to the next
   transaction.

.. tip::
   - The :guilabel:`Validate` button stays disabled until the entry balances; while it is not
     balanced, the button reads :guilabel:`Reconcile` and cannot be clicked.
   - :guilabel:`Reset reconciliation` clears everything you selected on the transaction and starts
     over from the automatic proposal.
   - :guilabel:`Unreconcile` undoes a reconciliation that was already validated. Odoo asks for a
     confirmation first.
   - :guilabel:`View move` opens the journal entry generated for the transaction.

.. tip::
   If you are not sure how to reconcile a particular transaction and would like to deal with it
   later, use the :guilabel:`To Check` button. All transactions marked this way can be displayed
   using the :guilabel:`To Check` filter or the :guilabel:`<N> to check` link on the dashboard.
   :guilabel:`Set as Checked` removes the flag.

.. note::
   Bank transactions are posted on the **journal's suspense account** until reconciliation. At this
   point, reconciliation modifies the transaction journal entry by replacing the bank suspense
   account with the corresponding receivable, payable, or outstanding account.

.. _reconciliation/existing-entries:

Match existing entries
----------------------

The :guilabel:`Reconcile` tab lists the open journal items that can be matched with the transaction:
posted lines with a remaining amount, on a reconcilable account, in the same company. Entries
pre-selected by the :doc:`reconciliation models <reconciliation_models>` appear first, and the list
is filtered on the transaction's partner when one is set. Click a line to add it to the resulting
entry, and click it again to remove it.

.. tip::
   The search bar of the tab allows you to look for specific journal items, for example by invoice
   number when the bank label does not contain it.

.. _reconciliation/manual-operations:

Manual operations
-----------------

If there is no existing entry to match the selected transaction, reconcile the transaction manually
in the :guilabel:`Manual operation` tab by choosing the :guilabel:`Account` and the
:guilabel:`Amount`, and completing the optional :guilabel:`Partner`, :guilabel:`Name` and
:guilabel:`Analytic Distribution` fields. This is also how you write off a small remaining
difference after matching an invoice.

.. tip::
   When the selected counterpart is an invoice or a bill that is only partially covered by the
   payment, the tab explains how much of it will be reduced and offers a :guilabel:`fully paid`
   button. Clicking it reconciles the invoice entirely and books the difference as a new line in
   the resulting entry, which you can then re-assign to another account.

.. _reconciliation/button:

Reconciliation model buttons
----------------------------

Use a :doc:`reconciliation model <reconciliation_models>` button for manual operations that are
frequently used, such as bank fees or rounding differences. These buttons are displayed above the
tabs and generate the counterpart line in one click; they can also be combined with existing
entries.

.. _accounting/reconciliation/filters:

Reconciliation filters
======================

Recurring searches can be saved as **reconciliation filters** and reused in both panes of the
reconciliation screen. Go to :menuselection:`Accounting --> Configuration --> Reconciliation
Filters` and click :guilabel:`New`:

- :guilabel:`Name`: the label shown in the reconciliation screen.
- :guilabel:`Applies to`: :guilabel:`Bank/cash lines` for the transaction list on the left, or
  :guilabel:`Counterpart candidates` for the list of entries to match.
- :guilabel:`Domain`: the condition to apply, e.g. ``[('amount', '>', 100000)]``.
- :guilabel:`Bank/cash journals`: restrict the filter to specific journals. Leave empty to apply it
  everywhere.
- :guilabel:`User`: leave empty to share the filter with everyone, or set a user to make it private.
- :guilabel:`Sequence`: the display order of the filters.

.. _accounting/reconciliation/automatic:

Automatic reconciliation
========================

When a reconciliation model has :guilabel:`Auto-validate` enabled and its conditions are perfectly
met, Odoo reconciles the transaction on its own, without waiting for you. Lines reconciled this way
carry the :guilabel:`Automatic` provenance and name the rule that matched them, so an automatic
match can always be traced back.

Transactions that could not be matched at import time are retried once a day by the *eYssen
Accountant: retry automatic statement line reconciliation* scheduled action, which picks up the
backlog in rotation. This means a transaction may become reconciled after the fact, for instance
once the corresponding invoice is finally posted.

.. seealso::
   :doc:`reconciliation_models`

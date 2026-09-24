============================
Accounting tools for Hungary
============================

Besides the :doc:`tax returns <vat_return>`, the :guilabel:`Magyar könyvelés és ÁNYK
adatszolgáltatás` (`eyssen_l10n_hu_accountant`) module gives accountants the following tools.

Change the account of a posted invoice line
===========================================

The income or expense account of a **posted** invoice or bill line can be corrected without resetting
the document to draft (which is not possible for invoices already reported to NAV). Click the
signpost icon (:guilabel:`Change Account`) at the end of the invoice line, or on the journal item in
:menuselection:`Accounting --> Accounting --> Journal Items`. In the :guilabel:`Change Posted
Account` dialog, select the :guilabel:`New Account` (and, if needed, the analytic distribution) and
click :guilabel:`Change`.

.. screenshot:: finance-fl-hungary-change-posted-account
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (posted invoice) ‣ signpost icon on a line
   :shows: The "Change Posted Account" dialog with "Current Account", "New Account", "Tax Grids", the analytic distribution, and the read-only item line, debit and credit; buttons "Change" and "Cancel".
   :highlight: The "New Account" field (red frame).
   :data: Posted invoice line "Consulting" on account 911; new account 913.
   :module: eyssen_l10n_hu_accountant
   :notes: English UI, light theme, 1440px width, crop to the dialog.

.. note::
   The dialog is available to users with the :guilabel:`Administrator` accounting access right.

Accounting date
===============

For Hungarian companies, the suggested accounting date of a document is based on its own date
(fulfillment date) rather than on today. When a lock date is set, the accounting date of sales
documents falling into the locked period is moved to the first day of the current month.

Inventory revaluation
=====================

With automated inventory valuation, the value of a single inventory valuation layer can be
corrected, for example when the purchase price on the receipt was wrong. In
:menuselection:`Inventory --> Reporting --> Valuation`, click the pencil icon (:guilabel:`Change
Valuation`) of the row and set the :guilabel:`New Unit Value` or the :guilabel:`New Total Value`.

- If the layer has a journal entry, the entry is reset to draft, its amounts are replaced and it is
  posted again.
- Otherwise, select the :guilabel:`Journal` and the :guilabel:`Counterpart Account`; a
  *Revaluation of …* journal entry is created.

Every change is kept with the old and new values and the user; the :guilabel:`Change History` icon
opens it. Products with the *Standard Price* costing method cannot be revalued.

Dashboard balance
=================

The bank and cash journal cards of the :guilabel:`Accounting Dashboard` display the general ledger
balance of the journal's default account (*<account code> <account name> egyenleg*), next to the
statement balance.

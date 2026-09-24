=====================
Reconciliation models
=====================

Reconciliation models are used to automate the :doc:`bank reconciliation <reconciliation>` process,
which is especially handy when dealing with recurring entries like bank fees. Reconciliation models
can also be helpful in handling :doc:`cash discounts <../customer_invoices/cash_discounts>`.

Each model is created based on a :ref:`model type <models/type>` and :guilabel:`bank transaction
conditions`.

.. seealso::
   - :doc:`bank_synchronization`
   - :doc:`reconciliation`

.. _models/type:

Reconciliation model types
==========================

The reconciliation models are available by going to :menuselection:`Accounting --> Configuration
--> Banks --> Reconciliation Models`. For each reconciliation model, a :guilabel:`Type` must be set.
Three types of models exist:

- :guilabel:`Add a button to the reconcile screen`: a button is created above the tabs of the bank
  reconciliation view. If clicked, this button generates a counterpart entry to reconcile with the
  active transaction based on the rules set in the model. The rules specified in the model determine
  the counterpart entry's account(s), amount(s), label(s), and analytic distribution. This type is
  **manual only**: it never runs on its own;
- :guilabel:`Suggest a fixed counterpart line`: used for recurring transactions to match the
  transaction to a new entry based on conditions that must match the information on the transaction;
- :guilabel:`Find a matching invoice/bill`: used for recurring transactions to match the transaction
  to existing invoices, bills, or payments based on conditions that must match the information on
  the transaction.

The form states under the :guilabel:`Type` whether the selected type :guilabel:`Can run
automatically` or is :guilabel:`Manual only`.

.. tip::
   To create a rule without going through the full form, use the guided wizard: it asks for a
   :guilabel:`Name`, for what the rule should do (:guilabel:`Find a matching invoice/bill`,
   :guilabel:`Suggest a fixed counterpart line` or :guilabel:`Add a button to the reconcile
   screen`), for the :guilabel:`Counterpart account` and the :guilabel:`Bank/cash journals`, and
   whether it should :guilabel:`Reconcile automatically`. It then summarizes in one sentence what
   the rule will do and creates it.

Default reconciliation models
=============================

In Odoo, different models are available by default depending on the company's fiscal localization.
These can be updated if needed. Users can also create their own reconciliation models by clicking
:guilabel:`New`.

.. important::
   If a record matches with several reconciliation models, the first one in the *sequence* of models
   is applied. You can rearrange the order by dragging and dropping the handle next to the name.

   .. screenshot:: accounting-reconciliation-models-sequence
      :menu: Accounting ‣ Configuration ‣ Banks ‣ Reconciliation Models
      :shows: The reconciliation model list with the drag handle in front of each row, four models
         in order (invoice matching, partial match, bank fees, manual write-off button).
      :highlight: The drag handles of the first column (red frame).
      :data: Demo company "YourCompany HU" with the default localization models.
      :module: account, account_reconcile_model_oca, eyssen_accountant
      :notes: English UI, light theme, 1440px width.

Invoices/Bills perfect match
----------------------------

This model should be at the top of the *sequence* of models, as it enables Odoo to suggest matching
existing invoices or bills with a bank transaction based on set conditions.

.. screenshot:: accounting-reconciliation-models-perfect-match
   :menu: Accounting ‣ Configuration ‣ Banks ‣ Reconciliation Models ‣ Invoices/Bills perfect match
   :shows: The reconciliation model form with Type "Find a matching invoice/bill", the "Reconcile
      automatically" toggle on, and the conditions "Label" and "Partner is Set" ticked.
   :highlight: The "Reconcile automatically" toggle and the matching conditions.
   :data: The default "Invoices/Bills perfect match" model.
   :module: account, account_reconcile_model_oca, eyssen_accountant
   :notes: English UI, light theme, 1440px width.

Odoo automatically reconciles the payment when the :guilabel:`Reconcile automatically` option is
enabled, and the model conditions are perfectly met. In this case, it expects to find on the bank statement's
line the invoice/payment's reference (as :guilabel:`Label` is selected) and the partner's name
(as :guilabel:`Partner is set` is selected) to suggest the correct counterpart entry and reconcile
the payment automatically.

Invoices/Bills partial match if underpaid
-----------------------------------------

This model suggests a customer invoice or vendor bill that partially matches the payment when the
amount received is slightly lower than the invoice amount, for example in the case of
**cash discounts**. The difference is reconciled with the account indicated in the
:guilabel:`counterpart entries` tab.

The reconciliation model :guilabel:`Type` is :guilabel:`Rule to match invoices/bills`, and the
:guilabel:`Payment tolerance` should be set.

.. screenshot:: accounting-reconciliation-models-partial-match
   :menu: Accounting ‣ Configuration ‣ Banks ‣ Reconciliation Models ‣ Invoices/Bills partial match
      if underpaid
   :shows: The reconciliation model form with Type "Find a matching invoice/bill", the "Payment
      Tolerance" checkbox on and a "Gap" of 2 in percentage, and the counterpart entries tab
      showing the write-off account.
   :highlight: The "Payment Tolerance" and "Gap" fields (red frame).
   :data: The default "Invoices/Bills partial match if underpaid" model.
   :module: account, account_reconcile_model_oca
   :notes: English UI, light theme, 1440px width.

.. note::
   The :guilabel:`Payment tolerance` is only applicable to lower payments. It is disregarded when an
   overpayment is received.

.. seealso::
   :doc:`../customer_invoices/cash_discounts`

Line with bank fees
-------------------

This model suggests a counterpart entry according to the rules set in the model. In this case, the
reconciliation model :guilabel:`Type` is :guilabel:`Rule to suggest counterpart entry`, and the
:guilabel:`Label` can be used for example, to identify the information referring to the
:guilabel:`Bank fees` in the label of the transaction.

.. screenshot:: accounting-reconciliation-models-bank-fees
   :menu: Accounting ‣ Configuration ‣ Banks ‣ Reconciliation Models ‣ (a bank fees model)
   :shows: A reconciliation model form with Type "Suggest a fixed counterpart line", the Label
      condition set to "Contains" with the parameter "BANK FEE", and a counterpart line booked on
      the bank charges account.
   :highlight: The Label condition and the counterpart line.
   :data: Model "Bank fees", counterpart account "Bank charges".
   :module: account, account_reconcile_model_oca
   :notes: English UI, light theme, 1440px width.

.. note::
   `Regular expressions <https://regexone.com/>`_, often abbreviated as **Regex**, can be used in
   Odoo in various ways to search, validate, and manipulate data within the system. Regex can be
   powerful but also complex, so it's essential to use it judiciously and with a good understanding
   of the patterns you're working with.

   To use regular expressions in your reconciliation models, set the :guilabel:`Transaction Type`
   to :guilabel:`Match Regex` and add your expression. Odoo automatically retrieves the
   transactions that match your Regex expression and the conditions specified in your model.

   .. screenshot:: accounting-reconciliation-models-regex
      :menu: Accounting ‣ Configuration ‣ Banks ‣ Reconciliation Models ‣ (a model using a regex)
      :shows: The Label condition set to "Match Regex" with a regular expression in the Label
         Parameter field.
      :highlight: The "Match Regex" selection and the expression (red frame).
      :data: Expression matching an invoice number, e.g. "INV/[0-9]{4}/[0-9]+".
      :module: account, account_reconcile_model_oca
      :notes: English UI, light theme, crop to the conditions block.

Partner mapping
===============

Partner mapping allows you to establish rules for automatically matching transactions to the correct
partner account, saving time and reducing the risk of errors that can occur during manual
reconciliation. For example, you can create a partner mapping rule for incoming payments with
specific reference numbers or keywords in the transaction description. When an incoming payment
meets these criteria, Odoo automatically maps it to the corresponding customer's account.

To create a partner mapping rule, go to the :guilabel:`Partner Mapping` tab and enter the
:guilabel:`Find Text in Label`, :guilabel:`Find Text in Notes`, and :guilabel:`Partner`.

.. screenshot:: accounting-reconciliation-models-partner-mapping
   :menu: Accounting ‣ Configuration ‣ Banks ‣ Reconciliation Models ‣ (a model) ‣ Partner Mapping
   :shows: The Partner Mapping tab with two lines: "Find Text in Label", "Find Text in Notes" and
      the mapped Partner.
   :highlight: The Partner Mapping tab (red frame).
   :data: One line mapping the label "DECO" to the customer "Deco Addict".
   :module: account
   :notes: English UI, light theme, crop to the tab.

.. _models/eyssen-options:

Additional options
==================

Two extra settings are available on the reconciliation model form:

:guilabel:`Show in reconcile toolbar`
   Only for the :guilabel:`Add a button to the reconcile screen` type. Turn it off to hide a rarely
   used write-off model from the reconciliation screen without deleting it.

:guilabel:`When bank amount exceeds matched invoices`
   Only for :guilabel:`Find a matching invoice/bill` rules that reconcile automatically. It decides
   what happens when the bank amount is *higher* than the sum of the matched invoices (an
   overpayment, or an incomplete multi-invoice match):

   - :guilabel:`Allow auto (leave residual open)`: reconcile anyway and leave the remainder as an
     open balance on the partner;
   - :guilabel:`Allow auto and mark To Check`: reconcile anyway, but flag the entry as
     :guilabel:`To Check` for review;
   - :guilabel:`Only auto on full amount match`: do not reconcile automatically unless the matched
     invoices fully cover the bank amount. The match is still suggested.

   The :guilabel:`Payment Tolerance` keeps handling *underpayments*; this setting only covers the
   opposite case.

.. warning::
   On a :guilabel:`Find a matching invoice/bill` rule, if any of the text conditions
   (:guilabel:`Label`, :guilabel:`Note`, :guilabel:`Reference`) is enabled and the statement text
   does not match, the rule does **not** fall back to matching on the amount alone.

.. _localizations/spain/cash-accounting:

======================================
Cash accounting regime (RECC) in Spain
======================================

Under the Spanish **cash accounting regime** (*régimen especial del criterio de caja*, RECC), the
output VAT of a sale is due, and the input VAT of a purchase is deductible, when the invoice is
collected or paid, and at the latest on **31 December of the year following the operation**
(LIVA arts. 163 decies to sexiesdecies). The ordinary rule is the opposite: VAT is due when the
invoice is issued.

The Spanish localization (*Spain - Accounting (PGCE 2008)*, `l10n_es`) supports the regime for:

- **companies under the regime**: their domestic sales and purchases follow the cash accounting
  rules;
- **companies under the general regime that buy from a supplier under the regime**: they deduct the
  VAT of that supplier's invoices when they pay them (LIVA art. 163 quinquiesdecies).

.. important::
   Odoo does not check that the company meets the conditions to opt for the regime, or that the
   option has been communicated to the tax agency. Confirm with your tax advisor before enabling it.

.. note::
   The regime works with the Spanish charts of accounts of mainland Spain. It is not available for
   the Canary Islands charts.

Enable the regime
=================

#. Go to :menuselection:`Accounting --> Configuration --> Settings` and scroll to the
   :guilabel:`Spain` section. The section is only shown for companies whose country is Spain.
#. In the :guilabel:`VAT regime` setting, select :guilabel:`Cash accounting (RECC)`.
#. Click :guilabel:`Save`.

.. screenshot:: finance-fl-spain-cash-accounting-settings
   :menu: Accounting ‣ Configuration ‣ Settings ‣ Spain
   :shows: The "Spain" section of the Accounting settings with the "Fiscal profile", "VAT regime" (set to "Cash accounting (RECC)") and "Company setup" settings.
   :highlight: The "VAT regime" setting.
   :data: Demo company "YourCompany ES", Spanish localization installed.
   :module: l10n_es
   :notes: English UI, light theme, 1440px width, crop to the "Spain" section.

The :guilabel:`VAT regime` can also be chosen in the :ref:`Spanish company setup wizard
<localizations/spain/setup-wizard>` (step :guilabel:`3. Tax regime`).

When the regime is saved for a company, Odoo:

- activates the **RECC taxes** (see below);
- enables the cash basis feature of the Accounting settings, if it is not enabled yet, and sets the
  tax cash basis journal of the company if there is none;
- creates the RECC taxes and the two transition accounts if the company was created before this
  feature existed.

.. _localizations/spain/cash-accounting/taxes:

RECC taxes and transition accounts
==================================

For each ordinary domestic VAT tax at 4 %, 10 % and 21 %, the localization provides a **twin tax**
named like the ordinary tax followed by *RECC*:

- sales: goods and services at 4 %, 10 % and 21 %;
- purchases: current goods, services and investment goods at 4 %, 10 % and 21 %.

The twin taxes are identical to the ordinary ones (same rate, same tags in the tax report, so they
are reported in the same boxes of the declarations), except that their :guilabel:`Tax Exigibility`
is :guilabel:`Based on Payment` and that they use a **transition account**. They are loaded
**inactive** (archived) and are activated when the company opts for the regime. You find them in
:menuselection:`Accounting --> Configuration --> Taxes`.

.. list-table::
   :header-rows: 1
   :widths: 15 45 40

   * - Account
     - Name
     - Used by
   * - 477900 (4779)
     - Output VAT pending accrual (cash accounting)
     - Sales RECC taxes: the VAT of a sale stays here until it is collected.
   * - 472900 (4729)
     - Input VAT pending deduction (cash accounting)
     - Purchase RECC taxes: the VAT of a purchase stays here until it is paid.

The Spanish names of the accounts are *Hacienda Pública. IVA repercutido pendiente de devengo
(criterio de caja)* and *Hacienda Pública. IVA soportado pendiente de deducir (criterio de caja)*.

Sales and purchases
===================

Once the regime is enabled, you work as usual. When taxes are computed on an invoice line, and
again when the invoice is posted, Odoo replaces the ordinary domestic VAT tax by its RECC twin:

- on **customer invoices and vendor bills** of a company under the regime;
- on **vendor bills** from a supplier flagged as being under the regime (see :ref:`below
  <localizations/spain/cash-accounting/supplier>`), even if the company itself is under the
  general regime.

Only the taxes that have a twin are replaced. The **excluded operations** keep their own taxes:
intra-community acquisitions, reverse charge operations, exports, the equivalence surcharge, and any
other tax without a RECC twin (for example other rates, exempt operations or withholdings).

.. note::
   The replacement only applies to invoices that are posted after the regime is enabled. Invoices
   that were already posted keep their ordinary taxes.

Collection and payment
----------------------

When an invoice with RECC taxes is posted, its VAT is booked to the transition account. Each
payment (partial or total) then generates an entry in the **tax cash basis journal** that moves the
proportional part of the VAT from the transition account to the ordinary VAT account: 477 for the
output VAT and 472 for the input VAT. The tax report tags are on this entry, so the VAT is reported
in the period of the payment date.

Example: an invoice of 1,000.00 € with 21 % VAT (total 1,210.00 €) issued on 10 March 2025, of
which 605.00 € (half) are collected on 10 May 2025.

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Date
     - Event
     - VAT accrued
   * - 10 March 2025
     - Invoice posted
     - 0.00 € (210.00 € in account 477900)
   * - 10 May 2025
     - Collection of 605.00 €
     - 105.00 € (105.00 € left in account 477900)
   * - 31 December 2026
     - Deadline (accrual entry created by the scheduled action)
     - 105.00 € on a base of 500.00 € (account 477900 is now 0.00 €)

Accrual on the deadline
-----------------------

The VAT that is still unpaid on **31 December of the year following the operation** becomes due
anyway. The operation date is the invoice date. In the example above, the deadline of an invoice
dated in 2025 is 31 December 2026.

A daily scheduled action, :guilabel:`Spain: VAT accrual of the cash accounting regime (RECC)`
(:menuselection:`Settings --> Technical --> Automation --> Scheduled Actions`, with the developer
mode active), looks for the posted invoices of Spanish companies with unpaid or partially paid RECC
VAT whose deadline has passed. For each of them it creates an entry in the tax cash basis journal:

- the entry is dated on the deadline, or on the first day after the lock date if the period is
  already locked;
- it mirrors the entry of a payment for the unpaid part of the invoice, and reports the base and
  the VAT with the same tax report tags;
- its reference is *<invoice> - VAT accrual on the deadline of the cash accounting regime*, and a
  message with a link to the entry is posted in the chatter of the invoice.

Payments received after the deadline accrue nothing more: the VAT was already accrued. The
scheduled action never accrues the same invoice twice.

For purchases, the mechanism is the same: the input VAT of a vendor bill that is still unpaid on the
deadline becomes deductible on that date.

Invoice mention
===============

The invoices of a company under the regime must state it. Customer invoices (and receipts) with at
least one RECC tax carry the mention **Régimen especial del criterio de caja**:

- on the invoice form, as a badge in the title area;
- on the invoice PDF, above the payment terms.

The mention is a legal text and is not translated. Vendor bills do not carry it.

.. screenshot:: finance-fl-spain-cash-accounting-invoice
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (an invoice with RECC taxes)
   :shows: A customer invoice of a company under the cash accounting regime: the "Régimen especial del criterio de caja" badge next to the title and a line with a "21% ... RECC" tax.
   :highlight: The badge and the RECC tax of the line.
   :data: Demo company "YourCompany ES" with the VAT regime set to "Cash accounting (RECC)".
   :module: l10n_es
   :notes: English UI, light theme, 1440px width.

.. _localizations/spain/cash-accounting/supplier:

Suppliers under the regime
==========================

If the company is under the general regime, it can only deduct the VAT of a supplier under the
cash accounting regime when it pays the supplier's invoice. To handle this:

#. Open the supplier's contact form and go to the :guilabel:`Invoicing` tab.
#. Enable :guilabel:`Supplier in the Cash Accounting Regime (RECC)` (below the
   :guilabel:`Fiscal Position`). The field is only shown when the fiscal country of your company is
   Spain.
#. Save.

Vendor bills from this supplier are then posted with the purchase RECC taxes, so that the input
VAT is deductible at the payment date, and at the latest on the deadline. The purchase RECC taxes
are created and activated the first time they are needed. The company's own sales are not affected.

.. note::
   The setting is shared by all the contacts of the same company: enabling it on a contact applies
   it to its company and to its other contacts. Ask the supplier which regime it applies.

Effects on the declarations
===========================

The AEAT declarations of the Accounting app take the regime into account, as long as they are
installed (see :doc:`aeat_declarations`):

- **Modelo 303**: the operations under the regime are reported when they accrue, in the boxes of
  their ordinary tax. Boxes [62]/[63] and [74]/[75] report the operations under the regime when
  they would have accrued under the general rule.
- **Modelo 390**: the VAT accrued in the year under the regime, including the accruals on 31
  December of the following year, is reported in boxes [643] to [648] (4, 10 and 21 %) instead of
  the boxes of the ordinary regime.
- **Modelo 347**: the operations of a partner under the regime (company regime or supplier under the
  regime) are flagged, and the amounts accrued in the year under the regime are reported
  separately. The entries that accrue the VAT do not repeat the invoices in the annual amount.
- **VAT books**: each collection or payment of an invoice with VAT due on payment is recorded
  (date, amount, means of payment and bank account). The accrual entries are not booked as
  invoices.

Gotchas
=======

- Enable the regime **before** posting the first invoice of the period it applies to: the taxes of
  the invoices that are already posted are not changed.
- The RECC taxes are archived until the company opts for the regime (or buys from a supplier under
  it). Do not archive them again while the regime is in use: Odoo activates them again when it
  needs them.
- The accrual on the deadline depends on the scheduled action: check that it is active if a
  deadline is missed.
- If the accounting period of the deadline is already locked, the accrual entry is dated on the
  first day after the lock date, not on the deadline.

.. seealso::
   - :doc:`aeat_declarations`
   - :doc:`../spain`

======
Mexico
======

.. |SAT| replace:: :abbr:`SAT (Servicio de Administración Tributaria)`
.. |RFC| replace:: :abbr:`RFC (Registro Federal de Contribuyentes)`
.. |CFDI| replace:: :abbr:`CFDI (Comprobante Fiscal Digital por Internet)`
.. |PAC| replace:: :abbr:`PAC (Proveedor Autorizado de Certificación)`

.. _l10n/mx/modules:

Modules
=======

The following modules related to the Mexican localization are available:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Mexico - Accounting`
     - `l10n_mx`
     - Default :ref:`fiscal localization package <fiscal_localizations/packages>`: the minimal
       Mexican chart of accounts (with the |SAT| grouping codes), the IVA / ISR / IEPS taxes with
       their |SAT| tax type and factor type, cash basis tax configuration, and the list of Mexican
       banks. Installed automatically for Mexican companies.
   * - :guilabel:`Employees - Mexico`
     - `l10n_mx_hr`
     - Adds the :guilabel:`CURP` and :guilabel:`RFC` fields to the employee form (installed
       automatically with the **Employees** app).

.. note::
   The electronic invoicing (signing of |CFDI| 4.0 documents through a |PAC|, payment complements,
   cancellations, global invoices, external trade complement, delivery guide / *carta porte*,
   customs numbers), the Mexican electronic accounting reports (chart of accounts and trial balance
   XML, DIOT, *pólizas*), the Point of Sale, eCommerce and subscription CFDI extensions, and the
   Mexican payroll are **not** available in this edition. Invoices are printed by Odoo and must be
   stamped through the |SAT| portal or a |PAC| outside Odoo.

.. _l10n/mx/company:

Company
=======

Verify that the company is configured with the correct data: go to :menuselection:`Settings -->
Users & Companies --> Companies`, and select the company to configure. Enter the full
:guilabel:`Address` in the resulting form, including: :guilabel:`ZIP` code, :guilabel:`State`,
:guilabel:`Country`, and |RFC| (:guilabel:`Tax ID` number).

.. important::
   From a legal point of view, Mexican companies **must** use the local currency (MXN). To use
   another currency, let MXN be the default currency and use a :doc:`pricelist
   <../../sales/sales/products_prices/prices/pricing>` instead.

.. _l10n/mx/contacts:

Contacts
========

To create a contact that can be invoiced, go to :menuselection:`Contacts --> New`. Then, enter the
contact name, full :guilabel:`Address` including the :guilabel:`ZIP` code, :guilabel:`State`,
:guilabel:`Country`, and |RFC| (:guilabel:`Tax ID`). The |RFC| is validated against the |SAT|
format.

.. _l10n/mx/taxes:

Taxes
=====

.. _l10n/mx/factor-type:

Factor type and SAT tax type
----------------------------

Both the :guilabel:`SAT Tax Type` and :guilabel:`Factor Type` fields are pre-loaded in the default
taxes. If new taxes are created, these fields must be set. To do so, go to
:menuselection:`Accounting --> Configuration --> Taxes`, then fill both fields in the
:guilabel:`Advanced Options` tab.

Odoo supports four groups of :guilabel:`SAT Tax Types`: :guilabel:`IVA`, :guilabel:`ISR`,
:guilabel:`IEPS`, and :guilabel:`Local`. The :guilabel:`Factor Type` is :guilabel:`Tasa` (rate),
:guilabel:`Cuota` (fixed amount), or :guilabel:`Exento` (exempt).

.. tip::
   Mexico manages two different kinds of 0% VAT to accommodate two scenarios:

   - For *0% VAT*, set the :guilabel:`Factor Type` as :guilabel:`Tasa`
   - For *VAT Exempt*, set the :guilabel:`Factor Type` as :guilabel:`Exento`

.. screenshot:: finance-fl-mexico-tax-factor-type
   :menu: Accounting ‣ Configuration ‣ Taxes ‣ (IVA 16%) ‣ Advanced Options tab
   :shows: The Advanced Options tab of the "IVA 16%" sales tax with the "SAT Tax Type" set to "IVA" and the "Factor Type" set to "Tasa".
   :highlight: The "SAT Tax Type" and "Factor Type" fields.
   :data: Demo company "YourCompany MX", Mexican localization installed.
   :module: l10n_mx
   :notes: English UI, light theme, 1440px width.

.. _l10n/mx/tax-config:

Cash basis taxes
----------------

The Mexican Localization uses :doc:`cash basis taxes <../../finance/accounting/taxes/cash_basis>`.
When registering a payment, Odoo carries out the movement of taxes from the *Cash Basis Transition
Account* to the account set in the :guilabel:`Definition` tab of the tax record set on the invoice
or bill line. For such movement, a tax base account is used: (:guilabel:`899.01.99 Base Imponible de
Impuestos en Base a Flujo de Efectivo`) in the journal entry when reclassifying taxes. **Do not
delete this account**.

Chart of accounts
=================

The chart of accounts follows the |SAT| grouping code structure (*código agrupador*): each account
code starts with the |SAT| group (e.g. `101.01` *Caja*), which makes it possible to build the
electronic accounting files from the general ledger outside Odoo. See the
:doc:`chart of accounts <../accounting/get_started/chart_of_accounts>` documentation for how to
add or edit accounts.

Employees
=========

With the *Employees - Mexico* module, the employee form gets the :guilabel:`CURP` and
:guilabel:`RFC` fields (Private Information tab, after the passport number), so that the identifiers required by the Mexican
authorities are stored with the employee.

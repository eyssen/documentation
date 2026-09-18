=======
Belgium
=======

.. _belgium/configuration:

Configuration
=============

Install the :guilabel:`🇧🇪 Belgium` :ref:`fiscal localization package
<fiscal_localizations/packages>` to get all the default accounting features of the Belgian
localization, following the :abbr:`IFRS(International Financial Reporting Standards)` rules.

.. seealso::
   :doc:`Documentation on e-invoicing’s legality and compliance in Belgium
   <../accounting/customer_invoices/electronic_invoicing/belgium>`

.. note::
   The Belgian versions of the financial reports (balance sheet, profit & loss, tax report, partner
   VAT listing, EC sales list, Intrastat declaration), the disallowed expenses report, the fee forms
   281.50 / 325, the CODA / SODA statement imports (including CodaBox and Codaclean) and the
   certified POS system with the Fiscal Data Module (black box) are **not** available in this
   edition. The generic :doc:`financial reports <../accounting/reporting>` and the
   :doc:`Intrastat declaration <../accounting/reporting/intrastat>` can be used instead.

.. _belgium/coa:

Chart of accounts
=================

You can reach the :guilabel:`Chart of accounts` by going to :menuselection:`Accounting -->
Configuration --> Accounting: Chart of Accounts`.

The Belgian chart of accounts includes pre-configured accounts as described in the :abbr:`PCMN(Plan
Comptable Minimum Normalisé)`. To add a new account, click :guilabel:`New`. A new line appears. Fill
it in, click :guilabel:`Save`, and then :guilabel:`Setup` to configure it further.

.. seealso::
   :doc:`../accounting/get_started/chart_of_accounts`

.. _belgium/taxes:

Taxes
=====

Default Belgian taxes are created automatically when the :guilabel:`Belgium - Accounting` module
is installed. Each tax is mapped to the grids of the Belgian VAT return, which are used by the
:doc:`tax report <../accounting/reporting/dynamic_reports>`.

In Belgium, the standard VAT rate is **21%**, but there are lower rates for some categories of goods
and services. An intermediate rate of **12%** is applied on social housing and food served in
restaurants, while a reduced rate of **6%** applies to most basic goods, such as food, water supply,
books, and medicine. A **0%** rate applies to some exceptional goods and services, such as some
daily and weekly publications, as well as recycled goods.

.. _belgium/non-deductible:

Non-deductible taxes
--------------------

In Belgium, some taxes are not fully deductible, such as taxes on the maintenance of cars. This
means a part of these taxes is considered as an expense.

In Odoo, you can configure non-deductible taxes by creating tax rules for these taxes and linking
them to the corresponding accounts. This way, the system automatically calculates the taxes and
allocates them to the appropriate accounts.

To configure a new non-deductible tax, go to :menuselection:`Accounting --> Configuration -->
Accounting: Taxes`, and click :guilabel:`New`:

#. :guilabel:`Add a line` and select :guilabel:`Base` in the :guilabel:`Based On` column;
#. :guilabel:`Add a line`, then select :guilabel:`on tax` in the :guilabel:`Based on` column and
   enter the **non-deductible** percentage in the :guilabel:`%` column;
#. On the :guilabel:`of tax` line, select the :guilabel:`Tax Grid(s)` related to your tax;
#. :guilabel:`Add a line` with the **deductible** percentage in the :guilabel:`%` column;
#. Set :guilabel:`of tax` in :guilabel:`Based On`;
#. Select :guilabel:`411000 VAT recoverable` as account, and select the related tax grid.

Once you have created a non-deductible tax, you can apply it to your transactions by selecting the
appropriate tax during the encoding of bills and credit notes. The system automatically calculates
the tax amount and allocates it to the corresponding accounts based on the tax rules configured.

.. example::
   With the Belgian localization, the **21% car** tax is created by default (50% non-deductible).

   .. screenshot:: finance-fl-belgium-deductible-tax
      :menu: Accounting ‣ Configuration ‣ Taxes ‣ "21% car"
      :shows: The tax form of the default Belgian "21% car" purchase tax, Definition tab: the distribution lines for invoices – Base (100%), "on tax" 50% non-deductible to the expense account, "of tax" 50% deductible to 411000 VAT recoverable – with their tax grids.
      :highlight: The two "of tax" distribution lines and their percentages.
      :data: Demo company "YourCompany BE", Belgian localization installed.
      :module: l10n_be, account
      :notes: English UI, light theme, 1440px width.

.. seealso::
  - :doc:`Taxes <../accounting/taxes>`
  - :doc:`../accounting/reporting/tax_returns`

Electronic invoicing
====================

Odoo supports the **Peppol BIS Billing 3.0 (UBL)** electronic invoicing format. To enable it for a
customer, go to :menuselection:`Accounting --> Customers --> Customers`, open their contact form,
and under the :guilabel:`Accounting` tab, select the :guilabel:`Peppol BIS Billing 3.0` format.

.. seealso::
   :doc:`../accounting/customer_invoices/electronic_invoicing`

.. _belgium/cash-discount:

Cash discount
=============

In Belgium, if an early payment discount is offered on an invoice, the tax is calculated based on
the discounted total amount, whether the customer benefits from the discount or not.

To apply the right tax amount and report it correctly in your VAT return, set the tax reduction as
:guilabel:`Always (upon invoice)`.

.. seealso::
   :doc:`../accounting/customer_invoices/cash_discounts`

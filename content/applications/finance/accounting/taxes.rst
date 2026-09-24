:show-content:

=====
Taxes
=====

There are numerous types of **taxes**, and their application varies greatly, depending mostly on
your company's localization. To make sure they are recorded with accuracy, Odoo's tax engine
supports all kinds of uses and computations.

.. _taxes/default:

Default taxes
=============

**Default taxes** define which taxes are automatically selected when creating a new product. They
are also used to prefill the :guilabel:`Taxes` field when adding a new line on an invoice in
:ref:`Accounting Firms <accounting/fiduciaries>` mode.

.. screenshot:: accounting-taxes-default-taxes-product
   :menu: Accounting ‣ Customers ‣ Products ‣ New
   :shows: New product form, "General Information" tab; the "Sales Taxes" field is prefilled with the default sales tax (e.g., "27%").
   :highlight: The "Sales Taxes" field (red frame).
   :data: Demo company "YourCompany HU" with the Hungarian chart of accounts; default sales tax "27%".
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the upper part of the form.

To change your **default taxes**, go to :menuselection:`Accounting --> Configuration --> Settings`,
scroll to the :guilabel:`Taxes` section, select the appropriate :guilabel:`Sales Tax` and
:guilabel:`Purchase Tax` in the :guilabel:`Default Taxes` setting, and click :guilabel:`Save`.

In the same setting, the :guilabel:`Prices` field defines whether the sales prices used on products
and invoices are :guilabel:`Tax Excluded` or :guilabel:`Tax Included` by default. This setting can
no longer be changed once a journal entry has been created.

.. screenshot:: accounting-taxes-default-taxes-settings
   :menu: Accounting ‣ Configuration ‣ Settings
   :shows: Settings page scrolled to the "Taxes" section; "Default Taxes" setting with the "Sales Tax", "Purchase Tax" and "Prices" fields, and the "Rounding Method" setting next to it.
   :highlight: The "Default Taxes" setting block (red frame).
   :data: Demo company "YourCompany HU"; Sales Tax "27%", Purchase Tax "27%", Prices "Tax Excluded".
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the Taxes section.

The :guilabel:`Rounding Method` setting defines how the total tax amount is computed on orders and
invoices: :guilabel:`Round per Line` or :guilabel:`Round Globally`. Rounding per line is advised if
your prices are tax-included, so that the sum of the line subtotals equals the total with taxes.

.. note::
   **Default taxes** are automatically set up according to the country selected at the creation of
   your database, or when you set up a :ref:`fiscal localization package
   <fiscal_localizations/packages>` for your company.

.. _taxes/list_activation:

Activate taxes from the list view
=================================

As part of your :ref:`fiscal localization package <fiscal_localizations/packages>`, most of your
country's sales taxes are already preconfigured on your database. However, only a few taxes are
activated by default. To activate taxes relevant to your business, go to :menuselection:`Accounting
--> Configuration --> Taxes` and enable the toggle button under the :guilabel:`Active` column.

.. screenshot:: accounting-taxes-list-activation
   :menu: Accounting ‣ Configuration ‣ Taxes
   :shows: Taxes list view (default Sale and Purchase filters) with the "Active" toggle column; some taxes active, some inactive (greyed out).
   :highlight: The "Active" column (red frame).
   :data: Demo company "YourCompany HU" with the Hungarian taxes.
   :module: account
   :notes: English UI, light theme, 1440px width.

.. tip::
   Use the :guilabel:`Active` and :guilabel:`Inactive` filters to display only the active or the
   deactivated taxes, and group the list by :guilabel:`Tax Type` or :guilabel:`Tax Scope`.

.. _taxes/configuration:

Configuration
=============

To edit or create a **tax**, go to :menuselection:`Accounting --> Configuration --> Taxes` and open
a tax or click on :guilabel:`New`.

.. screenshot:: accounting-taxes-tax-form
   :menu: Accounting ‣ Configuration ‣ Taxes ‣ (open a tax)
   :shows: Tax form of a 27% sales tax: Tax Name, Tax Computation, Active, Tax Type, Tax Scope, Amount fields; "Definition" tab with the "Distribution for Invoices" and "Distribution for Refunds" tables.
   :data: Demo company "YourCompany HU"; tax "27%" (Sales, Percentage, 27%).
   :module: account
   :notes: English UI, light theme, 1440px width.

Basic options
-------------

.. _taxes/name:

Tax name
~~~~~~~~

The **tax name** is displayed for backend users in the :guilabel:`Taxes` field in
:doc:`sales orders <../../sales/sales>`, :doc:`invoices <customer_invoices>`, product forms, etc.

.. _taxes/computation:

Tax computation
~~~~~~~~~~~~~~~

- **Group of Taxes**

  The tax is a combination of multiple sub-taxes. You can add as many taxes as you want, in the
  order you want them to be applied.

  .. important::
     Make sure that the tax sequence is correct, as the order in which they are may impact the
     taxes' amounts computation, especially if one of the taxes :ref:`affects the base of the
     subsequent ones <taxes/base-subsequent>`.

- **Fixed**

  The tax has a fixed amount in the default currency. The amount remains the same, regardless of the
  sales price.

.. example::
   A product has a sales price of $1000, and we apply a $10 *fixed* tax. We then have:

   +-------------+-------------+----------+----------+
   | Product     | Price       | Tax      | Total    |
   | sales price | without tax |          |          |
   +=============+=============+==========+==========+
   | 1,000       | 1,000       | 10       | 1,010.00 |
   +-------------+-------------+----------+----------+

- **Percentage**

  The *sales price* is the taxable basis: the tax amount is computed by multiplying the sales price
  by the tax percentage.

.. example::
   A product has a sales price of $1000, and we apply a *10%* :guilabel:`Percentage` tax. We then
   have:

   +-------------+-------------+----------+----------+
   | Product     | Price       | Tax      | Total    |
   | sales price | without tax |          |          |
   +=============+=============+==========+==========+
   | 1,000       | 1,000       | 100      | 1,100.00 |
   +-------------+-------------+----------+----------+

- **Percentage Tax Included**

  The **total** is the taxable basis: the tax amount is a percentage of the total.

.. example::
   A product has a Sales Price of $1000, and we apply a *10%* :guilabel:`Percentage Tax Included`
   tax. We then have:

   +-------------+-------------+----------+----------+
   | Product     | Price       | Tax      | Total    |
   | sales price | without tax |          |          |
   +=============+=============+==========+==========+
   | 1,000       | 1,000       | 111.11   | 1,111.11 |
   +-------------+-------------+----------+----------+

- **Custom Formula**

  The tax amount is computed by a formula entered in the :guilabel:`Formula` field, which appears
  when this computation is selected. The formula can use the `base` (the amount on which the tax is
  applied), `price_unit` and `quantity` values, as well as the `product` fields.

  .. note::
     This option requires the *Define Taxes as Python Code* (`account_tax_python`) module.

.. example::
   :guilabel:`Formula`: `price_unit * 0.10`

.. _taxes/active:

Active
~~~~~~

Only **active** taxes can be added to new documents.

.. important::
   It is not possible to delete taxes that have already been used. Instead, you can deactivate them
   to prevent future use.

.. note::
   This field can be modified from the :ref:`list view <taxes/list_activation>`.

.. _taxes/scope:

Tax type
~~~~~~~~

The :guilabel:`Tax Type` determines the tax application, which also restricts where it is displayed.

- :guilabel:`Sales`: Customer invoices, product customer taxes, etc.
- :guilabel:`Purchases`: Vendor bills, product vendor taxes, etc.
- :guilabel:`None`

.. tip::
   You can use :guilabel:`None` for taxes that you want to include in a :ref:`Group of Taxes
   <taxes/computation>` but that you do not want to list along with other sales or purchase taxes.

Tax scope
~~~~~~~~~

The :guilabel:`Tax Scope` restricts the use of taxes to a type of product, either **goods** or
**services**.

.. _taxes/definition-tab:

Definition tab
--------------

Allocate with precision the amount of the taxable basis or percentages of the computed tax to
multiple accounts and tax grids. The distribution is defined separately for invoices
(:guilabel:`Distribution for Invoices`) and refunds (:guilabel:`Distribution for Refunds`).

.. screenshot:: accounting-taxes-definition-tab
   :menu: Accounting ‣ Configuration ‣ Taxes ‣ (open a tax) ‣ Definition tab
   :shows: "Definition" tab with the "Distribution for Invoices" and "Distribution for Refunds" tables; one "Base" line and one "of tax" line (100%) each, with the tax account and the tax grids.
   :highlight: The "Based On", "Account" and "Tax Grids" columns (red frame).
   :data: Demo company "YourCompany HU"; tax "27%" with tax account "467 Fizetendő ÁFA".
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the tab.

- :guilabel:`%`: the percentage of the base or of the tax amount allocated by the line.
- :guilabel:`Based On`:

  - :guilabel:`Base`: the price on the invoice line
  - :guilabel:`of tax`: a percentage of the computed tax.

- :guilabel:`Account`: if defined, an additional journal item is recorded.
- :guilabel:`Tax Grids`: used to generate :doc:`tax reports <reporting/tax_returns>`
  automatically, according to your country's regulations.
- :guilabel:`Tax Closing Entry`: when enabled, the line is included in the tax closing entry.

.. _taxes/advanced-tab:

Advanced options tab
--------------------

.. _taxes/label-invoices:

Label on invoices
~~~~~~~~~~~~~~~~~

The tax label is displayed on each invoice line in the :guilabel:`Taxes` column. This is visible to
*front-end* users on exported invoices, in customer portals, etc.

.. screenshot:: accounting-taxes-invoice-label
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (open a posted invoice) ‣ Preview
   :shows: Invoice PDF/portal preview; the invoice lines' "Taxes" column shows the tax's "Label on Invoices" value.
   :highlight: The "Taxes" column (red frame).
   :data: Demo company "YourCompany HU"; tax "27%" with Label on Invoices "27%".
   :module: account
   :notes: English UI, light theme, crop to the invoice lines table.

Description
~~~~~~~~~~~

An internal description of the tax, displayed in the tax selector and when searching for taxes.

Legal notes
~~~~~~~~~~~

The :guilabel:`Legal Notes` are printed on the invoices that use the tax (e.g., the legal reason for
a VAT exemption or for a reverse charge).

.. _taxes/tax-group:

Tax group
~~~~~~~~~

Select which **tax group** the tax belongs to. The tax group name is the displayed above the
**total** line on exported invoices and in customer portals.

Tax groups include different iterations of the same tax. This can be useful when you must record
the same tax differently according to :doc:`fiscal positions <taxes/fiscal_positions>`.

.. example::

   .. screenshot:: accounting-taxes-invoice-tax-group
      :menu: Accounting ‣ Customers ‣ Invoices ‣ (open a posted invoice) ‣ Preview
      :shows: Invoice to an intra-community customer; the line's Taxes column shows "0% EU S", and the totals block shows the tax group "VAT 0%" above the "Total" line.
      :highlight: The "0% EU S" label and the "VAT 0%" tax group line (red frames).
      :data: Belgian demo company, intra-community customer with the "Intra-Community B2B" fiscal position.
      :module: account, l10n_be
      :notes: English UI, light theme, crop to the lines and the totals block.

   In the example above, the :guilabel:`0% EU S` tax for intra-community customers in Europe records
   the amount on specific accounts and tax grids. However, it remains a 0% tax to the customer. This
   is why the label indicates :guilabel:`0% EU S`, and the tax group name above the
   :guilabel:`Total` line indicates :guilabel:`VAT 0%`.

.. important::
   Taxes have three different labels, each one having a specific use. Refer to the following table
   to see where they are displayed.

   +------------------+-------------------------+-------------------------+
   | :ref:`Tax Name   | :ref:`Label on Invoice  | :ref:`Tax Group         |
   | <taxes/name>`    | <taxes/label-invoices>` | <taxes/tax-group>`      |
   +==================+=========================+=========================+
   | Backend          | :guilabel:`Taxes` column| Above the               |
   |                  | on exported invoices    | :guilabel:`Total` line  |
   |                  |                         | on exported invoices    |
   +------------------+-------------------------+-------------------------+

.. _taxes/analytic-cost:

Include in analytic cost
~~~~~~~~~~~~~~~~~~~~~~~~

With this option activated, the tax amount is assigned to the same **analytic account** as the
invoice line.

.. _taxes/included-in-price:

Included in price
~~~~~~~~~~~~~~~~~

The :guilabel:`Included in Price` field overrides the company's default (the :guilabel:`Prices`
field of the :ref:`Default Taxes <taxes/default>` setting) for this tax. Leave it empty to use the
company's default, or select :guilabel:`Tax Included` or :guilabel:`Tax Excluded`.

With :guilabel:`Tax Included`, the total (including the tax) equals the **sales price**.

`Total = Sales Price = Computed Tax-Excluded price + Tax`

.. example::
   A product has a sales price of $1000, and we apply a *10%* :guilabel:`Percentage` tax, which is
   *included in the price*. We then have:

   +-------------+-------------+----------+----------+
   | Product     | Price       | Tax      | Total    |
   | sales price | without tax |          |          |
   +=============+=============+==========+==========+
   | 1,000       | 900.10      | 90.9     | 1,000.00 |
   +-------------+-------------+----------+----------+

.. note::
   If you need to define prices accurately, both tax-included and tax-excluded, please refer to the
   following documentation: :doc:`taxes/B2B_B2C`.

.. note::
   On customer invoices, the :guilabel:`Amount` column of the invoice lines shows the tax-excluded
   amount if the company's default :guilabel:`Prices` setting is :guilabel:`Tax Excluded`, and the
   tax-included amount if it is :guilabel:`Tax Included`.

.. _taxes/base-subsequent:

Affect base of subsequent taxes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With this option, the total tax-included becomes the taxable basis for the other taxes applied to
the same product.

You can configure a new :ref:`group of taxes <taxes/computation>` to include this tax or add it
directly to a product line.

.. screenshot:: accounting-taxes-subsequent-line
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (open a draft invoice)
   :shows: Invoice line with two taxes "Ecotax 5%" and "21%"; the totals block shows the 21% tax computed on the price plus the eco-tax.
   :highlight: The line's Taxes field and the tax amounts in the totals block (red frames).
   :data: Belgian demo company; product sold at 1,000; taxes "Ecotax 5%" (Affect Base of Subsequent Taxes) and "21%".
   :module: account
   :notes: English UI, light theme, crop to the lines and the totals block.

.. warning::
   The order in which you add the taxes on a product line has no effect on how amounts are computed.
   If you add taxes directly on a product line, only the tax sequence determines the order in which
   they are applied.

   To reorder the sequence, go to :menuselection:`Accounting --> Configuration --> Taxes`, and drag
   and drop the lines with the handles next to the tax names.

   .. screenshot:: accounting-taxes-list-sequence
      :menu: Accounting ‣ Configuration ‣ Taxes
      :shows: Taxes list view with the drag handles in the first column; the "Ecotax 5%" tax placed above the "21%" tax.
      :highlight: The drag handles (red frame).
      :data: Belgian demo company; taxes "Ecotax 5%" and "21%".
      :module: account
      :notes: English UI, light theme, crop to the top of the list.

Extra taxes
===========

"Extra taxes" is a broad term referring to additional taxes beyond the standard or basic taxes
imposed by governments. These extra taxes can be **luxury** taxes, **environmental** taxes,
**import** or **export duties** taxes, etc.

.. note::
   The method to compute these taxes varies across different countries. We recommend consulting your
   country's regulations to understand how to calculate them for your business.

To compute an extra tax in Odoo, :ref:`create a tax <taxes/configuration>`, enter a tax name, select
a :ref:`Tax Computation <taxes/configuration>`, set an :guilabel:`Amount`, and in the
:guilabel:`Advanced Options` tab, check :guilabel:`Affect Base of Subsequent Taxes`. Then, drag and
drop the taxes in the :ref:`order they should be computed <taxes/base-subsequent>`.

.. example::
   - In Belgium, the formula to compute an environmental tax is: `(product price + environmental
     tax) x sales tax`. Therefore, our environmental tax has to come *before* the sales tax in the
     computation sequence.
   - In our case, we created a 5% environmental tax (Ecotax) and put it *before* the Belgian base
     tax of 21%.

   .. screenshot:: accounting-taxes-ecotax
      :menu: Accounting ‣ Configuration ‣ Taxes ‣ (open the Ecotax tax) ‣ Advanced Options tab
      :shows: Tax form of the "Ecotax 5%" tax on the "Advanced Options" tab, with "Affect Base of Subsequent Taxes" enabled.
      :highlight: The "Affect Base of Subsequent Taxes" checkbox (red frame).
      :data: Belgian demo company; tax "Ecotax 5%".
      :module: account
      :notes: English UI, light theme, 1440px width.

UNECE tax codes
===============

With the *Account Tax UNECE* (`account_tax_unece`) module, taxes can be classified according to the
nomenclature of the United Nations Economic Commission for Europe (UNECE). The codes are used when
generating structured electronic invoices (e.g., UBL or CII). The module adds two fields to the
:guilabel:`Advanced Options` tab of the tax form:

- :guilabel:`UNECE Tax Type`: the tax type code (UNECE DataElement 5153, e.g., `VAT`);
- :guilabel:`UNECE Tax Category`: the tax category code (UNECE DataElement 5305, e.g., `S` for
  standard rate, `E` for exempt).

Both fields can also be displayed as optional columns in the list of taxes.

.. screenshot:: accounting-taxes-unece-fields
   :menu: Accounting ‣ Configuration ‣ Taxes ‣ (open a tax) ‣ Advanced Options tab
   :shows: "Advanced Options" tab of the tax form with the "UNECE Tax Type" (VAT) and "UNECE Tax Category" (S) fields below the checkbox options.
   :highlight: The two UNECE fields (red frame).
   :data: Demo company "YourCompany HU"; tax "27%".
   :module: account, account_tax_unece
   :notes: English UI, light theme, 1440px width, crop to the tab.

.. seealso::
  - :doc:`taxes/fiscal_positions`
  - :doc:`taxes/B2B_B2C`

.. toctree::
   :titlesonly:

   taxes/cash_basis
   taxes/retention
   taxes/vat_verification
   taxes/fiscal_positions
   taxes/eu_distance_selling
   taxes/B2B_B2C

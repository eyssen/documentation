======
Brazil
======

.. _localizations/brazil/modules:

Modules
=======

The following modules related to the Brazilian localization are available:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Brazilian - Accounting`
     - `l10n_br`
     - Brazilian :ref:`fiscal localization package <fiscal_localizations/packages>`, complete with
       the Brazilian chart of accounts, taxes, tax grids, fiscal positions, and document and
       identification types (CNPJ, CPF).
   * - :guilabel:`Brazil - Sale`
     - `l10n_br_sales`
     - Brazilian layout of the sales order in the customer portal (tax totals per tax group).
   * - :guilabel:`Brazil - Website Sale`
     - `l10n_br_website_sale`
     - eCommerce adjustments for Brazil: prices are shown tax included, and the business (B2B)
       fields such as the identification number are always shown at checkout.

.. note::
   The localization's core modules are installed automatically with the localization. The rest can
   be manually :doc:`installed </applications/general/apps_modules>`.

   Tax computation through Avalara AvaTax, the electronic documents (NF-e, NFS-e, NFC-e) issued
   through AvaTax, the Brazilian accounting reports, and the subscription extension are **not**
   available in this edition. Taxes are computed by the standard tax engine from the taxes
   configured on products and fiscal positions.

.. _localizations/brazil/loc-review:

Localization overview
=====================

The Brazilian localization package ensures compliance with Brazilian fiscal and accounting
regulations. It includes tools for managing taxes, fiscal positions, reporting, and a predefined
chart of accounts tailored to Brazil’s standards.

The Brazilian localization package provides the following key features to ensure compliance with
local fiscal and accounting regulations:

- :ref:`Chart of accounts <localizations/brazil/chart-of-accounts>`: a predefined structure tailored
  to Brazilian accounting standards
- :ref:`Taxes <localizations/brazil/taxes>`: pre-configured tax rates, including standard VAT,
  zero-rated, and exempt options.
- :ref:`Fiscal positions <localizations/brazil/fiscal-positions>` for internal and interstate
  operations.
- :doc:`Reporting <../accounting/reporting>`

.. _localizations/brazil/chart-of-accounts:

Chart of accounts
-----------------

In the :doc:`chart of accounts <../accounting/get_started/chart_of_accounts>`, the accounts are
mapped automatically to their corresponding taxes, and the default account payable and account
receivable fields.

.. note::
   The Brazil chart of accounts is based on the SPED CoA, which provides a baseline of the necessary
   accounts.

.. _localizations/brazil/taxes:

Taxes
-----

:doc:`Taxes <../accounting/taxes>` are automatically created and configured when installing the
Brazilian localization: IPI, ICMS, PIS, COFINS, ISS, IR and CSLL taxes with their tax grids.

Taxes used for services must be manually added and configured, as the rate may differ depending on
the city where the service is offered.

Brazilian taxes have three additional options on the tax form (visible for Brazilian companies
only):

- :guilabel:`Discount this Tax in Price`: the tax amount is deducted from the price;
- :guilabel:`Redution`: percentage reduction of the tax base;
- :guilabel:`MVA Percent`: the *Margem de Valor Agregado* percentage used for the ICMS-ST
  base.

.. screenshot:: finance-fl-brazil-tax-form
   :menu: Accounting ‣ Configuration ‣ Taxes ‣ (an ICMS tax)
   :shows: The tax form of a Brazilian ICMS tax with the "Discount this Tax in Price", "Redution" and "MVA Percent" fields next to "Included in Price".
   :highlight: The three Brazil-specific fields.
   :data: Demo company "YourCompany BR", Brazilian localization installed.
   :module: l10n_br
   :notes: English UI, light theme, 1440px width.

.. _localizations/brazil/fiscal-positions:

Fiscal positions
----------------

Fiscal positions carry an :guilabel:`Interstate Fiscal Position Type` (:guilabel:`Internal`,
:guilabel:`South/Southeast selling to North/Northeast/Midwest`, or :guilabel:`Other interstate`)
so that the ICMS taxes of interstate operations can be mapped correctly. Assign the fiscal position
to the customer or vendor, or let Odoo detect it automatically from the partner's state.

.. _localizations/brazil/company-and-contacts:

Company and contacts
====================

The following fields should be filled in on the
:doc:`company record </applications/general/companies>`:

- :guilabel:`Name`
- :guilabel:`Address`: add :guilabel:`City`, :guilabel:`State`, :guilabel:`Zip Code`,
  :guilabel:`Country`

  - In the :guilabel:`Street` field, enter the street name, number, and any additional address
    information.
  - In the :guilabel:`Street 2` field, enter the neighborhood.

- :guilabel:`Identification Number`: :guilabel:`CNPJ` or :guilabel:`CPF`
- :guilabel:`Tax ID`: associated with the identification type
- :guilabel:`IE`: State registration
- :guilabel:`IM`: Municipal registration
- :guilabel:`SUFRAMA code`: Superintendence of the Manaus Free Trade Zone - add if applicable
- :guilabel:`Phone`
- :guilabel:`Email`

In the :guilabel:`Sales and Purchase` tab, add the :ref:`Fiscal Position
<localizations/brazil/fiscal-positions>` that applies to the partner.

.. tip::
   If it is a simplified regime, the ICMS rate must be configured. To do so, go to
   :menuselection:`Accounting --> Configuration --> Settings`, scroll down to the :guilabel:`Taxes`
   section, and set the :guilabel:`Sales Tax` and :guilabel:`Purchase Tax` fields in the
   :guilabel:`Default Taxes` section.

The same configuration applies to the relevant :doc:`contact <../../essentials/contacts>` form.

.. screenshot:: finance-fl-brazil-partner-fields
   :menu: Contacts ‣ (a Brazilian company contact)
   :shows: A contact form for a Brazilian company: Identification Number type "CNPJ" with the Tax ID, and the "IE", "IM" and "SUFRAMA code" fields; the address with Street, Street 2 (neighborhood), City, State, Zip and Country.
   :highlight: The "IE", "IM" and "SUFRAMA code" fields.
   :data: Contact "Empresa Exemplo Ltda", CNPJ 12.345.678/0001-95, São Paulo.
   :module: l10n_br
   :notes: English UI, light theme, 1440px width.

.. note::
   Select the :guilabel:`Company` option for a contact with a tax ID (CNPJ), or check
   :guilabel:`Individual` for a contact with a CPF.


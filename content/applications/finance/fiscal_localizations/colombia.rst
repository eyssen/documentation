========
Colombia
========

.. |DIAN| replace:: :abbr:`DIAN (Dirección de Impuestos y Aduanas Nacionales)`
.. |NIT| replace:: :abbr:`NIT (El Número de Identificación Tributaria)`

Odoo's Colombian localization package provides the base accounting features for databases in
Colombia: the PUC chart of accounts, taxes and withholdings, and the identification document types.

.. _localization/colombia/configuration:

Configuration
=============

.. _localization/colombia/modules:

Modules installation
--------------------

:ref:`Install <general/install>` the following modules to get all the features of the Colombian
localization:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Colombia - Accounting`
     - `l10n_co`
     - Default :ref:`fiscal localization package <fiscal_localizations/packages>`. This module adds
       the base accounting features for the Colombian localization: chart of accounts, taxes,
       withholdings, and identification document type.
   * - :guilabel:`Colombian - Point of Sale`
     - `l10n_co_pos`
     - This module includes **Point of Sale** receipts for Colombian localization (installed
       automatically with the Point of Sale app). It also lets you edit the :guilabel:`Order
       Reference` sequence in the Point of Sale settings.

.. note::
   Electronic invoicing with the |DIAN| (own software or Carvajal), the support documents for vendor
   bills, and the withholding certificates (*Certificado de Retención en ICA / IVA / Fuente*) are
   **not** available in this edition.

.. _localization/colombia/configuration/company:

Company information
-------------------

To configure your company information:

#. Access your company's contact form:

   - Go to the :guilabel:`Contacts` app and search for your company or;
   - Go to the :guilabel:`Settings` app, activate the :ref:`developer mode <developer-mode>`, and in
     the :guilabel:`Companies` section, click :guilabel:`Update Info`. Then, in the
     :guilabel:`Contact` field, click on the company name.

#. Configure the following information:

   - :guilabel:`Company Name`.
   - :guilabel:`Address`: Including :guilabel:`City`, :guilabel:`Department`, and :guilabel:`ZIP`
     code.
   - :guilabel:`Identification Number`: Select the :guilabel:`Identification Type` (:guilabel:`NIT`,
     :guilabel:`Cédula de Ciudadanía`, :guilabel:`Registro Civil`, etc.). When the
     :guilabel:`Identification Type` is :guilabel:`NIT`, the
     :guilabel:`Identification Number` **must** have the *verification digit* at the end of the ID
     prefixed by a hyphen (`-`).

.. screenshot:: finance-fl-colombia-company-identification
   :menu: Contacts ‣ (your company)
   :shows: The company's contact form with the "Identification Number" type drop-down open (NIT, Cédula de Ciudadanía, Cédula de Extranjería, Registro Civil, Pasaporte, …) and a NIT with the verification digit "900.123.456-7".
   :highlight: The identification type and number fields.
   :data: Demo company "YourCompany CO", Colombian localization installed.
   :module: l10n_co, l10n_latam_base
   :notes: English UI, light theme, 1440px width.

Master data
-----------

.. _localization/colombia/contacts:

Contacts
~~~~~~~~

Configure the following fields on the :doc:`contact form <../../essentials/contacts>`:

- :guilabel:`Identification Number` (VAT): Select the identification number type and enter the
  identification number. If the identification number type is :guilabel:`NIT`, the identification
  number must include the verification digit at the end, prefixed by a hyphen (`-`). The number is
  validated only for the :guilabel:`NIT` type.

.. _localization/colombia/taxes:

Taxes
~~~~~

Taxes are created automatically by the localization: IVA at the different rates, INC, and the
withholding taxes (*retenciones* ICA, IVA and Fuente, as negative purchase taxes). To create or
modify taxes, go to :menuselection:`Accounting --> Configuration --> Taxes`, and select the related
tax.

.. screenshot:: finance-fl-colombia-taxes
   :menu: Accounting ‣ Configuration ‣ Taxes
   :shows: The Taxes list of the Colombian localization with the IVA 19%, IVA 5%, INC and the negative "Rte" withholding taxes (ReteFuente, ReteIVA, ReteICA).
   :data: Demo company "YourCompany CO".
   :module: l10n_co
   :notes: English UI, light theme, 1440px width.

.. _localization/colombia/chart-of-accounts:

Chart of accounts
~~~~~~~~~~~~~~~~~

The :doc:`chart of accounts </applications/finance/accounting/get_started/chart_of_accounts>` is
installed by default as part of the localization module. The accounts are mapped automatically in
taxes, default account payable, and default account receivable. The chart of accounts for Colombia
is based on the PUC (Plan Unico de Cuentas).

.. _localization/colombia/workflows:

Multicurrency
-------------

The official exchange rate for Colombia is provided by the `Banco de la República
<https://suameca.banrep.gov.co/estadisticas-economicas/>`_. Currency rates can be updated
automatically with the *eYssen currency rate updater* module (see
:ref:`multi-currency/config-rates-auto`); the Banco de la República is not among its providers, so
the rates come from a generic provider (e.g., xe.com) or must be entered manually.

=========
Guatemala
=========

.. |SAT| replace:: :abbr:`SAT (Superintendencia de Administración Tributaria)`

.. _guatemala/intro:

Introduction
============

The Guatemalan localization provides the chart of accounts and the taxes required to keep the
books of a company in Guatemala according to the rules of the |SAT|.

.. note::
   Electronic invoicing (FEL) through the Infile provider — the electronic FACT / FCAM / FPEQ /
   NCRE / NDEB / NABN / FCAP documents, the export complement, and the related company fields such
   as the establishment code and phrases — is **not** available in this edition. Electronic
   documents must be issued through the SAT portal or a certified provider outside Odoo.

Glossary
--------

The following terms are used throughout the Guatemalan localization:

- **SAT**: *Superintendencia de Administración Tributaria* is the government entity responsible for
  enforcing tax payments in Guatemala.
- **FEL**: *Factura Electrónica en Línea* is the electronic invoicing system mandated by the SAT in
  Guatemala, which requires businesses to issue and manage electronic documents in compliance with
  local regulations.
- **Quetzal**: The official currency of Guatemala, represented by the symbol GTQ. This is the base
  currency for all financial transactions in the Guatemalan localization.

Configuration
=============

Modules installation
--------------------

:ref:`Install <general/install>` the following module to get the features of the Guatemalan
localization:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Guatemala - Accounting`
     - `l10n_gt`
     - Default :ref:`fiscal localization package <fiscal_localizations/packages>`: chart of
       accounts and taxes. Installed automatically for Guatemalan companies.

Company
-------

To configure your company information, open the **Settings** app, scroll down to the
:guilabel:`Companies` section, click :guilabel:`Update Info`, and configure the following:

- :guilabel:`Company Name`
- :guilabel:`Address`, including the :guilabel:`Street`, :guilabel:`City`, :guilabel:`State`,
  :guilabel:`ZIP`, and :guilabel:`Country`
- :guilabel:`Tax ID`: Enter the company's NIT.

Multi-currency
~~~~~~~~~~~~~~

The official currency exchange rate in Guatemala is provided by the Bank of Guatemala. Currency
rates can be updated automatically with the *eYssen currency rate updater* module (see
:ref:`multi-currency/config-rates-auto`); the Bank of Guatemala is not among its providers, so the
rates come from a generic provider (e.g., xe.com) or must be entered manually.

.. seealso::
   :doc:`Multi-currencies <../accounting/get_started/multi_currency>`

Master data
-----------

Chart of accounts
~~~~~~~~~~~~~~~~~

The :doc:`chart of accounts <../accounting/get_started/chart_of_accounts>` is installed by default
as part of the set of data included in the localization module, the accounts are mapped
automatically in taxes, default accounts payable, and default accounts receivable.

Accounts can be added or deleted according to the company's needs.

Contacts
~~~~~~~~

The following fields should be completed on contact forms:

- :guilabel:`Company Name`
- :guilabel:`Address`, including the :guilabel:`Street`, :guilabel:`City`, :guilabel:`State`,
  :guilabel:`ZIP`, and :guilabel:`Country`
- :guilabel:`Tax ID`: the contact's NIT (or CUI for individuals).

Taxes
~~~~~

As part of the Guatemala localization module, taxes are automatically created with their
configuration and related financial accounts: the 12 % VAT on sales and purchases, and the ISR (5 %) and VAT (12 %) withholding taxes.

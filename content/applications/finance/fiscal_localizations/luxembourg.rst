==========
Luxembourg
==========

.. _localizations/luxembourg/modules:

Modules
=======

The following modules are installed automatically with the Luxembourgish localization:

.. list-table::
   :header-rows: 1

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Luxembourg - Accounting`
     - `l10n_lu`
     - Default :ref:`fiscal localization package <fiscal_localizations/packages>`

.. note::
   The Luxembourgish country-specific reports (the monthly/quarterly and annual VAT declarations
   for the eCDF platform and the FAIA audit file export) are **not** available in this edition. The
   grids of the VAT declaration can be reviewed in the :doc:`tax report
   <../accounting/reporting/dynamic_reports>`.

.. note::
   In some cases, such as when upgrading to a version with additional modules, it is possible that
   modules may not be installed automatically. Any missing modules can be manually :ref:`installed
   <general/install>`.

.. seealso::
   :doc:`Documentation on e-invoicing’s legality and compliance in Luxembourg
   <../accounting/customer_invoices/electronic_invoicing/luxembourg>`

.. _localizations/luxembourg/overview:

Localization overview
=====================

The Luxembourgish localization includes the following features:

- :doc:`../accounting/get_started/chart_of_accounts`: a predefined set of accounts that follows the
  current official accounting standards (PCN 2020)
- :ref:`localizations/luxembourg/taxes`: pre-configured tax rates, including standard (17%),
  reduced (14%, 8%, and 3%) and zero-rated VAT, intra-community, and zero-rated export taxes
- :doc:`../accounting/taxes/fiscal_positions`: automated account and tax adjustments based on
  customer or supplier
- :ref:`localizations/luxembourg/e-invoicing`: E-invoicing with Peppol

.. _localizations/luxembourg/taxes:

Taxes
-----

The following :doc:`taxes <../accounting/taxes>` are available by default with the Luxembourgish
localization package:

- standard VAT (17%): applied to most goods and services within Luxembourg
- reduced VAT (14%, 8%, and 3%): applied to some goods and services within Luxembourg
- zero-rated VAT: applied to goods and services not subject to VAT
- intra-community VAT: applied to goods and services sold to or purchased from VAT-registered
  persons located in other EU countries
- export tax (0%): zero-rated tax applied to goods and services exported outside Luxembourg

.. _localizations/luxembourg/e-invoicing:

E-invoicing
-----------

Odoo users in Luxembourg can register on the :ref:`accounting/e-invoicing/peppol` network, which
allows exchanging e-invoices and credit notes with other participants on the network.

The e-invoice format in Luxembourg is **BIS Billing 3.0**.

.. important:: E-invoicing via Peppol is mandatory for all B2G transactions in Luxembourg.

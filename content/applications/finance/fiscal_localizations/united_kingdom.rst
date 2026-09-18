==============
United Kingdom
==============

.. _localization/united-kingdom/modules:

Configuration
=============

:ref:`Install <general/install>` the :guilabel:`UK - Accounting` module to get the features of
the UK localization.

.. list-table::
   :header-rows: 1

   * - Name
     - Technical name
     - Description
   * - :guilabel:`UK - Accounting`
     - `l10n_uk`
     -  - CT600-ready chart of accounts
        - VAT100-ready tax structure
        - Infologic UK counties listing

.. note::
   The UK accounting reports, the Making Tax Digital (MTD-VAT) submission to HMRC, the BACS
   payment files, the Construction Industry Scheme (CIS) deductions and monthly returns, and the
   Employment Hero payroll connector are **not** available in this edition. The VAT100 boxes can be
   reviewed in the :doc:`tax report <../accounting/reporting/dynamic_reports>` and submitted to
   HMRC through bridging software.

.. seealso::
   - `HM Revenue & Customs <https://www.gov.uk/government/organisations/hm-revenue-customs/>`_
   - `Overview of Making Tax Digital
     <https://www.gov.uk/government/publications/making-tax-digital/overview-of-making-tax-digital/>`_

.. _localization/united-kingdom/chart-of-account:

Chart of accounts
=================

The UK chart of accounts is included in the :guilabel:`UK - Accounting` module. Go to
:menuselection:`Accounting --> Configuration --> Accounting: Chart of Accounts` to access it.

Set up your :abbr:`CoA (chart of accounts)` and import your initial balances as described in the
:doc:`chart of accounts <../accounting/get_started/chart_of_accounts>` documentation.

.. _localization/united-kingdom/taxes:

Taxes
=====

As part of the localization module, UK taxes are created automatically with their related financial
accounts and configuration.

Go to :menuselection:`Accounting --> Configuration --> Settings --> Taxes` to update the
:guilabel:`Default Taxes`.

To edit existing taxes or to :guilabel:`Create` a new tax, go to :menuselection:`Accounting -->
Configuration --> Accounting: Taxes`.

.. seealso::
   :doc:`taxes <../accounting/taxes>`

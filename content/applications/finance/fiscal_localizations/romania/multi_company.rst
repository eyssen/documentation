=====================================
Romanian and Hungarian companies
=====================================

The eYssen Hungarian modules and the Romanian localization can be installed in the same database,
together with companies of other countries (for example Spain). This page explains how the
companies coexist, and what to check before going live.

How Odoo decides that a company is Hungarian
============================================

The Hungarian features (invoice layouts, NAV, *KVTD*, POS receipts, assets and so on) only apply to
a company if it is considered Hungarian. Odoo checks, in this order:

#. the **fiscal country** of the company (:menuselection:`Accounting --> Configuration --> Settings`,
   :guilabel:`Taxes` section, :guilabel:`Fiscal Country`);
#. if it is empty, the **country of the registered office** of the company;
#. if both are empty, whether the company uses the Hungarian (`hu`) chart of accounts.

The Romanian features work the other way: they only apply to a company whose fiscal country is
Romania.

.. important::
   Set the fiscal country on every company. The address is only used as a fallback.

Effects on the Hungarian features
=================================

For a company that is not Hungarian:

- The Hungarian logic on invoices is skipped: the narration, the exchange rate note, the invoice
  appearance type, the electronic signature, the delivery date, the payment term details, the
  storno mirror, the NAV send and the foreign VAT journal rules.
- The Hungarian fiscal position checks and the goods/services tax mapping are skipped.
- The NAV export wizard does not apply.
- No *KVTD* lines are generated, and the fixed assets have no *TAO* board.
- The POS receipt does not show the *Not a fiscal document!* header.
- The :guilabel:`Cash Register Disabled` option (company setting, shown on the form of the cash
  journals for account managers) turns off the eYssen cash register. When the cash register is
  installed as a dependency of `l10n_ro_cash` on an existing database, it is switched on
  automatically for the non-Romanian companies that already have entries. Their cash journals work
  as in standard Odoo. See :doc:`cash`.
- The default exchange rate provider is chosen from the fiscal country first, then from the address
  country. The MNB provider is only proposed for Hungarian companies (see :doc:`exchange_rates`).

Document layouts
================

The Hungarian layouts of the invoice, sales order, purchase order and portal are kept as they are
for Hungarian companies. The documents of the other companies are printed with the standard Odoo
(*core*) layout. If a print contains documents of Hungarian and non-Hungarian companies, each
document uses its own layout.

In the core layout, the Hungarian layout views and the customizations that extend them are
skipped. Views of the `l10n_ro` modules that extend these templates only apply to the core layout.

.. note::
   Custom views that extend the Hungarian layout templates (for example
   `eyssen_l10n_hu.report_invoice_document`), or that use an XPath on a node created by them, only
   apply to the Hungarian layout and are skipped in the core layout. A customization meant for the
   documents of all the companies must extend the standard Odoo template and must not depend on a
   Hungarian node.

Menus
=====

The Romanian menus are shown to the users who have the :guilabel:`Romanian Localization User`
group. It is granted automatically to the internal users who have access to a Romanian company, and
removed automatically (only if it was granted automatically) when they no longer have access.

.. caution::
   The menus are cached. After changing the fiscal country of a company, the menus are not
   refreshed immediately. Reload the page, or sign out and in again.

Check the data before go-live
=============================

The script `scripts/check_fiscal_country.py` is read-only. It lists the companies where the new
country logic could behave differently from the previous one. Run it either in the Odoo shell:

.. code-block:: console

   $ odoo-bin shell -d <database> --no-http < scripts/check_fiscal_country.py

or remotely:

.. code-block:: console

   $ ODOO_PASSWORD=... python3 scripts/check_fiscal_country.py --url <url> --db <database> --user admin

Add `--json` for a machine-readable output. In the remote mode, the exit code is 0 if nothing has
to be fixed, 1 if there are findings, and 2 for a connection error. The findings are:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Finding
     - Meaning
   * - `EMPTY_FISCAL_COUNTRY`
     - The company has no fiscal country.
   * - `HU_CHART_NOT_HU`
     - The company uses the Hungarian chart, but its fiscal country is not Hungary.
   * - `HU_ADDRESS_NOT_HU`
     - The company address is in Hungary, but its fiscal country is not (legitimate only for a
       foreign VAT setup).

The output also shows whether the Hungarian logic still applies after the upgrade. Fix the findings
in the :guilabel:`Fiscal Country` setting of the accounting settings.

Upgrade
=======

Update the eYssen modules on all databases when you go live, then restart. The country guards are
in the eYssen Hungarian modules and in the modules that depend on them (among them
`eyssen_l10n_hu`, `eyssen_l10n_hu_asset`, `eyssen_l10n_hu_kvtd`, `eyssen_l10n_hu_pos`,
`eyssen_cashregister` and `eyssen_currency_rate_live_community`).

The `l10n_ro` core module (version 1.3) has two eYssen migrations, which run on update:

Version 1.2 (VAT)
   The VAT on payment taxes get the right signs on the tax report, so they are no longer negative.
   The 50% non-deductible taxes also report their full base and VAT on the :doc:`D300 <d300>` rows
   24 and 25. Only the taxes of the Romanian chart that still have the original tags are changed,
   and only the new entries use the new tags; the posted entries are not changed. See
   :doc:`nondeductible_vat`.

Version 1.3 (account types)
   The types of the contra-assets accounts (28x, 29x) and of the 475x and 478x accounts are
   corrected, for the accounts created from the Romanian chart template. The balance sheets then
   classify these accounts correctly, also for past periods when you run the reports again. Printed
   or filed documents of closed periods are not changed. The accounts whose balance was moved to
   the result by a posted closing entry are not changed, and a warning is written in the log
   (`l10n_ro 1.3`). Review them and set the account type by hand in the chart of accounts.

Checklist
=========

#. Each company has a fiscal country.
#. `scripts/check_fiscal_country.py` returns no findings, or the findings are understood.
#. The eYssen modules are updated.
#. The log contains no `l10n_ro 1.3` warning, or the accounts were reviewed.
#. Users of the Romanian companies have the :guilabel:`Romanian Localization User` group, and the
   menus are reloaded.
#. A document of each company type (Hungarian, Romanian, other) is printed and checked.
#. A Hungarian partner invoiced from a Romanian company has a valid EU VAT number: the fiscal
   position detection of that company uses the standard Odoo VAT check, not the Hungarian rule.

.. seealso::
   - :doc:`../romania`
   - :doc:`../hungary`

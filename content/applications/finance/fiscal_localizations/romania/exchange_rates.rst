==================
BNR exchange rates
==================

The :guilabel:`Romania - BNR exchange rates` (`l10n_ro_currency_rate_bnr`) module adds the
reference exchange rates of the *Banca Națională a României* (BNR, National Bank of Romania) to the
:ref:`automatic currency rate update <multi-currency/config-rates-auto>`, loads the historical
rates, and applies the rule of article 290 of the Fiscal Code to the rate of foreign-currency
invoices.

.. _localizations/romania/bnr-provider:

BNR as the rate provider
========================

Go to :menuselection:`Accounting --> Configuration --> Settings` and, in the :guilabel:`Update
currency exchange rates` setting (displayed when the :guilabel:`Multi-Currencies` option is
enabled), select :guilabel:`National Bank of Romania (BNR)` in the :guilabel:`Provider` field. Set
the :guilabel:`Interval`, then use the refresh icon next to :guilabel:`Next run` to update the
rates immediately.

Odoo reads the rates published by BNR on its last banking day and stores them with their
**publication date**. On weekends and bank holidays BNR publishes nothing, so no new rate is
created for those days. The rates that BNR quotes per several units of a currency (for example
100 HUF or 100 JPY) are converted to the rate of one unit. If the currency of the company is not
the RON, the rates are converted through the RON.

Default provider by country
---------------------------

The default provider of a company depends on its **fiscal country** (or on the country of its
address if the fiscal country is not set). It is only a default: a provider that you chose is
never overwritten.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Fiscal country
     - Default provider
   * - Romania
     - :guilabel:`National Bank of Romania (BNR)`
   * - Hungary
     - :guilabel:`Hungarian National Bank` (MNB), with the `eyssen_currency_rate_live_mnb_community`
       module installed
   * - Other countries
     - :guilabel:`European Central Bank`, unless the country has its own provider (for example,
       India or the United Arab Emirates)

When the BNR module is installed, and when the Romanian chart of accounts is loaded for a company,
the Romanian companies that are still on an automatic default (no provider or the European Central
Bank, and, at installation, MNB) are switched to BNR once. Companies of other countries are not
touched.

.. note::
   The :guilabel:`Hungarian National Bank` (MNB) provider is no longer the default of every new
   company: it is only the default of Hungarian companies. A company of another country that
   needs it has to select it. The provider already stored on existing companies is kept.

Loading the historical rates
----------------------------

When BNR is the selected provider, a :guilabel:`BNR Range Load` button is displayed in the
setting. Click it, then fill in the :guilabel:`Import BNR exchange rates` dialog:

#. Set :guilabel:`From` and :guilabel:`To` (:guilabel:`To` is today by default).
#. Tick :guilabel:`Overwrite existing rates` to replace the rates that already exist for the same
   day and the same currency. Otherwise, the existing rates are kept.
#. Click :guilabel:`Import`.

The rates are downloaded from the yearly archives of BNR, which start in 2005. The period cannot
start before 2005 and cannot span more than 10 calendar years. The rates are stored for the main
company of the group (the branches share them) and dated with the publication date.

.. _localizations/romania/rate-date-rule:

Rate of foreign-currency invoices (article 290)
===============================================

According to article 290 of the Fiscal Code, the taxable amount of an invoice in a foreign
currency is converted into lei with the last exchange rate communicated by BNR **before** the day
on which the VAT becomes chargeable (article 282): the delivery date, or the invoice date if the
invoice is issued earlier. BNR publishes its rates around 13:00, and the rate published on day D
applies to the operations of day D+1.

The :guilabel:`Invoice exchange rate date (Romania)` setting (displayed for Romanian companies
when the :guilabel:`Multi-Currencies` option is enabled) offers two rules:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Option
     - Rate used on the invoice
   * - :guilabel:`Last rate published before the VAT chargeable date` (default)
     - The rate dated on or before the day **preceding** the chargeable date. The chargeable date
       is the :guilabel:`Delivery Date` of the invoice if it is set and earlier than the invoice
       date, otherwise the invoice date.
   * - :guilabel:`Rate of the invoice date (standard)`
     - The standard Odoo behavior: the rate of the invoice date.

For example, with the default rule, an invoice dated Tuesday uses the rate published on Monday,
and an invoice dated Monday uses the rate published on the previous Friday, since BNR publishes
nothing on weekends.

The rule applies to the invoices, credit notes and receipts of Romanian companies, and the date
used to find the rate is the :guilabel:`Exchange rate date` printed on the :doc:`invoice
<invoicing>`.

.. important::
   The rule finds the rate among the rates stored in the database. To get the exact BNR rate for
   an invoice, make sure that the rates of the previous days have been loaded: keep the automatic
   update enabled with a daily :guilabel:`Interval`, and use :guilabel:`BNR Range Load` to fill
   gaps or to load the rates before the first update.

.. seealso::
   - :doc:`invoicing`
   - :doc:`../romania`

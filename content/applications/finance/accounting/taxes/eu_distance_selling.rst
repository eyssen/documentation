===================================
EU intra-community distance selling
===================================

EU intra-community distance selling involves the cross-border trade of goods and services from
vendors registered for VAT purposes to individuals (B2C) located in a European Union member state.
The transaction is conducted remotely, typically through online platforms, mail orders, telephone,
or other means of communication.

EU intra-community distance selling is subject to specific VAT rules and regulations. The vendor
must charge VAT per the VAT rate applicable in the buyer's country.

.. note::
   This remains applicable even if the vendor is located outside of the European Union.

Configuration
=============

The **EU Intra-community Distance Selling** feature helps you comply with this regulation by
creating and configuring new **fiscal positions** and **taxes** based on your company's country. To
enable it, go to :menuselection:`Accounting --> Configuration --> Settings`, tick
:guilabel:`EU Intra-community Distance Selling` in the :guilabel:`Taxes` section, and
:guilabel:`Save`. This installs the *EU One Stop Shop (OSS)* (`l10n_eu_oss`) module.

.. screenshot:: accounting-taxes-eu-distance-selling-setting
   :menu: Accounting ‣ Configuration ‣ Settings
   :shows: "Taxes" section; "EU Intra-community Distance Selling" setting enabled, with the "Refresh tax mapping" button below it.
   :highlight: The setting block (red frame).
   :data: Demo company "YourCompany HU".
   :module: account, l10n_eu_oss
   :notes: English UI, light theme, 1440px width, crop to the setting.

.. tip::
   Whenever you add or modify taxes, you can automatically update your fiscal positions. To do so,
   go to :menuselection:`Accounting --> Configuration --> Settings`, and in the :guilabel:`EU
   Intra-community Distance Selling` setting of the :guilabel:`Taxes` section, click
   :guilabel:`Refresh tax mapping`.

.. note::
   We highly recommend checking that the proposed mapping is suitable for the products and services
   you sell before using it.

.. seealso::
   - :doc:`../taxes`
   - :doc:`../../fiscal_localizations`
   - :doc:`fiscal_positions`

One-Stop Shop (OSS)
===================

The :abbr:`OSS (One-Stop Shop)` system introduced by the European Union simplifies VAT collection
for **cross-border** sales of goods and services. It primarily applies to business-to-consumer
**(B2C)** cases. With the OSS, businesses can register for VAT in their home country and use a
single online portal to handle VAT obligations for their sales within the EU. There are **two
primary schemes**: the **Union OSS** scheme for cross-border services and the **Import OSS** scheme
for goods valued at or below €150.

The taxes created by the feature are linked to the **OSS tax grids**, so the OSS amounts can be
retrieved from the journal items and the tax reports of your country's fiscal localization.

.. seealso::
   - `European Commission: OSS | Taxation and Customs Union <https://ec.europa.eu/taxation_customs/business/vat/oss_en>`_

======================
EU OSS sales (Hungary)
======================

Hungarian companies registered in the EU :abbr:`OSS (One-Stop-Shop)` scheme charge the VAT of the
customer's member state on their distance sales and declare it in the quarterly OSS return on the NAV
OSS portal. The standard feature is described in :doc:`../../accounting/taxes/eu_distance_selling`.
The :guilabel:`Hungary - EU OSS Bridge` (`l10n_hu_oss`) module is installed automatically when
:guilabel:`EU Intra-community Distance Selling` is enabled in a database with the Hungarian
localization, and aligns the feature with the Hungarian invoicing rules:

- OSS invoices are issued in a **dedicated journal** and are **not reported to NAV Online Számla**;
- OSS taxes are excluded from the :doc:`Hungarian VAT return <vat_return>` and the VAT analytics
  (their :guilabel:`Alap % Áfa bevallásban` is set to `0` whenever the tax mapping is refreshed);
- a quarterly report summarizes the OSS sales per member state.

Configuration
=============

#. In :menuselection:`Accounting --> Configuration --> Settings --> Taxes`, enable :guilabel:`EU
   Intra-community Distance Selling`, tick :guilabel:`Company registered in EU OSS at
   oss.nav.gov.hu`, and click :guilabel:`Refresh tax mapping` to create the taxes and fiscal
   positions of the member states.
#. Create a sales journal for the OSS invoices. In :ref:`developer mode <developer-mode>`, open its
   :guilabel:`Journal Entries` tab and tick :guilabel:`EU OSS Journal` in the :guilabel:`Hungarian
   Invoicing` section. :guilabel:`No need to hand it over to the NAV!` is ticked automatically and
   becomes read-only.

.. note::
   The :guilabel:`Hungarian Invoicing` section is only visible in developer mode, on sales journals,
   when the :ref:`NAV data reporting <localizations/hungary/nav-settings>` is enabled.

Issue OSS invoices
==================

Create the customer invoice in the OSS journal. The fiscal position is set to the OSS fiscal
position of the **delivery address country** (or of the customer's country), so the lines get the
VAT rate of that member state. When the invoice is confirmed:

- an invoice with OSS taxes in a regular journal, an invoice without OSS taxes in the OSS journal,
  and an invoice mixing OSS and regular taxes are all refused;
- the invoice is marked :guilabel:`No need to hand it over to the NAV!` with the reason *EU OSS
  számla — nem kell NAV adatszolgáltatás*.

.. warning::
   The OSS fiscal positions are applied automatically to private customers of other member states on
   regular journals as well. Such an invoice cannot be confirmed until it is moved to the OSS
   journal (or its fiscal position and taxes are changed).

OSS report
==========

Go to :menuselection:`Accounting --> Reporting --> EU OSS Report` (accounting administrators),
select the :guilabel:`Year` and the :guilabel:`Quarter` (the previous quarter is proposed) and click
:guilabel:`Generate Report`. The lines show the :guilabel:`Country`, the :guilabel:`Type`
(:guilabel:`Goods` or :guilabel:`Services`), the :guilabel:`VAT Rate (%)`, the :guilabel:`Tax Base
(EUR)` and the :guilabel:`VAT Amount (EUR)` of the posted invoices and credit notes of the OSS
journals, with :guilabel:`Total Base` and :guilabel:`Total VAT`. The report is displayed on screen;
enter its figures in the OSS return on the NAV portal.

.. screenshot:: finance-fl-hungary-oss-report
   :menu: Accounting ‣ Reporting ‣ EU OSS Report
   :shows: The "EU OSS Quarterly Report" dialog after "Generate Report": year, quarter, result lines per country with type, VAT rate, tax base and VAT amount in EUR, and the totals.
   :highlight: The result lines (red frame).
   :data: Demo company "YourCompany HU"; Q2 with B2C sales to Germany (19%), Austria (20%) and Slovakia (23%).
   :module: l10n_hu_oss
   :notes: English UI, light theme, 1440px width, crop to the dialog.

.. important::
   Check the figures before filing. In the current module version, invoices dated on 31 December
   are missing from the fourth-quarter report, the proposed year is not decreased when the fourth
   quarter is proposed in January–March, and the amounts of invoices issued in a currency other than
   the company currency are converted incorrectly. The VAT amount is recomputed from the base and the
   rate, and the amounts are converted to EUR with the rate of the last day of the quarter stored in
   Odoo.

:show-content:
:show-toc:

=======
Hungary
=======

The Hungarian localization combines the standard :guilabel:`Hungary - Accounting` package with a set
of *eYssen* modules. Together they cover invoicing according to the Hungarian VAT Act, real-time
data reporting to the :abbr:`NAV (Nemzeti Adó- és Vámhivatal, National Tax and Customs
Administration)` *Online Számla* system, pro-forma and advance invoices, the VAT return (through
ÁNYK forms or the NAV eÁFA machine-to-machine interface), fixed assets, the auditor data export of
the Chamber of Hungarian Auditors (MKVK), the environmental product fee (KVTD), EU OSS sales and the
official exchange rates of the Hungarian National Bank (MNB).

.. _localizations/hungary/modules:

Modules
=======

:ref:`Install <general/install>` the following modules to get the features of the Hungarian
localization. Only the first two are required for invoicing; install the others according to the
needs of the company.

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Hungary - Accounting`
     - `l10n_hu`
     - Standard fiscal localization package: base data for Hungarian companies.
   * - :guilabel:`Magyar számlázás és NAV adatszolgáltatás`
     - `eyssen_l10n_hu`
     - Hungarian chart of accounts, journals, taxes and tax groups, invoice layout, Hungarian tax
       numbers on contacts, fulfillment date, corrective, aggregate and continuous-fulfillment
       invoices, and the :doc:`NAV Online Számla data reporting <hungary/nav_online_invoice>`.
   * - :guilabel:`Magyar számlázás (Pro-Forma)`
     - `eyssen_l10n_hu_proforma`
     - :doc:`Pro-forma invoices <hungary/proforma>` (*díjbekérő*) and advance invoices created from
       their payment.
   * - :guilabel:`eYssen Sale Stock Delivery Date`
     - `eyssen_l10n_hu_sale_stock_delivery_date`
     - Keeps the :ref:`fulfillment date <localizations/hungary/fulfillment-date>` rules of the
       localization when the *Inventory* and *Sales* apps are used together.
   * - :guilabel:`Magyar könyvelés és ÁNYK adatszolgáltatás`
     - `eyssen_l10n_hu_accountant`
     - Base of the :doc:`ÁNYK tax returns <hungary/vat_return>`, the VAT analytics report and
       :doc:`accounting tools <hungary/accounting_tools>` for accountants.
   * - :guilabel:`ABEV 2024`, :guilabel:`ABEV 2025`, :guilabel:`ABEV 2026`
     - `eyssen_l10n_hu_abev_24`, `eyssen_l10n_hu_abev_25`, `eyssen_l10n_hu_abev_26`
     - Yearly form packages of the VAT return (`2465`, `2565`, `2665`) and the EC recapitulative
       statement (`24A60`, `25A60`, `26A60`), exported as XML files that can be imported into ÁNYK.
   * - :guilabel:`Hungary - eVAT (eÁFA M2M) VAT Return`
     - `l10n_hu_evat`
     - :doc:`VAT return through the NAV eÁFA machine-to-machine interface <hungary/evat>`.
   * - :guilabel:`eYssen Hungarian Asset Localization`
     - `eyssen_l10n_hu_asset`
     - :doc:`Hungarian fixed asset accounting <hungary/assets>`: rate-based depreciation, corporate
       tax depreciation board, activation and disposal entries, protocols.
   * - :guilabel:`MKVK AuditXML adatexport (főkönyvi tételek)`
     - `l10n_hu_mkvk`
     - :doc:`General ledger data export for auditors <hungary/mkvk>` in the MKVK AuditXML format.
   * - :guilabel:`MKVK Audit XML export (készletleltár analitika)`
     - `l10n_hu_mkvk_stock`
     - Inventory analytics export for auditors in the MKVK Audit XML format.
   * - :guilabel:`Hungary - EU OSS Bridge`
     - `l10n_hu_oss`
     - :doc:`EU One-Stop-Shop sales <hungary/oss>` for Hungarian companies. Installed automatically
       with :guilabel:`EU Intra-community Distance Selling`.
   * - :guilabel:`KVTD`
     - `eyssen_l10n_hu_kvtd`
     - :doc:`Environmental product fee <hungary/kvtd>` (*környezetvédelmi termékdíj*) records on
       products and invoices.
   * - :guilabel:`Cashbook integráció`
     - `eyssen_l10n_hu_cashbook`
     - :doc:`Data transfer to the external Cashbook service <hungary/cashbook>`.
   * - :guilabel:`MNB (Magyar Nemzeti Bank) árfolyam szinkronizálás`
     - `eyssen_currency_rate_live_mnb_community`
     - :ref:`Official MNB exchange rates <localizations/hungary/mnb>`.
   * - :guilabel:`PoS Hungarian`
     - `eyssen_l10n_hu_pos`
     - Prints the line *Nem adóügyi bizonylat!* (not a fiscal receipt) in the header of every Point of
       Sale receipt.
   * - :guilabel:`eYssen Accountant - Hungarian Localization Bridge`
     - `eyssen_accountant_l10n_hu`
     - Installed automatically with the :doc:`cash register
       <../accounting/bank/cash_register>`: prints the Hungarian tax number and group tax number of
       the partner on payment receipts and cash vouchers.
   * - :guilabel:`Subscription Management - Hungarian Localization`
     - `l10n_hu_subscription`
     - Installed automatically with the *Subscriptions* app; see :ref:`continuous fulfillment on
       subscription invoices <localizations/hungary/subscription>`.

.. important::
   `eyssen_l10n_hu` replaces the standard :guilabel:`Hungary - E-invoicing` (`l10n_hu_edi`) module.
   The two modules cannot be installed together: installing `eyssen_l10n_hu` uninstalls
   `l10n_hu_edi` and disables its automatic installation.

.. _localizations/hungary/installation:

What changes at installation
----------------------------

When `eyssen_l10n_hu` is installed, the following is set up for every Hungarian company:

- The Hungarian language is activated, Hungary becomes a :guilabel:`Preferred` country (listed first
  in country selections), and the 20 Hungarian counties and the largest Hungarian banks are loaded.
- The Hungarian chart of accounts is loaded with the journals `KI` (customer invoices), `BE` (vendor
  bills), `EGYEB` (miscellaneous), `ARFKU` (exchange difference) and `CABA` (cash basis taxes), and
  27% default sales and purchase taxes. The customer invoice journal is secured with a hash (its
  entries are locked once posted) and uses a single number sequence for invoices, corrective
  invoices and credit notes.
- :guilabel:`Verify VAT Numbers` (VIES), :guilabel:`Cash Rounding` and tax rounding *globally* are
  enabled; the default invoicing policy of products becomes *Delivered quantities*; the standard
  :guilabel:`Pro-Forma Invoice` option of the Sales app is switched off and removed from the settings
  (see :doc:`hungary/proforma`).
- The payment terms :guilabel:`Cash`, :guilabel:`Card`, :guilabel:`Advance payment`,
  :guilabel:`Wire transfer, 8 day` and :guilabel:`Wire transfer, 30 day` are created. Existing
  payment terms without a :ref:`NAV payment method <localizations/hungary/payment-terms>` are set to
  *Egyéb* and **archived**.
- The unit of measure :guilabel:`Units` is renamed to *pcs* (*db*), the :ref:`NAV unit types
  <localizations/hungary/products>` are mapped and the imperial units are archived.
- The company name, address, tax numbers and registration number are written into the header and
  footer of the document layout.
- A to-do activity *NAV adatszolgáltatáshoz be kell állítani!* reminds the administrator to
  :ref:`configure the NAV data reporting <localizations/hungary/nav-settings>`.

.. _localizations/hungary/company:

Company
=======

Open :menuselection:`Settings --> Users & Companies --> Companies` and fill in the company's
address and the following fields, which replace the standard *Tax ID* field:

- :guilabel:`VAT Number`: the Hungarian tax number in the `12345678-1-12` format;
- :guilabel:`Group VAT Number`: for members of a VAT group only;
- :guilabel:`EU VAT Number`: the community tax number (for example, `HU12345678`);
- :guilabel:`Company ID`: the company registration number.

At least one bank account of the company must be recorded: a customer invoice cannot be confirmed
without a :guilabel:`Recipient Bank`. When the currency of an invoice or quotation changes, the first
company bank account in that currency is selected automatically.

.. screenshot:: finance-fl-hungary-company-form
   :menu: Settings ‣ Users & Companies ‣ Companies ‣ (company)
   :shows: Company form of a Hungarian company with the "VAT Number", "Group VAT Number" and "EU VAT Number" fields filled in, the "NAV Enable" toggle under "Company ID" and the "NAV Data Reporting" tab.
   :highlight: The three tax number fields (red frame).
   :data: Demo company "YourCompany HU", VAT Number "12345678-2-41", EU VAT Number "HU12345678", Budapest address.
   :module: eyssen_l10n_hu
   :notes: English UI, light theme, 1440px width, crop to the form sheet. Use fictitious tax numbers.

.. _localizations/hungary/contacts:

Contacts
========

On the contact form of companies located in Hungary, the standard *Tax ID* field is replaced by:

- :guilabel:`VAT Number`: the Hungarian tax number (`12345678-1-23`). The format and the check digit
  are verified; an invalid number is marked with a red ✕ and a warning.
- :guilabel:`Group VAT Number`: filled in automatically for members of a VAT group. If NAV reports
  that the partner is a group member but the full group number is not known, the warning *The
  Partner is a Group VAT payer! The Group VAT number must be provided, otherwise no invoice can be
  issued!* is displayed.
- :guilabel:`EU VAT Number`: the community tax number, available for companies of any country.
- :guilabel:`Co. Reg. Num.`: the company registration number.
- :guilabel:`KATA Taxpayer`, :guilabel:`Sole Trader` and :guilabel:`Sole Trader Reg. Num.`:
  informative fields for small taxpayers and sole traders (contacts located in Hungary).

Query the taxpayer data from NAV
--------------------------------

When the :ref:`NAV data reporting <localizations/hungary/nav-settings>` is enabled, entering the
first eight digits of the :guilabel:`VAT Number` is enough: Odoo queries the taxpayer from NAV and

- completes the tax number with the VAT code and the county code, and fills in the
  :guilabel:`Group VAT Number` if the partner belongs to a VAT group;
- loads the taxpayer's short or full name (legal forms are abbreviated, e.g., *Kft.*, *Zrt.*);
- loads the ZIP code, city and street of the registered seat.

Click the refresh icon next to the field (:guilabel:`Check`) to repeat the query at any time. The
options :guilabel:`Loading Taxpayer Name`, :guilabel:`Keep the manually set partner name` and
:guilabel:`Keep the manually set partner address` in the :ref:`NAV settings
<localizations/hungary/nav-settings>` control what the query may overwrite.

If another contact without a parent company already uses the same tax number, the banner *Another
partner is already registered with this tax number!* is shown with a :guilabel:`View the other
partner` link.

.. screenshot:: finance-fl-hungary-contact-vat
   :menu: Contacts ‣ (company contact)
   :shows: Contact form of a Hungarian company with "VAT Number" filled in and the refresh ("Check") icon next to it, "Group VAT Number", "EU VAT Number", "Co. Reg. Num.", and the "KATA Taxpayer" and "Sole Trader" checkboxes.
   :highlight: The "VAT Number" field with the refresh icon (red frame).
   :data: Contact "Minta Kft.", Budapest; VAT Number "12345678-2-41".
   :module: eyssen_l10n_hu
   :notes: English UI, light theme, 1440px width, crop to the upper part of the form. Use a fictitious tax number.

.. note::
   - The Hungarian tax number is shared with the child contacts of a company. On an *Invoice
     Address* contact, :guilabel:`Use as Company` (enabled by default) makes the invoice and the NAV
     data report use the tax number of the parent company.
   - The Hungarian :guilabel:`VAT Number` can only be recorded on company-type contacts.

Invoicing agreements
--------------------

In the :guilabel:`Accounting` tab of the contact, below :guilabel:`Fiscal Position`:

- :guilabel:`Aggregate Invoice Aggreement`: allows issuing :ref:`aggregate invoices
  <localizations/hungary/aggregate>` to the customer;
- :guilabel:`Electronic Invoice Aggreement`: the :ref:`invoice format
  <localizations/hungary/invoice-format>` of the customer's invoices defaults to *Electronic*.

.. _localizations/hungary/taxes:

Taxes, tax groups and fiscal positions
======================================

Tax groups
----------

The VAT data of the NAV report is taken from the **tax group** of the tax used on the invoice line.
Go to :menuselection:`Accounting --> Configuration --> Tax Groups` (the menu is visible without
:ref:`developer mode <developer-mode>` in Hungarian databases) and check the :guilabel:`NAV` section
of each group:

- :guilabel:`Amount %`: the VAT rate of the group, computed from its Hungarian taxes (0 for
  reverse-charge, exempt and out-of-scope groups);
- :guilabel:`Reversed`: domestic reverse charge (*fordított adózás*);
- :guilabel:`Az adómentesség jelölés kódja` (VAT exemption code): `AAM`, `TAM`, `KBAET`, `KBAUK`,
  `EAM`, `NAM` or `UNKNOWN`;
- :guilabel:`Az Áfa tv. hatályán kívüliség kódja` (out of the scope of the VAT Act): `ATK`,
  `EUFAD37`, `EUFADE`, `EUE`, `HO` or `UNKNOWN`;
- :guilabel:`Adóalap és felszámított adó eltérésének kódja` (VAT amount mismatch):
  `REFUNDABLE_VAT` or `NONREFUNDABLE_VAT`;
- :guilabel:`Különbözet szerinti jogcímek` (margin scheme): `TRAVEL_AGENCY`, `SECOND_HAND`,
  `ARTWORK` or `ANTIQUES`;
- :guilabel:`Legal Notes`: the reason text sent to NAV for exempt and out-of-scope items.

Only one of the four code fields can be set on a group. The labels of these fields are displayed in
Hungarian in the current module version.

.. important::
   Every product line of a customer invoice must carry **exactly one** tax, and the rate of the tax
   must equal the :guilabel:`Amount %` of its tax group; otherwise the invoice cannot be confirmed.
   Create one tax group per VAT rate.

.. screenshot:: finance-fl-hungary-tax-group
   :menu: Accounting ‣ Configuration ‣ Tax Groups ‣ (tax group)
   :shows: Tax group form with the "NAV" section ("Amount %", "Reversed", "Bi-Directional", the four NAV code fields, "Legal Notes") and the read-only "Taxes" list below.
   :highlight: The "NAV" section (red frame).
   :data: Tax group "ÁFA 27%" with Amount % 27; taxes "27%" (sales) and "27%" (purchases).
   :module: eyssen_l10n_hu
   :notes: English UI, light theme, 1440px width, crop to the form sheet. The NAV code labels are Hungarian.

Taxes
-----

The tax form (:menuselection:`Accounting --> Configuration --> Taxes`) contains three additional
options:

- :guilabel:`VTSZ is Required`: an invoice line with this tax can only be confirmed if a
  :ref:`customs tariff number (VTSZ) <localizations/hungary/products>` is set on the product
  (typically for domestic reverse-charge goods);
- :guilabel:`Nem készíthető Gyűjtőszámla ezzel az áfa kulccsal` (sales taxes): the tax cannot be used
  on :ref:`aggregate invoices <localizations/hungary/aggregate>`;
- :guilabel:`Alap % Áfa bevallásban` (purchase taxes, default `100`): the percentage of the tax base
  taken into account in the :doc:`VAT return <hungary/vat_return>` and in the VAT analytics, for
  partially deductible VAT.

A :guilabel:`Note` tab is available for internal remarks.

Fiscal positions
----------------

The fiscal positions *Domestic*, *EU Individual*, *EU Company*, *Non-EU* and *Cash Basis Taxes* are
created with the chart of accounts. In the :guilabel:`Tax Mapping` tab, the :guilabel:`Tax Scope`
column (:guilabel:`Services` or :guilabel:`Goods`) restricts a mapping line to service or goods
products; leave it empty to apply the line to both.

.. note::
   A Hungarian customer is never mapped automatically to the *EU Company* fiscal position, even if
   an EU VAT number is recorded on the contact.

.. _localizations/hungary/payment-terms:

Payment terms and cash rounding
===============================

On the payment term form (:menuselection:`Accounting --> Configuration --> Payment Terms`):

- :guilabel:`NAV Payment Method`: the payment method reported to NAV: *Banki átutalás* (transfer),
  *Készpénz* (cash), *Bankkártya, hitelkártya, egyéb készpénz helyettesítő eszköz* (card),
  *Utalvány, váltó, egyéb pénzhelyettesítő eszköz* (voucher) or *Egyéb* (other). Transfer is
  reported if nothing is set.
- The term's description is printed as :guilabel:`Payment method` on the invoice (*Wire transfer* by
  default).
- :guilabel:`Detailed description on the Invoice`: if filled in, it replaces the *Payment
  Communication* paragraph of the printed invoice. Use `%(invoice)s` for the invoice number and
  `%(amount)s` for the amount.
- On the term lines: :guilabel:`Invoice Note` (text of the installment on the invoice;
  placeholders `%(count)s`, `%(date)s`, `%(amount)s`), :guilabel:`Account Note` (label of the
  receivable journal item; placeholder `%(count)s`) and :guilabel:`Ignore in payment deadline` (the
  installment is skipped when the :guilabel:`Due Date` of the invoice is computed).

Cash rounding methods (:menuselection:`Accounting --> Configuration --> Cash Roundings`) can be
restricted with the :guilabel:`Payment Terms` and :guilabel:`Currency` fields (empty means *all*)
and ordered with the drag handle. On invoices, the first method matching the payment term and the
currency is selected automatically whenever the payment term or the currency changes. The method
*5 Ft-os kerekítés* (rounding to 5 HUF, for the :guilabel:`Cash` payment term in HUF) is created at
installation; set its :guilabel:`Profit Account` and :guilabel:`Loss Account` before using it.

.. _localizations/hungary/products:

Products and units of measure
=============================

The :guilabel:`General Information` tab of the product form contains the statistical codes printed
under the invoice lines and sent to NAV:

- goods: :guilabel:`VTSZ` (customs tariff number) and :guilabel:`KN` (Combined Nomenclature);
- services: :guilabel:`SZJ`, :guilabel:`TESZOR` and :guilabel:`Intermediated Service by Default`
  (invoice lines of the product are marked as :ref:`intermediated service
  <localizations/hungary/intermediated>` automatically).

The code lists are maintained by administrators in :menuselection:`Accounting --> Configuration -->
VTSZ, KN, SZJ, TESZOR`, under :guilabel:`Vámtarifaszám (VTSZ)` and :guilabel:`Kombinált
Nómenklatúra (KN)`. The VTSZ numbers of the goods subject to domestic reverse charge (cereals,
oilseeds, steel products) are preloaded.

.. note::
   There is no menu for the SZJ and TESZOR lists in the current module version; new codes can be
   created from the product form.

The NAV report requires a standard unit type for each unit of measure. Open
:menuselection:`Accounting --> Configuration --> Units Of Measure --> Units Of Measure Categories`
and check the :guilabel:`NAV volume unit types` column of the units: `PIECE`, `KILOGRAM`, `TON`,
`KWH`, `DAY`, `HOUR`, `MINUTE`, `MONTH`, `LITER`, `KILOMETER`, `CUBIC_METER`, `METER`,
`LINEAR_METER`, `CARTON`, `PACK` or `OWN` (own unit, reported with its name).

.. _localizations/hungary/journals:

Journals
========

The following options are available in the :guilabel:`Journal Entries` tab of journals
(:menuselection:`Accounting --> Configuration --> Journals`):

- :guilabel:`Invoice Format` (all journals): :guilabel:`Paper-based` or :guilabel:`Electronic`
  default :ref:`format <localizations/hungary/invoice-format>` of the invoices of the journal.
- :guilabel:`Foreign VAT (Külföldi adószám)` (sales journals): see :ref:`invoicing under a foreign
  VAT registration <localizations/hungary/foreign-vat>`.
- :guilabel:`Hungarian Invoicing` (sales journals, when the NAV data reporting is enabled; visible
  in :ref:`developer mode <developer-mode>` only): see :ref:`journals for invoices issued in another
  system <localizations/hungary/external-journal>`.

.. _localizations/hungary/mnb:

MNB exchange rates
==================

With the `eyssen_currency_rate_live_mnb_community` module, the :guilabel:`Magyar Nemzeti Bank`
provider is available for the :ref:`automatic currency rate update
<multi-currency/config-rates-auto>` in :menuselection:`Accounting --> Configuration -->
Settings --> Currencies`; it becomes the default provider of newly created companies. The official
rates are stored with the date on which MNB published them; on weekends and bank holidays the last
published rates are returned, so no new rate is created for those days.

When the provider is selected, the :guilabel:`MNB Range Load` button loads the historical rates of
all active currencies: set :guilabel:`Date from` and, optionally, :guilabel:`Date to` (today if
empty; the range cannot exceed 366 days) and click :guilabel:`Load`. Rates that already exist for a
currency and a date are not overwritten.

.. tip::
   The rate used on a foreign-currency invoice is the rate of the :ref:`fulfillment date
   <localizations/hungary/fulfillment-date>`, or today's rate if the fulfillment date is in the
   future. Credit notes and corrective invoices use the rate of the original invoice.

.. toctree::
   :titlesonly:

   hungary/nav_online_invoice
   hungary/invoicing
   hungary/proforma
   hungary/vat_return
   hungary/evat
   hungary/accounting_tools
   hungary/assets
   hungary/mkvk
   hungary/oss
   hungary/kvtd
   hungary/cashbook

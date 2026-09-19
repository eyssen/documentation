================================
MKVK data export for the auditor
================================

The Chamber of Hungarian Auditors (:abbr:`MKVK (Magyar Könyvvizsgálói Kamara)`) defines standard
XML formats in which accounting software hands over data to the auditor. Two exports are available:

- `l10n_hu_mkvk`: the **general ledger items** of a period in the *AuditXML* format (schema version
  1.0.23.0);
- `l10n_hu_mkvk_stock`: the **inventory analytics** at a cut-off date in the *Audit XML* format
  (schema version 19.0.1.6).

Both files are validated against the official XSD schema before they can be downloaded. The exports
can be created by users with the :guilabel:`Administrator` accounting access right; accountants can
view and download them.

Configuration
=============

In :menuselection:`Accounting --> Configuration --> Settings`, section :guilabel:`MKVK adatexport`:

- :guilabel:`MKVK short company name`: a short mnemonic used in the file names;
- :guilabel:`MKVK technical account`: an interposed account (e.g., `4999`) used to pair journal
  entries that have several debit **and** several credit lines. Its balance is zero within each
  entry. Without it, such entries cannot be exported;
- :guilabel:`MKVK opening journals`: entries of these journals are reported in period `0`
  (*Nyitás*);
- :guilabel:`MKVK closing journals`: entries of these journals are reported in period `13`
  (*Zárás*);
- :guilabel:`MKVK job number plan` and :guilabel:`MKVK cost center plan`: the analytic plans
  exported as job number and cost center.

Two optional fields refine the export:

- on taxes (:guilabel:`Advanced Options` tab), :guilabel:`MKVK VAT key` overrides the exported VAT
  key (e.g., `AM`, `AHK`); by default the integer tax percentage is exported;
- on contacts, :guilabel:`MKVK related party` marks related undertakings according to the Corporate
  Tax Act.

General ledger export
=====================

#. Go to :menuselection:`Accounting --> Reporting --> MKVK adatexport --> AuditXML_FkTet_export` and
   click :guilabel:`New`.
#. Set :guilabel:`Date From` and :guilabel:`Date To` and click :guilabel:`Generate XML`.
#. If the data is complete, the status becomes :guilabel:`Generated`; download the result with
   :guilabel:`Download XML` or :guilabel:`Download ZIP`
   (`AuditXML_FK_<short name>_<YYYYMM>-<YYYYMM>.xml`). Otherwise the export stays in draft and the
   errors are listed on the form; warnings do not block the export.
#. :guilabel:`Reset to draft` deletes the generated files so that the export can be repeated.

The file contains all **posted** journal entries of the company whose accounting date falls into the
period, from all journals, with the master data they use (journals, periods, accounts, partners,
users). Each item is exported as a debit–credit pair with amount, foreign currency amount and rate,
VAT base and VAT key, fulfillment date, due date, invoice reference, creator and analytic data.
Reversals within the period are marked as storno items. Opening balances are not computed: opening
entries are exported if they are booked in the period.

.. note::
   The company needs a valid Hungarian tax number, and its currency must be HUF, EUR, USD, GBP, JPY
   or CHF.

.. screenshot:: finance-fl-hungary-mkvk-export
   :menu: Accounting ‣ Reporting ‣ MKVK adatexport ‣ AuditXML_FkTet_export ‣ (export)
   :shows: MKVK export form in status "Generated" with the buttons "Download XML", "Download ZIP" and "Reset to draft", the "Date From" and "Date To" fields, the "XML file" and "ZIP file" links, and a warning box below.
   :highlight: The download buttons (red frame).
   :data: Demo company "YourCompany HU", period 2026-01-01 – 2026-06-30.
   :module: l10n_hu_mkvk
   :notes: English UI, light theme, 1440px width, crop to the form sheet.

Inventory analytics export
==========================

#. Post the inventory adjustments of the stocktaking **with the cut-off date**.
#. Go to :menuselection:`Accounting --> Reporting --> MKVK adatexport --> Audit XML export` and click
   :guilabel:`New`.
#. Set the :guilabel:`Cutoff Date` (*fordulónap*) and, optionally, the :guilabel:`Warehouses` (all
   warehouses of the company if empty), then click :guilabel:`Generate XML` and :guilabel:`Download
   XML` (`Audit_XML_keszlet_<short name>_<YYYYMMDD>.xml`).

The file lists the stock per product, internal location and lot/serial number at the end of the
cut-off day (Budapest time), with two quantities: the **book quantity** (without the inventory
adjustments dated on the cut-off day) and the **counted quantity** (including them). The unit value
is computed from the inventory valuation layers up to the cut-off date (the product cost is used if
there is none). Products, warehouses, locations and units of measure are exported as master data.

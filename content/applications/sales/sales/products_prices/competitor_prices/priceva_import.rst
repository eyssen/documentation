==============
Priceva import
==============

If you already follow your competitors with **Priceva**, the *Competitor Prices - Priceva Import*
module loads its Excel report: the product addresses on the competitor websites become listings, and
the prices go into the price history with the date of the report. Use it to start with the data you
have, or to get the prices of websites that block automated reading.

.. note::
   The import reads a file you export from Priceva; it does not connect to Priceva. It never changes
   a sales price: only competitor listings and the price history are written.

Export the report from Priceva as a **full export** in Excel format (.xlsx). Keep the file name:
Priceva puts the date and time of the export in it (for example
``priceva_report_full_..._2026_10_13_050218_full_export_yes_.xlsx``), and the import uses it as the
date of the prices.

Import a report
===============

Go to :menuselection:`Competitor Prices --> Configuration --> Priceva Import` and click
:guilabel:`New`.

.. screenshot:: sales-competitor-prices-priceva-import
   :menu: Competitor Prices ‣ Configuration ‣ Priceva Import ‣ (an import)
   :shows: A Priceva import form in the draft state with the information box, the File group (file,
      "Prices Valid On") and the Options group, and the Start Import button.
   :highlight: The Options group (red frame).
   :data: A Priceva full export file with 300 products.
   :notes: English UI, light theme, 1440px width.

:guilabel:`File`
   - :guilabel:`Priceva Export (.xlsx)`: the report.
   - :guilabel:`Prices Valid On`: the date of the export, read from the file name; correct it when
     the name was changed.

:guilabel:`Options`
   - :guilabel:`Match Products By`: the product field that holds the value of the report's *Code*
     column, :guilabel:`Internal reference` (default) or :guilabel:`Barcode`.
   - :guilabel:`Own Websites`: the domains of your own shops, separated by commas; their columns are
     skipped. The domains of your websites and of the company are filled in.
   - :guilabel:`Import Prices`: add the prices to the history. Switch it off to load only the
     addresses.
   - :guilabel:`Add New Addresses`: add the product addresses found in the report as listings, and
     create the websites that are not set up yet. Switch it off for an older report that should only
     fill in the price history.

Click :guilabel:`Start Import`. The import runs in batches; a scheduled job (*Competitor Prices:
continue Priceva imports*) continues it every 5 minutes, or press :guilabel:`Continue Now`. The form
shows the progress and, when it is done, the result: :guilabel:`Products Matched`, :guilabel:`Rows
Without Product`, :guilabel:`Listings Created`, :guilabel:`Prices Imported` and :guilabel:`Websites
Created`, and the :guilabel:`Codes Not Found` (the first 500).

What the import does
====================

- Each report row is a product, found by its *Code*. A column whose title is a website domain
  (``www.example.com``) holds the competitor's price and, as a hyperlink, the address of its product
  page. A price of 0 means that Priceva has no price. Tracking parameters (such as ``utm_source``)
  are removed from the addresses.
- For each website column a **confirmed listing** is created for the product, unless one exists, and
  the product is switched to :guilabel:`Track Competitor Prices`. A website that is not set up yet is
  created with :guilabel:`Fetching Active` switched **off**, a note says where it came from, and its
  terms of use are not reviewed. Review the terms and switch fetching on only for the websites you
  want to read yourself.
- The price is recorded with the method :guilabel:`Imported` and the date of the export.
- The recommendations of the touched products are recomputed.

Older reports and history
-------------------------

Import the reports in any order. When a newer report was already imported, or the listing already
has a newer price, the prices of the report are inserted into the history **before** the current
price: the current price does not change, and a price that equals its neighbour only extends it. To
fill in the history, import the older reports with :guilabel:`Add New Addresses` switched off.
Importing the same report again changes nothing.

Prices of imported listings are as old as the report. A recommendation uses only prices that are not
older than :guilabel:`Max. Price Age (days)` of the rule, so import a fresh report, or fetch the
website yourself, before relying on the recommendations.

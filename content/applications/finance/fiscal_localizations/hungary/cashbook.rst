====================
Cashbook integration
====================

`Cashbook <https://cashbook.hu>`_ is an external Hungarian online service that collects the invoices
of a business for bookkeeping and cash-flow follow-up. The :guilabel:`Cashbook integráció`
(`eyssen_l10n_hu_cashbook`) module transfers the invoices, credit notes and :doc:`pro-forma invoices
<proforma>` of the company to Cashbook automatically, as structured data together with the PDF, and
re-sends an invoice with its payment data whenever a payment is reconciled with it.

.. note::
   - This integration is not related to the :doc:`cash register
     <../../accounting/bank/cash_register>` (*házipénztár*) feature.
   - The module requires `eyssen_l10n_hu` and `eyssen_l10n_hu_proforma`. Its labels are displayed in
     Hungarian in the current module version.

Configuration
=============

Request an API key from Cashbook, then go to :menuselection:`Accounting --> Configuration -->
Settings`, section :guilabel:`Cashbook adatszolgáltatás` (the same fields are available in the
:guilabel:`CashBook adatszolgáltatás` tab of the company form):

- tick :guilabel:`Cashbook adatszolgáltatás`;
- :guilabel:`Üzemmód`: :guilabel:`Teszt üzemmód` (test system, the default) or :guilabel:`Éles
  adatszolgáltatás` (production);
- :guilabel:`Ne küldjük be a Cashbook-nak a számlákat. KIZÁRÓLAG TESZTELÉSRE!`: suspends the
  transfer, for testing;
- :guilabel:`Cashbook kulcs`: the API key.

.. screenshot:: finance-fl-hungary-cashbook-settings
   :menu: Accounting ‣ Configuration ‣ Settings
   :shows: Settings page scrolled to the "Cashbook adatszolgáltatás" section with the feature ticked, the mode selector, the testing switch and the "Login Details" block with the API key field.
   :highlight: The "Cashbook adatszolgáltatás" section (red frame).
   :data: Demo company "YourCompany HU"; mode "Teszt üzemmód".
   :module: eyssen_l10n_hu_cashbook
   :notes: Hungarian field labels (hardcoded), light theme, 1440px width, crop to the section. Use a throw-away secret; the key must not be readable.

At installation, a to-do activity *Cashbook adatszolgáltatáshoz be kell állítani!* is created on
every company. A copied (neutralized) database is switched to test mode with the transfer disabled.

.. important::
   Enter the API key right after installing the module. In the current module version, confirming a
   pro-forma invoice and reconciling a payment fail while the key is empty, even if the
   :guilabel:`Cashbook adatszolgáltatás` option is not ticked.

To exclude a whole journal (for example, a journal of invoices issued in another system), open it in
:ref:`developer mode <developer-mode>` and tick :guilabel:`Nem kell átadni a Cashbook-nak!` in the
:guilabel:`Hungarian Invoicing` section.

Transfer and follow-up
======================

Posted customer invoices, vendor bills and credit notes, as well as confirmed pro-forma invoices,
are queued when they are confirmed; a background job sends them about a minute later and retries
every five minutes. The PDF sent is the main attachment of the document, or the printed invoice.

The :guilabel:`CashBook` tab of the invoice and of the pro-forma invoice shows the
:guilabel:`Cashbook státusz`, which is also available as a column in the invoice, credit note and
pro-forma lists: *Beküldés folyamatban* (queued), *Beküldve* (sent), *Sikeresen feldolgozva*
(processed), or the error reported by Cashbook (for example, unreadable data, missing PDF, unknown
tax number, or missing permission for vendor bills). In :ref:`developer mode <developer-mode>`, the
tab contains the buttons :guilabel:`Beküldés a CashBook-ba`, :guilabel:`Azonnali beküldés a
CashBook-ba` and :guilabel:`Státusz ellenőrzés` for administrators.

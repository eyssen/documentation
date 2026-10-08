==============
Invoice layout
==============

The :guilabel:`Romania - Invoice Mentions` (`l10n_ro_invoice_report`) module adds the mentions
required on Romanian invoices by article 319 (20) of the Fiscal Code to the standard invoice PDF:
the identification data of the supplier and of the customer, the series and number of the invoice,
the *TVA la încasare* (VAT on collection) and *taxare inversă* (reverse charge) mentions, and the
exchange rate of invoices issued in a foreign currency.

The module is installed automatically with :guilabel:`Romania - Localization Base`
(`l10n_ro_base`, see :doc:`base`) and only changes the documents of companies whose **fiscal
country** is Romania. The invoices of the other companies of the database, for example the
Hungarian or Spanish ones, are printed as before.

.. _localizations/romania/invoice-mentions:

Mentions printed on the invoice
===============================

The mentions are added to the PDF (:guilabel:`Print` or :guilabel:`Send & Print`) of the invoices
and credit notes of Romanian companies, without any further configuration. The data comes from the
company, the customer and the invoice.

.. list-table::
   :header-rows: 1
   :widths: 25 45 30

   * - Mention
     - What is printed
     - Where to set it
   * - Supplier
     - Company name, :guilabel:`CUI` (the company's Tax ID), :guilabel:`Trade Register No.`
       (*Nr. Reg. Com.*, the NRC of the company's contact), :guilabel:`Share capital`, and the
       :guilabel:`IBAN` of the bank account of the invoice (otherwise the first bank account of the
       company) with the name of the bank.
     - Company :guilabel:`Tax ID` and :guilabel:`NRC` (see :ref:`localizations/romania/company`);
       :guilabel:`Share Capital` in the :ref:`Romanian Localization settings
       <localizations/romania/base-settings>`.
   * - Series and number
     - :guilabel:`Series`, :guilabel:`Number` and :guilabel:`Issue date` of the invoice.
     - Sequence of the journal (see below).
   * - Customer
     - :guilabel:`CUI` (when the Tax ID is not already printed in the address block),
       :guilabel:`Trade Register No.` and, for an individual, the :guilabel:`CNP`.
     - Tax ID and :guilabel:`NRC` of the customer; :guilabel:`CNP` field of the contact (see
       :ref:`localizations/romania/cnp`).
   * - *TVA la încasare*
     - The mention *TVA la încasare* (not translated, as it is a legal mention).
     - :guilabel:`VAT on Payment` setting, or a cash-basis tax (see below).
   * - *Taxare inversă*
     - The mention *Taxare inversă* (not translated).
     - Reverse-charge taxes (see below).
   * - Exchange rate
     - :guilabel:`BNR exchange rate`, :guilabel:`Exchange rate date`, :guilabel:`VAT amount in
       RON` and :guilabel:`Total in RON`.
     - Invoice currency (see below).

Series and number
-----------------

The series is the prefix of the journal sequence and the number is the running number that
follows it. An invoice numbered `FACT/2026/00012` is printed with the series `FACT/2026` and the
number `00012`. If the number of the invoice does not follow the sequence prefix of the journal,
the whole number is printed as :guilabel:`Number` and no series is shown.

.. _localizations/romania/vat-on-collection:

VAT on collection (*TVA la încasare*)
-------------------------------------

The mention *TVA la încasare* is printed on **customer invoices** in two cases:

- the company applies the VAT on collection system on the date of the invoice: tick
  :guilabel:`VAT on Payment` in the :ref:`Romanian Localization settings
  <localizations/romania/base-settings>` and, if the system applies only for a period, fill in
  :guilabel:`VAT on Payment From` and :guilabel:`VAT on Payment Until`;
- one of the taxes of the invoice lines is a cash-basis tax (:guilabel:`Tax Exigibility` set to
  :guilabel:`Based on Payment`), as the *VAT on collection* taxes of the Romanian chart of
  accounts are.

.. note::
   The :guilabel:`VAT on Payment` option of the company is the same flag as the one of the
   company's own contact in the *ANAF* register (see :ref:`localizations/romania/anaf-partners`):
   updating the company from ANAF also updates the option.

.. _localizations/romania/reverse-charge:

Reverse charge (*taxare inversă*)
---------------------------------

The mention *Taxare inversă* is printed when one of the taxes of the invoice lines requires it.
The taxes of the Romanian chart of accounts for which the customer owes the VAT are recognized
automatically: the *VAT Reverse Tax* tax (domestic simplification measures, article 331) and the
*Intra-Community VAT Delivery Services* tax (article 278 (2)).

To print the mention for another tax, open it in :menuselection:`Accounting --> Configuration
--> Taxes` and tick :guilabel:`Reverse Charge Mention (RO)` (displayed for the taxes of a Romanian
company, below :guilabel:`Label on Invoices`).

.. _localizations/romania/invoice-exchange-rate:

Exchange rate of foreign-currency invoices
------------------------------------------

When the currency of the invoice is not the currency of the company (RON), the invoice shows,
below the lines:

- the :guilabel:`BNR exchange rate`, as `1 EUR = 4.9767 RON` for example, with four decimals;
- the :guilabel:`Exchange rate date`, which is the date used to find the rate;
- the :guilabel:`VAT amount in RON` and the :guilabel:`Total in RON`, as article 319 (20) requires
  the VAT to be stated in lei. On a credit note, the amounts are printed with a negative sign.

The rate printed is the rate of the invoice. With the :doc:`BNR exchange rates module
<exchange_rates>`, it is the last rate published by the *Banca Națională a României* (BNR) before
the day on which the VAT becomes chargeable (article 290 of the Fiscal Code); otherwise it is the
standard rate of the invoice date. The mention is always titled :guilabel:`BNR exchange rate`,
whichever provider supplied the rate.

.. seealso::
   - :doc:`exchange_rates`
   - :doc:`nondeductible_vat`
   - :doc:`../romania`

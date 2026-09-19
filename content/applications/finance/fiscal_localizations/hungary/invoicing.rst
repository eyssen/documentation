===================
Hungarian invoicing
===================

The `eyssen_l10n_hu` module adapts customer invoices and vendor bills to the Hungarian VAT Act. The
features below are available for companies whose fiscal country is Hungary.

.. _localizations/hungary/fulfillment-date:

Fulfillment date
================

The :guilabel:`Fulfillment Date` (*teljesítés időpontja*) is displayed below the :guilabel:`Invoice
Date` on customer invoices, vendor bills and credit notes, and the :guilabel:`Accounting Date` is
always visible.

- On customer invoices, the accounting date must be equal to the fulfillment date. If they differ,
  the red banner *The Accounting Date is not the same as the Fulfillment Date!* is displayed and the
  invoice cannot be confirmed.
- If the fulfillment date is empty when :guilabel:`Confirm` is clicked, a :guilabel:`Fulfillment
  Date` dialog asks whether today can be used: :guilabel:`Yes, use today` or :guilabel:`No, keep
  editing`.
- When a sales order with *delivered quantities* products is invoiced, the accounting and
  fulfillment dates are set to the date of the latest delivery. With the
  `eyssen_l10n_hu_sale_stock_delivery_date` module, this also works together with the standard
  *effective date* logic of the Inventory app; the dates of posted invoices are never recomputed.
- Corrective invoices and credit notes always inherit the fulfillment date and the accounting date
  of the original invoice.
- The exchange rate of foreign-currency invoices is the rate of the fulfillment date (today's rate
  if the fulfillment date is in the future). The printed invoice repeats the VAT summary in HUF and
  shows the exchange rate.

A yellow banner *The invoice is not made out to the company, but to a contact or delivery address!*
warns when the selected customer is a child contact of a company.

.. screenshot:: finance-fl-hungary-invoice-form
   :menu: Accounting ‣ Customers ‣ Invoices ‣ New
   :shows: Draft customer invoice of a Hungarian company: "Invoice Date", "Fulfillment Date", "Accounting Date", "Payment terms", "Recipient Bank" on the right; "Continuous Fulfillment", "Aggregate Invoice" and "The invoice includes an intermediated service" checkboxes under "Reference"; the tabs "Invoice Lines", "Payment Dates", "Other Info", "Related Invoices".
   :highlight: The "Fulfillment Date" field and the three checkboxes (red frames).
   :data: Customer "Minta Kft." (with aggregate invoice agreement), one line "Consulting", 100,000 HUF + 27% VAT.
   :module: eyssen_l10n_hu
   :notes: English UI, light theme, 1440px width, crop to the form sheet.

.. _localizations/hungary/invoice-checks:

Checks at confirmation
======================

A **customer invoice** or credit note can only be confirmed if

- the customer has a country, ZIP code, city and street;
- a domestic company customer has a valid :ref:`Hungarian tax number
  <localizations/hungary/contacts>` (when the NAV data reporting is enabled), and an EU company
  customer has an EU VAT number that is valid in VIES;
- the fulfillment date is set and equals the accounting date;
- payment terms or a due date are set, and the due date is not earlier than the invoice date;
- the invoice date is **today** (the date of issue cannot be backdated or postdated);
- a :guilabel:`Recipient Bank` account is selected;
- every product line has exactly one tax whose rate matches its :ref:`tax group
  <localizations/hungary/taxes>`, and a VTSZ number if the tax requires it;
- a credit note refers to its original invoice (create it from the original invoice).

A **vendor bill** needs an invoice date, a fulfillment date and a :guilabel:`Bill Reference`.

A sales order of a Hungarian company cannot be confirmed without :guilabel:`Payment Terms`.

.. note::
   Some of these messages are displayed in Hungarian in the current module version.

.. _localizations/hungary/continuous:

Continuous fulfillment
======================

For periodic settlements (*folyamatos teljesítés*, Section 58 of the VAT Act), tick
:guilabel:`Continuous Fulfillment` on the draft invoice. The columns :guilabel:`Start of Period` and
:guilabel:`Fulfillment Date / End of Period` appear on the invoice lines; the end of the period is
mandatory on every product line. The copy icon next to a date copies it to all lines.

The :guilabel:`Fulfillment Date` of the invoice becomes read-only and is computed from the latest
end of period, the invoice date and the due date:

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Situation
     - Fulfillment date
   * - The due date is before the end of the period and the invoice is issued before the due date
     - Invoice date
   * - The due date is before the end of the period and the invoice is issued on or after the due
       date
     - End of the period
   * - The due date is the end of the period
     - End of the period
   * - The due date is after the end of the period, by no more than 60 days
     - Due date
   * - The due date is more than 60 days after the end of the period
     - End of the period + 60 days

The period (or the fulfillment date of the line) is printed under each invoice line, and the text
*Continuous fulfillment* is printed in the header of the invoice.

.. _localizations/hungary/subscription:

.. note::
   Invoices generated by the *Subscriptions* app are **not** marked as continuous fulfillment
   automatically. The `l10n_hu_subscription` module only stores the billed period on the invoice
   lines in technical fields that are not displayed; tick :guilabel:`Continuous Fulfillment` and
   check the line periods on the draft invoice before confirming it.

.. _localizations/hungary/aggregate:

Aggregate invoices
==================

An aggregate invoice (*gyűjtőszámla*) lists several supplies of a period, each with its own
fulfillment date. The :guilabel:`Aggregate Invoice` checkbox is available if the customer has an
:guilabel:`Aggregate Invoice Aggreement` (:ref:`contact form <localizations/hungary/contacts>`); it
cannot be combined with :guilabel:`Continuous Fulfillment`.

- Every product line needs a :guilabel:`Fulfillment Date / End of Period`.
- All line dates must fall into the same calendar month, cannot be in the future, and the start of
  a period cannot be later than its end.
- The :guilabel:`Fulfillment Date` of the invoice is the latest line date.
- Taxes flagged :guilabel:`Nem készíthető Gyűjtőszámla ezzel az áfa kulccsal` cannot be used.

The invoice is reported to NAV in the *aggregate* invoice category.

.. _localizations/hungary/intermediated:

Intermediated services
======================

Tick :guilabel:`The invoice includes an intermediated service` (*közvetített szolgáltatás*) to
display the :guilabel:`Intermediated Service` checkbox on the lines, then mark the relevant lines.
Lines of products with :guilabel:`Intermediated Service by Default` are marked automatically. At
least one line must be marked if the invoice-level checkbox is ticked. The text *The invoice includes
an intermediated service.* is printed on the invoice and the flag is reported to NAV line by line.

.. _localizations/hungary/corrective:

Corrective invoices and credit notes
====================================

A posted invoice cannot be modified. It can be **cancelled** with a credit note (*sztornó számla*) or
**corrected** with a corrective invoice (*helyesbítő számla*). All three documents share the number
sequence of the journal and are reported to NAV as a chain.

Credit note
-----------

The :guilabel:`Credit Note` button is available on posted, **unpaid** invoices that have no
corrective, advance or final invoice linked to them. The :guilabel:`Credit Method` is either
:guilabel:`Full refund` or :guilabel:`Full refund and new draft invoice`; partial refunds are made
with corrective invoices. :guilabel:`Payment Term` can be changed in the dialog. The credit note
keeps the fulfillment date, the accounting date and the exchange rate of the original invoice. A
credit note or a corrective invoice cannot be credited again.

.. tip::
   Enable :guilabel:`Automatically post Credit Note` in the Accounting settings to confirm credit
   notes as soon as they are created.

Corrective invoice
------------------

On a posted customer invoice, click :guilabel:`Corrective Invoice`. A draft is created with the
title *Corrective Invoice*, today as invoice date, the fulfillment and accounting dates of the
original invoice, and:

- a section *Helyesbített tételek* (corrected items) containing every line of the original invoice
  with a **negative quantity**, each followed by a note with the original quantity, unit price and
  discount;
- an empty section *Új tételek* (new items) for lines that were missing from the original invoice.

On the corrected lines only the :guilabel:`Quantity` and the :guilabel:`Label` can be edited. Enter
the quantity **by which** the original line changes: if 10 pieces were invoiced and 5 were delivered,
enter `-5`; to invoice 15 instead of 10, enter `5`. The pre-filled quantities reverse the original
invoice completely, so delete the lines that need no correction.

.. screenshot:: finance-fl-hungary-corrective-invoice
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (posted invoice) ‣ Corrective Invoice
   :shows: Draft corrective invoice: title "Corrective Invoice", the red explanation box above the lines, section "Helyesbített tételek" with a negative-quantity line and its note about the original data, section "Új tételek", and the lock toggle above the lines.
   :highlight: The quantity cell of the corrected line (red frame).
   :data: Original invoice "KI/2026/00012": 10 pcs "Office Chair" at 25,000 HUF; corrective quantity -5.
   :module: eyssen_l10n_hu
   :notes: English UI, light theme, 1440px width, crop to the lines area. The explanation box and section names are Hungarian.

When the corrective invoice is confirmed and its total is negative, it is converted into a
*Corrective Credit Note* automatically. The printed titles are *Correction Invoice* and *Correction
Credit Note*.

:guilabel:`Corrective Invoice to Zero` is available on invoices that are already (partially) paid.
It creates a corrective invoice that reverses the original invoice **and** all its previous
corrections, while the payments stay reconciled with the original invoice.

The :guilabel:`Related Invoices` tab links the documents of a chain: :guilabel:`Original Invoice`,
:guilabel:`Correction Serial Number`, the list of posted :guilabel:`Corrective Invoice` documents,
the :guilabel:`Final Invoice` and the :guilabel:`Down Payment Invoices` (see :doc:`proforma`).

.. note::
   The lock toggle above the invoice lines prevents the label, unit
   price and discount of the lines from being recomputed when the product or unit changes. It is
   enabled automatically on corrective invoices and on bills imported from NAV.

Advance and final invoices
--------------------------

When the final invoice of a sales order is created with :guilabel:`Create Invoice` --> *Regular
invoice*, the option :guilabel:`Előleg levonása a számlázandó összegig` limits the deducted advance
to the value of the products being invoiced; the rest of the advance remains on the order and is
deducted from a later invoice.

.. _localizations/hungary/invoice-format:

Paper-based and electronic invoices
===================================

The :guilabel:`Invoice Format` field (:guilabel:`Other Info` tab) is :guilabel:`Paper-based` or
:guilabel:`Electronic`. It defaults to *Electronic* for customers with an :guilabel:`Electronic
Invoice Aggreement`, otherwise to the format of the journal. Electronic invoices are titled
*E-Invoice* (*E-Credit Note*, …), are reported to NAV as electronic, and are digitally signed when
printed; the sentence *The invoice is valid without signature and stamp!* is printed on paper-based
invoices only.

.. note::
   Electronic invoices require the *eYssen E-sign* (`eyssen_esign`) module. Selecting
   :guilabel:`Electronic` on an invoice also records the electronic invoice agreement on the
   customer.

Other invoice features
======================

- :guilabel:`Payment Dates` tab: the installments of the invoice (due date, label, amount). They can
  be edited on the draft; on a posted invoice, accountants can move a due date with the
  :guilabel:`Change Payment Date` button.
- :guilabel:`Custom Fields` (:guilabel:`Other Info` tab): up to three name–value pairs that are
  printed in the information row of the invoice.
- :guilabel:`Last Seller`: keeps the name of the salesperson even if the user is later removed.
- :guilabel:`Address for sending an Invoice`: filled in with the *follow-up* address of the
  customer, when :guilabel:`Customer Addresses` is enabled.
- :guilabel:`Delete all lines`: removes every line of a draft invoice.
- **Vendor bills**: the link icon on a draft bill line opens the :guilabel:`Change Purchase Order
  Line Account` dialog, where the line can be linked to a not yet invoiced purchase order line of the
  vendor, or unlinked with :guilabel:`Clear purchase order line`.
- **Lists**: the :guilabel:`Fulfillment Date` column, amounts in the document currency and in the
  company currency, and grouping by :guilabel:`Currency`.
- **Sales orders**: :guilabel:`Delivery Deadline` (free text printed on the quotation) and
  :guilabel:`Bank Account` (the company account printed on the pro-forma and the invoice). The
  quotation shows net, VAT and gross amounts per line.
- **Numbering**: invoice numbers of the hash-secured customer invoice journal cannot be resequenced.

The printed invoice contains the data required by the VAT Act: the tax numbers of both parties (the
group VAT number if applicable), the payment method, the invoice, fulfillment and due dates, the
VTSZ/KN/SZJ/TESZOR code of the items, net amount, VAT rate, VAT amount and gross amount per line,
totals per VAT rate (also in HUF for foreign-currency invoices), and the declaration that the
invoicing software complies with Decree 23/2014 (VI. 30.) NGM.

.. _localizations/hungary/foreign-vat:

Invoicing under a foreign VAT registration
==========================================

A company that is registered for VAT in another country (for example, because of a local warehouse)
issues those invoices under its foreign tax number. They belong to the tax jurisdiction of the other
country: they are **not reported to NAV** and must be numbered separately from the Hungarian
invoices.

#. Create a :doc:`fiscal position <../../accounting/taxes/fiscal_positions>` for the country with
   the :guilabel:`Foreign Tax ID` of the company and the taxes of that country.
#. Create a dedicated sales journal. In its :guilabel:`Journal Entries` tab, tick
   :guilabel:`Foreign VAT Journal` and select the fiscal position in :guilabel:`Allowed Foreign VAT
   Fiscal Positions`.
#. Create the invoice in this journal. Only the allowed fiscal positions can be selected (a single
   allowed position is set automatically). An invoice created with a foreign VAT fiscal position is
   placed in the matching journal automatically.

On regular journals, fiscal positions with a foreign tax ID cannot be selected; if the customer would
normally get one, a warning suggests switching to the foreign VAT journal. The foreign VAT setting of
a journal cannot be removed once the journal contains such invoices.

.. screenshot:: finance-fl-hungary-foreign-vat-journal
   :menu: Accounting ‣ Configuration ‣ Journals ‣ (sales journal) ‣ Journal Entries tab
   :shows: Sales journal form with the "Foreign VAT (Külföldi adószám)" section: "Foreign VAT Journal" ticked and one fiscal position tag in "Allowed Foreign VAT Fiscal Positions"; the "Invoice Format" section below.
   :highlight: The "Foreign VAT (Külföldi adószám)" section (red frame).
   :data: Journal "Customer Invoices SK" (code KISK); fiscal position "Slovakia (SK VAT)".
   :module: eyssen_l10n_hu
   :notes: English UI, light theme, 1440px width, crop to the tab. Normal (non-developer) mode.

===========================
NAV Online Számla reporting
===========================

Hungarian taxpayers must report the data of every issued invoice to the *Online Számla* system of
the :abbr:`NAV (Nemzeti Adó- és Vámhivatal, National Tax and Customs Administration)` in real time.
With the `eyssen_l10n_hu` module, Odoo sends the customer invoices, corrective invoices and credit
notes to NAV automatically after they are confirmed, follows the processing of the reports, and can
import the invoices that suppliers reported on the company's tax number.

.. _localizations/hungary/nav-settings:

Configuration
=============

Technical user
--------------

Create a *technical user* on the `Online Számla website <https://onlineszamla.nav.gov.hu>`_ (or, for
testing, on the `test website <https://onlineszamla-test.nav.gov.hu>`_) and generate its **signing
key** (*XML aláírókulcs*) and **exchange key** (*XML cserekulcs*). The user name, the password and the
two keys are needed in Odoo.

Settings
--------

Go to :menuselection:`Accounting --> Configuration --> Settings`, scroll to the :guilabel:`NAV Online
invoice data reporting` section, and tick :guilabel:`NAV Enable`. The same options are available in
the :guilabel:`NAV Data Reporting` tab of the company form.

:guilabel:`NAV Data Reporting`

- :guilabel:`Operaion Mode`: :guilabel:`Test` sends the reports to the NAV test system with the test
  credentials, :guilabel:`Production` to the live system.
- :guilabel:`Do not send invoices to the NAV. FOR TESTING PURPOSES ONLY!`: suspends the reporting
  completely (for example, in a copy of the production database).
- :guilabel:`Loading Taxpayer Name` (:guilabel:`Short Name` or :guilabel:`Full Name`),
  :guilabel:`Keep the manually set partner name` and :guilabel:`Keep the manually set partner
  address`: control the :ref:`taxpayer query <localizations/hungary/contacts>` on contacts.
- :guilabel:`Do not check the VAT Number`: Hungarian tax numbers are accepted without querying NAV.
- :guilabel:`Import Default Journal` and :guilabel:`Import Default Account`: used by the
  :ref:`invoice import <localizations/hungary/nav-import>`.

:guilabel:`Login Details`

- :guilabel:`User Name`, :guilabel:`Password`, :guilabel:`Sign Key` and :guilabel:`Exchange Key` of
  the production technical user;
- :guilabel:`Test User Name`, :guilabel:`Test Password`, :guilabel:`Test Sign Key` and
  :guilabel:`Test Exchange Key` of the technical user created on the test website.

.. screenshot:: finance-fl-hungary-nav-settings
   :menu: Accounting ‣ Configuration ‣ Settings
   :shows: Settings page scrolled to the "NAV Online invoice data reporting" section: "NAV Enable" ticked, the operation mode, the testing switch, the taxpayer name options, the import journal and account, the "Login Details" block with the eight credential fields, and the "NAV Export", "NAV Technikai érvénytelenítés" and "NAV Import" buttons.
   :highlight: The "NAV Data Reporting" and "Login Details" blocks (red frame).
   :data: Demo company "YourCompany HU"; mode "Test"; test user name "abcdefgh1234567".
   :module: eyssen_l10n_hu
   :notes: English UI, light theme, 1440px width, crop to the section. Use throw-away secrets; password and keys must not be readable.

.. important::
   - The reporting only works if the company's :ref:`VAT Number <localizations/hungary/company>` is
     valid and all four credentials of the selected mode are filled in; otherwise confirming a
     customer invoice is refused.
   - A copied (neutralized) database should always run in :guilabel:`Test` mode or with the *Do not
     send invoices to the NAV* switch enabled.

:guilabel:`Other Settings`

- :guilabel:`Automatically post Credit Note`: credit notes created with the :guilabel:`Credit Note`
  button are confirmed (and therefore reported) immediately.

Reporting invoices
==================

When a customer invoice, corrective invoice or credit note is **confirmed**, Odoo first checks the
:ref:`mandatory data <localizations/hungary/invoice-checks>`, then queues the data report. The
report is sent by a background job about one minute later and is retried every five minutes until
NAV accepts it. Nothing else has to be done by the user.

The :guilabel:`NAV` tab of the invoice shows the result:

- :guilabel:`NAV Sending Date` and :guilabel:`NAV Sending State` (*Beküldés folyamatban* while the
  report is waiting to be sent);
- :guilabel:`NAV Processing State`: `RECEIVED`, `PROCESSING`, `SAVED`, `DONE` (accepted) or
  `ABORTED` (rejected);
- :guilabel:`NAV Transaction ID` and :guilabel:`NAV Response` (warnings and error messages of NAV);
- :guilabel:`NAV Submitted XML`: the data that was sent;
- :guilabel:`No need to hand it over to the NAV!` and :guilabel:`It did not have to be submitted to
  the NAV for the following reasons:` if the invoice was not reported.

The :guilabel:`NAV Processing State` is also displayed as a colored badge in the customer invoice
and credit note lists, so rejected reports are easy to find.

.. screenshot:: finance-fl-hungary-nav-tab
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (posted invoice) ‣ NAV tab
   :shows: Posted customer invoice with the "NAV" tab open: sending date, sending state, processing state "DONE" in green, transaction ID, empty response, and the submitted XML below.
   :highlight: The "NAV Processing State" field (red frame).
   :data: Invoice "KI/2026/00012" for "Minta Kft.", 127,000 HUF, reported in test mode.
   :module: eyssen_l10n_hu
   :notes: English UI, light theme, 1440px width, crop to the tab. Normal (non-developer) mode, so the technical buttons are hidden.

An `ABORTED` report means that NAV refused the data (the reason is in :guilabel:`NAV Response`).
Correct the cause (typically master data such as the tax number or address of the customer, or the
NAV settings of a tax group); the report is sent again automatically. In :ref:`developer mode
<developer-mode>`, the :guilabel:`NAV` tab also offers the buttons :guilabel:`Send to NAV`,
:guilabel:`Immediately Send to NAV`, :guilabel:`Check State`, :guilabel:`Get from NAV`,
:guilabel:`Get Invoice Chain from NAV` and :guilabel:`Link storno to original` for administrators.

Invoices that are not reported
------------------------------

No data report is sent, and the reason is recorded on the :guilabel:`NAV` tab, for

- vendor bills and other non-customer documents;
- invoices of journals marked :guilabel:`No need to hand it over to the NAV!` (see :ref:`below
  <localizations/hungary/external-journal>`), and invoices imported from NAV;
- invoices issued :ref:`under a foreign VAT registration <localizations/hungary/foreign-vat>` and
  :doc:`EU OSS invoices <oss>`;
- any invoice while :guilabel:`Do not send invoices to the NAV. FOR TESTING PURPOSES ONLY!` is
  enabled.

Scheduled actions
-----------------

The following scheduled actions are created (:menuselection:`Settings --> Technical --> Scheduled
Actions`, in :ref:`developer mode <developer-mode>`):

.. list-table::
   :header-rows: 1
   :widths: 50 15 35

   * - Name
     - Interval
     - Purpose
   * - *NAV beküldetlen számlák beküldése*
     - 5 minutes
     - Queues posted customer invoices that were not sent yet.
   * - *NAV beküldött számlák ellenőrzése*
     - 30 minutes
     - Refreshes the processing state of reports not yet `DONE`.
   * - *NAV sikeresen elvégzett adatküldés műveletek törlése*
     - 1 hour
     - Removes the finished per-invoice sending jobs (*NAV adatszolgáltatás: <number>*).
   * - *NAV számlák importálása (aktuális nap)*
     - 1 hour, inactive
     - Imports the vendor bills reported to NAV today.
   * - *NAV számlák importálása (utolsó 30 nap)*
     - 2 days, inactive
     - Imports the vendor bills reported to NAV in the last 30 days.

.. _localizations/hungary/external-journal:

Journals for invoices issued in another system
----------------------------------------------

Invoices that were issued and reported by another invoicing program (or in a previous system) can be
recorded in a dedicated sales journal. In :ref:`developer mode <developer-mode>`, open the journal
and set, in the :guilabel:`Hungarian Invoicing` section of the :guilabel:`Journal Entries` tab:

- :guilabel:`No need to hand it over to the NAV!`: the invoices of the journal are never reported
  and their :guilabel:`NAV` tab is hidden;
- :guilabel:`No automatic serial number`: the invoice number can be typed in on the draft invoice;
- :guilabel:`Backdated date can be set`: the invoice date may differ from today;
- :guilabel:`Accept externally-issued foreign VAT invoices`: the journal may also record invoices
  that were issued elsewhere under a foreign VAT registration (requires the first two options).

.. warning::
   Never use such a journal for invoices issued from Odoo: the continuous numbering and the data
   reporting obligation apply to every invoice issued by the company.

.. _localizations/hungary/nav-import:

Importing invoices from NAV
===========================

Vendor bills reported by suppliers on the company's tax number can be downloaded from NAV as draft
bills. Set the :guilabel:`Import Default Journal` in the :ref:`settings
<localizations/hungary/nav-settings>` first (its default account is the :guilabel:`Import Default
Account` used on lines for which no better account is found).

- **By period**: go to :menuselection:`Accounting --> Vendors --> NAV Inbound Invoice Import`, set
  the :guilabel:`Start Date` and :guilabel:`End Date` (the dates on which the invoices were reported
  to NAV), and click :guilabel:`Import`. The two inactive scheduled actions
  listed above can do the same automatically.
- **By invoice number**: in the settings, click :guilabel:`NAV Import`, choose the
  :guilabel:`Direction` (:guilabel:`Inbound` or :guilabel:`Outbound`) and the :guilabel:`Journal`,
  and list the :guilabel:`Invoice Numbers`, one per line. For inbound invoices, type the first eight
  digits of the supplier's tax number, a space, then the invoice number (`12345678 INV-2026-001`).

For every invoice that does not exist yet (an invoice with the same number is skipped, even if it is
cancelled), a **draft** bill is created:

- the supplier is found by tax number (or name and city); if there is no match, a new company
  contact is created from the NAV data;
- the supplier's invoice number becomes the :guilabel:`Bill Reference`; the invoice, fulfillment and
  due dates, the currency and the exchange rate are taken from the report;
- the lines are created with the product found by name, the unit of measure and a tax matching the
  reported VAT rate or exemption code. **If no matching tax exists, a new tax is created**, so review
  the taxes of imported bills;
- storno invoices become credit notes linked to the original bill, modifying invoices become
  :ref:`corrective invoices <localizations/hungary/corrective>`;
- the bill is marked :guilabel:`No need to hand it over to the NAV!`, its line data is locked
  against recomputation, and the downloaded XML is stored on the :guilabel:`NAV` tab.

Check the accounts, taxes and analytic distribution of the draft, then confirm it as usual.

.. screenshot:: finance-fl-hungary-nav-import-wizard
   :menu: Accounting ‣ Vendors ‣ NAV Inbound Invoice Import
   :shows: The import dialog with "Direction" (read-only, Inbound), "Start Date", "End Date" and the "Import" and "Cancel" buttons.
   :highlight: The date fields (red frame).
   :data: Start Date = first day of the current month, End Date = today.
   :module: eyssen_l10n_hu
   :notes: English UI, light theme, 1440px width, crop to the dialog.

Tax audit export
================

For a tax audit, NAV can request the data of the issued invoices in a standard XML file. In the
:ref:`settings <localizations/hungary/nav-settings>`, click :guilabel:`NAV Export`, set
:guilabel:`Date from` and :guilabel:`Date to`, and click :guilabel:`Export`. The file
`NAV_export.xml` contains the posted customer invoices and credit notes whose invoice date falls
into the period.

Technical annulment
===================

A data report that was sent with wrong data because of a technical error can be withdrawn with a
*technical annulment* (*technikai érvénytelenítés*). It does not cancel the invoice itself, only the
data report, and nothing changes on the invoice in Odoo.

In the :ref:`settings <localizations/hungary/nav-settings>`, click :guilabel:`NAV Technikai
érvénytelenítés` and fill in:

- :guilabel:`Számla sorszáma`: the number of the invoice whose report is annulled;
- :guilabel:`Érvénytelenítés kódja`: the reason code (wrong data content, wrong invoice number,
  wrong issue date, or wrong electronic invoice hash);
- :guilabel:`Érvénytelenítés oka`: a free-text explanation.

Click :guilabel:`Érvénytelenítés`. A notification shows the NAV transaction ID and the status of the
request.

.. important::
   According to the rules of the Online Számla system, a technical annulment takes effect only
   after it has been approved on the Online Számla website by a user of the taxpayer.

.. note::
   The labels of this dialog are displayed in Hungarian in the current module version.

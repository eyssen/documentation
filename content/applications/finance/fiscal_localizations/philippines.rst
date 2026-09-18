===========
Philippines
===========

Configuration
=============

:ref:`Install <general/install>` the :guilabel:`🇵🇭 Philippines` :ref:`fiscal localization package
<fiscal_localizations/packages>` to get all the default accounting features of the Philippine
localization, such as a chart of accounts and taxes. These provide a base template to get
started with using Philippine accounting.

.. note::
   The Philippine BIR 2307, SLSP, 2550Q, QAP and SAWT reports, and the Philippine check layout
   (*Print Check - PH*) are **not** available in this edition. The ATC codes of the withholding
   taxes are still stored on the taxes and can be exported from the :doc:`tax report
   <../accounting/reporting/dynamic_reports>`; checks can be printed with the generic
   :doc:`check layouts <../accounting/payments/pay_checks>`.

.. note::
  - When creating a new database and selecting the `Philippines` as a country, the fiscal
    localization module **Philippines - Accounting** is automatically installed.
  - If the module is installed in an existing company, the **chart of accounts** and **taxes** will
    *not* be replaced if there are already posted journal entries.

Chart of accounts and taxes
---------------------------

A minimum configuration default chart of accounts is installed, and the following types of taxes are
installed and linked to the relevant account:

- Sales and Purchase VAT 12%
- Sales and Purchase VAT Exempt
- Sales and Purchase VAT Zero-Rated
- Sales and Purchase Withholding

For the withholding taxes (:menuselection:`Accounting --> Configuration --> Taxes`), there is an
additional :guilabel:`Philippines ATC` field under the :guilabel:`Philippines` tab.

.. screenshot:: finance-fl-philippines-atc-code
   :menu: Accounting ‣ Configuration ‣ Taxes ‣ (a withholding tax) ‣ Philippines tab
   :shows: The "Philippines" tab of a withholding tax with the "Philippines ATC" field set (e.g. WC010).
   :highlight: The "Philippines ATC" field.
   :data: Demo company "YourCompany PH", Philippine localization installed.
   :module: l10n_ph
   :notes: English UI, light theme, 1440px width.

.. note::
  Taxes' ATC codes identify the withholding tax type towards the BIR. If a tax is created manually,
  its ATC code must be added.

Contacts
--------

When a company or an individual (not belonging to a company) contact is located in the Philippines,
fill in the :guilabel:`Tax ID` field with their `Taxpayer Identification Number (TIN)`.

For individuals not belonging to a company, identify them by using the following additional fields:

- :guilabel:`First Name`
- :guilabel:`Middle Name`
- :guilabel:`Last Name`

.. note::
  For both :guilabel:`Company` and :guilabel:`Individual`, the TIN should follow the
  `NNN-NNN-NNN-NNNNN` format. The branch code should follow the last digits of the TIN, or else it
  can be left as `00000`.

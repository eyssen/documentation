=======
Ecuador
=======

The Ecuadorian localization provides the chart of accounts, taxes, document types, and journal
settings (emission entity and point) required to issue invoices, credit notes, debit notes, and
withholdings according to the numbering rules of the :abbr:`SRI (Servicio de Rentas Internas)`.

.. tip::
   - **SRI**: *Servicio de Rentas Internas*, the government organization that enforces the payment
     of taxes in Ecuador.
   - **RIMPE**: *Regimen Simplificado para Emprendedores y Negocios*, the type of taxpayer qualified
     for SRI.

.. _localizations/ecuador/module-installation:

Modules
=======

:doc:`Install </applications/general/apps_modules>` the following modules to get all the features of
the Ecuadorian localization:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Ecuadorian - Accounting`
     - `l10n_ec`
     - The default :doc:`fiscal localization package <../fiscal_localizations>` adds accounting
       characteristics for the Ecuadorian localization, which represent the minimum configuration
       required for a company to operate in Ecuador according to the guidelines set by the
       :abbr:`SRI (servicio de rentas internas)`. The module's installation automatically loads:
       a chart of accounts, taxes with their form 103/104 codes, document types, and the SRI payment
       methods.
   * - :guilabel:`Ecuadorian Website`
     - `l10n_ec_website_sale`
     - Lets customers enter their identification type and number at checkout, and links each
       eCommerce payment method to an SRI payment method.

.. note::
   The electronic documents (XML generation, electronic signature with the SRI certificate and
   direct connection to the SRI), the automatic withholding computation on vendor bills, purchase
   liquidations, the electronic delivery guide, the Point of Sale electronic invoicing, and the
   103 / 104 / ATS reports are **not** available in this edition. The tax grids of the 103 and 104
   forms are available in the :doc:`tax report <../accounting/reporting/dynamic_reports>`.

.. _localizations/ecuador/specifics:

Localization overview
=====================

The Ecuadorian localization package provides the following key features:

- :doc:`../accounting/get_started/chart_of_accounts`: a predefined structure aligned with the latest
  standards of Ecuador’s *Superintendency of Companies*, organized into multiple categories and
  fully compatible with NIIF accounting
- :ref:`Taxes <localizations/ecuador/taxes>`: pre-configured tax rates, including standard VAT,
  zero-rated, and exempt options, and the withholding taxes
- :doc:`../accounting/taxes/fiscal_positions`: automated tax adjustments based on customer or
  supplier registration status
- :ref:`Document types <localizations/ecuador/document types>`: classification of transactions like
  *customer invoices* and *vendor bills* using government-defined document types set by the SRI
  (Ecuador’s tax authority)
- :ref:`Company and contacts <localizations/ecuador/company-contact>`
- :ref:`Printer points <localizations/ecuador/printer-points>`

.. _localizations/ecuador/taxes:

Taxes
-----

To manage taxes, navigate to :menuselection:`Accounting --> Configuration --> Taxes`. Depending on
the tax type, the following options may be required for additional configuration:

- :guilabel:`Tax Name`: Follows a specific format depending on the tax type:

  - | **For IVA (Value-Added Tax)**:
    | `IVA [percent] (104, [form code] [tax support code] [tax support short name])`
    | Example: `IVA 12% (104, RUC [tax support code] IVA)`
  - | **For Income Tax Withholding codes**:
    | `Code ATS [percent of withhold] [withhold name]`
    | Example: `Code ATS 10% Retención a la Fuente`

- :guilabel:`Code base` and :guilabel:`Code applied`: the codes of the form 103/104 boxes for the
  base amount and the tax amount.
- :guilabel:`Code ATS`: Configure only for income tax withholding codes.

The tax group of each tax carries a :guilabel:`Type Ecuadorian Tax` (e.g., *VAT*, *Profit Withhold
on Purchases*, *VAT Withhold on Purchases*) that tells Odoo how the tax must be treated.

In the :guilabel:`Definition` tab:

- :guilabel:`Tax Grids`: Configure the code of a 104 form if it is an IVA tax, and the code of a
  103 form if it is an income tax withholding code.

.. screenshot:: finance-fl-ecuador-tax-codes
   :menu: Accounting ‣ Configuration ‣ Taxes ‣ (an IVA tax)
   :shows: The tax form of an Ecuadorian IVA tax with the "Code base", "Code applied" and "Code ATS" fields next to the tax name, and the Definition tab with the 104 form tax grids.
   :highlight: The three code fields.
   :data: Demo company "YourCompany EC"; tax "IVA 15% (104, RUC 01 IVA)".
   :module: l10n_ec
   :notes: English UI, light theme, 1440px width.

.. seealso::
   :doc:`Configuring taxes <../accounting/taxes>`

.. _localizations/ecuador/document types:

Document types
--------------

To access or configure document types, go to :menuselection:`Accounting --> Configuration -->
Document Types`. Each document type can have a unique sequence per journal where it is assigned. As
part of the localization, the document type includes the country where the document is applicable;
also, the data is created automatically when the localization module is installed. The information
required for the document types is included by default and doesn't need to be changed.

.. _localizations/ecuador/company-contact:

Company and contact
-------------------

.. seealso::
   :doc:`Configure a company or individual contact <../../essentials/contacts>`

The following fields should be completed for localization purposes on the contact form:

- :guilabel:`Name`: Enter the company or individual's name.
- :guilabel:`Address`: The :guilabel:`Street` sub-field is required on invoices.
- :guilabel:`Identification Number`: For a company, enter the :guilabel:`RUC`. For individuals,
  enter the :guilabel:`Cédula` or :guilabel:`Passport` number. The number is checked (13 digits
  for a RUC, 10 for a Cédula); an invalid number is reported in the :guilabel:`VAT Error message
  validation` field.
- :guilabel:`Phone`: Enter the company or individual's phone number.
- :guilabel:`Email`: Enter the company or individual's email.

The identification type of the partner determines which document types can be used on an invoice
or bill for that partner.

.. _localizations/ecuador/printer-points:

Printer points
--------------

*Printer points* (emission points) need to be configured for each journal that issues legal
documents, such as customer invoices, credit notes, and debit notes.

To configure printer points, navigate to :menuselection:`Accounting --> Configuration -->
Journals`. For each document series, click :guilabel:`New`, and enter the following information
on the journal form:

- :guilabel:`Journal Name`: Enter in this format: `[Emission Entity]-[Emission Point] [Document
  Type]`, e.g., `001-001 Sales Documents`.
- :guilabel:`Type`: Refers to the journal type; select :guilabel:`Sales`.

Once the :guilabel:`Type` is selected, complete the following fields:

- :guilabel:`Use Documents?`: Enable this option if legal invoicing (invoices, debit/credit notes)
  is used, as this is the standard configuration. If not, select the option to record accounting
  entries unrelated to legal invoicing documents, such as receipts, tax payments, or journal
  entries.
- :guilabel:`Emission Entity`: Enter the facility number (3 digits).
- :guilabel:`Emission Point`: Enter the printer point (3 digits).
- :guilabel:`Emission address`: Enter the address of the facility.

In the :guilabel:`Journal Entries` tab, under the :guilabel:`Accounting information` section, fill
in the following fields:

- :guilabel:`Default Income Account`: Enter the default income account.
- :guilabel:`Dedicated Credit Note Sequence`: Enable this option if *credit notes* should be
  generated from this printer point (i.e., the journal).
- :guilabel:`Dedicated Debit Note Sequence`: Enable this option if *debit notes* should be
  generated from this printer point (i.e., the journal).
- :guilabel:`Short Code`: Enter a unique 5-digit code for the accounting entry sequence (e.g.,
  VT001).

Customer invoices, credit notes, and debit notes must use the same journal as the
:guilabel:`Emission Point`, whereas the entity / emission point pair should be unique per journal. The
document number is built as `[entity]-[emission point]-[sequence]`, e.g. `001-001-000000123`.

.. screenshot:: finance-fl-ecuador-journal-emission
   :menu: Accounting ‣ Configuration ‣ Journals ‣ (a sales journal)
   :shows: A sales journal form for Ecuador with "Use Documents?" enabled and the "Emission Entity" (001), "Emission Point" (001) and "Emission address" fields below it.
   :highlight: The "Emission Entity" and "Emission Point" fields.
   :data: Journal "001-001 Sales Documents", demo company "YourCompany EC".
   :module: l10n_ec
   :notes: English UI, light theme, 1440px width.

SRI payment methods
-------------------

Invoices carry a :guilabel:`Payment Method (SRI)` field (Other Info tab) with the payment methods
defined by the SRI (e.g., *Sin utilización del sistema financiero*, *Tarjeta de crédito*,
*Transferencia*). The list can be managed from :menuselection:`Accounting --> Configuration -->
Ecuadorian SRI --> Payment Methods SRI`.

eCommerce
=========

The *Ecuadorian Website* (`l10n_ec_website_sale`) module enables the following:

- Choose the :guilabel:`SRI Payment Method` for each payment method's configuration
  (:menuselection:`Website --> Configuration --> Payment Methods`).
- Customers can manually input their identification type and number during eCommerce checkout.

.. seealso::
   :doc:`eCommerce documentation <../../websites/ecommerce>`

.. _localizations/ecuador/online-payments:

Online payments
---------------

To enable online payments, add the relevant :doc:`payment provider(s) <../payment_providers>` and
configure the necessary :ref:`payment methods <payment_providers/payment_methods>`. Set the
:guilabel:`SRI Payment Method` for each method so that the invoices created from website orders get
the right :guilabel:`Payment Method (SRI)`.

.. _localizations/ecuador/ecommerce-workflow:

Identification type and number
------------------------------

During the checkout process, the client making a purchase will have the option to indicate their
identification type and number. This information is required to create the invoice with the
correct document type after the checkout is completed.

.. note::
   Verification is done to ensure the :guilabel:`Identification Number` field is completed and has
   the correct number of digits. For RUC identification, 13 digits are required, and for Cédula, 10
   digits are required.

.. screenshot:: finance-fl-ecuador-ecommerce-identification
   :menu: (website) ‣ Shop ‣ Checkout ‣ Address
   :shows: The eCommerce checkout address form for an Ecuadorian customer with the "Identification Type" drop-down (RUC, Cédula, Pasaporte) and the "Identification Number" field.
   :highlight: The identification fields.
   :data: Country Ecuador, type Cédula.
   :module: l10n_ec_website_sale
   :notes: English UI, light theme, 1440px width.

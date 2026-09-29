:show-content:
:show-toc:

=====
Spain
=====

Configuration
=============

Install the 🇪🇸 **Spanish** :doc:`fiscal localization package <../fiscal_localizations>` to get all
the default accounting features of the Spanish localization.

Several **Spanish** charts of accounts (**PGCE**) are pre-configured:

- Spain - SMEs (2008);
- Spain - Complete (2008);
- Spain - Non-profit entities (2008);
- Spain - Cooperatives - SMEs (2008);
- Spain - Cooperatives - Complete (2008);
- the equivalent charts for the Canary Islands.

The :ref:`company setup wizard <localizations/spain/setup-wizard>` can load the chart for you.

To select the one to use, go to :menuselection:`Accounting --> Configuration --> Settings` and
select a package in the :guilabel:`Fiscal Localization` section.

.. warning::
   You can only change the accounting package as long as you have not created any accounting entry.

.. seealso::
   - :doc:`Documentation on e-invoicing’s legality and compliance in Spain
     <../accounting/customer_invoices/electronic_invoicing/spain>`
   - :doc:`Documentation on e-invoicing’s legality and compliance in the Basque Country
     <../accounting/customer_invoices/electronic_invoicing/basque_country>`

.. _localizations/spain/base-layer:

Spanish setup and supported module combination
----------------------------------------------

The Spanish localization of eYssen is a *hybrid* localization: it combines the standard Odoo modules
(charts of accounts, Veri*Factu, Facturae, TicketBAI, Point of Sale) with the Spanish community
modules (OCA) for everything that the standard localization lacks (AEAT tax declarations, VAT books,
SII, Spanish contact and bank data, and others). The *Spain - Accounting (PGCE 2008)* module
(`l10n_es`) sets this combination up and keeps it consistent:

- the :ref:`Spanish company setup wizard <localizations/spain/setup-wizard>` guides you through the
  configuration of a Spanish company;
- the :ref:`fiscal profile <localizations/spain/fiscal-profile>` installs the modules that a
  self-employed person or a company needs;
- the :ref:`module choice <localizations/spain/module-choice>` refuses the modules that duplicate
  a supported one.

.. note::
   Earlier versions had a separate *Spain - Base Layer* module (`l10n_es_base_layer`). Its features
   are now part of `l10n_es`; there is nothing else to install. If a page or a message still
   mentions the base layer, it refers to this section.

Install the 🇪🇸 **Spanish** fiscal localization package as described above. Then set up the company
with the wizard, or set the fiscal profile directly in the settings. The :guilabel:`Spain` menu is
available to accounting administrators.

.. _localizations/spain/setup-wizard:

Company setup wizard
~~~~~~~~~~~~~~~~~~~~

The wizard configures a Spanish company step by step and records what it did. Use it for a new
company, or to review the configuration of an existing one. The wizard is only available for
companies whose country is Spain.

To open it, go to :menuselection:`Accounting --> Configuration --> Spain --> Company setup`, or to
:menuselection:`Accounting --> Configuration --> Settings`, scroll to the :guilabel:`Spain` section,
and click :guilabel:`Open the setup wizard`.

.. screenshot:: finance-fl-spain-setup-wizard
   :menu: Accounting ‣ Configuration ‣ Spain ‣ Company setup
   :shows: The "Spain: company setup" dialog at the step "2. Fiscal profile", with the progress bar (1. Company … Done), the "Fiscal profile" radio buttons, the "SII taxpayer" checkbox, the list of modules to install and the "Save and continue" button.
   :highlight: The progress bar at the top and the "Save and continue" button.
   :data: Demo company "YourCompany ES", wizard reopened after step 1.
   :module: l10n_es
   :notes: English UI, light theme, 1440px width, crop to the dialog.

Click :guilabel:`Save and continue` to apply a step and go to the next one, :guilabel:`Back` to go
to the previous step, and :guilabel:`Continue later` to close the wizard. The progress is saved:
when you reopen the wizard, it resumes at the step where you stopped. The steps
:guilabel:`6. Bank`, :guilabel:`7. Certificate` and :guilabel:`8. Tax advisor` can be skipped with
the :guilabel:`Skip` button.

.. list-table::
   :header-rows: 1
   :widths: 20 45 35

   * - Step
     - What you set
     - Good to know
   * - :guilabel:`1. Company`
     - :guilabel:`Legal form` (:guilabel:`Self-employed (autónomo)`, :guilabel:`Limited company
       (S.L.)`, :guilabel:`Public limited company (S.A.)`, :guilabel:`Joint ownership (C.B.)` or
       :guilabel:`Other entity`), :guilabel:`Name / company name`, :guilabel:`NIF`, the address and
       the :guilabel:`Province`. Also :guilabel:`Check intra-EU VAT numbers (VIES)` (enabled by
       default) and :guilabel:`Spanish language and Madrid time zone`.
     - The NIF is checked (format and check character) against the legal form: a self-employed
       person needs a DNI or an NIE; the NIF of an S.L. starts with B, of an S.A. with A, and of a
       C.B. with E; :guilabel:`Other entity` cannot use the NIF of a natural person. The NIF is
       stored as the :guilabel:`Tax ID` of the company, with the ES prefix. The currency is set to
       euro if no chart of accounts is loaded yet.
   * - :guilabel:`2. Fiscal profile`
     - :guilabel:`Fiscal profile` (:guilabel:`Self-employed (autónomo)` or :guilabel:`Company
       (S.L., S.A.)`), :guilabel:`SII taxpayer`, and :guilabel:`Install the modules of the profile
       now`.
     - See :ref:`localizations/spain/fiscal-profile`. The self-employed profile is refused for
       legal forms other than the self-employed person. When you continue, the missing modules are
       installed, the page reloads and the wizard resumes at the next step.
   * - :guilabel:`3. Tax regime`
     - :guilabel:`Territory`, :guilabel:`Chart of accounts`, :guilabel:`VAT regime` and, for a
       self-employed person, :guilabel:`IRPF withholding on your invoices` (:guilabel:`15 %`,
       :guilabel:`7 % (new professional)` or :guilabel:`No withholding`).
     - Only :guilabel:`Common territory (AEAT)` is available: the Canary Islands and the Basque
       Country are not available yet, and Navarre is not supported. If no chart of accounts is
       loaded yet, this step loads the one you select (:guilabel:`PGC PYMES 2008`, :guilabel:`PGC
       2008 (full)`, :guilabel:`PGC 2008 non-profit entities`, or one of the two cooperatives
       charts); afterwards the field is read-only. The :guilabel:`VAT regime` can be
       :guilabel:`General regime`, :guilabel:`Equivalence surcharge (recargo de equivalencia)`,
       :guilabel:`Agriculture, livestock and fishing (REAGYP)`, :guilabel:`Simplified regime
       (módulos)`, :guilabel:`General regime with VAT prorate` (you enter the :guilabel:`VAT prorate
       (%)`, greater than 0 and less than 100, applied from 1 January of the current year) or
       :guilabel:`Cash accounting (RECC)`, see :ref:`cash accounting regime
       <localizations/spain/cash-accounting>`. The regime is also sent to Veri*Factu as special VAT regime when it is the equivalence
       surcharge, REAGYP or the simplified regime.
   * - :guilabel:`4. Invoicing mode`
     - :guilabel:`Veri*Factu`, :guilabel:`SII (immediate supply of information)` or
       :guilabel:`Decide later`. For Veri*Factu, the :guilabel:`Veri*Factu production mode` option.
     - The step shows from which date Veri*Factu is mandatory for the company: 1 January 2027 for
       an S.L. or an S.A., and 1 July 2027 for the others. SII taxpayers are exempt. Choosing one
       mode turns the other off: a company cannot use the SII and Veri*Factu at the same time. The
       production mode is only available when the :ref:`production conditions
       <localizations/spain/veri-factu-production>` are met; otherwise the company stays in the AEAT
       test environment, and the step lists what is missing.
   * - :guilabel:`5. Invoice series`
     - :guilabel:`Invoice journal`, :guilabel:`Invoice series prefix`, :guilabel:`Separate series
       for corrective invoices` (enabled by default), and optionally :guilabel:`Separate series for
       simplified invoices (tickets)` with its prefix.
     - The prefix is at most 5 characters (default :guilabel:`F`). Invoices are numbered per series
       and year, for example *F/2027/00001*; corrective invoices use the prefix preceded by R
       (*RF/2027/00001*). Once a journal has a posted invoice, its series can no longer be changed.
       The simplified series creates a sales journal :guilabel:`Simplified invoices` (default
       prefix :guilabel:`T`).
   * - :guilabel:`6. Bank`
     - :guilabel:`IBAN`, :guilabel:`Bank journal`, :guilabel:`Bank statements` (:guilabel:`Norma
       43 / CAMT file`, :guilabel:`Online bank synchronisation` or :guilabel:`Manual`), and,
       depending on the installed modules, :guilabel:`SEPA creditor suffix`,
       :guilabel:`Confirming` and :guilabel:`Issued promissory notes (pagaré)`.
     - The IBAN is validated, and the bank is recognized for CaixaBank, Banco Santander, BBVA and
       Banco Sabadell. The bank account and the journal are created if needed. The SEPA creditor
       identifier is computed from the NIF and the three-character suffix agreed with the bank
       (default :guilabel:`000`). :guilabel:`Confirming` is offered for the banks that have a
       confirming file format installed, and uses the account 400100 :guilabel:`Suppliers,
       confirming`. :guilabel:`Issued promissory notes (pagaré)` uses an account 401 (trade bills
       payable). See :ref:`localizations/spain/promissory-notes`.
   * - :guilabel:`7. Certificate`
     - The AEAT certificate file (:file:`.p12` or :file:`.pfx`) and its password.
     - The step is shown once the modules of the profile are installed. The wizard shows the holder,
       the NIF and the expiry date of the certificate, and warns if the certificate belongs to
       someone other than the company NIF (a representative or adviser certificate only works if
       authorized at the AEAT) or expires in 30 days or less. Expired certificates are refused. One
       upload stores the certificate for Veri*Factu and, when installed, for the other AEAT
       services (SII, check of contacts). A new certificate replaces the previous one. The password
       is not kept.
   * - :guilabel:`8. Tax advisor`
     - :guilabel:`Tax advisor name` and :guilabel:`Tax advisor e-mail`.
     - Creates a user for the tax advisor (*gestoría*) with accounting access rights, or gives the
       access to an existing user with that e-mail, and sends an invitation e-mail. If the e-mail
       cannot be sent, the user is created anyway. If no contact e-mail of the AEAT declarations is
       set yet, this e-mail is used.
   * - :guilabel:`9. AEAT declarations`
     - :guilabel:`AEAT journal`, :guilabel:`VAT counterpart account`, :guilabel:`Withholding
       counterpart account`, :guilabel:`Filing frequency` (:guilabel:`Quarterly` or
       :guilabel:`Monthly`) and the contact name, phone and e-mail.
     - Shown once the AEAT modules of the profile are installed. These are the default values of
       the declarations, see :ref:`localizations/spain/aeat/configuration`.
   * - :guilabel:`Done`
     - A checklist of what is configured: NIF, logo, fiscal profile and its modules, chart of
       accounts, invoicing mode, bank account, AEAT certificate, tax advisor, AEAT journal.
     - Click :guilabel:`Create my first invoice` or :guilabel:`Finish`. Items marked with
       :guilabel:`[ ]` are still to do.

Every step that you apply or skip is written to the setup log, available in
:menuselection:`Accounting --> Configuration --> Spain --> Setup log`: date, user, step, action
(:guilabel:`Applied`, :guilabel:`Skipped` or :guilabel:`Finished`) and a summary of the values set.

.. tip::
   You do not have to use the wizard. Every value it sets can also be set in the Accounting
   settings, on the journals and on the company form.

.. _localizations/spain/fiscal-profile:

Fiscal profile
~~~~~~~~~~~~~~

The **fiscal profile** installs, in one step, the tax declarations, the books and the banking
modules that fit the taxpayer. Set it in :menuselection:`Accounting --> Configuration --> Settings`,
:guilabel:`Spain` section, :guilabel:`Fiscal profile` setting (or in step :guilabel:`2. Fiscal
profile` of the wizard):

- :guilabel:`Self-employed (autónomo)`: for a natural person.
- :guilabel:`Company (S.L., S.A.)`: for a legal entity.
- :guilabel:`SII Taxpayer`: adds the SII to the profile. Enable it for companies with a turnover
  above 6 M€, registered in the monthly VAT refund register (REDEME), members of a VAT group, or
  that opted voluntarily for the SII. SII taxpayers are exempt from Veri*Factu.

When you change the profile, a message below the setting lists the modules that will be installed.
Click :guilabel:`Save` to install them; the page reloads once the installation is done. Saving the
settings again without changing the profile installs nothing.

.. screenshot:: finance-fl-spain-fiscal-profile-settings
   :menu: Accounting ‣ Configuration ‣ Settings ‣ Spain
   :shows: The "Spain" section of the Accounting settings with the "Fiscal profile" set to "Company (S.L., S.A.)", the "SII Taxpayer" checkbox and the orange "Installed when saving" list of modules.
   :highlight: The "Fiscal profile" setting and the list of modules.
   :data: Demo company "YourCompany ES", profile just changed, not yet saved.
   :module: l10n_es
   :notes: English UI, light theme, 1440px width, crop to the "Spain" section.

Both profiles install the following modules:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Group
     - Modules
   * - AEAT framework
     - *AEAT Base* (tax maps, declaration records and export of the files), and the check of the
       contacts against the AEAT census.
   * - Contacts and banks
     - Spanish data of contacts and banks, and Spanish provinces and ZIP codes (see
       :ref:`localizations/spain/base-data`).
   * - Declarations
     - Modelos 303, 390, 111, 115, 180, 190, 347, 349 and 369. See :doc:`spain/aeat_declarations`.
   * - Books and reports
     - *Libros registro del IVA y del IRPF* (VAT and IRPF books), and the MIS Builder templates
       of the Spanish accounting reports (balance sheet, profit and loss).
   * - One-Stop-Shop (OSS)
     - The OSS extensions of the modelos 303 and 390 and of the VAT book.
   * - Veri*Factu
     - *Spain - Veri\*Factu*. Installing it does not enable it, see
       :ref:`localizations/spain/veri-factu`.

On top of that, each profile adds:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Profile
     - Additional modules
   * - :guilabel:`Self-employed (autónomo)`
     - Modelo 130 (*AEAT modelo 130*) and the Spanish Norma 43 bank statement import.
   * - :guilabel:`Company (S.L., S.A.)`
     - Modelos 123, 193, 216, 296 and 202; the VAT prorate (*Prorrata de IVA*) with its extensions
       of the modelos 303 and 390; the mercantile registry data of contacts (*Partner Mercantil*);
       the Norma 43 bank statement import; SEPA direct debit and credit transfer, payment order
       returns and the import of SEPA return reports (ISO 20022).
   * - :guilabel:`SII Taxpayer` (option, both profiles)
     - The community *Suministro Inmediato de Información en el IVA* module and its OSS,
       invoice matching and simplified invoice summary extensions, and the links between corrective
       invoices and their originals. See :doc:`spain/sii`.

The modelos 190 and 180 are the annual summaries of the modelos 111 and 115; the modelos 193 and 296
are the annual summaries of the modelos 123 and 216. The modelo 202 is the instalment payment of
the corporate income tax. Other declarations are separate modules that you can install from the
Apps menu. The details of each declaration are in :doc:`spain/aeat_declarations`.

The :doc:`Spain - Fixed Assets <spain/fixed_assets>` module is installed with the profile as well,
when it is available on the server.

.. note::
   If a module of the profile is not available on the server, saving the profile fails with a
   message that lists the missing modules. Ask your system administrator to add them.

.. _localizations/spain/base-data:

Contacts, banks and VAT numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The fiscal profile also installs these features:

- The :guilabel:`Trade name` of contacts. Contacts can also be searched by it.
- The Spanish bank directory. After the installation, the :guilabel:`Import spanish bank data`
  configuration wizard is offered: click :guilabel:`Import from Internet` (Bank of Spain, needs the
  *xlrd* Python library) or :guilabel:`Import from Local File`, or :guilabel:`Skip`.
- The Spanish provinces, municipalities and ZIP codes, used to fill in the city and the province
  from the ZIP code.
- The check of the identification data of contacts against the AEAT census: click
  :guilabel:`Check Partner Data` in the :guilabel:`AEAT` tab of a contact. To check contacts
  automatically when they are created or modified, enable :guilabel:`Verify Partner Data using AEAT
  Census` in the Accounting settings. The check uses the AEAT certificate.

The company setup wizard sets the :guilabel:`Verify VAT Numbers` option of the company (VIES
validation of intra-EU VAT numbers) from :guilabel:`Check intra-EU VAT numbers (VIES)` in step 1,
which is enabled by default. Without the wizard, set the option in the Accounting settings.

.. _localizations/spain/module-choice:

Supported module combination
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For several features, an alternative from the community localization (OCA) or from the standard
Odoo localization exists, but only one of them is supported. Odoo refuses to install the
alternative when the supported module is installed, and the other way round.

.. list-table::
   :header-rows: 1
   :widths: 22 39 39

   * - Feature
     - Supported module
     - Alternative that is refused
   * - Veri*Factu
     - *Spain - Veri\*Factu* (and *Spain - Veri\*Factu for Point of Sale*)
     - The community Veri*Factu module
   * - Facturae and FACe
     - *Spain - Facturae EDI*
     - The community Facturae and FACe modules
   * - TicketBAI
     - *Spain - TicketBAI*
     - The community TicketBAI modules (API, Batuz, Point of Sale)
   * - Point of Sale
     - *Spain - Point of Sale*
     - The community Spanish Point of Sale modules
   * - SII
     - *Suministro Inmediato de Información en el IVA* (community, on top of *AEAT Base*)
     - *Spain - SII EDI Suministro de Libros*
   * - Modelo 130
     - *AEAT modelo 130* (community)
     - *Spain - Modelo 130 Tax report*
   * - EU One-Stop-Shop (OSS)
     - *L10n EU OSS OCA*, used by the OSS versions of the AEAT declarations
     - *EU One Stop Shop (OSS)* and, as it depends on it, the Hungarian OSS bridge
   * - Fixed assets
     - :doc:`Spain - Fixed Assets <spain/fixed_assets>`
     - The community fixed asset modules (*Assets Management* and its Spanish version)

The community Veri*Factu, Facturae, TicketBAI and Point of Sale modules, and the community Spanish
fixed asset module, are refused as long as *Spain - Accounting (PGCE 2008)* is installed. The other
alternatives are refused only once the supported module of the pair (*AEAT Base*, *L10n EU OSS OCA*
or *Spain - Fixed Assets*) is installed: the standard OSS module, for example, remains available for
a Hungarian company that does not use the Spanish OSS. The refusal applies to installations from the
Apps menu and from the command line. It shows the message *The Spanish localisation supports one
module of each of these pairs only* or the message that Odoo shows for incompatible modules.

.. warning::
   If an alternative module is already installed, uninstall it before installing the supported one.
   Ask your system administrator before uninstalling a module, as its data is deleted. If a
   database already contains both modules of a pair, Odoo does not block other installations, but
   it writes a warning in the server log when one of them is updated.

.. _localizations/spain/promissory-notes:

Promissory notes and confirming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A vendor bill that is settled with a promissory note (*pagaré*) or a confirming remittance is not
paid until the bank debits the amount (Código Civil art. 1170). In Spanish companies, the bill
therefore stays :guilabel:`In Payment` while the payment is registered on a payable account, such as
the account 401 of the promissory notes or the account 400100 of the confirming, and it is not
reconciled with the bank statement line. It becomes :guilabel:`Paid` when you reconcile the bank
debit.

The bank step of the :ref:`setup wizard <localizations/spain/setup-wizard>` sets up the payment
method and the account of the bank journal for you.

.. seealso::
   - :doc:`spain/aeat_declarations`
   - :doc:`spain/sii`
   - :doc:`spain/cash_accounting`
   - :doc:`Spanish remittances per bank <../accounting/payments/spanish_remittances>`
   - :doc:`Norma 43 statement import <../accounting/bank/statement_import>` and :doc:`online bank
     synchronization with Enable Banking <../accounting/bank/enable_banking>`
   - :doc:`Redsys card payments and Bizum <../payment_providers/redsys>`

Chart of accounts
=================

You can reach the **Chart of Accounts** by going to :menuselection:`Accounting --> Configuration -->
Accounting: Chart of Accounts`.

.. tip::
    When a new database is created for a Spanish company, **Spain - SMEs (2008)** is installed by
    default.

Taxes
=====

Default Spain-specific taxes are created automatically when the
:guilabel:`Spanish - Accounting (PGCE 2008) (l10n_es)` module is installed. Each tax is mapped to
the boxes of the Spanish **Modelo 303** VAT return, which can be reviewed in the :doc:`tax report
<../accounting/reporting/dynamic_reports>`.

.. tip::
   With the :ref:`Spanish setup <localizations/spain/base-layer>` (fiscal profile), the AEAT tax
   declarations (modelos 303, 390, 111, 115, 347, 349, and others), the VAT books, and the official
   PGC annual accounts are prepared in the Accounting app. See :doc:`spain/aeat_declarations`.

.. _localizations/spain/vat-regime:

VAT regime
----------

The :guilabel:`VAT regime` of the company is set in :menuselection:`Accounting --> Configuration
--> Settings`, :guilabel:`Spain` section (or in step :guilabel:`3. Tax regime` of the :ref:`company
setup wizard <localizations/spain/setup-wizard>`). Of the available regimes, only the **cash
accounting regime (RECC)** changes how the taxes of the invoices are chosen: with it, the domestic
VAT of sales and purchases is due on payment. See :doc:`spain/cash_accounting`.

.. _localizations/spain/sii:

SII (Suministro Inmediato de Información)
=========================================

The *Spain - SII EDI Suministro de Libros* (`l10n_es_edi_sii`) module sends the VAT information of
customer invoices and vendor bills to the SII (*Llevanza de libros registro*) of the AEAT or of the
regional tax agencies. It is mandatory for companies with a turnover above 6 M€ and optional for
the others.

.. important::
   This module cannot be installed together with *AEAT Base* (`l10n_es_aeat`), which the
   :ref:`fiscal profile <localizations/spain/fiscal-profile>` installs. With the fiscal profile
   (option :guilabel:`SII Taxpayer`), the SII is handled by the community *Suministro Inmediato de
   Información en el IVA* module, see :doc:`spain/sii`. Use the module described in this section
   only on databases without the Spanish AEAT modules.

Configuration
-------------

#. :ref:`Install <general/install>` the :guilabel:`Spain - SII EDI Suministro de Libros
   (l10n_es_edi_sii)` module.
#. Go to :menuselection:`Accounting --> Configuration --> Settings`, scroll to the
   :guilabel:`Registro de Libros connection SII` setting and select the :guilabel:`Tax Agency for
   SII` (:guilabel:`Agencia Tributaria española`, :guilabel:`Hacienda Foral de Gipuzkoa`,
   :guilabel:`Hacienda Foral de Bizkaia`, or :guilabel:`Hacienda Foral de Navarra`).
#. Click the :guilabel:`Certificate (SII)` link to upload the company's digital certificate (file
   and password) used to sign the requests.
#. Keep :guilabel:`SII Test Mode` enabled while testing; disable it to send the data to the
   production web service.
#. On each sales and purchase journal that must report to the SII, enable the :guilabel:`SII IVA
   Llevanza de libros registro (ES)` format in the :guilabel:`Electronic invoicing` field of the
   :guilabel:`Advanced Settings` tab.

.. screenshot:: finance-fl-spain-sii-settings
   :menu: Accounting ‣ Configuration ‣ Settings ‣ Registro de Libros connection SII
   :shows: The "Registro de Libros connection SII" setting with the "Certificate (SII)" link, the "Tax Agency for SII" drop-down set to "Agencia Tributaria española" and the "SII Test Mode" checkbox enabled.
   :highlight: The "Tax Agency for SII" field.
   :data: Demo company "YourCompany ES", Spanish localization installed; test certificate.
   :module: l10n_es_edi_sii
   :notes: English UI, light theme, 1440px width; use a throw-away certificate.

Taxes
-----

The Spanish taxes carry a :guilabel:`Tax Type (Spain)` (:guilabel:`Sujeto`, :guilabel:`Exento`,
:guilabel:`Sujeto ISP`, :guilabel:`No Sujeto`, :guilabel:`Retencion`, :guilabel:`Recargo de
Equivalencia`, :guilabel:`DUA`, …), an :guilabel:`Exempt Reason (Spain)` for exempt taxes (E1 … E6) and
the :guilabel:`Bien de Inversion` flag, which determine how the amounts are reported to the SII.
The default taxes are configured; check these fields when creating new taxes.

Sending documents
-----------------

Once a customer invoice or vendor bill is posted in a journal with the SII format enabled, it is
sent to the SII by the scheduled action of the electronic invoicing (or immediately with the
:guilabel:`Process now` link of the blue banner). The status is shown in the
:guilabel:`Electronic invoicing` field; the CSV return code and the acceptance message (or the
errors reported by the agency) are logged in the chatter. The :guilabel:`Registration Date` field
of the document (Other Info tab) is the date reported as *fecha de registro contable* for vendor
bills.

.. _localizations/spain/veri-factu:

Veri*Factu
==========

.. note::
   The Veri*Factu invoicing system used by eYssen is declared to the AEAT by its producer, which
   issues the *declaración responsable* (responsible declaration) of each release. The declaration
   is available inside the application, see :ref:`localizations/spain/veri-factu-declaration`.

**Veri*Factu** is an e-Invoicing system used by the Spanish Tax Agency. It is mandatory for most
taxpayers in Spain, except for those who use the SII system or are under a regional tax regime
(i.e., TicketBai).

Odoo allows :ref:`invoices <localizations/spain/veri-factu-invoices>` and Point of Sale :ref:`orders
<localizations/spain/veri-factu-orders>` to be automatically sent to the tax authorities.

.. _localizations/spain/veri-factu-configuration:

Configuration
-------------

To enable **Veri\*Factu**, follow these steps:

#. Open the Settings app to make sure your company's :guilabel:`Country` and :guilabel:`Tax ID` are
   correctly set in the :ref:`Companies <general/companies/company>` section.
#. :ref:`Install <general/install>` the :guilabel:`Spain - Veri*Factu (l10n_es_edi_verifactu)`
   module, if it is not installed yet (the :ref:`fiscal profile
   <localizations/spain/fiscal-profile>` installs it).
#. Go to :menuselection:`Accounting --> Configuration --> Settings`, scroll to the
   :guilabel:`Veri\*Factu` section, check the :guilabel:`Enable Veri*Factu` option, and click
   :icon:`oi-arrow-right` :guilabel:`Manage certificates` to add a certificate.
#. In the :guilabel:`Certificates for Veri\*Factu` list view, click :guilabel:`New`.
#. Click :guilabel:`Upload your file`, then select a certificate file and enter the
   :guilabel:`Password` needed to open the certificate (if there is one).

.. note::
   - At least one certificate has to be uploaded.
   - By default Veri*Factu is in testing mode. The data is sent to test servers
     and is not considered official. When official data can be sent to the production servers, go to
     the :guilabel:`Veri\*Factu` section in the :guilabel:`Settings` and disable :guilabel:`Test
     Environment`. This is only possible when the :ref:`production conditions
     <localizations/spain/veri-factu-production>` are met.
   - Veri*Factu cannot be enabled on a company that uses the SII: SII taxpayers are exempt.

.. _localizations/spain/veri-factu-invoices:

Invoices
--------

Once an :doc:`invoice <../../finance/accounting/customer_invoices>` is confirmed, it can be
:ref:`sent <accounting/invoice/sending>`. In the :guilabel:`Send` window, the Veri*Factu option is
available if Veri*Factu has been enabled.

Click :guilabel:`Send` to generate a JSON file containing the invoice details. This file is stored
as a Veri*Factu document. In the :guilabel:`Veri*Factu` tab, all corresponding documents are
listed by their creation date and current status.

.. tip::
   To download a JSON file, click on its document in the :guilabel:`Veri*Factu` tab. Then, in
   the :guilabel:`Open: Veri*Factu Documents` window, click the link in the :guilabel:`JSON` field.

.. note::
   - The document should be sent to the :abbr:`AEAT (Agencia Estatal de Administración Tributaria)`
     immediately. However, it may be delayed due to mandatory waiting periods between submissions
     required by the :abbr:`AEAT (Agencia Estatal de Administración Tributaria)`. In such cases,
     the document is automatically sent the next time a scheduled action runs.
   - A Veri\*Factu **QR code** appears on the invoice PDF. Scan this code to verify that the invoice
     has been received and recognized by the :abbr:`AEAT (Agencia Estatal de Administración
     Tributaria)`.

.. _localizations/spain/veri-factu-orders:

Point of sale orders
--------------------

Once an order has been :ref:`paid <pos/sell>`, a JSON file containing the order details is
generated. This file is stored as a Veri*Factu document.

Go to :menuselection:`Point of Sale --> Orders --> Orders`. In the :guilabel:`Orders` list view,
select the relevant order. In the :guilabel:`Veri*Factu` tab, all the corresponding documents are
listed by their creation date and current status.

.. tip::
   To download a JSON file, click on its document in the :guilabel:`Veri*Factu` tab. Then, in
   the :guilabel:`Open: Veri*Factu Documents` window, click the link in the :guilabel:`JSON` field.

.. note::
   - The document should be sent to the :abbr:`AEAT (Agencia Estatal de Administración Tributaria)`
     immediately. However, it may be delayed due to mandatory waiting periods between submissions
     required by the :abbr:`AEAT (Agencia Estatal de Administración Tributaria)`. In such cases,
     the document is automatically sent the next time a scheduled action runs.

If an invoice is generated for an order during the payment process, the Veri*Factu document is
:ref:`created and sent for the invoice <localizations/spain/veri-factu-invoices>` instead.

.. note::
   A Veri\*Factu **QR code** appears on the order receipt, even if an invoice is created for the
   order. Scan this code to verify that the invoice has been received and recognized by the
   :abbr:`AEAT (Agencia Estatal de Administración Tributaria)`

.. _localizations/spain/veri-factu-declaration:

Software producer and responsible declaration
---------------------------------------------

The regulation requires the producer of a Veri*Factu system to declare the compliance of the system
(*declaración responsable*) and to make the declaration easy to reach from inside the system. In
eYssen, the producer of the fork is built into the release: the data sent to the AEAT in the
*SistemaInformatico* block of each record (producer, system name, software version, installation
number) cannot be edited in the interface. The installation number is unique per database and per
company.

.. important::
   After cloning a database (for example, to create a test copy), the database UUID must be
   regenerated. Otherwise the clone reports the same installation numbers as the original.

To read the declaration of the version you are running, use any of these entries:

- the user menu (your name at the top right), :guilabel:`Veri*Factu Responsible Declaration`;
- :menuselection:`Settings --> General Settings`, :guilabel:`About` section, :guilabel:`Veri*Factu`
  setting, :guilabel:`Responsible declaration` link. The setting also shows the software producer
  and the version of the software;
- :menuselection:`Accounting --> Configuration --> Settings`, :guilabel:`Veri*Factu` section, with
  the same producer, version and :guilabel:`Responsible declaration` link;
- :menuselection:`Accounting --> Configuration --> Veri*Factu (Spain) --> Responsible Declaration`.

.. screenshot:: finance-fl-spain-verifactu-settings
   :menu: Accounting ‣ Configuration ‣ Settings ‣ Veri*Factu
   :shows: The "Veri*Factu" section of the Accounting settings with "Enable Veri*Factu", "Manage certificates", the "Test Environment" checkbox, the "Production mode is not available" warning with its list of problems, the "Software producer" and "Version" lines and the "Responsible declaration" link.
   :highlight: The warning, the producer lines and the "Responsible declaration" link.
   :data: Demo company "YourCompany ES", development version (no published declaration).
   :module: l10n_es_edi_verifactu
   :notes: English UI, light theme, 1440px width, crop to the Veri*Factu section.

The declaration opens as a PDF (:file:`Declaracion_responsable_VeriFactu`), always in Spanish. It is
generated from the declaration file that ships with each release
(:file:`declarations/<version>.json` in the Veri*Factu module), which lists the producer, the
system, the place and date, and the Veri*Factu modules and their versions. Releases have an
identifier such as *18.0.es.2026.10.0*.

.. warning::
   If there is no published declaration for the version that is running, for example on a
   development version, the PDF is a **draft marked "BORRADOR – SIN VALIDEZ"** (draft, without
   validity) that lists the problems found. Do not give such a draft to customers or to the tax
   agency.

.. _localizations/spain/veri-factu-production:

Production mode
---------------

The :guilabel:`Test Environment` option of the :guilabel:`Veri*Factu` section of the Accounting
settings is enabled by default: the records are sent to the AEAT test servers. The production mode
(sending real records to the AEAT) is only allowed when all of these conditions are met:

- the producer data is complete;
- the running code is an ES release (identifier :samp:`18.0.es.{YYYY}.{MM}.{N}`), not a development
  version;
- the responsible declaration of the running version exists and matches the data that is sent to
  the AEAT.

As long as a condition is not met:

- the :guilabel:`Test Environment` option is read-only and a warning, :guilabel:`Production mode is
  not available`, lists the problems below the option. Records are still sent to the test servers,
  with the data shown in the section;
- Odoo refuses to generate or send production records, with the message *Veri\*Factu production
  submission is blocked until the software producer data is complete* followed by the list of
  problems;
- accounting managers see a warning in the :ref:`pending records indicator
  <localizations/spain/veri-factu-pending>`.

.. note::
   A company that already sent production records with an earlier version is not switched back to
   the test environment when the module is upgraded, but its records are not sent until the
   conditions above are met. A warning is written in the server log.

.. _localizations/spain/veri-factu-pending:

Pending records and submission
------------------------------

A record is generated when an invoice is sent from the :guilabel:`Send` window or a point of sale
order is paid, and it is sent to the AEAT afterwards. The AEAT imposes waiting times between
submissions, and a submission can fail when the AEAT or the network is unavailable. A record that is
not sent yet is *pending*.

- A scheduled action, :guilabel:`Veri*Factu: Submit / Cancel Records`, retries the pending records
  **every hour**. On databases that were installed with an earlier version, the upgrade sets the
  hourly interval.
- A **paper plane icon** in the top bar (systray) shows the number of pending records on a red
  badge, for the users of the companies that have Billing access rights. It is refreshed every five
  minutes and is only shown when records are pending or a warning exists. Hover over it to see the
  details. Click it to open the list :guilabel:`Veri*Factu Records Pending Submission` (creation
  date, company, journal entry, document type, chain index and state).
- If the production conditions above are not met, accounting managers see the icon turn into a
  warning triangle. When there are no pending records, clicking it opens the Accounting settings.
- The same list is available in :menuselection:`Accounting --> Configuration --> Veri*Factu (Spain)
  --> Pending Records`.

If a record is sent more than **240 seconds** after it was generated (for example because the AEAT
was unavailable or Odoo was not running), it is sent flagged as an *incident* (*Incidencia = S*)
automatically, so that the AEAT does not register it with error 2004. Nothing has to be done.

TicketBAI
=========

`Ticket BAI <https://www.gipuzkoa.eus/es/web/ogasuna/ticketbai>`_ or **TBAI** is an e-Invoicing
system used by the Basque government and its three provincial councils (Álava, Biscay, and
Gipuzkoa).

Odoo supports the **TicketBAI (TBAI)** electronic invoicing format for all three regions of the
**Basque Country**. To enable **TicketBAI**, set your company's :guilabel:`Country` and
:guilabel:`Tax ID` under :menuselection:`Settings --> General Settings` in the :guilabel:`Companies`
section.

Then, :ref:`install <general/install>` the module :guilabel:`Spain -TicketBAI (l10n_es_edi_TBAI)`,
go to :menuselection:`Accounting --> Configuration --> Settings`, and select a **region** in the
:guilabel:`Spain Localization` section's :guilabel:`Tax Agency for TBAI` field.

Once a region is selected, click :guilabel:`Manage certificates (SII/TicketBAI)`, then click
:guilabel:`New`, upload the certificate, and enter the password provided by the tax agency.

.. warning::
   If you are testing certificates, enable :guilabel:`Test Mode` in the
   :guilabel:`Spain Localization` section, which can be found under :guilabel:`Accounting` in
   the **Settings** app.

Use case
--------

Once an invoice has been :doc:`created <../../finance/accounting/customer_invoices>` and confirmed,
a TicketBAI **banner** appears at the top.

.. screenshot:: finance-fl-spain-ticketbai-invoice
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (a sent invoice)
   :shows: A posted invoice of a Basque company with the blue TicketBAI banner at the top stating that the invoice was sent to the tax agency, and the TicketBAI status.
   :highlight: The TicketBAI banner.
   :data: Demo company "YourCompany ES" (Bizkaia), TicketBAI test mode.
   :module: l10n_es_edi_tbai
   :notes: English UI, light theme, 1440px width.

Odoo sends invoices through TicketBAI automatically every **24 hours**. However, you can click
:guilabel:`Process now` to send the invoice immediately.

When the invoice is **sent**, the status of the field :guilabel:`Electronic Invoice` changes to
:guilabel:`Sent`, and the XML file can be found in the **chatter**. Under the
:guilabel:`EDI Documents` tab, you can see the traceability of other generated documents related to
the invoice (e.g., if the invoice should also be sent through the **SII**, it will appear here).

.. note::
   The TBAI **QR code** is displayed on the invoice PDF.

   .. screenshot:: finance-fl-spain-qr-code
      :menu: Accounting ‣ Customers ‣ Invoices ‣ (a sent invoice) ‣ Print
      :shows: The printed invoice PDF with the TicketBAI QR code and TBAI identifier in the footer.
      :highlight: The QR code.
      :data: Demo company "YourCompany ES" (Bizkaia).
      :module: l10n_es_edi_tbai
      :notes: English UI, light theme, 1440px width.

FACe
====

`FACe <https://face.gob.es/en>`_ is the e-Invoicing platform used by the public administrations in
Spain to send electronic invoices.

Before configuring the :abbr:`FACe (General Entrance for Electronic Invoices)` system,
:ref:`install <general/install>` the :guilabel:`Spain - Facturae EDI (l10n_es_edi_facturae)` module
and other **Facturae EDI**-related modules.

To configure FACe, follow these steps:

#. Go to :menuselection:`Accounting --> Configuration --> Certificates`.
#. Click :guilabel:`New` to create a new certificate.
#. Complete the fields, including uploading the file of the :guilabel:`Certificate` provided by the
   tax agency and the provided :guilabel:`Certificate Password`.

.. note::
   If using the Invoicing app instead of Accounting, go to :menuselection:`Invoicing -->
   Configuration --> Certificates`.

Use case
--------

Once you have :doc:`created <../../finance/accounting/customer_invoices>` an invoice and confirmed
it, click :guilabel:`Send & Print`. Make sure :guilabel:`Generate Facturae edi file` is enabled, and
click :guilabel:`Send & Print` again. Once the invoice is sent, the generated XML file is available
in the **chatter**.

.. warning::
   The file is **NOT** automatically sent. You have to send it yourself manually.

.. tip::
   You can send **FACe** XML files in batch through `the governmental portal <https://www.facturae.gob.es/formato/Paginas/descarga-aplicacion-escritorio.aspx>`_.

Administrative centers
----------------------

In order for **FACe** to work with **administrative centers**, the invoice *must* include specific
data about the centers.

.. note::
   Make sure to have the :guilabel:`Spain - Facturae EDI - Administrative Centers Patch
   (l10n_es_edi_facturae_adm_centers)` module :ref:`installed <general/install>`.

To add **administrative centers**, create a new **contact** to add to the **partner** company.
Select :guilabel:`FACe Center` as the **type**, assign one or more **role(s)** to that contact, and
:guilabel:`Save`. The **three** roles usually required are:

- Órgano gestor: :guilabel:`Receptor` (Receiver);
- Unidad tramitadora: :guilabel:`Pagador` (Payer);
- Oficina contable: :guilabel:`Fiscal` (Fiscal).

.. screenshot:: finance-fl-spain-administrative-center
   :menu: Contacts ‣ (a public entity) ‣ Administrative Centers
   :shows: The contact form of a public administration with the "Administrative Centers" section: a center with its "Center Code" (DIR3), role (Órgano gestor / Unidad tramitadora / Oficina contable) and address.
   :highlight: The administrative center lines.
   :data: Public entity "Ayuntamiento de Ejemplo", 3 DIR3 codes.
   :module: l10n_es_edi_facturae
   :notes: English UI, light theme, 1440px width.

.. tip::
   - If administrative centers need different :guilabel:`Codes` per role, you *must* create
     different centers for each role.
   - When an electronic invoice is created using a partner with **administrative centers**, *all*
     administrative centers are included in the invoice.
   - You can add one contact with multiple roles or multiple contacts with a different role each.

.. toctree::
   :titlesonly:

   spain/aeat_declarations
   spain/cash_accounting
   spain/sii
   spain/fixed_assets

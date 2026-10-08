.. _localizations/romania/declarations:

========================
ANAF declarations (base)
========================

The :guilabel:`Romania - ANAF Declarations Base` (`l10n_ro_declaration`) module is the common
framework of the Romanian tax declarations filed with :abbr:`ANAF (Agenția Națională de Administrare
Fiscală, National Agency for Fiscal Administration)`. Each declaration has its own module, which
computes the declaration from the posted journal items of the period, builds the official XML file,
and checks it before it is filed. The base module provides what all of them share: the period and
deadline handling, the status flow, the validation messages, the declarant data, the validation of
the XML against the official schema, and the connection to the ANAF validator *DUKIntegrator*.

.. list-table::
   :header-rows: 1
   :widths: 14 30 26 30

   * - Declaration
     - Content
     - Legal basis
     - Module
   * - :doc:`D300 <d300>`
     - VAT return (*Decont de TVA*), monthly, quarterly, semi-annual or annual, with the
       reconciliation with the ANAF e-TVA pre-filled return.
     - OPANAF 174/2026, periods from January 2026.
     - `l10n_ro_d300`
   * - :doc:`D390 <d390>`
     - Recapitulative statement of the intra-Community operations (*Declarația recapitulativă*,
       VIES), monthly.
     - OPANAF 705/2020.
     - `l10n_ro_d390`
   * - :doc:`D394 <d394>`
     - Informative statement on the domestic supplies and acquisitions (*Declarația informativă*).
     - OPANAF 3769/2015 as replaced by OPANAF 2194/2025, operations from August 2025.
     - `l10n_ro_d394`
   * - :doc:`D406 <saft_d406>`
     - SAF-T file (*Fișierul Standard de Control Fiscal*).
     - See the :doc:`SAF-T page <saft_d406>`.
     - `l10n_ro_d406`
   * - :doc:`D101 <d101>`
     - Annual profit tax return, and helper for the quarterly micro-enterprise tax.
     - OPANAF 206/2025, reporting year 2025.
     - `l10n_ro_d101`
   * - :doc:`S1002 to S1005, S1027 <financial_statements>`
     - Annual financial statements and annual accounting reports, and the half-year report.
     - OMF 2036/2025 (financial year 2025), OMF 1194/2025 (half-year report).
     - `l10n_ro_financial_statements`

The declarations are installed from the :guilabel:`Apps` menu; :ref:`install <general/install>`
the module of each declaration. The base module is installed automatically as a dependency. The
D390 and D394 modules require the D300 module (they check their totals against the VAT return of the
same period), and the D101 module requires the financial statements module.

.. important::
   - The declarations are available only for companies whose **fiscal country** is Romania and whose
     currency is **RON**. A declaration cannot be created for another company, and the computation
     is refused if the company currency is not RON.
   - The amounts of the declarations are rounded to whole lei (half up), as required by the ANAF
     forms.
   - The declarations are prepared in Odoo, but **filing them with ANAF is a manual step** outside
     Odoo, see :ref:`localizations/romania/declarations/filing`.

.. _localizations/romania/declarations/configuration:

Configuration
=============

Company data
------------

Go to :menuselection:`Accounting --> Configuration --> Settings` and scroll to the :guilabel:`Romanian
ANAF Declarations` section, which is displayed for Romanian companies. The values are stored on the
company and proposed on every new declaration.

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Setting
     - Fields
     - Used for
   * - :guilabel:`Declarant`
     - :guilabel:`Declarant Last Name`, :guilabel:`Declarant First Name`, :guilabel:`Declarant
       Position`, :guilabel:`Declarant CNP/CUI`, :guilabel:`Declarant Phone`, :guilabel:`Declarant
       Email`
     - The person who signs the declarations (*nume*, *prenume*, *funcție*). The last name, first
       name and position are mandatory: the validation fails if one of them is empty. The phone and
       email default to those of the company.
   * - :guilabel:`Activity and VAT Period`
     - :guilabel:`Main CAEN Code`, :guilabel:`VAT Period`, :guilabel:`Declaration Bank Account`
     - The CAEN code of the main activity actually carried out (exactly 4 digits); the VAT period
       (:guilabel:`Monthly`, :guilabel:`Quarterly`, :guilabel:`Semi-annual` or :guilabel:`Annual`),
       which is proposed as the period type of new declarations; and the bank account printed on the
       declarations (by default, the first bank account of the company).
   * - :guilabel:`Fiscal Representative`
     - :guilabel:`Representative Name`, :guilabel:`Representative CUI/CNP`, :guilabel:`Representative
       Address`
     - Optional. The proxy (*împuternicit*) who files the declarations on behalf of the company.
   * - :guilabel:`DUKIntegrator Validation`
     - :guilabel:`DUK Validator Service URL`, :guilabel:`DUK Validator Service Token`,
       :guilabel:`Request DUK PDF`
     - The connection to the ANAF validator, see :ref:`localizations/romania/declarations/duk`.

The declaration modules add their own settings to this section; for example, the D394 module adds
the data of the person who prepares the declaration.

The company needs a valid :abbr:`CUI (Cod Unic de Identificare, fiscal identification code)` in its
:guilabel:`Tax ID` field: the validation checks its control digit. A company whose Tax ID does not
start with `RO` is not registered for VAT, and the VAT declarations show a warning.

Access rights
-------------

The menu :menuselection:`Accounting --> Romania (ANAF)` is displayed to the users who have access to
a company whose fiscal country is Romania and who have an accounting access right. Accountants can
create and modify the declarations, users with read-only accounting access can only read them, and
accounting advisers (managers) can also delete them and edit the configuration. A user only sees the
declarations of the companies selected in the company switcher.

Tax codes and mapping rules
---------------------------

The declarations do not read the taxes directly. Every tax of the Romanian chart of accounts is
linked to a **Romanian tax code**, which tells each declaration where the operation is reported: the
rows of the D300, the operation type of the D390, and so on. The link is the :guilabel:`Romanian Tax
Code` field of the tax (:menuselection:`Accounting --> Configuration --> Taxes`), which is filled in
automatically for the taxes of the Romanian chart of accounts.

Accounting advisers can review and complete the catalogue in :menuselection:`Accounting --> Romania
(ANAF) --> Configuration` (this menu is reserved to them):

- :guilabel:`Romanian Tax Codes`: the codes, with the VAT rate, the kind of operation and the D300,
  D390 and D394 treatment of each code. This is global master data, shared by all companies.
- :guilabel:`Tax Mapping Rules`: rules that assign a tax code to an operation according to the tax,
  the type of document, the fiscal position, the location of the partner (Romania, EU, non-EU), the
  product category or a date range. They are used, for example, for the historic taxes at 19%, 9% and
  5%, and for the VAT on payment taxes.

.. note::
   If a tax used in the period has no tax code and no rule, the declaration shows an error message
   and the operation is left out. Link the tax to a code, or create a rule, and compute the
   declaration again.

.. _localizations/romania/declarations/usage:

Prepare a declaration
=====================

All the declarations work in the same way. Open the declaration from :menuselection:`Accounting -->
Romania (ANAF) --> Declarations` and click :guilabel:`New`.

#. Choose the period. The :guilabel:`Period Type` is proposed from the :guilabel:`VAT Period` of the
   company, and the year and the period number from the last finished period. The form shows the
   dates of the period (:guilabel:`Period`) and the legal :guilabel:`Deadline`. The declarant data
   is copied from the company and can be changed on the declaration.
#. Click :guilabel:`Compute`. The rows of the declaration are filled in from the posted journal
   items of the period, and the declaration moves to the :guilabel:`Computed` status. The local
   checks run at the same time and their findings are listed in the :guilabel:`Validation` tab.
#. Review the rows and complete the data that cannot be computed from the accounting. Edited values
   are kept when the declaration is recomputed with :guilabel:`Recompute`.
#. Click :guilabel:`Validate`. Odoo runs the local checks again, builds the XML, checks it against
   the official XSD schema, and, if the DUK validator is configured, validates it with
   DUKIntegrator. If no finding is an error, the declaration moves to :guilabel:`Validated`;
   otherwise it stays :guilabel:`Computed`.
#. Click :guilabel:`Export XML`. The XML file is attached to the declaration and downloaded, and the
   declaration moves to :guilabel:`Exported`.
#. File the declaration with ANAF (see :ref:`localizations/romania/declarations/filing`), then click
   :guilabel:`Mark as Submitted`.

The XML file is named `<form>_<CUI>_<period>_v<version>.xml`, for example `D300_12345678_2026-01_v1.xml`
(`2026-T1` for a quarter, `2026-S1` for a semester, `2026` for a year).

Statuses and buttons
--------------------

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Status
     - Meaning
   * - :guilabel:`Draft`
     - The declaration is created but not computed. The period can still be changed.
   * - :guilabel:`Computed`
     - The rows are computed. Click :guilabel:`Recompute` after correcting the accounting, or
       :guilabel:`Validate` to check the declaration.
   * - :guilabel:`Validated`
     - The validation found no error. :guilabel:`Revalidate` runs it again.
   * - :guilabel:`Exported`
     - The XML file is generated. :guilabel:`Export XML Again` replaces the attached file.
   * - :guilabel:`Submitted`
     - You marked the declaration as filed. The :guilabel:`Submission Date` is set to today unless
       you filled it in, and the :guilabel:`Registration Number` received from ANAF can be entered
       in the :guilabel:`Validation` tab.
   * - :guilabel:`Archived`
     - A declaration replaced by a later version, or archived with :guilabel:`Archive`.

:guilabel:`Reset to Draft` is available in the :guilabel:`Computed`, :guilabel:`Validated` and
:guilabel:`Exported` statuses and deletes the computed content and the messages. Only declarations
that are not yet exported can be deleted. A declaration of the same company, period type, period,
declaration type and version cannot exist twice.

Deadlines
---------

The :guilabel:`Deadline` is computed from the end of the period. If it falls on a weekend or on a
Romanian public holiday (calendar of the :doc:`localization base <base>`), it moves to the next
working day.

- D300 and D390: the 25th of the month following the period.
- D394: the 30th of the month following the period.
- D101: the 25th of June of the following year.
- Annual financial statements: 150 days after the end of the year; half-year report: 45 days.

Corrections
-----------

A declaration that is exported, submitted or archived cannot be modified. To correct it, click
:guilabel:`Create Rectificative` (:guilabel:`Create Corrected Declaration` in the D394). Odoo copies
the declaration as a new version of the same period (:guilabel:`Declaration Type`
:guilabel:`Rectificative`, :guilabel:`Version` + 1), linked to the declaration it corrects, and you
compute, validate, export and file it like the first one. When the corrected version is marked as
submitted, the previous versions are archived. The exact content of a rectificative depends on the
declaration: see its page.

Validation messages
-------------------

The findings of the checks are saved as validation messages. The buttons :guilabel:`Errors` and
:guilabel:`Warnings` at the top of the declaration open them, and :menuselection:`Accounting -->
Romania (ANAF) --> Validation Messages` lists those of all the declarations, with filters on the
severity and on the source of the message (:guilabel:`XSD`, :guilabel:`DUKIntegrator`, or the local
checks). Each message has a code, the row concerned and, when it applies, the journal entry and the
partner, to open them directly.

An **error** blocks the validation. A **warning** does not: read it, and correct the accounting or
the declaration if it is justified.

.. _localizations/romania/declarations/duk:

Validation with DUKIntegrator
=============================

*DUKIntegrator* is the Java program with which ANAF checks the declarations before they are filed;
it contains the official validation rules of each form. Odoo checks every XML against the XSD schema
bundled with the module on its own, but the ANAF rules are stricter. Odoo therefore sends the XML to
a small **DUK validator service**, which runs DUKIntegrator and returns the result. The service is
shipped with the module in `addons/l10n_ro_declaration/tools/duk_service` and is installed
separately from Odoo, on a server that can reach `static.anaf.ro`.

.. note::
   The ANAF programs (jar files) are not part of the module and are not redistributed: they are
   downloaded from the ANAF website with the script provided.

What the validation checks
--------------------------

When you click :guilabel:`Validate`, Odoo runs three checks in this order and records the result in
the :guilabel:`Validation` tab:

#. The **local checks** of the declaration (company data, declarant, rules of the form,
   cross-checks with other declarations).
#. The **XSD check** (:guilabel:`XSD Check`): :guilabel:`Valid`, :guilabel:`Invalid`, or
   :guilabel:`Schema missing`.
#. The **DUKIntegrator check** (:guilabel:`DUK Validation`).

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - :guilabel:`DUK Validation`
     - Meaning
   * - :guilabel:`Valid`
     - DUKIntegrator answered `ok`: it found no error and no warning. This is the result to expect
       before filing.
   * - :guilabel:`Valid with warnings`
     - DUKIntegrator reported only warnings (`W:`, `A:` or `I:` lines). The warnings are listed in the
       messages and do not block the validation.
   * - :guilabel:`Errors`
     - DUKIntegrator reported at least one error (`E:` or `F:` lines, or an unreadable result). The
       errors are listed in the messages and block the validation: correct them and click
       :guilabel:`Revalidate`.
   * - :guilabel:`Not configured`
     - No service URL is configured. The step is skipped, **without any message**, and the
       declaration can reach the :guilabel:`Validated` status without having been checked by ANAF's
       rules.
   * - :guilabel:`Service unavailable`
     - The service did not answer, answered with an error (for example, the token is wrong), or
       DUKIntegrator could not run (for example, the validator of the form is not installed). Odoo
       records a warning, which does not block the validation.

.. warning::
   :guilabel:`Validated` only means that Odoo found no error. If :guilabel:`DUK Validation` is
   :guilabel:`Not configured` or :guilabel:`Service unavailable`, the declaration has **not** been
   validated by DUKIntegrator. Install the service and make sure the status is :guilabel:`Valid`
   before filing.

When :guilabel:`Request DUK PDF` is ticked (the default), the service also returns the official PDF
produced by ANAF's program, with the XML attached, if the validation succeeds. It is attached to the
declaration as :guilabel:`DUK PDF`. The D101 and the financial statements are validated without the
PDF: ANAF's PDF of these forms contains the annexes of the declaration (notes, reports), which are
assembled with the ANAF assistance program.

Install the DUK validator service
---------------------------------

The service needs Java (OpenJDK 21 was used to verify it) and Python 3, and it is started with the
files of ANAF in one folder (`DUK_HOME`). The module provides a `Dockerfile` that contains Java and
Python.

#. **Download the ANAF programs.** On a machine that can reach `static.anaf.ro`, run the script
   `download_duk.sh` of the service folder with the destination folder and the forms to validate:

   .. code-block:: console

      $ ./download_duk.sh /srv/duk D300 D390 D394 D406

   The script downloads `DUKIntegrator.jar`, its libraries, the configuration, and the validator
   and PDF jars of every requested form (`D300Validator.jar`, `D300Pdf.jar`...) from the update feed
   of ANAF (`versiuni.xml`). Request all the forms that you use; for example, add `D101`, `S1002`,
   `S1003`, `S1004` and `S1005` for the profit tax return and the financial statements. When `D406`
   is requested, the script also installs `DUKIntegrator_AnLunaUI.jar`, the period-aware validator
   used for the SAF-T file (see :doc:`saft_d406`). Run the script again when ANAF publishes new
   versions of the validators.
#. **Choose a token.** The service **refuses to start without a token** (`DUK_TOKEN`), which Odoo
   sends as a bearer token. Use a long random secret. The `--insecure` option starts the service
   without a token and is only meant for private test machines.
#. **Start the service.** For example, with Docker:

   .. code-block:: console

      $ docker build -t eyssen/duk-service .
      $ docker run -d --name duk -p 127.0.0.1:8080:8080 -e DUK_TOKEN=<secret> \
            -v /srv/duk:/opt/duk:ro eyssen/duk-service

   Or directly on the server: `DUK_HOME=/srv/duk DUK_PORT=8080 DUK_TOKEN=<secret> python3
   duk_service.py`. By default, the service listens on `127.0.0.1` only.
#. **Check it.** `curl http://localhost:8080/health` answers `{"status": "ok"}`, and `curl -H
   "Authorization: Bearer <secret>" http://localhost:8080/info` lists the installed validators.

.. important::
   Do not expose the service on the Internet. Publish the port on a private interface or a private
   network that only the Odoo server can reach, and keep the token secret.

The service is configured with environment variables:

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Variable
     - Default
     - Meaning
   * - `DUK_HOME`
     - `/opt/duk`
     - Folder with `DUKIntegrator.jar`, `lib/` and `config/`.
   * - `DUK_TOKEN`
     - none
     - Bearer token, mandatory unless the service is started with `--insecure`.
   * - `DUK_BIND`, `DUK_PORT`
     - `127.0.0.1`, `8080`
     - Address and port of the service (`0.0.0.0` inside the Docker image).
   * - `DUK_TIMEOUT`
     - `120`
     - Seconds allowed for one validation. Raise it for large SAF-T files.
   * - `DUK_MAX_CONCURRENT`
     - `2`
     - Number of validations that run at the same time. A request that waits more than
       `DUK_QUEUE_TIMEOUT` seconds (60 by default) gets an HTTP 503 answer.
   * - `DUK_MAX_BYTES`
     - 400 MB
     - Maximum size of the XML file.
   * - `DUK_JAVA`, `DUK_JAVA_OPTS`
     - `java`
     - Java executable and extra options, for example `-Xmx4g` for large SAF-T files.

Connect Odoo to the service
---------------------------

Go to :menuselection:`Accounting --> Configuration --> Settings`, section :guilabel:`Romanian ANAF
Declarations`, setting :guilabel:`DUKIntegrator Validation`, and fill in:

- :guilabel:`DUK Validator Service URL`: the base URL of the service, for example
  `http://duk:8080`. Leave it empty to skip the ANAF validation.
- :guilabel:`DUK Validator Service Token`: the `DUK_TOKEN` of the service. Only administrators see
  this field.
- :guilabel:`Request DUK PDF`: tick it to receive the official PDF.

Instead of configuring each company, the service can be set once for the database with the system
parameters `l10n_ro_declaration.duk_service_url` and `l10n_ro_declaration.duk_service_token`
(:ref:`developer mode <developer-mode>`, :menuselection:`Settings --> Technical --> Parameters -->
System Parameters`). A company that has its own URL uses its own token; the token of the system
parameter is only sent to the URL of the system parameter, never to a URL typed on a company. The
parameters `l10n_ro_declaration.duk_service_timeout` (seconds, 120 by default) and
`l10n_ro_declaration.duk_raw_threshold` (bytes, 20 MB by default; larger files are streamed to the
service) can also be set.

.. _localizations/romania/declarations/filing:

Filing with ANAF
================

Odoo prepares and checks the declarations, but it **does not send them to ANAF**: there is no
connection to the ANAF filing services in the declaration modules. After the validation:

#. Click :guilabel:`Export XML` and, if it was requested, open the :guilabel:`DUK PDF` in the
   :guilabel:`Validation` tab.
#. File the declaration with ANAF yourself, for example through the *SPV* (*Spațiul Privat Virtual*,
   the private virtual space of the taxpayer on the ANAF portal), with the file that the portal
   requires for the form.
#. Back in Odoo, click :guilabel:`Mark as Submitted`. Optionally, enter the :guilabel:`Submission
   Date` and the :guilabel:`Registration Number` (*număr de înregistrare*) that ANAF gave to the
   declaration. These two fields are informative: Odoo does not check them.

.. note::
   The :doc:`e-Factura <e_factura>` integration, which sends invoices to the SPV, is a separate
   feature and does not file the declarations.

.. seealso::
   - :doc:`d300`
   - :doc:`d390`
   - :doc:`d394`
   - :doc:`saft_d406`
   - :doc:`d101`
   - :doc:`financial_statements`

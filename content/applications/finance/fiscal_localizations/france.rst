======
France
======

.. _localizations/france/configuration/modules:

Modules
=======

The following modules related to the French localization are available:

.. list-table::
    :header-rows: 1

    * - Name
      - Technical name
      - Description
    * - :guilabel:`France - Accounting`
      - `l10n_fr_account`
      - French :ref:`fiscal localization package <fiscal_localizations/packages>` that applies only
        to companies based in mainland France and doesn't include DOM-TOMs.
    * - :guilabel:`France - Factur-X integration with Chorus Pro`
      - `l10n_fr_facturx_chorus_pro`
      - Adds fields needed for :ref:`submitting invoices to Chorus Pro
        <localizations/france/e-invoicing>`.
    * - :guilabel:`France - E-Invoicing (Approved Platform)`
      - `l10n_fr_pdp`
      - Support for the mandatory French electronic invoicing reform: sends and receives
        invoices through an approved platform (*Plateforme de Dématérialisation Partenaire*)
        and the e-reporting flows. Installed automatically with the French package.
    * - :guilabel:`France - VAT Anti-Fraud Certification for Point of Sale (CGI 286 I-3 bis)`
      - `l10n_fr_pos_cert`
      - :ref:`Point of Sale VAT anti-fraud certification
        <localizations/france/vat-anti-fraud-certification>`

.. note::
   The localization's core modules are installed automatically with the localization. The rest can
   be manually :doc:`installed </applications/general/apps_modules>`.

   The French VAT report export (EDI to the DGFiP), the French payroll, the FEC import, the
   *liasse fiscale* (Teledec) synchronization and the French versions of the financial reports
   (*Bilan comptable (FR)*, *Compte de résultats (FR)*, *Rapport de taxes (FR)*) are **not**
   available in this edition; the generic :doc:`financial reports <../accounting/reporting>` and
   the :doc:`tax report <../accounting/reporting/dynamic_reports>` (with the French CA3 grids)
   can be used instead.

.. _localizations/france/loc-overview:

Localization overview
=====================

The French localization package ensures compliance with French fiscal and accounting regulations. It
includes tools for managing taxes, fiscal positions, reporting, and a predefined chart of accounts
tailored to France’s standards.

The French localization package provides the following key features to ensure compliance with local
fiscal and accounting regulations:

- :doc:`../accounting/get_started/chart_of_accounts`: a predefined structure tailored to French
  accounting standards
- :doc:`../accounting/taxes/fiscal_positions`: automated tax adjustments based on customer or
  supplier registration status
- :doc:`Taxes <../accounting/taxes>`: pre-configured tax rates, including standard VAT,
  zero-rated, and exempt options, mapped to the grids of the CA3 VAT return
- :doc:`Reporting <../accounting/reporting>`

.. _localizations/france/accounting:

Accounting
==========

.. _localizations/france/e-invoicing:

E-Invoicing
-----------

The `Chorus Pro <https://portail.chorus-pro.gouv.fr/aife_csm>`_ portal, managed by the AIFE (Agence
pour l'Informatique financière de l'État), is the official platform for submitting electronic
invoices to French public entities. It allows businesses to send and manage invoices, track their
processing status, and access payment updates. Since January 2020, electronic invoicing has been
mandatory for all business-to-government (B2G) transactions in France. Odoo supports integration
with Chorus Pro to submit invoices generated in Odoo.

.. _localizations/france/e-invoicing-configuration:

Configuration
~~~~~~~~~~~~~

To send invoices to Chorus Pro, the following configuration is required:

#. :doc:`Install </applications/general/apps_modules>` the :guilabel:`France - Factur-X integration
   with Chorus Pro` (`l10n_fr_facturx_chorus_pro`) module.
#. :ref:`Register <accounting/e-invoicing/peppol-registration>` with Peppol, as invoices are sent
   from Odoo to Chorus Pro via the :ref:`Peppol <accounting/e-invoicing/peppol>` network.
#. If you don’t already have a Chorus Pro account, go to the `Chorus Pro
   <https://portail.chorus-pro.gouv.fr/aife_csm>`_ page, click :guilabel:`Créer un compte`, and
   create one.
#. :ref:`Configure the relevant customers' contact form
   <localizations/france/e-invoicing-contacts>`.

.. seealso::
   `Chorus Pro documentation <https://portail.chorus-pro.gouv.fr/aife_documentation>`_

.. _localizations/france/e-invoicing-contacts:

Customers
*********

To submit invoices to Chorus Pro, configure the relevant customers' contact form as follows:

#. Ensure the :guilabel:`Country` field is completed, then select :guilabel:`VAT` as the
   :guilabel:`Identification Number` and enter the corresponding number.
#. In the :guilabel:`Sales & Purchase` tab, ensure the :guilabel:`SIRET` field is completed.
#. In the :guilabel:`Accounting` tab, fill in the following fields in the :guilabel:`Customer
   Invoices` section:

   - :guilabel:`eInvoice format`: Select :guilabel:`BIS Billing 3.0`.
   - Make sure :guilabel:`France SIRET` is selected in the next field, then type `11000201100044`,
     the reference used by Chorus Pro.

.. _localizations/france/e-invoicing-invoices:

Sending invoices to Chorus Pro
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To send invoices to Chorus Pro, follow these steps:

#. Go to :menuselection:`Accounting --> Customers --> Invoices` and open or create the invoice.
#. Make sure the following fields are filled in the :guilabel:`Other Info` tab:

   - :guilabel:`Buyer Reference`: :guilabel:`Service Exécutant` in Chorus Pro
   - :guilabel:`Contract Reference`: :guilabel:`Numéro de Marché` in Chorus Pro
   - :guilabel:`Purchase Order Reference`: :guilabel:`Engagement Juridique` in Chorus Pro

#. Confirm the invoice.
#. Click :guilabel:`Send` and, in the :guilabel:`Print & Send` window, enable :guilabel:`By Peppol`.
#. Click :guilabel:`Send`.

Once the invoice is sent, the Peppol status of the invoice is updated to :guilabel:`Done`.

.. seealso::
   :ref:`Peppol <accounting/e-invoicing/peppol>`

.. _localizations/france/pdp:

Approved platform (PDP) e-invoicing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The *France - E-Invoicing (Approved Platform)* (`l10n_fr_pdp`) module implements the French
electronic invoicing reform: B2B invoices are exchanged through an approved platform (*Plateforme
de Dématérialisation Partenaire*, PDP) and the sales data is e-reported to the tax administration.
The connection is configured in :menuselection:`Accounting --> Configuration --> Settings -->
French Electronic Invoicing`:

- Click :guilabel:`Activate Electronic Invoicing` to register the company (identified by its
  SIREN/SIRET) on the platform, with the :guilabel:`Primary contact email` and the
  :guilabel:`Incoming Invoices Journal` in which received vendor bills are created. The block then
  shows the registration state; :guilabel:`Disconnect` cancels the registration.
- :guilabel:`E-Reporting Periodicity`: the VAT regime of the company (monthly or quarterly *régime
  réel normal*, monthly *régime simplifié*, bimonthly *franchise*), which determines how often the
  e-reporting flows (*flux 10*) are generated.

Once active, customer invoices are sent from the :guilabel:`Send & Print` window like Peppol
invoices, incoming invoices are fetched automatically, and the generated e-reporting flows can be
followed under :menuselection:`Accounting --> Reporting --> France --> E-Reporting` (list of *Flows 10* with
their period, status and transmission type).

.. note::
   The platform connection is provided by an access-point service operated by Odoo S.A.; the
   registration requires the company's SIRET, a public URL for the database and two-factor
   authentication for the users.

.. screenshot:: finance-fl-france-pdp-settings
   :menu: Accounting ‣ Configuration ‣ Settings ‣ French Electronic Invoicing
   :shows: The "French Electronic Invoicing" settings block of a French company after activation: the SIRET identification with the "active" state, "Primary contact email", "Incoming Invoices Journal", "E-Reporting Periodicity" and the "Disconnect" button.
   :highlight: The "Activate Electronic Invoicing" / state line.
   :data: Demo company "YourCompany FR" registered in test mode.
   :module: l10n_fr_pdp
   :notes: English UI, light theme, 1440px width; use a test registration.

.. _localizations/france/fec:

FEC - Fichier des Écritures Comptables
--------------------------------------

An FEC :dfn:`Fichier des Écritures Comptables` audit file contains all the accounting data and
entries recorded in all the accounting journals for a financial year. The entries in the file must
be arranged in chronological order. Since January 2014, every French company is required to produce
and transmit this file upon request by the tax authorities for audit purposes.

.. note::
   The :guilabel:`FEC File Generation` wizard (`l10n_fr.fec.export.wizard`) is part of the
   :guilabel:`France - Accounting` module, but the menu that opens it is **not** available in this
   edition. Ask your system administrator to open the wizard (a window action on that model can be
   created from :menuselection:`Settings --> Technical --> Actions --> Window Actions` in
   developer mode), or export the journal items from the :doc:`general ledger
   <../accounting/reporting/dynamic_reports>` instead.

.. _localizations/france/fec-export:

FEC Export
~~~~~~~~~~

In the :guilabel:`FEC File Generation` window, fill in the following fields:

- :guilabel:`Start Date`
- :guilabel:`End Date`
- :guilabel:`Export Type`: :guilabel:`Official FEC report (posted entries only)` or
  :guilabel:`Non-official FEC report (posted and unposted entries)` (for testing).
- :guilabel:`Exclude lines at 0`: Enable this option if needed.
- :guilabel:`Excluded Journals`: Select the journal(s) to exclude.

Then, click :guilabel:`Generate`.

.. seealso::
   - `Official Technical Specification (fr)
     <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000027804775>`_
   - `Test-Compta-Demat (Official FEC Testing tool)
     <https://github.com/DGFiP/Test-Compta-Demat>`_

.. _localizations/france/pos:

Point of sale
=============

.. _localizations/france/vat-anti-fraud-certification:

VAT anti-fraud certification
----------------------------

Since January 2018, new anti-fraud legislation has been in effect in France and its overseas
territories (DOM-TOM). This legislation establishes specific requirements for the integrity,
security, storage, and archiving of sales data. Odoo complies with these legal requirements by
providing a dedicated module.

Anti-fraud cash register software, such as Odoo (CGI art. 286, I. 3° bis), is required for companies
taxable in France or DOM-TOM, where some customers are private individuals (B2C). This rule applies
to all company sizes, but auto-entrepreneurs exempt from VAT are unaffected.

.. seealso::
   - `Frequently Asked Questions
     <https://www.economie.gouv.fr/files/files/directions_services/dgfip/controle_fiscal/actualites_reponses/logiciels_de_caisse.pdf>`_
   - `Official Statement
     <http://bofip.impots.gouv.fr/bofip/10691-PGP.html?identifiant=BOI-TVA-DECLA-30-10-30-20160803>`_
   - `Item 88 of Finance Law 2016
     <https://www.legifrance.gouv.fr/affichTexteArticle.do?idArticle=JORFARTI000031732968&categorieLien=id&cidTexte=JORFTEXT000031732865>`_

.. _localizations/france/pos-odoo-certification:

Certification
~~~~~~~~~~~~~

The tax administration requires all companies to provide a certificate of conformity confirming that
their software complies with anti-fraud legislation. In case of non-compliance, a €7,500 fine may be
imposed.

.. note::
   The certificate of conformity is a document issued by the software vendor for the certified
   software version. Ask your support provider which certificate applies to your installation.

To activate the anti-fraud features, follow these steps:

#. :doc:`Install </applications/general/apps_modules>` the :guilabel:`France - VAT Anti-Fraud
   Certification for Point of Sale (CGI 286 I-3 bis)` (`l10n_fr_pos_cert`) module.
#. Set the :guilabel:`Country` field on the :doc:`company record </applications/general/companies>`
   to encrypt entries for the inalterability check.

.. _localizations/france/pos-anti-fraud-features:

Anti-fraud features
~~~~~~~~~~~~~~~~~~~

The anti-fraud module introduces the following features:

- :ref:`Inalterability <localizations/france/pos-inalterability>`
- :ref:`Security <localizations/france/pos-security>`
- :ref:`Storage <localizations/france/pos-storage>`

.. _localizations/france/pos-inalterability:

Inalterability
**************

All methods to cancel or modify key data in POS orders, invoices, and journal entries are
deactivated for companies located in France or any DOM-TOM.

.. note::
   In a multi-company environment, only the documents of such companies are impacted.

.. _localizations/france/pos-security:

Security
********

To ensure inalterability, every order or journal entry is encrypted upon validation. This number
(or hash) is calculated from the document's key data and the hash of the precedent documents. The
module introduces an interface to test the data's inalterability. The test will fail if any
information is modified on a document after its validation. The algorithm recomputes all the hashes
and compares them against the initial ones. In case of failure, the system points out the first
corrupted document recorded in the system.

Only users with :doc:`administrator </applications/general/users/access_rights>` access rights can
initiate the inalterability check:

- For POS orders, go to :menuselection:`Point of Sale --> Reporting --> POS Inalterability Check`;
- For journal entries, run the :guilabel:`Data Inalterability Check` server action as described in
  :doc:`../accounting/reporting/data_inalterability`.

.. _localizations/france/pos-storage:

Storage
*******

The system also processes automatic sales closings daily, monthly, and annually. Such closings
compute the sales total for the period and the cumulative grand totals from the very first sales
entry recorded in the system.

To access closings, either go to :menuselection:`Point of Sales --> Reporting --> Sales Closings` or
:menuselection:`Invoicing/Accounting --> Reporting --> Sales Closings`.

.. note::
   - Closings compute the totals for journal entries of sales journals (Journal Type = Sales).
   - For multi-companies environments, such closings are performed by company.
   - POS orders are posted as journal entries at the closing of the POS session. Closing a POS
     session can be done anytime. To prompt users to do it daily, the module prevents them from
     resuming a session that was opened more than 24 hours ago. Such a session must be closed before
     selling again.
   - A period’s total is computed from all the journal entries posted after the previous closing of
     the same type, regardless of their posting date. Recording a new sales transaction for a
     period already closed will be counted in the very next closing.

.. tip::
   For test & audit purposes, closings can be manually generated in :ref:`developer mode
   <developer-mode>`. To do so, go to :menuselection:`Settings --> Technical --> Scheduled Actions`.
   In the scheduled actions list view, open the desired :guilabel:`Sale Closing` action and click
   :guilabel:`Run manually`.

.. _localizations/france/pos-responsibilities:

Responsibilities
~~~~~~~~~~~~~~~~

Uninstalling this module will reset the security hashes. This means the system will no longer
guarantee the integrity of the past data.

Users are responsible for their Odoo system and must operate it carefully. Modifying source code
responsible for ensuring data integrity is not allowed.

Odoo is not responsible for any issues with this module's functionality if caused by uncertified
third-party applications.

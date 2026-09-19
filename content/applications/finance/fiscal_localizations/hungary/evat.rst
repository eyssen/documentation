===================================
VAT return with NAV eÁFA (eVAT M2M)
===================================

The :guilabel:`Hungary - eVAT (eÁFA M2M) VAT Return` (`l10n_hu_evat`) module files the Hungarian VAT
return through the *eÁFA* machine-to-machine interface of NAV instead of an ÁNYK form. Odoo builds
the VAT **analytics** of the period from the posted journal entries (one line per source document,
classified with the *standard tax codes* of NAV), validates them with the rules and the XML schema
published by NAV, uploads them in the background, follows the processing at NAV, and finally an
approver submits the legally binding return. Self-revisions and corrections of submitted returns are
supported.

.. note::
   - The module requires `eyssen_l10n_hu` and uses the technical user of the :doc:`NAV Online Számla
     reporting <nav_online_invoice>`.
   - Returns can only be generated for companies whose currency is HUF.
   - The module is independent of the :doc:`ÁNYK form packages <vat_return>`; use one of the two
     methods for a given period. The domestic recapitulative M sheets and the EC recapitulative
     statement (`A60`) are not part of this module: the partner-level data travel in the analytics
     lines, and the recapitulative statement is prepared with the ÁNYK form package.

Configuration
=============

Access rights
-------------

Two access rights are available in the :guilabel:`Hungarian eVAT` category of the user form:

- :guilabel:`eVAT User`: create, generate, validate and upload returns, reopen aborted returns, and
  fetch the NAV documents;
- :guilabel:`eVAT Approve`: everything above, plus delete draft returns and **submit** the return to
  NAV. The administrator receives this right at installation.

The configuration menus require the :guilabel:`Administrator` accounting access right.

Settings
--------

Go to :menuselection:`Accounting --> Configuration --> Settings`, section :guilabel:`Hungarian eVAT`:

- :guilabel:`eVAT M2M Enabled`: enables the interface for the company;
- :guilabel:`eVAT Software ID`: the 18-character identifier (digits and capital letters) of the
  software, pre-filled;
- :guilabel:`NAV Mode`: displays the :guilabel:`Test`/:guilabel:`Production` mode selected in the
  :ref:`NAV Data Reporting settings <localizations/hungary/nav-settings>`; the matching user name,
  password and signing key of those settings are used;
- :guilabel:`eVAT VPID`: the 12-digit customs identifier, needed only if a tax account transfer line
  credits a customs-related tax type.

.. screenshot:: finance-fl-hungary-evat-settings
   :menu: Accounting ‣ Configuration ‣ Settings
   :shows: Settings page scrolled to the "Hungarian eVAT" section with "eVAT M2M Enabled" ticked, the software ID, the read-only NAV mode and the empty VPID field, and the sentence about the NAV technical user below.
   :highlight: The "eVAT M2M Declaration" setting block (red frame).
   :data: Demo company "YourCompany HU"; NAV mode "Test".
   :module: l10n_hu_evat
   :notes: English UI, light theme, 1440px width, crop to the section.

Standard tax codes
------------------

Every analytics line carries a NAV *standard tax code*, which describes the type of the transaction
and its VAT rate.

- :menuselection:`Accounting --> eVAT --> Configuration --> Standard Tax Codes` contains the
  catalogue published by NAV. :guilabel:`Sync from NAV` downloads new codes and closes expired ones.
- On each tax, set the default code in the :guilabel:`eVAT` tab, field :guilabel:`eVAT Standard Tax
  Code`.
- :menuselection:`Accounting --> eVAT --> Configuration --> Mapping Rules` handles the exceptions.
  A rule has :guilabel:`Conditions` (:guilabel:`Taxes`, :guilabel:`Move Types`, :guilabel:`Partner
  Status`, :guilabel:`Fiscal Positions`, :guilabel:`Product Categories`, :guilabel:`Products`) and a
  :guilabel:`Result`: the :guilabel:`eVAT Standard Tax Code` and the :guilabel:`Taxpoint Strategy`
  (:guilabel:`Default`, :guilabel:`Delivery date`, :guilabel:`Accounting date` or :guilabel:`Period
  end`). The first matching rule wins; if no rule matches, the default code of the tax is used.

A document whose tax has neither a rule nor a default code is skipped and reported on the
:guilabel:`Validation` tab of the return (code `GEN0001`).

Other tables
------------

- :guilabel:`MNB Base Rates`: the central bank base rate series used to compute the self-revision
  surcharge. The historical rates are preloaded; **add a new row whenever the base rate changes**.
- :guilabel:`VTSZ Tariff Mapping`: maps the VTSZ prefixes of domestic reverse-charge goods
  (agricultural products, steel, gas) to the product category and unit of measure required on
  sheets `07` and `08`.

.. _localizations/hungary/evat-return:

Prepare and file a return
=========================

Go to :menuselection:`Accounting --> eVAT --> Declarations` and click :guilabel:`New`. Set the
:guilabel:`Period Start`, the :guilabel:`Period End` and the :guilabel:`Frequency`
(:guilabel:`Monthly`, :guilabel:`Quarterly` or :guilabel:`Annual`), then follow the steps below. The
status bar shows the main steps: :guilabel:`Draft`, :guilabel:`Generated`, :guilabel:`Finished` and
:guilabel:`Submitted`.

#. Click :guilabel:`Generate`. The analytics lines are built from the posted entries of the period
   (taxes due on payment are included by payment date), the summary is computed, the local
   validation runs and the reverse-charge sheets `07`/`08` are filled in. :guilabel:`Reset to Draft`
   discards the generated data.
#. Review the tabs:

   - :guilabel:`Lines`: the analytics lines with their source document, taxpoint date and partner;
   - :guilabel:`Summary`: payable, deductible, reclaimed and transferable tax in thousand HUF.
     Tick :guilabel:`Lapsed Residual Tax` if the amount carried forward from the previous period can
     no longer be used;
   - :guilabel:`Statements`: the :guilabel:`Return Decision` (:guilabel:`No return`, :guilabel:`Full
     return` or :guilabel:`Tax account transfer`), the :guilabel:`Refund Entitlement Code` and the
     procedure indicators of the return. Click :guilabel:`Compute Summary` after changing them;
   - :guilabel:`Transfer (170)`: the transfer request lines, if the return decision is a tax account
     transfer;
   - :guilabel:`Reverse charge (07/08)`: the domestic reverse-charge sheets, which can be
     regenerated with :guilabel:`Regenerate 07/08 Sheets`;
   - :guilabel:`Validation`: the messages of the local check (:guilabel:`Critical`,
     :guilabel:`Error`, :guilabel:`Warning`, :guilabel:`Info`). Correct the source documents or the
     tax code mapping, and click :guilabel:`Generate` again after a :guilabel:`Reset to Draft`.
     :guilabel:`Validate` reruns the check at any time.

#. Optionally, click :guilabel:`Export XML` to download the analytics file
   (`EVAT_<start>_<end>_v<version>.xml`) for review.
#. Click :guilabel:`Upload to NAV`. The return must be free of local validation errors. The status
   changes to :guilabel:`Uploading`, and a background job uploads the data about a minute later.
   If the upload fails, the return goes back to :guilabel:`Generated` and the reason is shown in the
   :guilabel:`Error Note` of the :guilabel:`NAV` tab.
#. NAV processes the upload. A scheduled action checks the status every five minutes
   (:guilabel:`Received` → :guilabel:`Processing` → :guilabel:`BEVFELD Check` →
   :guilabel:`Finished`); :guilabel:`Check Status Now` checks it on demand. The messages of NAV are
   added to the :guilabel:`Validation` tab. If NAV rejects the data, the status becomes
   :guilabel:`Aborted`: click :guilabel:`Reopen`, correct the problem and upload again.
#. When the status is :guilabel:`Finished`, every user with the :guilabel:`eVAT Approve` right
   receives a to-do activity *Submit eVAT declaration to NAV*. The :guilabel:`Submission Deadline`
   on the :guilabel:`NAV` tab shows until when the processed data is kept by NAV (30 days); after
   that the upload must be repeated.
#. An approver clicks :guilabel:`Submit to NAV`. The dialog lists the high-priority warnings of NAV,
   which must be acknowledged with :guilabel:`I acknowledge the warnings above`, and reminds that
   *submitting is the legally binding filing of the VAT return with NAV* and cannot be undone. After
   the confirmation the status is :guilabel:`Submitted` and the return document received from NAV
   is attached.

.. screenshot:: finance-fl-hungary-evat-declaration
   :menu: Accounting ‣ eVAT ‣ Declarations ‣ (declaration)
   :shows: eVAT declaration "eVAT 2026-08 v1" in status "Generated" with the buttons "Reset to Draft", "Compute Summary", "Validate", "Export XML", "Upload to NAV", the header fields (period, frequency, declaration method, version) and the "Lines" tab with a few analytics lines and their "NAV Match" badges.
   :highlight: The "Upload to NAV" button and the status bar (red frames).
   :data: Demo company "YourCompany HU", monthly period 2026-08-01 – 2026-08-31, ~10 lines.
   :module: l10n_hu_evat
   :notes: English UI, light theme, 1440px width, crop to the form sheet.

.. tip::
   - The taxpoint date of a document is its fulfillment date, unless a mapping rule sets another
     strategy. It can be overridden on the :guilabel:`eVAT` tab of the invoice (:guilabel:`eVAT
     Taxpoint Date`). The same tab lists the returns that contain the invoice, and
     :guilabel:`Query NAV Tax Codes` shows the codes NAV suggests for a posted invoice (for
     information only).
   - Vendor bills are identified by their :guilabel:`Bill Reference`; bills without a reference are
     skipped with a validation message.

Reconcile with the NAV data
---------------------------

On the :guilabel:`NAV Documents` tab, click :guilabel:`Fetch NAV Documents` to download the invoice
data, cash register summaries and customs declarations that NAV holds for the period. The
:guilabel:`Reconciliation Summary` and the :guilabel:`NAV Match` badge of the lines show which
documents are :guilabel:`Matched` and which are :guilabel:`Missing in Odoo`, for example vendor bills
that were not recorded yet.

Self-revision and correction
============================

On a :guilabel:`Submitted` return, click :guilabel:`Self-check` (*önellenőrzés*) or
:guilabel:`Correction` to create the next version for the same period, then generate, upload and
submit it like a base return. The :guilabel:`Changes` tab compares it with the original return
(summary differences and added, removed and changed lines).

For a self-revision, the :guilabel:`Self-check (04)` tab contains the self-revision surcharge
(*önellenőrzési pótlék*). Select the :guilabel:`Non-standard Calculation Reason` if one applies, and
click :guilabel:`Compute Allowance`: the surcharge is computed from the MNB base rate, from the day
after the original deadline, with a 50% increase for a repeated self-revision. If the surcharge was
computed on an earlier day than the submission, the submit dialog asks to acknowledge it.

Scheduled actions and limitations
=================================

Two scheduled actions are created: *eVAT: poll NAV processing status* (every 5 minutes) and *eVAT:
remove finished one-shot upload jobs* (hourly).

The following are not supported in the current module version: the sheets for animal disease
deferment, bad debt, chassis numbers and new means of transport; attachments to the return; and the
automatic handling of lapsed residual tax. There is no PDF print of the return.

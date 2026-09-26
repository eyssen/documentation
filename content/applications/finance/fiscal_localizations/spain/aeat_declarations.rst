=====================
AEAT tax declarations
=====================

With the :ref:`Spain - Base Layer <localizations/spain/base-layer>`, the Spanish tax declarations
(*modelos*) of the AEAT are prepared in the Accounting app: the declaration computes its boxes from
the posted journal items of the period, creates the regularization entry, and exports the file
(*fichero BOE*) that is uploaded to the AEAT electronic office.

:ref:`Install <general/install>` the *Spain - AEAT Declarations Integration* module. It installs
the declarations below and fits them into the Accounting app:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Declaration
     - Content
   * - Modelo 303
     - VAT self-assessment, monthly or quarterly.
   * - Modelo 390
     - Annual VAT summary.
   * - Modelo 111
     - Withholdings on work income and professional activities.
   * - Modelo 115
     - Withholdings on the rent of urban property.
   * - Modelo 130
     - Instalment payment of the personal income tax (IRPF) of self-employed persons in direct
       estimation.
   * - Modelo 347
     - Annual declaration of operations with third parties above 3,005.06 €.
   * - Modelo 349
     - Recapitulative statement of intra-community operations.
   * - Modelo 369
     - VAT One-Stop-Shop (OSS) return for distance sales within the EU.
   * - VAT and IRPF books
     - *Libros registro* of issued and received invoices, exported to XLSX.

It also adds the official annual accounts (PGC balance sheet and profit and loss), see
:ref:`localizations/spain/aeat/annual-accounts`.

.. note::
   Other declarations (for example modelos 123, 190, 216 and 296) are separate modules. Once
   installed, they appear in the same menu and work the same way.

Users with the *Accountant* role (and advisers) can create and file the declarations.

.. _localizations/spain/aeat/configuration:

Configuration
=============

Default values of the declarations
----------------------------------

Go to :menuselection:`Accounting --> Configuration --> Settings`, and scroll to the
:guilabel:`AEAT Declarations` section. The values set here are proposed on every new declaration of
the company:

- :guilabel:`Regularization entries`: the :guilabel:`AEAT Journal` in which the regularization
  entries are posted, the :guilabel:`VAT Counterpart Account` (by default 4750) for the VAT
  declarations whose counterpart is not computed by the declaration itself, such as the modelo 369,
  and the :guilabel:`Withholding Counterpart Account` (by default 4751) for the withholding
  declarations. The modelo 303 chooses 4750 or 4700 from its result by itself.
- :guilabel:`Submitter and frequency`: the :guilabel:`AEAT Contact Name`, :guilabel:`AEAT Contact
  Phone` and :guilabel:`AEAT Contact Email` printed in the declarations (if empty, the data of the
  current user is used), and the :guilabel:`Filing Frequency` (:guilabel:`Quarterly` or
  :guilabel:`Monthly`). Monthly filing applies to large companies and to taxpayers registered in the
  REDEME or in the SII. A new declaration proposes the last closed period of this frequency; annual
  declarations propose the previous year.

.. screenshot:: finance-fl-spain-aeat-settings
   :menu: Accounting ‣ Configuration ‣ Settings ‣ AEAT Declarations
   :shows: The "AEAT Declarations" settings section with the "Regularization entries" block (AEAT Journal, VAT Counterpart Account 4750, Withholding Counterpart Account 4751), the "Submitter and frequency" block (contact name, phone, email, Filing Frequency "Quarterly") and the "Tax map check" link.
   :highlight: The "Filing Frequency" field.
   :data: Spanish demo company with the PGC chart of accounts.
   :module: l10n_es_aeat_integration
   :notes: English UI, light theme, 1440px width.

.. _localizations/spain/aeat/tax-map:

Tax map check
-------------

Each declaration adds up the amounts of the taxes listed in its *tax map*: a tax that is in no map
line of an installed declaration is silently left out of the declarations. The :guilabel:`Tax map
check` setting shows how many taxes of the company are in this situation. Click the link to open the
list of these taxes, or go to :menuselection:`Accounting --> Configuration --> AEAT --> Taxes
missing from the AEAT declarations`. In the tax list, the :guilabel:`Missing from AEAT declarations`
filter gives the same result.

Review the listed taxes: either the tax is not used, or it must be replaced by one of the default
Spanish taxes. The withholding taxes of declarations that are not installed (123, 216, 296) also
appear in the list.

.. tip::
   The tax maps themselves can be consulted under :menuselection:`Accounting --> Configuration -->
   AEAT --> Tax mapping`. Do not modify them unless your tax adviser asks for it.

.. _localizations/spain/aeat/file:

File a declaration
==================

The declarations are under :menuselection:`Accounting --> Reporting --> AEAT`, one menu per
declaration, for example :menuselection:`Accounting --> Reporting --> AEAT --> AEAT 303 model`.

#. Click :guilabel:`New`. The :guilabel:`Year` and the :guilabel:`Period Type` of the last closed
   period, the journal, the counterpart account, and the contact data are proposed from the
   :ref:`settings <localizations/spain/aeat/configuration>`. Change them if needed.
#. Select the :guilabel:`Statement Type`: :guilabel:`Normal`, or :guilabel:`Complementary` or
   :guilabel:`Substitutive` to correct a declaration already filed. For the last two, enter the
   :guilabel:`Previous declaration number`.
#. Click :guilabel:`Calculate`. The boxes of the declaration are computed from the posted journal
   items of the period. Open the :guilabel:`Tax lines` tab, and use the button at the end of a line
   to see the journal items that make up the amount of a box.
#. Fill in the boxes that are not computed automatically, if any, then click
   :guilabel:`Recalculate` if you changed accounting data in the meantime.
#. Click :guilabel:`Confirm` when the amounts are correct.
#. Click :guilabel:`Create move` to post the regularization entry, which moves the balances of the
   tax accounts to the counterpart account. Use :guilabel:`Show move` to open it.
#. Click :guilabel:`Export to BOE` to download the file, and upload it in the AEAT electronic
   office.

.. screenshot:: finance-fl-spain-aeat-303
   :menu: Accounting ‣ Reporting ‣ AEAT ‣ AEAT 303 model ‣ (a calculated declaration)
   :shows: A calculated modelo 303 of the third quarter: header with Year, Period Type "3T", Statement Type "Normal", the journal and counterpart account, the result section with the result type, and the "Tax lines" tab listing the boxes and their amounts; buttons Recalculate, Confirm and Cancel in the header.
   :highlight: The "Calculate"/"Confirm" buttons and the "Tax lines" tab.
   :data: Spanish demo company with sales and purchases in the quarter.
   :module: l10n_es_aeat_mod303, l10n_es_aeat_integration
   :notes: English UI, light theme, 1440px width.

.. important::
   The regularization entry is dated on the last day of the period. If this date is in a locked
   period, a warning banner is shown on the declaration as soon as it is opened, and the entry
   cannot be posted. Create the declaration entry before locking the period, or ask an adviser to
   move the lock date.

.. note::
   A banner also warns when taxes used in the period are not in any AEAT tax map, as they are left
   out of the declaration. Click :guilabel:`Show taxes` to list them, and see
   :ref:`localizations/spain/aeat/tax-map`.

Specific declarations
---------------------

Modelo 303
   The :guilabel:`Result Type` shows whether the result is to be paid, returned, or compensated in
   later periods. The amount to compensate from previous periods is proposed from the previous
   declarations. In the last period of the year (4T or month 12), indicate whether the company is
   exempt from the modelo 390, and if so, fill in the additional data of the activities.

Modelo 390
   The annual summary is computed for the whole year. Fill in the fields that are not computed
   automatically before confirming it.

Modelos 111 and 115
   The withholdings are computed from the withholding taxes of the vendor bills. In the modelo 111,
   fill in the boxes that Odoo cannot compute, such as the work income paid outside Odoo.

Modelo 347
   After :guilabel:`Calculate`, the :guilabel:`Partner records` tab lists the partners whose
   operations exceed the threshold; a record shown in red misses data needed for the declaration.
   Click :guilabel:`Send emails` to send each partner its record for verification, and use
   :guilabel:`Confirm as valid` when a partner agrees. Real estate rentals not declared in the
   modelo 115 can be added in the :guilabel:`Real estate records` tab. To exclude a contact from
   the declaration regardless of its amounts, tick :guilabel:`Not included in 347 report` on the
   contact form.

Modelo 349
   The :guilabel:`Partner records` and :guilabel:`Partners refunds` tabs list the intra-community
   operations of the period. Delete the operations that must not be declared from these tabs before
   confirming.

Modelo 369
   The OSS return is computed from the OSS taxes of the distance sales to consumers of other EU
   countries.

.. _localizations/spain/aeat/vat-book:

VAT and IRPF books
==================

Go to :menuselection:`Accounting --> Reporting --> AEAT --> Libros del IVA y del IRPF` and create a
book for the period, then click :guilabel:`Calculate`. The :guilabel:`Issued Invoices` and
:guilabel:`Received Invoices` tabs list the invoices with their taxes; the :guilabel:`Summary` tab
totals them per tax. Click :guilabel:`View Issued Invoices` or :guilabel:`View Received Invoices` to
display the books. Click :guilabel:`Export draft` to download them as an XLSX file; after
:guilabel:`Confirm`, the final file is downloaded with :guilabel:`Export BOE`.

.. _localizations/spain/aeat/annual-accounts:

Official annual accounts (PGC)
==============================

The official Spanish balance sheet and profit and loss, in the format of the annual accounts filed
with the Mercantile Registry, are available under :menuselection:`Accounting --> Reporting -->
Annual Accounts (PGC)`:

- :guilabel:`Balance Sheet (PGC)`;
- :guilabel:`Profit and Loss (PGC)`.

The report opens directly with two columns, :guilabel:`Current year` and :guilabel:`Previous
year`, based on the posted entries. The template (SMEs, complete, or non-profit entities) follows
the chart of accounts of the company. Click an amount to see the journal items behind it, and use
:guilabel:`Print` or :guilabel:`Export` to get a PDF or XLSX file.

.. note::
   Only accounts numbered according to the PGC are included. An account with a custom code that is
   not a sub-account of a PGC account is not included in the report.

.. seealso::
   - :doc:`../spain`
   - :doc:`../../accounting/reporting`

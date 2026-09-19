==========================
VAT return with ÁNYK forms
==========================

The :guilabel:`Magyar könyvelés és ÁNYK adatszolgáltatás` (`eyssen_l10n_hu_accountant`) module and
the yearly :guilabel:`ABEV` form packages prepare the Hungarian VAT return (form `xx65`, including
the domestic recapitulative `M` sheets) and the EC recapitulative statement (form `xxA60`) from the
posted journal entries, and export them as XML files that can be opened in the :abbr:`ÁNYK
(Általános Nyomtatványkitöltő)` form-filling program of NAV and submitted from there.

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Module
     - VAT return
     - EC recapitulative statement
   * - :guilabel:`ABEV 2024` (`eyssen_l10n_hu_abev_24`)
     - `2465`
     - `24A60`
   * - :guilabel:`ABEV 2025` (`eyssen_l10n_hu_abev_25`)
     - `2565`
     - `25A60`
   * - :guilabel:`ABEV 2026` (`eyssen_l10n_hu_abev_26`)
     - `2665`
     - `26A60`

The packages can be installed side by side; every tax year has its own menu entries under
:menuselection:`Accounting --> Adóbevallás`. The pages below describe the 2026 forms; the forms of
the other years work in the same way.

.. note::
   - The menus, fields and messages of these modules are displayed in Hungarian, following the
     official wording of the ÁNYK forms.
   - The returns can be created by users with the :guilabel:`Show Full Accounting Features` access
     right. Returns cannot be deleted.
   - As an alternative to ÁNYK, the VAT return can be filed through the :doc:`NAV eÁFA
     machine-to-machine interface <evat>`.

.. _localizations/hungary/abev-codes:

Return lines and tax grids
==========================

The lines of the returns are computed from the **tax grids** of the posted journal items. The mapping
is maintained in :menuselection:`Accounting --> Configuration --> Adóbevallás --> Adóbevallás
kódok`: each row is a line of a form (:guilabel:`Kód`, :guilabel:`Megnevezés`, :guilabel:`Bevallás
típus`, :guilabel:`Kategória`) with the tax grids (:guilabel:`Címkék`) that feed it. Each form
package loads its lines with the tax grids of the Hungarian chart of accounts (for example, line
`05` collects the grids `+alap_fiz_5` and `+afa_fiz_5`), so the list normally needs to be changed
only when custom taxes with custom tax grids are used. Use the :guilabel:`Aktív` toggle to switch a
line off, and the filters to display the lines of one form.

.. important::
   Make sure that the taxes used on invoices carry the tax grids of the Hungarian chart of accounts
   on their :guilabel:`Distribution for Invoices` and :guilabel:`Distribution for Refunds` lines;
   amounts without a mapped tax grid are not included in the return.

VAT return (2665)
=================

Go to :menuselection:`Accounting --> Adóbevallás --> 2665 - Áfa bevallás` and click
:guilabel:`New`. Only one draft return can exist at a time.

#. On the :guilabel:`2665A` tab, check the taxpayer data (:guilabel:`Adózó`, tax number or group
   identification number), fill in the :guilabel:`Ügyintéző` (contact person) and phone number, and
   set the period (:guilabel:`Bevallási időszak kezdete` and :guilabel:`vége`) and the
   :guilabel:`Bevallás gyakorisága`: *H = Havi* (monthly), *N = Negyedéves* (quarterly) or
   *E = Éves* (yearly). A new return proposes the month following the last finished return; for
   quarterly and yearly returns type the dates of the period.
#. Click :guilabel:`Frissítés` (refresh). The lines are computed from the posted entries whose
   **accounting date** falls into the period, in thousand HUF:

   - tabs :guilabel:`01-01` and :guilabel:`01-02`: payable VAT; :guilabel:`01-03`: deductible VAT
     (partially deductible taxes are weighted with their :ref:`Alap % Áfa bevallásban
     <localizations/hungary/taxes>` value); :guilabel:`01-04`: settlement (lines 82–86) and detailed
     data; :guilabel:`01-05`: domestic reverse charge and the totals of the M sheets;
   - tabs :guilabel:`07` and :guilabel:`08`: domestic reverse-charge sales and purchases per invoice
     and product, with VTSZ number and weight;
   - tab :guilabel:`2665M`: one M sheet per domestic partner tax number, listing **all** posted
     vendor bills (sheet `02`) and vendor credit notes (sheet `02-K`) of the period. The invoice
     number is the :guilabel:`Bill Reference`.

   The two icons next to every non-zero line open the journal entries and the journal items behind
   the amount.
#. Check the settlement on tab :guilabel:`01-04`. Line `82` (amount carried forward from the
   previous period) is taken from line `86` of the last finished return of the same year's form; on
   the very first return it must be typed in (a red message reminds of it). If line `83` is
   negative, choose in the yellow box whether the amount is reclaimed (:guilabel:`Visszaigénylem`,
   line `85`) or carried forward (:guilabel:`Átviszem a következő hónapra`, line `86`, the default).
#. Click :guilabel:`Export XML` to download the file
   `ABEV2665_<tax number>_<period start>_<period end>.xml`, which contains the `2665A` form and the
   `2665M` sheets. Import it into ÁNYK (:menuselection:`Szerviz --> Egyedi importálás`), check it,
   and submit it.
#. Click :guilabel:`Kész` (done) to close the return. A finished return cannot be reset to draft.

:guilabel:`Kiürítés` empties a draft return (everything except line `82`).

.. screenshot:: finance-fl-hungary-abev-2665-form
   :menu: Accounting ‣ Adóbevallás ‣ 2665 - Áfa bevallás ‣ (draft return)
   :shows: Draft VAT return with the header buttons "Export XML", "Frissítés", "Kiürítés", "Kész", the status badge "Tervezet", and the tab bar ("2665A", "01-01" … "2665M"); tab "01-01" open with computed base and VAT amounts and the two drill-down icons next to the lines.
   :highlight: The "Frissítés" and "Export XML" buttons (red frame).
   :data: Demo company "YourCompany HU", monthly return for the previous month with a few sales at 27% and 5%.
   :module: eyssen_l10n_hu_abev_26
   :notes: Hungarian field labels (hardcoded), light theme, 1440px width, crop to the form sheet.

The return stops with an error message if, for example, a domestic vendor has no tax number, a vendor
credit note is not linked to its original bill, the original bill has no reference, or (from the 2025
forms) the VAT of lines `14` or `69` differs from 27% of their base by more than the tolerance.

On invoices and bills that were included in a return, a tab named after the return (for example,
:guilabel:`2665 - Áfa bevallás`) appears inside the :guilabel:`NAV` tab.

Self-revision
-------------

On a finished return, click :guilabel:`Önellenőrzés` to create a self-revision for the same period
(:guilabel:`Bevallás jellege`: *O = Önellenőrzés*), then click :guilabel:`Frissítés`. The
:guilabel:`Változások` tab compares the self-revision with the original return: changed fields (the
original value is also shown in red under every changed line), and the invoices that were added or
removed.

.. important::
   The self-revision sheet (tab :guilabel:`04`) is not computed and is not part of the exported XML
   in the current module version: fill in the self-revision data and the self-revision surcharge in
   ÁNYK. The tabs :guilabel:`170`, :guilabel:`02`, :guilabel:`EUNY`, :guilabel:`06`, :guilabel:`09`
   and :guilabel:`A88` are placeholders; fill in these sheets in ÁNYK if they apply to the company.

EC recapitulative statement (26A60)
===================================

Go to :menuselection:`Accounting --> Adóbevallás --> 26A60 - Összesítő nyilatkozat`, click
:guilabel:`New`, fill in the contact person, the period and the :guilabel:`Összesítő nyilatkozat
gyakorisága` (*H = Havi*, *N = Negyedéves*, *Á = Negyedévesről havira áttérés*, *V = Haviról
negyedévesre visszatérés*), and click :guilabel:`Frissítés`.

The tabs :guilabel:`01` (intra-Community supplies of goods), :guilabel:`02` (acquisitions of goods),
:guilabel:`03` (services supplied) and :guilabel:`04` (services received) list one row per partner
with the country code, the EU VAT number and the value in thousand HUF. Only partners located in
another EU member state are included (the country must belong to a country group flagged
:guilabel:`EU`). :guilabel:`Show Invoices` and the row icons open the underlying entries.

Click :guilabel:`Export XML` to download `ABEV26A60_<EU VAT number>_<start>_<end>.xml` for ÁNYK, then
:guilabel:`Kész`. Sheet `05` (call-off stock) is not filled in.

VAT analytics
=============

:menuselection:`Accounting --> Reporting --> Statement Reports --> Áfa analítika` lists the VAT
content of the posted invoices, credit notes and miscellaneous entries of a period by document and
tax, as a supporting schedule of the VAT return. Set :guilabel:`Kezdete` (start) and :guilabel:`Vége`
(end) and click :guilabel:`Print` for a PDF or :guilabel:`Excel` for a spreadsheet with the sheets
*Összesítő* (summary), *Fizetendő áfa* (payable VAT) and *Levonható|visszaigényelhető áfa*
(deductible VAT). Documents are selected by accounting date; cash-basis taxes are included when
their cash-basis entry is created.

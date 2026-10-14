============================
CAD bill of materials import
============================

A steel structure fabricator usually receives the project documentation as a DWG (sometimes DXF)
drawing. The drawing may contain one or more parts lists (also tables pasted from a spreadsheet, and
lists per assembly with a summary table), position blocks with attributes, or nothing but
position labels next to the members ("R1 / 100x100x4", "GM1 / U180", "PM 2 / 300x300x10",
"Bolt / M 16"). The eYssen module **CAD Bill of Materials Import** (``mrp_cad_bom_import``) turns such
a drawing into:

- a reviewed material list with weights taken from a steel section catalogue;
- a material summary by kind of material, section and grade, with the total weight without and with
  purlins;
- a purely kg-based quotation (manufacturing price per kg and assembly price per kg);
- after acceptance, a bill of materials with matched or newly created products; and
- a procurement list in stock lengths with cutting waste, and draft requests for quotation.

.. note::
   Nothing is final until you have reviewed it. The importer marks every line it is unsure of, and
   the :doc:`AI bridge <../../productivity/ai/cad_bom_import>` only ever *suggests* quantities
   and lengths that you accept or reject one by one.

The workflow
============

Every import is a record in :menuselection:`Manufacturing app --> CAD imports` that moves through six
statuses: :guilabel:`Draft`, :guilabel:`Parsed`, :guilabel:`Reviewed`, :guilabel:`Quoted`,
:guilabel:`Accepted` and :guilabel:`Done`.

.. list-table::
   :header-rows: 1
   :widths: 18 32 50

   * - Step
     - What you do
     - Result
   * - Upload
     - Add the DWG or DXF files under :guilabel:`Drawings (DWG, DXF)`.
     - The files are attached to the import.
   * - Parse
     - Click :guilabel:`Parse drawings`. If the drawings contain several parts lists, choose the ones
       to import first.
     - The lines are extracted, the products are matched and the summary is built. Status:
       :guilabel:`Parsed`.
   * - Review
     - Correct the lines, then click :guilabel:`Mark as reviewed`.
     - Status :guilabel:`Reviewed`. Open conflicts are logged in the chatter.
   * - Quote
     - Click :guilabel:`Create quotation`.
     - A sales quotation priced per kg. Status :guilabel:`Quoted`.
   * - Accept
     - Confirm the quotation, or click :guilabel:`Mark as accepted`.
     - Status :guilabel:`Accepted`. If the setting is on, the bill of materials is created at once.
   * - Bill of materials
     - Click :guilabel:`Create BoM` (Manufacturing administrators).
     - A new bill of materials version. Status :guilabel:`Done`.
   * - Purchase
     - Click :guilabel:`Procurement list`, then :guilabel:`Create RFQs`.
     - A list of bars and sheets to buy, and draft requests for quotation. Nothing is confirmed.

.. screenshot:: manufacturing-cad-import-form
   :menu: Manufacturing app --> CAD imports --> (an import)
   :shows: A parsed CAD import with the status bar, the weight block (Option 1, purlins, Option 2) and the
      Lines tab.
   :highlight: The status bar and the weights block (red frames).
   :data: A staircase steel structure with about twenty lines, two of them orange and one red.
   :module: mrp_cad_bom_import
   :notes: English UI, light theme, 1440px width.

.. toctree::
   :titlesonly:

   cad_bom_import/setup
   cad_bom_import/drawings
   cad_bom_import/quotation_bom

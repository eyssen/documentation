===========================================
Read a drawing and review the material list
===========================================

Create an import
================

Open :menuselection:`Manufacturing app --> CAD imports` and click :guilabel:`New`. Give the import a
name (for example "Staircase steel structure") and, if you want, a :guilabel:`Customer`, a
:guilabel:`Project` and a :guilabel:`Responsible`. The :guilabel:`Reference` is numbered
automatically (``CAD/<year>/...``). Add the drawings under :guilabel:`Drawings (DWG, DXF)`; you can add
several files.

Under the drawings, :guilabel:`Default material grade` and :guilabel:`Bolt property class` give the grade
of the lines that name none. They start from the :ref:`settings <manufacturing/cad_bom_import/requirements>`
and are overridden by the general notes of the drawing, for example "MATERIALE FOLOSITE: PROFILE
LAMINATE - OL 37 (S235) ... ȘURUBURI - GRUPA 8.8", which gives S235JR and 8.8.

Click :guilabel:`Parse drawings`. The :guilabel:`Extraction` field then names the strategy that found
the lines, the tab :guilabel:`Parse log` lists what was read, repaired or ignored, and the import is
:guilabel:`Parsed`. You can parse again while the import is parsed or reviewed: the lines that were not
added by hand are replaced, and the lines you added manually are kept.

.. note::
   Texts are read from model space and every paper space of the drawing, including the texts inside
   blocks. For a DWG, ``dwgread`` converts the file first; text in other code pages (for example
   Central European drawings) is decoded with the code page stored in the drawing.

How the lines are found
=======================

The importer tries three strategies in order. The first one that finds lines wins; the label
strategy runs only when the others found nothing. The :guilabel:`Source` of every line shows which
one produced it: :guilabel:`Parts list table`, :guilabel:`Block attributes`, :guilabel:`Labels`,
:guilabel:`Manual` or :guilabel:`AI suggestion`.

Parts list table
----------------

The texts of the drawing are grouped into rows. A row is the **header** of a parts list when at least
three of its cells are recognised by a table of synonyms in Romanian, Hungarian, English, German and
Spanish, for example mark (*Poz, Pos, Mark, Marca, Tétel, Jel*), quantity (*Buc, Db, Qty, Pcs, Stk,
Cant*), profile (*Profil, Szelvény, Section, Perfil*), material or grade, length, width, thickness,
weight, description, area and notes.

- The columns come from the vertical lines that cross the header, or else from the midpoints
  between the header texts.
- The rows below *and above* the header are read (a parts list in a title block grows upwards) and
  the longer run is kept. The run ends at a gap that is too large, at another header, or where no
  text is left in the table.
- A row of units (``mm``, ``kg``, ``buc``) sets the column units, and units in the header such as
  ``[m]`` or ``(cm)`` convert lengths to millimetres. A length below 30 with decimals and no unit is
  read as metres, and the parse log says so.
- ACAD_TABLE objects are read the same way.
- A weight written on the drawing is kept in :guilabel:`Weight on drawing (kg)`. If it differs from
  the computed weight by more than 5 %, the line gets a conflict note.

Block attributes
----------------

Blocks with attributes (``POS``, ``QTY``, ``PROFILE``, ``LENGTH``, ``MATERIAL``, ``WEIGHT``, and
their Romanian, Hungarian and German names) become lines, grouped by mark, section and length. With
a quantity attribute the quantity is the largest value found (different values are a conflict,
because several references often carry the assembly quantity). Without it, the quantity is the
number of block references and the line is flagged to review. The setting :guilabel:`Block attribute
tags` adds your own tag names.

Labels
------

Many drawings have no parts list, only a label next to each member. The importer then reads every
short text, pairs a mark (``R1``, ``PM 2``, ``GM1``) with a section designation written in the same
text or just below or beside it, and groups the lines by mark and section.

.. important::
   **The number of labels is not the quantity.** The same member is labelled in several views and
   sometimes several times in one view. The label strategy therefore stores the count as
   :guilabel:`Occurrences`, sets the quantity to 1, leaves the length empty and flags the line
   :guilabel:`To review`. Only an explicit text such as ``4 buc``, ``2 db``, ``n=2`` or ``L=2500``
   fills the quantity or the length. Without a length, a linear member has no weight until you
   enter it (or accept an :doc:`AI suggestion <../../../productivity/ai/cad_bom_import>`).

Other rules of the label strategy:

- Words for existing members (*existent, existing, meglévő, vorhanden, existente*) make the line
  :guilabel:`Excluded`: it is shown but not counted.
- Holes and annotations (*Găuri, furat, holes, Bohrung, Secțiune, Plan, Detaliu*) are ignored and
  counted in the parse log.
- Bolt words (*Bulon, Șurub, Csavar, Bolt, Schraube, Tornillo*) make a bolt line.
- A bare plate or round size without a mark is ignored as too ambiguous.
- If the same mark appears with different sections (for example PM 3 as 200x250x10 and 200x350x10),
  every line of that mark gets a conflict note.

Section designations
--------------------

Designations are normalised before they are looked up: upper case, no accents, ``×`` and ``*`` as
``x``, decimal comma as point, and a trailing grade (``S235JR``, ``OL 37``) is split off. A count
prefix such as ``2xL50x5`` is kept as a count.

.. list-table::
   :header-rows: 1
   :widths: 20 50 30

   * - Family
     - Accepted forms
     - Becomes
   * - I and H sections
     - ``IPE200``, ``HE 200 A``, ``HE200B``, ``I 200``
     - ``IPE 200``, ``HEA 200``
   * - Channels
     - ``U180``, ``UNP 180``, ``UPN180``, ``UPE 200``
     - ``UPN 180``
   * - Angles
     - ``L50x5``, ``L 50x50x5``, ``L100x50x6``, ``Cornier 60x6``
     - ``L 50x5``, ``L 100x50x6``
   * - Square and rectangular hollow sections
     - ``SHS 100x100x4``, ``RHS 80x120x5``, ``TEAVA 60x60x4``, a bare ``100x100x4``
     - ``SHS 100x100x4``
   * - Round hollow sections
     - ``Ø88.9x4``, ``CHS 114.3x5``, ``%%C88,9x4``
     - ``CHS 88.9x4``
   * - Flat and round bars
     - ``FL 50x5``, ``Platbandă 5x60``, ``-80x8``, ``Ø20``
     - ``FL 60x5``, ``Ø20``
   * - Plates
     - ``PL 10x300x400``, ``PL10``, ``t=12``, ``Tablă 2x1000x2000``
     - ``PL 300x400x10``
   * - Z, C and Σ purlins
     - ``Z200/2.0``, ``Z 200x2``, ``C150/2``, ``Σ200/2.5``
     - ``Z200/2.0``
   * - Bolts
     - ``M16``, ``M16x60-8.8``, ``4xM20x80 10.9``, ``Șurub M12``
     - ``M16x60`` and a property class

A bare ``AxBxC`` is decided by context: a plate mark prefix (see the settings) or a thickness written
first (``10x300x300``) means a plate; otherwise it is a hollow section when the thickness is at most
16 mm and the sides at most 500 mm, and the line is marked as ambiguous with a lower confidence.
A plate thinner than 3 mm is a sheet.

Review the lines
================

The tab :guilabel:`Lines` is an editable list. Change anything that is wrong, add lines with
:guilabel:`Add a line` and drag the handle to reorder. When you change the :guilabel:`Section`, the
dimensions, family and weight are worked out again.

The colour of a line tells you what to look at:

- **Orange**: :guilabel:`To review`, for example a quantity that is only a guess.
- **Red**: a :guilabel:`Conflict`, with the reason in the conflict note (same mark with different
  sizes, weight on the drawing that differs from the computed weight, a grade that is not in the
  material master, different quantities in the attributes).
- **Grey**: :guilabel:`Excluded`, an existing member that is not counted.

.. screenshot:: manufacturing-cad-import-lines
   :menu: Manufacturing app --> CAD imports --> (an import) --> Lines
   :shows: The Lines tab with orange, red and grey lines, and the columns Mark, Section, Material,
      Quantity, Length, Unit weight, Total length and Total weight.
   :highlight: One orange line, one red line and the Quantity and Length columns (red frames).
   :data: The staircase import: marks R1, GM1, PM 2 (orange), PM 3 (red, two sizes) and an excluded
      existing member.
   :module: mrp_cad_bom_import
   :notes: English UI, light theme, 1440px width.

Use the optional columns for the rest: :guilabel:`Family`, :guilabel:`Height (mm)`,
:guilabel:`Width (mm)`, :guilabel:`Thickness (mm)`, :guilabel:`Diameter (mm)`,
:guilabel:`Occurrences`, :guilabel:`Source`, :guilabel:`Confidence`, :guilabel:`Weight on drawing
(kg)`, :guilabel:`Drawing text` and :guilabel:`Product action`. For bolts the grade column becomes the
:guilabel:`Property class`. A grade written on the drawing that is not in the material master is kept
as :guilabel:`Grade on drawing`; the line is flagged and weighed with the density of steel until you
choose a material.

When every line is right, click :guilabel:`Mark as reviewed`. Open conflicts are written in the
chatter.

Weights and the steel section catalogue
=======================================

The weight of a line comes from the density of its material and from the mass per metre of the
section.

- The **catalogue** under :menuselection:`Manufacturing app --> Configuration --> Steel sections`
  holds the sections with their dimensions and mass per metre: IPE 80 to 600, HEA, HEB and HEM, UPN
  and UPE channels, and equal and unequal angles. The values follow EN 10365 and EN 10056-1 and are
  tabulated for steel of 7850 kg/m³. Manufacturing administrators can edit the catalogue.
- The tabulated mass is scaled by *density of the grade / 7850*, so the same section in stainless
  steel (7900 kg/m³) or aluminium (2700 kg/m³) is weighed correctly. A line without a grade is weighed
  as steel at 7850 kg/m³.
- **Hollow sections** are calculated from their dimensions with the corner radii of EN 10219-2
  (SHS 100x100x4 is 11.73 kg/m); round hollow sections, flat bars and round bars from their
  geometry.
- **Plates** weigh width x length x thickness x density per piece (300x300x10 is 7.065 kg), and
  their area is given in m².
- **Z, C and Σ purlins** are calculated from the developed width of the section and its thickness.
  The generic geometry per height is stored in the catalogue and is editable; the server action
  :guilabel:`Recompute purlin weight from geometry` recalculates the mass after you change the
  flange or lip. Align the values with your supplier.
- **Bolts** are counted in pieces and add no weight to the totals.

For each line the list shows the :guilabel:`Unit weight` (per metre or per piece), the
:guilabel:`Total length (m)`, the :guilabel:`Total area (m²)` and the :guilabel:`Total weight (kg)`. If
nothing can be calculated, the weight written on the drawing is used.

Material summary and the two options
====================================

The tab :guilabel:`Material summary` adds the lines up by kind of material and section: pieces, total
length, area and weight. Click :guilabel:`Refresh` to rebuild it; it is also rebuilt whenever a line
changes. The weights block above the tabs shows three totals:

- :guilabel:`Option 1: without purlins (kg)`: the total weight without the purlin lines;
- :guilabel:`Purlins (kg)`: the weight of the purlins; and
- :guilabel:`Option 2: with purlins (kg)`: the total weight including the purlins.

A line is a purlin when its family is Z, C or Σ; the :guilabel:`Purlin` box can be changed by hand.
Excluded lines are in no total.

Use :guilabel:`PDF` or :guilabel:`Print summary` for the report *Material summary* (the summary,
option 1, the purlins, option 2 and the lines to check), and :guilabel:`XLSX` for a spreadsheet with
the summary and a sheet with the detailed lines.

Limits
======

- The label strategy cannot know quantities and lengths. They are left for you to review, or for the
  :doc:`AI bridge <../../../productivity/ai/cad_bom_import>` to suggest.
- A parts list needs a header with at least three recognised columns. Rotated tables and tables
  that are split over several areas of the drawing are not joined.
- LibreDWG does not decode every DWG object (for example proxy entities). The contents of an
  ACAD_TABLE in a DWG are read from the graphics of the table, not from its cells.
- Purlin weights are generic until you align the catalogue with the supplier.

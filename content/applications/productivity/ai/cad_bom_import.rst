==================
AI for CAD imports
==================

The module **AI CAD BoM import** (``ai_mrp_cad_bom``) helps with the part of a CAD import that the
rules cannot do. A drawing that only has position labels ("R1 / 100x100x4", "PM 2 / 300x300x10",
"Bolt / M 16") tells you *which* members exist but not *how many* there are or *how long* they are,
because the same member is labelled in several views. The AI reads the drawing again, including its
dimensions, and **suggests** values that you accept or reject. It installs itself when the AI module and
the :doc:`CAD import <../../inventory_and_mrp/manufacturing/cad_bom_import>` are both installed.

.. important::
   The AI never writes a quantity, length, section or product on its own, and it never creates products
   or bills of materials. A suggestion changes the import only when you accept it, and the weights, the
   totals of the two options and the material summary change only then. Products and bills of
   materials are still created by the normal flow of the CAD import.

Requirements
============

- A chat model is configured (see :doc:`models_and_providers`).
- You are in the group :guilabel:`AI: User`, the capability *Ask* is on for you (see
  :doc:`feature_access`) and you may edit CAD imports (*Manufacturing / User*).
- The import is :guilabel:`Parsed` or :guilabel:`Reviewed`.

Analyse an import
=================

Open a parsed import and click :guilabel:`Analyse with AI` in the form header. The analysis runs in the
background, so you can keep working. The form shows the progress (it refreshes every few seconds) and
you are notified when the suggestions are ready or when the analysis failed. Only one analysis runs for
an import at a time, and while it runs you can neither parse the import again nor accept or reject
suggestions.

The job runs in your own environment: your language, your company, your access rights. It goes through
these steps and commits each one separately, so a failure keeps the suggestions of the steps that were
finished and shows the error under :guilabel:`AI analysis failed:` and in the chatter.

1. **Reading the drawing.** The drawing is read again for its geometry (see below).
2. **Interpreting the lines.** The AI checks every line: its kind, family, designation, grade, whether it
   is a purlin and a short description. It decides the ambiguous ``AxBxC`` (plate or hollow section),
   reads the general notes of the drawing (grade, bolt class, standards) and explains conflicts such as
   the same mark with different sizes.
3. **Estimating quantities and lengths.** For the lines that came from labels, the AI proposes the
   number of pieces and the length of one piece (or the width and length of a plate), with its
   reasoning and the evidence. A quantity or a length that is written on the drawing is never
   estimated again. A line whose quantity and length are both stated is not sent to the model at all.
   When only one of the two is stated, it is passed to the model as known, and the answer cannot
   change it. Lines that were read from a parts list or from block attributes are not estimated.
4. **Matching products.** Lines without a product get a suggested existing product, chosen among a few
   candidates that the server selected.
5. **Checks.** Rule-based checks look for gaps (see below). This step does not use the AI.
6. **Review note.** A short note in your language with the totals now and the totals if you accepted
   every suggestion, the main materials and the checks. It is shown on the tab :guilabel:`AI review` and
   posted in the chatter.

Every answer is parsed as JSON and checked. Whatever is not valid is dropped: unknown lines, products
that were not offered as candidates, designations the parser cannot read, negative values and views that
do not exist.

How the drawing is read
-----------------------

The geometry step collects the dimensions of the drawing (linear and aligned dimensions of model and
paper space), splits each space into views and sheet frames, and finds the title of each view
(*SECTIUNE, PLAN, DETALIU, SECTION, DETAIL, METSZET, ALAPRAJZ, ...*), the cut markers and the sheet
numbers. The scale of a view comes from its dimensions: a drawing made at 1:10 with a dimension scale
factor of 10 is detected as such, and lengths are given to the AI in millimetres.

For each line the AI receives its labels per view, with the position of each label, the leader line that
touches it, the segments the leader points to (the member), the nearest lines and the nearest
dimensions. The AI is told that the same piece is labelled in several views, so pieces are counted once
(usually from the plan) and lengths are taken from sections and details.

Review the suggestions
======================

The tab :guilabel:`AI review` appears after an analysis. It has:

- the :guilabel:`AI review note` and the :guilabel:`Drawing notes read by the AI`;
- the list :guilabel:`Suggestions to review`: for each line the current quantity and length, what the AI
  proposes (:guilabel:`AI quantity`, :guilabel:`AI length (mm)`), its :guilabel:`Confidence`, the reasoning,
  the evidence (views and values) and a note; and
- the list :guilabel:`Checks`.

Use the buttons :guilabel:`Accept` and :guilabel:`Reject` on a line (the ticks in the list of lines do the
same), :guilabel:`Accept all above the threshold` and :guilabel:`Reject all`. :guilabel:`Run the checks
again` repeats the checks without the AI, for example after you corrected a line. Suggestions can be
accepted or rejected while the import is parsed or reviewed.

Accepting a suggestion applies:

- a changed designation (the line is parsed again: family, kind, dimensions, plate size), otherwise the
  kind;
- the grade (it is resolved through the material master, so "OL37" becomes S235JR), the description and
  the purlin flag;
- the quantity, and the length of a linear member or the width and length of a plate when missing; and
- the suggested product, as if you had chosen it by hand.

The line's source becomes :guilabel:`AI suggestion` and the confidence is stored. **A line whose confidence
is below the threshold stays flagged** :guilabel:`To review` after you accept it. The threshold is the
field :guilabel:`AI confidence threshold` on the tab (0.6 by default, from the settings), and
:guilabel:`Accept all above the threshold` accepts only suggestions that reach it.

A product that you accept from the AI, or that you choose by hand on an analysed line, is remembered as
an alias, so the next import finds it without the AI.

.. screenshot:: manufacturing-cad-import-ai-review
   :menu: Manufacturing app --> CAD imports --> (an import) --> AI review
   :shows: The AI review tab with the review note, the suggestions list with the proposed quantity,
      length, confidence and reasoning, and the checks list.
   :highlight: The confidence column and the Accept and Reject buttons (red frames).
   :data: The staircase import after an analysis, with one low-confidence suggestion.
   :module: ai_mrp_cad_bom
   :notes: English UI, light theme, 1440px width.

Checks
------

The checks never change data. They report: bolts without nuts or washers; a plate with no bolt or hole
label near any of its labels; purlins without sag rods or tie rods (information); a missing grade; open
conflicts, with the AI's explanation; a linear member without a length and without an estimate; a piece
longer than the stock bar (information); a line whose weight is far above the others (more than eight
times the median and more than 40 % of the total); and the number of suggestions below the threshold
(information). Each check is a warning or an information.

Quick prompts
=============

On a CAD import the AI panel (see :doc:`panel`) offers the quick prompts :guilabel:`Explain this import`
(in place of the generic *Summarise*), :guilabel:`What still needs review?` and :guilabel:`Material totals
by type`. The panel sees the lines, the material summary and the checks of the import, as far as your
own access rights allow.

Choose the model
================

The analysis is interactive: you wait for the suggestions. Use a fast chat model with a low cost per
call (see :doc:`models_and_providers`).

- Model variants that run as a batch (names ending in ``:batch``) do not suit this analysis, because
  their answers arrive much later.
- Very slow reasoning modes can take longer than the timeout of the provider. If you use one, raise the
  :guilabel:`Timeout` of the provider (see :doc:`configuration`).

Cost, limits and data sent to the model
=======================================

- Every call goes through the normal AI machinery: the capability *Ask*, the rate limit, the blocked
  patterns and the AI log with its cost (see :doc:`monitoring`). In the background job the per-minute
  rate limit is waited for instead of failing, but the daily limits stop the job at once.
- The size depends on the drawing. The analysis of a staircase drawing with 260 labels, 17 groups of
  members and 787 dimensions took seven calls and about 22,000 input tokens. A very large drawing is
  limited to twenty estimation requests (roughly 100,000 tokens); the lines beyond are reported as not
  estimated.
- The model receives the line data and texts of the drawing, the general notes, the geometric context
  (numbers, view titles and sheet numbers), the totals and check messages for the note, and, for matching,
  the names and internal references of the candidate products. It receives **no** customer, project or
  import name and no other business data.

Settings
========

In :menuselection:`Manufacturing app --> Configuration --> Settings`, block :guilabel:`CAD BoM import`,
under :guilabel:`AI suggestions`:

- :guilabel:`AI confidence threshold`: estimates below it stay flagged to review and are left out of
  :guilabel:`Accept all above the threshold`. Default 0.6.
- :guilabel:`Analyse with AI after parsing`: queues the analysis automatically after each parse when
  label lines need a review and you may use the AI; otherwise it is skipped silently. Off by default.

.. seealso::
   - :doc:`../../inventory_and_mrp/manufacturing/cad_bom_import`
   - :doc:`app_integrations`

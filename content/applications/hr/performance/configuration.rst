=============
Configuration
=============

Everything on this page lives under :menuselection:`Performance --> Configuration` and needs
the :guilabel:`Administrator` access level of the :guilabel:`Performance` category. Set the
rating scale up first, then the questionnaire that uses it, then the company options.

.. _performance/config/scales:

Rating scales
=============

A rating scale is a list of levels. Each level carries a name, a numeric value and a
description of the behaviour it stands for.

Why a level carries a number
----------------------------

Without a number, a rating is a word. *Good* cannot be averaged, compared with last year,
plotted against a department, or weighted against another question. The number is what makes
a rating comparable; the description is what makes it fair. A scale that has one without the
other produces either arithmetic nobody trusts or opinions nobody can aggregate.

.. tip::
   If you would rather not show the numbers, tick :guilabel:`Hide Numeric Value` on the scale.
   The levels are then shown by name only, while everything that has to compute still can.

Creating a scale
----------------

#. Go to :menuselection:`Performance --> Configuration --> Rating Scales` and create a record.
#. Give it a :guilabel:`Name` and, if you like, a short :guilabel:`Code`.
#. Leave :guilabel:`Company` empty to make the scale a shared catalogue entry every company
   reads, or set it to restrict the scale to one company.
#. Decide on :guilabel:`Allow Not Applicable`. When it is on, a rater may state that they are
   not in a position to judge a question instead of guessing. When it is off, a question that
   uses the scale has to be answered.
#. On the :guilabel:`Levels` page, add one line per level:

   +-------------------------------+-------------------------------------------------------------+
   | Field                         | What it is for                                              |
   +===============================+=============================================================+
   | :guilabel:`Name`              | What the rater picks, for example *Meets expectations*.     |
   +-------------------------------+-------------------------------------------------------------+
   | :guilabel:`Value`             | The numeric anchor. This is the reason the level exists as  |
   |                               | a record: it is what makes two ratings comparable and what  |
   |                               | every average is computed from.                             |
   +-------------------------------+-------------------------------------------------------------+
   | :guilabel:`Description`       | The behaviour a rater should recognise before picking this  |
   |                               | level. It is shown at rating time, and it is the single     |
   |                               | most effective thing you can write to make two managers     |
   |                               | rate the same way.                                          |
   +-------------------------------+-------------------------------------------------------------+
   | :guilabel:`Below Expectation` | Marks the level as under the bar. Used by the analysis      |
   |                               | views and by decorations.                                   |
   +-------------------------------+-------------------------------------------------------------+
   | :guilabel:`Count In Average`  | On by default. Turn it off for a level that should not drag |
   |                               | a score, for instance a *Not observed* level.               |
   +-------------------------------+-------------------------------------------------------------+
   | :guilabel:`Target Share (%)`  | Advisory distribution guidance for calibration              |
   |                               | conversations. It is never enforced: nothing stops a        |
   |                               | department from rating everybody at the top level.          |
   +-------------------------------+-------------------------------------------------------------+

.. important::
   Write the :guilabel:`Description` of every level. It costs an afternoon, and it is what
   stops *3* meaning "fine, I suppose" for one manager and "genuinely strong" for another.

Starting from a scale somebody else wrote
-----------------------------------------

If you would rather not start from an empty form, open
:menuselection:`Performance --> Configuration --> Starter Rating Scale`. Give the scale a
:guilabel:`Scale Name`, decide on :guilabel:`Allow Not Applicable`, and click
:guilabel:`Create the Scale`. It writes an ordinary five-level scale — from *Well below
expectations* to *Outstanding* — that you then rename and reword. It is a starting point, not a
recommendation, and the wizard says so.

If you already have a scale, the wizard warns you that this creates another one.

Nothing is shipped, on purpose
------------------------------

No rating scale and no questionnaire come with the application. Generic seed content would
encode one company's culture and one language's wording, and every customer would then spend
their first week editing it out. The Hungarian pack does ship a five-level Hungarian scale with
behavioural descriptions and four Hungarian questionnaires, because those are written for one
specific practice — see :doc:`probation_hu`.

A scale that has been used is frozen
------------------------------------

As soon as a rating has been recorded on a scale, its levels can no longer be added, removed or
re-valued, and the form says so in a banner. Re-valuing a level would silently rewrite the
meaning of every rating ever given on it: last year's *3* would quietly become worth something
else, and every average, comparison and trend computed since would be wrong.

To change a frozen scale, click :guilabel:`New Version`. That copies the scale into a new,
editable one, points the old scale at its successor and archives it. Existing reviews keep the
version they were rated on; new cycles pick up the new one.

.. note::
   A used scale cannot be deleted either. Archive it instead: the reviews rated on it stay
   readable.

.. _performance/config/questionnaires:

Questionnaires
==============

A questionnaire is what people actually fill in. It is made of **sections**, and a section is
made of **questions**. Go to :menuselection:`Performance --> Configuration --> Questionnaires`.

Sections
--------

Each section has a :guilabel:`Name`, a :guilabel:`Sequence` and a :guilabel:`Kind`:

- **Questions** — the ordinary case: the questions you write under it.
- **Objectives of the period** — no questions of its own. It renders the objectives that were
  in scope for the period, so the conversation starts from what was agreed. See
  :doc:`objectives`.
- **Competencies** — filled in by the **Review Competencies** module. See :doc:`competencies`.
- **Free text** — a section with no structure, for a narrative.

Audiences
---------

Both a section and a question state who is asked to answer it:

+------------------------+----------------------------------------------------------------------+
| Audience               | Who answers                                                          |
+========================+======================================================================+
| Everybody              | The employee, the reviewer and every other rater.                    |
+------------------------+----------------------------------------------------------------------+
| The employee           | The self-assessment only.                                            |
+------------------------+----------------------------------------------------------------------+
| The manager            | The reviewer only.                                                   |
+------------------------+----------------------------------------------------------------------+
| Other raters           | Peers, direct reports, skip levels and outside contacts only.        |
+------------------------+----------------------------------------------------------------------+
| Same as the section    | On a question: inherit whatever the section says. This is the        |
|                        | default.                                                             |
+------------------------+----------------------------------------------------------------------+

This is what lets one questionnaire serve the whole review. The employee is asked the questions
addressed to them, the reviewer is asked theirs, and a multi-rater round asks the *Other raters*
ones — out of a single stored set of answers, which is why aggregation, weighting and the
anonymity threshold behave consistently everywhere.

Questions
---------

A question carries:

- :guilabel:`Name` — the question itself, and :guilabel:`Guidance` under it for what the person
  answering should think about.
- :guilabel:`Answer Type`:

  +----------------------+--------------------------------------------------------------------+
  | Answer type          | What the person answering sees                                     |
  +======================+====================================================================+
  | Rating               | The levels of the rating scale, with their descriptions.           |
  +----------------------+--------------------------------------------------------------------+
  | Free text            | A text box.                                                        |
  +----------------------+--------------------------------------------------------------------+
  | Number               | A numeric field.                                                   |
  +----------------------+--------------------------------------------------------------------+
  | Yes / No             | A checkbox.                                                        |
  +----------------------+--------------------------------------------------------------------+
  | Multiple choice      | The options you defined on the question, each carrying its own     |
  |                      | numeric value.                                                     |
  +----------------------+--------------------------------------------------------------------+

- :guilabel:`Rating Scale` — set it only to override the questionnaire's default scale for this
  one question.
- :guilabel:`Required` — a required question blocks submission until it is answered.
- :guilabel:`Comment Policy` — *No comment*, *Comment optional* or *Comment required*. Use
  *Comment required* on the summary rating: a number with no sentence behind it is the hardest
  thing to defend in a review conversation.
- :guilabel:`Weight` — only used when :guilabel:`Use Weights` is on for the questionnaire.
  Leave weights off unless you have a reason; while they are off, a score is a plain mean of
  the rating answers whose level counts in the average.

.. _performance/config/shared:

The "shared with the employee" decision
---------------------------------------

Every question carries :guilabel:`Shared With Employee`. It decides whether the answer to that
question is shown to the employee when the review is released to them. It is on by default.

Turn it off deliberately and rarely. A question the employee never sees is a question they
cannot answer back to, and a review made mostly of such questions is not a review, it is a
file. The legitimate cases are narrow: a succession or readiness judgement that is an input to
a management decision rather than feedback to a person.

.. important::
   :guilabel:`Shared With Employee` decides what is shown **when the review is shared**, not
   whether an answer is confidential in general. HR reads every answer. The rating and the
   calibration are confidential for a different reason and by a different mechanism — see
   :doc:`confidentiality`.

Releasing and versioning
------------------------

A questionnaire is :guilabel:`Draft` while you build it. Click :guilabel:`Release` to make it
usable by a cycle. Release refuses a questionnaire that is not finished, and says which part:

- a questionnaire with no section;
- a *Questions* section with no question;
- a multiple choice question with fewer than two options;
- a rating question with no rating scale.

Once released, the structure is frozen: sections and questions can no longer be added, removed
or restructured, and the form says so in a banner. Answers were given under that wording, and
changing a question after the fact would leave an answer attached to a question nobody was
asked.

- :guilabel:`New Version` copies the questionnaire into a fresh draft with the version number
  raised by one. That is how you change a questionnaire between cycles.
- :guilabel:`Archive` takes a released questionnaire out of circulation without touching the
  reviews that used it.
- :guilabel:`Reset to Draft` is only possible while no review has used the questionnaire yet.
  Once one has, the answer is :guilabel:`New Version`.

.. _performance/config/which-questionnaire:

Which questionnaire a review uses
---------------------------------

When a review is opened, the questionnaire is resolved in this order and the first one found
wins:

#. the questionnaire named on the review itself;
#. :guilabel:`Review Questionnaire` on the employee record, in the
   :guilabel:`Performance Reviews` group of its :guilabel:`Settings` page;
#. :guilabel:`Default Review Questionnaire` on the department;
#. the questionnaire of the cycle the review belongs to;
#. :guilabel:`Default Review Questionnaire` in the company settings.

If none is set, or the one that is found has not been released, opening the review is refused
and says which. The rating scale is resolved the same way, from the questionnaire and then from
the company.

.. _performance/config/settings:

Company settings
================

Open :menuselection:`Settings --> Employees` and find the :guilabel:`Performance Reviews`
block.

+--------------------------------------------+--------------------------------------------------+
| Setting                                    | What it does                                     |
+============================================+==================================================+
| :guilabel:`Default Content`                | The questionnaire and rating scale used when a   |
|                                            | review names neither of its own.                 |
+--------------------------------------------+--------------------------------------------------+
| :guilabel:`Plan Reviews Automatically`     | Computes a next review date for every employee   |
|                                            | from the three intervals below it. It is also    |
|                                            | the master switch of the daily generator: while  |
|                                            | it is off, anniversary and probation cycles      |
|                                            | create no review at all, however they are        |
|                                            | configured.                                      |
+--------------------------------------------+--------------------------------------------------+
| :guilabel:`First Review After (months)`    | Months between a new employee's anchor date and  |
|                                            | their first review. Zero means the interval is   |
|                                            | not configured.                                  |
+--------------------------------------------+--------------------------------------------------+
| :guilabel:`Second Review After (months)`   | Months between the first review and the next     |
|                                            | one.                                             |
+--------------------------------------------+--------------------------------------------------+
| :guilabel:`Following Reviews Every         | Months between two reviews of an established     |
| (months)`                                  | employee.                                        |
+--------------------------------------------+--------------------------------------------------+
| :guilabel:`Reminder Lead Time`             | Days before a stage deadline the default         |
|                                            | reminder goes out.                               |
+--------------------------------------------+--------------------------------------------------+
| :guilabel:`Minimum Answers Before          | The anonymity threshold: how many submitted      |
| Aggregation`                               | answers a rater group must reach before its      |
|                                            | pooled result is shown at all. Default 5, and it |
|                                            | cannot be set below 5.                           |
+--------------------------------------------+--------------------------------------------------+
| :guilabel:`Review Retention (months)`      | How long a completed review is kept before the   |
|                                            | system proposes it for purge. Default 36.        |
+--------------------------------------------+--------------------------------------------------+

.. important::
   No review cadence is shipped. All three intervals start at zero, which states plainly that
   the interval is *not configured* rather than pretending a default is a policy. How often
   your company reviews its people is a decision for your company.

.. _performance/config/reminders:

Reminder templates
==================

:menuselection:`Performance --> Configuration --> Reminder Templates` lists the mail templates
written on the review. They are ordinary Odoo mail templates, so you can reword them in your
own voice and your own language. Five are shipped:

- *Review: Opened*
- *Review: Self-Assessment Reminder*
- *Review: Manager Reminder*
- *Review: Shared with the Employee*
- *Review: Sign-off Requested*

Which template goes out, to whom and when is decided by the reminders you attach to a cycle
stage — see :doc:`review_cycles`.

.. seealso::
   - :doc:`review_cycles` — stages, deadlines and the reminder schedule
   - :doc:`confidentiality` — what the sharing decision does and does not cover

============
Competencies
============

The **Review Competencies** module puts a competency framework over Odoo's skills. It answers
three questions a rating on its own cannot: *what does this job need*, *what does level 3
actually mean here*, and *where is the difference*.

It adds a :guilabel:`Competencies` page to the review, and two configuration lists under
:menuselection:`Performance --> Configuration`.

.. _performance/competencies/anchors:

Behavioural anchors
===================

A rater who reads *Expert (90%)* learns nothing. A rater who reads what somebody at that level
actually does in this job rates the same way as their colleague two aisles down.

Go to :menuselection:`Performance --> Configuration --> Behavioural Anchors` and write one
description per skill level:

- :guilabel:`Skill` and :guilabel:`Level` — what is being described.
- :guilabel:`Job Position` — the job this description was written for. Leave it empty for the
  description that applies to every job.
- :guilabel:`Description` — what somebody at this level does in practice. This is the text the
  rater reads while assessing the competency.

.. tip::
   Write anchors in observable behaviour, not adjectives. "Loads and unloads without a spotter,
   spots a damaged pallet before it moves, and trains a newcomer on the aisle rules" tells a
   rater what to look for. "Strong operational skills" does not.

A job-specific description takes precedence over the general one, which is why the same skill
can mean different things for a warehouse operator and for a buyer.

.. _performance/competencies/matrix:

The per-job requirement matrix
==============================

:menuselection:`Performance --> Configuration --> Job Competencies` states what each job needs:
a :guilabel:`Job Position`, a skill, the :guilabel:`Required Level` it needs, and a
:guilabel:`Weight` saying how much that competency counts against the others.

A requirement written down once is a requirement the review can measure against. Without it,
every review argues about the expectation before it can discuss the person. A job requires a
given skill at exactly one level; two contradictory rows are refused.

.. _performance/competencies/review:

Competencies in a review
========================

For a questionnaire to assess competencies, give it a section whose :guilabel:`Kind` is
*Competencies* — see :doc:`configuration`.

When the review is opened, one line is created for each of the employee's current skills
**plus** each skill their job requires that they do not have yet. The second half matters: a
competency the person is missing entirely is exactly the one worth discussing, and it would be
invisible if the lines came only from what they already hold.

Each line carries:

+------------------------------------------+----------------------------------------------------+
| Column                                   | What it is                                         |
+==========================================+====================================================+
| :guilabel:`Required Level`               | Copied from the job's requirement matrix when the  |
|                                          | review opened. Empty when the job asks nothing of  |
|                                          | this competency.                                   |
+------------------------------------------+----------------------------------------------------+
| :guilabel:`Previous Level`               | The level the employee held when the review        |
|                                          | opened. A snapshot; it is never recomputed         |
|                                          | afterwards.                                        |
+------------------------------------------+----------------------------------------------------+
| :guilabel:`Employee's View`              | What the employee thinks their level is.           |
+------------------------------------------+----------------------------------------------------+
| :guilabel:`Manager's View`               | What the reviewer thinks it is.                    |
+------------------------------------------+----------------------------------------------------+
| :guilabel:`Agreed Level`                 | What the two of them settled on. This is the       |
|                                          | **only** level ever written back onto the          |
|                                          | employee.                                          |
+------------------------------------------+----------------------------------------------------+
| :guilabel:`Gap`                          | The agreed level minus the required level, in      |
|                                          | percentage points of level progress. Negative      |
|                                          | means the job asks for more than what was agreed.  |
+------------------------------------------+----------------------------------------------------+
| :guilabel:`Certification`                | Tick when the level rests on a certificate rather  |
|                                          | than on an opinion.                                |
+------------------------------------------+----------------------------------------------------+
| :guilabel:`Valid From` /                 | When the agreed level holds from and until. For a  |
| :guilabel:`Valid To`                     | certificate, its expiry date.                      |
+------------------------------------------+----------------------------------------------------+
| :guilabel:`Note`                         | What was said about this competency, for the       |
|                                          | record and for the next review.                    |
+------------------------------------------+----------------------------------------------------+

The gap is shown with a colour on every list that displays it, and the standalone list totals
it. A search filter, :guilabel:`Below the Requirement`, brings up every line where the agreed
level falls short of what the job asks for.

.. note::
   A level that is not set counts as zero when the gap is computed. A person assessed against a
   requirement they have never been assessed on shows the full gap, which is the honest answer.

.. important::
   The :guilabel:`Competencies` page is visible from the :guilabel:`Reviewer` access level up.
   The employee does not read the competency lines on the review; what reaches them is the
   agreed level, once it has been written onto their own skills at closing. Discuss the
   assessment in the review conversation rather than expecting them to find it on the form.

.. _performance/competencies/writeback:

Writing agreed levels back to the employee
==========================================

When the review is closed, the levels agreed on this page are written back onto the employee's
skills. Three properties of that write-back are worth knowing:

- **It is a difference, not a replacement.** Only the competencies whose agreed level actually
  differs from what the employee currently holds are touched, and the existing skill row is
  updated in place. Nothing is deleted and recreated, so the employee's skill history and
  anything else pointing at those rows survive.
- **A skill the employee did not have yet is added**, at the agreed level.
- **A competency whose skill type has been archived is left alone and reported.** An archived
  skill type is out of the framework; rewriting a level on it would resurrect a classification
  somebody deliberately retired.

Only the :guilabel:`Agreed Level` is ever written back. The employee's own view and the
manager's view stay on the review as a record of the conversation, and neither one silently
becomes the truth.

.. important::
   Every change the write-back makes is logged on the **confidential assessment** of the
   review, never on the review itself, together with the old and new level of each skill and
   the name of the person who closed the review. A level a manager wrote down is a rating, and
   ratings do not go in a log the employee reads. See :doc:`confidentiality`.

.. _performance/competencies/reporting:

Competency evolution
====================

:menuselection:`Performance --> Reporting --> Competency Evolution` opens a pivot of the gap
across skill types, skills and cycles, with a bar chart alongside.

Once a few cycles have closed, that view stops being a report and becomes a training plan: a
skill with a persistent negative gap across a department is a course to book, not an opinion to
argue about.

Access to it follows the reviews it is built from: a reviewer sees the competency lines of the
people they review, and an officer sees them all. Employees have no access to this view.

.. seealso::
   - :doc:`configuration` — the *Competencies* section kind on a questionnaire
   - :doc:`conducting_a_review` — where the write-back sits in the closing sequence
   - :doc:`confidentiality` — why the write-back is logged where it is

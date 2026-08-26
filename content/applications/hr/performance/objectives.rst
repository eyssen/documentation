==========
Objectives
==========

An objective states what is to be achieved, how it will be measured and by when. Progress is
derived from the measurement rather than typed in as a feeling, and dated **check-ins** record
the story behind the number as it moves.

Objectives are useful on their own, and they are what a review has to talk about if the
conversation is going to start from facts. A questionnaire section of the kind *Objectives of
the period* renders exactly the objectives that were in scope when the review opened.

Where they live
===============

- :menuselection:`Performance --> Objectives --> My Objectives` and
  :menuselection:`Performance --> Objectives --> All Objectives`.
- The same lists also appear under :menuselection:`Employees --> Objectives`, together with
  :menuselection:`Employees --> Objectives --> Templates`.
- :menuselection:`Employees --> Configuration --> Objective Tags` for the tags.
- Each employee's form carries an :guilabel:`Objectives` smart button.

.. _performance/objectives/create:

Creating an objective
=====================

#. Create a record and give it a :guilabel:`Name` — a sentence stating the outcome, not the
   activity.
#. In :guilabel:`Scope`, set the :guilabel:`Kind`:

   +----------------------+---------------------------------------------------------------------+
   | Kind                 | Use it for                                                          |
   +======================+=====================================================================+
   | Objective            | The thing to be achieved.                                           |
   +----------------------+---------------------------------------------------------------------+
   | Key Result           | A measurable component of an objective. Align it under the          |
   |                      | objective it belongs to.                                            |
   +----------------------+---------------------------------------------------------------------+
   | Development Goal     | Something the person is working on about themselves rather than     |
   |                      | about the business. It behaves identically; the kind is there so    |
   |                      | you can report on the two separately.                               |
   +----------------------+---------------------------------------------------------------------+

   Then choose the :guilabel:`Employees` it belongs to. An objective may be assigned to more
   than one person, which is how a shared team objective works: it appears on each of their
   lists and there is only one of it.

   :guilabel:`Follow-up Owners` are the people who follow the objective up besides the ones it
   is assigned to.

#. In :guilabel:`Planning`, set the :guilabel:`Start Date`, the :guilabel:`Deadline` and, if
   you want a rhythm, a :guilabel:`Checkin Frequency`.
#. In :guilabel:`Measurement`, choose how the objective is measured — see below.
#. Use :guilabel:`Status` on the status bar (*On Track*, *At Risk*, *Off Track*, *Achieved*,
   *Missed*, *Cancelled*) and :guilabel:`Confidence` (*Low*, *Medium*, *High*) to say how it is
   going. Status is a judgement; progress is arithmetic. Both are useful, and they are
   deliberately not the same field.

.. _performance/objectives/metrics:

Measuring an objective
======================

:guilabel:`Metric` decides what you fill in and how :guilabel:`Progress (%)` is worked out:

+-------------------+--------------------------------+-------------------------------------------+
| Metric            | What you fill in               | How progress is worked out                |
+===================+================================+===========================================+
| Done / Not Done   | :guilabel:`Current Value`      | 100% as soon as the current value is      |
|                   |                                | anything other than zero, 0% otherwise.   |
+-------------------+--------------------------------+-------------------------------------------+
| Percentage        | :guilabel:`Current Value`      | The current value itself, kept between 0  |
|                   |                                | and 100.                                  |
+-------------------+--------------------------------+-------------------------------------------+
| Number            | :guilabel:`Start Value`,       | How far the current value has travelled   |
|                   | :guilabel:`Target Value`,      | from the start towards the target, as a   |
|                   | :guilabel:`Current Value`,     | percentage, kept between 0 and 100.       |
|                   | :guilabel:`Unit`               |                                           |
+-------------------+--------------------------------+-------------------------------------------+
| Amount            | The same, plus a               | As for *Number*.                          |
|                   | :guilabel:`Currency`           |                                           |
+-------------------+--------------------------------+-------------------------------------------+

:guilabel:`Direction` says which way is good. With *Increase*, progress rises as the current
value climbs from the start towards the target; with *Decrease*, it rises as the value falls.
That is what makes "cut the scrap rate from 4% to 1.5%" a first-class objective rather than
something you have to invert by hand.

.. note::
   For *Number* and *Amount*, the target has to differ from the start value. An objective whose
   target equals its start cannot be measured, and saving it is refused.

.. _performance/objectives/alignment:

Alignment, and why it is not roll-up
====================================

:guilabel:`Aligned To` points an objective at another one. That is a statement about *meaning*:
this objective exists in order to serve that one. It builds the alignment tree, it lets you
group and report along it, and it costs nothing — the parent's progress is unaffected.

:guilabel:`Roll Up Children` is a statement about *arithmetic*: when it is ticked, the
objective stops computing its own measurement and takes the weighted average of the objectives
aligned under it instead, using each child's :guilabel:`Weight`. An objective that rolls up with
no children sits at 0%.

.. important::
   Align freely; roll up sparingly. Alignment describes how the work fits together, which is
   almost always worth recording. Roll-up hands your number to somebody else's data quality: a
   parent that rolls up is only as honest as the children under it, and a child nobody checks
   in on drags a whole department's figure down without anybody noticing.

An objective cannot be aligned to one of the objectives aligned under it; a cycle is refused.

.. _performance/objectives/visibility:

Who can see an objective
========================

:guilabel:`Visibility` decides who reaches an objective:

+--------------------------------+--------------------------------------------------------------+
| Visibility                     | Who reaches the objective                                    |
+================================+==============================================================+
| Everybody                      | Every colleague in the company may read it.                  |
+--------------------------------+--------------------------------------------------------------+
| Employee and Management Line   | The employees it is assigned to, their line managers and its |
|                                | follow-up owners. This is the default.                       |
+--------------------------------+--------------------------------------------------------------+
| Employee Only                  | The employees it is assigned to. Neither the line manager    |
|                                | nor the follow-up owners reach it.                           |
+--------------------------------+--------------------------------------------------------------+

HR officers reach every objective whatever this says.

*Employee Only* is the setting to use for a development goal about a personal difficulty. Note
that it excludes the line manager, which is usually the point, and that HR still reaches it.

.. _performance/objectives/checkins:

Check-ins
=========

A check-in states where an objective stands on a given date, how confident its owner is, and
why. It is what turns a percentage into something the next review can actually talk about.

#. Open the objective and click :guilabel:`Check In`.
#. Enter the :guilabel:`Date`, the :guilabel:`New Value` the objective reached, and your
   :guilabel:`Confidence`.
#. Under :guilabel:`What happened`, write what moved, what is in the way, and what happens next.

Recording a check-in writes the new value and the confidence back onto the objective, stores a
snapshot of the resulting progress on the check-in itself, and logs the change. The history is
on the :guilabel:`Check-ins` page of the objective and behind its :guilabel:`Check-ins` smart
button.

Keeping the rhythm
------------------

:guilabel:`Checkin Frequency` (*No Reminder*, *Weekly*, *Every Two Weeks*, *Monthly*) sets
:guilabel:`Next Checkin Date` from the last check-in, or from the start date when there has not
been one yet.

There is no nagging job behind this. "Stale" is simply a filter: the
:guilabel:`Needs a Check-in` filter in the search view lists every objective whose next
check-in date has arrived. Combine it with :guilabel:`My Team` to prepare a one-to-one, or with
:guilabel:`Late` — deadline passed, not achieved and not cancelled — before a cycle launch.

.. tip::
   The reason this matters at review time: an objective with monthly check-ins produces twelve
   dated facts a year. An objective with none produces one argument in December.

.. _performance/objectives/templates:

Templates and bulk assignment
=============================

When the same objective goes to many people, write it once as a template.

#. Go to :menuselection:`Employees --> Objectives --> Templates` and create a record, or tick
   :guilabel:`Is Template` on an existing one.
#. A template carries **no** employees — that is enforced. It is the shared wording, not
   somebody's objective.
#. Build the tree under it if you want key results to come with it.
#. Use :guilabel:`Instantiate Objective Template`, choose the :guilabel:`Employees`, and
   optionally override :guilabel:`Start Date` and :guilabel:`Deadline` (leave them empty to keep
   the dates on the template).
#. :guilabel:`Include Aligned Objectives` also copies the objectives aligned under the template
   and aligns each copy under the copy of the template.
#. :guilabel:`Keep Link to Template` records on every new objective which template it came from,
   so the instances of one template can be reported on together.

Each selected employee gets **their own copy**. They can then be measured, checked in on and
closed independently, which is what you want: one shared record with fifteen owners cannot say
that eleven of them are on track.

.. note::
   A template is explicit, never inferred. An ordinary objective that happens to have lost its
   employees does not quietly become a template.

.. _performance/objectives/rights:

Who can do what
===============

- An employee creates and edits the objectives assigned to them, and records their own
  check-ins.
- A line manager, and anybody named as a follow-up owner, does the same for the objectives of
  the people they manage — except for the ones marked *Employee Only*.
- Nobody but HR can delete an objective. Set its status to *Cancelled* instead; the record of
  what was agreed and then dropped is usually worth more than a clean list.
- HR officers reach everything.

.. seealso::
   - :doc:`conducting_a_review` — how the period's objectives are pulled into a review
   - :doc:`configuration` — the *Objectives of the period* section kind

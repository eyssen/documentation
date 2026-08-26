=============
Review cycles
=============

A cycle is a wave of reviews: a stated population, dated stages, and reminders that chase
exactly the people who have not acted yet. It is how you run a review round without keeping a
spreadsheet of who has done what.

Cycles live under :menuselection:`Performance --> Cycles --> Review Cycles` and need the
:guilabel:`Officer` access level.

.. _performance/cycles/types:

Cycle types
===========

+-----------------+--------------------------------------+---------------------------------------+
| Type            | What it is                           | How reviews appear                    |
+=================+======================================+=======================================+
| Focal           | Everybody reviewed at the same time, | All at once, when you launch.         |
|                 | on the same period. The ordinary     |                                       |
|                 | annual or half-yearly wave.          |                                       |
+-----------------+--------------------------------------+---------------------------------------+
| Anniversary     | Each employee reviewed on their own  | A daily job creates each review as it |
|                 | rhythm, counted from their anchor    | falls due.                            |
|                 | date.                                |                                       |
+-----------------+--------------------------------------+---------------------------------------+
| Probation       | The trial period. Counted from the   | A daily job, working backwards from   |
|                 | contract rather than from an         | the end of the trial period. Needs    |
|                 | anniversary.                         | the Hungarian pack — see              |
|                 |                                      | :doc:`probation_hu`.                  |
+-----------------+--------------------------------------+---------------------------------------+
| Continuous      | A standing cycle for lightweight,    | All at once, when you launch.         |
|                 | recurring check-in conversations.    |                                       |
+-----------------+--------------------------------------+---------------------------------------+
| Ad hoc          | A one-off wave outside any rhythm: a | All at once, when you launch.         |
|                 | reorganisation, a new manager, a     |                                       |
|                 | pilot.                               |                                       |
+-----------------+--------------------------------------+---------------------------------------+

.. note::
   *Anniversary* and *Probation* create their reviews through a daily scheduled job, which is
   governed by a master switch: while :guilabel:`Plan Reviews Automatically` is off in the
   company settings, those cycles create nothing at all, however they are configured. See
   :doc:`configuration`.

.. _performance/cycles/create:

Setting a cycle up
==================

#. Create a cycle and give it a :guilabel:`Name` that a manager will recognise in a reminder
   mail — *2026 H1 review*, not *Cycle 4*.
#. In :guilabel:`Scope`, set the :guilabel:`Type`, the :guilabel:`Period From` and
   :guilabel:`Period To` — the period under review, not the period the reviews are run in — and
   the :guilabel:`Company`.
#. In :guilabel:`Content`, choose the :guilabel:`Questionnaire` (only released ones are
   offered) and the :guilabel:`Rating Scale`, then decide:

   - :guilabel:`Release Mode` — *The manager shares the review* lets each reviewer release to
     their own employee. *HR releases, then the manager shares* holds every review until an
     officer acts, which is what you want the first time you run a cycle, or whenever ratings
     have to be calibrated across departments before anybody sees one.
   - :guilabel:`Signoff Required` — whether a review has to be acknowledged or commented on by
     the employee before it can be closed. On by default.

#. In :guilabel:`Population`, write the :guilabel:`Population Filter` and, if relevant, a
   :guilabel:`Min Tenure Days` — employees whose anchor date is more recent than that are left
   out.
#. In :guilabel:`Rules`, set the :guilabel:`Anonymity Threshold` and the
   :guilabel:`Retention Months` for this cycle. Both fall back to the company settings.
#. Build the :guilabel:`Stages` — see below.

.. _performance/cycles/population:

The population, and what the launch tells you first
===================================================

:guilabel:`Population Filter` states who is in scope, as a filter on employees. It is resolved
**once**, at launch, and the resulting list of employees is then stamped onto the cycle. Every
review the cycle ever creates comes from that stamped list.

That is deliberate. A filter that is re-evaluated each time would quietly change the population
of a running cycle every time somebody changes department, and no two runs would agree on who
was supposed to be reviewed.

Before anything is created, the launch shows you exactly what it is about to do, in four
groups:

+------------------------------------------+----------------------------------------------------+
| The launch reports                       | What it means                                      |
+==========================================+====================================================+
| :guilabel:`Reviews to Create`            | The employees who will get a review. This is the   |
|                                          | number that matters.                               |
+------------------------------------------+----------------------------------------------------+
| :guilabel:`Already Have a Review`        | They are in scope but already have a review in     |
|                                          | this cycle. Launching again never creates a second |
|                                          | one for them.                                      |
+------------------------------------------+----------------------------------------------------+
| :guilabel:`Skipped, No Manager`          | They have no manager on their employee record, so  |
|                                          | nobody could conduct their review. Set a manager   |
|                                          | and launch again, or accept that they stay out.    |
+------------------------------------------+----------------------------------------------------+
| :guilabel:`Skipped, Minimum Tenure Not   | They have not served the minimum tenure this cycle |
| Reached`                                 | asks for, counted from their review plan anchor    |
|                                          | date.                                              |
+------------------------------------------+----------------------------------------------------+

Read those four numbers before you confirm. The overwhelming majority of "the cycle went wrong"
situations are visible here — a filter that caught a whole company instead of a department, or
forty people with no manager set.

.. important::
   A launch is idempotent. An employee who already has a review in this cycle never gets a
   second one, so a launch that was interrupted can simply be run again.

If the filter resolves to nobody who can be reviewed, the launch is refused and says so, rather
than creating an empty running cycle that quietly does nothing for three weeks.

.. _performance/cycles/stages:

Stages and deadlines
====================

A stage is a dated milestone of the round. Each one has a :guilabel:`Code` that says which part
of the work it is about, a :guilabel:`Name` in your own words, and a :guilabel:`Deadline`.

+------------------------+----------------------------------------------------------------------+
| Stage code             | The work it stands for                                               |
+========================+======================================================================+
| Nomination             | The employee proposes their raters (multi-rater rounds only).        |
+------------------------+----------------------------------------------------------------------+
| Self-assessment        | The employee has submitted their own part.                           |
+------------------------+----------------------------------------------------------------------+
| Manager assessment     | The reviewer has submitted theirs, with a proposed rating.           |
+------------------------+----------------------------------------------------------------------+
| Calibration            | A final rating has been set on the confidential assessment.          |
+------------------------+----------------------------------------------------------------------+
| Release                | The review has been shared with the employee.                        |
+------------------------+----------------------------------------------------------------------+
| Sign-off               | The employee has acknowledged the review or commented on it.         |
+------------------------+----------------------------------------------------------------------+

:guilabel:`Blocks Next` makes the stage a gate: while it is ticked and the work of that stage
is not in for a given review, the work of a later stage on that review is refused. Use it to
stop a manager writing their assessment before the employee's self-assessment is in, when that
is the order your process actually requires.

.. tip::
   Set the deadlines with the conversation in mind, not the paperwork. The sign-off deadline
   should leave room for the meeting to have happened.

.. _performance/cycles/reminders:

Reminders and escalation
========================

Each stage carries its own reminders, on the :guilabel:`Reminders` page of the stage.

+----------------------------+------------------------------------------------------------------+
| Field                      | What it does                                                     |
+============================+==================================================================+
| :guilabel:`Offset Days`    | When to send, relative to the stage deadline. Negative is        |
|                            | *before* the deadline: -3 means three days early, 0 means on the |
|                            | day, 2 means two days late.                                      |
+----------------------------+------------------------------------------------------------------+
| :guilabel:`Audience`       | *Whoever has not answered* chases exactly the people who still   |
|                            | owe something. *The managers* and *HR* go to the reviewers and   |
|                            | to the officers instead.                                         |
+----------------------------+------------------------------------------------------------------+
| :guilabel:`Mail Template`  | Which of the reminder templates to send. See                     |
|                            | :doc:`configuration`.                                            |
+----------------------------+------------------------------------------------------------------+
| :guilabel:`Escalate`       | *Nobody*, *The manager* or *HR* — who also hears about it.       |
+----------------------------+------------------------------------------------------------------+
| :guilabel:`Active`         | Untick to switch a reminder off without deleting it and losing   |
|                            | its history.                                                     |
+----------------------------+------------------------------------------------------------------+

A daily job sends every reminder whose stage deadline plus offset falls on today, working out
the audience per review. Two reminders on one stage — say -5 and +1 — give you an early nudge
and a chase, with different wording and different escalation.

.. note::
   Every reminder mail is written into a log in the same transaction as the mail itself, which
   is what makes the daily job safe to run again: a reminder already logged is never sent
   twice, even if the job runs several times in a day. The log is on the
   :guilabel:`Sent Reminders` page of each reminder, so you can prove what went to whom.

.. _performance/cycles/launch:

Launching
=========

#. Open the cycle and check it is in :guilabel:`Draft`.
#. Click :guilabel:`Launch`. The preview described above appears; read it.
#. Confirm.

The cycle moves to :guilabel:`Running`, the launch date is stamped, the resolved population and
the filter that produced it are written into the cycle's log, and one draft review is created
per employee.

Reviews are created as drafts, and a draft review is not yet chasing anybody. Opening a review
is what snapshots the reviewers, the department, the job, the questionnaire and the objectives
of the period, creates the questions, and sends the opening mail — see
:doc:`conducting_a_review`. Select the drafts in the review list and use
:guilabel:`Open the Reviews` to open a whole wave at once; whatever could not be opened is
reported by employee name and reason rather than silently skipped.

What can no longer change
-------------------------

Once a cycle has been launched, its questionnaire, rating scale, period and population filter
are frozen. Those are the things every review in the wave was built on, and changing them
half-way through would leave two halves of one cycle that cannot be compared.

A launched cycle can no longer go back to draft, and a cycle that owns reviews cannot be
deleted. Cancel it instead.

.. _performance/cycles/track:

Tracking a cycle
================

The cycle form carries a :guilabel:`Reviews` smart button and a :guilabel:`Completed` one, a
completion percentage on the list view, and a :guilabel:`Reviews` page listing every review
with its employee, reviewers, due date, status and sign-off state.

For the wider picture, :menuselection:`Performance --> Cycles --> Cycle Dashboard` opens the
completion analysis grouped by cycle and status. See :doc:`reporting`.

.. _performance/cycles/close:

Closing a cycle
===============

Click :guilabel:`Close` when the wave is finished. The closure is refused while any review is
still open, and the message says how many.

That refusal is on purpose: a cycle closed over twelve unfinished reviews is twelve people who
were told they would have a review and did not get one. Finish them, or cancel them one by one
so that the decision is recorded per person.

If you genuinely have to close over open reviews — a reorganisation made them moot — a
:guilabel:`Administrator` can force the closure, and is required to state a reason, which is
logged.

:guilabel:`Cancel` stops a draft or running cycle. :guilabel:`Reset to Draft` puts a cancelled
cycle back, but only if it never produced a review.

.. _performance/cycles/one-off:

Reviews outside a cycle
=======================

Not every review belongs to a wave. A reviewer or an officer can ask for one directly, at
:menuselection:`Performance --> Reviews --> Request a Review` or from the employee list:

- :guilabel:`Employees` — who is to be reviewed. A manager may only ask for the people who
  report to them; an officer, for anybody in their companies.
- :guilabel:`Questionnaire` and :guilabel:`Rating Scale` — leave empty to fall back to the
  employee's, the department's and then the company's.
- :guilabel:`Due Date` — written on the review and on every participant's to-do.
- :guilabel:`Additional Reviewers` — the line manager is always a reviewer; anybody listed here
  is added. A non-officer may only add somebody who already manages the employee.
- :guilabel:`Message` — posted on each review so that everybody involved knows why it was asked
  for. **The employee reads it too.**

The wizard refuses an employee with no manager, and refuses more than a hundred employees at a
time — a request for two hundred people is a cycle, not an ad-hoc request.

.. _performance/cycles/reassign:

Changing the reviewer
=====================

When a manager leaves half-way through a wave, an officer uses :guilabel:`Reassign the Reviews`.
The new reviewer replaces the reviewer of record on every selected review; an assessment that
has already been submitted stays attributed to whoever wrote it, and everything still pending
moves. A :guilabel:`Reason` is required, and is written to the confidential log of each review
together with the name of the reviewer being replaced.

Reviews that are already signed off and locked are refused by name: unlock them first, with a
reason, if the reviewer really has to change on a finished review.

.. seealso::
   - :doc:`conducting_a_review` — what happens to a review once it is opened
   - :doc:`multi_rater` — nomination stages and why an anonymous round is checked at launch
   - :doc:`reporting` — completion tracking across a cycle

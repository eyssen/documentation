=========
Reporting
=========

Everything in this section reports on records the reader is already allowed to read. There is
no reporting view that widens access: a reviewer's pivot table covers their own team, an
officer's covers their companies, and an employee has no reporting menu at all.

The reporting menu sits at :menuselection:`Performance --> Reporting` and is visible from the
:guilabel:`Reviewer` access level up.

.. _performance/reporting/cycle:

The cycle dashboard
===================

:menuselection:`Performance --> Cycles --> Cycle Dashboard` opens a pivot and graph of reviews
grouped by cycle and by status. It answers the question a cycle owner asks every morning: where
is this wave stuck, and with whom.

Group it by :guilabel:`Reviewer` to find the manager with nine unstarted assessments, or by
:guilabel:`Department` to see whether a whole area is behind.

Each cycle also reports on itself: :guilabel:`Reviews` and :guilabel:`Completed` smart buttons,
a completion percentage in the cycle list, and a :guilabel:`Reviews` page listing every review
with its employee, reviewers, due date, status and sign-off state.

.. _performance/reporting/completion:

Tracking completion
===================

The review list itself is the tracking tool. The search view carries the filters that matter:

+------------------------------------+----------------------------------------------------------+
| Filter                             | What it brings up                                        |
+====================================+==========================================================+
| :guilabel:`To Do by Me`            | Reviews waiting for something from you.                  |
+------------------------------------+----------------------------------------------------------+
| :guilabel:`Open`                   | Everything not yet closed or cancelled.                  |
+------------------------------------+----------------------------------------------------------+
| :guilabel:`Late`                   | Past the due date and not finished.                      |
+------------------------------------+----------------------------------------------------------+
| :guilabel:`Waiting for Sign-off`   | Shared with the employee, still unsigned. The usual      |
|                                    | bottleneck of a cycle.                                   |
+------------------------------------+----------------------------------------------------------+
| :guilabel:`Disagreed`              | Signed off with a written disagreement. Read these; they |
|                                    | are the most useful feedback the process produces about  |
|                                    | itself.                                                  |
+------------------------------------+----------------------------------------------------------+
| :guilabel:`Past its Retention      | Candidates for the purge.                                |
| Date`                              |                                                          |
+------------------------------------+----------------------------------------------------------+

Group by :guilabel:`Cycle`, :guilabel:`Reviewer`, :guilabel:`Department`, :guilabel:`Status`,
:guilabel:`Sign-off` or :guilabel:`Due Date`. The Kanban view grouped by status gives the same
picture as a board, and the calendar on the due date shows the shape of the coming fortnight.

.. tip::
   :guilabel:`Waiting for Sign-off` combined with a group by reviewer is usually the most useful
   single view during a cycle. It separates "the manager has not written it" from "the employee
   has not read it", which need completely different chasing.

.. _performance/reporting/ratings:

Scores and rating analysis
==========================

:menuselection:`Performance --> Reporting --> Ratings` opens the confidential assessments as a
list, graph and pivot: the proposed rating, the final rating, the self, manager and composite
scores, the potential and the flight risk.

Use it for the questions a single review cannot answer:

- **Distribution.** How many people ended at each level, per department and per reviewer. Set
  a :guilabel:`Target Share (%)` on your scale levels and you have something to compare against
  — advisory guidance, never enforced.
- **Reviewer effect.** Two managers of comparable teams whose average ratings differ by a whole
  level are worth a conversation before the next calibration round, not after it.
- **Self versus manager.** A large systematic gap between the self-assessment score and the
  manager score, in either direction, usually says something about how expectations are being
  communicated rather than about the people.
- **Calibration.** The filter :guilabel:`Calibrated` shows where a final rating was moved away
  from what the reviewer proposed; each of those carries the written reason.

.. important::
   This is the confidential side of the review. A reviewer sees only the assessments of the
   people they review; an officer sees their companies; the employee under review has no access
   to this data at all, here or anywhere else. See :doc:`confidentiality`.

.. _performance/reporting/development:

Development plans
=================

:menuselection:`Performance --> Reporting --> Development Plans` lists every development action
across every review, opening on the ones still open.

The two filters that earn their keep are :guilabel:`Late` — past its deadline and still planned
or in progress — and :guilabel:`Carried Over`, which shows the actions that were agreed in an
earlier review and are still not done. A list of actions carried over twice is the most honest
measure of whether your review process changes anything.

Group by :guilabel:`Type` to see what your company actually commits to: if every plan in the
company is *Training*, either you have solved coaching and stretch assignments or nobody is
offering them.

.. _performance/reporting/other:

The rest
========

- **Competency evolution** — :menuselection:`Performance --> Reporting --> Competency Evolution`,
  a pivot of the gap by skill type, skill and cycle. See :doc:`competencies`.
- **Objectives** — the objective list has its own graph, pivot and calendar views, with progress
  as the measure and status, department and tag as the axes. See :doc:`objectives`.
- **Sent reminders** — every reminder mail is logged with its recipient and date, on the
  reminder that sent it. Useful when somebody says they were never told.
- **Retention** — :menuselection:`Performance --> Configuration --> Retention and Purge` lists
  the reviews that have reached their retention date. See :doc:`confidentiality`.

.. _performance/reporting/access:

Who may see which report
========================

+------------------------------------+------------------------+------------------+----------------+
| View                               | Employee               | Reviewer         | HR officer     |
+====================================+========================+==================+================+
| Completion analysis on reviews     | Own reviews only       | Their own team   | Everything     |
+------------------------------------+------------------------+------------------+----------------+
| Ratings and scores                 | No                     | Their own team   | Everything     |
+------------------------------------+------------------------+------------------+----------------+
| Development plans                  | Own actions, and the   | Their own team   | Everything     |
|                                    | ones they own          |                  |                |
+------------------------------------+------------------------+------------------+----------------+
| Competency evolution               | No                     | Their own team   | Everything     |
+------------------------------------+------------------------+------------------+----------------+
| Objectives                         | Own, plus what         | Their team       | Everything     |
|                                    | visibility allows      |                  |                |
+------------------------------------+------------------------+------------------+----------------+

.. seealso::
   - :doc:`confidentiality` — the access rules every one of these views inherits
   - :doc:`review_cycles` — running a cycle from the numbers above

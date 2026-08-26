===========
Performance
===========

The **Performance** application runs the conversation a company has with its people about
how work is going: what was agreed, what happened, what it was worth and what comes next.
It covers the whole cycle — objectives and their check-ins, a structured questionnaire, a
self-assessment and a manager assessment, an optional multi-rater round, a rating that is
calibrated before it is released, the employee's own written reply, a development plan that
outlives the review, and a retention period after which the review is proposed for deletion.

It is built for a small or mid-sized company: one HR officer, line managers who conduct two
or three reviews a year each, and employees who should be able to read their own review
without asking anybody's permission — and should never be able to read anybody else's.

.. important::
   A performance review is one of the most sensitive records a company keeps about a person.
   The confidentiality architecture is not an option you switch on: it is how the data is
   laid out. Read :doc:`performance/confidentiality` before you launch a real cycle, and
   before you grant anybody the :guilabel:`Officer` access level.

The five modules
================

The application is a family of five modules. Installing **Performance Reviews** installs the
first two; the other three are optional and can be added at any time.

+----------------------------+--------------------------------------------------------------------+
| Module                     | What it adds                                                       |
+============================+====================================================================+
| **Performance Reviews**    | The application itself: rating scales, questionnaires, review      |
| (``hr_review``)            | cycles, the review packet, the confidential assessment, sign-off,  |
|                            | reminders and retention.                                           |
+----------------------------+--------------------------------------------------------------------+
| **Objectives**             | Objectives, key results and development goals with a real          |
| (``hr_objective``)         | measurement and dated check-ins. Installed with the application,   |
|                            | and usable on its own.                                             |
+----------------------------+--------------------------------------------------------------------+
| **Multi-rater Reviews      | Peer, direct report, skip-level and outside raters, nomination and |
| (360)**                    | approval, the anonymity threshold and the portal form outside      |
| (``hr_review_360``)        | raters answer on.                                                  |
+----------------------------+--------------------------------------------------------------------+
| **Review Competencies**    | A competency framework over Odoo's skills: behavioural anchors, a  |
| (``hr_review_competency``) | per-job requirement matrix, gap analysis and a non-destructive     |
|                            | write-back.                                                        |
+----------------------------+--------------------------------------------------------------------+
| **Hungary - Performance    | Trial-period (*próbaidő*) reviews counted from the contract, the   |
| Reviews**                  | probation decision record and its printed Hungarian document, and  |
| (``l10n_hu_hr_review``)    | Hungarian master data.                                             |
+----------------------------+--------------------------------------------------------------------+

.. note::
   Technical names, for whoever installs them: ``hr_review`` (the application, listed as
   *Performance Reviews*), ``hr_objective``, ``hr_review_360``, ``hr_review_competency`` and
   ``l10n_hu_hr_review``. The application appears in the apps switcher as **Performance**.

Who does what
=============

Three access levels sit in the :guilabel:`Performance` category of a user's access rights,
each one implying the one above it. Being in a group says *what a person may do*; the record
rules decide *whose records they may do it to*.

+----------------------------+-------------------+------------------------------------------------+
| Access level               | Who it is for     | What it allows                                 |
+============================+===================+================================================+
| (none)                     | Every employee    | Read their own review, answer their own        |
|                            |                   | questions, acknowledge or comment on a review  |
|                            |                   | that has been shared with them, and run their  |
|                            |                   | own objectives.                                |
+----------------------------+-------------------+------------------------------------------------+
| :guilabel:`Reviewer`       | Line managers     | Everything above, plus conducting the reviews  |
|                            |                   | of the people who report to them: the manager  |
|                            |                   | assessment, the rating, the notes, the panel   |
|                            |                   | and the development plan of *their own*        |
|                            |                   | reviews only.                                  |
+----------------------------+-------------------+------------------------------------------------+
| :guilabel:`Officer`        | HR                | Runs and sees every review in the companies    |
|                            |                   | they are allowed to work in: cycles, launches, |
|                            |                   | reassignment, legal hold, unlocking and the    |
|                            |                   | purge.                                         |
+----------------------------+-------------------+------------------------------------------------+
| :guilabel:`Administrator`  | Whoever sets the  | Everything above, plus the configuration:      |
|                            | system up         | rating scales, questionnaires, reminder        |
|                            |                   | templates and retention.                       |
+----------------------------+-------------------+------------------------------------------------+

.. important::
   :guilabel:`Reviewer` is not a job title, it is an access level. A line manager who has it
   still only reaches the reviews of the people whose reviews name them as reviewer. Granting
   :guilabel:`Officer` to a line manager gives them every review in the company, including
   their own manager's — that is almost never what is wanted.

Setting it up the first time
============================

The order matters: a cycle cannot be launched on a questionnaire that has not been released,
and a questionnaire cannot be released without a rating scale.

#. **Install the application.** Go to :menuselection:`Apps`, search for *Performance Reviews*
   and install it. Add **Multi-rater Reviews (360)**, **Review Competencies** and, in Hungary,
   **Hungary - Performance Reviews** if you need them.
#. **Grant access rights.** In :menuselection:`Settings --> Users & Companies --> Users`, give
   yourself :guilabel:`Administrator` in the :guilabel:`Performance` category, give HR
   :guilabel:`Officer`, and give the line managers :guilabel:`Reviewer`. Everybody else needs
   nothing: a plain internal user already reaches their own review and their own objectives.
#. **Create a rating scale.** No scale is shipped on purpose — see
   :doc:`performance/configuration`. Either write your own at
   :menuselection:`Performance --> Configuration --> Rating Scales`, or let
   :menuselection:`Performance --> Configuration --> Starter Rating Scale` write a five-level
   one for you to rename and reword. The Hungarian pack ships a Hungarian scale with
   behavioural descriptions.
#. **Build a questionnaire** under :menuselection:`Performance --> Configuration -->
   Questionnaires`, then click :guilabel:`Release`. A released questionnaire is frozen; that
   is what keeps the answers stored under it meaningful.
#. **Set the company options.** In :menuselection:`Settings --> Employees`, in the
   :guilabel:`Performance Reviews` block, set the default questionnaire and scale, the
   retention period, and — if you want them — the automatic review intervals.
#. **Check that the employees have a manager.** A review needs somebody to conduct it. An
   employee with no manager on their employee record is reported and skipped when a cycle is
   launched, never silently included.
#. **Launch a first cycle** from :menuselection:`Performance --> Cycles --> Review Cycles`.
   The launch shows you exactly who is in scope and who is being skipped, before anything is
   created.

.. tip::
   Run the first cycle on one department. The launch preview, the reminder schedule and the
   sign-off step are all easier to judge on twenty reviews than on two hundred.

What the application deliberately refuses to do
===============================================

Several of these will look like missing features until you need them. They are decisions, and
each one is explained where it applies.

- **A rating scale that is already in use cannot be re-valued.** Changing what "3" is worth
  would silently rewrite every rating ever given on it. Create a new version instead.
- **A released questionnaire cannot be restructured.** Answers were given under its wording.
- **A multi-rater round that cannot keep its anonymity promise is refused at launch**, not at
  release time — by release time people have already answered under the promise. See
  :doc:`performance/multi_rater`.
- **Retention is proposed, never executed automatically.** There is no cron that deletes
  reviews. A person runs a dry run, reads what it lists, and confirms. See
  :doc:`performance/confidentiality`.
- **A review under legal hold is never purged and never deleted**, whatever its retention date
  says.
- **A trial-period termination records the fact, not a justification.** See
  :doc:`performance/probation_hu`.
- **The employee's disagreement is recorded in their own words.** Sign-off is not a checkbox
  that says the employee agrees; it is a record that they were shown the review, with room for
  what they think of it.

.. toctree::
   :titlesonly:

   performance/confidentiality
   performance/configuration
   performance/objectives
   performance/review_cycles
   performance/conducting_a_review
   performance/multi_rater
   performance/competencies
   performance/probation_hu
   performance/reporting

.. seealso::
   - :doc:`employees` — employee records, managers and departments, which every review reads
   - :doc:`../general/users/access_rights` — how Odoo groups and record rules work

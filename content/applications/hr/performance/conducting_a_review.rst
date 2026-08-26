===================
Conducting a review
===================

This page follows one review from the moment it is created to the moment it is closed, from
both sides: the reviewer's and the employee's.

Reviewers reach their reviews at :menuselection:`Performance --> Reviews --> My Team`;
employees reach their own at :menuselection:`Performance --> Reviews --> My Reviews`; HR sees
everything at :menuselection:`Performance --> Reviews --> All Reviews`.

.. _performance/review/lifecycle:

The lifecycle
=============

+------------------------+----------------------+------------------------------------------------+
| Status                 | Who acts             | What has to happen to move on                  |
+========================+======================+================================================+
| Draft                  | The reviewer or HR   | The review is created but not yet live. Nobody |
|                        |                      | has been asked for anything.                   |
+------------------------+----------------------+------------------------------------------------+
| Self-Assessment        | The employee         | Answer every required question addressed to    |
|                        |                      | the employee and submit.                       |
+------------------------+----------------------+------------------------------------------------+
| Manager Assessment     | The reviewer         | Answer every required question addressed to    |
|                        |                      | the manager, set the proposed rating, and      |
|                        |                      | submit.                                        |
+------------------------+----------------------+------------------------------------------------+
| Shared                 | The employee         | The review has been released. The employee     |
|                        |                      | reads it and signs it off, either              |
|                        |                      | acknowledging it or recording a written        |
|                        |                      | disagreement.                                  |
+------------------------+----------------------+------------------------------------------------+
| Done                   | —                    | Closed and locked. The retention date is       |
|                        |                      | stamped.                                       |
+------------------------+----------------------+------------------------------------------------+
| Cancelled              | HR                   | The review will not happen. Its to-dos are     |
|                        |                      | closed and its meeting removed.                |
+------------------------+----------------------+------------------------------------------------+

Each step is a button on the review, not a field you edit. A review's status cannot be changed
by typing over it, dragging a Kanban card or importing a file — only by the buttons, which
check that the person pressing them is entitled to and that the work of the step is actually
done.

.. _performance/review/form:

What is on a review
===================

+----------------------------+----------------------------------------------+--------------------+
| Page                       | What is on it                                | Who sees it        |
+============================+==============================================+====================+
| :guilabel:`Previous Plan`  | What was agreed last time and what came of   | Everyone           |
|                            | it. Shown first, when a previous review      |                    |
|                            | exists.                                      |                    |
+----------------------------+----------------------------------------------+--------------------+
| :guilabel:`Questionnaire`  | The answers of this review, filtered to what | Everyone           |
|                            | the reader may see.                          |                    |
+----------------------------+----------------------------------------------+--------------------+
| :guilabel:`Objectives`     | The objectives that were in scope for the    | Everyone           |
|                            | period.                                      |                    |
+----------------------------+----------------------------------------------+--------------------+
| :guilabel:`Evidence`       | What was actually recorded about the         | Everyone           |
|                            | employee during the period.                  |                    |
+----------------------------+----------------------------------------------+--------------------+
| :guilabel:`Development     | What was agreed for next time, including     | Everyone           |
| Plan`                      | carried-over actions.                        |                    |
+----------------------------+----------------------------------------------+--------------------+
| :guilabel:`Participants`   | Who owes an answer, and where each of them   | Reviewer, HR       |
|                            | stands.                                      |                    |
+----------------------------+----------------------------------------------+--------------------+
| :guilabel:`Notes`          | The reviewer's own working notes.            | Their author, and  |
|                            |                                              | HR through         |
|                            |                                              | break-glass        |
+----------------------------+----------------------------------------------+--------------------+
| :guilabel:`Rating`         | The confidential assessment: proposal, final | Reviewer, HR       |
|                            | rating, calibration, scores.                 |                    |
+----------------------------+----------------------------------------------+--------------------+
| :guilabel:`Sign-off`       | The sign-off state, the timestamps and the   | Everyone           |
|                            | employee's own comment.                      |                    |
+----------------------------+----------------------------------------------+--------------------+

A row of smart buttons sits above them: :guilabel:`My Answers` opens the part of the
questionnaire you personally have to fill in, :guilabel:`Objectives` the employee's objectives,
:guilabel:`Development Actions` the plan, :guilabel:`Meeting` the review conversation once one
has been scheduled, and :guilabel:`Review History` this employee's other reviews.

.. _performance/review/open:

Opening the review
==================

Click :guilabel:`Open the Review`. This is the moment the review becomes real, and a great deal
is fixed in place:

- the **reviewers** are snapshotted from the employee's management line, together with the
  **department** and the **job position**. If the employee moves department in March, the
  review opened in February still says where they were and who reviewed them.
- the **questionnaire version** and the **rating scale** are stamped, so that a new version
  released next week does not rewrite a review already in progress;
- the **objectives** of the period are pulled in — the ones whose dates overlap the review
  period;
- the questions each person has to answer are created;
- one to-do is placed on **each participant's** own record — never on the review, so that the
  employee cannot see who else was asked;
- the unfinished development actions of the previous review are copied in, marked as carried
  over;
- the opening mail goes out.

Opening is refused, with a message saying which, when the employee has no manager, when no
questionnaire can be resolved, when the questionnaire found has not been released, or when no
rating scale can be resolved.

.. tip::
   After launching a cycle you have a list of drafts. Select them all in the list view and click
   :guilabel:`Open the Reviews`. Whatever could not be opened is reported by employee name and
   reason, and the rest are opened.

.. _performance/review/self:

The self-assessment
===================

The employee gets a mail and a to-do. On their review, they click :guilabel:`Fill in my part`
(or the :guilabel:`My Answers` smart button) and answer the questions addressed to them.
Answers save as they are entered; nothing is submitted until they say so.

When they are ready, they click :guilabel:`Submit my Self-Assessment`. If a required question
is still unanswered, the submission is refused and the missing questions are named.

Submitting freezes those answers. From then on the employee can still read them but no longer
change them; only an HR officer can correct a submitted answer, and it is recorded that they
did.

.. note::
   :guilabel:`Self-Assessment Progress` on the review shows how much of the required part is
   answered, so a reviewer can see whether it is worth chasing without reading anything.

.. _performance/review/manager:

The manager assessment
======================

The reviewer answers their own part the same way, and additionally sets the **proposed rating**
on the :guilabel:`Rating` page, on the confidential assessment. :guilabel:`Submit the Manager
Assessment` is refused without it: a review with no rating is an opinion that was never
committed to.

Preparing well
--------------

Four things on the form exist to make the assessment about facts rather than about the last
three weeks:

- **The objectives of the period**, with every dated check-in behind them.
- **The previous plan**, on the first page: what was agreed last time, and what came of it.
- **The reviewer's working notes**, on the :guilabel:`Notes` page — what you wrote down in
  March, when it happened. A note belongs to its author; another reviewer does not see it. Read
  :doc:`confidentiality` on what a note is and is not before you rely on that.
- **The evidence panel.** On the :guilabel:`Evidence` page, :guilabel:`Show the evidence of the
  period` gathers what was actually recorded about this employee between :guilabel:`From` and
  :guilabel:`To` from the modules that keep it — today, the check-ins on their objectives. Every
  entry is resolved with **your own** access rights, so the panel can never show a reviewer
  something they were not already entitled to read, and it will show an employee looking at
  their own review a shorter list than it shows their manager.

.. important::
   Calibration happens on the confidential assessment, not on the review. If the final rating
   ends up different from the one the reviewer proposed, both are kept and a written reason is
   required. Neither the proposal nor the reason is ever shown to the employee. See
   :doc:`confidentiality`.

.. _performance/review/conversation:

The review conversation
=======================

The conversation is the point of the exercise; the record is the residue.
:guilabel:`Schedule the Review Conversation` creates a calendar event attached to the review and
fills in :guilabel:`Review Meeting`, after which the :guilabel:`Meeting` smart button opens it.
The meeting belongs to the review: it is removed with it if the review is cancelled.

Hold the conversation around the release, not after it. An employee who reads their rating in
a system before anybody has spoken to them about it has already formed their view of the
process by the time the meeting starts.

.. _performance/review/share:

Sharing the review with the employee
====================================

:guilabel:`Share with the Employee` releases the review. It:

- makes the reviewer's answers visible to the employee — but only for the questions marked
  :guilabel:`Shared With Employee`, and never an answer given anonymously;
- copies the proposed rating into the final rating if no final rating has been set yet;
- moves the review to :guilabel:`Shared` and mails the employee;
- records on the confidential log who released it, with which final rating, and how many
  answers were made visible.

If the cycle's release mode is *HR releases, then the manager shares*, a reviewer pressing this
button is refused: an officer releases centrally. That is how you calibrate a whole cycle before
anybody sees a rating.

.. _performance/review/signoff:

Sign-off: acknowledged, or disagreed
====================================

Sign-off is **not** a statement that the employee agrees with the review. It is a record that
they were shown it, plus room for what they think of it. Both outcomes close the review equally.

- :guilabel:`I acknowledge this review` records that the employee has read and accepted it.
- :guilabel:`I disagree with this review` opens a short form that asks for their own words, and
  refuses to record an empty one. A recorded dissent with no words in it would be worth nothing
  to the employee later, which is exactly when it matters. They write what they disagree with
  under :guilabel:`My Comment` and click :guilabel:`Record my Comment`.

Either way the review is locked, the moment is timestamped, and the employee's own words are
stored on the review, shown on the :guilabel:`Sign-off` page and printed on **every** copy of
the review packet, including the reviewer's and HR's.

.. important::
   Only the employee under review can sign off, and only through those two acts. There is no
   field a manager or an officer can write to say that an employee acknowledged something.

If an employee is slow, the reviewer can ask again: a sign-off reminder mail goes to the
employee without disclosing anything new, since the review is already shared with them.

.. _performance/review/close:

Closing the review
==================

:guilabel:`Close the Review` finishes it. It is refused unless the review has been shared, and
— when the cycle requires sign-off — unless the employee has signed off. A final rating is
required.

Closing writes the employee's last review and, if automatic planning is on, their next review
date; closes the outstanding to-dos; runs the write-backs of the optional modules (competency
levels, for instance); stamps the **retention date**; and locks the review.

.. _performance/review/plan:

The development plan
====================

The development plan is what a review is actually for, and it is the part designed to outlive
the review that created it.

Add one line per action on the :guilabel:`Development Plan` page: a :guilabel:`Name`, a
:guilabel:`Type` (*Training*, *Mentoring*, *Coaching*, *Stretch Assignment*, *Rotation*,
*Certification*, *Reading*, *Other*), an :guilabel:`Owner`, a :guilabel:`Deadline`, optionally
a :guilabel:`Cost` and a link to an :guilabel:`Objective`. Under :guilabel:`What we agreed`,
write what will be done and what good looks like.

As the action progresses, keep :guilabel:`Status` up to date and fill in
:guilabel:`What came of it`.

Carry-forward
-------------

When the next review of the same employee is opened, every action still *Planned* or *In
Progress* is copied onto it and marked as carried over, together with the outcome recorded so
far. The next review's first page is therefore *Previous Plan*: what we agreed, and what
happened.

That is the mechanism that stops a development plan from being a promise made once a year and
never mentioned again. An action that has been carried forward twice is visible as such, which
is a conversation worth having.

.. _performance/review/print:

Printing a review
=================

:guilabel:`Print` produces the review packet: the employee, job, department, cycle and period;
the questionnaire with the answers; the released rating; the development plan; the sign-off
block with the employee's own comment; and the retention date in the footer.

The same template serves everybody. The employee's copy contains less than the reviewer's,
because the document only renders what its reader is entitled to see — the rating block, for
example, is only present for a reviewer or an officer. There is no separate "employee version"
that somebody could forget to keep in step.

.. _performance/review/correct:

Correcting a finished review
============================

A signed-off review is locked. That lock is real: it is refused through the interface, through
an import, and on the answers underneath it.

An HR officer can lift it with :guilabel:`Unlock` or :guilabel:`Reopen`, and either one asks
for a :guilabel:`Reason` before it will do anything. The reason goes on the confidential log
with their name.

- :guilabel:`Unlock` leaves the review closed but makes it writable again, for a correction.
- :guilabel:`Reopen` puts a closed review back into the shared state, where the employee is
  asked for their sign-off once more — the honest option whenever the correction changes
  something the employee was told.

Unlocking is refused once the review has reached its retention date.

Cancelling
----------

:guilabel:`Cancel` is for a review that will not happen. It closes the outstanding to-dos and
removes the review meeting. An officer can bring a cancelled review back to draft. A review
that has already started cannot be deleted — cancel it instead, so the record of what was
planned and dropped survives.

.. seealso::
   - :doc:`confidentiality` — what each party sees at every step above
   - :doc:`objectives` — the objectives and check-ins the assessment reads
   - :doc:`multi_rater` — adding peer, direct report and outside feedback to this flow
   - :doc:`competencies` — the competency page and the write-back that runs at closing

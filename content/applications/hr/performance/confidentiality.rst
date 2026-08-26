===============
Confidentiality
===============

A performance review contains an opinion about a person, written down and kept for years. Who
may read which part of it is not a preference to be configured later: it is the first thing to
get right, and the reason several parts of this application are laid out the way they are.

This page is written for the person who has to answer, in a works council meeting or to a data
protection authority, the question *"who can see this?"*.

.. _performance/confidentiality/matrix:

Who can see what
================

+-----------------------------------------+-----------------+------------------+-------------------+
| What                                    | Employee        | Their reviewer   | HR officer        |
+=========================================+=================+==================+===================+
| The review itself: period, dates,       | Read            | Read and write   | Everything        |
| status, who reviews them                |                 |                  |                   |
+-----------------------------------------+-----------------+------------------+-------------------+
| Their own answers to the questionnaire  | Read and write  | No               | Everything        |
+-----------------------------------------+-----------------+------------------+-------------------+
| The reviewer's answers, once the review | The shared      | Read and write   | Everything        |
| is shared                               | questions only  |                  |                   |
+-----------------------------------------+-----------------+------------------+-------------------+
| Answers given anonymously in a          | No              | No               | Pooled only       |
| multi-rater round                       |                 |                  |                   |
+-----------------------------------------+-----------------+------------------+-------------------+
| The rating, the calibration decision    | The released    | Their own        | Everything        |
| and the scores                          | rating only     | reviews          |                   |
+-----------------------------------------+-----------------+------------------+-------------------+
| The reviewer's private working notes    | No              | Their own only   | Break-glass,      |
|                                         |                 |                  | logged            |
+-----------------------------------------+-----------------+------------------+-------------------+
| Who was asked for feedback (the panel)  | No              | Named raters     | Everything        |
|                                         |                 | only             |                   |
+-----------------------------------------+-----------------+------------------+-------------------+
| The development plan                    | Read            | Read and write   | Everything        |
+-----------------------------------------+-----------------+------------------+-------------------+
| Their own written comment at sign-off   | Read and write, | Read             | Read              |
|                                         | once            |                  |                   |
+-----------------------------------------+-----------------+------------------+-------------------+

Two of those rows deserve more than a table cell.

The confidential assessment
---------------------------

The rating, the reviewer's proposal, the calibration decision, the composite scores, the
potential and flight-risk entries and the succession note do **not** live on the review. They
live on a separate record, reached from the :guilabel:`Rating` page of the review form, which
carries its own access rules — and none of those rules ever matches the employee under review.

That distinction matters more than it looks. If the rating were a hidden field on the review,
its confidentiality would rest on a screen setting, and an export, a filter, a grouping or a
report could still reach it. Because it is a separate record, an employee looking at their own
review does not have the field at all: not in the interface, not in an export, not in a
group-by.

.. important::
   The employee sees a rating exactly once: the **released** rating, on the review that has
   been shared with them, and only after somebody decided to share it. The rating the reviewer
   originally proposed, and the reason it was changed, are never shown to them.

.. note::
   The original proposal and the final rating are both kept, side by side, permanently. A
   calibration that moves a rating away from the proposal is refused unless the person who
   moves it writes down why. That is an audit trail, not a formality: it is what lets a rating
   be explained a year later.

What is written in the log of a review
--------------------------------------

The message log — the chatter — of a review is treated as a document the employee reads,
because they can. Every confidential entry (a rating being set, a calibration, the decision to
release, an unlock and its reason, a competency written back to the employee's skills) is
logged on the **confidential assessment** instead, where the employee has no access.

The same reasoning applies to to-dos. A scheduled activity is readable by anybody who can read
the document it hangs on, so a review activity is never placed on the review: each person who
owes something is chased on their own participation record. An employee therefore cannot work
out who else was asked for feedback by looking at the to-do list of their own review.

.. _performance/confidentiality/employee-sees:

What the employee can always see
================================

Whatever else is configured, an employee reaches, for their own review and without asking:

- the review record itself — the period, the questionnaire, the due date, the status and who
  their reviewer is;
- every question they were asked, and every answer they gave;
- once the review has been shared with them: the reviewer's answers to the questions marked
  :guilabel:`Shared With Employee` on the questionnaire, and the released rating;
- the development plan agreed with them, including the actions carried over from the previous
  review and what came of them;
- the printed review packet — the same document, produced from the same template, whoever
  prints it;
- their own comment at sign-off, in their own words.

And, deliberately, nothing else: not the panel, not another employee's review, not the
reviewer's working notes, not the calibration, and not an individual answer from an anonymous
round.

.. _performance/confidentiality/sar:

Answering a subject access request
==================================

There is no button labelled *subject access request*, and none is needed: the employee already
holds the readable part of their own file, and the confidential part is a short, well-defined
list an officer can produce by hand.

#. Ask the employee to print their own reviews from :menuselection:`Performance --> Reviews -->
   My Reviews`, using :guilabel:`Print`. That is the review packet: the questionnaire with the
   answers, the released rating, the development plan and the sign-off, with the retention date
   stated in the footer.
#. As an officer, add what the packet does not carry, if the request asks for it: the rating the
   reviewer proposed and the calibration reason, from the confidential assessment; the scores;
   and the potential, flight-risk and succession entries if they were used.
#. Add the reviewer's working notes about that employee, if any exist.

.. warning::
   A reviewer's working note is **not** secret from the employee it is about. It is not
   routinely shared, which is a different thing. Anybody writing notes should write them
   knowing that a subject access request, a labour dispute or a court can bring them out. The
   application does not pretend otherwise, and an HR policy should not either.

An officer who has to read another reviewer's notes does so through a break-glass action, which
records on the confidential log of the review that they did. Use it when you have a reason, and
expect the fact to be visible afterwards.

.. _performance/confidentiality/retention:

Retention and the purge
=======================

When a review is closed it is stamped with a retention date: the day it closed plus the
retention period of its cycle, or of the company when the cycle does not state one. The default
is 36 months, the Hungarian limitation period for labour claims; set it to whatever your own
legal advice says.

The retention date is a **proposal**. Nothing happens on that day. No scheduled job deletes
anything, ever.

Running a purge
---------------

#. Look at what is due first, at
   :menuselection:`Performance --> Configuration --> Reviews Past their Retention Date`.
#. Open :menuselection:`Performance --> Configuration --> Retention and Purge`, choose the
   :guilabel:`Companies` and the :guilabel:`Retention Reached On` date, and click
   :guilabel:`Dry Run`.
#. Read what the dry run reports on the :guilabel:`Dry Run` page: how many reviews would be
   anonymised per company, how many are refused because they are under legal hold, and the
   oldest and newest retention dates concerned. The :guilabel:`Reviews Concerned` and
   :guilabel:`Refused, Under Legal Hold` pages name them. Nothing has been touched at this
   point.
#. If you are satisfied, click :guilabel:`Anonymise the Listed Reviews` and confirm.

.. important::
   A purge **anonymises**; it does not delete. Each review keeps its row, its dates, the rating
   that was released and the sign-off, and is archived. What is removed is the free text and the
   identity of the raters: the employee's own comment, the text and the comment of every answer,
   the body of every working note, and the identity of every rater other than the employee
   themselves. With the multi-rater pack installed, the outside raters' names and addresses, who
   nominated and who approved each rater, and the fingerprint of every feedback link go with
   them.

   This is not reversible.

A single run touches at most 500 reviews. If more are due, the result says so and you run it
again.

.. note::
   A review is only anonymised while it is genuinely past its retention date. If a review was
   reopened, or its retention date changed, between the dry run and the execution, it is refused
   and named in the result rather than being purged on stale information.

Legal hold
----------

An officer can tick :guilabel:`Legal Hold` in the :guilabel:`Retention` group of the review
form. A review under legal hold:

- is refused by the purge, whatever its retention date says, and is named in the result so that
  you can see it was refused rather than missed;
- cannot be deleted at all.

Use it the moment a dispute, an inspection or a claim becomes foreseeable, and take it off when
the matter is closed. It is the one switch that overrides the retention schedule.

.. _performance/confidentiality/limits:

What this does not protect you from
===================================

Being clear about the boundary is part of being trustworthy about what is inside it.

- **An officer sees everything in their companies.** That is what the access level means. Grant
  it to as few people as the work allows, and review the list of holders periodically.
- **A database administrator sees everything.** No application rule constrains somebody with
  server or database access.
- **A printed packet leaves the system.** Once a review has been printed or exported, retention
  and legal hold no longer reach that copy.
- **Anonymity is a threshold, not a cryptographic guarantee.** It stops a small group being
  identified from counts and averages. It does not stop somebody being recognised by their
  writing style in a pooled comment — see :doc:`multi_rater`.
- **Notes are private, not privileged.** See the warning above.

.. seealso::
   - :doc:`multi_rater` — how the anonymity threshold works and what it refuses to do
   - :doc:`conducting_a_review` — sign-off, unlocking, and what each one records
   - :doc:`../../general/users/access_rights` — the Odoo access rights every rule above sits on

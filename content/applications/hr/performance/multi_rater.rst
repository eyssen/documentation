=========================
Multi-rater (360) reviews
=========================

The **Multi-rater Reviews (360)** module adds feedback from more than one direction to a review:
peers, direct reports, skip levels and people outside the company. It also adds the machinery
that makes an anonymity promise mean something.

.. _performance/360/roles:

Rater roles
===========

+------------------+-----------------------------------+-----------------------------------------+
| Rater role       | Who it is                         | Where they come from                    |
+==================+===================================+=========================================+
| Peer             | A colleague at roughly the same   | Nominated by the employee, approved by  |
|                  | level.                            | the reviewer.                           |
+------------------+-----------------------------------+-----------------------------------------+
| Direct Report    | Somebody who reports to the       | Nominated by the employee; the          |
|                  | employee.                         | nomination is refused if the person     |
|                  |                                   | does not actually report to them.       |
+------------------+-----------------------------------+-----------------------------------------+
| Skip Level       | Somebody a level further away —   | Nominated by the employee, approved by  |
|                  | their manager's manager, or a     | the reviewer.                           |
|                  | report's report.                  |                                         |
+------------------+-----------------------------------+-----------------------------------------+
| External         | A client, a supplier or any other | Proposed by name and address; answers   |
|                  | person with no account in the     | through a single-purpose link.          |
|                  | system.                           |                                         |
+------------------+-----------------------------------+-----------------------------------------+

Everything a rater answers goes into the same store as the self-assessment and the manager
assessment. That is why weighting, scoring and the anonymity threshold behave identically
wherever an answer came from: there is one code path, not four.

.. _performance/360/configure:

Configuring a round
===================

Multi-rater settings live on the cycle. Tick :guilabel:`Multi-rater Round` and open the
:guilabel:`Raters` page.

Set a :guilabel:`Nomination Deadline` — the date by which employees are expected to have
proposed their raters — and then, per role:

+------------------------------+----------------------------------------------------------------+
| Group                        | What you set                                                   |
+==============================+================================================================+
| :guilabel:`Peers`            | :guilabel:`Peers, at least`, :guilabel:`Peers, at most` (zero  |
|                              | means no upper limit), and :guilabel:`Peer Feedback is         |
|                              | Anonymous`.                                                    |
+------------------------------+----------------------------------------------------------------+
| :guilabel:`Direct reports`   | :guilabel:`Direct Reports, at least`, :guilabel:`Direct        |
|                              | Reports, at most`, and :guilabel:`Direct Report Feedback is    |
|                              | Anonymous`.                                                    |
+------------------------------+----------------------------------------------------------------+
| :guilabel:`Skip levels`      | :guilabel:`Skip Levels, at least`, :guilabel:`Skip Levels, at  |
|                              | most` (zero means this role is not used at all), and           |
|                              | :guilabel:`Skip Level Feedback is Anonymous`.                  |
+------------------------------+----------------------------------------------------------------+
| :guilabel:`Outside contacts` | :guilabel:`Ask Outside Contacts`, the minimum and maximum, and |
|                              | :guilabel:`Outside Feedback is Anonymous`.                     |
+------------------------------+----------------------------------------------------------------+

.. important::
   Whether a role is anonymous is decided **per role, per cycle**, and it is a promise. Once
   raters have answered under it, it is not something to reconsider.

.. _performance/360/threshold:

The anonymity threshold, and what it refuses to do
==================================================

An anonymous role is pooled: the reviewer and the employee see an average per question and the
written remarks shuffled into a random order, never an individual answer and never a name.

Pooling only protects people if there are enough of them. The threshold — :guilabel:`Anonymity
Threshold` on the cycle, falling back to :guilabel:`Minimum Answers Before Aggregation` in the
company settings — is the number of submitted answers a role must reach before anything at all
is released for it. It defaults to 5, and **it cannot be set below 5**, in the settings or
anywhere else.

Below the threshold, nothing is shown. Not the average, not the remarks, and **not even how
many people answered**. That last one is the part that is usually got wrong elsewhere: a count
on its own is enough to identify a small group across rounds. If two peers answered this year
and three last year, and you know who left, you can work out who said what.

Refused at launch, not at release
---------------------------------

If an anonymous role could never gather enough answers, the **launch is refused**. Not the
release — the launch.

That timing is the whole point. Refusing at release time would mean the round ran, people
answered under a promise of anonymity, and only afterwards did anybody discover the promise
could not be kept. By then the only options are to break the promise or to throw the answers
away, and both are bad.

Three situations are refused, each naming the cycle and the role:

- the round promises anonymity to a role but asks for **fewer** raters of that role than the
  threshold, so it could never release anything;
- the round promises anonymity but **caps** that role below the threshold;
- some employees in scope simply **do not have** enough possible raters of that role — a team
  of three cannot produce five peers. The message names how many employees are affected and how
  many raters each of them actually has.

In each case the fix is one of three: take those employees out of scope, turn the anonymity of
that role off for this round, or leave the round unlaunched.

.. note::
   The same check runs again when a panel is approved and when an employee nominates, so an
   anonymous role that has been whittled down to four people by rejections is caught before
   anybody is invited.

.. _performance/360/nomination:

Nomination and approval
=======================

#. The reviewer starts the nomination round with :guilabel:`Ask for Nominations`. The employee
   is mailed.
#. The employee opens their review and clicks :guilabel:`Propose my Raters`. The form asks for
   :guilabel:`Peers`, :guilabel:`Direct Reports`, :guilabel:`Skip Levels` and
   :guilabel:`Outside Contacts` (one per line, as ``Anna Nagy <anna.nagy@example.com>`` or just
   the address), plus a :guilabel:`Message to the reviewer` explaining the choice.
#. The employee submits. The reviewer is mailed and finds the proposals waiting on the
   :guilabel:`Participants` page.
#. The reviewer accepts each nomination, turns it down, or replaces it with somebody else —
   which keeps the trace of both, and asks for a reason.
#. When the panel is right, the reviewer clicks :guilabel:`Approve the Panel`. That is the
   moment the invitations go out.

The nomination form refuses, with a message saying why: nominating yourself; the same person
twice in two capacities; somebody from another company; somebody as a *direct report* who does
not report to the employee; a role this round does not ask for; too few or too many for a role;
and — for an anonymous role — a number below the threshold, with the option of proposing none
at all instead.

.. important::
   The employee nominates through a form and never gains access to the panel record itself. Once
   an anonymous rater is accepted, they stop being listed even for the reviewer: from then on
   their answers exist only inside the pooled result. That is what makes the answers anonymous
   rather than merely unlabelled.

.. _performance/360/rater:

What a rater does
=================

Internal raters
---------------

An internal rater gets a mail and a to-do, and finds the request at
:menuselection:`Performance --> Reviews --> Feedback I Owe`. They answer the questions addressed
to *Other raters*, and hand their feedback in when they are ready. Handing it in is final, and
they are told so before confirming.

A rater who is not the right person to answer can decline, optionally saying why, and will not
be asked about that review again.

Outside raters
--------------

Somebody with no account gets a single-purpose link that:

- carries a token that is **never stored** — only a fingerprint of it is kept, so a link can be
  reissued but never read back out of the database;
- **expires**, and says so in the invitation;
- resolves the review and the answerable questions from the token itself, never from anything
  the browser sends;
- is rate-limited, per link and per address.

An expired, unknown or already-used link shows a plain page explaining which of those it is and
what to do — ask the person who invited you to send a new one — rather than an error.

Outside raters can save their answers and come back to the same link to finish later.

What every rater is told
------------------------

Before answering, every rater reads what will happen to their answers: whether the role they are
answering in is anonymous, what the threshold is, that nothing at all is released below it, that
written remarks are shuffled and separated from the question they were written under, and — for
a non-anonymous role — that their answers are recorded under their name and how many of the
questions are also shown to the person being reviewed.

.. important::
   That text is **generated from the settings of the round as they stand at that moment**, never
   shipped as a fixed sentence. A promise that outlives the configuration it was made under is
   not a promise.

.. _performance/360/results:

What each person sees at the end
================================

The reviewer
------------

A :guilabel:`Multi-rater Feedback` page on the review, with one block per rater role: how many
people answered, the average per question, and the written remarks pooled and shuffled.

A role that has not reached the threshold shows a short explanation instead — that nobody was
asked in that group, that nobody has answered yet, or that fewer than the threshold have
answered and therefore nothing is released, including the count.

Named roles behave differently: if a role was not promised anonymity, its answers appear as
ordinary answers, attributed.

The employee
------------

Whatever the reviewer decided to share, on the questions marked as shared, plus the released
rating. Never an individual anonymous answer, and never the panel.

HR officers
-----------

Everything the reviewer sees. An officer can read an individual non-anonymous answer; an
anonymous one is excluded for them too.

.. seealso::
   - :doc:`confidentiality` — the wider picture, and what a purge removes from a panel
   - :doc:`review_cycles` — the nomination stage and its reminders

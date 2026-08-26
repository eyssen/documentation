===============================
Trial-period reviews in Hungary
===============================

The **Hungary - Performance Reviews** module adds what Hungarian practice needs on top of the
generic application: trial-period (*próbaidő*) reviews counted from the employment contract,
a probation decision record with its own printed Hungarian document, and Hungarian master data
to start from.

It contains data and wiring only. Nothing here changes how a review works elsewhere.

.. _performance/probation/plan:

How the plan counts from the contract
=====================================

A trial-period review does not count months from an anniversary. It reads the employee's
**running employment contract** and works backwards from the end of the trial period, so that
the decision is prepared while there is still time to take it.

- The **anchor date** of the plan is the contract's start date. An employee with no running
  Hungarian contract falls back to the generic anchor.
- The **decision review** falls due :guilabel:`Probation Decision Lead Time (days)` before the
  trial period ends — 10 days by default. Set it in :menuselection:`Settings --> Employees`,
  in the :guilabel:`Performance Reviews` block. It has to leave enough time to hold the
  conversation, write the decision and hand it over **while the trial period is still running**.
- Optionally, :guilabel:`Probation Checkpoints` also plans a short review 30 and 60 days after
  the employment started, in front of the decision review. It is off by default: whether every
  probationer is reviewed twice on the way is your decision, not the module's.

A checkpoint is only planned when it falls before the decision review, so a short trial period
does not produce a checkpoint after the decision it was meant to inform. An employee whose
contract has no trial period end date has no probation plan at all.

.. note::
   A trial period shorter than the lead time still gets its decision review; it simply falls
   due on the first day of the employment.

Running a probation cycle
-------------------------

#. Create a cycle of the type *Probation*, on the *Próbaidős értékelés* questionnaire, with a
   population filter that selects the people on trial.
#. Launch it. Launching a probation cycle creates **no** review — it puts the cycle into
   :guilabel:`Running`, and from then on a daily job creates each review as it falls due.
#. Make sure :guilabel:`Plan Reviews Automatically` is on in the company settings. It is the
   master switch of that job: while it is off, a probation cycle creates nothing at all.

At most one review per employee is created per run, and none while a previous probation review
of the same cycle is still open — a checkpoint nobody has answered yet must not be buried under
the next one.

.. note::
   Probationers who have no manager on their employee record cannot be reviewed. The cycle's log
   records **how many** were skipped for that reason but never their names, since the log of a
   cycle is read by more people than the list itself should be.

.. _performance/probation/decision:

The probation decision
======================

The decision is a record of its own, not a field on the review. It has its own document, its
own lock and its own audit trail, because it is the thing that gets handed to a person and may
have to be produced years later.

Reach it from the :guilabel:`Probation Decision` button, or the page of the same name, on a
probation review — both visible to an officer — or from
:menuselection:`Performance --> Reviews --> Probation Decisions`.

Fill in:

- :guilabel:`Employee` and :guilabel:`Contract`, which bring in :guilabel:`Employment Start` and
  :guilabel:`End of Trial Period`;
- :guilabel:`Decision Date` — the date the decision was taken. It cannot be earlier than the
  start of the employment it decides about;
- :guilabel:`Decided By` — the person who *took* the decision, not the person who typed it in;
- :guilabel:`Decision`:

  +------------------------+-----------------------------------+---------------------------------+
  | Decision               | What it means                     | What it also requires           |
  +========================+===================================+=================================+
  | Employment confirmed   | The trial period ends and the     | A :guilabel:`Reason`, which is  |
  |                        | employment continues on unchanged | printed on the document.        |
  |                        | terms.                            |                                 |
  +------------------------+-----------------------------------+---------------------------------+
  | Trial period extended  | The trial period is prolonged.    | A :guilabel:`Reason`, and       |
  |                        |                                   | :guilabel:`Trial Period         |
  |                        |                                   | Extended To` — a date later     |
  |                        |                                   | than the current end of the     |
  |                        |                                   | trial period.                   |
  +------------------------+-----------------------------------+---------------------------------+
  | Terminated during the  | The employment ends with          | Nothing further. See below.     |
  | trial period           | immediate effect while the trial  |                                 |
  |                        | period runs.                      |                                 |
  +------------------------+-----------------------------------+---------------------------------+

When the decision is settled, click :guilabel:`Lock`. A locked decision is the document that was
handed over: it can no longer be edited or deleted. Only an officer can unlock it, and the fact
is recorded on the decision.

:guilabel:`Print` produces the Hungarian document.

.. important::
   A trial period may be extended once, and its total length is capped by law and by the
   applicable collective agreement. The new end date is checked against the contract, but it is
   never invented for you — check it before the decision is handed over.

.. _performance/probation/termination:

Why a termination carries no stated reason
==========================================

This is the part of the module most likely to look like a missing feature, so it is worth being
explicit about it.

Under the Hungarian Labour Code, either party may end the employment with immediate effect while
the trial period runs, and **the law asks the terminating party for no justification**. The
decision document for a termination therefore records the date, the person who took the
decision, and the fact — and nothing else. The :guilabel:`Reason` field is not rendered on it,
and the *Indokolás* (Reasoning) heading is not printed at all.

That is not squeamishness. A reason that does not have to be given, but is given anyway, becomes
a statement the employer has to stand behind. If the termination is later challenged, the
employer is no longer defending a lawful trial-period termination that needs no grounds; they
are defending the specific grounds they chose to write down, and every weakness in that sentence
is now theirs to answer for. The form says so, in a warning shown as soon as *Terminated during
the trial period* is chosen.

You can still record something internally: the :guilabel:`Reason` field remains, and remains
readable by HR. It is an internal note. It never reaches the document.

.. warning::
   An internal note is not a secret. Read :doc:`confidentiality` on what a subject access
   request, a labour dispute or a court can bring out. If you would not want to defend a
   sentence in front of a labour court, do not write it — not in the reason field, and not in a
   working note.

Confirmations and extensions are the opposite case: both **require** a reason, and it is printed.
Those are decisions the employee is entitled to see the reasoning of.

.. _performance/probation/document:

The printed decision
====================

The document is produced in the employee's own language, falling back to the company's. For a
Hungarian employee it prints entirely in Hungarian: *Próbaidős döntés* with the employee, job,
department, employment start, end of trial period and decision date; then the paragraph for the
decision that was taken; then, for a confirmation or an extension only, *Indokolás* with the
reason; then the acknowledgement paragraph, the two signature lines and the place and date.

The paragraph for a termination cites the Labour Code provisions that make the termination
lawful without grounds, which is precisely why no grounds appear anywhere else on the page.

.. _performance/probation/data:

Hungarian master data
=====================

Installing the pack adds ready-made content, so a Hungarian company is not starting from a
blank rating scale.

The rating scale
----------------

*Ötfokozatú értékelési skála* — a five-level scale, from *Nem felel meg az elvárásoknak* (1) to
*Kiemelkedő* (5), each level carrying a behavioural description written in Hungarian and an
advisory target share. The two lowest levels are marked as below expectation.

.. note::
   The middle level, *Megfelel az elvárásoknak*, is described as the expected performance and
   not as a tolerable minimum. That wording is deliberate and it is worth keeping: a scale whose
   middle rung reads as "adequate, at best" pushes every manager upwards and stops
   distinguishing anybody.

The questionnaires
------------------

Four released questionnaires, all in Hungarian:

+------------------------------------+----------------------------------------------------------+
| Questionnaire                      | For                                                      |
+====================================+==========================================================+
| *Éves teljesítményértékelés*       | The annual review.                                       |
+------------------------------------+----------------------------------------------------------+
| *Próbaidős értékelés*              | The trial-period review.                                 |
+------------------------------------+----------------------------------------------------------+
| *Vezetői visszajelzés*             | Upward feedback on a manager.                            |
+------------------------------------+----------------------------------------------------------+
| *Negyedéves előrehaladás*          | A short quarterly check-in.                              |
+------------------------------------+----------------------------------------------------------+

Each was written from Hungarian HR practice and from the obligations of the Labour Code. They
are ordinary questionnaires: use them as they are, or use :guilabel:`New Version` to make them
yours.

Company defaults
----------------

On installation, and only where they are still empty, Hungarian companies get a retention period
of 36 months — the limitation period for labour claims — with *Ötfokozatú értékelési skála* as
the default rating scale and *Éves teljesítményértékelés* as the default questionnaire. Settings
you have already made are never overwritten.

.. seealso::
   - :doc:`review_cycles` — cycle types, and the daily generator behind the probation plan
   - :doc:`confidentiality` — retention, legal hold and what an internal note really is

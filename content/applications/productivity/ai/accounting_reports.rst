=========================
AI for accounting reports
=========================

The module AI for Accounting Reports adds an assistant to the financial reports.
It explains a report in plain language, points out trends and anomalies, and can
run a second, independent check of its own findings with two AI agents. It never
changes any accounting data.

Analyse a report
================

1. Open a report wizard, for example profit and loss, balance sheet, trial
   balance, general ledger, partner ledger, aged partner balance, tax report or
   journal audit, and set the dates and options as you normally would.
2. Click :guilabel:`Analyse with AI` next to the usual print button (accountants
   only). You land on a new analysis. The analysis runs in the background; the
   form shows its progress and you are notified when it is done.
3. Read the result on the tab :guilabel:`Analysis`. The tab :guilabel:`Report
   data` shows the rows the AI was given. Use :guilabel:`Analyse again` to run
   it again.

All analyses are listed in :menuselection:`Accounting --> Reporting --> AI
Report Analyses`. You see your own analyses; accounting managers see those of
the company. Each analysis has its own chatter.

What the AI is given
--------------------

- The AI works from the report's own computed rows, the same figures you could
  print, calculated in your environment with your access rights. No PDF is read.
  Each row gets a reference (R1, R2, and so on) so that findings can point to
  their evidence.
- For financial reports and the trial balance with two dates and no comparison
  chosen, the same report is also computed for the previous period of the same
  length, so the AI can describe trends.
- Key figures such as current ratio, quick ratio, debt to equity, margins, net
  result and income growth are calculated by the program, not by the AI. The AI
  only explains them. They are approximations from the account lines of the
  report, and a report without account detail gives none.
- A report is limited to 400 rows. A large general ledger is reduced to account
  totals plus the 25 largest items of the period, and the text given to the AI
  is capped.

Audit with an auditor and a reviewer
====================================

On an analysis, click :guilabel:`Audit with AI agents` for a more careful check.
It also runs in the background.

1. The agent :guilabel:`Financial Auditor` proposes up to eight findings, each
   citing the report rows as evidence and, where relevant, an amount.
2. It hands them to a second agent, :guilabel:`Financial Reviewer`, which looks
   the rows up and confirms or rejects every finding.
3. The program then checks the evidence itself: a finding stays
   :guilabel:`Confirmed` only if the reviewer confirmed it, every row it cites
   exists and its amount (if any) is found in the cited rows within 0.5 percent.
   Findings that were not reviewed or are not supported are kept as rejected,
   with the reason, so nothing is hidden.

The result is the tab :guilabel:`Audit` with a summary, the :guilabel:`Confirmed
findings` and the :guilabel:`Rejected findings` with their severity, evidence
and verdict, plus a note in the chatter that lists the confirmed findings. Click
:guilabel:`Open audit in AI panel` to read or continue the conversation with the
auditor in the AI panel (see :doc:`panel`). The panel can also look up the
report rows while the analysis is open, and two quick prompts are offered:
:guilabel:`Explain this report` and :guilabel:`What should I check first?`.

Safety and requirements
=======================

- Read-only: the two agents have only the Ask capability and no tools that read
  or write records. The only things written are the analysis and its findings,
  the AI conversation and the logs. Journal entries and other accounting data
  stay unchanged.
- Before anything is sent, the program checks that a model is configured, that
  you have the Ask and Read capabilities, and that the AI read policy allows
  journal items and accounts (see :doc:`access_policy`). If not, you get a plain
  message and no strike is recorded.
- The agents are available to accountants only. Their names are translatable, so
  they follow the language of the user.
- Reports of the optional cash book, bank book and day book modules have their
  own wizards and are not covered.

Note for administrators: background jobs and time limits
========================================================

An audit makes several model calls and easily takes longer than an ordinary web
request is allowed to run. That is why analyses and audits run as background
jobs of the scheduled action "AI: Run accounting report analyses and audits".
The job runs in the environment of the person who clicked, never in the identity
of the scheduler, and the form refreshes by itself. A job that stays in the
running state for more than 30 minutes is marked as failed, so nothing stays
stuck.

.. important::
   The time a background job may run comes from the server option
   ``limit_time_real_cron`` when it is set to a positive value, otherwise from
   ``limit_time_real``, and otherwise from Odoo's default. If audits fail with a
   timeout, raise ``limit_time_real_cron`` in the server configuration file (for
   example to 900 seconds) and restart the server. The value 0 is not treated as
   "no limit".

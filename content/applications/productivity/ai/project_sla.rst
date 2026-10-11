========================
AI for projects with SLA
========================

If you handle customer tickets as tasks of a project with service levels (SLA),
the module AI Project SLA gives your team reply drafts, hand-over summaries, an
SLA risk check and an optional automatic triage of new tickets. It needs the
project SLA app and the knowledge sources module (see :doc:`knowledge_sources`).

Quick prompts on tickets
========================

For project users, these quick prompts appear in the AI panel on a task (see
:doc:`panel`). They read the recent messages, the SLA lines of the task, similar
solved tickets and your knowledge sources, and they change nothing:

- :guilabel:`Draft customer reply`: a reply based on the conversation, the way
  similar tickets were solved and your sources, with numbered citations. It is
  never posted for you.
- :guilabel:`Summarise ticket`: a hand-over summary including the SLA situation.
  It replaces the generic summary prompt on tasks.
- :guilabel:`Suggest priority and assignee`: a suggestion with reasons, based on
  similar tickets, the SLA and the workload of the candidates.
- :guilabel:`SLA risk`: for every SLA, what it measures, the deadline in your
  time zone, the hours left, whether it is paused, fulfilled, urgent or
  breached, and what to do now.

.. note::
   The suggestions about similar tickets depend on the similar-tasks feature
   being on for the project and on an embedding model (see
   :doc:`knowledge_sources`). The prompts are offered on every task for project
   users; on a task without an SLA they say so.

Automatic triage of new tickets
===============================

The triage lets the AI classify a new ticket: its priority, its tags and ticket
type, and its assignee when nobody is assigned yet. It is off by default and is
set per project.

Set it up
---------

1. Open the project form and find the setting :guilabel:`AI triage` in the AI
   block. Choose :guilabel:`Off`, :guilabel:`Propose for review` or
   :guilabel:`Apply automatically`.
2. Choose the :guilabel:`Triage reviewer` (by default the project manager). The
   reviewer must be an AI user, and the project cannot be saved with triage on
   otherwise.
3. Optionally list the tags that stand for ticket types in :guilabel:`Ticket
   types`, for example Bug and Question.
4. Ask an administrator to allow AI writes on tasks: the capability
   :guilabel:`Write data` must be on and an AI access rule must allow writing
   the priority, tags and assignees of tasks (see :doc:`feature_access` and
   :doc:`access_policy`). Both are off by default.

What happens
------------

- A new task of the project is marked :guilabel:`Waiting for AI triage`. About
  every 10 minutes (and right after the task is created) the AI first embeds the
  new tasks so that similar tickets are known, and then triages each queued task
  in the name of the reviewer, with the reviewer's rights.
- The AI sees the ticket, its messages, the allowed priorities, ticket types and
  tags, the possible assignees (only when the task has none), similar solved
  tickets and the SLA. It can answer only with the offered values: a priority,
  tags and a ticket type from the lists and an assignee from the candidates.
  Values that equal the current ones are dropped. If nothing is left, the task
  shows :guilabel:`Nothing to change`.
- With :guilabel:`Propose for review`, the proposal waits for the reviewer. On
  the task, the reviewer sees a banner with the reasoning and the buttons
  :guilabel:`Apply` and :guilabel:`Discard`, gets a to-do activity, and finds
  the proposal also under the AI write proposals. With :guilabel:`Apply
  automatically` the same proposal is applied at once, and if that fails it
  waits for review. Unreviewed proposals expire after 24 hours by default.
- You can also triage a single ticket yourself with :guilabel:`Triage with AI`
  in the task header. The proposal is then addressed to you.
- Applying a triage does not count as the team's first reaction to the customer,
  so a "first activity" SLA is not marked as fulfilled by the AI's
  classification.

.. note::
   Nothing is changed on a ticket without the reviewer's confirmation unless the
   project manager chose :guilabel:`Apply automatically`. Every applied change
   is recorded in the AI change log (see :doc:`monitoring`). The AI reads only
   the names of the possible assignees, and the workload comes from the tasks
   themselves.

==============================
Service level agreements (SLA)
==============================

An **SLA policy** sets a deadline for the work on a task: how many working hours or days may pass
before the task reaches a target stage, or before someone first works on it. The database then
tracks each task against its policies, warns the assignee before the deadline, and escalates when
the deadline is missed.

.. note::
   This feature is provided by the *Project SLA* (`eyssen_project_sla`) module.

Configuration
=============

SLA tracking is switched on per project through a :doc:`project category <categories>` that has the
:guilabel:`SLA` option enabled. Then open the project, go to the :guilabel:`SLA` section of the
settings, and select the policies that apply in the :guilabel:`SLA` field.

.. _project/sla-policy:

Creating an SLA policy
======================

Go to :menuselection:`Project --> Configuration --> SLA Policies` and click :guilabel:`New`.

Target
------

- :guilabel:`SLA Type` decides what is measured:

  - :guilabel:`Stage Completion` – the time the task may take to reach one of the
    :guilabel:`Target Stages`.
  - :guilabel:`First Activity` – the time that may pass until somebody first works on the task
    (a stage change, an assignment, a message, and similar events all count).

- :guilabel:`Time` and :guilabel:`Time Unit` set the allowed duration in :guilabel:`Hours` or
  :guilabel:`Days`.
- :guilabel:`Resource Calendar` is the working schedule used to count that time, so nights,
  weekends, and company holidays do not consume the SLA.
- :guilabel:`Target Stages` (for :guilabel:`Stage Completion`) are the stages that fulfill the
  policy.
- :guilabel:`Freeze Stages` pause the timer. While the task sits in one of these stages — waiting
  for a customer answer, for instance — the clock does not run, and the deadline moves accordingly.

Scope
-----

- :guilabel:`Minimum Priority` restricts the policy to tasks of at least that priority. Leave it at
  :guilabel:`All Priorities` to apply it everywhere.
- :guilabel:`Customers` restricts the policy to the tasks of the selected customers. Leave it empty
  to apply it to all customers.

Warnings
--------

- :guilabel:`Urgent Time` is the remaining time at which the task switches to the
  :guilabel:`Urgent` state.
- :guilabel:`Warning Before (hours)` schedules a :guilabel:`To Do` activity for the assignee (or,
  if the task is unassigned, for the project manager) that many hours before the deadline. Only one
  reminder is created per policy and task.

The :guilabel:`SLA Policy Description` is a rich-text field for the wording of the agreement; it is
translatable, as is the policy name. The :guilabel:`Projects` and :guilabel:`Tasks` smart buttons
show where the policy is in use.

.. screenshot:: services-project-sla-form
   :menu: Project ‣ Configuration ‣ SLA Policies
   :shows: An SLA policy form named "First response - 4h", with SLA Type "First Activity", Time 4 Hours, a resource calendar, Urgent Time and Warning Before filled in, and two escalation rules in the list at the bottom.
   :highlight: The SLA Type, Time and Freeze Stages fields (red frame).
   :data: Policy "First response - 4h"; calendar "Standard 40 hours/week"; escalation rules "Notify manager" and "Raise priority".
   :module: eyssen_project_sla
   :notes: English UI, light theme, 1440px width, crop to the form sheet.

.. _project/sla-states:

SLA states on tasks
===================

Every task of an SLA-enabled project carries one line per applicable policy in its
:guilabel:`SLAs` tab, showing the :guilabel:`SLA Deadline`, the :guilabel:`SLA Remaining Time`, and
the state:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - State
     - Meaning
   * - :guilabel:`In Time`
     - The deadline is still comfortably ahead.
   * - :guilabel:`Urgent`
     - The remaining time has fallen below the policy's :guilabel:`Urgent Time`.
   * - :guilabel:`Success`
     - The task reached a target stage (or was first worked on) before the deadline.
   * - :guilabel:`Fail`
     - The deadline passed without the target being reached.
   * - :guilabel:`None`
     - No deadline could be computed, for example because the policy has no resource calendar.

The same states are shown as colored badges next to the task title, on the Kanban cards, and as
:guilabel:`SLA In Time`, :guilabel:`SLA Urgent`, :guilabel:`SLA Success`, and :guilabel:`SLA
Failed` filters in the search panel of the task list.

A scheduled action re-evaluates the open SLA states in the background, so the states, the
reminders, and the escalations stay up to date without anyone opening the task.

.. screenshot:: services-project-sla-task-tab
   :menu: Project ‣ (project) ‣ (open a task) ‣ SLAs
   :shows: The SLAs tab of a task with two policy lines, one in the "In Time" state and one in the "Urgent" state, with their deadlines and remaining times.
   :highlight: The SLA State badges (red frame).
   :data: Task "Boiler not heating"; policies "First response - 4h" (Success) and "Resolution - 2 days" (Urgent).
   :module: eyssen_project_sla
   :notes: English UI, light theme, 1440px width, crop to the tab.

.. _project/sla-escalation:

Escalation rules
================

The :guilabel:`Escalation Rules` list at the bottom of the policy defines what happens when the SLA
goes wrong. Each rule has:

- a :guilabel:`Trigger`: :guilabel:`On SLA Breach` (the state became :guilabel:`Fail`) or
  :guilabel:`On Urgent Status`;
- an :guilabel:`Action`:

  - :guilabel:`Send Notification` – schedules a :guilabel:`To Do` activity for each user in
    :guilabel:`Notify Users`;
  - :guilabel:`Reassign Task` – assigns the task to the user in :guilabel:`Reassign To`, replacing
    the current assignees;
  - :guilabel:`Raise Priority` – raises the task to :guilabel:`New Priority`, never lowering it.

Rules run in the order of the list handle, and each rule fires **at most once** per task and
policy. A rule can be deactivated with its :guilabel:`Active` toggle without deleting its history.

.. _project/sla-assignment:

Team members and automatic assignment
=====================================

The :guilabel:`SLA` section of the project settings also holds the project's team:

- :guilabel:`Team Members` – the users among whom the work is shared.
- :guilabel:`Automatic Assignment` – when enabled, each new task of the project is assigned
  automatically to a team member.
- :guilabel:`Assignment Method` – :guilabel:`Randomly` picks any team member, while
  :guilabel:`Balanced` picks the member with the fewest open tasks in the project.

The project settings also display the live SLA counters of the project — :guilabel:`In Time`,
:guilabel:`Urgent`, :guilabel:`Success`, :guilabel:`Failed`, and the success :guilabel:`Rate`.

.. _project/sla-reporting:

SLA analysis
============

Go to :menuselection:`Project --> Reporting --> SLA Analysis` for a pivot and graph view of the SLA
results. Measures and groupings include the policy, the project, the customer, the assignee, the
stage, the priority, the SLA type, the :guilabel:`SLA Target (hours)`, the :guilabel:`Hours to
Close`, and the :guilabel:`Exceeded Hours`, so that recurring breaches can be traced back to a
team, a customer, or a policy that is set too tightly.

.. screenshot:: services-project-sla-analysis
   :menu: Project ‣ Reporting ‣ SLA Analysis
   :shows: The SLA Analysis pivot view grouped by SLA policy in rows and SLA state in columns, with task counts.
   :highlight: None.
   :data: Two policies across roughly 40 tasks with a mix of Success and Fail results.
   :module: eyssen_project_sla
   :notes: English UI, light theme, 1440px width, crop to the pivot table.

.. seealso::
   - :doc:`categories`
   - :doc:`templates`

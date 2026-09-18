==============
Gantt planning
==============

The **Gantt** view places the tasks of your projects on a timeline, so that you can plan them,
shift them, and see at a glance where the schedule breaks.

.. note::
   This feature is provided by the *Project Gantt* (`project_gantt`) module.

.. _project/gantt-dates:

Planned dates
=============

The Gantt bar of a task is drawn between its :guilabel:`Start Date` and its :guilabel:`Planned
End`; both fields are on the task form, next to the :guilabel:`Deadline`. The deadline itself is
kept separate and is drawn on the chart as a marker, so that the plan and the commitment stay
distinguishable.

Two more fields control how the task appears:

- :guilabel:`Progress` – the completion percentage drawn inside the bar.
- :guilabel:`Gantt Shape` – :guilabel:`Task` draws a bar, :guilabel:`Milestone` draws a diamond.

Two buttons are available on tasks that are scheduled:

- :guilabel:`Unschedule` clears the planned dates and moves the task back to the unscheduled list.
- :guilabel:`Save Baseline` stores the current planned dates as the **baseline**, which is then
  drawn under the bar so later changes to the plan remain visible.

.. important::
   The planned end date must not be earlier than the planned start date, and the progress must be
   between 0 and 100.

.. _project/gantt-view:

Working in the Gantt view
=========================

Open :menuselection:`Project --> Tasks` (or the tasks of a project) and switch to the
:icon:`fa-tasks` :guilabel:`Gantt` view. The view opens on the :guilabel:`Month` scale, grouped by
assignee, and offers the :guilabel:`Day`, :guilabel:`Week`, :guilabel:`Month`, and
:guilabel:`Year` scales.

In this view you can:

- drag a bar to move a task, or drag its edge to change its duration; dates snap to the scale, and
  non-working days are skipped;
- draw a bar in an empty cell to plan an unscheduled task;
- open the :guilabel:`Unscheduled` panel to plan the tasks that have no dates yet;
- shift the successors of a task automatically when you move it;
- display the columns :guilabel:`Assignees`, :guilabel:`Stage`, :guilabel:`Allocated Hours`, and
  :guilabel:`Deadline` next to the chart;
- show the **critical path**, the **baseline**, and the **workload** of the assignees.

Tasks are colored by project, and tasks that overlap or whose dependencies are inconsistent are
highlighted in red.

.. screenshot:: services-project-gantt-view
   :menu: Project ‣ Tasks ‣ (Gantt view)
   :shows: The Gantt view of project tasks on the Month scale, grouped by assignee, with several bars, one milestone diamond, a dependency arrow between two tasks, and one bar highlighted in red.
   :highlight: The scale selector and the red (conflicting) bar (red frames).
   :data: Project "Boiler maintenance 2026" with about eight tasks across two assignees.
   :module: project_gantt
   :notes: English UI, light theme, 1440px width, crop to the chart area.

.. _project/gantt-links:

Dependencies between tasks
==========================

Dependencies can be drawn directly in the chart, or maintained in the :guilabel:`Gantt Links` tab
of the task, which lists the incoming and the outgoing links. Each link has:

- a :guilabel:`Type`: :guilabel:`Finish to Start`, :guilabel:`Start to Start`, :guilabel:`Finish to
  Finish`, or :guilabel:`Start to Finish`;
- a :guilabel:`Lag (days)`, a positive delay or a negative lead between the two tasks.

.. note::
   - A task cannot be linked to itself, the same pair cannot be linked twice, and circular chains
     of dependencies are refused.
   - :guilabel:`Finish to Start` links are kept in sync with the standard :doc:`task dependencies
     <tasks/task_dependencies>` of the task, so both views of the same relationship stay
     consistent.

When a predecessor finishes later than its successor should start, taking the lag into account, the
successor is flagged and drawn in red until the plan is corrected.

.. seealso::
   - :doc:`tasks/task_dependencies`
   - :doc:`project_management`

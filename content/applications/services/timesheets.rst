:nosearch:
:show-content:
:hide-page-toc:
:show-toc:

==========
Timesheets
==========

**Timesheets** record the time your employees spend on the tasks of your :doc:`projects <project>`.
The hours logged feed the progress of the tasks, the profitability of the projects, and the
invoicing of the work.

Configuration
=============

Time is logged on the tasks of the projects where it is allowed. Open a project's settings and
enable :guilabel:`Timesheets` to log time on its tasks.

The database-wide options are under :menuselection:`Timesheets --> Configuration --> Settings`:

- :guilabel:`Project Time Unit` – the unit in which time is stored and reported, usually
  :guilabel:`Hours` or :guilabel:`Days`.
- :guilabel:`Encoding Method` – whether users enter their time in :guilabel:`Hours` or in
  :guilabel:`Days`. This only affects how the time is typed and displayed, not how it is stored.
- :guilabel:`Time Off` – see :doc:`timesheets/time_off`.

.. screenshot:: services-timesheets-settings
   :menu: Timesheets ‣ Configuration ‣ Settings
   :shows: The Timesheets settings page with the Time Encoding block (Project Time Unit and Encoding Method) and the Time Off block.
   :highlight: The Time Encoding block (red frame).
   :data: Project Time Unit "Hours", Encoding Method "Hours".
   :module: hr_timesheet
   :notes: English UI, light theme, 1440px width, crop to the settings blocks.

Recording and reviewing time
============================

- :menuselection:`Timesheets --> Timesheets --> My Timesheets` shows your own entries, where a new
  line is added with the project, the task, a description, and the time spent.
- :menuselection:`Timesheets --> Timesheets --> All Timesheets` shows the entries of everybody you
  are allowed to see.

Time can also be logged directly from the :guilabel:`Timesheets` tab of a task, which compares the
hours spent with the :guilabel:`Allocated Hours` of that task.

Reporting
=========

:menuselection:`Timesheets --> Reporting` analyzes the logged time :guilabel:`By Employee`,
:guilabel:`By Project`, and :guilabel:`By Task`, in list, pivot, and graph views.

.. toctree::
   :titlesonly:

   timesheets/logging_time
   timesheets/services
   timesheets/time_off

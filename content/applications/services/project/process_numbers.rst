===============
Process numbers
===============

A **process number** is a case identifier that ties together everything belonging to the same
matter across the database. On the Project side it can be attached to a project and to its tasks,
so that all the work on one case can be found from a single number.

.. note::
   This feature is provided by the *Process Number - Project* (`process_number_project`) module,
   which requires the *Process Number* (`process_number`) module.

Configuration
=============

To have a process number created automatically for every new project, go to
:menuselection:`Settings --> eYssen ERP`, and, in the :guilabel:`Process Number` section, enable
:guilabel:`Create Automatically` under the :guilabel:`Project` option. The setting is per company.

.. seealso::
   :doc:`../../general/process_numbers` for the process number records themselves, and their use
   in the other applications.

.. _project/process-number-mode:

Process number mode
===================

Every project has a :guilabel:`Process Number Mode`:

:guilabel:`Single`
   The whole project belongs to one case. The :guilabel:`Process Number` chosen on the project is
   applied to all of its tasks, and tasks created later inherit it. Changing the project's process
   number updates the tasks.

:guilabel:`Multi`
   Each task carries its own process number. The project itself has none, and every task can be
   assigned to a different case.

If the project already contains tasks with different process numbers, switching the mode back to
:guilabel:`Single` is refused, so that existing case assignments are not silently overwritten.

Use the :guilabel:`Create a new process number` link on the project or on the task to generate a
number on the spot instead of picking an existing one.

.. screenshot:: services-project-process-number
   :menu: Project ‣ Projects ‣ (open a project) ‣ Settings
   :shows: The project settings with the Process Number Mode set to "Single", a process number selected, and the "Create a new process number" link below it.
   :highlight: The Process Number Mode and Process Number fields (red frame).
   :data: Project "Boiler maintenance 2026", process number "PN/2026/0007".
   :module: process_number_project
   :notes: English UI, light theme, 1440px width, crop to the settings block.

Finding the work behind a number
================================

Open a process number to see the :guilabel:`Projects` and :guilabel:`Tasks` smart buttons with
their counts, and the lists of the linked projects and tasks below them. The process number list
also shows the linked projects and tasks as tags.

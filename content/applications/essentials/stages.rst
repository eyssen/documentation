======
Stages
======

*Stages* are used to organize an app's pipeline and track the progress of configured items, from now
on are referred to as cards.

In apps these cards represent specific items, for example, in the **Project** app, stages track
tasks, and in the **CRM** app, stages track opportunities. Stages are customizable, and can be
renamed to fit the needs of each team.

Create or modify stages
=======================

.. important::
   :ref:`Developer mode <developer-mode>` **must** be activated to access the stages menu. To
   activate developer mode, go to :menuselection:`Settings app --> General Settings --> Developer
   Tools`, and click :guilabel:`Activate the developer mode`.

To view or modify stages, go to the desired app and go to its stage configuration menu, for example
:menuselection:`Project --> Configuration --> Task Stages` or :menuselection:`CRM --> Configuration
--> Stages`.

The default list view on the :guilabel:`Stages` page displays the stages currently available in the
app. They are listed in the order they appear in the pipeline.

To change the order of the stages, click the :icon:`oi-draggable` :guilabel:`(draggable)` icon, to
the left of the stage name, and drag it to the desired place on the list.

.. screenshot:: essentials-stages-list
   :menu: Project ‣ Configuration ‣ Task Stages
   :shows: List view of task stages in pipeline order, with the drag handle to the left of each
      stage name and the New button at the top left.
   :highlight: The drag handle column.
   :data: Demo task stages "New", "In Progress", "Done", "Cancelled".
   :module: project
   :notes: English UI, developer mode active, 1440px width, crop to the list.

.. tip::
   Change the stage order on the Kanban view of a team's pipeline by dragging and dropping
   individual columns.

To create a new stage, click the :guilabel:`New` button at the top-left of the stage list. Doing so
reveals a blank stage form.

Choose a :guilabel:`Name` for the new stage.

.. screenshot:: essentials-stages-form
   :menu: Project ‣ Configuration ‣ Task Stages ‣ New
   :shows: Task stage form with Name, Email Template, SMS Template, Rating Email Template, Folded in
      Kanban and
      Projects fields.
   :highlight: The Name field.
   :data: New stage "Review".
   :module: project, project_sms
   :notes: English UI, developer mode active, crop to the form sheet.

Progress bar
============

The progress bar is visible above each stage, displaying the percentage breakdown of every status
type for all the cards within that stage. Each status type has an assigned color that appears within
the bar.

The specific definition of these statuses changes depending on the app. For example, in the
**Project** app, the progress bar of a task stage consists of the :guilabel:`In Progress`,
:guilabel:`Changes Requested`, :guilabel:`Approved`, :guilabel:`Waiting`, :guilabel:`Done`, and
:guilabel:`Cancelled` task states. In the **CRM** app, the progress bar shows the status of the
activities planned on the opportunities.

To see a detailed count, hover over a representative color, which activates a notification detailing
the number of cards in the stage of that specific status.

Clicking a status color filters the stage to show only cards with that status. The card count for
the selected status appears next to the progress bar.

.. screenshot:: essentials-stages-progress-bar
   :menu: Project ‣ (any project) kanban view
   :shows: Kanban column header with its colored progress bar; one color is clicked, so the column
      is filtered and the count for that state is displayed next to the bar.
   :highlight: The progress bar and the filtered count.
   :data: Demo project "Office Design", stage "In Progress" with tasks in several states.
   :module: project
   :notes: English UI, crop to one or two kanban columns.

Add email and SMS templates to stages
=====================================

When an :guilabel:`Email Template` is added to a stage, a preconfigured email is automatically sent
to the customer when a card (e.g., a task) reaches that specific stage in the pipeline. Likewise,
adding an :guilabel:`SMS Template` triggers a preconfigured SMS text message to send to the
customer.


.. note::
   The :guilabel:`SMS Template` field is available when the *Project - SMS* module (`project_sms`)
   is installed. SMS text messaging is an :doc:`In-App Purchase (IAP)
   </applications/essentials/in_app_purchase>` service that requires prepaid credits to work.

To select an existing email template, select it from the :guilabel:`Email Template` field. After
choosing a template, click on the :icon:`oi-arrow-right` :guilabel:`(right arrow)` icon to the right
of the field to edit the chosen template.

To create a new template from this form, click the field, and enter a title for the new template.
Then, select :guilabel:`Create and edit` from the drop-down menu that appears, and complete the form
details.

Follow the same steps to select, edit, or create an :guilabel:`SMS Template`.

.. screenshot:: essentials-stages-sms-template
   :menu: Project ‣ Configuration ‣ Task Stages ‣ (stage) ‣ SMS Template ‣ Create and edit
   :shows: SMS template form opened from the stage: Name, Applies to "Task", and the message body.
   :highlight: The message body.
   :data: Template "Task in review"; body using the task name placeholder.
   :module: project_sms, sms
   :notes: English UI, crop to the dialog.

.. seealso::
   :doc:`/applications/general/companies/email_template`

Fold a stage
============

By default, stages are unfolded in the Kanban view. If there is a Won or Closed stage, it is folded
by default.

Cards in an unfolded stage are visible in the pipeline under the stage name, and are considered
*open*.

Stages can be configured to be folded in the Kanban view of the pipeline page.

The name of the folded stages are still visible, but the cards in the stage are hidden from view.

To fold a stage, tick the :guilabel:`Folded in Kanban` checkbox on the :guilabel:`Stages` form.

.. warning::
   Cards that reach a *folded* stage are considered *closed*. Closing a card before the work is
   completed can result in reporting and communication issues. This setting should **only** be
   enabled for stages that are considered *closing* stages.

Temporarily fold a stage
------------------------

Stages can be temporarily folded in the Kanban view of the pipeline, as well.

Open the pipeline in the desired app, e.g., a project's Kanban view in the **Project** app.

Hover the cursor at the top of the desired stage to fold temporarily, then click the :icon:`fa-gear`
:guilabel:`(gear)` icon that appears, and select :guilabel:`Fold` from the drop-down menu.

.. screenshot:: essentials-stages-fold-kanban
   :menu: Project ‣ (any project) kanban view
   :shows: Kanban column header with the gear icon clicked and its dropdown open (Fold, Edit,
      Automations, Archive All, Unarchive All, Delete).
   :highlight: The "Fold" entry.
   :data: Demo project "Office Design".
   :module: project
   :notes: English UI, crop to the column header and dropdown.

.. important::
   Manually folding a stage from the Kanban view is temporary and does **not** close the cards in
   the stage.

Assign stages to projects or teams
==================================

Depending on the app, a stage can be limited to specific pipelines:

- In the **Project** app, make a selection in the :guilabel:`Projects` field on the task stage form.
  More than one project may be selected, since the same stage can be shared by multiple projects.
- In the **CRM** app, select a :guilabel:`Sales Team` on the stage form. If the field is left empty,
  the stage is available for all sales teams.

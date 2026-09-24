=================
Project templates
=================

**Project templates** store the setup you repeat on every similar project: the stages, the tags,
the starting tasks, and whether timesheets and billing are allowed. Creating a project from a
template applies all of it at once.

.. note::
   This feature is provided by the *Project Template* (`eyssen_project_template`) module.

.. _project/templates:

Creating a template
===================

Go to :menuselection:`Project --> Configuration --> Project Templates` and click :guilabel:`New`.
Give the template a unique :guilabel:`Name`, then fill in:

:guilabel:`Stages`
   - :guilabel:`Add Existing Stages` – pick task stages that already exist in the database.
   - :guilabel:`Create New Stages` – type the stage names to be created, separated by commas, for
     example `New, In Progress, Paused|, Testing, Closed|`. A name that ends with a `|` character
     creates a **folded** stage in the Kanban view.

:guilabel:`More`
   - :guilabel:`Timesheets` and :guilabel:`Billable` – the corresponding project settings.
   - :guilabel:`Tags` – project tags to apply.
   - :guilabel:`Tasks` – the tasks to create in the new project, **one per line**.
   - :guilabel:`Add Existing Categories` – the :doc:`project categories <categories>` to apply, and
     with them the optional features of the project.
   - :guilabel:`Company` – in a multi-company database, the company the template belongs to.

The :guilabel:`sequence` handle in the template list controls the order in which the templates are
offered.

.. screenshot:: services-project-template-form
   :menu: Project ‣ Configuration ‣ Project Templates
   :shows: A project template form named "Field service intervention", with existing stages selected, a comma-separated new-stage list, Timesheets and Billable enabled, tags, and three task lines.
   :highlight: The "Create New Stages" and "Tasks" fields (red frame).
   :data: Template "Field service intervention"; stages "New, On site|, Invoiced|"; tasks "Site survey", "Intervention", "Handover".
   :module: eyssen_project_template, eyssen_project_category
   :notes: English UI, light theme, 1440px width, crop to the form sheet.

Creating a project from a template
==================================

Create the project as usual and select the :guilabel:`Template` on the project form. When the
project is saved, Odoo applies the template:

- the existing stages and the newly created stages are added to the project, in the order given;
- the tags and the categories of the template are copied onto the project;
- the tasks listed in the template are created, in the order they appear;
- the :guilabel:`Timesheets` and :guilabel:`Billable` settings are applied.

.. important::
   The template is applied **when the project is created**. Changing the template on an existing
   project, or editing a template afterwards, does not modify projects that already exist.

.. screenshot:: services-project-template-selection
   :menu: Project ‣ Projects ‣ New
   :shows: A new project form with the Template field set to "Field service intervention".
   :highlight: The Template field (red frame).
   :data: Project "Boiler maintenance 2026".
   :module: eyssen_project_template
   :notes: English UI, light theme, 1440px width, crop to the project settings.

.. seealso::
   - :doc:`categories`
   - :doc:`project_management`

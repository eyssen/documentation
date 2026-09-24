==================
Project categories
==================

**Project categories** classify your projects and, at the same time, switch on the optional
features of a project. A category is a colored tag that carries a set of options; every project
that uses the category inherits those options, and so do its tasks.

.. note::
   This feature is provided by the *Project Category* (`eyssen_project_category`) module. The
   individual options only appear when the module that implements them is installed.

.. _project/categories:

Creating a category
===================

Go to :menuselection:`Project --> Configuration --> Project Category` and click :guilabel:`New`.
Fill in the :guilabel:`Project Category` name, pick a :guilabel:`Color`, and set the options you
want the category to enable:

.. list-table::
   :header-rows: 1
   :widths: 25 45 30

   * - Option
     - What it adds to the projects and tasks
     - Module
   * - :guilabel:`Field Service`
     - The intervention :guilabel:`Location` on the task.
     - `eyssen_project_fsm`
   * - :guilabel:`Worksheet`
     - The :guilabel:`Sign Report` and :guilabel:`Print` buttons, and the quotation creation.
     - `eyssen_project_worksheet`
   * - :guilabel:`Product`
     - The :guilabel:`Products` tab on the task.
     - `eyssen_project_product`
   * - :guilabel:`SLA`
     - The :doc:`SLA policies <sla>` and the :guilabel:`SLAs` tab on the task.
     - `eyssen_project_sla`

Category names must be unique. Categories you no longer use can be archived instead of deleted, so
that existing projects keep their history.

.. screenshot:: services-project-category-list
   :menu: Project ‣ Configuration ‣ Project Category
   :shows: The project category list in edit mode with three categories ("Field Service", "Support", "Internal") and the option checkbox columns.
   :highlight: The option checkbox columns (red frame).
   :data: Demo company "YourCompany HU"; categories "Field Service" (Field Service, Worksheet, Product ticked), "Support" (SLA ticked), "Internal" (none ticked).
   :module: eyssen_project_category, eyssen_project_fsm, eyssen_project_worksheet, eyssen_project_product, eyssen_project_sla
   :notes: English UI, light theme, 1440px width, crop to the list.

Using categories on projects
============================

Open a project and add one or more categories in the :guilabel:`Categories` field of the project
settings. The categories are then displayed:

- on the project cards in Kanban view and as a column in the project list;
- in the search panel of the project list, where :guilabel:`Category` is available both as a filter
  field and as a grouping;
- on every task of the project, as a read-only field.

A project takes on a feature as soon as **at least one** of its categories enables it, so features
can be combined by adding several categories.

.. tip::
   Add the categories to a :ref:`project template <project/templates>` so that new projects are
   created with the right features already switched on.

.. _project/task-pricelist:

Pricelist on tasks
==================

Installing *Project Category* also adds a :guilabel:`Pricelist` field, with its
:guilabel:`Currency`, to project tasks. When a :guilabel:`Customer` is selected, the customer's
pricelist is filled in automatically; it can be changed manually afterwards. Tasks that are
:guilabel:`Done` or :guilabel:`Canceled` keep the pricelist they had.

The pricelist determines the prices of the :ref:`products used on the task
<field_service/products-tab>` and the currency of the quotation created from it.

.. seealso::
   - :doc:`templates`
   - :doc:`sla`
   - :doc:`../field_service/configuration`

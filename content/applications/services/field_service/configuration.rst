=============
Configuration
=============

Field Service is switched on per project by assigning it a :ref:`project category
<project/categories>` that has the field service options enabled. This keeps ordinary projects
untouched while intervention projects get the extra fields, tabs, and buttons.

.. _field_service/category:

Enabling field service on a category
====================================

Go to :menuselection:`Project --> Configuration --> Project Category`, open a category (or create
one), and tick the options you need:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Option
     - Effect on the tasks of every project using this category
   * - :guilabel:`Field Service`
     - Adds the mandatory :guilabel:`Location` field on the task, so the technician knows where the
       intervention takes place.
   * - :guilabel:`Worksheet`
     - Adds the :guilabel:`Sign Report` and :guilabel:`Print` buttons and the
       :guilabel:`Quotations/Orders` smart button to the task.
   * - :guilabel:`Product`
     - Adds the :guilabel:`Products` tab, where the materials used during the intervention are
       recorded.
   * - :guilabel:`SLA`
     - Applies the :doc:`SLA policies <../project/sla>` of the project to the tasks.

.. screenshot:: services-field-service-category-options
   :menu: Project ‣ Configuration ‣ Project Category
   :shows: The form (list row in edit mode) of a project category named "Field Service", with the Field Service, Worksheet and Product checkboxes ticked.
   :highlight: The Field Service, Worksheet and Product checkboxes (red frame).
   :data: Demo company; categories "Field Service", "Internal", "Support".
   :module: eyssen_project_category, eyssen_project_fsm, eyssen_project_worksheet, eyssen_project_product
   :notes: English UI, light theme, 1440px width, crop to the category row.

.. note::
   The options only appear if the corresponding module is installed. Use the
   :guilabel:`Field Services` filter in the search bar of the category list to find the categories
   that already act as field service categories.

.. _field_service/project:

Assigning the category to a project
===================================

Open a project, and in the :guilabel:`Categories` field add the field service category. A project
can carry several categories; the field service behavior is activated as soon as **one** of them
has the corresponding option.

The categories are also shown on the project cards in Kanban view and in the project list, and the
search panel offers a :guilabel:`Category` filter and grouping.

.. tip::
   To create intervention projects that are always configured the same way, add the category to a
   :ref:`project template <project/templates>`. Projects created from that template receive the
   category, the stages, the tags, and the starting tasks automatically.

.. screenshot:: services-field-service-project-categories
   :menu: Project ‣ Projects ‣ (open a project) ‣ Settings
   :shows: The project settings form with the "Categories" tag field filled with the "Field Service" tag.
   :highlight: The Categories field (red frame).
   :data: Project "Boiler maintenance 2026" with category "Field Service".
   :module: eyssen_project_category
   :notes: English UI, light theme, 1440px width, crop to the top of the settings tab.

.. seealso::
   - :doc:`../project/categories`
   - :doc:`../project/templates`

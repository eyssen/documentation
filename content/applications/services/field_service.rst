:nosearch:
:show-content:
:hide-page-toc:
:show-toc:

=============
Field Service
=============

**Field Service** covers the work your technicians perform at the customer's premises: the
intervention is prepared in the office, carried out and documented on site, and then billed.

In this database, Field Service is not a separate application. It is a working mode of the
:doc:`Project <project>` app, enabled per project through :ref:`project categories
<project/categories>`. A project whose category has the :guilabel:`Field Service` flag gains an
intervention :guilabel:`Location`, and the categories that add :guilabel:`Worksheet` and
:guilabel:`Product` turn its tasks into full intervention sheets that can be printed, signed by the
customer, and turned into a quotation.

.. note::
   The features described in this section require the *Project Field Service*
   (`eyssen_project_fsm`), *Project Worksheet* (`eyssen_project_worksheet`) and *Project Product*
   (`eyssen_project_product`) modules, which all build on *Project Category*
   (`eyssen_project_category`).

.. toctree::
   :titlesonly:

   field_service/configuration
   field_service/creating_tasks
   field_service/product_management
   field_service/worksheets

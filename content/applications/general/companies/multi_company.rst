=============
Multi-company
=============

.. seealso::
   :ref:`Branches <general/companies/branches>`

.. |mcd| replace:: multi-company database

In Odoo, multiple companies can be configured under one database. This allows some data to be shared
among companies while maintaining some separation between entities.

A centralized management environment allows authorized users to select multiple companies
simultaneously and set their specific warehouses, customers, equipment, and contacts. It also
generates reports of aggregated figures without switching interfaces, facilitating daily tasks and
enhancing the overall management process.

.. _general/multi-company/configuration:

Configuration
=============

Open the Settings app, navigate to the :guilabel:`Companies` section, and click
:icon:`oi-arrow-right` :guilabel:`Manage Companies`. Then, click :guilabel:`New` and :ref:`fill in
the form with the company's information <general/companies/company>` or select an existing company
to edit it.

.. note::
   Alternatively, it is possible to create a company by going to :menuselection:`Settings --> Users
   & Companies --> Companies`.

.. tip::
   To archive a company, follow these steps:

   #. In the Settings app, navigate to the :guilabel:`Companies` section and click
      :icon:`oi-arrow-right` :guilabel:`Manage Companies`.
   #. In the :guilabel:`Companies` list view, select the company to be archived.
   #. Click the :icon:`fa-cog` :guilabel:`Actions` menu and select :guilabel:`Archive`.
   #. Click :guilabel:`Archive` to confirm.

.. _general/multi-company/multi-company-environment:

Multi-company environment
=========================

In a multi-company environment, users are granted :ref:`access to one or more companies
<general/multi-company/user-access>`, and :ref:`data
<general/multi-company/shared-and-unshared-records>` is created or modified based on its intended
use within that structure.

.. _general/multi-company/user-access:

User access
-----------

A multi-company environment allows flexible control over :ref:`user access <users/multi-companies>`
and :doc:`access rights <../users/access_rights>` that can be granted or restricted as needed.

.. _general/multi-company/company-selector:

Company selector
----------------

To switch between (or select) multiple companies, follow these steps:

#. Click the company selector in the top-right corner of the header menu.
#. In the drop-down list, select the checkboxes next to the desired companies.
#. The highlighted company indicates the current active environment.
#. To switch to another company, click its name in the list of selected companies.

.. example::
   In the example below, the user can access six companies, two of which are selected. The current
   active company is *My Company (San Francisco)*.

   .. screenshot:: general-multi-company-selector
      :menu: Top menu bar ‣ company selector
      :shows: The company selector dropdown with six companies, two of them ticked, and the active
         company "My Company (San Francisco)" highlighted.
      :highlight: The ticked companies and the active company.
      :data: Six demo companies, including "My Company (San Francisco)" and "My Company (Chicago)".
      :module: base
      :notes: English UI, crop to the top bar and dropdown.

.. _general/multi-company/shared-and-unshared-records:

Shared and company-specific records
-----------------------------------

Data, such as products, contacts, and equipment can either be shared across companies or restricted
to a specific company by setting the :guilabel:`Company` field on the relevant records:

- either leave the field blank to make it accessible to all companies;
- or select the company to make it visible to users logged in to that specific company.

Records specifically linked to a particular company are accessible only within that entity. For
instance, quotations, invoices, and vendor bills associated with a company are visible only when
logged into that company, and the corresponding company is automatically selected by default and
displayed in the :guilabel:`Company` field.

In a |mcd|, new products and contacts are shared across companies by default. To restrict them to a
specific company, set the :guilabel:`Company` field on the record's form.

.. _general/multi-company/use-cases:

Use cases
=========

.. _general/multi-company/use-cases-multinational-companies:

Multinational companies
-----------------------

A multinational retail chain operating in the United States and Canada must manage transactions in
USD and CAD.

Since each country has its own tax laws and regulations, using Odoo’s multi-company feature is
highly beneficial.

This setup keeps the accounting of each company separate while sharing products and contacts. It
also simplifies the sales process by enabling customers transactions in their local currency.

.. _general/multi-company/use-cases-seperate-processes:

Separate processes
------------------

A small furniture company is launching a new product line that requires separate procurement,
inventory, and manufacturing workflows. These new products differ significantly from the existing
catalog. To manage this efficiently, the company is considering using the multi-company feature to
manage the new line as a separate business entity.

However, creating a completely new company might add unnecessary complexity to the database.
Instead, the company can leverage existing features such as :doc:`analytic accounting
<../../finance/accounting/reporting/analytic_accounting>` and multiple warehouses to manage the new
product line without complicating overall operations.

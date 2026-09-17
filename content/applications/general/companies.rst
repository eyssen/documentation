:show-content:

=========
Companies
=========

In Odoo, a company is an individual business entity that operates independently, with its own legal
identity, financial records, and specific operational settings.

.. seealso::
   - :ref:`general/companies/branches`
   - :doc:`Multi-company <companies/multi_company>`

.. _general/companies/configuration:

Configuration
=============

To set up a company, follow these steps:

#. :ref:`Configure the company details <general/companies/company>`.
#. :ref:`Manage users and their access rights <general/companies/users>`.
#. :ref:`Customize the document layout <general/companies/document-layout>`.

.. _general/companies/company:

Company
-------

To create a company, open the Settings app, navigate to the :guilabel:`Companies` section, and click
:icon:`oi-arrow-right` :guilabel:`Manage Companies`. In the :guilabel:`Companies` list view, click
:guilabel:`New` and configure the following fields:

- :guilabel:`Company Name`
- :guilabel:`Address`
- :guilabel:`Tax ID`: tax identification number.
- :guilabel:`Company ID`: company's registry number, if different from :guilabel:`Tax ID`
- :ref:`Currency <multi-currency/config-main-currency>`
- :guilabel:`Phone` and :guilabel:`Mobile`
- :guilabel:`Email`
- :guilabel:`Website`
- :guilabel:`Email Domain`
- :guilabel:`Color`

Upload the company's logo and :guilabel:`Save`.

.. note::
   - Alternatively, it is possible to create a company by going to :menuselection:`Settings -->
     Users & Companies --> Companies`.
   - The company's :guilabel:`General information` may vary based on the :doc:`fiscal localization
     <../finance/fiscal_localizations>`.

.. _general/companies/users:

Users
-----

After setting up a company, add :doc:`users <users>` and configure their :ref:`access
<users/add-individual>` and :doc:`access rights <users/access_rights>`.

.. seealso::
   :ref:`Users in multi-company environment <users/multi-companies>`

.. _general/companies/document-layout:

Document layout
---------------

Configure the default layout of the company's printed and PDF documents (quotations, invoices,
delivery slips, etc.). Go to :menuselection:`Settings`, then, in the :guilabel:`Companies` section,
click :guilabel:`Configure Document Layout`. Layout settings are company-specific, but apply to all
reports of that company.

.. tip::
   The preview on the right side of the :guilabel:`Configure your document layout` window shows how
   the settings affect the documents.

The following settings are available:

- :guilabel:`Layout`: :guilabel:`Light`, :guilabel:`Boxed`, :guilabel:`Bold`, :guilabel:`Striped`,
  :guilabel:`Bubble`, :guilabel:`Wave`, or :guilabel:`Folder`.
- :guilabel:`Background`: :guilabel:`Blank`, :guilabel:`Demo logo`, or :guilabel:`Custom`, to
  upload a custom background image.
- :guilabel:`Text`: the font used in the documents: Lato, Roboto, Open Sans, Montserrat, Oswald,
  Raleway, Tajawal (which supports Arabic and Latin scripts), or Fira Mono.
- :guilabel:`Logo`: upload or change the company logo. The logo is also saved on the company record.
- :guilabel:`Colors`: the primary and secondary colors used to structure the documents. By default,
  they are generated from the colors of the logo.
- :guilabel:`Address`: the company details displayed in the header of the documents. Multiple lines
  of text can be added.
- :guilabel:`Tagline`: displayed in the header (Light, Striped, Bubble, Wave, and Folder layouts) or
  in the footer (Boxed and Bold layouts) of the documents.
- :guilabel:`Footer`: the text displayed at the bottom of the documents, e.g., bank account details.
- :guilabel:`Paper format`: the default paper size, e.g., :guilabel:`A4` or :guilabel:`US Letter`.
  Other paper formats may be available depending on the installed apps, e.g., label sheets.

Click :guilabel:`Continue` to save the settings.

.. screenshot:: general-companies-document-layout
   :menu: Settings ‣ General Settings ‣ Companies ‣ Configure Document Layout
   :shows: The "Configure your document layout" dialog: Layout, Background, Text, Logo,
      Colors, Address, Tagline, Footer and Paper format settings on the left, and the live document
      preview on the right.
   :highlight: The Layout selector and the preview.
   :data: Company "YourCompany HU" with logo; layout "Light"; A4 paper format.
   :module: web, base_setup
   :notes: English UI, 1440px width, crop to the dialog.

.. _general/companies/branches:

Branches
========

Branches represent subdivisions within a company, such as regional offices or departments, that
operate under a common parent company. They support hierarchical company structures through
:ref:`configurable settings <general/companies/branches/configuration>`, enabling
:ref:`comprehensive or branch-specific views <general/companies/branches/consolidated-view>` with
flexible :ref:`access control <general/companies/branches/user-access>`, :ref:`entity-specific or
shared record visibility <general/companies/branches/shared-records>`, and customizable
:ref:`reporting <general/companies/branches/reporting>`.

.. note::
   Independent subsidiaries should be created as additional companies, not branches.

.. seealso::
   - :doc:`Multi-company </applications/general/companies/multi_company>`
   - :ref:`Branch accounting <accounting/branches>`

.. _general/companies/branches/configuration:

Configuration
-------------

Each branch is linked to its parent company but may contain different or specific information, such
as its address or logo. A branch can be a parent company of branches at a lower level to create a
multi-level architecture.

.. important::
   - Clarify the company's structure and hierarchy before creating companies and branches in Odoo. A
     company defined as a parent cannot be converted into a branch later, as doing so may result in
     :doc:`access rights <users/access_rights>` issues.
   - Always create the parent company first.

To create a branch, follow these steps in the Settings app:

#. Navigate to the :guilabel:`Companies` section, click :icon:`oi-arrow-right` :guilabel:`Manage
   Companies`, or go to :menuselection:`Settings --> Users & Companies --> Companies`.
#. In the :guilabel:`Companies` list view, open the desired parent company form.
#. In the :guilabel:`Branches` tab, click :guilabel:`Add a line` and fill in the :ref:`General
   Information <general/companies/company>` fields in the :guilabel:`Create Branches` window.

To create branches from a branch and create a multi-level architecture, click :guilabel:`Add a line`
in the new branch's :guilabel:`Branches` tab.

.. tip::
   Activate the :ref:`developer mode <developer-mode>` to set :doc:`social media accounts
   <../marketing/social_marketing>` and company-specific :doc:`email <email_communication>` system
   parameters.

.. warning::
   Adding a branch to a company enables :doc:`multi-company <companies/multi_company>` functions.

.. _general/companies/branches/consolidated-view:

Comprehensive or branch-specific view
-------------------------------------

.. note::
   Selecting the parent company automatically links all its branches, while selecting a branch
   connects to that branch only. To switch between them, use the :ref:`company selector
   <general/multi-company/company-selector>`.

All configurations, except for :ref:`accounting <accounting/branches>` settings inherited from the
parent company, must be set individually per branch. This allows for branch-specific setups such as
:doc:`loyalty programs <../sales/point_of_sale/pricing/loyalty>`, :doc:`price lists
<../sales/point_of_sale/pricing/pricelists>`, or :doc:`inventory locations
<../inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_locations>`.

.. _general/companies/branches/user-access:

User access
~~~~~~~~~~~

Like in a multi-company environment, parent companies and branches support flexible :ref:`user
access <users/multi-companies>` control and :doc:`access rights <users/access_rights>`. User access
can be granted or restricted at the parent company level, the branch level, or both. For example, a
user can be limited to a specific branch, while an administrator with access to the parent company
can manage all associated branches.

.. _general/companies/branches/shared-records:

Shared records
~~~~~~~~~~~~~~

In Odoo, some records are, by default, either specific to a single entity or shared across the
parent company and all its branches.

When creating a quotation, invoice, or vendor bill, the active company or branch is automatically
selected and displayed in the :guilabel:`Company` field. If the active company is the parent company
or one of its branches, then records specifically linked to that entity are accessible only within
that entity and will only be visible when the company or branch is selected using the :ref:`company
selector <general/multi-company/company-selector>`.

In contrast, some records, such as :ref:`products or contacts
<general/multi-company/shared-and-unshared-records>`, are not tied to any particular entity and are
shared by default across the parent company and all its branches. However, they can be restricted to
a single entity by setting the appropriate value in the :guilabel:`Company` field, if needed.

.. seealso::
   :ref:`Branches accounting <accounting/branches>`

.. _general/companies/branches/reporting:

Reporting
~~~~~~~~~

All :doc:`reports <../finance/accounting/reporting>` can be generated for the parent company alone
or with its branches, based on :ref:`user access <general/multi-company/user-access>`.

.. toctree::
   :titlesonly:

   companies/multi_company
   companies/digest_emails
   companies/email_template

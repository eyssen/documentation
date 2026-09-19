===============
Process numbers
===============

A **process number** is a case identifier shared by all the documents that belong to the same
business matter: the opportunity, the quotation, the purchase orders, the transfers, the invoices,
the project, and its tasks. Once the documents carry the same process number, the whole history of
a case can be found from a single record, whatever application the documents were created in.

The feature is made of a base module, *Process Number* (`process_number`), and one optional bridge
module per application.

.. _process-numbers/configuration:

Configuration
=============

Go to :menuselection:`Settings --> eYssen ERP`, and, in the :guilabel:`Process Number` section,
enable :guilabel:`Process Number`. Then, tick the applications in which process numbers are to be
used, and click :guilabel:`Save`:

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Option
     - Module
     - Documentation
   * - :guilabel:`CRM`
     - `process_number_crm`
     - :ref:`Leads and opportunities <process-numbers/crm>`
   * - :guilabel:`Sale`
     - `process_number_sale`
     - :doc:`Sales order extensions <../sales/sales/order_extensions>`
   * - :guilabel:`Purchase`
     - `process_number_purchase`
     - :doc:`Requests for quotation <../inventory_and_mrp/purchase/manage_deals/rfq>`
   * - :guilabel:`Stock`
     - `process_number_stock`
     - :doc:`Stock helpers <../inventory_and_mrp/inventory/product_management/stock_helpers>`
   * - :guilabel:`Invoicing`
     - `process_number_account`
     - :ref:`Invoices and bills <process-numbers/invoicing>`
   * - :guilabel:`Project`
     - `process_number_project`
     - :doc:`Process numbers in Project <../services/project/process_numbers>`

.. screenshot:: general-process-numbers-settings
   :menu: Settings ‣ eYssen ERP
   :shows: The "Process Number" section of the eYssen ERP settings with the "Process Number" option enabled, the six application checkboxes below it, and the "Create Automatically" checkbox under CRM.
   :highlight: The "Process Number" setting block (red frame).
   :module: eyssen_base, process_number, process_number_crm
   :notes: English UI, light theme, 1440px width, crop to the section.

.. _process-numbers/manage:

Manage process numbers
======================

The :guilabel:`Process Numbers` application lists all the process numbers of the current company.
All internal users can create and edit them.

Click :guilabel:`New` to create a process number. The number itself is assigned automatically from
the *Process Number* sequence (by default `PN/<year>/<5-digit counter>`, e.g., `PN/2026/00042`) and
cannot be modified. It is unique per company. Optionally, fill in:

- :guilabel:`Assignees`: the users in charge of the case;
- :guilabel:`Description`: a rich-text description of the case. Several users can edit it at the
  same time, and its previous versions are kept in the history of the field.

The chatter of the process number can be used to discuss the case and to schedule activities; the
activities are also displayed in the list and in the activity view. A closed case can be archived
with the :menuselection:`Action --> Archive` menu.

Each installed bridge module adds to the process number form a smart button with the number of
linked documents, and the list of these documents. The same documents are shown as tags in the list
view of the process numbers.

.. tip::
   The prefix and the padding of the numbers can be changed in :ref:`developer mode
   <developer-mode>` from :menuselection:`Settings --> Technical --> Sequences & Identifiers -->
   Sequences`, on the *Process Number* sequence.

.. note::
   - A number is reserved as soon as the creation form is opened. Discarding the form therefore
     leaves a gap in the numbering.
   - The cost summary table displayed at the top of the form (planned cost, actual cost,
     readiness) is a placeholder: it is not filled in yet.

.. screenshot:: general-process-numbers-form
   :menu: Process Numbers ‣ (open a process number)
   :shows: A process number form with the smart buttons of the installed bridge modules (CRM Leads, In Invoices, Out Invoices, Projects, Tasks), the number in the title, the lists of linked documents and the Description tab.
   :highlight: The row of smart buttons (red frame).
   :data: Process number "PN/2026/00042" linked to one opportunity, two vendor bills and one customer invoice.
   :module: process_number, process_number_crm, process_number_account
   :notes: English UI, light theme, 1440px width.

Link a document to a process number
-----------------------------------

On the documents of the applications for which a bridge module is installed, the
:guilabel:`Process Number` field is displayed above the title of the form. Either select an
existing process number, or, as long as the field is empty, click :guilabel:`Create a new process
number` in the yellow banner to generate a new one and link it to the document in one step.

Changes of the process number are logged in the chatter of the document.

.. _process-numbers/crm:

Leads and opportunities
=======================

With the *Process Number - CRM* module (`process_number_crm`), the :guilabel:`Process Number` field
is available on leads and opportunities: on the form, as a column of the list view, and on the
Kanban cards of the pipeline.

To get a process number for every new lead or opportunity, go to :menuselection:`Settings -->
eYssen ERP`, and, in the :guilabel:`Process Number` section, tick :guilabel:`Create Automatically`
under the :guilabel:`CRM` option. The setting is company-specific. A lead created without a company
gets a number as soon as the option is enabled in at least one company. Leads that already have a
process number, e.g., one selected on the creation form, keep it.

On the process number, the :guilabel:`CRM Leads` smart button opens the linked opportunities in the
pipeline, and the :guilabel:`CRM Leads` list shows their name, salesperson, expected revenue, and
stage.

.. screenshot:: general-process-numbers-crm-lead
   :menu: CRM ‣ (open an opportunity without a process number)
   :shows: The top of an opportunity form with the empty "Process Number" field and the yellow banner "Create a new process number or select an existing one!" above the opportunity name.
   :highlight: The "Create a new process number" link (red frame).
   :data: Opportunity "Office furniture for Deco Addict".
   :module: process_number_crm
   :notes: English UI, light theme, 1440px width, crop to the upper half of the form.

.. _process-numbers/invoicing:

Invoices and bills
==================

With the *Process Number - Account* module (`process_number_account`), the :guilabel:`Process
Number` field is available on all journal entries: customer invoices, credit notes, vendor bills,
and refunds. It is also added as the first column of the customer invoices list.

On the process number, two smart buttons and two lists separate the documents:

- :guilabel:`In Invoices`: the vendor bills and vendor refunds of the case;
- :guilabel:`Out Invoices`: the customer invoices and credit notes of the case.

.. note::
   The process number of a sales order is not copied to its invoices automatically; select it on
   the invoice.

.. seealso::
   - :doc:`../services/project/process_numbers`
   - :doc:`eyssen_erp_settings`

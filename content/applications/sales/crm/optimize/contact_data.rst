=========================
Customer and company data
=========================

Two eYssen modules extend what the database records about a contact: *eYssen Partner*
(``eyssen_partner``) adds company background and a VAT re-check, and *Partner Group Category*
(``partner_group_category``) adds a hierarchical grouping that also becomes a reporting dimension.

Customer and supplier flags
===========================

*eYssen Partner* adds two explicit checkboxes on the contact form: :guilabel:`Customer` and
:guilabel:`Supplier`. They make the role of a contact a deliberate choice rather than something
inferred from its documents, and they drive the :guilabel:`Customers` and :guilabel:`Suppliers`
filters on the contact list.

The :guilabel:`Sales` and :guilabel:`Purchase` groups of the contact form are hidden while the
matching checkbox is off, so a supplier form is not cluttered with sales fields.

VIES re-check
=============

Next to the VAT number, a :guilabel:`Recheck VIES` button re-validates the number against the EU VIES
service on demand, and a read-only :guilabel:`Last VIES Check` field records when that last happened.

.. note::
   The button only appears when VIES validation is enabled for the company, in
   :menuselection:`Settings --> Accounting --> Verify VAT Numbers`.

.. screenshot:: sales-crm-contact-vies
   :menu: Contacts ‣ (a company contact)
   :shows: The top of a company contact form with the VAT field, the "Recheck VIES" button and the "Last VIES Check" timestamp, and the Customer / Supplier checkboxes.
   :highlight: The "Recheck VIES" button and the Customer/Supplier checkboxes (red frames).
   :data: Company "Deco Addict" with a valid EU VAT number.
   :module: eyssen_partner
   :notes: English UI, light theme, 1440px width, crop to the contact header.

Business Info tab
=================

A :guilabel:`Business Info` tab collects the company background that sales uses to qualify an
account:

- :guilabel:`Company Profile`: :guilabel:`Year of Foundation`, :guilabel:`Number of Employees` and
  the :guilabel:`Risk Rating`, which has four levels — :guilabel:`Minimal risk`, :guilabel:`Below
  average risk`, :guilabel:`Above average risk` and :guilabel:`High risk`.
- :guilabel:`Financials`: the :guilabel:`Yearly Revenue` and the :guilabel:`Registered Capital`.

.. screenshot:: sales-crm-contact-business-info
   :menu: Contacts ‣ (a company contact) ‣ Business Info
   :shows: The Business Info tab with the Company Profile group (year of foundation, number of employees, risk rating) and the Financials group (yearly revenue, registered capital).
   :highlight: The Risk Rating field (red frame).
   :data: Company "Deco Addict"; founded 2005, 45 employees, risk rating "Below average risk".
   :module: eyssen_partner
   :notes: English UI, light theme, 1440px width, crop to the notebook.

Partner group categories
========================

A **group category** puts contacts into a tree — for example by segment, by chain or by industry —
and carries that grouping onto the documents they generate.

Maintain the tree in :menuselection:`Contacts app --> Configuration --> Partner Group Categories`.
Each category has a :guilabel:`Name` and an optional :guilabel:`Parent Category`; the computed
:guilabel:`Complete Name` shows the full path.

Set the :guilabel:`Group Category` field on the contact. It is then copied onto every sales order
and customer invoice of that contact, where it can be used as a filter and a grouping — and, most
usefully, as a dimension in the **Sales Analysis** and **Invoice Analysis** reports.

.. example::
   With the categories `Retail / Furniture chains` and `Retail / Independent shops`, the Sales
   Analysis report grouped by :guilabel:`Group Category` shows the revenue of each segment, and
   collapsing to the parent gives the whole `Retail` segment.

.. screenshot:: sales-crm-group-category-report
   :menu: Sales ‣ Reporting ‣ Sales
   :shows: The Sales Analysis report grouped by "Group Category", showing the parent categories with their child categories underneath.
   :highlight: The "Group Category" grouping facet (red frame).
   :data: Two parent categories with two children each.
   :module: partner_group_category
   :notes: English UI, light theme, 1440px width, crop to the search bar and the table.

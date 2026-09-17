================================
Convert leads into opportunities
================================

*Leads* act as a qualifying step before an opportunity is created. This provides additional time to
review its potential, and gauge its viability, before the opportunity is assigned to a salesperson.

Configuration
=============

To activate the *Leads* setting, navigate to :menuselection:`CRM app --> Configuration --> Settings`
and check the box labeled, :guilabel:`Leads`. Then, click :guilabel:`Save`.

.. screenshot:: sales-crm-convert-leads-setting
   :menu: CRM ‣ Configuration ‣ Settings
   :shows: The CRM settings with the "Leads" checkbox enabled in the CRM section.
   :highlight: The "Leads" setting (red frame).
   :data: Demo company.
   :module: crm
   :notes: English UI, light theme, 1440px width, crop to the setting block.

Activating this feature adds a new menu option, :guilabel:`Leads`, to the header bar, located along
the top of the screen.

.. screenshot:: sales-crm-convert-leads-menu
   :menu: CRM ‣ Leads
   :shows: The CRM menu bar with the Leads menu visible after the setting was enabled.
   :highlight: The Leads menu (red frame).
   :data: Demo database.
   :module: crm
   :notes: English UI, light theme, 1440px width, crop to the menu bar.

Once the *Leads* setting has been activated, it applies to all sales teams by default. To turn off
leads for a specific team, navigate to :menuselection:`CRM app --> Configuration --> Sales Teams`.
Then, select a team from the list to open that team's configuration page. Clear the
:guilabel:`Leads` checkbox, located beneath the :guilabel:`Sales Team` field, then click
:guilabel:`Save`.

.. screenshot:: sales-crm-convert-team-leads-button
   :menu: CRM ‣ Configuration ‣ Sales Teams ‣ (a team)
   :shows: A sales-team form with the Leads smart button in the button box.
   :highlight: The Leads smart button (red frame).
   :data: Sales team "Europe".
   :module: crm
   :notes: English UI, light theme, 1440px width, crop to the button box.

Convert a lead into an opportunity
==================================

To convert a lead into an *opportunity*, navigate to :menuselection:`CRM app --> Leads`, and click
on a lead from the list to open it.

.. warning::
   If a :guilabel:`Similar Leads` smart button appears at the top of the page for the lead, it
   indicates a similar lead or opportunity already exists in the database. Before converting this
   lead, click the smart button to confirm if the lead should be merged.

   .. screenshot:: sales-crm-convert-similar-leads-button
      :menu: CRM ‣ Leads ‣ Leads ‣ (a lead)
      :shows: A lead form with the "Similar Leads" smart button showing the number of matching records.
      :highlight: The "Similar Leads" smart button (red frame).
      :data: Lead "Interest in office chairs", 2 similar leads.
      :module: crm
      :notes: English UI, light theme, 1440px width, crop to the button box.

Click the :guilabel:`Convert to Opportunity` button, located at the top-left of the page.

.. screenshot:: sales-crm-convert-button
   :menu: CRM ‣ Leads ‣ Leads ‣ (a lead)
   :shows: The header of a lead form with the "Convert to Opportunity" button.
   :highlight: The "Convert to Opportunity" button (red frame).
   :data: Same lead.
   :module: crm
   :notes: English UI, light theme, 1440px width, crop to the header.

This opens a :guilabel:`Convert to opportunity` pop-up modal. Here, in the :guilabel:`Conversion
Action` field, select the :guilabel:`Convert to opportunity` option.

.. note::
   To merge this lead with an existing similar lead or opportunity, select :guilabel:`Merge with
   existing opportunities` in the :guilabel:`Conversion Action` field. This generates a list of the
   similar leads/opportunities to be merged.

   When merging, Odoo gives priority to whichever lead/opportunity was created in the system first,
   merging the information into the first created lead/opportunity. However, if a lead and an
   opportunity are being merged, the resulting record is referred to as an opportunity, regardless
   of which record was created first.

Then, select a :guilabel:`Salesperson` and a :guilabel:`Sales Team` to which the opportunity should
be assigned. Neither field is required, though if a selection is made in the :guilabel:`Salesperson`
field, the :guilabel:`Sales Team` field is populated automatically, based on the salesperson's team
assignments.

If the lead has already been assigned to a salesperson or a team, these fields automatically
populate with that information.

.. screenshot:: sales-crm-convert-popup
   :menu: CRM ‣ Leads ‣ Leads ‣ (a lead) ‣ Convert to Opportunity
   :shows: The "Convert to opportunity" pop-up with the Conversion Action options, the Salesperson and Sales Team fields and the customer options.
   :highlight: The Conversion Action options (red frame).
   :data: "Convert to opportunity" selected.
   :module: crm
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

Under the :guilabel:`Customer` heading, choose from the following options:

- :guilabel:`Create a new customer`: choose this option to use the information in the lead to create
  a new customer record.
- :guilabel:`Link to an existing customer`: choose this option, then select a customer from the
  resulting drop-down menu, to link this opportunity to an existing customer record.
- :guilabel:`Do not link to a customer`: choose this option to convert the lead, but not link it to
  a new or existing customer.

Lastly, when all configurations are complete, click :guilabel:`Create Opportunity`.

To view the newly created opportunity, navigate to :menuselection:`CRM app --> My Pipeline`.

.. note::
   Some filters may need to be removed from the :guilabel:`Search...` bar on the top
   :guilabel:`Pipeline` page to view all opportunities.


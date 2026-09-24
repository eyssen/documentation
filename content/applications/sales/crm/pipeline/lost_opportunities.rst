==================
Lost opportunities
==================

Not every opportunity results in a successful sale. To keep the pipeline up-to-date, *lost*
opportunities need to be identified. Specifying why an opportunity was lost helps identify recurring
issues, reveal coaching opportunities, and can assist with improving overall sales strategy.

.. note::
   :doc:`Merging lost opportunities <merge_similar>` with active ones will pull them back into the
   pipeline.

Mark an opportunity as lost
===========================

To mark an opportunity as lost, first open the :menuselection:`CRM app`, and then select an
opportunity from the pipeline by clicking on its corresponding Kanban card. Doing so reveals that
opportunity's detail form.

Then, click :guilabel:`Lost`, located at the top of the opportunity's detail form.

.. screenshot:: sales-crm-lost-button
   :menu: CRM ‣ Sales ‣ My Pipeline ‣ (an opportunity)
   :shows: The header of an opportunity form with the Lost button next to New Quotation and Won.
   :highlight: The Lost button (red frame).
   :data: Opportunity "Office furniture".
   :module: crm
   :notes: English UI, light theme, 1440px width, crop to the header.

This opens the :guilabel:`Mark Lost` pop-up window. From the :guilabel:`Lost Reason` drop-down menu,
choose an existing lost reason. If no applicable reason is available, then create a new one by
entering it into the :guilabel:`Lost Reason` field, and then clicking :guilabel:`Create`.

Additional notes and comments can be added below the lost reason in the designated
:guilabel:`Closing Note` field.

.. tip::
   Neither the :guilabel:`Lost Reason` field, nor the :guilabel:`Closing Note` field, on the
   :guilabel:`Mark Lost` pop-up window are required. However, it is recommended to include this
   information for the sake of traceability, accountability, and reporting purposes.

When all the desired information has been entered in the :guilabel:`Mark Lost` pop-up window, click
:guilabel:`Mark as Lost`.

.. screenshot:: sales-crm-lost-reason-popup
   :menu: CRM ‣ Sales ‣ My Pipeline ‣ (an opportunity) ‣ Lost
   :shows: The "Mark Lost" pop-up with the Lost Reason drop-down and the Closing Note field.
   :highlight: The Lost Reason drop-down (red frame).
   :data: Reasons "Too expensive", "Not enough stock".
   :module: crm
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

After clicking :guilabel:`Mark as Lost`, a red :guilabel:`Lost` banner is added to the upper-right
corner of the opportunity.

.. screenshot:: sales-crm-lost-banner
   :menu: CRM ‣ Sales ‣ My Pipeline ‣ (a lost opportunity)
   :shows: A lost opportunity with the red "Lost" ribbon and the lost reason shown on the form.
   :highlight: The "Lost" ribbon (red frame).
   :data: Opportunity marked lost for "Too expensive".
   :module: crm
   :notes: English UI, light theme, 1440px width, crop to the top of the form.

.. note::
   To mark an *inactive* (archived) opportunity as lost, set the :guilabel:`Probability` field to
   `0` percent.

.. _crm/lost-reasons:

Create/edit lost reasons
========================

To create a new lost reason, or edit an existing one, navigate to :menuselection:`CRM app -->
Configuration --> Lost Reasons`.

To edit an existing lost reason, click the reason to be edited to highlight it. From here, change
the selected lost reason by editing the :guilabel:`Description` field.

To create a new lost reason, click :guilabel:`New` in the upper-left corner of the :guilabel:`Lost
Reasons` page. Then, type the new lost reason in the :guilabel:`Description` field.

View lost opportunities
=======================

To retrieve lost opportunities, go :menuselection:`CRM app --> Sales --> My Pipeline`, then click on
the search bar at the top of the page, and then remove all of the default filters.

.. screenshot:: sales-crm-lost-filter
   :menu: CRM ‣ Sales ‣ My Pipeline
   :shows: The pipeline search bar with the "Lost" filter applied and the resulting records.
   :highlight: The "Lost" filter facet (red frame).
   :data: Three lost opportunities.
   :module: crm
   :notes: English UI, light theme, 1440px width, crop to the search bar and the first rows.

Open the :guilabel:`Filters` drop-down menu by clicking the :icon:`fa-caret-down`
:guilabel:`(dropdown)` icon to the right of the search bar to open the drop-down menu containing
:guilabel:`Filters`, :guilabel:`Group By`, and :guilabel:`Favorites` options, designated into
respective columns.

Select the :guilabel:`Lost` option from the :guilabel:`Filters` section. Upon selecting
:guilabel:`Lost`, only the opportunities marked as `Lost` appear on the :guilabel:`Pipeline` page.

Sort opportunities by lost reason
---------------------------------

To filter opportunities by a specific lost reason, click the :icon:`fa-caret-down`
:guilabel:`(dropdown)` icon to the right of the search bar again to open the drop-down menu. In
addition to the :guilabel:`Lost` filter, under the :guilabel:`Filters` column, click :guilabel:`Add
Custom Filter`, which opens an :guilabel:`Add Custom Filter` pop-up window.

On the :guilabel:`Add Custom Filter` pop-up window, click in the first field and type `Lost Reason`
in the search bar, or scroll to search through the list to locate it. Then, click into the next
field, and select :guilabel:`=` from the drop-down menu. Click into the third field, and then select
a lost reason from the drop-down menu. Finally, click :guilabel:`Add`.

.. screenshot:: sales-crm-lost-custom-filter
   :menu: CRM ‣ Sales ‣ My Pipeline ‣ Filters ‣ Add Custom Filter
   :shows: The search bar with a custom filter on the Lost Reason field applied alongside the Lost filter.
   :highlight: The custom filter facet (red frame).
   :data: Lost Reason = "Too expensive".
   :module: crm
   :notes: English UI, light theme, 1440px width, crop to the search bar.

.. tip::
   To view results for more than one lost reason, select the operator :guilabel:`is in` in the
   second field of the custom filter in the :guilabel:`Add Custom Filter` pop-up window. Choosing
   this operator makes it possible to choose multiple lost reasons in the third field.

   .. screenshot:: sales-crm-lost-custom-filter-popup
      :menu: CRM ‣ Sales ‣ My Pipeline ‣ Filters ‣ Add Custom Filter
      :shows: The "Add Custom Filter" pop-up with a Lost Reason condition and several reasons selected in the value field.
      :highlight: The selected lost reasons (red frame).
      :data: Two lost reasons selected.
      :module: crm
      :notes: English UI, light theme, 1440px width, crop to the pop-up.

Restore lost opportunities
==========================

To restore a lost opportunity, open the :menuselection:`CRM` app to reveal the :guilabel:`Pipeline`
dashboard. Or, navigate to :menuselection:`CRM app --> Sales --> My Pipeline`. From here, click the
:icon:`fa-caret-down` :guilabel:`(dropdown)` icon to the right of the search bar to open the
drop-down menu that contains :guilabel:`Filters`, :guilabel:`Group By`, and :guilabel:`Favorites`
columns.

Under the :guilabel:`Filters` column, select :guilabel:`Lost`. Doing so reveals all the lost
opportunities on the :guilabel:`Pipeline` page.

.. tip::
   To see all opportunities in the database, remove the default :guilabel:`My Pipeline` filter from
   the search bar.

From the lost opportunity's detail form, click :guilabel:`Restore` in the upper-left corner. Doing
so removes the red :guilabel:`Lost` banner from the opportunity form, signifying the opportunity has
been restored.

.. screenshot:: sales-crm-lost-restore-button
   :menu: CRM ‣ Sales ‣ My Pipeline ‣ (a lost opportunity)
   :shows: A lost opportunity with the Restore button in the header.
   :highlight: The Restore button (red frame).
   :data: A lost opportunity.
   :module: crm
   :notes: English UI, light theme, 1440px width, crop to the header.

Restore multiple opportunities at once
--------------------------------------

To restore multiple opportunities at once, open the dashboard mega menu by clicking the
:icon:`fa-caret-down` :guilabel:`(dropdown)` icon (to the right of the search bar) and select the
default :guilabel:`Lost` option located under the left-side :guilabel:`Filters` column.

Next, select the list view option, represented by the :icon:`fa-bars` :guilabel:`(list)` icon in the
upper-right corner. Doing so places all the opportunities from the :guilabel:`Pipeline` page in a
list view. With the list view chosen, select the checkbox to the left of each opportunity to be
restored.

Once the desired opportunities have been selected, click the :icon:`fa-cog` :guilabel:`Actions`
drop-down menu at the top of the :guilabel:`Pipeline` page. From the :icon:`fa-cog`
:guilabel:`(Actions)` drop-down menu, select :guilabel:`Unarchive`.

Doing so removes those selected opportunities from the :guilabel:`Pipeline` page because they no
longer fit the :guilabel:`Lost` filter criteria. Delete the :guilabel:`Lost` filter from the search
bar to reveal these newly-restored opportunities.

.. screenshot:: sales-crm-lost-unarchive-action
   :menu: CRM ‣ Sales ‣ My Pipeline
   :shows: The pipeline list view with several lost records selected and the gear (Actions) menu open on "Unarchive".
   :highlight: The "Unarchive" item (red frame).
   :data: Three lost opportunities selected.
   :module: crm
   :notes: English UI, light theme, 1440px width, crop to the open menu.

Manage lost leads
=================

If *Leads* are enabled on a database, then they can be marked as *lost* in the same manner as
opportunities. Leads use the same :ref:`lost reasons <crm/lost-reasons>` as opportunities.

.. note::
   To enable leads, navigate to :menuselection:`CRM app --> Configuration --> Settings` and check
   the :guilabel:`Leads` checkbox. This adds a new :guilabel:`Leads` menu to the header menu bar at
   the top of the page.

Mark a lead as lost
-------------------

To mark a lead as lost, navigate to :menuselection:`CRM app --> Leads`, and select a lead from the
list. Doing so reveals that lead's detail form. Then, click :guilabel:`Lost`, located at the top of
the lead's detail form.

This opens the :guilabel:`Mark Lost` pop-up window. From the :guilabel:`Lost Reason` drop-down menu,
choose an existing lost reason. If no applicable reason is available, then create a new one by
entering it into the :guilabel:`Lost Reason` field, and selecting :guilabel:`Create`.

Additional notes and comments can be added below the lost reason designated in the
:guilabel:`Closing Note` field.

When all the desired information has been entered in the :guilabel:`Mark Lost` pop-up window, click
:guilabel:`Mark as Lost`.

Restore lost leads
------------------

To restore a lost lead, navigate to :menuselection:`CRM app --> Leads`, and then click the
:icon:`fa-caret-down` :guilabel:`(dropdown)` icon to the right of the search bar to open the
drop-down menu that contains the :guilabel:`Filters`, :guilabel:`Group By`, and
:guilabel:`Favorites` columns.

Under the :guilabel:`Filters` column, select :guilabel:`Lost`. Doing so reveals all the lost leads
on the :guilabel:`Leads` page.

Then, click on the desired lost lead to restore, which opens that lead's detail form.

From the lost lead's detail form, click :guilabel:`Restore` in the upper-left corner. Doing so
removes the red :guilabel:`Lost` banner from the lead form, signifying the lead has been restored.

Restore multiple leads at once
------------------------------

To restore multiple leads at once, navigate to :menuselection:`CRM app --> Leads`, open the
:guilabel:`Filters` drop-down menu, and select the :guilabel:`Lost` option. Select the checkbox to
the left of each lead to be restored.

Once the desired leads have been selected, click the :icon:`fa-cog` :guilabel:`(Actions)` drop-down
menu at the top of the :guilabel:`Leads` page. From the :icon:`fa-cog` :guilabel:`(Actions)`
drop-down menu, select :guilabel:`Unarchive`.

Doing so removes those selected leads from the :guilabel:`Leads` page because they no longer fit the
:guilabel:`Lost` filter criteria. Delete the :guilabel:`Lost` filter from the search bar to reveal
these newly-restored leads.

.. seealso::
   :doc:`../performance/win_loss`

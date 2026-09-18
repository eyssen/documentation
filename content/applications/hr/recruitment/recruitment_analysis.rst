====================
Recruitment analysis
====================

The :guilabel:`Recruitment Analysis` report shows how many applications the company receives, where
they stand, and how they are distributed across job positions, recruiters, sources and time.

To open it, go to :menuselection:`Recruitment app --> Reporting --> Recruitment Analysis`. The
report opens as a graph of the applicants by stage, filtered to the applications created this month
and grouped by job position.

.. screenshot:: hr-recruitment-analysis-default
   :menu: Recruitment ‣ Reporting ‣ Recruitment Analysis
   :shows: The Recruitment Analysis report as a bar chart of applicants per stage, grouped by job position, with the default filters in the search bar.
   :highlight: The default filters in the search bar (red frame).
   :data: Demo company "YourCompany HU"; three job positions with applicants in several stages.
   :module: hr_recruitment
   :notes: English UI, light theme, 1440px width.

Change the view with the buttons in the upper-right corner:

- :icon:`fa-area-chart` :guilabel:`(Graph)`: a bar, line or pie chart. Bar and line charts can be
  stacked, descending or ascending.
- :icon:`oi-view-pivot` :guilabel:`(Pivot)`: a table, by default with the creation month in the rows
  and the stages in the columns.

Group and filter
================

Use the :guilabel:`Filters` and :guilabel:`Group By` menus of the search bar to answer the usual
questions. The groupings available on applications include:

- :guilabel:`Job Position`, :guilabel:`Department` and :guilabel:`Company`.
- :guilabel:`Stage`, :guilabel:`Recruiter` and :guilabel:`Degree`.
- :guilabel:`Source` and :guilabel:`Medium`: where the applications come from.
- :guilabel:`Refuse Reason`: why applications were turned down.
- :guilabel:`Creation Date`, :guilabel:`Hire Date` and :guilabel:`Last Stage Update` by year,
  quarter, month, week or day.

.. example::
   To see which sources produce hires rather than just applications, open the pivot view, filter on
   :guilabel:`Hired`, put :guilabel:`Source` in the rows and :guilabel:`Job Position` in the
   columns.

.. tip::
   Add :guilabel:`Comparison --> Creation Date: Previous Period` to any grouping to see the change
   against the previous month, quarter or year, with the variation column next to each figure.

.. screenshot:: hr-recruitment-analysis-pivot
   :menu: Recruitment ‣ Reporting ‣ Recruitment Analysis
   :shows: The Recruitment Analysis report in pivot view with the sources in the rows and the job positions in the columns, filtered to hired applicants.
   :highlight: The totals column (red frame).
   :data: Six months of applications from four sources across three job positions.
   :module: hr_recruitment
   :notes: English UI, light theme, 1440px width.

.. seealso::
   - :doc:`../recruitment`
   - :doc:`new_job`

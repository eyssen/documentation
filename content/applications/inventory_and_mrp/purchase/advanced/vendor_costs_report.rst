===================
Vendor costs report
===================

.. |RFQ| replace:: :abbr:`RfQ (Request for Quotation)`
.. |RFQs| replace:: :abbr:`RfQs (Requests for Quotation)`
.. |POs| replace:: :abbr:`POs (Purchase Orders)`
.. |caret| replace:: :icon:`fa-caret-down` :guilabel:`(down)` icon

With the *Purchase* application, users can track the fluctuation of vendor costs over time. This
allows users to identify the most expensive vendors, and track seasonal changes.

Create vendor costs reports
===========================

To create a vendor costs report, first navigate to :menuselection:`Purchase app --> Reporting -->
Purchase` to open the :guilabel:`Purchase Analysis` dashboard. By default, the dashboard displays a
line chart overview of the :guilabel:`Untaxed Total` of POs (Purchase Orders) with a
:guilabel:`Confirmation Date` for the current month, or of RFQs (Requests for Quotation) with a
status of *Draft*, *Sent, or *Cancelled*.

.. _purchase/vender-cost-report-filters:

Add filters and groups
----------------------

On the top-right, click the :icon:`oi-view-pivot` :guilabel:`(pivot)` icon to switch to pivot view.

Remove any default filters from the :guilabel:`Search...` bar. Then, click the |caret| to open the
drop-down menu that contains the :guilabel:`Filters`, :guilabel:`Group By`, and
:guilabel:`Favorites` columns.

.. note::
   Unless otherwise specified, the report displays data from both |RFQs| and |POs|. This can be
   changed by selecting either :guilabel:`Requests for Quotation` or :guilabel:`Purchase Orders`
   under the :guilabel:`Filters` column.

Under the :guilabel:`Filters` column, select a date range to use for comparison. The report can be
filtered by either :guilabel:`Order Date` or :guilabel:`Confirmation Date`. Choose one from the
list, and click the |caret| to specify the date range, either by month, quarter, or year.

Next, under the :guilabel:`Group by` column, select :guilabel:`Vendor`. Then, select
:guilabel:`Product`, which is also located in the :guilabel:`Group By` column.

.. note::
   Selecting :guilabel:`Product` is **not** required for this report. However, it is recommended, as
   it provides additional insight into the performance of individual vendors. Additional selections
   can be made under the :guilabel:`Group by` heading as well, including :guilabel:`Product
   Category`, :guilabel:`Status`, and :guilabel:`Purchase Representative`.

   To ensure the report is generated correctly, make sure that :guilabel:`Vendor` is the **first**
   selection made under the :guilabel:`Group By` column.

Next, make a selection under the :guilabel:`Comparison` heading. These options are only available
after the date range is selected under the :guilabel:`Filters` column, and vary based on that range.
:guilabel:`Previous Period` adds a comparison to the previous period, such as the last month or
quarter. :guilabel:`Previous Year` compares the same time period from the previous year.

.. note::
   While multiple time-based filters can be added at once, only one comparison can be selected at a
   time.

.. screenshot:: purchase-vendor-costs-filters-groups
   :menu: Purchase ‣ Reporting ‣ Purchase
   :shows: The drop-down menu with the Filters, Group By, and Comparison columns, with Vendor and
           Product selected under Group By.
   :highlight: The Group By column (red frame).
   :data: Demo company "YourCompany".
   :module: purchase
   :notes: English UI, light theme, 1440px width.

Add measures
------------

After selecting the :guilabel:`Filters`, :guilabel:`Group by`, and :guilabel:`Comparison` settings,
click out of the drop-down menu.

By default, the report displays with the following measures: :guilabel:`Order`, :guilabel:`Total`,
:guilabel:`Untaxed Total`, and :guilabel:`Count`. Click :guilabel:`Measures` at the top-left to open
the drop-down list of available measures. Click :guilabel:`Average Cost` to add it to the report.
Select any additional measures to add to the report, or click on any of the already selected
measures to remove them, if desired.

.. tip::
   It is recommended to run the report with at least :guilabel:`Average Cost`, :guilabel:`Total`, or
   :guilabel:`Untaxed Total` selected from the :guilabel:`Measures` list. Additional measures, such
   as :guilabel:`Days to Receive`, can be added to provide additional insights.

View results
============

After all of the :ref:`filters and measures have been selected
<purchase/vender-cost-report-filters>`, the report generates in the pivot view.

.. screenshot:: purchase-vendor-costs-sample-report
   :menu: Purchase ‣ Reporting ‣ Purchase
   :shows: A pivot table vendor costs report, grouped by Vendor then Product, with the Total and
           Average Cost measures.
   :highlight: The Average Cost column (red frame).
   :data: Demo company "YourCompany"; two vendors, a few products each.
   :module: purchase
   :notes: English UI, light theme, 1440px width.

To keep a copy of the results outside the pivot view, click the :icon:`fa-download`
:guilabel:`(download)` icon at the top of the pivot table to download it as an XLSX spreadsheet.

.. note::
   The vendor costs report is also available in *graph* view. Click the :icon:`fa-area-chart`
   :guilabel:`(area chart)` icon to change to graph view. Click the corresponding icon at the top of
   the report to switch to a :icon:`fa-bar-chart` :guilabel:`(bar chart)`, :icon:`fa-line-chart`
   :guilabel:`(line chart)`, or :icon:`fa-pie-chart` :guilabel:`(pie chart)`.

.. seealso::
   To save this report as a *favorite*, see :ref:`search/favorites`.

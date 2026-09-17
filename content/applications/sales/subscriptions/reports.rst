=========
Reporting
=========

MRR / ARR analysis
==================

Go to :menuselection:`Subscriptions app --> Reporting --> MRR / ARR Analysis`. The report reads the
:guilabel:`MRR` and :guilabel:`ARR` of the contracts: the monthly recurring revenue is normalised
from the billing period of every active line, and the annual figure is twelve times that.

The report opens as a pivot table and can be switched to a line graph to follow the MRR over time.

Filters: :guilabel:`Running`, :guilabel:`Suspended`, :guilabel:`Hard decline`, :guilabel:`Not
archived` and :guilabel:`Created this month`.

Groupings: :guilabel:`Customer`, :guilabel:`State`, :guilabel:`Dunning state`,
:guilabel:`Company` and :guilabel:`Created month`.

.. screenshot:: sales-subscriptions-mrr-report
   :menu: Subscriptions ‣ Reporting ‣ MRR / ARR Analysis
   :shows: The MRR / ARR analysis in pivot view, grouped by customer, with the MRR and ARR measures and the filter facets in the search bar.
   :highlight: The MRR and ARR measure columns (red frame).
   :data: Six demo contracts across two customers.
   :module: subscription
   :notes: English UI, light theme, 1440px width, crop to the search bar and the table.

.. screenshot:: sales-subscriptions-mrr-graph
   :menu: Subscriptions ‣ Reporting ‣ MRR / ARR Analysis
   :shows: The same report as a line graph showing the MRR over the months.
   :highlight: No highlight; the chart is the subject.
   :data: Twelve months of demo contracts.
   :module: subscription
   :notes: English UI, light theme, 1440px width, crop to the chart.

Following one contract
======================

Contract-level figures are on the contract itself: :guilabel:`MRR` and :guilabel:`ARR` in the
:guilabel:`Billing` group, the billed history on each line's :guilabel:`Billed Periods` tab, and
every change on its :guilabel:`Change History` tab.

.. seealso::
   - :doc:`contracts`
   - :doc:`lines`

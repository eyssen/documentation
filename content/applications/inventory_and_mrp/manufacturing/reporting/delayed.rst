======
Delays
======

.. |SO| replace:: :abbr:`SO (sales order)`
.. |SOs| replace:: :abbr:`SOs (sales orders)`
.. |MO| replace:: :abbr:`MO (manufacturing order)`
.. |MOs| replace:: :abbr:`MOs (manufacturing orders)`
.. |RfQ| replace:: :abbr:`RfQ (request for quotation)`

Odoo's *Manufacturing* app displays *delays* in manufacturing orders through the :guilabel:`Delayed
Productions` filter. If the |MO| is delayed, it is highlighted in red on the list view of
manufacturing orders, to draw attention to the delay.

.. screenshot:: manufacturing-delayed-filter
   :menu: Manufacturing app --> Operations --> Manufacturing Orders
   :shows: The list view of manufacturing orders, "Delayed Productions" filter applied in the
      "Search..." bar, one MO shown with its deadline/end date highlighted in red.
   :highlight: The red-highlighted deadline column of the delayed MO.
   :data: Demo company "YourCompany"; one manufacturing order past its deadline.
   :module: mrp
   :notes: English UI, light theme, 1440px width.

Deadline calculation
====================

The |MO| deadline depends on how the |MO| was created, and is calculated as follows:

- **Make To Order**: the |MO| deadline is the *Sales Order Delivery Date*.
- **Replenishment**: the |MO| deadline is *today + Manufacturing Lead Time*.
- **Manually created MO**: the deadline field remains empty.

.. important::
   The |MO| *deadline* is not the same as the |MO| *end date*.

   The end date is computed as:

   .. math::
      \text{End date} =
       \text{Scheduled start date}
       +\text{Total duration of all operations}

Filters
=======

Several additional filters are available in the :guilabel:`Search...` bar, on the list of
manufacturing orders, to help track delays:

- :guilabel:`Delayed Productions`: the |MO| is either late (see below), or has one or more
  components with a delayed delivery.
- :guilabel:`Late Availability`: one or more required components are not available before the
  deadline. For example, a confirmed purchase order or manufacturing order for components is
  scheduled to end *after* the |MO| deadline.
- :guilabel:`Components Available`: all components are available to begin production.

An |MO| is considered *late* when it is confirmed or in progress, and its deadline has already
passed, or its computed end date falls after the deadline. Late |MOs| are highlighted in red on
list views.

Use case
========

Consider an |MO| with a deadline of **September 17th**:

- If production on the |MO| starts after September 17th, it appears in the :guilabel:`Delayed
  Productions` filter.
- If required components are scheduled to arrive after September 17th, the |MO| appears in the
  :guilabel:`Late Availability` filter.
- If the |MO| has a scheduled end date after September 17th, it is considered late, and its
  deadline is highlighted in red.

.. screenshot:: manufacturing-delayed-deadline
   :menu: Manufacturing app --> Operations --> Manufacturing Orders (open a manufacturing order)
   :shows: The manufacturing order form, "Scheduled Date"/deadline field emphasized to show it is
      in the past.
   :highlight: The deadline field, shown in red.
   :data: Demo company "YourCompany"; one late manufacturing order.
   :module: mrp
   :notes: English UI, light theme, 1440px width, crop to the header of the form.

By combining these indicators, planners can quickly identify where production is at risk of missing
delivery commitments.

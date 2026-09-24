=================
Working schedules
=================

A *working schedule* defines the hours employees are expected to work. It is set on the employee's
:doc:`contract <contracts>` and on the employee record, and it is the reference against which
:doc:`attendances <../attendances>` and :doc:`time off <../time_off>` are measured.

To see the configured working schedules, go to :menuselection:`Employees app --> Configuration -->
Working Schedules`.

Working schedules are company-specific. In a multi-company database, every company needs its own
schedules; the :guilabel:`Company` column only appears when more than one company exists.

.. example::
   A database with five companies that all work a standard 40-hour week needs five separate
   40-hour working schedules, one per company.

.. screenshot:: hr-working-schedules-list
   :menu: Employees ‣ Configuration ‣ Working Schedules
   :shows: The Working Schedules list with the standard 40 hours/week and a 20 hours/part time schedule.
   :highlight: The Name and Company columns (red frame).
   :data: Demo company "YourCompany HU"; schedules "Standard 40 hours/week" and "20 Hours/Part time".
   :module: resource, hr
   :notes: English UI, light theme, 1440px width.

.. _employees/new-working-schedule:

Create a working schedule
=========================

Click :guilabel:`New` and fill in the form. The form has a general information section and a
:guilabel:`Working Hours` tab listing the individual time ranges per day.

- :guilabel:`Name`: a descriptive name, such as `Standard 20 Hours/Week`.
- :guilabel:`Company`: the company the schedule belongs to. An empty field makes it available to
  all companies.
- :guilabel:`Timezone`: the time zone the hours are expressed in.
- :guilabel:`Flexible Hours`: tick this checkbox when employees may work their hours freely rather
  than at fixed times. The :guilabel:`Working Hours` tab then disappears, the
  :guilabel:`Company Full Time` field is relabeled :guilabel:`Hours per Week`, and
  :guilabel:`Average Hour per Day` becomes editable.
- :guilabel:`Company Full Time`: the number of hours per week that counts as full time in the
  company, typically `40`.
- :guilabel:`Average Hour per Day`: computed from the :guilabel:`Working Hours` tab, and editable
  on a flexible schedule. It is used wherever a day has to be converted into hours, for example
  when a day of time off is deducted.

Next, configure the :guilabel:`Working Hours` tab. Each line has a :guilabel:`Day of Week`, a
:guilabel:`Day Period` (:guilabel:`Morning`, :guilabel:`Lunch`, or :guilabel:`Afternoon`), and a
:guilabel:`Work from` and :guilabel:`Work to` time. A default 40-hour week is pre-filled with morning (8:00-12:00), lunch
(12:00-13:00), and afternoon (13:00-17:00) lines.

.. note::
   :guilabel:`Work from` and :guilabel:`Work to` use the 24-hour format: `2:00 PM` is entered as
   `14:00`.

.. tip::
   If the hours alternate between two weeks, click :guilabel:`Switch to 2 weeks calendar` at the top
   of the form. The :guilabel:`Working Hours` tab then shows an even and an odd week that can be
   configured separately.

.. screenshot:: hr-working-schedules-form
   :menu: Employees ‣ Configuration ‣ Working Schedules ‣ New
   :shows: A working schedule form named "20 Hours/Part time" with Company Full Time 40, Average Hour per Day, and the Working Hours tab listing the Monday to Friday morning lines.
   :highlight: The Working Hours tab lines (red frame).
   :data: Demo company "YourCompany HU"; five morning lines 8:00-12:00, Monday to Friday.
   :module: resource, hr
   :notes: English UI, light theme, 1440px width.

.. important::
   Working schedules cannot be shared between companies. Each company needs its own set.

The company's default schedule for new employees is selected as :guilabel:`Company Working Hours` in
:menuselection:`Employees app --> Configuration --> Settings`.

.. seealso::
   - :doc:`contracts`
   - :doc:`../attendances`

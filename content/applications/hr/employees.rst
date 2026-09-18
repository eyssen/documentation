:show-content:

=========
Employees
=========

Odoo **Employees** centralizes :doc:`personnel files <employees/new_employee>`, employment
:doc:`contracts <employees/contracts>`, and :doc:`departmental hierarchies <employees/departments>` in
one system. Properly configuring its settings ensures the dashboard shows each employee's real-time
attendance and work location—data that drives payroll accuracy, capacity planning, and compliance
reporting.

.. cards::

   .. card:: New employees
      :target: employees/new_employee

      Set up new employee records.

   .. card:: Departments
      :target: employees/departments

      Create and manage the departments employees are a part of.

   .. card:: Contracts
      :target: employees/contracts

      Manage and create employee contracts.

   .. card:: Certifications
      :target: employees/certifications

      Certify employees as subject matter experts with certifications.

   .. card:: Badges
      :target: employees/badges

      Grant badges to employees for performance and achievements.

   .. card:: Working schedules
      :target: employees/working_schedules

      Define the hours employees are expected to work.

   .. card:: Equipment
      :target: employees/equipment

      Manage and track employee equipment.

   .. card:: Offboarding
      :target: employees/offboarding

      Take care of employee records when collaboration ends.

   .. card:: Employee retention report
      :target: employees/retention_report

      Gain insight to the retention rate for a company.

.. _employees/settings:

Settings
========

To view and configure the available settings, navigate to :menuselection:`Employees app -->
Configuration --> Settings`.

Employees
---------

- :guilabel:`Presence Display`: select how the employee's availability status is calculated.

  - :guilabel:`Based on attendances`: marked available when :ref:`checked into <attendances/check-in>`
    the **Attendances** app.
  - :guilabel:`Based on user status in system`: marked available when the :doc:`employee logs in to
    Odoo <attendances/check_in_check_out>`.

- :guilabel:`Advanced Presence Control`: when enabled, presence status can be calculated from
  operational signals rather than check-ins or logins:

  - :guilabel:`Based on number of emails sent`: an employee is marked present if they send at least
    # emails per hour; otherwise, they are marked absent. Enter the minimum number of emails that
    must be sent in the :guilabel:`Sent Emails` field.
  - :guilabel:`Based on IP Address`: an employee is marked present only when connected from one of
    the specified corporate IP addresses. Enter the IP addresses in the :guilabel:`IP Addresses`
    field, separating each address with a comma.

- :guilabel:`Skills Management`: enable this option to display the :ref:`resumé tab <employees/resume>`
  on employee profiles. This allows for the display of :ref:`work experience <employees/resume>`,
  :ref:`skills <employees/skills>`, and :doc:`certifications <employees/certifications>`.
- :guilabel:`Remote Work`: enable this option to allow for a detailed schedule to appear on the
  employee form, in the :ref:`Work Information <employees/work-info-tab>` tab. When enabled, the
  specific location can be set for each working day for the employee. The corresponding icon is
  displayed in the upper-right corner of the employee card, indicating their location by icon, and
  status by color.

  .. example::
     A green :icon:`fa-home` :guilabel:`(home)` icon indicates the employee is working from home
     that day. A :icon:`fa-building` :guilabel:`(building)` icon means the employee is scheduled to
     work at the office.

     The *color* of the icon indicates the employee's status, with green indicating present, yellow
     indicating absent, and gray indicating it is outside of the employee's working hours.

     .. screenshot:: hr-employees-presence-cards
        :menu: Employees ‣ Employees
        :shows: Two employee kanban cards, one with a green home icon and one with a building icon, showing the work location and the presence colour.
        :highlight: The location icons in the upper-right corner of the cards (red frame).
        :data: Demo company "YourCompany HU"; one employee working from home, one at the office.
        :module: hr, hr_homeworking
        :notes: English UI, light theme, 1440px width. Crop to the two cards.

Work organization
-----------------

Using the drop-down menu, select the default :guilabel:`Company Working Hours`. The default options
are :guilabel:`Standard 40 hours/week`, :guilabel:`Appointment Resource Default Calendar`, and
:guilabel:`Standard 32 hours/week (4 work days, Friday free)`.

The available working hours listed are the same as the configured :doc:`working schedules
<employees/working_schedules>` configured for the company.

Employee update rights
----------------------

Enable the :guilabel:`Employee Editing` option to allow employees to edit their own data on their
employee record.

.. toctree::
   :titlesonly:

   employees/new_employee
   employees/onboarding
   employees/departments
   employees/contracts
   employees/working_schedules
   employees/certifications
   employees/badges
   employees/equipment
   employees/offboarding
   employees/retention_report

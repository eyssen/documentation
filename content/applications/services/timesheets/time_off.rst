==========================================
Create Timesheets upon Time Off Validation
==========================================

Odoo automatically timesheets on project/tasks upon time off requests. This allows for better
overall control over the validation of timesheets, as it does not leave place for forgetfulness
and questions after hours that have not been timesheeted by the employee.

Activate the :ref:`developer mode <developer-mode>`, go to *Timesheets*, and change the *Project*
and *Task* set by default, if you like.

.. screenshot:: services-timesheets-time-off-setting
   :menu: Timesheets ‣ Configuration ‣ Settings
   :shows: The Time Off block of the Timesheets settings with the "Generate timesheets for validated time off requests and public holidays" option enabled, and the internal project and task it uses.
   :highlight: The Time Off setting (red frame).
   :data: Internal project "Internal", task "Time Off".
   :module: project_timesheet_holidays
   :notes: English UI, light theme, developer mode on, 1440px width, crop to the setting block.

Go to :menuselection:`Time Off --> Configuration --> Time Off Types`. Select or create the
needed type, and decide if you would like the requests to be validated or not.

.. screenshot:: services-timesheets-time-off-type
   :menu: Time Off ‣ Configuration ‣ Time Off Types
   :shows: A time off type form with the approval setting and the timesheets section that decides whether validated requests generate timesheet entries.
   :highlight: The approval and timesheets settings (red frame).
   :data: Time off type "Paid Time Off".
   :module: hr_holidays, project_timesheet_holidays
   :notes: English UI, light theme, 1440px width, crop to the settings block.

| Now, once the employee has requested his time off and the request has been validated (or not,
  depending on the setting chosen), the time is automatically allocated on *Timesheets*, under the
  respective project and task.
| On the example below, the user requested *Paid Time off* from July 13th to 15th.

.. screenshot:: services-timesheets-time-off-request
   :menu: Time Off ‣ My Time ‣ Time Off ‣ New
   :shows: A validated time off request for three consecutive days of paid time off.
   :highlight: None.
   :data: Employee "Marc Demo", Paid Time Off from 13 to 15 July.
   :module: hr_holidays
   :notes: English UI, light theme, 1440px width, crop to the request form.

Considering that validation is not required, the requested time off is automatically displayed in
*Timesheets*. If validation is necessary, the time is automatically allocated after the responsible
person for validating does it so.

.. screenshot:: services-timesheets-time-off-generated
   :menu: Timesheets ‣ Timesheets ‣ My Timesheets
   :shows: The timesheet grid of the employee, with the three days of the validated time off automatically filled in on the internal time off task.
   :highlight: The three generated cells (red frame).
   :data: Employee "Marc Demo", week of 13 July, 8 hours per day on "Internal / Time Off".
   :module: project_timesheet_holidays
   :notes: English UI, light theme, 1440px width, crop to the grid.

Click on the magnifying glass, hovering over the concerned cell, to access all the aggregated data
on that cell (day), and see details regarding the project/task.

.. screenshot:: services-timesheets-time-off-cell-detail
   :menu: Timesheets ‣ Timesheets ‣ My Timesheets
   :shows: The detail popup of a timesheet cell, opened with the magnifying glass, listing the entries of that day with their project, task and description.
   :highlight: The magnifying glass and the popup (red frame).
   :data: Employee "Marc Demo", 14 July, one 8-hour time off entry.
   :module: project_timesheet_holidays
   :notes: English UI, light theme, 1440px width, crop to the cell and the popup.

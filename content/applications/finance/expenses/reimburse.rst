===================
Reimburse employees
===================

After an expense report is :doc:`posted to an accounting journal <../expenses/post_expenses>`, the
next step is to reimburse the employee. Employees can be reimbursed via cash, check, or direct
deposit in two ways:

- :ref:`Individually <expenses/reimburse-single>`: Each individual expense report is reimbursed
  separately.
- :ref:`In bulk <expenses/reimburse-bulk>`: Multiple expense reports are reimbursed in a single
  payment.

.. note::
   Reimbursing expenses through the employee's payslip is **not** available; the
   :guilabel:`Reimburse in Payslip` option on the settings page should be left disabled. Expenses
   are always paid with a regular payment registered in the **Accounting** app.

.. _expenses/reimburse-settings:

Reimbursement settings
======================

Reimbursements can be paid via check, cash, or bank transfer (usually referred to as direct
deposit). To set up payment options, first configure the various settings by navigating to
:menuselection:`Expenses app --> Configuration --> Settings`.

Set how payments are made in the :guilabel:`Accounting` section. Click the drop-down menu
under :guilabel:`Payment methods`, and select the desired payment option(s). The available options
are the outgoing payment method lines of the bank and cash journals, for example
:guilabel:`Manual (Bank)`, :guilabel:`Manual (Cash)`, and, when the *Checks* payment method is
enabled on a bank journal, :guilabel:`Checks (Bank)`. This setting only restricts the payment methods
for expenses **paid by the company**.

Leaving this field blank allows for **all** available payment options to be used.

The same section also holds the :guilabel:`Employee Expense Journal` (the default journal used when
posting reports paid by employees) and the :guilabel:`Expense Outstanding Account` (the default
outstanding account for expenses paid by the company).

.. screenshot:: finance-expenses-reimburse-settings
   :menu: Expenses ‣ Configuration ‣ Settings
   :shows: The "Accounting" block of the Expenses settings with the "Employee Expense Journal", "Expense Outstanding Account" and "Payment methods" settings.
   :highlight: The "Payment methods" many2many field (red frame).
   :data: Demo company; Employee Expense Journal "Expenses", Payment methods "Manual (Bank)".
   :module: hr_expense
   :notes: English UI, light theme, 1440px width, crop to the Accounting block.

When all desired configurations are complete, click :guilabel:`Save` to activate the settings.

.. _expenses/reimburse-single:

Reimburse individually
======================

To reimburse an individual expense report, first navigate to :menuselection:`Expenses app -->
Expense Reports`. All expense reports are presented in a default list view. Click on the expense
report being reimbursed to view the report details.

.. important::
   **Only** expense reports with a status of :guilabel:`Posted` can be reimbursed directly to the
   employee.

Click the :guilabel:`Pay` button in the top-left corner of the expense report, and a :guilabel:`Pay`
pop-up window loads. Enter the following information in the pop-up window:

- :guilabel:`Journal`: Select the accounting journal to post the payment using the drop-down menu.
  The default options are :guilabel:`Bank` or :guilabel:`Cash`.
- :guilabel:`Payment Method`: Select how the payment is made using the drop-down menu. If
  :guilabel:`Cash` is selected for the :guilabel:`Journal`, the only option available is
  :guilabel:`Manual Payment`. If :guilabel:`Bank` is selected for the :guilabel:`Journal`, the
  default options are :guilabel:`Manual Payment` or :guilabel:`Checks`.
- :guilabel:`Recipient Bank Account`: This field only appears if the :guilabel:`Journal` is set to
  :guilabel:`Bank`. The employee's :ref:`bank account <employees/private-info>` populates this
  field, by default. If the employee has more than one trusted bank account on their employee
  profile, use the drop-down menu to select the desired bank account.
- :guilabel:`Amount`: The total amount being reimbursed populates this field, by default.
- :guilabel:`Payment Date`: Enter the date the payment is issued in this field. The current date
  populates this field, by default.
- :guilabel:`Memo`: The text entered in the :doc:`Expense Report Summary
  <../expenses/expense_reports>` field of the expense report populates this field, by default.

.. screenshot:: finance-expenses-reimburse-payment
   :menu: Expenses ‣ Expense Reports ‣ (a posted report) ‣ Register Payment
   :shows: The "Register Payment" pop-up for one expense report: Journal "Bank", Payment Method "Manual", Recipient Bank Account, Amount, Payment Date and Memo fields, and the "Create Payment" button.
   :highlight: The "Journal" and "Payment Method" fields.
   :data: Report "Trip to Brussels", amount 210.00, journal Bank.
   :module: hr_expense
   :notes: English UI, light theme, 1440px width.

When the fields of the pop-up window are completed, click the :guilabel:`Create Payment` button to
register the payment, and reimburse the employee. A green :guilabel:`In Payment` banner now appears
on the expense report.

.. _expenses/reimburse-bulk:

Reimburse in bulk
=================

To reimburse multiple expense reports at once, navigate to :menuselection:`Expenses app --> Expense
Reports` to view all expense reports in a list view. Next, select the expense reports to be
reimbursed.

.. important::
   **Only** expense reports with a status of :guilabel:`Posted` can be reimbursed directly to the
   employee.

.. tip::
   Adjust the :guilabel:`STATUS` filter on the left side to only show :guilabel:`Posted` expense
   reports. This displays **only** expense reports that are able to be reimbursed.

Tick the checkbox next to the expense reports being reimbursed, then click the :guilabel:`Pay`
button, and a :guilabel:`Pay` pop-up window loads. Enter the following information in the pop-up
window:

- :guilabel:`Journal`: Select the accounting journal to post the payment using the drop-down menu.
  The default options are :guilabel:`Bank` or :guilabel:`Cash`.
- :guilabel:`Payment Method`: Select how the payment is made using the drop-down menu. If
  :guilabel:`Cash` is selected for the :guilabel:`Journal`, the only option available is
  :guilabel:`Manual Payment`. If :guilabel:`Bank` is selected for the :guilabel:`Journal`, the
  default options are :guilabel:`Manual Payment` or :guilabel:`Checks`.
- :guilabel:`Group Payments`: When multiple expense reports are selected for the same employee, this
  option appears. Tick the checkbox to have only one payment made per employee, rather than issuing
  multiple payments to the same employee.
- :guilabel:`Amount`: The total amount being reimbursed for all the expense reports populates this
  field, by default.
- :guilabel:`Payment Date`: Enter the date the payments are issued. The current date populates this
  field, by default.

When the fields on the :guilabel:`Pay` pop-up window are completed, click the :guilabel:`Create
Payments` button to register the payments, and reimburse the employees.

.. screenshot:: finance-expenses-reimburse-repay-multiple
   :menu: Expenses ‣ Expense Reports ‣ (several posted reports selected) ‣ Register Payment
   :shows: The "Register Payment" pop-up opened for several posted expense reports at once: Journal, Payment Method, Group Payments checkbox, Payment Date and the "Create Payment" button.
   :highlight: The "Group Payments" checkbox.
   :data: Two posted reports of the same employee.
   :module: hr_expense
   :notes: English UI, light theme, 1440px width.

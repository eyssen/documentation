:show-content:

.. _general/automation-rules:

================
Automation rules
================

Automation rules allow the execution of one or more predefined actions in response to a specific
trigger, e.g., create an activity when a field is set to a specific value, or archive a record 7
days after its last update.

When creating an automation rule, :ref:`domain filters <general/automation-rules/conditions>`
allow you to add conditions that must be met for the automation rule to run, e.g., the opportunity
must be assigned to a specific salesperson, or the state of the record must not be
:guilabel:`Draft`.

Automation rules are provided by the *Automation Rules* module (`base_automation`). If the menu
described below is not available, go to the :guilabel:`Apps` app, remove the :guilabel:`Apps` filter
from the search bar, search for `Automation Rules`, and click :guilabel:`Activate`.

.. note::
   Managing automation rules requires :ref:`developer mode <developer-mode>` and the
   *Administration / Settings* access rights.

To create an automation rule, proceed as follows:

#. With :ref:`developer mode activated <developer-mode>`, go to :menuselection:`Settings -->
   Technical --> Automation --> Automation Rules`, then click :guilabel:`New`.
#. Select the :guilabel:`Model` the automation rule applies to, e.g., :guilabel:`Sales Order`.
#. Give the automation rule a clear, meaningful name that identifies its purpose.
#. Select the :ref:`trigger <general/automation-rules/trigger>` and, if necessary, fill in the
   fields that appear on the screen based on the chosen trigger.
#. Click :guilabel:`Add an action`, then select the :guilabel:`Type` of
   :ref:`action <general/automation-rules/action>` and fill in the fields that appear on the screen
   based on your selected action.
#. Save the automation rule.

.. screenshot:: general-automation-rules-form
   :menu: Settings ‣ Technical ‣ Automation ‣ Automation Rules ‣ New
   :shows: Automation rule form: name, Model, Trigger and Delay fields, "Actions To Do" tab with one
      action line and the "Add an action" button, "Notes" tab.
   :highlight: The Trigger field and the "Add an action" button.
   :data: Rule "Follow up unhappy customers" on model Sales Order, trigger "After creation", delay 3 months.
   :module: base_automation
   :notes: English UI, developer mode active, 1440px width, crop to the form sheet.

.. example::

   To ensure follow-up on less satisfied clients, this automation rule creates an activity 3 months
   after a sales order is created for clients with a satisfaction percentage lower than 30%.

   .. screenshot:: general-automation-rules-example-activity-conditions
      :menu: Settings ‣ Technical ‣ Automation ‣ Automation Rules
      :shows: Automation rule on the Sales Order model with trigger "After creation", delay 3 months,
         an extra condition on the customer satisfaction field lower than 30%, and a "Create Activity"
         action in the "Actions To Do" tab.
      :highlight: The Trigger/Delay block and the extra condition.
      :data: Rule "Follow up unhappy customers"; activity type "To-Do".
      :module: base_automation, sale
      :notes: English UI, developer mode active, crop to the form sheet.

.. tip::
   - Use the :guilabel:`Notes` tab to document the purpose and functioning of automation rules. This
     makes rules easier to maintain and facilitates collaboration between users.
   - The model targeted by the automation rule is set in the :guilabel:`Model` field of the
     automation rule form.
   - Automation rules can be created from any kanban stage by clicking the :icon:`fa-cog`
     :guilabel:`(Settings)` icon that appears when hovering over the kanban stage name, then
     selecting :guilabel:`Automations`. In this case, the :guilabel:`Trigger` is set to
     :guilabel:`Stage is set to` by default, but it can be changed if necessary.

     .. screenshot:: general-automation-rules-kanban-stage
        :menu: Project ‣ (any project) kanban view
        :shows: Kanban stage header with the gear (Settings) dropdown open, showing the
           "Automations" entry.
        :highlight: The "Automations" dropdown entry.
        :data: Demo project "Office Design", stage "In Progress".
        :module: base_automation, project
        :notes: English UI, crop to the stage column header and dropdown.

.. _general/automation-rules/trigger:

Trigger
=======

The :guilabel:`Trigger` is used to define what kind of event needs to occur for the automation rule
to run. The available triggers depend on the model. Five trigger
categories are available overall:

- :ref:`general/automation-rules/trigger-values-updated`
- :ref:`general/automation-rules/trigger-email-events`
- :ref:`general/automation-rules/trigger-timing-conditions`
- :ref:`general/automation-rules/trigger-custom`
- :ref:`general/automation-rules/trigger-external`

.. _general/automation-rules/conditions:

Adding conditions
-----------------

Domain filters allow you to determine the records an automation rule should target or exclude.
Efficient filtering enhances overall performance as it avoids unnecessary processing on records that
are not impacted by the rule.

.. tip::
   :ref:`Activate developer mode <developer-mode>` before creating an automation rule to have the
   most flexibility in adding domain filters.

Depending on the trigger chosen, it is possible to define one or more conditions a record must meet
*before* and/or *after* a trigger occurs.

- The :guilabel:`Before Update Domain` defines the conditions a record must meet *before* the
  trigger event occurs, e.g., the record must have `Type = Customer Invoice` and `Status = Posted`.

  With :ref:`developer mode activated <developer-mode>`, click :guilabel:`Edit Domain`, if
  available, then :guilabel:`New Rule`.

- :guilabel:`Extra Conditions`, or in some cases :guilabel:`Apply on` filters, define the conditions
  a record must meet *after* the trigger event occurs, e.g., the customer invoice must have `Payment
  Status = Partially Paid`.

  With :ref:`developer mode activated <developer-mode>` if needed, click :guilabel:`Add conditions`
  or :guilabel:`Edit Domain`, as relevant, then :guilabel:`New Rule`.

When a :ref:`trigger <general/automation-rules/trigger>` occurs, e.g., the payment status of a
posted customer invoice is updated, the automation rule checks the defined conditions and only
executes the :ref:`action <general/automation-rules/action>` if the record matches those conditions.

.. example::
   If the automated action should be executed when an email address is set for the first time (in
   contrast to modifying an email address) on an existing contact that is an individual rather than
   a company, use `Email is not set` and `Is a Company is not set` as the :guilabel:`Before Update
   Domain` and `Email is set` as the :guilabel:`Apply on` domain.

   .. screenshot:: general-automation-rules-before-update-domain
      :menu: Settings ‣ Technical ‣ Automation ‣ Automation Rules
      :shows: Automation rule on the Contact model with trigger "On save"; Before Update Domain
         "Email is not set" and "Is a Company is not set"; Apply on domain "Email is set".
      :highlight: The Before Update Domain and Apply on fields.
      :data: Rule "Welcome new individual contacts".
      :module: base_automation, contacts
      :notes: English UI, developer mode active, crop to the trigger section.

.. note::
   The :guilabel:`Before Update Domain` is not checked upon the creation of a record.

.. _general/automation-rules/trigger-values-updated:

Values Updated
--------------

Trigger automated actions when specific changes happen in the database. The triggers available in
this category depend on the model and are based on common changes, such as adding a specific tag
(e.g., to a task) or setting a field's value (e.g., setting the :guilabel:`User` field).

Select the trigger, then select a value if required.

.. _general/automation-rules/trigger-email-events:

Email Events
------------

Trigger automated actions upon receiving or sending emails:

- :guilabel:`On incoming message`: when a message is received on the record.
- :guilabel:`On outgoing message`: when a message is sent from the record.

These triggers are only available for models that have a chatter.

.. _general/automation-rules/trigger-timing-conditions:

Timing Conditions
-----------------

Trigger automated actions at a point in time relative to a date field or to the creation or update
of a record. The following triggers are available:

- :guilabel:`Based on date field`: The action is triggered a defined period of time before or after
  the date of the selected date field.
- :guilabel:`After creation`: The action is triggered a defined period of time after a record is
  created and saved.
- :guilabel:`After last update`: The action is triggered a defined period of time after an existing
  record is edited and saved.

You can then define:

- a :guilabel:`Delay`: Specify the number of minutes, hours, days, or months. To have an action
  executed before the trigger date, specify a negative number. If you selected the :guilabel:`Based
  on date field` trigger, you must also select the date field to be used to determine the delay.

  .. note::
     By default, the scheduler checks for time-triggered automation rules every 240 minutes, or 4
     hours. This frequency is generally sufficient for delays such as 3 months after the order date
     or 7 days after the last update.

     For delays of less than the equivalent of 2400 minutes, or 40 hours, the system recalculates
     the frequency of this check to ensure that more granular delays, e.g., 1 hour before the event
     start date and time, or 30 minutes after creation, can be respected as closely as possible.

     An on-screen message indicates the possible delay after the scheduled triggering of the rule.

     .. screenshot:: general-automation-rules-trigger-delay-message
        :menu: Settings ‣ Technical ‣ Automation ‣ Automation Rules
        :shows: Timing trigger with a delay and the grey information message below it about the
           possible delay after the scheduled execution of the rule.
        :highlight: The information message.
        :module: base_automation
        :notes: English UI, crop to the trigger/delay block.

     To view or manually edit the frequency of the scheduler, with :ref:`developer mode activated
     <developer-mode>`, go to :menuselection:`Settings --> Technical --> Scheduled Actions` to see
     all scheduled actions for your database.

     Enter `Automation` in the search bar, then, in the list of results, click :guilabel:`Automation
     Rules: check and execute`. If desired, update the value of the :guilabel:`Execute Every` field.
     Click :guilabel:`Run Manually` at any time to manually trigger this scheduled action.

- :guilabel:`Extra Conditions`: Click :guilabel:`Add condition`, then specify the conditions to be
  met for the automation rule to run. Click :guilabel:`New Rule` to add another condition.

The action is executed when the delay is reached and the conditions are met.

.. example::
   To send a reminder email 30 minutes *before* the start of a calendar event, select
   :guilabel:`Start (Calendar Event)` as the date field for the :guilabel:`Trigger` and set the
   :guilabel:`Delay` to `-30` :guilabel:`Minutes`.

   .. screenshot:: general-automation-rules-timing-trigger
      :menu: Settings ‣ Technical ‣ Automation ‣ Automation Rules
      :shows: Automation rule on the Calendar Event model with trigger "Based on date field",
         Delay "-30 Minutes" and trigger date "Start".
      :highlight: The Trigger, Delay and date field.
      :data: Rule "Meeting reminder".
      :module: base_automation, calendar
      :notes: English UI, crop to the trigger section.

.. _general/automation-rules/trigger-custom:

Custom
------

Trigger automated actions:

- :guilabel:`On save`: when a record is saved.
- :guilabel:`On deletion`: when a record is deleted.
- :guilabel:`On archived` / :guilabel:`On unarchived`: when a record is archived or restored, for
  models that can be archived.
- :guilabel:`On UI change`: when a field's value is changed on the Form view, even before the record
  is saved.

For the :guilabel:`On save` and :guilabel:`On UI change` triggers, you **must** then select the
field(s) to be used to trigger the automation rule in the :guilabel:`When updating` field.

.. warning::
   If no field is selected in the :guilabel:`When updating` field, the automated action may be
   executed multiple times per record.

Optionally, you can also define additional conditions to be met to trigger the automation rule in
the :guilabel:`Apply on` field.

.. example::
   To trigger an automated action *upon* the creation of a record, e.g., when a new contact is
   created, select the :ref:`On save <general/automation-rules/trigger-custom>` trigger and use
   `ID is not set` as the :guilabel:`Before Update Domain` and `ID is set` as the
   :guilabel:`Apply on` domain. Make sure the correct field is selected in the :guilabel:`When
   updating` field.

   When a new contact is saved, it is automatically assigned a database ID, thereby triggering the
   automation rule.

   .. screenshot:: general-automation-rules-on-save-creation
      :menu: Settings ‣ Technical ‣ Automation ‣ Automation Rules
      :shows: Automation rule on the Contact model with trigger "On save", Before Update Domain
         "ID is not set", Apply on "ID is set" and the "When updating" field filled.
      :highlight: The two domains and the "When updating" field.
      :module: base_automation, contacts
      :notes: English UI, developer mode active, crop to the trigger section.

.. note::
   The :guilabel:`On UI change` trigger can only be used with the :ref:`Execute Code
   <general/automation-rules/action-execute-code>` action and only works when a modification is made
   manually. The action is not executed if the field is changed through another automation rule.

.. _general/automation-rules/trigger-external:

External
--------

Trigger automated actions based on a specific event in an external system or application using a
:doc:`webhook <automation_rules/webhooks>`.

After the webhook is configured in Odoo, where the webhook's URL is generated and the target record
defined, it needs to be implemented in the external system.

.. warning::
  It is *highly recommended* to consult with a developer, solution architect, or another technical
  role when deciding to use webhooks and throughout the implementation process. If not properly
  configured, webhooks may disrupt the Odoo database and can take time to revert.

.. screenshot:: general-automation-rules-webhook-trigger
   :menu: Settings ‣ Technical ‣ Automation ‣ Automation Rules
   :shows: Automation rule with trigger "On webhook": the generated webhook URL with copy button,
      the "Target Record" field, the "Log Calls" option and an "Update Record" action.
   :highlight: The webhook URL field.
   :module: base_automation
   :notes: English UI, developer mode active; blur the UUID part of the URL.

.. note::
   It is also possible to set up an automated action that :ref:`sends data to a external system's
   webhook <general/automation-rules/action-webhook>` when an event occurs in your Odoo database.

.. seealso::
   :doc:`Webhook documentation <automation_rules/webhooks>`

.. _general/automation-rules/action:

Actions
=======

Once you have defined the automation rule's :ref:`trigger <general/automation-rules/trigger>`, click
:guilabel:`Add an action` in the :guilabel:`Actions To Do` tab to define the action to be executed.

.. tip::
   You can define multiple actions for the same automation rule. By default, actions are executed in
   the order in which they were defined.

   This means, for example, that if you define an :guilabel:`Update record` action and then a
   :guilabel:`Send email` action where the email references the field that was updated, the email
   uses the updated values. However, if the :guilabel:`Send email` action is defined before the
   :guilabel:`Update record` action, the email uses the values set *before* the record is updated.

   To change the order of defined actions, click the :icon:`oi-draggable` :guilabel:`(drag handle)`
   icon beside an action and drag it to the desired position.

.. _general/automation-rules/action-update-record:

Update Record
-------------

This action updates one of the record's (related) fields. Click the :guilabel:`Update` field and, in
the list that opens, select or search for the field to be updated. If needed, click the
:icon:`oi-chevron-right` :guilabel:`(right arrow)` next to the field name to access the list of
related fields.

If you selected a many2many field, choose whether
the field must be updated by :guilabel:`Adding`, :guilabel:`Removing`, or :guilabel:`Setting it to`
the selected value or by :guilabel:`Clearing it`.

.. example::
   If you want the automated action to remove a tag from the customer record, set the
   :guilabel:`Update` field to :guilabel:`Customer > Tags`, select :guilabel:`by Removing`, then
   select the tag.

   .. screenshot:: general-automation-rules-update-record-tags
      :menu: Settings ‣ Technical ‣ Automation ‣ Automation Rules ‣ Add an action
      :shows: Action dialog with Type "Update Record", Update field "Customer > Tags", "by Removing"
         selected and one tag chosen.
      :highlight: The Update field and the by Adding/Removing/Setting it to/Clearing it choice.
      :module: base_automation
      :notes: English UI, crop to the dialog.

.. tip::
   Alternatively, you can also set a record's field dynamically using Python code. To do so, select
   :guilabel:`Compute` instead of :guilabel:`Update`, then enter the code to be used for computing
   the field's value. For example, if you want the automation rule to compute a custom
   datetime field when a task's priority is set to
   `High` (by starring the task), you can define the trigger :guilabel:`Priority is set to` to
   `High` and define the :guilabel:`Update Record` action as follows:

   .. screenshot:: general-automation-rules-update-record-compute
      :menu: Settings ‣ Technical ‣ Automation ‣ Automation Rules ‣ Add an action
      :shows: Action dialog with Type "Update Record", "Compute" selected instead of "Update", a
         custom datetime field of the Task model and a short Python expression.
      :highlight: The Compute toggle and the expression.
      :module: base_automation, project
      :notes: English UI, developer mode active, crop to the dialog.

.. _general/automation-rules/action-create-activity:

Create Activity
---------------

This action is used to schedule a new activity linked to the record. Select an :guilabel:`Activity
Type`, enter a :guilabel:`Title` and description, then specify when you want the activity to be
scheduled in the :guilabel:`Due Date In` field, and select a :guilabel:`User type`:

- To always assign the activity to the same user, select :guilabel:`Specific User`, then add the
  user in the :guilabel:`Responsible` field;
- To target a user linked to the record dynamically, select :guilabel:`Dynamic User (based on
  record)` and change the :guilabel:`User Field` if necessary.

.. example::
   After a lead is turned into an opportunity, you want the automated action to set up a call for
   the user responsible for the lead. To do so, set the :guilabel:`Activity Type` to
   :guilabel:`Call` and the :guilabel:`User Type` to :guilabel:`Dynamic User (based on record)`.

   .. screenshot:: general-automation-rules-create-activity
      :menu: Settings ‣ Technical ‣ Automation ‣ Automation Rules ‣ Add an action
      :shows: Action dialog with Type "Create Activity", Activity Type "Call", User Type
         "Dynamic User (based on record)" and User Field "Salesperson".
      :highlight: The Activity Type and User Type fields.
      :module: base_automation, mail, crm
      :notes: English UI, crop to the dialog.

.. _general/automation-rules/action-send-email-sms:

Send Email and Send SMS
-----------------------

These actions are used to send an email or a text message to a contact linked to a specific record.
To do so, select or create an :guilabel:`Email Template` or an :guilabel:`SMS Template`, then, in
the :guilabel:`Send Email As` or :guilabel:`Send SMS As` field, choose how you want to send the
email or text message:

- :guilabel:`Email`: to send the message as an email to the recipients of the :guilabel:`Email
  Template`.
- :guilabel:`Message`: to post the message on the record and notify the record's followers.
- :guilabel:`Note`: to send the message as an internal note visible to internal users in the
  chatter.
- :guilabel:`SMS (without note)`: to send the message as a text message to the recipients of the
  :guilabel:`SMS template`.
- :guilabel:`SMS (with note)`: to send the message as a text message to the recipients of the
  :guilabel:`SMS template` and post it as an internal note in the chatter.
- :guilabel:`Note only`: to only post the message as an internal note in the chatter.

.. _general/automation-rules/action-add-remove-followers:

Add Followers and Remove Followers
----------------------------------

This action is used to subscribe/unsubscribe existing contacts to/from the record.

.. _general/automation-rules/action-create-record:

Create Record
-------------

This action is used to create a new record on any model.

Select the required model in the :guilabel:`Record to Create` field; it contains the current model
by default. Specify a :guilabel:`Name` for the record, and then, if you want to create the record on
another model, select a field in the :guilabel:`Link Field` field to link the record that
triggered the creation of the new record.

.. note::
   The dropdown list related to the :guilabel:`Link Field` field only contains one2many fields
   existing on the current model that are linked to a many2one field on the target model.

.. tip::
   You can create another automation rule with :ref:`general/automation-rules/action-update-record`
   actions to update the fields of the new record if necessary. For example, you can use a
   :guilabel:`Create Record` action to create a new project task and then assign it to a specific
   user using an :guilabel:`Update Record` action.

.. _general/automation-rules/action-execute-code:

Execute Code
------------

.. important::
   Custom code runs with the rights of the automation rule and is not covered by standard
   upgrades. Have it written and maintained by a developer.

This action is used to execute Python code. You can write your code into the :guilabel:`Code` tab
using the following variables:

- `env`: environment on which the action is triggered
- `model`: model of the record on which the action is triggered; is a void recordset
- `record`: record on which the action is triggered; may be void
- `records`: recordset of all records on which the action is triggered in multi-mode; this may be
  left empty
- `time`, `datetime`, `dateutil`, `timezone`: useful Python libraries
- `float_compare`: utility function to compare floats based on specific precision
- `log(message, level='info')`: logging function to record debug information in ir.logging
  table
- `_logger.info(message)`: logger to emit messages in server logs
- `UserError`: exception class for raising user-facing warning messages
- `Command`: x2many commands namespace
- `action = {...}`: to return an action

.. tip::
   The available variables are described both in the :guilabel:`Code` and :guilabel:`Help` tabs.

.. seealso::
   :doc:`Odoo's ORM capabilities </developer/reference/backend/orm>`

.. _general/automation-rules/action-webhook:

Send Webhook Notification
-------------------------

This action is used to send a `POST` API request with the values of the selected :guilabel:`Fields`
to the webhook URL specified in the :guilabel:`URL` field.

The :guilabel:`Sample Payload` provides a preview of the data included in the request using a random
record's data or dummy data if no record is available.

.. note::
   It is also possible to set up an automated action that :doc:`uses a webhook to receive data from
   an external system <automation_rules/webhooks>` when a predefined event occurs in that system.

.. _general/automation-rules/action-existing-actions:

Execute Existing Actions
------------------------

The action is used to trigger multiple actions (linked to the current model) at the same time. To do
so, click on :guilabel:`Add a line`, then, in the :guilabel:`Add: Child Actions` pop-up, select an
existing action or click :guilabel:`New` to create a new one.

.. toctree::
   :titlesonly:

   automation_rules/webhooks

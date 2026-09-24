=========
Audit log
=========

The *Audit Log* module (`auditlog`) records the operations performed by the users on the data models
selected by the administrator: creations, modifications, deletions, and, optionally, consultations.
For every logged operation, the module keeps the user, the date, the record, and the old and new
value of each modified field.

Unlike the tracking messages of the :doc:`chatter <../productivity/discuss/chatter>`, the audit log
works on any model (including the ones without a chatter), covers all the fields, and can only be
consulted by authorized users.

.. note::
   The menus of the module are located under :menuselection:`Settings --> Technical --> Audit`. They
   are displayed in :ref:`developer mode <developer-mode>` to the users with the
   :guilabel:`Administration: Settings` access right.

.. _audit-log/rules:

Audit rules
===========

A rule defines which operations are logged for a model. There can only be one rule per model.

Go to :menuselection:`Settings --> Technical --> Audit --> Rules`, click :guilabel:`New`, and fill
in the fields:

- :guilabel:`Name`: the name of the rule;
- :guilabel:`Model`: the model to audit (e.g., *Contact* or *Product*);
- :guilabel:`Type`:

  - :guilabel:`Full log`: the data of the record is compared before and after the operation. The
    log also contains the computed fields that changed as a consequence of the operation, but the
    operation is slower;
  - :guilabel:`Fast log`: only the values sent by the create and write operations are logged. The
    log contains less information, but the impact on performance is lower;

- :guilabel:`Log Reads`, :guilabel:`Log Writes`, :guilabel:`Log Deletes`, :guilabel:`Log
  Creates`: the operations to log. All of them are enabled by default, except :guilabel:`Log
  Reads`;
- :guilabel:`Capture Record`: displayed for a :guilabel:`Full log` rule with :guilabel:`Log
  Deletes` enabled; tick it to keep the field values of the deleted records in the log;
- :guilabel:`Users to Exclude`: the users whose operations are not logged (e.g., a technical user
  running an integration);
- :guilabel:`Fields to Exclude`: the fields of the model that are left out of the log.

Then, click :guilabel:`Subscribe` to start logging. The rule moves to the :guilabel:`Subscribed`
status, and its fields become read-only. To modify or stop a rule, click :guilabel:`Unsubscribe`
first; the logs already recorded are kept.

.. warning::
   Logging has a cost: every logged operation creates additional records. Avoid :guilabel:`Log
   Reads` and :guilabel:`Full log` rules on models with heavy traffic (e.g., journal items, stock
   moves, or messages), and enable the :ref:`automatic clean-up <audit-log/cleanup>`.

.. screenshot:: general-audit-log-rule
   :menu: Settings ‣ Technical ‣ Audit ‣ Rules ‣ New (developer mode)
   :shows: An audit rule form in the Draft status with the Subscribe button, the model "Contact", the type "Full log", the excluded users and fields, and the four Log checkboxes (Reads unticked, the others ticked).
   :highlight: The "Subscribe" button and the four "Log ..." checkboxes (red frames).
   :data: Rule "Contacts audit"; Users to Exclude "OdooBot"; Fields to Exclude "Last Updated on".
   :module: auditlog
   :notes: English UI, light theme, 1440px width, developer mode enabled.

.. _audit-log/logs:

Consult the logs
================

From a record
-------------

As soon as a rule is subscribed, a :guilabel:`View logs` entry is added to the :icon:`fa-cog`
:guilabel:`Action` menu of the audited model. Open a record (or select it in the list view), and
click :menuselection:`Action --> View logs` to display the operations logged for that record.

This entry is the only access to the logs for the users who belong to the :guilabel:`Auditlog User`
group without being administrators.

From the Audit menu
-------------------

- :menuselection:`Settings --> Technical --> Audit --> Logs` lists all the logged operations with
  their date, :guilabel:`User`, :guilabel:`Model`, :guilabel:`Resource Name`, :guilabel:`Resource
  ID`, and method (*create*, *read*, *write*, or *unlink*). Open a log to see the
  :guilabel:`Fields updated` list, with the technical name and the description of each field, and
  its old and new value. The list can be grouped by user, model, record, date, user session, or
  HTTP request.
- :menuselection:`Settings --> Technical --> Audit --> Log Lines` lists the field changes of all the
  logs in a single list, grouped by model. It is the most convenient view to follow the successive
  values of one field.
- :menuselection:`Settings --> Technical --> Audit --> User sessions` and
  :menuselection:`Settings --> Technical --> Audit --> HTTP Requests` list the sessions and the
  requests during which logged operations took place, with the user, the path of the request, and
  the related logs. They help to reconstruct what a user did during one session.

.. screenshot:: general-audit-log-log-form
   :menu: Settings ‣ Technical ‣ Audit ‣ Logs ‣ (open a "write" log)
   :shows: A log form with the Log group (date, user, method "write", type, model, resource ID and name), the HTTP Context group, and the "Fields updated" list showing two fields with their old and new values.
   :highlight: The "Fields updated" list (red frame).
   :data: Contact "Deco Addict": Phone changed, Salesperson changed from "Marc Demo" to "Mitchell Admin".
   :module: auditlog
   :notes: English UI, light theme, 1440px width.

.. _audit-log/access:

Access rights
=============

The module adds the :guilabel:`Auditlog Rights` category to the :doc:`access rights
<users/access_rights>` of the users, with two levels:

- :guilabel:`Auditlog User`: read-only access to the logs, through the :guilabel:`View logs`
  action of the audited records;
- :guilabel:`Auditlog Manager`: in addition, can create, modify, subscribe, and delete rules, and
  delete logs. Users with the :guilabel:`Administration: Settings` access right are automatically
  managers.

.. _audit-log/cleanup:

Automatic clean-up of old logs
==============================

The *Auto-vacuum audit logs* scheduled action deletes the logs, the log lines, the user sessions,
and the HTTP requests older than 180 days. It is **disabled by default**.

To enable it, go to :menuselection:`Settings --> Technical --> Automation --> Scheduled Actions`,
open :guilabel:`Auto-vacuum audit logs`, and turn on the :guilabel:`Active` toggle. To keep the logs
for a different period, change the number of days in the code of the action, e.g.,
`model.autovacuum(365)` for one year.

.. seealso::
   - :doc:`users/access_rights`
   - :doc:`users/access_management`
   - :doc:`developer_mode`

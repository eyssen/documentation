=============
Data Cleaning
=============

The **Data Cleaning** app keeps the database free of old and outdated records: customizable rules
detect the records that have not changed for a given period of time, and either archive or delete
them.

.. note::
   The app is provided by the *Data Recycle* (``data_recycle``) module.

.. _data_cleaning/recycle:

Recycle records
===============

The :guilabel:`Recycle Records` dashboard displays the records detected by the :ref:`recycle rules
<data_cleaning/recylce-rule>`. Go to :menuselection:`Data Cleaning --> Recycle Records`.

The :guilabel:`RECYCLE RULES` sidebar lists each of the active recycle rules. By default, the
:guilabel:`All` option is selected, and the records are displayed with the following columns:

- :guilabel:`Record ID`: the ID of the original record;
- :guilabel:`Record Name`: the name or title of the original record.

Select a specific rule in the :guilabel:`RECYCLE RULES` sidebar to filter the records.

To recycle a record, click the :icon:`fa-check` :guilabel:`Validate` button on its row. Depending on
how the rule is configured, the record is then archived or deleted from the database.

.. tip::
   Discard a proposal by clicking the :icon:`fa-times` :guilabel:`Discard` button. The record is
   hidden from the list, and is not detected by the recycle rule again in the future.

   View discarded records by selecting the :guilabel:`Discarded` filter from the :ref:`search bar
   <search/filters>` drop-down menu.

.. screenshot:: productivity-data-cleaning-recycle-records
   :menu: Data Cleaning ‣ Recycle Records
   :shows: The Recycle Records dashboard with the "RECYCLE RULES" sidebar on the left and a list of records with the Record ID, Record Name columns and the Validate / Discard buttons.
   :data: Demo company "YourCompany HU"; one rule "Lead/Opportunity" with a few detected records.
   :module: data_recycle
   :notes: English UI, light theme, 1440px width.

.. _data_cleaning/recylce-rule:

Recycle record rules
--------------------

The *recycle rules* set the conditions for how records are recycled. They can be configured for each
model in the database, and with varying levels of specificity. To get started, go to
:menuselection:`Data Cleaning --> Configuration --> Rules --> Recycle Records`.

.. tip::
   Recycle rules run once a day, as part of the *Data Recycle: Clean Records* scheduled action.
   However, each rule can be :ref:`run manually <data-cleaning/run-recycle-rule>` at any time.

By default, no recycle rules exist. Click :guilabel:`New` to create one.

On the rule form, first choose a :guilabel:`Model` for the rule to target. Selecting a model updates
the rule title to the chosen model.

Optionally, configure a :guilabel:`Filter` to specify the records eligible for this rule. The number
of eligible records is shown in the :icon:`oi-arrow-right` :guilabel:`# record(s)` link.

Next, configure the field and time range the rule uses to detect the records to recycle:

- :guilabel:`Time Field`: select a date or datetime field of the model to base the time on;
- :guilabel:`Delta`: type the length of time, which must be a whole number (e.g. `7`);
- :guilabel:`Delta Unit`: select the unit of time (:guilabel:`Days`, :guilabel:`Weeks`,
  :guilabel:`Months`, or :guilabel:`Years`).

Then, select a :guilabel:`Recycle Mode`:

- :guilabel:`Manual`: each detected record must be validated manually on the :ref:`Recycle Records
  dashboard <data_cleaning/recycle>`. This mode enables the :guilabel:`Notify Users` field, where
  the administrators to inform can be selected, together with the notification frequency
  (:guilabel:`Notify` every *n* :guilabel:`Days`, :guilabel:`Weeks`, or :guilabel:`Months`).
- :guilabel:`Automatic`: the detected records are recycled automatically, without notifying users.

Lastly, select a :guilabel:`Recycle Action` to either :guilabel:`Archive` or :guilabel:`Delete` the
records. If :guilabel:`Delete` is selected, choose whether or not to :guilabel:`Include Archived`
records in the rule.

.. note::
   The :guilabel:`Archive` action is only available for models that have an :guilabel:`Active`
   field; otherwise, Odoo raises an error when the rule is saved.

With the rule's configuration complete, either close the rule form, or :ref:`run the rule manually
<data-cleaning/run-recycle-rule>` to instantly capture records to recycle.

.. example::
   A recycle rule can be configured to delete archived leads and opportunities that were last
   updated a year ago, and with a specific lost reason, by using the following configuration:

   - :guilabel:`Model`: :guilabel:`Lead/Opportunity`
   - :guilabel:`Filter`:

     - `Active` `is` `not set`
     - `Lost Reason` `is in` `Too expensive`

   - :guilabel:`Time Field`: :guilabel:`Last Updated on (Lead/Opportunity)`
   - :guilabel:`Delta`: `1`
   - :guilabel:`Delta Unit`: :guilabel:`Years`
   - :guilabel:`Recycle Mode`: :guilabel:`Automatic`
   - :guilabel:`Recycle Action`: :guilabel:`Delete`
   - :guilabel:`Include Archived`: :icon:`fa-check-square`

   .. screenshot:: productivity-data-cleaning-recycle-rule
      :menu: Data Cleaning ‣ Configuration ‣ Rules ‣ Recycle Records
      :shows: A recycle rule form for Lead/Opportunity with the Filter, Time Field, Delta, Delta Unit, Recycle Mode, Recycle Action and Include Archived fields filled in as in the example, and the "Records" smart button.
      :highlight: The Recycle Mode and Recycle Action fields (red frame).
      :data: Rule on "Lead/Opportunity", lost reason "Too expensive".
      :module: data_recycle, crm
      :notes: English UI, light theme, 1440px width.

.. _data-cleaning/run-recycle-rule:

Manually run a recycle rule
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To manually run a specific recycle rule at any time, go to :menuselection:`Data Cleaning -->
Configuration --> Rules --> Recycle Records`, and select the rule to run.

Then, on the rule form, click the :guilabel:`Run Now` button at the top left. The :icon:`fa-bars`
:guilabel:`Records` smart button then displays the number of records captured.

Click the :icon:`fa-bars` :guilabel:`Records` smart button to :ref:`manage these records
<data_cleaning/recycle>`.

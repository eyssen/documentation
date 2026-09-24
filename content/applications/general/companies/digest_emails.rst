=============
Digest emails
=============

*Digest Emails* are periodic snapshots sent via email to users in an organization that include
high-level information about how the business is performing.

To start sending digest emails, begin by navigating to :menuselection:`Settings app --> Statistics
section`, activate the :guilabel:`Digest Emails` feature, and click :guilabel:`Save`.

.. screenshot:: general-digest-settings
   :menu: Settings ‣ General Settings ‣ Statistics
   :shows: The Statistics section with the "Digest Emails" checkbox ticked, the Digest Email field
      set to "Your Odoo Periodic Digest", and the "Configure Digest Emails" link.
   :highlight: The Digest Emails setting.
   :module: digest
   :notes: English UI, crop to the section.

A variety of settings can be configured for digest emails, such as:

- Deciding which :abbr:`KPIs (key performance indicators)` are shared in the digest emails
- Determining how often digest emails are sent
- Choosing who in the organization receives digest emails
- Creating custom digest email templates
- Adding additional :abbr:`KPIs (key performance indicators)` (custom development required)

.. note::
   By default, the :guilabel:`Digest Email` feature is enabled. :guilabel:`Your Odoo Periodic
   Digest` serves as the primary template, which includes all :abbr:`KPI (key performance
   indicator)` measurements across the Odoo database, and is sent daily to administrators.

.. warning::
   When creating duplicates of databases that have sending capabilities (not testing-mode), the
   digest emails continue to send from the duplicate database, unless deactivated.

   To deactivate the digest email, navigate to :menuselection:`Settings --> Statistics section`.
   Then, deactivate the :guilabel:`Digest Emails` feature, by un-ticking the checkbox, and clicking
   :guilabel:`Save`. See the section on :ref:`digest-emails/deactivate`.

.. _digest-emails/customize-digest:

Customize default digest email
==============================

To customize the default digest email (*Your Odoo Periodic Digest*), go to :menuselection:`Settings
app --> Statistics section --> Digest Email field`. Then, select :guilabel:`Your Odoo Periodic
Digest`, and click on the :guilabel:`↗️ (External link)` icon, next to the drop-down menu selection.

A pop-up window appears, and presents a variety of editable settings, which include:

- :guilabel:`Digest Title`: the name of the digest email.
- :guilabel:`Periodicity`: control how often digest emails are sent (:guilabel:`Daily`,
  :guilabel:`Weekly`, :guilabel:`Monthly`, or :guilabel:`Quarterly`).
- :guilabel:`Next Mailing Date`: the date on which the digest email will be sent again.
- :guilabel:`KPIs` tab: check/uncheck each calculated :abbr:`KPI (key performance indicator)` that
  appears in digest emails. A ticked box indicates an active :abbr:`KPI (key performance indicator)`
  in the digest email. See the section on :ref:`digest-emails/kpis`.
- :guilabel:`Recipients` tab: add/remove users who receive the digest emails. See the section on
  :ref:`digest-emails/recipients`.

.. note::
   Additional :abbr:`KPIs (key performance indicators)` can be added with a custom module. See this
   section on :ref:`digest-emails/custom-kpi`.

.. screenshot:: general-digest-form
   :menu: Settings ‣ General Settings ‣ Statistics ‣ Digest Email ‣ (internal link)
   :shows: The "Your Odoo Periodic Digest" form: Digest Title, Periodicity, Next Mailing Date, and the
      KPIs tab with checkboxes grouped by app.
   :highlight: The KPIs tab.
   :module: digest
   :notes: English UI, crop to the form sheet.

.. _digest-emails/deactivate:

Deactivate digest email
=======================

To manually deactivate an individual digest email, first navigate to :menuselection:`Settings app
--> Statistics section`, and click :guilabel:`Configure Digest Emails`. Then, select the desired
digest email from the list that should be deactivated.

Next, click :guilabel:`Deactivate` to deactivate the digest email for everyone. A deactivated digest
can be reactivated with the :guilabel:`Activate` button. Both buttons are located at the top of the
form, next to the :guilabel:`Send Now` button, which sends the digest immediately.

.. tip::
   A recipient can stop receiving a digest by clicking the :guilabel:`Unsubscribe` link at the
   bottom of the digest email.

Manually send digest email
==========================

To manually send a digest email, first navigate to :menuselection:`Settings app --> Statistics
section`, and click :guilabel:`Configure Digest Emails`. Then, select the desired digest email, and
click :guilabel:`SEND NOW`. This button is located in the top menu, just above the :guilabel:`Digest
Name`.

.. _digest-emails/kpis:

KPIs
====

Pre-configured :abbr:`KPIs (key performance indicators)` can be added to the digest email from the
:guilabel:`KPIs` tab of the digest email template form.

First, navigate to :menuselection:`Settings app --> Statistics section`, and click
:guilabel:`Configure Digest Emails`.

Then, select the desired digest email, and open the :guilabel:`KPIs` tab.

To add a :abbr:`KPI (key performance indicator)` to the digest email, tick the checkbox next to the
desired :abbr:`KPI (key performance indicator)`. After all :abbr:`KPIs (key performance indicators)`
are added (or deselected), click :guilabel:`Save`.

The following :abbr:`KPIs (key performance indicators)` are available in the :guilabel:`KPIs` tab on
a digest email template form out-of-box in Odoo:

.. screenshot:: general-digest-kpis
   :menu: Settings ‣ Statistics ‣ Configure Digest Emails ‣ (digest)
   :shows: The KPIs tab of a digest listing the available KPIs grouped under General, Project,
      Recruitment, CRM, Sales, Point of Sale, Live Chat and Invoicing.
   :module: digest
   :notes: English UI, crop to the KPIs tab; displayed on the right of the list.

:guilabel:`General`
   - :guilabel:`Connected Users`
   - :guilabel:`Messages Sent`

:guilabel:`Project`
   - :guilabel:`Open Tasks`

:guilabel:`Recruitment`
   - :guilabel:`New Employees`

:guilabel:`CRM`
   - :guilabel:`New Leads`
   - :guilabel:`Opportunities Won`

:guilabel:`Sales`
   - :guilabel:`All Sales`
   - :guilabel:`eCommerce Sales`

:guilabel:`Point of Sale`
   - :guilabel:`POS Sales`

:guilabel:`Live Chat`
   - :guilabel:`% of Happiness`
   - :guilabel:`Conversations handled`
   - :guilabel:`Time to answer (sec)`

:guilabel:`Invoicing`
   - :guilabel:`Revenue`

.. note::
   The KPIs of an app are only available if the app is installed.

.. _digest-emails/recipients:

Recipients
==========

Digest email recipients are added from the :guilabel:`Recipients` tab of the digest email template
form.

To add a recipient, navigate to :menuselection:`Settings app --> Statistics section`, and click
:guilabel:`Configure Digest Emails`. Then, select the desired digest email, and open the
:guilabel:`Recipients` tab.

To add a recipient, click :guilabel:`Add a line`, and an :guilabel:`Add Recipients` pop-up window
appears, with all available users to add as recipients.

From the pop-up window, tick the checkbox next to the :guilabel:`Name` of the user(s), and click the
:guilabel:`Select` button.

To remove a user as a recipient, click the :guilabel:`❌ (remove)` icon to the far-right of the user
listed in the :guilabel:`Recipients` tab.

Click :guilabel:`Save` to implement the changes.

.. _digest-emails/custom-emails:

Create digest emails
====================

To create a new digest email, navigate to :menuselection:`Settings app --> Statistics section`, and
click :guilabel:`Configure Digest Emails`. Then, click :guilabel:`New` to create a new digest
email.

A separate page, with a blank digest email template appears, and presents a variety of editable
settings, including:

- :guilabel:`Digest Title`: the name of the digest email.
- :guilabel:`Periodicity`: control how often digest emails are sent (:guilabel:`Daily`,
  :guilabel:`Weekly`, :guilabel:`Monthly`, or :guilabel:`Quarterly`).
- :guilabel:`Next Mailing Date`: the date on which the digest email will be sent again.
- :guilabel:`KPIs` tab: check/uncheck each calculated :abbr:`KPI (key performance indicator)` that
  appears in digest emails. A ticked box indicates an active :abbr:`KPI (key performance indicator)`
  in the digest email. See the section on :ref:`digest-emails/kpis`.
- :guilabel:`Recipients` tab: add/remove users who receive the digest emails. See the section on
  :ref:`digest-emails/recipients`.

From there, give the digest email a :guilabel:`Digest Title`, specify :guilabel:`Periodicity`,
choose the desired :abbr:`KPIs (key performance indicators)`, and add :guilabel:`Recipients`, as
needed.

After clicking :guilabel:`Save`, the new custom digest email is available as a selection in the
:guilabel:`Digest Email` field, located in the :menuselection:`Settings app --> Statistics section`.

.. _digest-emails/custom-kpi:

Custom KPIs
===========

Additional :abbr:`KPIs (key performance indicators)` can be added to the :guilabel:`KPIs` tab of the
digest email template form by a developer, in a custom module. For each new KPI, two fields are
needed on the digest model (`digest.digest`):

#. A boolean field, e.g., `kpi_myfield`, displayed in the :guilabel:`KPIs` tab, to enable the KPI.
#. A computed field, e.g., `kpi_myfield_value`, that computes the value of the KPI.

Once the module is installed, the new KPI can be selected in the :guilabel:`KPIs` tab.

.. tip::
   The `digest.py` file of the *Digest* module (`digest/models/digest.py`) and the modules that add
   the standard KPIs (e.g., `crm`, `sale`, `project`) can be used as examples for the computed
   fields.

Computed values reference table
-------------------------------

+-----------------------+-------------------------------------------+
| LABEL                 | VALUE                                     |
+=======================+===========================================+
| Connected Users       | `kpi_res_users_connected_value`           |
+-----------------------+-------------------------------------------+
| Messages Sent         | `kpi_mail_message_total_value`            |
+-----------------------+-------------------------------------------+
| New Leads             | `kpi_crm_lead_created_value`              |
+-----------------------+-------------------------------------------+
| Opportunities Won     | `kpi_crm_opportunities_won_value`         |
+-----------------------+-------------------------------------------+
| Open Tasks            | `kpi_project_task_opened_value`           |
+-----------------------+-------------------------------------------+
| % of Happiness        | `kpi_livechat_rating_value`               |
+-----------------------+-------------------------------------------+
| Conversations handled | `kpi_livechat_conversations_value`        |
+-----------------------+-------------------------------------------+
| Time to answer (sec)  | `kpi_livechat_response_value`             |
+-----------------------+-------------------------------------------+
| All Sales             | `kpi_all_sale_total_value`                |
+-----------------------+-------------------------------------------+
| eCommerce Sales       | `kpi_website_sale_total_value`            |
+-----------------------+-------------------------------------------+
| Revenue               | `kpi_account_total_revenue_value`         |
+-----------------------+-------------------------------------------+
| POS Sales             | `kpi_pos_total_value`                     |
+-----------------------+-------------------------------------------+
| New Employees         | `kpi_hr_recruitment_new_colleagues_value` |
+-----------------------+-------------------------------------------+

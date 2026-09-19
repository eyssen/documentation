============
SMS analysis
============

On the :guilabel:`Reporting` page (accessible via the :menuselection:`Reporting` option in the
header menu), there are options to apply different combinations of :guilabel:`Filters` and
:guilabel:`Measures` to view metrics in a number of different layouts (e.g. :guilabel:`Graph`
and :guilabel:`List` views).

Each :guilabel:`Reporting` metric view option allows for more extensive performance analysis of
:abbr:`SMS (Short Message Service)` mailings.

For example, while in the default :guilabel:`Graph` view, :abbr:`SMS (Short Message Service)` data
is visualized as different graphs and charts, which can be sorted and grouped in various ways (e.g.
:guilabel:`Measures` drop down menu).

.. screenshot:: sms-sms-analysis-sms-reporting-page
   :menu: SMS Marketing ‣ Reporting
   :shows: The SMS Marketing reporting page in graph view with the Measures drop-down menu open.
   :highlight: The Measures drop-down menu (red frame).
   :data: Data from three sent SMS mailings.
   :module: mass_mailing_sms
   :notes: English UI, light theme, 1440px width.

.. tip::
   SMS messages can be sent using :doc:`automation rules
   </applications/general/automation_rules>`. To create one, activate the :ref:`developer mode
   <developer-mode>`, open the model's list or form view, and select :menuselection:`(gear icon) -->
   Automations`.

   Enter a name for the automation rule, and select a :guilabel:`Model` to implement this rule on.

   Based on the selection for the :guilabel:`Trigger`, additional fields will populate below. Set
   the :guilabel:`Trigger` to one of the following options:

   :guilabel:`Values Updated`

   - :guilabel:`User is set`
   - :guilabel:`State is set to`
   - :guilabel:`On archived`
   - :guilabel:`On unarchived`

   :guilabel:`Timing Conditions`

   - :guilabel:`Based on date field`
   - :guilabel:`After creation`
   - :guilabel:`After last update`

   :guilabel:`Custom`

   - :guilabel:`On save`
   - :guilabel:`On deletion`
   - :guilabel:`On UI change`

   :guilabel:`External`

   - :guilabel:`On webhook`

   Other options may appear based on the :guilabel:`Model` selected. For example if the
   :guilabel:`Calendar Event` model is selected, then the following options appear in addition to
   those above:

   :guilabel:`Email Events`

   - :guilabel:`On incoming message`
   - :guilabel:`On outgoing message`

   Under the :guilabel:`Before Update Domain` field, set a condition to be met before updating the
   record. Click :guilabel:`Edit Domain` to set record parameters.

   Under the :guilabel:`Actions To Do` tab, select :guilabel:`Add an action`. Next, in the resulting
   :guilabel:`Create Actions` pop-up window, select :guilabel:`Send SMS`, and set the
   :guilabel:`Allowed Groups`. :guilabel:`Allowed Groups` are the access rights groups that are
   allowed to execute this rule. Leave the field empty to allow all groups. See this documentation:
   :ref:`access-rights/groups`.

   Next, set the :guilabel:`SMS Template` and choose whether the SMS message should be logged as a
   note, by making a selection in the drop-down menu: :guilabel:`Send SMS as`. Click
   :guilabel:`Save and Close` to save the changes to this new action.

   .. screenshot:: sms-sms-analysis-automation-rule-sms
      :menu: Settings ‣ Technical ‣ Automation Rules ‣ New
      :shows: An automation rule form with a trigger set, and an action 'Send SMS' added in the Actions To Do tab with an SMS template selected.
      :highlight: The 'Send SMS' action line and its SMS Template field (red frame).
      :data: Model 'Sales Order', trigger 'On save'.
      :module: mass_mailing_sms
      :notes: English UI, light theme, 1440px width.

   Add any necessary notes under the :guilabel:`Notes` tab. Finally, navigate away from the
   completed automation rule, or manually save (by clicking the :guilabel:`☁️ (cloud)` icon), to
   implement the change.

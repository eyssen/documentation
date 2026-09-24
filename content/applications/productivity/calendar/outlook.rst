================================
Outlook Calendar synchronization
================================

Synchronizing a user's *Outlook Calendar* with Odoo is useful for keeping track of tasks and
appointments across all related applications.

.. seealso::
   - :doc:`../../general/users/azure`
   - :doc:`../../general/email_communication/azure_oauth`

Microsoft Azure setup
=====================

To sync the *Outlook Calendar* with Odoo's *Calendar*, a Microsoft *Azure* account is required.
Creating an account is free for users who have never tried, or paid for, *Azure*. For more
information, view the account options on the `Azure website
<https://azure.microsoft.com/en-us/free/?WT.mc_id=A261C142F>`_.

Refer to `Microsoft's documentation <https://docs.microsoft.com/en-us/azure/active-directory/
develop/quickstart-create-new-tenant>`_ on how to set up a Microsoft *Entra ID* (formally called
Microsoft *Azure Active Directory (Azure AD)*). This is an API console to manage and register
Microsoft applications.

Existing Microsoft *Entra ID* users should log in at the `Microsoft Azure developer portal
<https://portal.azure.com/#home>`_. Next, select :guilabel:`View` under the section labeled
:guilabel:`Manage Microsoft Entra ID`.

Register application
--------------------

After logging in with the Microsoft *Entra ID*, `register an application
<https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app>`_.

To create an application, click :guilabel:`+ Add` in the top menu. From the resulting drop-down
menu, select :guilabel:`App Registration`.

.. screenshot:: outlook-calendar-app-register
   :menu: (Microsoft Entra admin center) ‣ App registrations
   :shows: The Microsoft Entra ID app registrations page with the "+ New registration" button.
   :highlight: The "New registration" button (red frame).
   :module: microsoft_calendar
   :notes: English UI, light theme, 1440px width.

Enter a unique :guilabel:`Name` for the connected application.

Choosing the appropriate :guilabel:`Supported account type` is essential, or else the connected
application will not work. Users who wish to connect their *Outlook Calendar* to Odoo should select
the :guilabel:`Accounts in any organizational directory (Any Microsoft Entra ID directory -
Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)` option for :guilabel:`Supported
account types`.

When configuring the :guilabel:`Redirect URI`, choose the :guilabel:`Web` option from the first
drop-down menu. Then, enter the Odoo database URI (URL) followed by
`/microsoft_account/authentication`.

.. example::
   Enter `https://yourdbname.odoo.com/microsoft_account/authentication` for the :guilabel:`Redirect
   URI`. Replace `yourdbname.odoo.com` with the :abbr:`URL (Uniform Resource Locator)`.

.. tip::
   Ensure the database's :abbr:`URL (Uniform Resource Locator)` (domain) used in the URI is the
   exact same domain as the one configured on the `web.base.url` system parameter.

   Access the `web.base.url` by activating :ref:`developer mode <developer-mode>`, and navigating to
   :menuselection:`Settings app --> Technical header menu --> Parameters section --> System
   Parameters`. Then, select it from the :guilabel:`Key` list on the :guilabel:`System Parameters`
   page.

.. screenshot:: outlook-calendar-register-application
   :menu: (Microsoft Entra admin center) ‣ App registrations ‣ New registration
   :shows: The application registration form with the name, the "Supported account types" option selected and the redirect URI of the database.
   :highlight: The "Supported account types" and "Redirect URI" fields (red frame).
   :data: Redirect URI https://company-name.com/microsoft_account/authentication.
   :module: microsoft_calendar
   :notes: English UI, light theme, 1440px width.

For more information on the restrictions and limitations of URIs, check Microsoft's `Redirect URI
(reply URL) restrictions and limitations
<https://docs.microsoft.com/en-us/azure/active-directory/develop/reply-url>`_ page.

Finally, on the application registration page, click :guilabel:`Register` button to complete the
application registration. The :guilabel:`Application (client) ID` is produced. Copy this value, as
it is needed later, in the :ref:`outlook_calendar/odoo_setup`.

.. screenshot:: outlook-calendar-client-id
   :menu: (Microsoft Entra admin center) ‣ App registrations ‣ Overview
   :shows: The Essentials section of the registered application, showing the Application (client) ID.
   :highlight: The "Application (client) ID" value (red frame).
   :data: Use a throw-away application.
   :module: microsoft_calendar
   :notes: English UI, light theme, 1440px width.

Create client secret
--------------------

The second credential needed to complete the synchronization of the Microsoft *Outlook Calendar* is
the *Client Secret*. The user **must** add a client secret, as this allows Odoo to authenticate
itself, requiring no interaction from the user's side. *Certificates* are optional.

To add a client secret, click :menuselection:`Certificates & secrets` in the left menu. Then click
:guilabel:`+ New client secret` to create the client secret.

.. screenshot:: outlook-calendar-new-client-secret
   :menu: (Microsoft Entra admin center) ‣ Certificates & secrets
   :shows: The "Certificates & secrets" page with the "+ New client secret" option and the description and expiry fields of the new secret.
   :highlight: The "New client secret" button (red frame).
   :module: microsoft_calendar
   :notes: English UI, light theme, 1440px width.

Next, type a :guilabel:`Description`, and select when the client secret :guilabel:`Expires`.
Available options include: :guilabel:`90 days (3 months)`, :guilabel:`365 days (12 months)`,
:guilabel:`545 days (18 months)`, :guilabel:`730 days (24 months)` or :guilabel:`Custom`. The
:guilabel:`Custom` option allows the administrator to set a :guilabel:`Start` and :guilabel:`End`
date.

Finally, click :guilabel:`Add` to :guilabel:`Add a client secret`.

.. tip::
   Since resetting the synchronization can be tricky, Odoo recommends setting the maximum allowed
   expiration date for the client secret (24 months or custom), so there is no need to
   re-synchronize soon.

Copy the :guilabel:`Value` for use in the next section.

.. warning::
   Client secret values cannot be viewed, except immediately after creation. Be sure to save the
   secret when created *before* leaving the page.

.. _outlook_calendar/odoo_setup:

Configuration in Odoo
=====================

In the Odoo database, go to :menuselection:`Calendar app --> Configuration --> Settings`, and tick
the checkbox beside the :guilabel:`Outlook Calendar` setting. Remember to click :guilabel:`Save` to
implement the changes.

.. screenshot:: outlook-calendar-odoo-setting
   :menu: Settings ‣ General Settings ‣ Integrations
   :shows: The Integrations section of the General Settings with the "Outlook Calendar" checkbox enabled and the Client ID and Client Secret fields below it.
   :highlight: The "Outlook Calendar" setting (red frame).
   :data: Use a throw-away client ID and secret.
   :module: microsoft_calendar
   :notes: English UI, light theme, 1440px width.

From the Microsoft *Azure* portal, under the :guilabel:`Overview` section of the application, copy
the :guilabel:`Application (Client) ID`, if it has not already been copied, and paste it into the
:guilabel:`Client ID` field in Odoo.

.. screenshot:: outlook-calendar-copy-client-id
   :menu: (Microsoft Entra admin center) ‣ App registrations ‣ Overview
   :shows: The Application (client) ID being copied from the application overview page.
   :module: microsoft_calendar
   :notes: English UI, light theme, 1440px width.

Copy the previously-acquired :guilabel:`Value` (Client Secret Value), and paste it into the
:guilabel:`Client Secret` field in Odoo.

.. screenshot:: outlook-calendar-secret-value
   :menu: (Microsoft Entra admin center) ‣ Certificates & secrets
   :shows: The client secret list with the Value column that has to be copied into Odoo.
   :highlight: The "Value" column (red frame).
   :data: Use a throw-away secret.
   :module: microsoft_calendar
   :notes: English UI, light theme, 1440px width.

Finally, on the Odoo :menuselection:`Settings --> General Settings` page, click :guilabel:`Save`.

.. _outlook/sync:

Sync with Outlook
=================

.. warning::

   Odoo highly recommends testing the Outlook calendar synchronization on a test database and a
   test email address (that is not used for any other purpose) before attempting to sync the
   desired Outlook Calendar with the user's production database.

   If the user has any past, present, or future events on their Odoo calendar before syncing their
   Outlook calendar, Outlook will treat the events pulled from Odoo's calendar during the sync as
   new events, causing an email notification to be sent from Outlook to all the event attendees.

   To avoid unwanted emails being sent to all past, present, and future event attendees, the user
   must add the events from the Odoo calendar to the Outlook calendar before the first ever sync,
   delete the events from Odoo, and then start the sync.

   Even after synchronizing the Odoo Calendar with the Outlook calendar, Outlook will still send a
   notification to all event participants every time an event is edited (created, deleted,
   unarchived, or event date/time changed), with no exceptions. This is a limitation that cannot be
   fixed from Odoo's side.

   In summary, once a user synchronizes their Outlook calendar with the Odoo calendar:

   - Creating an event in Odoo causes Outlook to send an invitation to all event attendees.
   - Deleting an event in Odoo causes Outlook to send a cancellation to all event attendees.
   - Unarchiving an event in Odoo causes Outlook to send an invitation to all event attendees.
   - Archiving an event in Odoo causes Outlook to send a cancellation to all event attendees.
   - Adding a contact to an event causes Outlook to send an invitation to all event attendees.
   - Removing a contact from an event causes Outlook to send a cancellation to all event attendees.

Sync Odoo Calendar and Outlook
------------------------------

In the Odoo database, open to the *Calendar* module, and click the :guilabel:`Outlook` sync button
on the right-side of the page, beneath the monthly calendar.

.. screenshot:: outlook-calendar-sync-button
   :menu: Calendar
   :shows: The Calendar app with the "Outlook" synchronization button in the side panel.
   :highlight: The "Outlook" button (red frame).
   :module: microsoft_calendar
   :notes: English UI, light theme, 1440px width.

The synchronization is a two-way process, meaning that events are reconciled in both accounts
(*Outlook* and Odoo). The page redirects to a Microsoft login page, and the user is asked to log in
to their account, if they are not already. Finally, grant the required permissions by clicking
:guilabel:`Accept`.

.. screenshot:: outlook-calendar-consent
   :menu: (Microsoft account consent screen)
   :shows: The Microsoft authentication page asking to grant the application access to the account's calendar.
   :data: Use a throw-away Microsoft test account.
   :module: microsoft_calendar
   :notes: English UI, light theme, 1440px width.

.. note::
   All users that want to use the synchronization simply need to :ref:`sync their calendar with
   Outlook <outlook/sync>`. The configuration of Microsoft's *Azure* account is only done once, as
   Microsoft *Entra ID* tenants' client IDs and client secrets are unique, and help the user manage
   a specific instance of Microsoft cloud services for internal and external users.

.. seealso::
   - :doc:`../../general/integrations/mail_plugins/outlook`
   - :doc:`google`

Troubleshoot sync
=================

There may be times when the *Microsoft Outlook Calendar* account does not sync correctly with Odoo.
Sync issues can be seen in the database logs.

In these cases, the account needs troubleshooting. A reset can be performed using the
:guilabel:`Reset Account` button, which can be accessed by navigating to :menuselection:`Settings
app --> Manage Users`. Then, select the user to modify the calendar, and click on the
:guilabel:`Calendar` tab.

.. screenshot:: outlook-calendar-reset-buttons
   :menu: Settings ‣ Users & Companies ‣ Users
   :shows: The Calendar tab of a user form with the "Reset Account" buttons of the synchronized calendars.
   :highlight: The "Reset Account" button (red frame).
   :module: microsoft_calendar
   :notes: English UI, light theme, 1440px width.

Next, click :guilabel:`Reset Account` under the correct calendar.

Reset options
-------------

The following reset options are available for troubleshooting *Microsoft Outlook Calendar* sync with
Odoo:

.. screenshot:: outlook-calendar-reset-options
   :menu: Settings ‣ Users & Companies ‣ Users
   :shows: The Outlook calendar reset dialog with the "User's Existing Events" and synchronization options.
   :module: microsoft_calendar
   :notes: English UI, light theme, 1440px width.

:guilabel:`User's Existing Events`:

 - :guilabel:`Leave them untouched`: no changes to the events.
 - :guilabel:`Delete from the current Microsoft Calendar account`: delete the events from *Microsoft
   Outlook Calendar*.
 - :guilabel:`Delete from Odoo`: delete the events from the Odoo calendar.
 - :guilabel:`Delete from both`: delete the events from both *Microsoft Outlook Calendar* and Odoo
   calendar.

:guilabel:`Next Synchronization`:

 - :guilabel:`Synchronize only new events`: sync new events on *Microsoft Outlook Calendar* and/or
   Odoo calendar.
 - :guilabel:`Synchronize all existing events`: sync all events on *Microsoft Outlook Calendar*
   and/or Odoo calendar.

Click :guilabel:`Confirm` after making the selection to modify the user's events and the calendar
synchronization.


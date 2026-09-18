===============================
Google Calendar synchronization
===============================

Synchronize Google Calendar with Odoo to see and manage meetings from both platforms (updates go in
both directions). This integration helps organize schedules, so a meeting is never missed.

.. seealso::
   - :doc:`/applications/general/users/google`
   - :doc:`/applications/general/email_communication/google_oauth`

Setup in Google
===============

Select (or create) a project
----------------------------

Create a new Google API project and enable the Google Calendar API. First, go to the `Google API
Console <https://console.developers.google.com>`_ and log into the Google account.

.. note::
   If this is the first time visiting this page, Google will prompt the user to enter a country and
   agree to the Terms of Service. Select a country from the drop-down list and agree to the
   :abbr:`ToS (Terms of Service)`.

Next, click :guilabel:`Select a project` and select (or create) an API project to configure OAuth
in, and store credentials. Click :guilabel:`New Project`.

.. screenshot:: google-calendar-new-api-project
   :menu: (Google Cloud console) ‣ Select a project
   :shows: The Google Cloud console project selector with the "New project" button, used to create the API project.
   :data: Project name "Odoo Sync".
   :module: google_calendar
   :notes: English UI, light theme, 1440px width.

Give the API project a clear name, like `Odoo Sync`, so it can be identified. Then click the
:guilabel:`Create` button.

Enable Google calendar API
--------------------------

Now, click on :guilabel:`Enabled APIs and Services` in the left menu. Select :guilabel:`Enabled APIs
and Services` again if the :guilabel:`Search bar` does not appear.

.. screenshot:: google-calendar-enable-apis
   :menu: (Google Cloud console) ‣ APIs & Services ‣ Enabled APIs and Services
   :shows: The "Enabled APIs & Services" page with the "+ ENABLE APIS AND SERVICES" button.
   :highlight: The "Enable APIs and Services" button (red frame).
   :module: google_calendar
   :notes: English UI, light theme, 1440px width.

After that, search for `Google Calendar API` using the search bar and select :guilabel:`Google
Calendar API` from the search results. Click :guilabel:`Enable`.

.. screenshot:: google-calendar-enable-calendar-api
   :menu: (Google Cloud console) ‣ API Library ‣ Google Calendar API
   :shows: The Google Calendar API page of the API library with the "Enable" button.
   :highlight: The "Enable" button (red frame).
   :module: google_calendar
   :notes: English UI, light theme, 1440px width.

OAuth consent screen
--------------------

Now that the API project has been created, OAuth should be configured. To do that, click on
:guilabel:`OAuth consent screen` in the left menu, then click the :guilabel:`Get started` button.

.. warning::
   *Personal* Gmail Accounts are only allowed to be **External** User Type, which means Google may
   require an approval, or for *Scopes* to be added on. However, using a *Google WorkSpace* account
   allows for **Internal** User Type to be used.

   Note, as well, that while the API connection is in the *External* testing mode, then no approval
   is necessary from Google. User limits in this testing mode is set to 100 users.

Follow the proceeding steps, in order:

#. In :guilabel:`App Information`, type `Odoo` in the :guilabel:`App name` field, then enter the
   email address for the :guilabel:`User support email` field and click the :guilabel:`Next` button.
#. In :guilabel:`Audience`, select :guilabel:`External`, then click the :guilabel:`Next` button.
#. In :guilabel:`Contact Information`, enter the email again, then click the :guilabel:`Next`
   button.
#. In :guilabel:`Finish`, tick the checkbox to agree to :guilabel:`Google API Services: User
   Policy.` For the last step, click the :guilabel:`Create` button.

Authorized domain setup
-----------------------

Next, any domains set to appear on the consent screen or in an OAuth client's configuration must be
pre-registered. To do so, navigate to :guilabel:`Branding` in the left menu. In the
:guilabel:`Authorized domains` section, click the :guilabel:`Add domain` button to create a field to
enter an authorized domain. Enter a domain, such as `odoo.com`, then click the :guilabel:`Save`
button at the bottom of the page.

Test users
----------

To give users the ability to sync with personal Gmail accounts, they must be set as a test user.
Setup test users by going to :guilabel:`Audience` in the left-side menu and clicking the
:guilabel:`Add users` button in the :guilabel:`Test users` section. Enter any desired user emails,
and click the :guilabel:`Save` button.

Create credentials
------------------

The *Client ID* and the *Client Secret* are both needed to connect Google Calendar to Odoo. This is
the last step in the Google console. Begin by clicking :guilabel:`Clients` in the left menu.
Then, click :guilabel:`Create Credentials`, and select :guilabel:`OAuth client ID`, Google will open
a guide to create credentials.

Under :menuselection:`Create OAuth Client ID`, select :guilabel:`Website application` for the
:guilabel:`Application Type` field, and type `My Odoo Database` for the :guilabel:`Name`.

- Under the :guilabel:`Authorized JavaScript Origins` section, click :guilabel:`+ Add URI` and type
  the company's Odoo full :abbr:`URL (Uniform Resource Locator)` address.
- Under the :guilabel:`Authorized redirect URIs` section, click :guilabel:`+ Add URI` and type the
  company's Odoo :abbr:`URL (Uniform Resource Locator)` address followed by
  `/google_account/authentication`. Finally, click :guilabel:`Create`.

.. screenshot:: google-calendar-oauth-uris
   :menu: (Google Cloud console) ‣ APIs & Services ‣ Credentials ‣ Create OAuth client ID
   :shows: The OAuth client creation form with the authorized JavaScript origins and the authorized redirect URIs filled in with the database URL.
   :highlight: The two URI fields (red frame).
   :data: Database URL https://company-name.com and .../google_account/authentication.
   :module: google_calendar
   :notes: English UI, light theme, 1440px width.

A :guilabel:`Client ID` and :guilabel:`Client Secret` will appear, save these somewhere safe.

Setup in Odoo
=============

Once the *Client ID* and the *Client Secret* are located, open the Odoo database and go to
:menuselection:`Settings --> Calendar` to find the :guilabel:`Google Calendar` feature. Tick the
checkbox labeled :guilabel:`Google Calendar`.

.. screenshot:: google-calendar-odoo-settings
   :menu: Settings ‣ General Settings ‣ Integrations
   :shows: The Integrations section of the General Settings with the "Google Calendar" checkbox enabled and the Client ID and Client Secret fields below it.
   :highlight: The "Google Calendar" setting (red frame).
   :data: Use a throw-away client ID and secret.
   :module: google_calendar
   :notes: English UI, light theme, 1440px width.

Next, copy and paste the *Client ID* and the *Client Secret* from the Google Calendar API
credentials page into their respective fields below the :guilabel:`Google Calendar` checkbox. Then,
click :guilabel:`Save`.

.. note::
   Tick the :guilabel:`Pause Synchronization` checkbox to temporarily pause events from being
   updated. This allows for testing and troubleshooting without removing credentials or uninstalling
   the synchronization. To resume the sync, clear the checkbox and save.

Sync calendar in Odoo
=====================

Finally, open the :menuselection:`Calendar` app in Odoo and click on the :guilabel:`Google` sync
button to sync Google Calendar with Odoo.

.. screenshot:: google-calendar-sync-button
   :menu: Calendar
   :shows: The Calendar app with the "Google" synchronization button in the side panel.
   :highlight: The "Google" button (red frame).
   :module: google_calendar
   :notes: English UI, light theme, 1440px width.

.. note::
   When syncing Google Calendar with Odoo for the first time, the page will redirect to the Google
   Account. From there, select the :guilabel:`Email Account` that should have access, then select
   :guilabel:`Continue` (should the app be unverified), and finally select :guilabel:`Continue` (to
   give permission for the transfer of data).

.. screenshot:: google-calendar-consent
   :menu: (Google account consent screen)
   :shows: The Google consent screen asking to grant access to the Google Calendar of the account.
   :data: Use a throw-away Google test account.
   :module: google_calendar
   :notes: English UI, light theme, 1440px width.

Now, Odoo Calendar is successfully synced with Google Calendar!

.. warning::
   Odoo highly recommends testing the Google calendar synchronization on a test database and a test
   email address (that is not used for any other purpose) before attempting to sync the desired
   Google Calendar with the user's production database.

   Once a user synchronizes their Google calendar with the Odoo calendar:

   - Creating an event in Odoo causes Google to send an invitation to all event attendees.
   - Deleting an event in Odoo causes Google to send a cancellation to all event attendees.
   - Adding a contact to an event causes Google to send an invitation to all event attendees.
   - Removing a contact from an event causes Google to send a cancellation to all event attendees.

   Events can be created in *Google Calendar* without sending a notification by selecting
   :guilabel:`Don't Send` when prompted to send invitation emails.

Troubleshoot sync
=================

There may be times when the *Google Calendar* account does not sync correctly with Odoo. Sync issues
can be seen in the database logs.

In these cases, the account needs troubleshooting. A reset can be performed using the
:guilabel:`Reset Account` button, which can be accessed by navigating to :menuselection:`Settings
app --> Manage Users`. Then, select the user to modify the calendar, and click the
:guilabel:`Calendar` tab.

.. screenshot:: google-calendar-reset-buttons
   :menu: Settings ‣ Users & Companies ‣ Users
   :shows: The Calendar tab of a user form with the "Reset Account" buttons of the synchronized calendars.
   :highlight: The "Reset Account" button (red frame).
   :module: google_calendar
   :notes: English UI, light theme, 1440px width.

Next, click :guilabel:`Reset Account` under the correct calendar.

Reset options
-------------

The following reset options are available for troubleshooting Google calendar sync with Odoo:

.. screenshot:: google-calendar-reset-options
   :menu: Settings ‣ Users & Companies ‣ Users
   :shows: The Google calendar reset dialog with the "User's Existing Events" and synchronization options.
   :module: google_calendar
   :notes: English UI, light theme, 1440px width.

:guilabel:`User's Existing Events`:

 - :guilabel:`Leave them untouched`: no changes to the events.
 - :guilabel:`Delete from the current Google Calendar account`: delete the events from *Google
   Calendar*.
 - :guilabel:`Delete from Odoo`: delete the events from the Odoo calendar.
 - :guilabel:`Delete from both`: delete the events from both *Google Calendar* and Odoo calendar.

:guilabel:`Next Synchronization`:

 - :guilabel:`Synchronize only new events`: sync new events on *Google Calendar* and/or Odoo
   calendar.
 - :guilabel:`Synchronize all existing events`: sync all events on *Google Calendar* and/or Odoo
   calendar.

Click :guilabel:`Confirm` after making the selection to modify the user's events and the calendar
synchronization.

Google OAuth FAQ
================

At times there can be configuration errors that occur, and troubleshooting is needed to resolve the
issue. Below are the most common errors that may occur when configuring the *Google Calendar* for
use with Odoo.

Production vs. testing publishing status
----------------------------------------

Choosing :guilabel:`Production` as the :guilabel:`Publishing Status` (instead of
:guilabel:`Testing`) displays the following warning message:

`OAuth is limited to 100 sensitive scope logins until the OAuth consent screen is verified. This may
require a verification process that can take several days.`

To correct this warning, navigate to the `Google API Platform
<https://console.cloud.google.com/apis/credentials/consent>`_. If the :guilabel:`Publishing Status`
is :guilabel:`In Production`, click :guilabel:`Back to Testing` to correct the issue.

No test users added
-------------------

If no test users are added to the :guilabel:`OAuth consent screen`, then an :guilabel:`Error 403:
access_denied` populates.

.. screenshot:: google-calendar-error-403
   :menu: (Google account consent screen)
   :shows: The "403: access_denied" error page shown when the user is not a test user of the API project.
   :data: Use a throw-away Google test account.
   :module: google_calendar
   :notes: English UI, light theme, 1440px width.

To correct this error, return to the :guilabel:`OAuth consent screen`, under :guilabel:`APIs &
Services`, and add test users to the app. Add the email to be configured in Odoo.

Application Type
----------------

When creating the credentials (OAuth *Client ID* and *Client Secret*), if :guilabel:`Desktop App` is
selected for the :guilabel:`Application Type`, an :guilabel:`Authorization Error` appears
(:guilabel:`Error 400:redirect_uri_mismatch`).

.. screenshot:: google-calendar-error-400
   :menu: (Google account consent screen)
   :shows: The "400: redirect_uri_mismatch" error page shown when the redirect URI does not match the one configured in the credentials.
   :module: google_calendar
   :notes: English UI, light theme, 1440px width.

To correct this error, delete the existing credentials, and create new credentials, by selecting
:guilabel:`Web Application` for the :guilabel:`Application Type`.

Then, under :guilabel:`Authorized redirect URIs`, click :guilabel:`ADD URI`, and type:
`https://yourdbname.odoo.com/google_account/authentication` in the field, being sure to replace
*yourdbname* in the URL with the **real** Odoo database name.

.. tip::
   Ensure that the domain (used in the URI:
   `https://yourdbname.odoo.com/google_account/authentication`) is the exact same domain as
   configured in the `web.base.url` system parameter.

   Access the `web.base.url` by activating :ref:`developer mode <developer-mode>`, and navigating to
   :menuselection:`Settings app --> Technical header menu --> Parameters section --> System
   Parameters`.

=============================
Google Sign-In Authentication
=============================

The *Google Sign-In Authentication* is a useful function that allows Odoo users to sign in to their
database with their Google account.

This is particularly helpful if the organization uses Google Workspace, and wants employees within
the organization to connect to Odoo using their Google Accounts.

.. tip::
   Keep at least one administrator account that logs in with a password, so the database remains
   accessible if the OAuth provider is unavailable.

.. seealso::
   - :doc:`/applications/productivity/calendar/google`
   - :doc:`../email_communication/google_oauth`

.. _google-sign-in/configuration:

Configuration
=============

The integration of the Google sign-in function requires configuration both on Google *and* Odoo.

.. _google-sign-in/api:

Google API Dashboard
--------------------

#. Go to the `Google API Dashboard <https://console.developers.google.com/>`_.
#. Make sure the right project is opened. If there isn't a project yet, click on :guilabel:`Create
   Project`, fill out the project name and other details of the company, and click on
   :guilabel:`Create`.

   .. screenshot:: general-google-signin-new-project
      :menu: (Google Cloud console) ‣ New Project
      :shows: The New Project form with Project name and Location filled, and the Create button.
      :module: auth_oauth
      :notes: Google website.

   .. tip::
      Choose the name of the company from the drop-down menu.

.. _google-sign-in/oauth:

OAuth consent screen
~~~~~~~~~~~~~~~~~~~~

#. On the left side menu, click on :menuselection:`OAuth consent screen`.

   .. screenshot:: general-google-signin-consent-menu
      :menu: (Google Cloud console) ‣ APIs & Services
      :shows: The left menu of APIs & Services with "OAuth consent screen" highlighted.
      :module: auth_oauth
      :notes: Google website.

#. Choose one of the options (:guilabel:`Internal` / :guilabel:`External`), and click on
   :guilabel:`Create`.

   .. screenshot:: general-google-signin-user-type
      :menu: (Google Cloud console) ‣ OAuth consent screen
      :shows: The User Type choice (Internal / External) and the Create button.
      :highlight: The User Type options.
      :module: auth_oauth
      :notes: Google website.

   .. warning::
      *Personal* Gmail Accounts are only allowed to be **External** User Type, which means Google
      may require an approval, or for *Scopes* to be added on. However, using a *Google WorkSpace*
      account allows for **Internal** User Type to be used.

      Note, as well, that while the API connection is in the *External* testing mode, then no
      approval is necessary from Google. User limits in this testing mode is set to 100 users.

#. Fill out the required details and domain info, then click on :guilabel:`Save and Continue`.
#. On the :menuselection:`Scopes` page, leave all fields as is, and click on :guilabel:`Save and
   Continue`.
#. Next, if continuing in testing mode (*External*), add the email addresses being configured under
   the :guilabel:`Test users` step by clicking on :guilabel:`Add Users`, and then the
   :guilabel:`Save and Continue` button. A summary of the app registration appears.
#. Finally, scroll to the bottom, and click on :guilabel:`Back to Dashboard`.

.. _google-sign-in/credentials:

Credentials
~~~~~~~~~~~

#. On the left side menu, click on :menuselection:`Credentials`.

   .. screenshot:: general-google-signin-credentials-menu
      :menu: (Google Cloud console) ‣ APIs & Services
      :shows: The left menu with "Credentials" highlighted.
      :module: auth_oauth
      :notes: Google website.

#. Click on :guilabel:`Create Credentials`, and select :guilabel:`OAuth client ID`.

   .. screenshot:: general-google-signin-create-client-id
      :menu: (Google Cloud console) ‣ Credentials ‣ Create Credentials
      :shows: The "Create Credentials" dropdown open with "OAuth client ID" highlighted.
      :module: auth_oauth
      :notes: Google website.

#. Select :guilabel:`Web Application` as the :guilabel:`Application Type`. Now, configure the
   allowed pages on which Odoo will be redirected.

   In order to achieve this, in the :guilabel:`Authorized redirect URIs` field, enter the database's
   domain immediately followed by `/auth_oauth/signin`. For example:
   `https://erp.example.com/auth_oauth/signin`, then click on :guilabel:`Create`.

#. Now that the *OAuth client* has been created, a screen will appear with the :guilabel:`Client ID`
   and :guilabel:`Client Secret`. Copy the :guilabel:`Client ID` for later, as it will be necessary
   for the configuration in Odoo, which will be covered in the following steps.

.. _google-sign-in/auth-odoo:

Google Authentication on Odoo
-----------------------------

.. _google-sign-in/client-id:

Retrieve the Client ID
~~~~~~~~~~~~~~~~~~~~~~

Once the previous steps are complete, two keys are generated on the Google API Dashboard:
:guilabel:`Client ID` and :guilabel:`Client Secret`. Copy the :guilabel:`Client ID`.

.. screenshot:: general-google-signin-client-created
   :menu: (Google Cloud console) ‣ Credentials
   :shows: The "OAuth client created" dialog showing the Client ID and Client Secret with copy buttons.
   :highlight: The Client ID.
   :module: auth_oauth
   :notes: Google website; blur IDs and secrets.

.. _google-sign-in/odoo-activation:

Odoo activation
~~~~~~~~~~~~~~~

#. Go to :menuselection:`Odoo General Settings --> Integrations` and activate :guilabel:`OAuth
   Authentication`.

   .. note::
      Odoo may prompt the user to log-in again after this step.

#. Go back to :menuselection:`General Settings --> Integrations --> OAuth Authentication`, activate
   the selection and :guilabel:`Save`. Next, return to :menuselection:`General Settings -->
   Integrations --> Google Authentication` and activate the selection. Then fill out the
   :guilabel:`Client ID` with the key from the Google API Dashboard, and :guilabel:`Save`.

   .. screenshot:: general-google-signin-odoo-setting
      :menu: Settings ‣ General Settings ‣ Integrations
      :shows: The "OAuth Authentication" and "Google Authentication" settings enabled, with the Client ID field filled.
      :highlight: The Client ID field.
      :module: auth_oauth, base_setup
      :notes: English UI, crop to the section; blur the Client ID.

   .. note::
      Google OAuth2 configuration can also be accessed by clicking on :guilabel:`OAuth Providers`
      under the :guilabel:`OAuth Authentication` heading in :menuselection:`Integrations`.

.. _google-sign-in/log-in:

Log in to Odoo with Google
==========================

To link the Google account to the Odoo profile, click on :guilabel:`Log in with Google` when first
logging into Odoo.

   .. screenshot:: general-google-signin-login
      :menu: (Odoo login / reset password page)
      :shows: The Odoo login (reset password) page with the "Log in with Google" button.
      :highlight: The Google button.
      :module: auth_oauth
      :notes: English UI, crop to the login box.


Existing users must :ref:`reset their password <users/reset-password>` to access the
:menuselection:`Reset Password` page, while new users can directly click on :guilabel:`Log in with
Google`, instead of choosing a new password.

.. seealso::
   - `Google Cloud Platform Console Help - Setting up OAuth 2.0
     <https://support.google.com/cloud/answer/6158849>`_

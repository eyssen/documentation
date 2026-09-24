:show-content:

.. |2fa| replace:: :abbr:`2FA (two-factor authentication)`

=====
Users
=====

Odoo defines a *user* as someone who has access to a database. An administrator can add as many
users as the company needs and, in order to restrict the type of information each user can access,
rules can be applied to each user. Users and access rights can be added and changed at any point.

.. seealso::
   - :doc:`users/language`
   - :doc:`users/access_rights`
   - :ref:`access-rights/superuser`
   - :ref:`access-rights/groups`

.. _users/add-individual:

Add individual users
====================

To add new users, navigate to :menuselection:`Settings app --> Users section --> Manage Users`, and
click on :guilabel:`New`.

.. screenshot:: general-users-manage-users
   :menu: Settings ‣ General Settings ‣ Users
   :shows: The Users section of the settings with the number of active users, the "Invite New Users" field and the "Manage Users" link.
   :highlight: The "Manage Users" link.
   :module: base_setup
   :notes: English UI, crop to the relevant area.

Fill in the form with all the required information. Under the :doc:`Access Rights
<users/access_rights>` tab, choose the group within each application the user can have access to.

The list of applications shown is based on the applications installed on the database.

.. screenshot:: general-users-new-user-form
   :menu: Settings ‣ Users & Companies ‣ Users ‣ New
   :shows: User form with Name, Email Address, the Access Rights tab (application access dropdowns per app) and the Preferences tab.
   :highlight: The Access Rights tab.
   :data: New user "Anita Oliver", Sales: "User: Own Documents Only".
   :module: base
   :notes: English UI, 1440px width, crop to the form sheet.

After filling out all the necessary fields on the page, :icon:`fa-cloud-upload` :guilabel:`(Save
manually)`. An invitation email is automatically sent to the user, using the email in the
:guilabel:`Email Address` field. The user must click on the link included in the email to accept the
invitation, and to create a database login.

.. screenshot:: general-users-invitation-sent
   :menu: Settings ‣ Users & Companies ‣ Users ‣ (new user)
   :shows: Saved user form with the notification/banner that the invitation email has been sent and the "Send an Invitation Email" button.
   :highlight: The banner.
   :module: auth_signup
   :notes: English UI, crop to the relevant area.

.. tip::
   Users can also be invited quickly by entering their email addresses in the :guilabel:`Invite New
   Users` field of the :guilabel:`Users` section in the :menuselection:`Settings` app, then clicking
   :guilabel:`Invite`.

User type
---------

:guilabel:`User Type` can be chosen on the :guilabel:`Manage Users` page by clicking on the search
bar, and then :ref:`setting a filter <search/preconfigured-filters>` for either :guilabel:`Internal
User` or :guilabel:`Portal User`.

Odoo databases have three types of users: :guilabel:`Internal User`, :guilabel:`Portal`, and
:guilabel:`Public`. Users are considered *internal database* users. Portal users are *external
users*, who only have access to the database portal to view records. Public users are those visiting
websites, via the website's frontend. See the documentation on :doc:`users/portal`.

The :guilabel:`Portal` user option does **not** allow the administrator to choose access rights.
These users have specific access rights pre-set (such as, record rules and restricted menus), and
usually do not belong to the usual Odoo groups.

.. _users/deactivate:

Deactivate users
================

To deactivate (i.e. archive) a user, navigate to :menuselection:`Settings app --> Users section -->
Manage Users`. Then, tick the checkbox to the left of the users to be deactivated.

After selecting the appropriate user to be archived, click the :icon:`fa-cog` :guilabel:`(Actions)`
icon, and select :guilabel:`Archive` from the resulting drop-down menu. Then, click :guilabel:`OK`
from the :guilabel:`Confirmation` pop-up window that appears.

.. danger::
   **Never** deactivate the main/administrator user (admin). Making changes to admin users can have
   a detrimental impact on the database. This includes *impotent admin*, which means that no user in
   the database can make changes to the access rights. For this reason, contact your Odoo partner or
   system administrator before making changes.

.. _users/passwords-management:

Password management
===================

Password management is an important part of granting users autonomous access to the database at all
times. Odoo offers a few different methods to reset a user's password.

.. tip::
   Odoo has a setting to specify the length needed for a password. This setting can be accessed by
   navigating to :menuselection:`Settings app --> Permissions` section, and entering the desired
   password length in the :guilabel:`Minimum Password Length` field. By default the value is `8`.

.. screenshot:: general-users-min-password-length
   :menu: Settings ‣ General Settings ‣ Permissions
   :shows: The Permissions section with the "Minimum Password Length" field (value 8).
   :highlight: The "Minimum Password Length" field.
   :module: auth_password_policy
   :notes: English UI, crop to the relevant area.

.. _users/reset-password:

Reset password
--------------

Sometimes, users might wish to reset their personal password for added security, so they are the
only ones with access to the password. Odoo offers two different reset options: one initiated by the
user to reset the password, and another where the administrator triggers a reset.

.. _users/reset-password-login:

Enable password reset from login page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to enable/disable password resets directly from the login page. This action is
completed by the individual user, and this setting is enabled by default.

To change this setting, go to :menuselection:`Settings app --> Permissions` section, activate
:guilabel:`Password Reset`, and then click :guilabel:`Save`.

.. screenshot:: general-users-password-reset-setting
   :menu: Settings ‣ General Settings ‣ Permissions
   :shows: The Permissions section with the "Password Reset" checkbox enabled.
   :highlight: The "Password Reset" setting.
   :module: auth_signup
   :notes: English UI, crop to the relevant area.

On the login page, click :guilabel:`Reset Password` to initiate the password reset process, and have
a reset-token sent to the email on file.

.. _users/reset-password-email:

Send reset instructions
~~~~~~~~~~~~~~~~~~~~~~~

Go to :menuselection:`Settings app --> Users & Companies --> Users`, select the user from the list,
and click on :guilabel:`Send Password Reset Instructions` on the user form. An email is
automatically sent to them with password reset instructions.

.. note::
   The :guilabel:`Send Password Reset Instructions` button **only** appears if the Odoo invitation
   email has already been confirmed by the user. Otherwise, a :guilabel:`Re-send Invitation Email`
   button appears.

This email contains all the instructions needed to reset the password, along with a link redirecting
the user to an Odoo login page.

.. screenshot:: general-users-password-reset-email
   :menu: (email client)
   :shows: The password reset email received by the user, with the "Change password" button.
   :module: auth_signup
   :notes: Any email client; blur personal data.

.. _users/change-password:

Change user password
--------------------

Go to :menuselection:`Settings app --> Users & Companies --> Users`, and select a user to access its
form. Click on the :icon:`fa-cog` :guilabel:`(Actions)` icon, and select :guilabel:`Change Password`
from the resulting drop-down menu. Enter a new password in the :guilabel:`New Password` column of
the :guilabel:`Change Password` pop-up window that appears, and confirm the change by clicking
:guilabel:`Change Password`.

.. screenshot:: general-users-change-password
   :menu: Settings ‣ Users & Companies ‣ Users ‣ (a user) ‣ Actions ‣ Change Password
   :shows: The Change Password dialog listing the user with the "New Password" column, and the "Change Password" button.
   :highlight: The "New Password" cell.
   :module: base
   :notes: English UI, crop to the relevant area.

.. note::
   This operation only modifies the password of the users in this database. Alternatively, the
   user can set the password themselves by using the :ref:`password reset email
   <users/reset-password-email>`.

After clicking :guilabel:`Change Password`, the page is redirected to an Odoo login page where the
database can be re-accessed using the new password.

.. _users/default-access-rights:

Default access rights
=====================

By default, new users get the highest access rights for all installed apps. To define the access
rights given to new users instead, go to :menuselection:`Settings app --> Permissions` section,
enable :guilabel:`Default Access Rights`, click :guilabel:`Save`, then click the :guilabel:`Default
Access Rights` link. The form that opens is a template user: set its :guilabel:`Access Rights` as
needed. If the setting is disabled, new users only get basic employee access.

.. screenshot:: general-users-default-access-rights
   :menu: Settings ‣ General Settings ‣ Permissions
   :shows: The Permissions section with the "Customer Account" options (On invitation / Free sign
      up), the "Default Access Rights" setting enabled with its link, "Password Reset", and "API
      Keys" with the "Manage API Keys" link.
   :highlight: The "Default Access Rights" setting.
   :module: base_setup, auth_signup
   :notes: English UI, crop to the Permissions section.

.. _users/security:

Account security
================

Each user can manage the security of their account from their preferences: click the avatar in the
upper-right corner, select :guilabel:`My Profile`, and open the :guilabel:`Account Security` tab.
The following options are available:

- :guilabel:`Change password`: set a new password after confirming the current one.
- :doc:`Two-factor Authentication <users/2fa>`: enable or disable |2fa|.
- :guilabel:`Log out from all devices`: close all the other sessions of the user, e.g., after
  losing a device. The active sessions are listed in the :guilabel:`Devices` tab.
- :guilabel:`API Keys`: API keys are used to connect to Odoo from external tools (e.g., scripts or
  integrations) without a password or two-factor authentication. Click :guilabel:`New API Key`,
  enter a description, select a :guilabel:`Duration` (from :guilabel:`1 Day` to :guilabel:`1 Year`;
  administrators can also choose :guilabel:`Persistent Key` or :guilabel:`Custom Date`), confirm the
  password, and click :guilabel:`Generate key`. Copy the key immediately: it cannot be displayed
  again. Existing keys can be deleted with the :icon:`fa-trash` :guilabel:`(delete)` icon.

.. note::
   Administrators can view and revoke the API keys of all users by clicking :guilabel:`Manage API
   Keys` in the :guilabel:`Permissions` section of the :menuselection:`Settings` app.

.. screenshot:: general-users-account-security
   :menu: Avatar ‣ My Profile ‣ Account Security tab
   :shows: The Account Security tab: "Change password", the Two-factor Authentication toggle,
      "Log out from all devices", and the API Keys list with one key and the "New API Key" button.
   :highlight: The API Keys block.
   :data: API key "Reporting script", scope rpc, expiration in 3 months.
   :module: base, auth_totp
   :notes: English UI, crop to the tab.

.. _users/multi-companies:

Multi Companies
===============

The :guilabel:`Multi Companies` field on a user form allows an administrator to provide access to
multiple companies for users. To configure a multi-company environment for a user, navigate to the
desired user by going to: :menuselection:`Settings app --> Users section --> Manage users`. Then,
select the user to open their user form, and configure with multi-company access.

Under :guilabel:`Multi Companies` in the :guilabel:`Access Rights` tab, set the fields labeled
:guilabel:`Allowed Companies` and :guilabel:`Default Company`.

The :guilabel:`Allowed Companies` field can contain multiple companies. These are the companies the
user can access and edit, according to the set access rights. The :guilabel:`Default Company` is the
company the user defaults to, upon logging in each time. This field can contain only **one**
company.

.. warning::
   If multi-company access is not configured correctly, it could lead to inconsistent multi-company
   behaviors. Because of this, only experienced Odoo users should make access rights changes to
   users for databases with a multi-company configuration. For technical explanations, refer to the
   developer documentation on :doc:`/developer/howtos/company`.

.. screenshot:: general-users-multi-companies
   :menu: Settings ‣ Users & Companies ‣ Users ‣ (a user)
   :shows: User form with the "Allowed Companies" and "Default Company" fields in a multi-company database.
   :highlight: The two company fields.
   :data: Two companies "YourCompany HU" and "YourCompany ES".
   :module: base
   :notes: English UI, crop to the relevant area.

.. seealso::
   :doc:`companies`

.. toctree::
   :titlesonly:

   users/language
   users/2fa
   users/access_rights
   users/access_management
   users/portal
   users/facebook
   users/google
   users/azure
   users/ldap

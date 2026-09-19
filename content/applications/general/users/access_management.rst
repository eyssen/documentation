=================
Access management
=================

The *Access Management* module (`eyssen_access_management`) gives administrators three additional
tools to control what a user can reach, on top of the standard :doc:`access rights
<access_rights>`:

- :ref:`IP subnets <access-management/ip-subnets>` from which a user is allowed, or not allowed, to
  log in;
- :ref:`restricted menus <access-management/menus>`, to hide menu items from a user;
- :ref:`model domain rules <access-management/domain-rules>`, to reserve a set of records for some
  users in the views.

It also keeps a :ref:`log of the logins <access-management/logins>` of every user.

.. note::
   - To install the module, go to :menuselection:`Settings --> eYssen ERP`, and, in the
     :guilabel:`General Modules` section, enable :guilabel:`Access Management`. See
     :doc:`../eyssen_erp_settings`.
   - All the features described on this page are only available to users whose
     :guilabel:`Administration` access right is set to :guilabel:`Access Rights` or
     :guilabel:`Settings`.

The rules can be managed from two places:

- on the user: go to :menuselection:`Settings --> Users & Companies --> Users`, open a user, and
  click the :guilabel:`Access Management` tab, which contains the :guilabel:`IP Subnets`,
  :guilabel:`Restricted Menus`, and :guilabel:`Model Domain Rules` sub-tabs;
- for all users at once: from the :menuselection:`Settings --> Access Management` menu.

.. screenshot:: general-access-management-user-tab
   :menu: Settings ‣ Users & Companies ‣ Users ‣ (open a user) ‣ Access Management tab
   :shows: The Access Management tab of a user form with its three sub-tabs; the IP Subnets sub-tab is open with one green "Allow" line and one red "Deny" line, and the instructions list below it. The "Logins" smart button is visible at the top of the form.
   :highlight: The "Access Management" tab and the "Logins" smart button (red frames).
   :data: User "Marc Demo"; Allow IPv4 192.0.2.0/24 "Office"; Deny IPv4 192.0.2.66 "Guest Wi-Fi gateway".
   :module: eyssen_access_management
   :notes: English UI, light theme, 1440px width. Use documentation-range IP addresses only.

.. _access-management/ip-subnets:

IP subnets
==========

An IP subnet rule restricts the network addresses from which a user can log in through the login
page.

To create a rule, go to :menuselection:`Settings --> Access Management --> IP Subnets`, click
:guilabel:`New`, and fill in the following fields:

- :guilabel:`Rule`: :guilabel:`Allow` or :guilabel:`Deny`;
- :guilabel:`Type`: :guilabel:`IPv4` or :guilabel:`IPv6`;
- :guilabel:`IP Subnet`: the subnet in CIDR notation, e.g., `192.0.2.0/24`. To target a single
  address, enter the address alone (`192.0.2.78`) or with a `/32` suffix. An invalid subnet is
  refused when the rule is saved;
- :guilabel:`Users`: the users the rule applies to;
- :guilabel:`Company`: optionally, the company the rule belongs to;
- :guilabel:`Description`: a free text, e.g., the name of the office.

The same rule can be assigned to several users. In the lists, :guilabel:`Allow` rules are displayed
in green and :guilabel:`Deny` rules in red.

When a user logs in, the rules assigned to them are evaluated as follows:

- If the user has no rule, they can log in from anywhere.
- If the user has at least one :guilabel:`Allow` rule, they can only log in from an address that
  belongs to one of the allowed subnets.
- If the user only has :guilabel:`Deny` rules, they can log in from anywhere, except from the
  denied subnets.
- A :guilabel:`Deny` rule always wins: use it to exclude a smaller subnet, or a single address,
  from an allowed subnet.

A user who tries to log in from a forbidden address gets the message *Access from this IP address is
not allowed*, and the attempt is recorded in the :ref:`login log <access-management/logins>`.

.. warning::
   - Overlapping subnets are not checked. Review the rules of a user as a whole before saving,
     in particular for your own administrator account, to avoid locking yourself out.
   - The address taken into account is the one transmitted by the reverse proxy in front of the
     database. If all logins appear to come from the same internal address, ask your system
     administrator to check the proxy configuration.

.. _access-management/menus:

Restricted menus
================

Menu items can be hidden user by user, without creating a dedicated user group.

Open the :guilabel:`Restricted Menus` sub-tab of the user's :guilabel:`Access Management` tab and
choose how the list works with the :guilabel:`Hide all menu items` toggle:

- **disabled** (default): all the menu items the user has access to are displayed, *except* the
  ones added to the list;
- **enabled**: all menu items are hidden, *except* the ones added to the list (and provided the
  user has access to them).

Then, click :guilabel:`Add a line` and select the menu items. Both applications (top-level menus)
and sub-menus can be selected.

.. tip::
   When :guilabel:`Hide all menu items` is enabled, remember to add the parent menus as well: a
   sub-menu whose application is hidden cannot be reached.

The reverse view is available on the menu items: in :ref:`developer mode <developer-mode>`, go to
:menuselection:`Settings --> Technical --> User Interface --> Menu Items`, open a menu item, and
click the :guilabel:`Restricted Users` tab. A user displayed in red sees everything but this menu
item; a user displayed in green sees nothing but the menu items explicitly allowed, including this
one.

.. important::
   - Menu restrictions are ignored for users whose :guilabel:`Administration` access right is
     :guilabel:`Access Rights` or :guilabel:`Settings`.
   - Hiding a menu item only removes it from the navigation. It does not change the user's access
     rights on the underlying records; use :doc:`groups and access rights <access_rights>` for
     that.
   - The user has to reload the page for a change to be taken into account.

.. screenshot:: general-access-management-restricted-menus
   :menu: Settings ‣ Users & Companies ‣ Users ‣ (open a user) ‣ Access Management tab ‣ Restricted Menus
   :shows: The Restricted Menus sub-tab with the "Hide all menu items" toggle disabled, the blue information banner explaining the mode, and a list of three hidden menu items.
   :highlight: The "Hide all menu items" toggle (red frame).
   :data: Hidden menus: "Invoicing/Configuration", "Sales/Reporting", "Employees".
   :module: eyssen_access_management
   :notes: English UI, light theme, 1440px width, crop to the tab.

.. _access-management/domain-rules:

Model domain rules
==================

A model domain rule reserves a set of records for one or more users: the records matching the rule
are only listed for the users of the rule, and are left out of the views of everybody else.

To create a rule, activate the :ref:`developer mode <developer-mode>` (the filter editor is only
displayed in developer mode), go to :menuselection:`Settings --> Access Management --> Model
Domain Rules`, click :guilabel:`New`, and fill in:

- the name of the rule;
- :guilabel:`Users`: the users for whom the records are reserved;
- :guilabel:`Company`: optionally, the company in which the rule applies. A rule without a company
  applies in every company;
- :guilabel:`Lines`: click :guilabel:`Add a line`, select a :guilabel:`Model` (e.g., *Sales
  Order*), and define the :guilabel:`Filter Domain` with the domain editor. A rule can contain
  lines for several models.

Finally, the rule can also be assigned from the :guilabel:`Model Domain Rules` sub-tab of a user's
:guilabel:`Access Management` tab.

For each model, the records displayed to a user are determined as follows:

- records that do not match any rule line with users remain visible to everybody;
- records that match a rule line are only visible to the users of that rule;
- records that match a line of a rule **without** any user are visible to everybody, even if another
  rule reserves them.

.. example::
   The rule *Key accounts* has the users *Anita* and *Marc*, and one line on the model *Sales Order*
   with the filter `Customer > Tags contains "Key account"`. The quotations and sales orders of
   the key accounts are now only listed for Anita and Marc; all the other orders remain visible
   to the whole sales team.

.. important::
   Model domain rules filter the records loaded in the views of the web client (list, Kanban,
   etc.). They are not a security mechanism: totals of grouped views, pivot and graph analyses,
   exports, and printed reports are not filtered, and a record can still be opened with a
   direct link. For a strict restriction, ask your system administrator to set up record rules.

   The rules never apply to the *Users*, *Contacts*, and *Companies* models.

.. screenshot:: general-access-management-domain-rule
   :menu: Settings ‣ Access Management ‣ Model Domain Rules ‣ New (developer mode)
   :shows: A model domain rule form with its name, two users, the "Manual" type badge and one line for the model "Sales Order" with its domain.
   :highlight: The "Lines" list (red frame).
   :data: Rule "Key accounts"; users "Anita Oliver", "Marc Demo"; line model "Sales Order", domain on the customer tag "Key account".
   :module: eyssen_access_management
   :notes: English UI, light theme, 1440px width, developer mode enabled.

.. note::
   IP subnets, model domain rules and their lines cannot be deleted from the interface. To stop
   using an IP subnet rule, remove its users.

.. _access-management/journals:

Restrict journals to users
--------------------------

With the *Access Management - Account* module (`eyssen_access_management_account`), a journal can
be reserved for some users without writing a domain by hand.

Go to :menuselection:`Accounting --> Configuration --> Journals`, open a journal, click the
:guilabel:`Advanced Settings` tab, and select the users in the :guilabel:`Limited Users` field of
the :guilabel:`Access Rules` section. The field is not available on journals of the
:guilabel:`Miscellaneous` type.

Each time a journal is saved, the rules of the :guilabel:`Automatic` type are rebuilt: one rule
named *Access Management Rule for Journals* is created per group of users, with lines on the
journals, the journal entries (and therefore the invoices and bills), and the journal items. As a
result, the limited journals and their entries are only listed for the selected users. Automatic
rules are read-only.

In addition, the :menuselection:`Accounting --> Reporting --> Management --> Invoice Analysis`
report only includes the invoices of the journals that are either not limited, or limited to the current user.

.. note::
   To install the module, enable :guilabel:`Account` under :guilabel:`Access Management` in
   :menuselection:`Settings --> eYssen ERP`. In the same place, the :guilabel:`PoS` option installs
   the restriction of points of sale by user; see the :ref:`point of sale configuration
   <pos/configuration/access-rules>`.

.. screenshot:: general-access-management-journal
   :menu: Accounting ‣ Configuration ‣ Journals ‣ (open a bank journal) ‣ Advanced Settings tab
   :shows: The Advanced Settings tab of a journal with the "Access Rules" section and two users selected in the "Limited Users" field.
   :highlight: The "Limited Users" field (red frame).
   :data: Journal "Bank (EUR)"; limited users "Anita Oliver", "Mitchell Admin".
   :module: eyssen_access_management_account
   :notes: English UI, light theme, 1440px width, crop to the tab.

.. _access-management/logins:

User logins
===========

Every login attempt made on the login page with an existing user name is recorded with the
:guilabel:`User`, the :guilabel:`IP Address`, the browser (:guilabel:`User Agent`), and, for a
failed attempt, the :guilabel:`Reason`: *Wrong login/password* or *Access from this IP address is
not allowed*. Successful logins are displayed in green and failed attempts in red.

- To see the logins of one user, open the user and click the :guilabel:`Logins` smart button.
- To see all logins, go to :menuselection:`Settings --> Access Management --> User Logins`. Use the
  :guilabel:`Success` and :guilabel:`Unsuccess` filters, the :guilabel:`Date` filter, and group the
  list by :guilabel:`User`, :guilabel:`IP Address`, :guilabel:`Reason`, or :guilabel:`Date`, e.g.,
  to spot repeated failed attempts from one address.

The log is read-only. Attempts made with a user name that does not exist are not recorded in this
list.

.. screenshot:: general-access-management-logins
   :menu: Settings ‣ Access Management ‣ User Logins
   :shows: The login log grouped by user, with green successful lines and red failed lines showing the IP address, the reason and the user agent.
   :highlight: The "Reason" column (red frame).
   :data: Three users; at least one "Wrong login/password" and one "Access from this IP address is not allowed" line.
   :module: eyssen_access_management
   :notes: English UI, light theme, 1440px width, crop to the list. Documentation-range IP addresses only.

.. seealso::
   - :doc:`access_rights`
   - :doc:`2fa`

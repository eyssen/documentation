=================
Localization base
=================

The :guilabel:`Romania - Localization Base` (`l10n_ro_base`) module is the foundation of the
eYssen Romanian modules. It provides the data and the tools that the other modules share:

- the :ref:`Romanian Localization settings <localizations/romania/base-settings>` of the company;
- the :ref:`CNP <localizations/romania/cnp>` (*Cod Numeric Personal*) of the individuals;
- the :ref:`lookup of the partners in the ANAF register <localizations/romania/anaf-partners>`;
- the :ref:`checks of duplicate contacts <localizations/romania/duplicates>`;
- the :ref:`calendar of the Romanian legal holidays <localizations/romania/calendar>` and the
  working-day calculations;
- the :ref:`Romanian Localization User group <localizations/romania/user-group>`, which shows the
  Romanian menus to the users who work on a Romanian company.

It is installed automatically with the other Romanian modules. Its features only apply to
companies whose **fiscal country** is Romania; set the :guilabel:`Fiscal Country` of the company in
the :guilabel:`Taxes` section of :menuselection:`Accounting --> Configuration --> Settings`. The other companies of the database are not changed (see
:doc:`multi_company`).

.. _localizations/romania/base-settings:

Company settings
================

In :menuselection:`Accounting --> Configuration --> Settings`, the :guilabel:`Romanian
Localization` section (displayed for Romanian companies) groups the following settings.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Setting
     - Purpose
   * - :guilabel:`VAT on Payment`
     - The company applies the VAT on collection system (*TVA la încasare*, article 282 of the
       Fiscal Code). The invoices carry the mention *TVA la încasare* (see
       :ref:`localizations/romania/vat-on-collection`). Optionally fill in
       :guilabel:`VAT on Payment From` and :guilabel:`VAT on Payment Until` if the system applies
       only for a period; leave a date empty for no limit.
   * - :guilabel:`Share Capital`
     - The subscribed and paid-up share capital (*capital social*), printed on the
       :doc:`invoices <invoicing>`.
   * - :guilabel:`ANAF Partner Data`
     - :guilabel:`Autocomplete Partners from ANAF` (enabled by default) fills new contacts from
       their fiscal code. :guilabel:`ANAF Refresh Interval (days)` (7 by default) is the age
       after which the scheduled action refreshes the ANAF statuses of a contact; set it to 0 to
       disable the scheduled refresh. See :ref:`localizations/romania/anaf-partners`.
   * - :guilabel:`Duplicate Partners`
     - The :guilabel:`Duplicate CUI / Trade Register No.` policy: :guilabel:`No check`,
       :guilabel:`Warning only` (default) or :guilabel:`Block duplicates`. See
       :ref:`localizations/romania/duplicates`.

.. _localizations/romania/cnp:

CNP of individuals
==================

On the form of a contact that is **not** a company, the :guilabel:`CNP` field is displayed next
to the :guilabel:`NRC`, for the contacts of Romanian companies. The CNP (*Cod Numeric Personal*)
of the buyer is printed on the :doc:`invoices <invoicing>` and identifies the buyer of the
individual invoices sent to :doc:`RO e-Factura <e_factura>`.

Odoo validates the CNP when you save the contact, if the country of the contact is Romania or is
not set: it has 13 digits and does not start with 0; its birth date is valid and not in the
future; the county code (digits 8 and 9) is valid; the sequence number (digits 10 to 12) is not
`000`; and the control digit is correct. Spaces are removed when you type. A foreign contact is
not checked.

.. important::
   The CNP is personal data. The field is only visible to the users with the invoicing or the
   *Contact Creation* access rights.

.. _localizations/romania/anaf-partners:

Contacts and the ANAF register
==============================

Odoo queries the public web service of ANAF for the taxpayers (*PlatitorTvaRest*, version 9). No
credentials are needed; the requests are limited to one per second.

Autocomplete of new contacts
----------------------------

When you create a contact and type a valid Romanian fiscal code (CUI) as its **name** (or as its
**Tax ID**, while the name is still empty), with or without the `RO` prefix, Odoo fills the
contact with the official data: the
name, the trade register number (:guilabel:`NRC`), the address with the county, the phone number
(if there is none), and the Tax ID, which gets the `RO` prefix only if the company is a VAT payer.
The contact is created as a company in Romania. If the code is not found, a warning is displayed.
Disable the feature with :guilabel:`Autocomplete Partners from ANAF` in the settings.

ANAF statuses
-------------

The :guilabel:`Romania - ANAF` group of the :guilabel:`Invoicing` tab of the contact shows the
statuses of the ANAF register:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Field
     - Meaning
   * - :guilabel:`VAT Payer (RO)`
     - Registered for VAT in Romania.
   * - :guilabel:`VAT on Payment (RO)`
     - Registered in the register of the taxpayers who apply the VAT on collection system.
   * - :guilabel:`RO e-Factura Register`
     - Registered in the RO e-Factura register.
   * - :guilabel:`Inactive Taxpayer (RO)`
     - Declared inactive by ANAF. The VAT of the purchases from an inactive taxpayer is not
       deductible.
   * - :guilabel:`Split VAT (RO)`
     - Applies the split VAT payment system (*plata defalcată a TVA*), displayed with
       :doc:`e_factura`.
   * - :guilabel:`Last ANAF Check`
     - Date of the last successful lookup.

Click :guilabel:`Update from ANAF` (displayed when the contact has a Tax ID) to refresh the
identity data (name, address, Tax ID, NRC) and the statuses of the contact; a notification tells
you if the fiscal code was not found. The statuses are stored on the company of the contact and
shared with its child contacts. The filters :guilabel:`RO Inactive
Taxpayers` and :guilabel:`RO VAT on Payment` of the contact search find the contacts by status.

A scheduled action, :guilabel:`Romania: refresh partner statuses from ANAF`, runs every day for
the Romanian companies. It refreshes the **statuses only** (the name and the address are not
overwritten) of the contacts used on the invoices, credit notes and vendor bills of the last 90
days, whose last check is at least :guilabel:`ANAF Refresh Interval (days)` old. If ANAF does not
answer, the action stops and tries again the next day.

.. _localizations/romania/duplicates:

Duplicate contacts
==================

The :guilabel:`Duplicate CUI / Trade Register No.` setting controls what happens when you create a
Romanian contact with a Tax ID or a trade register number that another contact already has:

- :guilabel:`No check`: nothing happens;
- :guilabel:`Warning only` (default): a banner on the contact form tells you that a contact with
  the same trade register number already exists;
- :guilabel:`Block duplicates`: the contact cannot be saved, and an error message names the
  contact that already uses the fiscal code or the trade register number.

Only contacts without a parent, whose country is Romania (or empty), in a Romanian company, are
checked, and they are compared with the contacts of the same company and with the shared contacts.
The Hungarian and Spanish contacts are never blocked.

.. _localizations/romania/calendar:

Legal holidays and working days
===============================

Deadlines such as the :ref:`E-Factura submission deadline <localizations/romania/efactura-deadline>`
are counted in working days: the days that are neither a weekend day nor a legal holiday. The
legal holidays follow article 139 of the Labor Code:

- 1 and 2 January;
- 6 and 7 January (since 2024);
- 24 January;
- Orthodox Good Friday, Easter Sunday and Easter Monday;
- 1 May and 1 June;
- Orthodox Pentecost (*Rusalii*) Sunday and Monday;
- 15 August;
- 30 November and 1 December;
- 25 and 26 December.

The moving holidays are calculated from the date of the Orthodox Easter. To add days off decided
by the Government, enable the :ref:`developer mode <developer-mode>` and create the system
parameter `l10n_ro_base.extra_holidays` in :menuselection:`Settings --> Technical --> System
Parameters`. Its value is a list of dates in the `YYYY-MM-DD` format, separated by commas, for
example `2026-12-24,2026-12-28`.

.. _localizations/romania/user-group:

Romanian menus and the Romanian Localization User group
=======================================================

All the menus of the Romanian modules (declarations, registers, E-Factura deadlines and
messages, assets and stock reports) are restricted to the members of the **Romanian Localization
User** group, in addition to their usual access rights. The group is managed automatically:

- the internal users who have access to at least one company whose fiscal country is Romania are
  added to the group (when the module is installed, and each time the companies or the groups of
  a user, or the fiscal country of a company, change);
- a user who loses that access is removed from the group, but only if the group was granted
  automatically. A membership that you granted by hand is never removed.

This way, the users who work only on Hungarian or Spanish companies do not see the Romanian
menus. To grant or remove the group by hand, edit the user in :ref:`developer mode
<developer-mode>`.

.. note::
   The menus can be refreshed with a delay when the fiscal country of a company changes: reload
   the page, or log in again, if a menu does not appear or disappear immediately.

.. seealso::
   - :doc:`../romania`
   - :doc:`e_factura`
   - :doc:`multi_company`

=======================================
E-Factura rules, deadlines and messages
=======================================

The standard :ref:`E-Factura integration <localizations/romania/efactura>` sends the invoices to
the ANAF *SPV*. Two eYssen modules complete it with the rules that Romanian companies have to
follow every day:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Romania - E-Factura Extensions`
     - `l10n_ro_edi_extra`
     - Invoices to individuals (B2C) and Law 88/2026, buyers identified by CNP, submission
       deadline of 5 working days with reminders, corrections as storno invoices, inbox of the
       SPV messages, check of the customer at ANAF before sending.
   * - :guilabel:`PoS Invoice - Romania`
     - `l10n_ro_pos_invoice`
     - Data required to invoice a customer from the Point of Sale. Installed automatically with
       `eyssen_pos_invoice` and :doc:`base`.

The rules only apply to the customer invoices and credit notes of companies whose **fiscal
country** is Romania. The settings are in :menuselection:`Accounting --> Configuration -->
Settings`, in the :guilabel:`RO e-Factura Rules` section, below the :guilabel:`Romanian
E-Factura` connection settings.

.. _localizations/romania/efactura-obligation:

Which invoices are sent
=======================

When a customer invoice or credit note is posted, Odoo decides how it is handled by RO e-Factura
and stores the decision in the :guilabel:`RO e-Factura Obligation` field.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Obligation
     - Meaning
   * - :guilabel:`B2B`
     - The customer has a Romanian fiscal code. The invoice is sent through the B2B channel.
   * - :guilabel:`Individual in the optional register`
     - The customer is an individual enrolled in the optional RO e-Factura register. The invoice
       is sent through the B2B channel, with the CNP of the buyer.
   * - :guilabel:`B2C`
     - The customer is an individual. The invoice is reported through the B2C channel, with the
       CNP of the buyer if it is known, otherwise with the code of 13 zeros (OUG 120/2021).
   * - :guilabel:`Not sent (issuer identified by CNP, Law 88/2026)`
     - Only for the companies that opted in to the exemption of Law 88/2026 (see below).
   * - :guilabel:`Foreign customer`
     - The customer is established outside Romania and has no Romanian fiscal code: RO e-Factura
       is not mandatory.

An **individual** is a customer that is not a company and has no Tax ID. A sole trader (*PFA*,
*II*) with a fiscal code is a business customer, not an individual.

The decision is taken with the data of the customer and of the company at the time the invoice is
posted. Later changes, for example the enrolment of the customer in the optional register, do not
change the invoices already posted; to apply them to an invoice, reset it to draft and post it
again.

To see the decision of the invoices, add the optional column :guilabel:`RO e-Factura Obligation`
to the list of the invoices or group the invoices by :guilabel:`E-Factura Obligation`. For the
individuals in the optional register and for the invoices that are not sent, a banner with the
:guilabel:`RO e-Factura Decision` is displayed on the invoice.

.. _localizations/romania/efactura-b2c:

Invoices to individuals (B2C) and Law 88/2026
---------------------------------------------

The :guilabel:`Invoices to Individuals` setting (:guilabel:`B2C Invoices (RO e-Factura)` field)
has two values:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Option
     - Effect
   * - :guilabel:`Report every B2C invoice (companies: SRL, SA, ...)` (default)
     - Every invoice to an individual is reported to RO e-Factura. This is mandatory for
       companies.
   * - :guilabel:`Issuer identified by CNP: Law 88/2026 exemption (PFA, II, IF)`
     - From 1 June 2026, the invoices to individuals are not sent, unless the customer is
       enrolled in the optional RO e-Factura register.

.. warning::
   Law 88/2026 (in force on 1 June 2026) exempts only the **issuers identified by their CNP**
   (individuals such as PFA, II or IF without a separate fiscal code). Companies (SRL, SA, ...)
   must keep reporting every B2C invoice, and unreported invoices are fined. Do **not** select
   the exemption for a company. Confirm the situation of the company with its accountant before
   changing this setting. A warning is displayed in the settings when the exemption is selected.

With the exemption, the invoices dated on or after 1 June 2026 to individuals that are not in the
optional register get the obligation :guilabel:`Not sent`. They are never uploaded to the SPV (the
E-Factura option is not applied in :guilabel:`Send & Print`), and an information message lists
them. The filter :guilabel:`Not Sent (CNP Issuer Exemption)` finds them.

To identify the buyer by CNP, fill in the :guilabel:`CNP` of the contact (see
:ref:`localizations/romania/cnp`). To enroll an individual in the optional register, tick
:guilabel:`RO e-Factura Register` in the :guilabel:`Romania - ANAF` group of the
:guilabel:`Invoicing` tab of the contact (for an individual, this is set by hand).

.. note::
   An earlier version of the module applied a wrong reading of Law 88/2026. When the module is
   upgraded, the companies on the former setting are reset to :guilabel:`Report every B2C
   invoice`, the invoices that had been marked as not sent are recomputed, and a warning listing
   them is logged. Select the exemption again if it applies to the company.

.. _localizations/romania/efactura-deadline:

Submission deadline
===================

An invoice must be uploaded to RO e-Factura within **5 working days** of its issue date. The
:guilabel:`E-Factura Deadline` field of the invoice (:guilabel:`E-Factura` tab, below the index)
holds the last day: the invoice date plus 5 working days, without the weekends and the Romanian
legal holidays (see :ref:`localizations/romania/calendar`). For the invoices issued until 31
December 2025, the deadline is 5 calendar days.

The deadline is shown in orange when the invoice is *due soon* and in red when it is *overdue*,
until ANAF accepts the invoice. The invoices that must be sent but are not validated yet can be
followed in several places:

- :menuselection:`Accounting --> Customers --> E-Factura Deadlines (RO)` lists them with their
  deadline, the obligation and the status. The filters :guilabel:`E-Factura Pending`,
  :guilabel:`E-Factura Overdue` and :guilabel:`E-Factura Due in 2 Days` are available in the
  invoice lists as well.
- On the card of the sales journals of the :guilabel:`Accounting Dashboard`, the links
  :guilabel:`E-Factura Overdue` and :guilabel:`E-Factura Due Soon` show the number of invoices
  and open the list.
- A daily scheduled action, :guilabel:`E-Factura: Submission Deadline Reminders (RO)`, creates an
  :guilabel:`E-Factura Deadline` activity on every pending invoice that is due soon or overdue,
  with the deadline of the invoice as due date. It is assigned to the salesperson of the invoice,
  otherwise to the creator of the invoice, otherwise to the user who runs the action. When the
  deadline passes, the summary of the activity changes to *E-Factura overdue* and a note is posted
  in the chatter. The activity is closed with the feedback *Accepted by ANAF.* when the invoice
  is validated.

Set in :guilabel:`Deadline Reminder (working days)` how many working days before the deadline an
invoice is *due soon* and the reminder is created (2 by default).

.. _localizations/romania/efactura-storno:

Corrections: credit notes or storno invoices
============================================

The :guilabel:`Corrections` setting (:guilabel:`Corrections in RO e-Factura` field) chooses the
XML document that is sent for a customer credit note. ANAF accepts both:

- :guilabel:`Credit note (CreditNote 381)` (default): the standard CIUS-RO credit note;
- :guilabel:`Storno invoice (Invoice 380 with negative quantities)`: the credit note is sent as an
  invoice (type 380) whose quantities, and so all its amounts, are negative, with positive unit
  prices. It references the number and the date of the corrected invoice.

The reference to the corrected invoice is taken from the invoice that the credit note reverses:
create the credit note from the invoice with the :guilabel:`Credit Note` button.

.. _localizations/romania/spv-messages:

SPV messages
============

The SPV does not only answer to the uploads: it also sends the errors found in the invoices and
the messages of the buyers. A daily scheduled action, :guilabel:`E-Factura: Store SPV Messages
(RO)`, stores all the messages of each Romanian company that has an access token for the SPV (see
:ref:`localizations/romania/efactura-spv`). In the :guilabel:`SPV Messages` setting:

- :guilabel:`SPV Messages Lookback (days)` is the number of days (1 to 60) requested at each
  synchronization (3 by default);
- :guilabel:`Last SPV Synchronisation` and :guilabel:`Last SPV Error` show the result of the
  last synchronization;
- the :guilabel:`SPV Messages` link opens the messages.

The messages are listed in :menuselection:`Accounting --> Accounting --> SPV Messages (RO)`.
Click :guilabel:`Synchronize Now` to fetch them immediately.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Type
     - Content
   * - :guilabel:`Invoice sent`, :guilabel:`Invoice received`
     - Notifications of the invoices sent and received through the SPV.
   * - :guilabel:`Invoice errors`
     - The validation errors of an uploaded invoice.
   * - :guilabel:`Buyer message received`, :guilabel:`Buyer message sent`
     - The messages exchanged with the buyer about an invoice.
   * - :guilabel:`Other`
     - Any other message of the SPV.

Each message has a status: :guilabel:`New`, :guilabel:`Downloaded` or :guilabel:`Download error`.
The content of the errors, of the buyer messages and of the other messages is downloaded and
shown in the message (not that of the notifications of invoices sent and received);
:guilabel:`Download ZIP` gets the file received from ANAF. Use :guilabel:`Download Content` to try
again after a download error.

A message is linked to the invoice with the same E-Factura index (:guilabel:`Match Invoices`
links the messages that are not linked yet; the filter :guilabel:`Not Matched` lists them). On
the linked invoice:

- the :guilabel:`SPV Messages` button opens its messages;
- the error and buyer messages are posted in the chatter;
- a red banner, *SPV errors*, shows the latest error until the invoice is validated.

.. _localizations/romania/efactura-anaf-check:

Check of the customer at ANAF
=============================

Enable :guilabel:`Check Partner at ANAF before Sending` (:guilabel:`ANAF Check before Sending`
setting) to check the customer when an invoice is sent. If the ANAF data of the customer was last
refreshed more than :guilabel:`ANAF Data Maximum Age (days)` ago (30 by default), Odoo refreshes
its VAT statuses (see :ref:`localizations/romania/anaf-partners`) and notes in the chatter of the
invoice if the lookup failed or if the fiscal code is not in the ANAF register.

The check never blocks the sending. It warns when the customer is registered as an **inactive
taxpayer** or applies the **split VAT payment** system (*plata defalcată a TVA*): a warning
banner is displayed on the invoice, an alert in :guilabel:`Send & Print` with a link to the
contact, and a note in the chatter. The :guilabel:`Inactive Taxpayer (RO)` and :guilabel:`Split
VAT (RO)` fields of the contact give the status.

.. _localizations/romania/pos-invoice:

Invoicing from the Point of Sale
================================

The *PoS Invoice* module checks the invoicing address of the customer while the order is being
registered (see :doc:`../../../sales/point_of_sale/receipts_invoices`). For a Romanian company, a
customer can be invoiced from the Point of Sale only if:

- a **business** customer has a fiscal code (:guilabel:`Tax ID`);
- an **individual** has a name;
- the contact has a street, a city and a country;
- if the country is Romania, the contact has a :guilabel:`State` (the county required by the
  CIUS-RO format). The postal code is **not** required for Romanian addresses.

The :guilabel:`CNP` of an individual is optional. The check uses the company of the point of sale.
The other companies of the database, for example Hungarian ones, keep their own rules.

.. seealso::
   - :ref:`localizations/romania/efactura`
   - :doc:`base`
   - :doc:`../../accounting/customer_invoices/electronic_invoicing/romania`

=====================
Enable Banking (PSD2)
=====================

*Enable Banking* is an account information provider for the :doc:`online bank synchronization
<bank_synchronization>`. It connects Odoo to the bank accounts of Spanish banks and of many other
European banks, using the PSD2 interface every bank has to offer. You give a consent at your bank
once, and Odoo then imports the booked transactions into the matching bank journal, several times a
day, without you handing over your online banking password.

Use it when your bank does not offer a file export you want to upload every day, or when you manage
many accounts and want the transactions and the balance check to be up to date on their own.

.. note::
   The provider is delivered by the *Online Bank Sync: Enable Banking (PSD2)* module
   (``account_bank_sync_enablebanking``), which requires the *Online Bank Sync* module. Enable
   Banking is a third-party service: you need an account and a registered application with them.

Before you start
================

- The people who set up the connection need the :guilabel:`Bank Sync / Manager` access right. The
  person who enters the private key needs :guilabel:`Bank Sync / Admin` (see
  :ref:`accounting/bank-sync/access-rights`).
- Your database must be served over https, and the *web.base.url* system parameter must hold the
  address your users type in their browser: Odoo builds the return address of the bank consent from
  it, and the bank sends your browser back to that address.
- Your bank must be one of those offered by Enable Banking for its country. The list is loaded from
  Enable Banking when you set up the connection.
- Each bank account should have its own :ref:`bank journal <accounting/bank/create>`, or you let
  Odoo create the journals from the IBANs delivered by the bank.

.. _accounting/bank-sync/enablebanking/application:

Register an application at Enable Banking
=========================================

This is done on the Enable Banking site (its *Control Panel*), not in Odoo. Create an application
with the following properties:

- **Environment**: :guilabel:`Sandbox` gives you mock banks to try the connection without touching
  real accounts; :guilabel:`Production` gives you your real banks. The environment is a property of
  the application, so register one application per environment.
- **Redirect URL**: ``https://<your database address>/bank_sync/callback/enablebanking``. This is
  the page where the bank sends you back to Odoo after the consent. It must be identical to the
  address Odoo uses, including the ``https://`` scheme, otherwise the consent is refused.
- **Key pair**: Odoo signs every request with the private key of the application. Generate the pair
  on your own computer and upload only the public certificate, for example:

  .. code-block:: console

     $ openssl req -x509 -newkey rsa:4096 -nodes -days 3650 \\
         -keyout eb_private.pem -out eb_public.crt -subj "/CN=my-company"

  Alternatively, let the Control Panel generate the pair and download the ``.pem`` file.

Enable Banking then shows the **application id** of the application. You need this id and the
private key file (PEM format) in Odoo.

.. warning::
   The private key allows anyone who holds it to access the accounts you connect. Keep the file in
   a safe place and never send it by email or paste it into a chat, a ticket or a document.

.. note::
   A production application that has no commercial agreement with Enable Banking is, according to
   Enable Banking's rules at the time of writing, limited to the bank accounts of its owner, which
   are linked in the Control Panel. Check the conditions with Enable Banking before you connect the
   accounts of other companies.

.. _accounting/bank-sync/enablebanking/settings:

Enter the credentials in Odoo
=============================

Go to :menuselection:`Accounting --> Configuration --> Settings` and, in the :guilabel:`Bank & Cash`
section, find :guilabel:`Enable Banking (PSD2)`. The setting is stored per company. Fill out:

- :guilabel:`Enable Banking environment`: :guilabel:`Sandbox` (default) or :guilabel:`Production`,
  matching the application you registered. New connections take this value.
- :guilabel:`Enable Banking application id`: the id shown by the Control Panel.
- :guilabel:`Enable Banking private key (PEM)`: the whole content of the private key file, from the
  ``-----BEGIN ... PRIVATE KEY-----`` line to the ``END`` line. The field is only displayed to users
  of the :guilabel:`Bank Sync / Admin` group: users with the :guilabel:`Bank Sync / Manager` right
  can use the connection, but cannot read the key.

Click :guilabel:`Save`. The description of the setting repeats the redirect URL to register at
Enable Banking.

.. screenshot:: accounting-bank-sync-enablebanking-settings
   :menu: Accounting ‣ Configuration ‣ Settings ‣ Bank & Cash
   :shows: The "Enable Banking (PSD2)" setting in the Bank & Cash block with the environment
      selector, the application id field and the masked private key field.
   :highlight: The three fields of the setting (red frame).
   :data: Environment "Sandbox", a throw-away application id, a masked key.
   :module: account_bank_sync_enablebanking
   :notes: English UI, light theme, crop to the setting; never show a real key.

Use a separate application for one connection
---------------------------------------------

A connection can carry its own :guilabel:`Enable Banking application id` and :guilabel:`Enable
Banking private key (PEM)` in its :guilabel:`Credentials` section, for example when the accounts
belong to a customer who has an Enable Banking application of their own. Leave both fields empty to
use the company settings.

.. important::
   As soon as a connection has its own application id, it uses its own private key too: it never
   falls back to the key of the company settings. Fill out both fields, or none.

.. _accounting/bank-sync/enablebanking/connect:

Connect a bank
==============

#. Go to :menuselection:`Accounting --> Bank Sync --> Connections` and click :guilabel:`New`.
#. Enter a :guilabel:`Name` and select :guilabel:`Enable Banking (PSD2)` as :guilabel:`Provider`.
   The :guilabel:`Environment` is filled in from the settings.
#. Click :guilabel:`Test connection`. Odoo signs a request with your key: the message *Enable
   Banking application ... works.* confirms that the application id and the key are correct. If
   the environment of the connection differs from the one of the application, the message tells you
   so; correct the :guilabel:`Environment` of the connection.
#. In the :guilabel:`Credentials` section, keep the :guilabel:`Bank country` (two letters, ``ES`` by
   default) or change it, and set the :guilabel:`Account holder type` of the :guilabel:`Bank
   consent` section: :guilabel:`Business` if you log in to the online banking of the company,
   :guilabel:`Personal` otherwise.
#. Click :guilabel:`Load banks`. Odoo reads the banks that Enable Banking offers for the country and
   the holder type, and confirms it with *N banks available in ES.* Select your bank in the
   :guilabel:`Bank` field.
#. Click :guilabel:`Connect to bank`. Your browser opens the login page of your bank; identify
   yourself and authorize the access to your accounts, as you do for any online banking operation.
#. The bank sends you back to Odoo, on the connection. It is now :guilabel:`Connected`, and
   :guilabel:`Consent valid until` shows the end of the consent. The :guilabel:`Session status`
   field shows the state of the session at Enable Banking.

.. screenshot:: accounting-bank-sync-enablebanking-connection
   :menu: Accounting ‣ Bank Sync ‣ Connections ‣ (an Enable Banking connection)
   :shows: An Enable Banking connection in state "Connected" with the Load banks, Connect to bank
      (or Renew consent), Discover accounts and Disconnect buttons, the Bank consent section with
      the expiry date, and the Credentials section with the country, the bank and the session.
   :highlight: The header buttons and the "Consent valid until" field (red frame).
   :data: Connection "Bank Company SL", bank country ES, a business account, consent valid for 180
      days.
   :module: account_bank_sync, account_bank_sync_enablebanking
   :notes: English UI, light theme, 1440px width; the private key field must be empty or masked.

The consent lasts as long as the bank allows, at most 180 days. The :guilabel:`Max. consent (days)`
column of :menuselection:`Accounting --> Bank Sync --> Banks (Enable Banking)` shows the maximum for
each bank; the list is filtered on Spain by default, and the :guilabel:`Holder types` column shows
whether the bank offers business and/or personal logins.

.. tip::
   In the sandbox, the mock banks of Enable Banking can be listed under another country than yours.
   If you do not find the mock bank, change the :guilabel:`Bank country` and load the banks again.

.. tip::
   :guilabel:`Load banks` only lists the banks for the selected :guilabel:`Account holder type`.
   After changing the type, load the banks again. Banks that Enable Banking no longer returns for
   the country are archived in the list.

.. _accounting/bank-sync/enablebanking/accounts:

The accounts and their journals
===============================

When the consent is completed, Odoo reads the accounts of the bank session and creates one
:guilabel:`Bank Sync Account` for each of them, in :menuselection:`Accounting --> Bank Sync -->
Accounts`. Each account is linked to a bank journal:

- if a bank journal of the company already has a bank account with the **same IBAN**, that journal
  is used;
- otherwise, Odoo creates a bank journal named after the account, with a code starting with
  ``EB`` and the IBAN set as its bank account. The journal takes the currency of the account when
  it differs from the company currency.

A journal linked to an account has its :guilabel:`Bank Feeds` setting switched to :guilabel:`Online
Bank Sync`. The :guilabel:`Import (OCA)` button then disappears from the journal card, but statement
files can still be imported with the :guilabel:`Import Statement (OCA)` link, for example to
:ref:`back-fill the older history <accounting/bank/import-backfill>`.

The accounts are created with :guilabel:`Sync enabled` switched **off** and a :guilabel:`Sync every`
interval of 6 hours. To start the automatic import, switch :guilabel:`Sync enabled` on for each
account, and ask your system administrator to enable the *Online Bank Sync: pull statements*
scheduled action (see :ref:`accounting/bank-sync/run`). You can click :guilabel:`Sync now` at any
time to get the first transactions immediately.

.. tip::
   Check the :guilabel:`Journal` of every new account. If your bank did not deliver the IBAN, or if
   the journal's bank account has a different number, Odoo creates a new journal instead of using
   your existing one. Change the :guilabel:`Journal` of the account, and archive the journal that
   was created by mistake.

Use :guilabel:`Discover accounts` on the connection to read the accounts of the session again, for
example after the bank added an account to the consent.

What is imported
================

Odoo asks the bank for the transactions since the last successful run, with a 48-hour overlap, and
books the following as bank statement lines:

- only **booked** transactions. Pending ones are ignored until the bank has booked them;
- the amount, negative for a debit and positive for a credit, and the booking date (or, when the
  bank does not send it, the value date or the transaction date);
- the :guilabel:`Label`, made of the remittance information of the bank (or, in this order, its
  note, the name of the counterparty or the transaction reference);
- the counterparty name and IBAN, when the bank delivers them, which help to recognize the partner
  during :doc:`reconciliation <reconciliation>`;
- a note with the bank's transaction description, reference number and remark.

Every line keeps the transaction id of the bank, prefixed with ``EB-``. When the bank does not send
any id, Odoo builds a stable one from the date, the amount, the label and the counterparty. This id
is what prevents duplicates: running a synchronization again, or renewing the consent, never books a
transaction twice.

The first synchronization only reaches back a short time. If you need the history that precedes the
connection, import a statement file: :ref:`accounting/bank/import-backfill`.

After the transactions, Odoo reads the balance of the account and runs the :ref:`balance check
<accounting/bank-sync/balance-check>`. It uses the booked closing balance of the bank; if the bank
does not report one, the interim, expected, opening or available balance is used, in that order.
With an available balance the comparison can differ from your books by the amount of the pending
operations.

Limits of the bank interface
============================

PSD2 allows the bank to limit the automatic calls made while you are not in front of your screen to
**4 per account and day**. Odoo respects that limit:

- the connection has :guilabel:`Max. unattended syncs per day` set to 4, and the scheduled runs of
  an account are spread at least 6 hours apart. Once the 4 runs of the day (UTC) are used, the next
  scheduled run waits for the next day;
- :guilabel:`Sync now` is a run made while you are present. Odoo does not count it, and tells the
  bank that the request comes from the customer.

If the bank refuses a request because the limit was reached anyway, the account shows the message
*The bank refused the request: daily access limit reached (PSD2 allows 4 automatic updates a day).
Try again tomorrow or sync manually.*

.. _accounting/bank-sync/enablebanking/renew:

Renew the consent
=================

The consent ends at :guilabel:`Consent valid until`. Seven days before (or the number of days set in
:guilabel:`Remind days before expiry`), the :guilabel:`Consent responsible` receives a
:guilabel:`Renew the bank consent` activity. To renew:

#. Open the connection and click :guilabel:`Renew consent`.
#. Authorize the access again at your bank, as for the first consent.
#. Back in Odoo, check that :guilabel:`Consent valid until` moved forward.

You can renew at any time, also after the connection has expired. A renewal creates a new session at
Enable Banking and closes the previous one. Because a bank can give a new identifier to each account
of a new session, Odoo recognizes the accounts again by their stable account identity or, failing
that, their IBAN: your journals, the synchronization settings and the imported transactions are
kept. Some banks only accept one active consent per customer and application, so a new consent can
end the previous one.

To end the access on purpose, click :guilabel:`Disconnect` on the connection and confirm: the
session is closed at Enable Banking, the connection goes back to :guilabel:`Draft`, and a new
authorization at the bank is needed to connect again.

Troubleshooting
===============

Errors of a scheduled or manual synchronization are shown on the account (:guilabel:`Last state`
:guilabel:`Error` and :guilabel:`Last error`); errors of a button on the connection are displayed in
a dialog. Keys and tokens are removed from the messages.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Message
     - What to do
   * - *Set the Enable Banking application id and private key first (Accounting settings or the
       connection).*
     - Fill out the :ref:`credentials <accounting/bank-sync/enablebanking/settings>`. Also check
       that a connection with its own application id has its own key.
   * - *The Enable Banking private key is not a valid PEM RSA key.*
     - Paste the complete content of the key file, from the ``BEGIN`` to the ``END`` line, without
       a password protection.
   * - *Choose the bank first (use 'Load banks' to get the list).*
     - Click :guilabel:`Load banks` and select the :guilabel:`Bank`.
   * - *The bank did not return an authorization code.*
     - The consent was cancelled or refused at the bank. Click :guilabel:`Connect to bank` again.
   * - *The bank authorization took too long. Please start it again.*
     - The consent must be completed within an hour. Click :guilabel:`Connect to bank` again.
   * - *The bank consent is no longer valid (...). Renew the consent on the connection.*
     - The session expired or was closed or revoked at the bank. The connection is set to
       :guilabel:`Expired`: click :guilabel:`Renew consent`.
   * - *The bank consent expired on ... Renew it on the connection.*
     - Same as above; Odoo stopped calling the bank when the consent ended.
   * - *The bank refused the request: daily access limit reached ...*
     - Wait for the next day, or click :guilabel:`Sync now`.
   * - *Enable Banking is not reachable: ...*
     - A network problem or a temporary outage of the service. The next scheduled run tries again.
   * - *Enable Banking error <status> <code>: ...*
     - The answer of Enable Banking, unchanged. A 4xx status usually points to the application (for
       instance an unknown redirect URL or an environment mismatch), a 5xx status to a temporary
       problem at Enable Banking or the bank.
   * - The bank returns you to Odoo with *Bank authorization failed*
     - The bank or Enable Banking refused the consent; the reason is displayed. Fix it and click
       :guilabel:`Connect to bank` again. If the redirect URL is refused, compare it with the one
       registered in the Control Panel.

.. seealso::
   - :doc:`bank_synchronization`
   - :doc:`statement_import`
   - :doc:`reconciliation`

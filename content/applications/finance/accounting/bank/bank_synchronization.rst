=====================
Bank synchronization
=====================

Odoo can fetch your bank transactions automatically instead of having you upload a statement file
every day. The *Online Bank Sync* modules connect a bank or payment account to an Odoo journal,
poll the provider at a fixed interval, and create the matching bank statement lines, ready for
:doc:`reconciliation <reconciliation>`.

The feature is split in two layers:

- **Online Bank Sync** (``account_bank_sync``) provides the connections, the remote accounts, the
  journal mapping, the scheduled import, and the secure storage of the provider credentials.
- A **provider module** implements one specific institution or aggregator. Three are available:

  - **Enable Banking (PSD2)** (``account_bank_sync_enablebanking``) — a PSD2 account information
    provider for Spanish and other European banks, with a consent given at the bank. See
    :doc:`enable_banking`.
  - **Nyíltbankolás Partner** (``account_bank_sync_bankszamlakivonat``) — a multi-bank aggregator
    covering the Hungarian banks through the `bankszamlakivonat.hu` service.
  - **Wise** (``account_bank_sync_wise``) — the Wise (formerly TransferWise) multi-currency
    balances, including outbound payouts.

.. note::
   Online synchronization requires at least one provider module. If your bank is not covered by a
   provider, :doc:`import the statement files <statement_import>` instead.

.. _accounting/bank-sync/which-method:

File import or online synchronization?
======================================

Both methods end in the same place: bank statement lines in a bank journal, ready for
:doc:`reconciliation <reconciliation>`. Choose according to what your bank offers and how fresh the
data must be.

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * -
     - :doc:`File import <statement_import>`
     - Online synchronization
   * - Freshness
     - As fresh as the last file you downloaded.
     - Automatic; scheduled runs and a manual :guilabel:`Sync now` button.
   * - Set-up
     - Nothing to configure besides the bank account and the journal.
     - A provider account, credentials and, for PSD2 banks, a consent given at the bank.
   * - Upkeep
     - Someone downloads and uploads a file regularly.
     - The consent must be renewed at the bank (PSD2: at most every 180 days), and the number of
       automatic calls per day is limited by the bank.
   * - History
     - Whatever period the file covers.
     - Starts when the connection is made; older history is not pulled.

The two methods work well together. Connect the journal for the day-to-day flow, then
:ref:`back-fill the older history from a statement file <accounting/bank/import-backfill>`. When
the *Online Bank Sync* and the file import are both installed, the lines of the file that the
synchronization has already booked are skipped automatically.

.. _accounting/bank-sync/access-rights:

Access rights
=============

Synchronization introduces its own access groups, which you assign under :menuselection:`Settings
--> Users & Companies --> Users` in the :guilabel:`Online Bank Sync` category:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Group
     - Rights
   * - :guilabel:`Bank Sync / User`
     - Read the synchronization status and results. No access to credentials.
   * - :guilabel:`Bank Sync / Manager`
     - Configure connections, accounts, and the journal mapping. Required to see the
       :guilabel:`Bank Sync` menu. No access to credentials.
   * - :guilabel:`Bank Sync / Payment Approver`
     - Approve and send outbound payouts.
   * - :guilabel:`Bank Sync / Admin`
     - Read and write the provider credentials and secrets, such as private keys.

The groups build on each other: *Manager* includes *User*, and *Payment Approver* and *Admin* both
include *Manager*.

.. warning::
   The :guilabel:`Bank Sync / Admin` group also grants the *Settings* administrator rights. Assign
   it only to the people who may manage the whole database.

.. _accounting/bank-sync/connection:

Create a connection
===================

Go to :menuselection:`Accounting --> Bank Sync --> Connections` and click :guilabel:`New`. Fill out:

- :guilabel:`Name`: a label of your choice, e.g. the name of the bank.
- :guilabel:`Provider`: the provider module handling this institution.
- :guilabel:`Environment`: :guilabel:`Sandbox` for testing, :guilabel:`Production` for live data.
- The :guilabel:`Credentials` section, whose fields depend on the selected provider. Secrets such as
  private keys are only visible to the :guilabel:`Bank Sync / Admin` group.

The :guilabel:`Capabilities` section is filled in by the provider module and tells you what the
connection supports: :guilabel:`Supports statement pull`, :guilabel:`Supports FX rates`,
:guilabel:`Supports webhooks`, :guilabel:`Supports payouts` and :guilabel:`Supports consent
redirect`.

Click :guilabel:`Test connection` to verify the credentials: a notification confirms that the
provider answered, and if it refuses the credentials the reason is displayed in an error message.

The status bar shows where the connection stands. How a connection becomes :guilabel:`Connected`
depends on the provider: with Wise, a successful :guilabel:`Test connection`; with Nyíltbankolás,
the end of the pairing (:guilabel:`Refresh / discover`); with Enable Banking, the consent given at
the bank. A failed bank authorization sets the status to :guilabel:`Error` and stores the reason in
:guilabel:`Last error`. A connection whose consent has run out is set to :guilabel:`Expired` and
must be renewed, see :ref:`accounting/bank-sync/consent`.

.. screenshot:: accounting-bank-sync-connection
   :menu: Accounting ‣ Bank Sync ‣ Connections ‣ (open a connection)
   :shows: A connection form in state "Connected", with the Name, Provider, Environment, Last
      refresh fields, a filled Credentials section and the five Capabilities checkboxes.
   :highlight: The status bar and the "Test connection" / "Discover accounts" buttons.
   :data: Connection "OTP – Nyíltbankolás", provider "Nyíltbankolás Partner", environment
      "Production".
   :module: account_bank_sync, account_bank_sync_bankszamlakivonat
   :notes: English UI, light theme, 1440px width; use a throw-away API key.

.. _accounting/bank-sync/nyiltbankolas:

Nyíltbankolás Partner
---------------------

The aggregator connects to the Hungarian banks on your behalf. Enter the :guilabel:`Nyíltbankolás
entity id` and the :guilabel:`Nyíltbankolás API key` you received from the service, then click
:guilabel:`Get connection code`.
Odoo requests a connection code, which is displayed in the :guilabel:`Connection code` field: use it
on the provider's site to authorize your bank accounts. Once the authorization is done, click
:guilabel:`Refresh / discover`: the connection becomes :guilabel:`Connected` and the list of
authorized accounts is pulled into Odoo. Requesting a new connection code sets the connection back
to :guilabel:`Draft` until the pairing is finished again.

.. _accounting/bank-sync/wise:

Wise
----

Enter the :guilabel:`Wise profile id` and the :guilabel:`Wise API token`. For payouts, Wise also
requires a :guilabel:`Wise SCA RSA private key (PEM)` used to sign strong-customer-authentication
challenges, and for webhook delivery the :guilabel:`Wise webhook public key (PEM)` published by Wise
for the chosen environment. Use
:guilabel:`Subscribe webhooks` to register Odoo with Wise so that new transactions trigger an
immediate refresh, and :guilabel:`Unsubscribe webhooks` to stop them.

.. important::
   Webhook events are delivered to `/bank_sync/webhook/<provider>` on your database. Signature
   verification fails closed: an event that cannot be verified is rejected. Ask your system
   administrator to make sure this address is reachable from the internet.

.. _accounting/bank-sync/consent:

Bank consent and expiry
=======================

Providers that read your accounts through PSD2 (currently Enable Banking) do not use a password
stored in Odoo. Instead, you give a **consent** at your bank, with the bank's own strong customer
authentication. The :guilabel:`Bank consent` section of the connection, shown for such providers,
holds the settings:

- :guilabel:`Account holder type`: :guilabel:`Business` (default) or :guilabel:`Personal`, the type
  of online banking login you use at the bank.
- :guilabel:`Consent valid until`: the end of the consent. PSD2 allows at most 180 days, and a bank
  may grant less.
- :guilabel:`Consent responsible`: the user who receives the renewal reminder (by default, the user
  who created the connection).
- :guilabel:`Remind days before expiry`: how many days ahead the reminder is created (7 by default).
- :guilabel:`Max. unattended syncs per day`: how many scheduled synchronizations the bank allows per
  account and day (see :ref:`accounting/bank-sync/run`). Enable Banking sets 4.

Click :guilabel:`Connect to bank` to open the authorization page of the bank. When you come back to
Odoo, the connection is :guilabel:`Connected` and :guilabel:`Consent valid until` is filled in. A
message is logged in the chatter of the connection. If the authorization is refused or takes longer
than an hour, an error page is displayed with a link back to the connections; start again with
:guilabel:`Connect to bank`.

Once a day, the *Online Bank Sync: consent expiry reminder* scheduled action (enabled by default)
does two things:

- when the consent is :guilabel:`Remind days before expiry` days from its end, it schedules a
  :guilabel:`Renew the bank consent` activity for the :guilabel:`Consent responsible`;
- when the consent has ended, it sets the connection to :guilabel:`Expired` and logs a message.

An expired connection is not called any more: its accounts show the error *The bank consent expired
on ...* until you click :guilabel:`Renew consent` and authorize again at the bank. The accounts, the
journal mapping and the imported history are kept, and the next synchronization catches up from the
last successful run (within what the bank still delivers).

.. _accounting/bank-sync/accounts:

Map the remote accounts to journals
===================================

On a connected connection, click :guilabel:`Discover accounts`. Odoo queries the provider and
creates one :guilabel:`Bank Sync Account` record per remote account or balance. Open
:menuselection:`Accounting --> Bank Sync --> Accounts` and set, for each of them:

- :guilabel:`Journal`: the bank journal in which the transactions are booked. **Nothing is imported
  until a journal is set.**
- :guilabel:`Sync enabled`: activates the scheduled import for this account. It is off by default,
  also for the accounts discovered by a provider.
- :guilabel:`Sync every`: the polling interval (for example, 1 hour). For a provider with a daily
  call limit, Odoo never polls more often than the limit allows (every 6 hours for 4 calls a day).

The list view shows :guilabel:`Last successful run` and a colored :guilabel:`Last state` badge
(:guilabel:`OK`, :guilabel:`Running`, :guilabel:`Error`), so you can spot an account that has
stopped importing at a glance. The optional :guilabel:`Balance difference` column belongs to the
:ref:`balance check <accounting/bank-sync/balance-check>`.

Once a journal is mapped, its :guilabel:`Bank Feeds` setting (:guilabel:`Journal Entries` tab of the
journal) is set to :guilabel:`Online Bank Sync`, and the journal card of the
:guilabel:`Accounting Dashboard` gets a :guilabel:`Sync now` button. Statement files can still be
imported into the journal, see :ref:`accounting/bank/import-backfill`.

.. screenshot:: accounting-bank-sync-accounts
   :menu: Accounting ‣ Bank Sync ‣ Accounts
   :shows: The Accounts list with three rows: connection, account name, currency, mapped journal,
      the "Sync enabled" toggle, the last successful run and the colored state badges (one "Ok",
      one "Error").
   :highlight: The "Last state" column (red frame).
   :data: Two HUF accounts mapped to "Bank" and "Bank (OTP)", one EUR Wise balance.
   :module: account_bank_sync
   :notes: English UI, light theme, 1440px width.

.. _accounting/bank-sync/run:

Run a synchronization
=====================

There are three ways a synchronization runs:

- **Scheduled**: the *Online Bank Sync: pull statements* scheduled action checks every 15 minutes
  which accounts are due and imports them. This scheduled action is **disabled by default**; ask
  your system administrator to enable it once the mapping is in place.
- **Manual**: click :guilabel:`Sync now` on the account form, or on the journal card of the
  :guilabel:`Accounting Dashboard`. Manual runs are made while you are present, so they do not use
  up the daily limit of the scheduled runs described below.
- **Webhook-triggered**: for providers supporting webhooks, an incoming event flags the account and
  the next scheduled run imports it immediately, even when periodic polling is off.

Each run fetches the transactions since the last successful run, with a 48-hour overlap so that
transactions the bank posts late are not missed. Importing is **idempotent**: a transaction already
present in the journal is skipped, so running a synchronization twice never creates duplicates.

.. note::
   A synchronization only looks back a short time before its first run. It does not load the
   history that precedes the connection: import it from a statement file, see
   :ref:`accounting/bank/import-backfill`.

**Daily limit of PSD2 banks.** PSD2 allows a bank to refuse more than 4 account requests a day when
the customer is not present. When the connection has a value in :guilabel:`Max. unattended syncs per
day`, the scheduled runs stop for the rest of the day (UTC) once that number is reached for an
account, and resume the next day. Manual runs are not counted.

If a run fails, the account is set to :guilabel:`Error` and the message is stored in
:guilabel:`Last error`; the other accounts are not affected. Credentials and tokens are removed from
the stored messages.

.. warning::
   :guilabel:`Sync now` displays *Bank sync finished.* even when the run failed, because the error
   is recorded on the account instead of being raised. After a manual synchronization, check
   :guilabel:`Last state` and :guilabel:`Last error` on the account.

.. _accounting/bank-sync/balance-check:

Balance check
=============

When the provider reports the balance of the account (Enable Banking does), every successful run
compares the booked balance of the bank with the balance of the journal's bank account in your
books, up to the date of the bank balance. Only posted entries count. The account form shows the
result in the :guilabel:`Balance check` section (:guilabel:`Balance`, :guilabel:`Bank balance date`,
:guilabel:`Accounting balance` and :guilabel:`Balance difference`, in red when it is not zero).

When the two differ, the journal card of the :guilabel:`Accounting Dashboard` shows a
:guilabel:`Balance differs` warning next to :guilabel:`Sync now`. The usual reasons are:

- the balance of the account before the first imported transaction was never booked in Odoo. Post
  an opening balance entry in the journal's bank account;
- transactions are still missing, for example because the history was not back-filled;
- a transaction is still pending at the bank: Enable Banking only imports booked transactions.

The check is a control, not a correction: nothing is booked automatically.

.. _accounting/bank-sync/payouts:

Outbound payouts
================

Providers that support payouts (currently Wise) can also send money out of Odoo. Because this moves
real funds, payouts are protected by a maker–checker workflow.

Configuration
-------------

On the connection form, in the :guilabel:`Payout controls` section:

- :guilabel:`Payout enabled`: the feature flag, editable by the :guilabel:`Bank Sync / Admin` group
  only. Payouts remain impossible while it is off, even if the provider supports them.
- :guilabel:`Payout dual control threshold`: above this amount, a second person must approve. Set it
  to 0 to always require a separate approver.
- :guilabel:`Payout per tx limit`: the largest single payout allowed. 0 means no limit.
- :guilabel:`Payout daily limit`: the largest total that may be approved per day (UTC). 0 means no
  limit.

Create and send a payout
------------------------

Go to :menuselection:`Accounting --> Bank Sync --> Payouts` and click :guilabel:`New`. Set the
:guilabel:`Payee`, the :guilabel:`Recipient bank account`, the :guilabel:`Amount` and currency, and
a :guilabel:`Payment reference` (35 characters maximum, as required by SEPA). Then use the buttons
in the header:

#. :guilabel:`Quote` asks the provider for the exchange rate and the fee, shown in the
   :guilabel:`Quote` section together with an expiry time.
#. :guilabel:`Request` submits the payout for approval. Whether dual control applies is frozen at
   this moment, so raising the threshold afterwards cannot weaken it.
#. :guilabel:`Approve` is done by a user with the :guilabel:`Bank Sync / Payment Approver` group.
   When dual control applies, the approver must be a different person from the one who requested it.
#. :guilabel:`Send via Wise` transmits the payout to the provider.

The status bar follows the payout through :guilabel:`Draft`, :guilabel:`Pending checker`,
:guilabel:`Approved`, :guilabel:`Submitted`, :guilabel:`Executed` and :guilabel:`Reconciled`, with
:guilabel:`Failed` and :guilabel:`Cancelled` as the alternative outcomes. :guilabel:`Cancel` is
available until the payout has been executed. Once the provider confirms the transfer, the payout
receipt can be fetched and stored on the record.

.. note::
   Each payout carries an idempotency key, so a network problem during sending can never result in
   the money being transferred twice.

Payout batches
--------------

To pay several recipients at once, use :menuselection:`Accounting --> Bank Sync --> Payout Batches`.
A batch holds its payouts in the :guilabel:`Members` tab and offers the same steps at batch level:
:guilabel:`Quote all`, :guilabel:`Request`, :guilabel:`Approve`, :guilabel:`Send`,
:guilabel:`Refund` and :guilabel:`Cancel`. The limits and the dual-control rule of the connection
apply to the batch total.

.. screenshot:: accounting-bank-sync-payout
   :menu: Accounting ‣ Bank Sync ‣ Payouts ‣ (open a payout)
   :shows: A payout form in state "Pending checker" with the header buttons Quote / Request /
      Approve / Send via Wise / Cancel, the Payee, amount and payment reference, and the Quote
      section showing the rate, the fee and the expiry.
   :highlight: The status bar and the Approval section (requester and approver).
   :data: Payee "Deco Addict", amount 1,250.00 EUR, reference "INV/2026/0042".
   :module: account_bank_sync, account_bank_sync_wise
   :notes: English UI, light theme, 1440px width.

.. seealso::
   - :doc:`statement_import`
   - :doc:`transactions`
   - :doc:`reconciliation`

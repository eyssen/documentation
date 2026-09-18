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
- A **provider module** implements one specific institution or aggregator. Two are available:

  - **Nyíltbankolás Partner** (``account_bank_sync_bankszamlakivonat``) — a multi-bank aggregator
    covering the Hungarian banks through the `bankszamlakivonat.hu` service.
  - **Wise** (``account_bank_sync_wise``) — the Wise (formerly TransferWise) multi-currency
    balances, including outbound payouts.

.. note::
   Online synchronization requires at least one provider module. If your bank is not covered by a
   provider, :doc:`import the statement files <statement_import>` instead.

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
       :guilabel:`Bank Sync` menu.
   * - :guilabel:`Bank Sync / Payment Approver`
     - Approve and send outbound payouts.
   * - :guilabel:`Bank Sync / Admin`
     - Read and write the provider credentials and secrets.

.. _accounting/bank-sync/connection:

Create a connection
===================

Go to :menuselection:`Accounting --> Bank Sync --> Connections` and click :guilabel:`New`. Fill out:

- :guilabel:`Name`: a label of your choice, e.g. the name of the bank.
- :guilabel:`Provider`: the provider module handling this institution.
- :guilabel:`Environment`: :guilabel:`Sandbox` for testing, :guilabel:`Production` for live data.
- The :guilabel:`Credentials` section, whose fields depend on the selected provider. Credentials are
  only visible to the :guilabel:`Bank Sync / Admin` group.

The :guilabel:`Capabilities` section is filled in by the provider module and tells you what the
connection supports: :guilabel:`Supports statement pull`, :guilabel:`Supports FX rates`,
:guilabel:`Supports webhooks`, and :guilabel:`Supports payouts`.

Click :guilabel:`Test connection` to verify the credentials. The :guilabel:`Status` bar moves from
:guilabel:`Draft` to :guilabel:`Connected`; if the provider refuses the credentials, the status
becomes :guilabel:`Error` and the reason is shown in :guilabel:`Last error`. A connection whose
authorization has run out is set to :guilabel:`Expired` and must be renewed with the provider.

.. screenshot:: accounting-bank-sync-connection
   :menu: Accounting ‣ Bank Sync ‣ Connections ‣ (open a connection)
   :shows: A connection form in state "Connected", with the Name, Provider, Environment, Last
      refresh fields, a filled Credentials section and the four Capabilities checkboxes.
   :highlight: The status bar and the "Test connection" / "Discover accounts" buttons.
   :data: Connection "OTP – Nyíltbankolás", provider "Nyíltbankolás Partner", environment
      "Production".
   :module: account_bank_sync, account_bank_sync_bankszamlakivonat
   :notes: English UI, light theme, 1440px width; use a throw-away API key.

.. _accounting/bank-sync/nyiltbankolas:

Nyíltbankolás Partner
---------------------

The aggregator connects to the Hungarian banks on your behalf. Enter the :guilabel:`Entity id` and
the :guilabel:`API key` you received from the service, then click :guilabel:`Get connection code`.
Odoo requests a connection code, which is displayed in the :guilabel:`Connection code` field: use it
on the provider's site to authorize your bank accounts. Once the authorization is done, click
:guilabel:`Refresh / discover` to pull the list of authorized accounts into Odoo.

.. _accounting/bank-sync/wise:

Wise
----

Enter the :guilabel:`Wise profile id` and the :guilabel:`API token`. For payouts, Wise also requires
a :guilabel:`Private key` used to sign strong-customer-authentication challenges, and for webhook
delivery the :guilabel:`Webhook public key` published by Wise for the chosen environment. Use
:guilabel:`Subscribe webhooks` to register Odoo with Wise so that new transactions trigger an
immediate refresh, and :guilabel:`Unsubscribe webhooks` to stop them.

.. important::
   Webhook events are delivered to `/bank_sync/webhook/<provider>` on your database. Signature
   verification fails closed: an event that cannot be verified is rejected. Ask your system
   administrator to make sure this address is reachable from the internet.

.. _accounting/bank-sync/accounts:

Map the remote accounts to journals
===================================

On a connected connection, click :guilabel:`Discover accounts`. Odoo queries the provider and
creates one :guilabel:`Bank Sync Account` record per remote account or balance. Open
:menuselection:`Accounting --> Bank Sync --> Accounts` and set, for each of them:

- :guilabel:`Journal`: the bank journal in which the transactions are booked. **Nothing is imported
  until a journal is set.**
- :guilabel:`Sync enabled`: activates the scheduled import for this account.
- :guilabel:`Sync every`: the polling interval (for example, 1 hour).

The list view shows :guilabel:`Last successful run` and a colored :guilabel:`Last state` badge
(:guilabel:`Ok`, :guilabel:`Error`, :guilabel:`Stale`), so you can spot an account that has stopped
importing at a glance.

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
  :guilabel:`Accounting Dashboard`.
- **Webhook-triggered**: for providers supporting webhooks, an incoming event flags the account and
  the next scheduled run imports it immediately, even when periodic polling is off.

Each run fetches the transactions since the last successful run, with a 48-hour overlap so that
transactions the bank posts late are not missed. Importing is **idempotent**: a transaction already
present in the journal is skipped, so running a synchronization twice never creates duplicates.

If a run fails, the account is set to :guilabel:`Error` and the message is stored in
:guilabel:`Last error`; the other accounts are not affected. Credentials and tokens are removed from
the stored messages.

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

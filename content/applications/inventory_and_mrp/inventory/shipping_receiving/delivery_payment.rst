.. _inventory/shipping_receiving/delivery_payment:

==============================
Delivery-based payment methods
==============================

Which payment options a webshop should offer depends on how the order will be delivered: cash on
delivery (COD) only makes sense with a carrier that actually collects money at the door or at a
pickup point, while a B2B pallet carrier may be strictly prepaid. Standard Odoo offers the same
payment providers regardless of the chosen delivery method (only the optional Click & Collect
feature ties its own "Pay on site" option to in-store pickup), and its offline payment flow (the
one COD is built on) shows wire-transfer wording and a JavaScript-dependent waiting page that fit
a bank transfer, not a parcel paid at handover.

The eYssen delivery–payment layer solves both problems. The ``eyssen_delivery_payment`` module
lets each shipping method declare exactly which payment providers may be offered with it, teaches
checkout to validate COD options against the *delivery* address, and rewrites the post-checkout
screens so a COD customer reads "your order has been confirmed — pay on delivery" instead of bank
transfer instructions. The companion ``payment_custom_skip_status`` module makes the redirect to
the order confirmation page robust for every offline payment method by skipping the intermediate
payment-status page on the server side.

.. seealso::
   - :doc:`cash_on_delivery` — how the collectable COD amount is computed per outgoing delivery,
     and the Utánvét Ellenőr fraud screening
   - :doc:`payment_gated_delivery` — holding outgoing deliveries until an order is paid
   - :doc:`delivery_status_and_dates` — delivery progress and dates on orders and invoices
   - :doc:`setup_configuration/gls`, :doc:`setup_configuration/foxpost` and
     :doc:`setup_configuration/mpl` — the carrier integrations that ship the COD providers

How payment methods are filtered per delivery method
====================================================

Every shipping method (:menuselection:`Inventory app --> Configuration --> Delivery Methods`)
gains a :guilabel:`Payment Providers` tab with a single field, :guilabel:`Enabled payment
acquirers`. It is a whitelist:

- When the list is **empty**, nothing changes: the shopper is offered every payment provider that
  is otherwise compatible with the order (enabled, published, matching country, currency and
  amount limits).
- When the list is **filled**, only the listed providers survive the compatibility check while
  this shipping method is selected. Because payment methods are derived from the surviving
  providers, filtering a provider out also removes its payment methods from the payment step.

The shopper sees the effect immediately: changing the delivery method at checkout changes the set
of payment options presented on the payment step.

.. important::
   The shipping methods shipped by the GLS, Foxpost and MPL integrations come with their
   :guilabel:`Enabled payment acquirers` list pre-filled with **only that carrier's own COD
   provider**. Out of the box, selecting such a shipping method therefore offers COD *alone*. Add
   the shop's online providers (card, wire transfer, …) to each shipping method's list to offer a
   mixed choice.

When several providers remain, they are ranked by *specificity*: each of :guilabel:`Countries`,
:guilabel:`Currencies` and :guilabel:`Maximum Amount` set on a payment provider counts as one
point, and higher-scoring providers take precedence over catch-all ones. This ranking does not
change the order of the payment options shown to the shopper (that follows the payment methods'
own sequence); it decides which provider serves a shared payment method: when two providers can
serve the same method (for example two providers behind one "Pay by card" method), the most
specific compatible provider is the one that actually processes the transaction.

Cash on delivery at checkout
============================

Payment providers can carry a technical *COD* flag. The shared layer itself marks no provider as
COD — the flag is set by the carrier integrations for their own :guilabel:`Payment on
Delivery`-style providers, so COD behavior appears only once at least one carrier module (GLS,
Foxpost or MPL) is installed. For flagged providers, checkout behaves differently in three ways:

- **Availability follows the delivery address.** For regular (online) providers, Odoo checks the
  provider's :guilabel:`Countries` limit against the customer's (billing) address, and its
  currency and amount limits against the order. For COD providers, the compatibility check is
  re-run with the **shipping address** instead — a COD provider limited to Hungary is offered for
  a parcel going to a Hungarian pickup point even when the billing address is foreign, and hidden
  when the parcel itself leaves the country.
- **The pending screens drop the wire-transfer wording.** The offline payment flow normally shows
  the heading :guilabel:`Finalize your payment`, a bank-app QR code and a
  :guilabel:`Communication` block with the transfer reference. For COD, the heading becomes
  :guilabel:`Thank you for your order` and the QR and reference blocks are hidden. Real wire
  transfers keep the original screens untouched.
- **The order confirmation card turns green.** On the order confirmation page, a pending COD
  payment is shown as a green success card instead of the blue "waiting for payment" card, and the
  card displays the provider's :guilabel:`Pending Message` — by default *"Your order has been
  confirmed. Please pay upon delivery."* (in Hungarian: *"Rendelésed visszaigazolásra került.
  Kérjük, fizess átvételkor."*).

Each carrier integration ships its own COD provider:

.. list-table::
   :header-rows: 1
   :widths: 20 48 32

   * - Carrier
     - COD payment provider
     - Documentation
   * - GLS
     - :guilabel:`Payment on Delivery`
     - :doc:`setup_configuration/gls`
   * - Foxpost
     - :guilabel:`FoxPost COD, with credit card at parcelmachine or at delivery`
       (ships with a :guilabel:`Maximum Amount` of 150 000, in the company's main currency — HUF
       for a Hungarian shop)
     - :doc:`setup_configuration/foxpost`
   * - MPL
     - :guilabel:`MPL COD, with credit card at parcelshop or at delivery`
     - :doc:`setup_configuration/mpl`

Each COD option also hides itself automatically when no published shipping method of its carrier
exists on the website, or when the cart contains no physical products.

.. note::
   The whitelist reliably restricts *online* payment providers. COD providers are validated on
   their own track (against the delivery address), so an enabled COD option belonging to a
   *different* carrier can still be offered even when it is not on the selected shipping method's
   list — its own carrier-published/physical-goods rules are what hide it. To remove a COD option
   from the shop entirely, disable or unpublish its payment provider instead of relying on the
   whitelist alone.

.. important::
   The green card and the *"Your order has been confirmed"* wording are customer-facing copy — the
   sales order itself is **not** confirmed automatically by a pending COD payment. The standard
   payment post-processing only marks the quotation as sent, assigns the payment reference and
   sends the payment-status e-mail; confirming the order (and thereby creating the delivery)
   remains a back-office step, or whatever order-confirmation automation the shop already uses.

The amount actually collected at the door is *not* simply the order total: it is computed per
outgoing delivery (transfer) at shipping-label time — one amount covering all packages of the
transfer — taking partial shipments, service lines and invoiced down payments into account. See
:doc:`cash_on_delivery` for the full computation, and for the Utánvét Ellenőr reputation
screening that can hide COD from unreliable customers.

Order confirmation without online payment
=========================================

With any offline payment method (COD, wire transfer), no payment gateway ever confirms the
transaction — it simply rests as *pending*. Standard Odoo bridges this with an
intermediate payment-status page ("Please wait…") whose JavaScript polls the server and then
forwards the customer to the order confirmation. If that JavaScript fails to run — a blocked or
broken asset bundle, an aggressive privacy extension, a script blocked on that page — the
customer is stranded on the waiting page and may believe the order failed.

The ``payment_custom_skip_status`` module removes this fragility on the server side. When the
customer arrives at the payment-status page with exactly one *offline* transaction being monitored
in their checkout session, resting in the pending state, the server answers with a direct redirect
to the order confirmation page — the waiting page is never rendered, and no browser scripting is
involved. Every other situation (online providers, an errored or cancelled transaction, an expired
session) falls through to the standard page, so retry and error handling keep working exactly as
before.

.. note::
   The redirect deliberately does not finalize the transaction on the spot. The follow-up work —
   marking the quotation as sent, generating the payment reference, sending the payment-status
   e-mail — is left to the standard :guilabel:`Payment: Post-process transactions` scheduled
   action, which runs every 10 minutes. Customers see their confirmation page instantly; the
   paperwork catches up within minutes.

.. note::
   The skip applies to *all* offline custom payment methods, not only COD: wire-transfer customers
   also land directly on the order confirmation page, where the provider's payment instructions
   (the bank details from its :guilabel:`Pending Message`) are still displayed in the confirmation
   card; the :guilabel:`Communication` transfer reference appears there once the
   :guilabel:`Payment: Post-process transactions` action has assigned it, within a few minutes.

Configuration
=============

Installing ``eyssen_delivery_payment`` automatically installs ``payment_custom_skip_status`` as a
dependency; the latter has no settings of its own.

To control which payment options each delivery method offers:

#. Go to :menuselection:`Inventory app --> Configuration --> Delivery Methods` and open a shipping
   method.
#. On the :guilabel:`Payment Providers` tab, fill :guilabel:`Enabled payment acquirers` with every
   provider that may be offered together with this method — typically the carrier's COD provider
   plus the shop's online card provider. Leave the list empty to allow all compatible providers.

To influence which provider serves a payment method offered by several providers, set the
availability limits on each payment provider (:menuselection:`Website --> Configuration -->
eCommerce: Payment Providers`, :guilabel:`Configuration` tab): :guilabel:`Countries`,
:guilabel:`Currencies` and :guilabel:`Maximum Amount`. The more of these a provider defines, the
higher its precedence when a shared payment method is paid.

The customer-facing COD text comes from each COD provider's :guilabel:`Pending Message` and can be
edited freely on the provider form.

.. note::
   The COD pending messages are provisioned automatically when the module is installed (a
   one-time migration also applied them when upgrading to version 18.0.1.1): every COD provider
   whose :guilabel:`Pending Message` is empty or still contains the generic "waiting for approval"
   default receives the COD copy, in English and — when the Hungarian language is installed — in
   Hungarian. A provider whose message has been customized in every installed language is left
   untouched (if either the English or the Hungarian text still holds the default, both are
   replaced with the COD copy).

.. important::
   The scheduled action :guilabel:`Payment: Post-process transactions` must be active for COD and
   wire-transfer orders to receive their follow-up processing after the skipped status page. Odoo
   activates it automatically when a payment provider is enabled; do not archive it.

Usage
=====

#. The administrator fills the :guilabel:`Enabled payment acquirers` list on each shipping method,
   pairing every carrier with the payment options that make sense for it.
#. At checkout, the shopper selects a delivery method — for example a parcel-machine carrier.
#. On the payment step, only the payment options allowed for that shipping method are offered, and
   COD options appear or disappear based on the delivery address.
#. The shopper picks :guilabel:`Payment on Delivery` and confirms. They are redirected straight to
   the order confirmation page, which shows a green card reading *"Your order has been confirmed.
   Please pay upon delivery."* — the waiting page is never shown, and the redirect needs no
   JavaScript on the status page.
#. The back office confirms the order as usual; when the shipping label is generated, the exact
   amount to collect is computed per outgoing delivery as described in :doc:`cash_on_delivery`.

Scope and modules
=================

- ``eyssen_delivery_payment`` — the per-shipping-method :guilabel:`Enabled payment acquirers`
  whitelist, the COD flag with delivery-address compatibility and specificity-based provider
  selection, and the rewritten COD pending and confirmation screens.
- ``payment_custom_skip_status`` — the server-side skip of the payment-status waiting page for
  pending offline transactions, making the redirect to the order confirmation independent of
  browser JavaScript.

The dynamic per-delivery COD amount is provided by ``eyssen_delivery_cod`` and is documented on
:doc:`cash_on_delivery`; the COD providers themselves ship with the carrier integrations
(:doc:`setup_configuration/gls`, :doc:`setup_configuration/foxpost`,
:doc:`setup_configuration/mpl`).

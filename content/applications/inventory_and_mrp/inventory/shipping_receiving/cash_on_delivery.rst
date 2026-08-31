======================
Cash on delivery (COD)
======================

.. Screenshot plan:
..
.. cash_on_delivery-checkout-payment-methods.png
..   What: the website checkout payment step for a logged-in customer whose
..   reputation is above the configured threshold, showing the "Payment on
..   Delivery" option next to the other payment methods.
..   Click path: Website app --> open the shop --> add a product to the
..   cart --> proceed to checkout --> reach the Payment step.
..
.. cash_on_delivery-provider-check-toggle.png
..   What: a "Payment on Delivery" payment.provider form (e.g. the one
..   created by eyssen_delivery_gls) with the Configuration tab open on the
..   Availability group, showing the "Utánvét Ellenőr Check" checkbox.
..   Click path: Website app --> Configuration --> Payment Providers -->
..   open "Payment on Delivery" --> Configuration tab --> Availability
..   group.
..
.. cash_on_delivery-settings.png
..   What: the Website Settings page scrolled to the "Shop - Checkout
..   Process" block, with the "Utánvét Ellenőr" collapsible setting expanded
..   showing Mode, key fields, Reputation Threshold, Fallback on API Error,
..   API Timeout and Chatter Verbosity.
..   Click path: Website app --> Configuration --> Settings --> Shop -
..   Checkout Process section --> Utánvét Ellenőr.
..
.. cash_on_delivery-partner-chatter-log.png
..   What: a res.partner (Contacts) form with the chatter open, showing an
..   internal note logged by the module after a blocked or errored check
..   (Mode, Threshold, HTTP status, Good/Bad, Reputation, Blocked, Reason
..   lines).
..   Click path: Contacts app --> open a customer that has placed a webshop
..   order paid by a guarded provider --> chatter / Log note history.
..
.. cash_on_delivery-signal-queue-list.png
..   What: the Utánvét Ellenőr signals list view with a few rows in
..   different states, showing the green/red/grey state decorations and the
..   Retry button on a failed row.
..   Click path: Website app --> Configuration --> Utánvét Ellenőr signals.
..
.. cash_on_delivery-picking-cod-amount.png
..   What: an outgoing delivery transfer form for an order paid through a
..   carrier's "Payment on Delivery" method, with the read-only COD Amount
..   field visible next to the Carrier field.
..   Click path: Inventory app --> Transfers --> open the outgoing delivery
..   for a COD sale order (after it has produced a shipping label).

**Cash on delivery (COD)** lets a webshop customer pay for an order in cash
(or by card) at the moment the parcel is handed over, instead of paying
online at checkout. Because a single sales order can ship in several
separate shipments — a multi-step warehouse route, an out-of-stock
backorder, a partial delivery — the amount to collect on *each* shipment
must be computed individually, and the risk of an unreliable COD customer
must be screened *before* the order is confirmed. eYssen covers both problems with
two focused modules: one computes the correct COD amount per shipment for
the carrier integrations, the other gates cash-on-delivery-style payment
methods at checkout against the shared **utanvet-ellenor.hu** fraud
database.

.. seealso::
   - :doc:`delivery_payment` — how payment providers are filtered per
     delivery method, and the COD checkout experience
   - :doc:`setup_configuration/gls`, :doc:`setup_configuration/foxpost` and
     :doc:`setup_configuration/mpl` — the carrier integrations that call
     the COD computation
   - :doc:`payment_gated_delivery` — holding deliveries until an order is
     paid

.. image:: cash_on_delivery/cash_on_delivery-checkout-payment-methods.png
   :alt: Website checkout payment step showing the Payment on Delivery option

Key features
============

- **Dynamic, per-delivery COD computation.** Each outgoing delivery gets its
  own COD amount, proportionate to the goods it actually contains, so
  partial and multi-step shipments never over- or under-charge the
  customer.
- **One computation shared by every carrier.** GLS, Foxpost and MPL each
  call the same underlying method when building their shipping label
  request, so the business rule lives in a single place instead of being
  duplicated per carrier.
- **Shared fraud-database check at checkout.** Payment providers can be
  individually flagged to be hidden from customers with a poor reputation
  on the Utánvét Ellenőr shared database, before the order is even placed.
- **Fail-open by default.** If the fraud-check API is unreachable, checkout
  is not blocked unless an administrator explicitly opts into the stricter
  policy.
- **Closed-loop reporting.** Successful and failed/cancelled deliveries are
  reported back to Utánvét Ellenőr asynchronously, so the shared database
  stays accurate for every merchant using it.

How the COD amount is computed
==============================

The ``eyssen_delivery_cod`` module adds a read-only ``cod_amount`` field to
:guilabel:`Transfers` (``stock.picking``) and a single method,
``_compute_dynamic_cod()``, that carrier integrations call while preparing a
shipment. It is not triggered automatically — GLS (``eyssen_delivery_gls``),
Foxpost (``eyssen_delivery_foxpost``) and MPL (``eyssen_delivery_mpl``) each
depend on ``eyssen_delivery_cod`` and call the method with their own
"Payment on Delivery" provider's XML ID when they build the shipping label
request for a picking.

.. image:: cash_on_delivery/cash_on_delivery-picking-cod-amount.png
   :alt: Outgoing delivery form showing the read-only COD Amount field

The method only computes an amount when the sales order's **last payment
transaction** is on that carrier's own "Payment on Delivery" provider; for
any other payment method it returns ``0.0`` and logs a warning. When it does
apply, the amount is built up as follows:

#. **Goods value of this delivery** — for every stock move in the picking
   that is linked to a sale order line, the line's unit price
   (``price_total`` ÷ ``product_uom_qty``, i.e. tax included) is multiplied
   by the quantity actually shipped in this picking.
#. **Goods value already shipped** — the same calculation is repeated for
   every *other* picking on the same order that already has a
   ``cod_amount`` set, i.e. deliveries that shipped earlier.
#. **Service lines** — order lines that are not stockable/consumable
   products and are not a down payment (for example shipping surcharges)
   are added to the cumulative total in full.
#. **Invoiced down payments** — down-payment order lines with an invoiced
   quantity are computed with taxes (via ``tax_id.compute_all``) and
   subtracted from the cumulative total.
#. **Amount already collected** — the sum of ``cod_amount`` on the sibling
   pickings that already shipped is subtracted from the cumulative target
   to get the amount still owed.
#. **Order total cap** — the result is capped so the sum of everything
   collected across all deliveries of the order never exceeds the order's
   ``amount_total``.

.. note::
   Because the cumulative target already includes service lines from the
   first computation onward, and every later delivery subtracts what earlier
   deliveries already collected, in practice the customer only pays for
   service lines once — together with the first delivery that ships.

The resulting amount is stored on ``stock.picking.cod_amount`` and shown,
read-only, on the delivery form right after the :guilabel:`Carrier` field
(hidden while it is zero). Each carrier module then uses that amount to fill
in the "collect on delivery" field of its own label request. Some carriers
additionally enforce their own hard ceiling on top of this computation — for
example Foxpost refuses to generate a label above 150 000 HUF.

.. important::
   ``eyssen_delivery_cod`` has no configuration screen of its own. It only
   becomes active once a carrier module that depends on it (GLS, Foxpost or
   MPL) is installed and the customer pays through that carrier's own
   "Payment on Delivery" method.

The Utánvét Ellenőr fraud check at checkout
===========================================

The ``utanvetellenor`` module integrates the `utanvet-ellenor.hu
<https://utanvet-ellenor.hu>`_ shared customer-reputation database, which
several Hungarian webshops feed with delivery outcomes. It plugs into two
points of the order lifecycle: filtering payment methods at checkout, and
reporting the delivery outcome back afterwards.

Filtering payment providers at checkout
---------------------------------------

The module extends the payment provider's compatible-providers lookup so
that any :guilabel:`Payment Provider` with :guilabel:`Utánvét Ellenőr Check`
enabled is only offered to customers whose reputation clears the configured
threshold.

.. image:: cash_on_delivery/cash_on_delivery-provider-check-toggle.png
   :alt: Payment provider form with the Utánvét Ellenőr Check option

- If **no** enabled provider has the check turned on, the module does
  nothing — there is no performance cost for shops that don't use it.
- Before calling the API, the module verifies that the checkout partner is
  either the current user's own partner, a contact in the same commercial
  entity, or that the caller is an internal user — this stops the endpoint
  from being used to probe the reputation of an arbitrary customer.
- The customer's e-mail, phone (normalised to E.164 through
  ``phone_validation`` when installed), country code, ZIP code and street
  address are sent to the ``/request`` endpoint together with the
  configured reputation threshold; name, payment data and tax numbers are
  **never** sent.
- The verdict is cached in memory per worker process for five minutes,
  keyed on company, partner, the partner's ``write_date``, the threshold and
  the mode — so any local edit to the partner's contact details immediately
  invalidates the cached verdict.
- The API's HTTP response is translated into a decision: a ``blocked``
  result, a ``204`` (temporary/non-existent mailbox), a missing e-mail, or a
  ``404`` (unknown customer, always allowed) are all handled explicitly.
  ``401`` (bad keys) and ``402`` (quota exhausted) are logged but never
  block checkout by themselves — only genuine transport failures (timeout,
  connection error, 5xx) and quota errors are subject to the fallback
  policy below.

.. important::
   When the customer is blocked, or a transport/quota error occurs while
   :guilabel:`Fallback on API Error` is set to :guilabel:`Block payment`,
   every provider that has :guilabel:`Utánvét Ellenőr Check` enabled is
   removed from the list of payment methods offered at checkout. Providers
   that don't opt in — for example a card payment method — are never
   affected.

Every API call that results in a block or an error can be logged as an
internal note on the customer, controlled by the :guilabel:`Chatter
Verbosity` setting:

.. image:: cash_on_delivery/cash_on_delivery-partner-chatter-log.png
   :alt: Customer chatter with an Utánvét Ellenőr request log entry

The note records the mode, threshold, HTTP status, the API's good/bad
counts, the numeric reputation and the verbatim reason — never the API
keys.

Reporting the outcome back
--------------------------

Once an outgoing delivery linked to a sale order paid through a guarded
provider is validated or cancelled, the module queues a signal so the
shared database learns the outcome:

- validating the transfer (``_action_done``) queues outcome ``1``
  (:guilabel:`Successful delivery (+1)`);
- cancelling the transfer (``action_cancel``) queues outcome ``-1``
  (:guilabel:`Failed / refused (-1)`).

A queue row is only created if the picking is outgoing, linked to a sale
order, and that order has a transaction in the ``done`` state on a provider
with :guilabel:`Utánvét Ellenőr Check` enabled. A database constraint
guarantees at most one row per picking and outcome, and a re-validated
picking can never queue a contradictory outcome once one has already been
sent.

.. image:: cash_on_delivery/cash_on_delivery-signal-queue-list.png
   :alt: Utánvét Ellenőr signals list with pending, sent and failed rows

The queued rows are visible under :menuselection:`Website --> Configuration
--> Utánvét Ellenőr signals`, colour-coded by :guilabel:`State`
(:guilabel:`Pending`, :guilabel:`Sent`, :guilabel:`Failed`). A scheduled
action, :guilabel:`Utánvét Ellenőr: send pending signals`, runs every 10
minutes and drains up to 100 due rows per run, retrying failed calls up to
three times with a backoff of 5 minutes, then 30 minutes, then 2 hours,
before marking a row :guilabel:`Failed`. An administrator can reset a failed
row with the :guilabel:`Retry` button to have the cron pick it up again.

Configuration
=============

``eyssen_delivery_cod`` needs no setup: install it as a dependency of a
carrier module and the COD computation runs automatically for orders paid
through that carrier's "Payment on Delivery" method.

To configure the Utánvét Ellenőr check:

#. Install ``utanvetellenor``.
#. Go to :menuselection:`Website --> Configuration --> Settings --> Shop -
   Checkout Process --> Utánvét Ellenőr` and set:

   - :guilabel:`Mode` — :guilabel:`Sandbox` or :guilabel:`Production`;
   - the matching public/private key pair for that mode;
   - :guilabel:`Reputation Threshold` — a value between ``-1.0`` and
     ``+1.0`` (default ``0.5``);
   - :guilabel:`Fallback on API Error` — :guilabel:`Allow payment` (default)
     or :guilabel:`Block payment`;
   - :guilabel:`API Timeout (s)` — the HTTP timeout used for every call
     (default ``5``);
   - :guilabel:`Chatter Verbosity` — :guilabel:`All API calls`,
     :guilabel:`Blocked customers and errors only` (default) or
     :guilabel:`Errors only`.

   .. image:: cash_on_delivery/cash_on_delivery-settings.png
      :alt: Utánvét Ellenőr settings under Shop - Checkout Process

#. On each payment provider that should be gated (typically a
   cash-on-delivery or bank-transfer method), open the
   :guilabel:`Configuration` tab, :guilabel:`Availability` group, and enable
   :guilabel:`Utánvét Ellenőr Check`.

.. important::
   The integration is a **joint-controller data sharing arrangement**: it
   sends the customer's e-mail, phone, postal code, country code and
   address line to a third party. Sign the Utánvét Ellenőr joint data
   controller agreement and update the shop's privacy policy before
   enabling the check in :guilabel:`Production` mode.

.. note::
   Sandbox and production API keys are stored in clear text on the company
   record; the password widget in :guilabel:`Settings` only masks the value
   on screen. Access to :guilabel:`Settings` is restricted to the
   :guilabel:`Administration / Settings` (``base.group_system``) group, and
   the same group is required to open the signal queue and to see the API
   keys — never lower that restriction. Use different key pairs for
   sandbox and production so a leaked test key cannot be replayed against
   the live database.

Usage
=====

#. A customer checks out on the website. If any offered payment provider
   has :guilabel:`Utánvét Ellenőr Check` enabled, the module looks up (or
   reuses the cached) reputation verdict for that customer and hides the
   guarded providers if the customer is blocked, or if the API failed and
   the fallback policy is set to :guilabel:`Block payment`. Other payment
   methods stay available either way.
#. The order is confirmed and the warehouse processes the delivery, in one
   shipment or several, depending on the route and stock availability.
#. When the carrier module (GLS, Foxpost or MPL) generates the shipping
   label for a picking paid through its own "Payment on Delivery" method,
   it calls ``_compute_dynamic_cod()`` to work out exactly how much to
   collect on *that* delivery, and stores it on the picking's
   :guilabel:`COD Amount` field.
#. Once the transfer is validated (delivered) or cancelled, a signal is
   queued automatically and sent to Utánvét Ellenőr by the scheduled action
   within about 10 minutes, so the shared reputation database reflects the
   real outcome for future checks — by this shop and by every other
   merchant using the service.

Scope and modules
=================

- ``eyssen_delivery_cod`` — computes the dynamic, per-delivery COD
  amount (partial shipments, service lines, down payments, order-total cap)
  shared by the carrier integrations.
- ``utanvetellenor`` — integrates the utanvet-ellenor.hu shared fraud
  database into checkout (payment-provider filtering) and post-fulfilment
  reporting (signal queue and retry cron).

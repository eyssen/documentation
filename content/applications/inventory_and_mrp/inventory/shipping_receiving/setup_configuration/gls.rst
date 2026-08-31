.. _inventory/shipping_receiving/gls:

===============
GLS integration
===============

*GLS* is one of the most widely used parcel carriers in Hungary, offering both home delivery and
pickup at a nationwide network of *parcel shops* (the GLS flavour of pickup points). The eYssen GLS
integration connects Odoo to the *MyGLS* API so a webshop can offer both delivery modes, let the
shopper choose a parcel shop on the official GLS map at checkout, print shipping labels straight
from delivery transfers, follow every parcel through the GLS tracking states, collect cash on
delivery (COD), and even turn parcels that bounce back to the sender into return orders (RMAs)
automatically.

The feature is delivered by the ``eyssen_delivery_gls`` module, with two optional extensions:
``rma_delivery_gls`` for return automation and ``eyssen_stock_multi_warehouse_delivery_gls`` for
warehouse-to-warehouse shipments.

.. seealso::
   - :doc:`third_party_shipper`
   - :doc:`../cash_on_delivery`
   - :doc:`../delivery_payment`
   - :doc:`../delivery_status_and_dates`
   - :doc:`../payment_gated_delivery`

Account setup
=============

The integration talks to the GLS *MyGLS* system, so a MyGLS business contract is required. GLS
provides the following, which are entered on the shipping method in Odoo:

- a **client number** identifying the contract;
- an **API user** and **API password** for the production system;
- a separate **test API user** and **test API password** for the GLS test environment (the
  shipping method form requires all credential fields to be filled).

Request the test credentials as well when onboarding: they allow label generation and tracking to
be tried end to end against the separate GLS test system before going live.

.. note::
   Odoo never transmits the MyGLS password in clear text — every API call authenticates with a
   SHA-512 digest of the password, as required by the MyGLS API convention.

Shipping method configuration
=============================

Installing ``eyssen_delivery_gls`` creates two ready-made shipping methods, :guilabel:`GLS Parcel
Shop` and :guilabel:`GLS Home delivery`. To configure them (or to create additional GLS methods),
go to :menuselection:`Inventory app --> Configuration --> Delivery Methods` and open the method.
With :guilabel:`Provider` set to :guilabel:`GLS`, two extra tabs appear on the form:
:guilabel:`Pricing` and :guilabel:`GLS Configuration`.

For the generic fields shared by all carriers — :guilabel:`Delivery Product`, availability
countries, publishing the method on the website — refer to :doc:`third_party_shipper`. Remember to
**publish** each method that should be offered in the webshop.

Credentials
-----------

On the :guilabel:`GLS Configuration` tab, fill in:

- :guilabel:`API User` and :guilabel:`API Password`: the production MyGLS credentials.
- :guilabel:`Test API User` and :guilabel:`Test API Password`: the credentials for the GLS test
  system.
- :guilabel:`Client number`: the MyGLS client number.

The standard :guilabel:`Environment` toggle of the shipping method decides everything at once:
in the *Test* environment, Odoo calls the GLS test API with the test credential pair; in the
*Production* environment, it calls the live API with the production pair. No other switch is
needed when going live.

.. note::
   The credential fields are only visible to users with :guilabel:`Administration / Settings`
   access. If the applicable credentials are left empty, validating a GLS delivery does **not**
   fail: the transfer is validated normally and a chatter note records that no GLS parcel was
   created, so an unconfigured method never blocks the warehouse.

Delivery types
--------------

The :guilabel:`Delivery type` field on the :guilabel:`GLS Configuration` tab selects how the
parcel reaches the customer:

.. list-table::
   :header-rows: 1
   :widths: 24 38 38

   * - Topic
     - :guilabel:`Parcel Shop` (default)
     - :guilabel:`Home delivery`
   * - Where the parcel goes
     - A GLS parcel shop chosen by the shopper
     - The customer's own address
   * - Checkout behavior
     - The GLS map opens to pick a shop
     - Behaves like any normal carrier
   * - Shipping address
     - Optionally replaced by an auto-created parcel-shop address
     - The customer's delivery address
   * - Label requirement
     - A parcel shop must be selected before a label can be generated
     - No extra requirement

For parcel-shop methods, the extra option :guilabel:`Create Delivery Address for PS` controls what
happens to the order's shipping address once a shop is chosen:

- **Enabled**: a separate delivery address named after the shop (its name and identifier) is
  created under the customer, carrying the shop's street, ZIP, city and country, and it becomes the
  order's shipping address. Auto-created shop addresses are hidden from the checkout address
  chooser and cleaned up automatically when they are no longer used by any order.
- **Disabled** (default): the shipping address stays the customer's own; only the parcel shop
  identifier is stored on the order and sent to GLS with the label.

Pricing
-------

The :guilabel:`Pricing` tab offers two pricing modes:

- **Banded pricing**: add one or more rows to the :guilabel:`Pricing Rules` list. Each rule matches
  on the order's weight, volume, price or quantity; the rules are evaluated in sequence and the
  **first matching rule** sets the shipping price (converted to the order's currency when the
  company currency differs). If no rule matches — for example, the cart is heavier than the last
  band — the method remains listed at checkout but cannot be selected: Odoo shows *Not available
  for current order*.
- **Fixed price**: when no pricing rule is defined, the shipping price is the sales price of the
  method's :guilabel:`Delivery Product`, resolved through the order's pricelist; the
  :guilabel:`Fixed Price` field edits that product's base sales price, and pricelist rules on the
  delivery product override it per pricelist (and therefore per website).

.. example::
   Two rules — *weight <= 2 kg → 990 Ft* and *weight <= 10 kg → 1 590 Ft* — charge 990 Ft for a
   1.5 kg cart and 1 590 Ft for a 7 kg cart, and show the GLS method as *Not available for
   current order* for a 25 kg cart.

The core carrier option :guilabel:`Free if order amount is above` keeps working on top of both
modes: when it applies, the shipping price drops to zero while the real cost is still recorded on
the order.

Cash on delivery
----------------

Installing the module also creates the GLS-specific :guilabel:`Payment on Delivery` payment
provider — a COD-style provider that lets the shopper place the order online and pay the courier
or the parcel shop at handover; the sales order itself is still confirmed in the back office (see
:doc:`../delivery_payment`). It is created disabled, like any payment provider, and must be
enabled and published before use.

Both shipped GLS methods pre-list this provider as the only entry of their :guilabel:`Enabled
payment acquirers` list, so out of the box a GLS delivery offers *only* COD at the payment step —
as long as no other carrier's COD provider is enabled: the whitelist reliably restricts online
providers, while COD providers are validated on their own track (shipping-address compatibility).
Add the shop's card or wire-transfer providers to each method to offer more. How the per-carrier
payment filtering and the COD checkout experience work is described in
:doc:`../delivery_payment`; how the exact amount to collect for each shipment is computed
(partial shipments, down payments, order-total cap) is described in :doc:`../cash_on_delivery`.
To hold back deliveries until payment is actually received, see :doc:`../payment_gated_delivery`.

.. note::
   The :guilabel:`Payment on Delivery` option only appears at checkout when at least one GLS
   method is published on the website and the cart contains physical products.

FlexDeliveryService and options
-------------------------------

- :guilabel:`FlexDeliveryService`: when enabled, parcels are announced to GLS with the recipient's
  e-mail address, so GLS notifies the customer about the delivery and lets them interact with it
  (GLS *FDS* service). The :guilabel:`FDS Countries` list restricts the service to selected
  destination countries; leave it empty to apply it everywhere.
- A :guilabel:`GLS Box` package type (carrier :guilabel:`GLS`) is shipped under
  :menuselection:`Inventory app --> Configuration --> Package Types`, ready to be used when
  packing GLS parcels.

Website checkout: choosing a parcel shop
========================================

When the shopper selects a GLS parcel-shop method at checkout, the **official GLS map** opens
automatically in a dialog: it shows every GLS parcel shop in Hungary with its own search and map
controls. After the shopper picks a shop, the dialog closes and the selection is stored on the
order. Depending on :guilabel:`Create Delivery Address for PS`, the shipping address is either
switched to the auto-created shop address or left untouched.

Switching to another delivery method reverts the shipping address to the customer's own address
and removes the now-unused shop address; selecting a different shop replaces the previous one the
same way.

.. important::
   Choosing a shop is **not enforced** at checkout: a shopper can close the map without picking
   one and still place the order. The safety net is at fulfilment time — generating the label for
   such an order stops with the message *"Please select a GLS parcel shop on the sales order or
   transfer before validating the delivery."*, and staff fill in the missing shop before shipping.

Back-office users can view and change the chosen shop as well: on the sales order (and on the
linked transfer), a :guilabel:`GLS parcel shop` field appears next to the delivery address for
parcel-shop methods, together with a :guilabel:`Select on map` button that opens the same GLS map
inside the backend. The identifier can also be typed manually (for example `HU-123456`). The field
locks as soon as a label exists or the order is done or cancelled, so the shop can no longer
diverge from what is printed on the label.

Shipping labels
===============

Labels are generated from the outgoing transfer, either automatically through the standard carrier
flow when the transfer is validated, or manually with the :guilabel:`Print GLS Label` button on
the transfer form.

- One GLS shipment is registered per transfer. The :guilabel:`GLS parcel count` equals the number
  of packages on the transfer (or 1 when the goods are not packed), so multi-package transfers
  should use :guilabel:`Put in Pack` once per physical parcel *before* printing.
- GLS requires complete contact data: the company's phone number and e-mail, and the recipient's
  phone number and e-mail must all be set, otherwise label generation stops with an explicit
  message naming what is missing.
- On success, the transfer stores the :guilabel:`GLS parcel ID` and the :guilabel:`GLS parcel
  number` (one number per package, comma-separated), the label PDF is saved in the :guilabel:`GLS
  label` field and attached to the chatter named after the parcel number, and each package on the
  transfer receives its own parcel number — the packages list gains :guilabel:`GLS parcel number`
  and :guilabel:`Parcel state` columns.
- When the order was placed with :guilabel:`Payment on Delivery`, the amount to collect is
  computed for the outgoing transfer at label time and sent to GLS together with the label
  request — one amount covers all packages of the transfer (see :doc:`../cash_on_delivery`).

.. important::
   **Re-printing creates a new parcel.** The :guilabel:`Print GLS Label` button disappears once a
   label exists, because clicking it again does not re-download the existing label — it clears the
   stored parcel data and registers a **brand-new parcel** with GLS, while the previously created
   parcel stays live in the GLS system (there is no cancellation call). A second, always-visible
   copy of the button is available in developer mode for deliberate regeneration; use it only when
   the original parcel is really not going to be shipped.

Tracking and statuses
=====================

The module ships a catalogue of 90 GLS parcel states, editable under :menuselection:`Inventory app
--> Configuration --> GLS Parcel States` (visible to administrators). Each state has a code, a
translatable name, and a :guilabel:`Delivered State` checkbox; the two "parcel has been delivered"
states (codes `05` and `92`) come pre-flagged as delivered.

Tracking is synchronised automatically by two scheduled actions that run every three hours: one
polls every in-flight labelled transfer, the other rotates through labelled packages (a limited
batch per run, each package at most once per hour by default). The latest status text, the mapped
state and the status date are stored on the transfer and on the matching package. Users can also
refresh on demand with the :guilabel:`Update GLS Status` button in the transfer header, or the
inline :guilabel:`Update` arrow next to the :guilabel:`Parcel state`.

Two automations build on the state catalogue:

- **Auto-validation**: on the operation type (:menuselection:`Inventory app --> Configuration -->
  Operations Types`), tick :guilabel:`Validate Picking on Delivery` and pick the states in
  :guilabel:`Validate on GLS States`. A transfer is then validated automatically as soon as its
  parcel — or, for packed transfers, **all** of its packages — reaches one of the chosen states.
  Packed transfers are validated without creating a backorder; an unpacked transfer is only
  auto-validated when it can be validated outright (a partial unpacked transfer is left open for
  manual processing). This suits flows where the transfer is kept open until GLS confirms the
  handover or the delivery.
- **Delivered date**: when a parcel reaches a state flagged :guilabel:`Delivered State`, the date
  the customer actually received the goods is stamped on the transfer. This feeds the delivery
  status and dates shown on sales orders and the customer portal — see
  :doc:`../delivery_status_and_dates`.

.. note::
   The raw status text returned by GLS is in Hungarian regardless of the user's language; the
   mapped state name from the catalogue is translatable and is the one to rely on in multilingual
   databases.

Returns: automatic RMA on return-to-sender
==========================================

The optional ``rma_delivery_gls`` module automates the return side of GLS shipping. It is **not**
installed automatically together with the other modules — auto-creating return orders has
financial consequences, so an administrator must install it deliberately per database.

Automatic RMA when a parcel bounces
-----------------------------------

GLS reports parcels that the customer never picked up with the state "The parcel has been returned
to sender." (codes `23` and `40`). The module pre-flags these two states in its data; the flag is
a technical field on the state record and is not shown in the :guilabel:`GLS Parcel States` list —
adjust it in developer mode if a different state set is needed. The module also extends the
tracking cron to keep polling recently shipped parcels *after* the transfer is done, until they
reach a delivered or returned state.

When an outgoing customer delivery reaches a flagged state, **one** auto-approved, return-only
:abbr:`RMA (Return Merchandise Authorization)` is created on its sales order, covering all
delivered returnable lines, and the order is flagged as needing a refund. The automation is
best-effort and safe: a failure never breaks the tracking update — it is logged and escalated as a
to-do activity (:guilabel:`Automatic non-pickup RMA failed`) on the salesperson, and the next
status update retries cleanly. Repeated status updates never create duplicate RMAs.

GLS return labels
-----------------

For an approved return RMA, the module generates a GLS **return label**: the customer's address is
the pickup side and the company's address the destination. The RMA's :guilabel:`Return Method`
selects the GLS return service:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - :guilabel:`Return Method`
     - Behavior
   * - :guilabel:`Parcel Locker`
     - The customer drops the parcel in a GLS locker; when GLS issues a locker PIN for the
       parcel, it is stored as :guilabel:`GLS Locker PIN` next to the label.
   * - :guilabel:`Parcel Shop`
     - The customer hands the parcel in at any GLS parcel shop.
   * - :guilabel:`Collect from Customer`
     - A GLS courier collects the parcel at the customer's address.

The result is stored on the RMA's :guilabel:`GLS Return` tab: the :guilabel:`GLS Return Parcel`
number, the :guilabel:`GLS Locker PIN` (locker returns, when GLS issues one), the downloadable
:guilabel:`GLS Return Label` PDF and the :guilabel:`GLS Return Status`. A return label is
generated automatically when a customer-initiated (webshop portal) B2C return is approved; for
RMAs created in the backend, RMA managers generate the label with the :guilabel:`Generate GLS
Return Label` button. Once a return parcel exists, re-generation is skipped, so no duplicate
parcels are registered. Searching RMAs by a scanned return parcel number finds the record
directly.

:doc:`Withdrawal declarations <../../../../sales/withdrawal>` are excluded — they are handled
manually, and no GLS return label can be generated for them.

A daily scheduled action, :guilabel:`GLS: Update Return Parcel Tracking`, follows the return
parcels until they reach a delivered state, updating the :guilabel:`GLS Return Status` on each
RMA.

Multi-warehouse transfers
=========================

The optional ``eyssen_stock_multi_warehouse_delivery_gls`` module adapts the GLS carrier to the
eYssen multi-warehouse internal-transfer flow, for companies that ship goods **between their own
warehouses** with GLS:

- Labels printed for a transfer step of an internal transfer are addressed warehouse-to-warehouse:
  the source warehouse is the sender and the destination warehouse the recipient (each shown as
  the company name together with the warehouse address), instead of company-to-customer.
- When a transfer chain recreates the packages for its next step, the GLS parcel identity (parcel
  ID and parcel number) is copied along, so tracking follows the physical parcel across the legs
  of the transfer — including intercompany legs.
- The internal transfers list can be searched by GLS parcel number through its :guilabel:`Tracking
  Number` search field.

Install this bridge only when both the multi-warehouse module and the GLS carrier are in use; it
has no configuration of its own.

Configuration
=============

A complete GLS rollout touches the following settings:

#. **Modules**: install ``eyssen_delivery_gls``; add ``rma_delivery_gls`` (return automation — a
   deliberate, per-database decision) and ``eyssen_stock_multi_warehouse_delivery_gls``
   (warehouse-to-warehouse shipping) only where needed.
#. **Shipping methods** (:menuselection:`Inventory app --> Configuration --> Delivery Methods`):
   on :guilabel:`GLS Parcel Shop` and :guilabel:`GLS Home delivery`, fill the :guilabel:`GLS
   Configuration` tab (credentials, :guilabel:`Client number`, :guilabel:`Delivery type`,
   :guilabel:`Create Delivery Address for PS`, :guilabel:`FlexDeliveryService`), set the
   :guilabel:`Environment`, configure the :guilabel:`Pricing` tab, and publish the methods on the
   website.
#. **Payments**: enable and publish the :guilabel:`Payment on Delivery` provider; review each GLS
   method's :guilabel:`Enabled payment acquirers` list and add the shop's other providers (see
   :doc:`../delivery_payment`).
#. **Operation types** (:menuselection:`Inventory app --> Configuration --> Operations Types`):
   optionally enable :guilabel:`Validate Picking on Delivery` and select the :guilabel:`Validate
   on GLS States` for the outgoing operation type.
#. **State catalogue** (:menuselection:`Inventory app --> Configuration --> GLS Parcel States`):
   review the :guilabel:`Delivered State` flags (codes `05` and `92` by default). With
   ``rma_delivery_gls``, the non-pickup RMA trigger flags (codes `23` and `40` by default) are
   technical fields on the state records, not shown in the list — adjust them in developer mode.
#. **Scheduled actions**: the transfer- and package-tracking crons run every three hours; the
   return-tracking cron (with ``rma_delivery_gls``) runs daily.
#. **System parameters** (:menuselection:`Settings --> Technical --> System Parameters`) tune the
   polling volume. None of these parameters exists by default — the built-in default applies
   until the parameter is created manually with a different value:

   .. list-table::
      :header-rows: 1
      :widths: 45 12 43

      * - Parameter
        - Default
        - Purpose
      * - ``gls_tracking_check_interval_minutes``
        - 60
        - Minimum minutes between two checks of the same package by the package-tracking cron.
      * - ``gls_done_tracking_batch_size``
        - 25
        - Maximum done transfers re-polled per run once ``rma_delivery_gls`` enables
          post-handover polling (60-day window).
      * - ``gls_return_tracking_check_interval_minutes``
        - 720
        - Minimum minutes between two checks of the same return parcel.
      * - ``gls_return_tracking_batch_size``
        - 100
        - Maximum return parcels polled per run of the daily return-tracking cron.

.. note::
   All GLS credential fields, the state catalogue and the parcel-state menu are restricted to the
   :guilabel:`Administration / Settings` group; regular warehouse users see the tracking data but
   cannot change the configuration.

Usage
=====

A typical GLS order runs end to end as follows:

#. The shopper selects :guilabel:`GLS Parcel Shop` (or :guilabel:`GLS Home delivery`) at checkout.
   For a parcel-shop method, the GLS map opens and the shopper picks a shop; the choice is stored
   on the order.
#. The shopper pays online with any provider enabled for the method, or places the order with
   :guilabel:`Payment on Delivery` to pay at handover — in that case, the sales order is
   confirmed in the back office (see :doc:`../delivery_payment`).
#. The warehouse prepares the delivery, using :guilabel:`Put in Pack` once per physical parcel
   when shipping more than one.
#. Validating the transfer (or clicking :guilabel:`Print GLS Label`) registers the shipment with
   GLS: parcel numbers are assigned to the packages, the label PDF is stored on the transfer and
   attached in the chatter, and any COD amount is included automatically.
#. The parcels are handed to GLS. The scheduled actions follow every parcel through the GLS
   states; the current :guilabel:`Parcel state` is visible on the transfer and on each package,
   and can be refreshed on demand with :guilabel:`Update GLS Status`.
#. When GLS reports the parcel delivered, the customer receipt date is stamped on the transfer
   (see :doc:`../delivery_status_and_dates`) and, if configured on the operation type, the
   transfer validates itself.
#. If the customer never picks the parcel up and GLS returns it to the sender, an auto-approved
   return RMA appears on the sales order (with ``rma_delivery_gls``), ready for the refund
   decision.
#. For returns initiated by the customer, the RMA produces a GLS return label — with a locker PIN,
   a parcel-shop drop-off or a courier collection — and the return parcel is tracked daily until
   it arrives back.

Scope and modules
=================

- ``eyssen_delivery_gls`` — the GLS carrier itself: parcel-shop and home-delivery shipping
  methods, the checkout and backend map picker, label generation, the 90-state tracking catalogue
  with auto-validation, the :guilabel:`Payment on Delivery` COD provider and the return-label API.
- ``rma_delivery_gls`` — return automation on top of the carrier: automatic non-pickup RMAs for
  returned-to-sender parcels, GLS return labels (locker PIN, parcel shop, courier collection) and
  daily return-parcel tracking.
- ``eyssen_stock_multi_warehouse_delivery_gls`` — GLS support for internal transfers between
  warehouses: warehouse-to-warehouse label addresses, parcel-number continuity across transfer
  legs and tracking-number search.

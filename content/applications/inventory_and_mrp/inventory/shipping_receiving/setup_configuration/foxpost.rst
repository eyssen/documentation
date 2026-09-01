.. _inventory/shipping_receiving/foxpost:

===================
Foxpost integration
===================

Foxpost is a Hungarian parcel carrier best known for its nationwide network of parcel machines
(lockers). The **Delivery Foxpost** module (``eyssen_delivery_foxpost``) connects Odoo to the
Foxpost web API: it adds a :guilabel:`Foxpost` shipping provider with a *parcel machine (APM)* mode
and a *home delivery* mode, registers each parcel and downloads its PDF label when the delivery
order is validated, keeps the parcel status in sync with Foxpost, and ships a dedicated *FoxPost
COD* cash on delivery (COD) payment provider capped at 150 000 HUF. On the webshop, customers pick
their parcel machine on the official Foxpost map without leaving checkout.

To configure the integration, complete these steps:

#. Get the :ref:`Foxpost API credentials <inventory/shipping_receiving/foxpost-account>`.
#. :ref:`Set up the shipping method(s) in Odoo <inventory/shipping_receiving/foxpost-method>`.
#. Optionally, enable the :ref:`FoxPost COD payment provider
   <inventory/shipping_receiving/foxpost-cod>`.

.. seealso::
   - :doc:`third_party_shipper`
   - :doc:`../cash_on_delivery`
   - :doc:`../delivery_payment`
   - :doc:`../delivery_status_and_dates`
   - :doc:`../payment_gated_delivery`

.. _inventory/shipping_receiving/foxpost-account:

Account setup
=============

The connector talks to the Foxpost *web API*, which requires three credentials issued by Foxpost
under the company's carrier contract: an API user, an API password, and an API key. Foxpost
operates a separate **test** system and **production** system, so request access to both from
Foxpost: the test system allows the full flow (parcel registration, labels, tracking) to be
rehearsed without real parcels being created in the production network.

.. important::
   Credentials are environment-specific: use each set only against the environment it was issued
   for. Which environment Odoo calls is decided per shipping method by its
   :guilabel:`Environment` button (see below) — always double-check that the credentials entered on
   the method match the selected environment.

.. _inventory/shipping_receiving/foxpost-method:

Shipping method configuration
=============================

Installing the module creates two ready-made shipping methods: *Foxpost Parcelmachine* (parcel
machine mode) and *Foxpost Home delivery* (home delivery mode). Both install **unpublished**, with
a zero price and empty credentials — they are templates to complete rather than working methods.

To configure them (or to create additional ones), go to :menuselection:`Inventory app -->
Configuration --> Delivery Methods` and open the method. Selecting :guilabel:`Foxpost` in the
:guilabel:`Provider` field reveals two Foxpost-specific tabs on the form: :guilabel:`Foxpost
Configuration` and :guilabel:`Pricing`.

For the fields shared by every third-party carrier, such as :guilabel:`Delivery Product` or
:guilabel:`Countries`, refer to the :doc:`third-party carrier <third_party_shipper>` documentation.

.. note::
   To have Odoo register parcels and fetch labels, keep the :guilabel:`Integration Level` at
   :guilabel:`Get Rate and Create Shipment`. With :guilabel:`Get Rate`, the method only computes
   prices at checkout and never contacts Foxpost at shipping time.

Credentials
-----------

On the :guilabel:`Foxpost Configuration` tab, fill in the three credentials from the
:ref:`account setup <inventory/shipping_receiving/foxpost-account>`:

- :guilabel:`API User` and :guilabel:`API Password`: the HTTP authentication pair for the Foxpost
  web API.
- :guilabel:`API Key`: the additional key Foxpost requires on every API call.

These fields — together with the :guilabel:`Delivery type` field described below — are only visible
to users in the *Administration / Settings* group; other users see the shipping method form without
them.

The :guilabel:`Environment` smart button in the top-right corner of the form toggles between
:guilabel:`Test Environment` and :guilabel:`Production Environment`. In test mode, every call goes
to Foxpost's test API; switch the method to production once the flow has been verified end to end.

Delivery types
--------------

The :guilabel:`Delivery type` field on the :guilabel:`Foxpost Configuration` tab selects one of two
operating modes. A single shipping method always works in exactly one mode; to offer both, publish
two methods (which is what the two preinstalled records provide).

.. list-table::
   :header-rows: 1
   :widths: 24 38 38

   * - Mode
     - :guilabel:`Parcelmachine` (APM)
     - :guilabel:`Home delivery`
   * - Destination
     - A Foxpost parcel machine chosen by the customer.
     - The customer's shipping address.
   * - Parcel machine selection
     - Map modal at website checkout; :guilabel:`Select on map` button in the backend.
     - Not applicable.
   * - Required before validating the delivery
     - Parcel machine ID and a recipient phone number.
     - Complete shipping address and a recipient phone number.
   * - Preinstalled method
     - *Foxpost Parcelmachine*
     - *Foxpost Home delivery*

The :guilabel:`Is web` field (:guilabel:`Visible on foxpost.hu` or :guilabel:`Not visible on
foxpost.hu`) is meant to control whether the parcel is flagged as visible on foxpost.hu when it is
registered. In the current version, every parcel is registered as visible regardless of this
setting, so keep the default :guilabel:`Visible on foxpost.hu`.

.. note::
   The recipient phone number is mandatory for every Foxpost shipment: the mobile number is used
   when set, the landline otherwise, and validating a delivery for a contact without any phone
   number fails with a blocking message. Foxpost uses it to notify the customer about the parcel.

Pricing
-------

The :guilabel:`Pricing` tab supports two pricing strategies:

- **Fixed price**: when no pricing rule is defined, the shipping price is the sales price of the
  method's :guilabel:`Delivery Product`, resolved through the order's pricelist. The
  :guilabel:`Fixed Price` field edits that product's base sales price, and pricelist rules on the
  delivery product override it per pricelist.
- **Banded rules**: adding one or more :guilabel:`Pricing Rules` switches the method to banded
  pricing by weight, volume, weight × volume, price, or quantity. Rules are evaluated in sequence
  order and the **first** matching rule wins. When no rule matches (for example, the cart is
  heavier than the largest weight band), the method stays visible at checkout but is greyed out and
  cannot be selected — the message *Not available for current order* is shown in place of the
  price.

Prices defined in the company currency are converted to the order's pricelist currency
automatically, and the standard :guilabel:`Free if order amount is above` option works on top of
either strategy.

.. example::
   Two rules — *weight ≤ 2 kg → 990 Ft* and *weight ≤ 5 kg → 1 990 Ft* — charge 990 Ft for a
   1.5 kg cart and 1 990 Ft for a 4 kg cart. A 10 kg cart matches neither band, so the Foxpost
   method is greyed out and cannot be selected for that cart.

.. _inventory/shipping_receiving/foxpost-cod:

Cash on delivery
----------------

The module ships a payment provider named :guilabel:`FoxPost COD, with credit card at parcelmachine
or at delivery`, letting the customer pay in cash or by card when picking up the parcel. Like every
payment provider, it installs disabled: enable and publish it under :menuselection:`Website -->
Configuration --> eCommerce: Payment Providers` to offer it at checkout.

The provider only appears on the payment step when a published Foxpost shipping method serves the
website and the cart contains physical goods, and its :guilabel:`Maximum Amount` is preset to
`150000` — the connector does not support COD parcels above 150 000 HUF — so larger orders never
see the option. The same ceiling is enforced a second time at shipping: generating a label whose
COD amount exceeds the cap is blocked with the message *"Maximum cash on delivery amount is
150.000,- HUF"*.

After a COD order is placed, the customer sees the confirmation message *"Your order has been
confirmed. Please pay upon delivery."* instead of wire-transfer instructions. This is
customer-facing copy only: the pending COD payment does not confirm the sales order — confirming it
(and creating the delivery) remains a back-office step. The amount to collect is computed
dynamically per outgoing delivery (transfer) when the shipping label is generated — one amount
covers the whole delivery, with partial shipments, service lines and down payments taken into
account.

.. seealso::
   - How the per-delivery COD amount is computed, and the optional fraud screening of COD
     customers: :doc:`../cash_on_delivery`
   - How payment methods are filtered per shipping method, and the COD checkout and confirmation
     experience: :doc:`../delivery_payment`

.. important::
   Both preinstalled Foxpost methods list **only** the FoxPost COD provider in their
   :guilabel:`Enabled payment acquirers` whitelist. Out of the box, a customer choosing Foxpost can
   therefore *only* pay on delivery — as long as no other carrier's COD provider is enabled, since
   COD providers are validated on their own track (see :doc:`../delivery_payment`). Add the shop's
   card and wire-transfer providers to each Foxpost method's :guilabel:`Payment Providers` tab to
   offer them as well.

Website checkout: choosing a parcel machine
===========================================

When the customer selects a Foxpost parcel machine method on the delivery step of the website
checkout, a full-screen window titled *Válasszon Foxpost csomagpontot* opens with the official
Foxpost *apt-finder* map — the same searchable map and list customers know from foxpost.hu.
Choosing a machine closes the window, saves the machine on the order, and displays the choice under
the selected delivery method as *Választott csomagpont:* followed by the machine's name. Clicking
the Foxpost method again reopens the map, so the customer can change their pick any time before
placing the order.

If the shipping method restricts :guilabel:`Countries`, the chosen machine is validated against
that list: a parcel machine located in a country the method does not serve is refused.

.. note::
   Closing the map without choosing a machine does **not** block the checkout — the customer can
   still place the order. The missing parcel machine is caught later, when the warehouse validates
   the delivery: validation is refused with the message *"Please select a Foxpost parcel machine
   (APM ID) on the sales order or transfer before validating the delivery."*, and staff can pick
   the machine on the order or transfer at that point (see below).

.. note::
   The map window texts are currently displayed in Hungarian regardless of the website language.

When the selected carrier is a Foxpost parcel machine method, both the sales order form and the
transfer form show a :guilabel:`Foxpost parcel machine` field with a :guilabel:`Select on map`
button. The button opens the :guilabel:`Select Foxpost parcel machine` dialog with the same Foxpost
map used at checkout; alternatively, the machine's operator ID (e.g. `hu472`) can be typed in
directly. The order and all of its transfers share one parcel machine — editing it on the transfer
updates the order, and it can only be set on transfers linked to a sales order.

Once the first shipping label has been generated for the order, the field and the button become
read-only on both forms: changing the destination machine after the parcel exists in Foxpost's
system requires contacting Foxpost.

Shipping labels
===============

When an outgoing delivery with a Foxpost shipping method is validated, Odoo registers the parcel
with Foxpost and immediately downloads its label:

- The returned parcel identifier is stored on the transfer as :guilabel:`Foxpost parcel ID` and
  becomes the transfer's :guilabel:`Tracking Reference`.
- The PDF label is attached to the transfer and posted to its chatter as
  `LabelFoxpost-<parcel id>.pdf`, ready to print.
- If Foxpost rejects the parcel (invalid machine ID, malformed data, etc.), the validation stops
  with a readable error message and nothing is registered.

Parcel registration on validation requires the method's :guilabel:`Integration Level` to be
:guilabel:`Get Rate and Create Shipment` and the :guilabel:`Generate Shipping Labels` option to be
enabled on the operation type (:menuselection:`Inventory app --> Configuration --> Operations
Types`); both are the defaults for delivery operations.

If the label download fails (a network hiccup after a successful registration, for example), the
parcel stays registered and the label can be re-downloaded at any time with the :guilabel:`Get
Foxpost Label` header button on the transfer. The button is available whenever the transfer already
has a parcel ID; labels are printed in A6 size.

.. note::
   Each transfer travels as a single Foxpost parcel with a fixed, medium parcel size — package
   dimensions and weights are not transmitted to Foxpost. Ship one Foxpost transfer per physical
   parcel, and make sure the goods physically fit a medium locker compartment.

Tracking and statuses
=====================

Once a parcel is registered, the transfer displays its live Foxpost status: :guilabel:`Parcel
state` (a human-readable description) and :guilabel:`Parcel state code` (the Foxpost status code).
The date of the last status event is also recorded on the transfer, where it drives the
delivered-date tracking described below.

A scheduled action, :guilabel:`Picking: Update foxpost tracking information`, polls the Foxpost
tracking API every 3 hours for every transfer whose parcel has not yet reached a final state
(delivered, returned, or expired), so open parcels keep updating without any manual work. The
interval can be changed under :menuselection:`Settings --> Technical --> Automation: Scheduled
Actions`, and the :guilabel:`Update Foxpost Status` header button on the transfer refreshes a
single parcel on demand.

When Foxpost reports that the customer has received the parcel — picked it up at the machine, or
accepted the home delivery — the event date is recorded on the transfer as the actual customer
receipt date. That date feeds the order's delivery status and the delivery-date reporting described
in :doc:`../delivery_status_and_dates`.

Configuration
=============

Summary checklist for a working Foxpost setup:

#. Install the **Delivery Foxpost** module (``eyssen_delivery_foxpost``); the shared delivery,
   payment, and delivery-status layers install automatically as dependencies.
#. Get :ref:`test and production API credentials <inventory/shipping_receiving/foxpost-account>`
   from Foxpost.
#. In :menuselection:`Inventory app --> Configuration --> Delivery Methods`, open *Foxpost
   Parcelmachine* and/or *Foxpost Home delivery* (or create new methods with :guilabel:`Provider`
   set to :guilabel:`Foxpost`), then:

   - enter the :guilabel:`API User`, :guilabel:`API Password`, and :guilabel:`API Key`;
   - check the :guilabel:`Delivery type` and, if needed, the :guilabel:`Countries` restriction;
   - configure the :guilabel:`Pricing` tab (fixed price or banded rules);
   - test in :guilabel:`Test Environment`, then switch to :guilabel:`Production Environment` with
     the production credentials;
   - publish the method so it appears on the website.

#. To offer COD, enable and publish the :guilabel:`FoxPost COD, with credit card at
   parcelmachine or at delivery` payment provider under :menuselection:`Website --> Configuration
   --> eCommerce: Payment Providers`.
#. Add the shop's other payment providers (card, wire transfer) to each Foxpost method's
   :guilabel:`Payment Providers` tab, so COD is not the only choice (see
   :doc:`../delivery_payment`).
#. Verify that the outgoing operation type has :guilabel:`Generate Shipping Labels` enabled.

Usage
=====

#. The customer checks out on the website and selects a Foxpost method. For a parcel machine
   method, the Foxpost map opens and they pick their machine; for home delivery, the parcel goes to
   their shipping address.
#. On the payment step they pay online, or — for orders up to 150 000 HUF — choose *FoxPost COD*
   and pay at pickup.
#. The sales order is confirmed — automatically for online payments; for COD orders, confirming it
   remains a back-office step — and the warehouse processes the delivery. If the customer skipped
   the machine selection, staff pick one with :guilabel:`Select on map` (or type the ID) on the
   order or transfer.
#. Validating the transfer registers the parcel with Foxpost, stores the :guilabel:`Foxpost parcel
   ID`, and attaches the printable label to the chatter. For COD orders, the amount to collect for
   this specific delivery is computed and sent along (see :doc:`../cash_on_delivery`).
#. The tracking cron keeps the :guilabel:`Parcel state` up to date. When the customer receives the
   parcel, the receipt date is recorded and the order's delivery status updates accordingly (see
   :doc:`../delivery_status_and_dates`).

Scope and modules
=================

- ``eyssen_delivery_foxpost`` — the Foxpost carrier connector: the *Foxpost* shipping provider with
  parcel machine (APM) and home delivery modes, the map-based parcel machine picker (checkout and
  backend), banded/fixed pricing, parcel registration and PDF labels, tracking synchronization, and
  the *FoxPost COD* payment provider record.

The connector builds on shared eYssen modules documented on their own pages: the per-carrier
payment filtering and COD checkout experience (:doc:`../delivery_payment`), the dynamic
per-delivery COD amount (:doc:`../cash_on_delivery`), and the delivered-date tracking
(:doc:`../delivery_status_and_dates`).

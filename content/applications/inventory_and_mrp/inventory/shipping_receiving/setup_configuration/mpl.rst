.. _inventory/shipping_receiving/mpl:

===============
MPL integration
===============

**MPL** is the parcel service of Magyar Posta, the Hungarian postal operator. The
``eyssen_delivery_mpl`` module connects an Odoo webshop and warehouse directly to the MPL API v2:
customers choose between home delivery and pickup at an MPL *parcel point* (Csomagautomata,
PostaPont or Postán maradó) during checkout, the warehouse prints A6 PDF shipping labels straight
from the delivery order, tracking statuses are synchronized automatically against MPL's
tracking-event catalogue, and a dedicated *MPL COD* cash on delivery (COD) payment method transmits
the amount to collect with every label.

.. seealso::
   - :doc:`third_party_shipper`
   - :doc:`../cash_on_delivery`
   - :doc:`../delivery_payment`
   - :doc:`../delivery_status_and_dates`
   - :doc:`../payment_gated_delivery`

Account setup
=============

MPL shipping requires a business contract with Magyar Posta and access to the **MPL API v2**. The
integration authenticates with OAuth2 client credentials, so the following values must be obtained
from Magyar Posta before configuring Odoo:

- a *Client ID* / *Client Secret* pair for the **test** (sandbox) environment;
- a *Client ID* / *Client Secret* pair for the **production** environment;
- the customer accounting code (*Vevőkód*), sent with shipment and parcel-point API requests;
- the eight-character agreement number (*Megállapodásszám*) of the Magyar Posta contract.

.. tip::
   Start with the test credentials and the :guilabel:`Environment` toggle set to *Test*. The module
   then talks to Magyar Posta's sandbox, so labels and shipments created while testing never enter
   the real MPL network. Switch the carrier to *Production* only when the flow has been verified
   end to end.

.. _inventory/shipping_receiving/mpl-method:

Shipping method configuration
=============================

Two shipping methods ship preconfigured with the module: :guilabel:`MPL Parcel Shop` (pickup at a
parcel point) and :guilabel:`MPL Home delivery`. To review or create one, go to
:menuselection:`Inventory app --> Configuration --> Delivery Methods` and set the
:guilabel:`Provider` field to :guilabel:`MPL`. Doing so reveals two extra tabs on the form: the
:guilabel:`MPL Configuration` tab and a :guilabel:`Pricing` tab.

For the generic fields shared by every carrier — such as :guilabel:`Delivery Product`,
:guilabel:`Countries` availability or the free-over threshold — refer to
:doc:`third_party_shipper`.

.. note::
   To generate MPL shipping labels when a delivery order is validated, set the
   :guilabel:`Integration Level` option to :guilabel:`Get Rate and Create Shipment`. Labels can
   also be created manually at any time with the :guilabel:`Print MPL Label` button on the
   transfer.

Credentials
-----------

The fields on the :guilabel:`MPL Configuration` tab are only visible to users with
:guilabel:`Administration: Settings` rights:

- :guilabel:`Test Client ID` / :guilabel:`Test Client Secret`: the sandbox credential pair, used
  while the carrier's :guilabel:`Environment` is set to *Test*.
- :guilabel:`Production Client ID` / :guilabel:`Production Client Secret`: the live credential
  pair, used in *Production*. The secrets are masked on screen.
- :guilabel:`Accounting Code (Vevőkód)`: the Magyar Posta customer accounting code, transmitted as
  a header with shipment registrations and parcel-point catalog queries.
- :guilabel:`Agreement Number (Megállapodásszám)`: the eight-character contract number, transmitted
  as the sender's agreement on every shipment.

If a label is created, or a synchronization is triggered manually, without credentials for the
active environment, the operation stops with an explicit error message. The scheduled catalog
synchronization logs the failure and retries on its next run.

Delivery types
--------------

The :guilabel:`Delivery type` field on the :guilabel:`MPL Configuration` tab decides how the
carrier behaves:

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * -
     - :guilabel:`Home delivery`
     - :guilabel:`Parcel Shop`
   * - Destination
     - The customer's delivery address.
     - An MPL parcel point chosen by the customer.
   * - Checkout
     - Behaves like any other carrier.
     - Opens the parcel-point selector; the order cannot be confirmed until a point is chosen.
   * - Label
     - Registered as a home-delivery shipment.
     - Registered for pickup at the selected point, using the point's service type.

A parcel point is one of three MPL service point types, all offered together in the selector:

- **Csomagautomata** (parcel locker) — an automated locker, typically available around the clock;
- **Postán maradó** (post office hold) — the parcel is held for collection at a post office;
- **PostaPont** — a staffed pickup location, usually operated by Magyar Posta's retail partners.

The type of the point the customer picks is stored on the sales order together with the point's
identifier and name, and is transmitted to MPL when the label is created.

The :guilabel:`Create Delivery Address for PS` option (off by default, parcel-point carriers only)
makes the webshop create a separate delivery address under the customer for the chosen parcel
point and set it as the order's shipping address. When the customer later switches to another
delivery method, the shipping address reverts to the customer and the temporary parcel-point
address is cleaned up automatically.

Pricing
-------

The module-added :guilabel:`Pricing` tab supports two pricing modes:

- **Banded pricing**: add one or more :guilabel:`Pricing Rules` (by weight, volume, price or
  quantity). Rules are evaluated in order and the *first* matching rule sets the shipping price; if
  no rule matches, the method remains listed at checkout but cannot be selected — Odoo shows *Not
  available for current order*.
- **Fixed fallback**: when no pricing rule is defined, the shipping price is the sales price of the
  method's :guilabel:`Delivery Product`, resolved through the order's pricelist; the
  :guilabel:`Fixed Price` field edits that product's base sales price, and pricelist rules on the
  delivery product override it per pricelist.

Standard carrier mechanics — the free-over threshold, margins and taxes — are applied on top of
both modes, exactly as for any other shipping method.

.. note::
   Selecting *any* MPL method at checkout also adds a :guilabel:`Handling service` product line to
   the order (default sales price: 2 000 in the company currency — i.e. 2 000 HUF on a Hungarian
   database — priced through the order's pricelist). The line is
   removed automatically when the customer switches to a non-MPL method. To disable this surcharge,
   set the sales price of the *Handling service* product to ``0``.

Cash on delivery
----------------

The module ships a payment provider named :guilabel:`MPL COD, with credit card at parcelshop or at
delivery`. Like every provider, it must be enabled and published before it appears at checkout,
and it is only offered when the website has a published MPL shipping method and the cart contains
physical products.

- The amount to collect is computed per outgoing delivery (transfer) — partial shipments, service
  lines and invoiced down payments are all handled by the shared computation described in
  :doc:`../cash_on_delivery`, and the result is stored in the :guilabel:`COD Amount` field of the
  transfer.
- The amount is transmitted as a whole number: orders in HUF are sent as-is; orders in another
  currency are converted to HUF at the current exchange rate when the label is created, and the
  order's currency code is transmitted alongside the amount. Verify foreign-currency COD orders
  with Magyar Posta before relying on this.
- The :guilabel:`COD Bank Account` field on the :guilabel:`MPL Configuration` tab is sent as the
  payout account for collected amounts.
- Which payment methods are offered together with each MPL shipping method — and the COD-specific
  checkout experience — is controlled by the per-carrier payment filtering described in
  :doc:`../delivery_payment`. Out of the box, the shipped MPL carriers only allow their own COD
  provider — as long as no other carrier's COD provider is enabled, since COD providers are
  validated on their own track (see :doc:`../delivery_payment`) — so add the shop's card or
  wire-transfer providers to the carriers to offer a choice.

.. important::
   When a COD shipment is split into several packages, the current integration transmits the *full*
   COD amount with every package. Ship COD orders as a single package, or verify with Magyar Posta
   how multi-package COD dispatches are collected, to avoid over-charging the customer.

Phone number validation
-----------------------

MPL requires a valid **Hungarian mobile or phone number** for every shipment. When a label is
created, the module takes the delivery address's :guilabel:`Mobile` number, then its
:guilabel:`Phone` number, then falls back to the parent contact, and normalizes the result to the
international ``+36`` format (numbers entered with the domestic ``06`` prefix are converted
automatically). If no number is found, or the number is not Hungarian, label creation stops with a
blocking error — the integration is domestic-only in this respect.

.. _inventory/shipping_receiving/mpl-catalog:

Parcel-point catalog
====================

The webshop selector does not query Magyar Posta on every page view. Instead, the module keeps a
**local catalog** of all MPL parcel points (name, address, coordinates and service point type),
kept up to date by the daily scheduled action :guilabel:`MPL: Sync Delivery Places`:

- the full list of Csomagautomata, Postán maradó and PostaPont locations is downloaded from the
  MPL API, using the credentials of a configured MPL shipping method;
- existing entries are updated in place, new ones are added, and points that no longer exist at
  Magyar Posta are removed;
- each entry records when it was last synchronized.

An order that already stores a chosen point keeps working even if that point later disappears from
the catalog — the point's identifier and name are copied onto the order at selection time.

.. tip::
   Right after installation the catalog is empty until the scheduled action first runs. The backend
   selector helps out in this state: searching by ZIP code or city fetches matching points live
   from the MPL API and stores them locally.

Website checkout: choosing a parcel point
=========================================

When a customer selects an MPL parcel-point shipping method at checkout, a full-screen selector
opens immediately, and the checkout cannot continue until a point is chosen — a warning is shown
under the shipping method until then. The selected point is displayed under the method, stored on
the order, and restored automatically when the customer returns to the checkout later.

The selector has two modes, decided by the website configuration:

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * -
     - Map widget
     - Searchable list
   * - Requirement
     - :guilabel:`Google Maps API Key` set in the website settings
     - none (default)
   * - Interface
     - Magyar Posta's official *PostaPont* map widget on a Google map
     - Built-in list with type filters (Csomagautomata / Postán maradó / PostaPont), text search
       and paging
   * - Data source
     - Loaded live from Magyar Posta
     - The local :ref:`parcel-point catalog <inventory/shipping_receiving/mpl-catalog>`
   * - Service point type
     - Not provided by the widget — shipments are registered with the generic *PostaPont* delivery
       mode
     - Stored with the selection and transmitted to MPL

To enable the map mode, go to :menuselection:`Website --> Configuration --> Settings`, find the
:guilabel:`MPL` block and enter a :guilabel:`Google Maps API Key`. Leave the key empty to use the
searchable list, which needs no external service beyond the daily catalog synchronization.

Back-office users can pick or change the point without the webshop: the sales order and the
transfer both show an :guilabel:`MPL parcel point` field with a :guilabel:`Select on map` button
that opens the :guilabel:`Select MPL parcel point` dialog — a searchable list with
:guilabel:`Parcel locker`, :guilabel:`Post office hold` and :guilabel:`PostaPont` filters. The
field locks once the shipment has been registered with MPL or the order is done or cancelled.

Shipping labels
===============

Labels are generated in **A6 PDF** format, ready for label printers:

- With the :guilabel:`Integration Level` set to :guilabel:`Get Rate and Create Shipment`,
  validating the delivery order registers the shipment with MPL automatically.
- The :guilabel:`Print MPL Label` button on the transfer creates the shipment manually at any
  time; it disappears once a label exists.
- On success, the transfer stores the :guilabel:`MPL parcel ID`, the :guilabel:`MPL parcel number`
  (when the shipment is registered by validating the transfer, the number is also copied to the
  standard tracking reference; the manual :guilabel:`Print MPL Label` button fills only the MPL
  fields) and the downloadable :guilabel:`MPL label`, and the label PDF is attached to the
  transfer's chatter together with the tracking number.

When the products are packed into several packages, one parcel is registered per package, and each
package's shipping weight is transmitted individually (weights are sent in grams, with a minimum
of 100 g and a default of 1 kg when no weight is set). When MPL returns per-package tracking
numbers, each package record stores its own number so parcels can be followed one by one;
otherwise, the packages share the shipment's tracking number.

.. important::
   :guilabel:`Print MPL Label` is not a reprint button. Pressing it clears the stored parcel data
   and registers a **new** shipment with MPL. For this reason it is hidden once a label exists;
   re-registering a shipment is only offered to users with developer mode enabled. To reprint an
   existing label, download the stored :guilabel:`MPL label` file or the chatter attachment
   instead.

.. note::
   The sender address transmitted to MPL is always the **company address**, not the warehouse
   address. Merchants shipping from several warehouses appear towards MPL under the company's
   registered address.

Tracking and statuses
=====================

The module ships MPL's tracking-event catalogue — 46 states across the pickup,
processing, transport and delivery phases — as editable records under
:menuselection:`Inventory app --> Configuration --> MPL Delivery States`, each with a
:guilabel:`State Code`, :guilabel:`State Category`, :guilabel:`MPL State Name` and a
:guilabel:`Delivered State` checkbox.

Statuses are refreshed automatically by two scheduled actions, each running every three hours:

- :guilabel:`Picking: Update MPL tracking information` polls every transfer that has an MPL parcel
  number and is not yet done or cancelled;
- :guilabel:`Package: Update MPL tracking information` polls individual packages, up to 50 per
  run, spacing repeat checks of the same package by the configured :guilabel:`Tracking Check
  Interval` (default: 60 minutes).

The latest state, its code and its timestamp are shown on the transfer (:guilabel:`Parcel state`,
:guilabel:`Parcel state code`, :guilabel:`Parcel state date`) and on each package; the transfer
also has an :guilabel:`Update MPL Status` button for an on-demand refresh.

Two automations build on the state catalogue:

- **Delivered date**: when a tracking event maps to a state whose :guilabel:`Delivered State` box
  is checked, the date the customer actually received the goods is stamped on the transfer (the
  actual customer receipt date), using the delivery timestamp reported by MPL. This feeds the
  order-level delivery progress described in :doc:`../delivery_status_and_dates`.
- **Auto-validation**: on the operation type (:menuselection:`Inventory app --> Configuration -->
  Operations Types`), the :guilabel:`Validation on MPL Delivery` group offers
  :guilabel:`Validate Picking on Delivery` together with a :guilabel:`Validate on MPL States`
  list. Once *every* package of a transfer reaches one of the selected states, the transfer is
  validated automatically. This enables a deferred-validation flow: leave the delivery order open
  after printing the label, let the scheduled actions follow the parcel, and have Odoo close the
  transfer when MPL reports delivery.

.. warning::
   When using the deferred-validation flow, set the shipping method's :guilabel:`Integration Level`
   to :guilabel:`Get Rate` (or untick :guilabel:`Generate Shipping Labels` on the operation type).
   With :guilabel:`Get Rate and Create Shipment`, the automatic validation registers the shipment
   with MPL a *second* time, because the :guilabel:`Print MPL Label` button does not fill the
   standard tracking reference that suppresses the validation-time registration.

.. important::
   None of the 46 shipped states is pre-flagged as delivered. Tick :guilabel:`Delivered State` on
   the terminal *Kézbesített* (delivered) rows after installation — otherwise neither the
   delivered-date stamping nor a delivery-based auto-validation setup has any effect.

.. note::
   The transfer-level scheduled action deliberately skips transfers that are already done. If
   deliveries are validated immediately at shipping time, tracking keeps refreshing only through
   the package-level action and the manual :guilabel:`Update MPL Status` button.

Configuration
=============

Checklist to take MPL live:

#. Install ``eyssen_delivery_mpl``.
#. On each MPL shipping method (:menuselection:`Inventory app --> Configuration --> Delivery
   Methods`), fill in the :guilabel:`MPL Configuration` tab: credentials for the chosen
   :guilabel:`Environment`, :guilabel:`Accounting Code (Vevőkód)`, :guilabel:`Agreement Number
   (Megállapodásszám)` and — for COD — the :guilabel:`COD Bank Account`.
#. Choose the :guilabel:`Delivery type` per method, set up the :guilabel:`Pricing` tab, and
   publish the methods on the website.
#. Enable and publish the :guilabel:`MPL COD, with credit card at parcelshop or at delivery`
   payment provider, and review each carrier's enabled payment providers (see
   :doc:`../delivery_payment`).
#. In :menuselection:`Website --> Configuration --> Settings`, :guilabel:`MPL` block: optionally
   set a :guilabel:`Google Maps API Key` for the map selector, and adjust the
   :guilabel:`Tracking Check Interval` if needed.
#. Under :menuselection:`Inventory app --> Configuration --> MPL Delivery States`, tick
   :guilabel:`Delivered State` on the delivered rows.
#. Optionally configure auto-validation on the outgoing operation type
   (:guilabel:`Validate Picking on Delivery` + :guilabel:`Validate on MPL States`).
#. Set the sales price of the :guilabel:`Handling service` product (``0`` disables the checkout
   surcharge).
#. Let the daily :guilabel:`MPL: Sync Delivery Places` scheduled action populate the parcel-point
   catalog, or trigger an initial ZIP-code search from the backend selector.

Usage
=====

#. A customer checks out on the website and picks an MPL shipping method. For a parcel-point
   method, the selector opens and the customer chooses a Csomagautomata, Postán maradó or
   PostaPont location; the checkout is blocked until a point is selected.
#. The customer pays — with the *MPL COD* method, or any other provider enabled for the carrier —
   and the chosen parcel point is stored on the sales order.
#. The warehouse processes the delivery order. Validating it (or pressing :guilabel:`Print MPL
   Label`) registers the shipment with MPL, computes the COD amount when applicable, and attaches
   the A6 PDF label — with per-package tracking numbers when MPL provides them.
#. The scheduled actions follow the parcel through MPL's tracking states. When a state flagged as
   :guilabel:`Delivered State` is reached, the customer receipt date is stamped, and — if
   configured on the operation type — the transfer is validated automatically.

Scope and modules
=================

- ``eyssen_delivery_mpl`` — the MPL carrier connector: the *MPL* shipping method type with home
  delivery and parcel-point flavours, the parcel-point catalog and selectors, A6 PDF label
  generation, tracking synchronization with auto-validation, and the *MPL COD* payment provider.

The COD amount computation, the per-carrier payment filtering and the delivery-status fields the
connector plugs into are shared building blocks documented in :doc:`../cash_on_delivery`,
:doc:`../delivery_payment` and :doc:`../delivery_status_and_dates`.

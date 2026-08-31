.. _inventory/shipping_receiving/custom-carrier:

==============
Custom carrier
==============

Not every parcel leaves the warehouse with an external courier. Goods delivered by the company's
**own fleet** — a van route, a local driver, a one-off transport — still need a shipping cost on the
order and a proper address label on every box, but there is no courier API to call and no tracking
number to fetch. The **Custom** carrier, added by the ``eyssen_delivery_custom`` module, covers
exactly this case: it behaves like any other delivery method on quotations, in the webshop and on
delivery orders, while the address labels are generated *in-house* as a printable PDF, with no
external service involved. A small bridge module, ``eyssen_stock_multi_warehouse_delivery_custom``,
extends the same labels to warehouse-to-warehouse internal transfers.

.. seealso::
   - :doc:`Add a new delivery method <new_delivery_method>` — the standard fixed-price and
     rule-based providers
   - :doc:`Delivery-based payment methods <../delivery_payment>` — restricting which payment
     methods are offered per carrier
   - :doc:`../delivery_status_and_dates` — delivery status and dates on the sales order
   - :doc:`../payment_gated_delivery` — holding deliveries until the order is paid

How it differs from a standard delivery method
==============================================

The Custom carrier is a full *provider*, selectable in the :guilabel:`Provider` field of a shipping
method, alongside :guilabel:`Fixed Price`, :guilabel:`Based on Rules` and the third-party
connectors. It differs from those options in how the price is found and where the label comes from:

.. list-table::
   :header-rows: 1
   :widths: 24 38 38

   * - Aspect
     - Standard method (fixed / rules)
     - Custom carrier
   * - Shipping cost
     - A fixed amount, or computed from weight, volume, quantity or price rules
     - The **pricelist price** of the method's delivery product — so the fee can differ per
       pricelist, per website or per customer, using ordinary pricelist rules
   * - Availability
     - Can be restricted by destination (country, state, zip prefix), a maximum weight or volume,
       and product tags
     - The same generic restrictions apply; the provider adds no availability rules of its own,
       and computing the rate never fails
   * - Shipping label
     - None (or provided by a third-party connector)
     - Generated **in-house** as a PDF of address labels with barcodes, four per A4 landscape page
   * - Tracking reference
     - Provided by the external carrier, where one is integrated
     - The delivery order's own reference; there is **no external tracking link** for the customer
   * - External account
     - Third-party connectors require credentials and a carrier contract
     - None — no API, no credentials, no per-label fee

.. note::
   Because nothing reports the parcel's journey back to Odoo, the :guilabel:`Actual Customer
   Receipt Date` used by carrier-tracking integrations is never filled for Custom deliveries; the
   sales order's delivery status is still computed from the validated transfers as described in
   :doc:`../delivery_status_and_dates`.

Configuration
=============

Carrier record
--------------

Installing ``eyssen_delivery_custom`` creates a ready-to-use shipping method named
:guilabel:`Custom`, visible under :menuselection:`Inventory app --> Configuration --> Delivery
Methods`. Its :guilabel:`Provider` is :guilabel:`Custom` and its :guilabel:`Delivery Product` is
the :guilabel:`Custom Shipping Product` described below. Additional methods using the same provider
can be created with :guilabel:`New` by selecting :guilabel:`Custom` in the :guilabel:`Provider`
field — each with its own delivery product, and therefore its own pricing.

To offer the method in the webshop, it must also be **published**, like any other carrier.

Shipping product and pricing
----------------------------

The module ships a service product, :guilabel:`Custom Shipping Product`, that is added to the sales
order as the delivery line. The shipping fee charged to the customer is simply **the price of this
product on the order's pricelist**:

- setting the product's :guilabel:`Sales Price` defines a flat default fee;
- adding :doc:`pricelist rules <../../../../sales/sales/products_prices/prices/pricing>` on the
  product defines different fees per pricelist — and, since each website can use its own pricelist,
  per website.

.. note::
   The chatter message logged when the shipment is registered reports a carrier *cost* of zero —
   the Custom carrier has no external cost — unless a :guilabel:`Fixed Margin` is configured on
   the shipping method, which is then reported as the cost. The amount the customer pays is the
   delivery line added to the sales order from the pricelist price.

Package types
-------------

Labels are generated **per package**, so goods must be packed before a label can be printed. The
module adds a package type, :guilabel:`Custom Box`, whose :guilabel:`Carrier` is set to
:guilabel:`Custom`; further package types (different box sizes, pallets) can be created under
:menuselection:`Inventory app --> Configuration --> Package Types` and tagged with the
:guilabel:`Custom` carrier the same way.

.. important::
   Always use :guilabel:`Put in Pack` on the delivery order before validating it or printing the
   label. The label PDF contains one label per package; on a delivery order without packages,
   label generation fails with an error — no PDF is produced — and validating the transfer fails
   with it.

Paper format
------------

The label report prints on a dedicated :guilabel:`A4 / Landscape` paper format (10 mm margins, no
header), with **four labels per page** — each label fills a quarter of the sheet, ready to be cut
and affixed. With the :ref:`developer mode <developer-mode>` enabled, the format can be adjusted
under :menuselection:`Settings app --> Technical --> Reporting: Paper Format` if a different
layout is needed.

Printing delivery labels
========================

The label PDF is generated in two ways:

- **Automatically**, when the delivery order is validated — exactly like a third-party carrier
  registering a shipment; or
- **Manually**, with the :guilabel:`Print Custom Label` button shown on the delivery order form
  next to the :guilabel:`Carrier` field. The button is only visible while no label exists yet;
  once generated, the PDF is stored in the :guilabel:`Custom label` field on the same form, and
  removing the file there makes the button reappear so the label can be regenerated.

In both cases the PDF is also attached to the delivery order's chatter (message *Shipment
created*), named after the transfer reference, so it can be reprinted at any time.

Each label shows:

- the **delivery order reference**, as text and as a barcode — this is also the tracking reference
  recorded on the transfer;
- the **package name**, as text and as a barcode, with a counter (for example `2/3` for the second
  of three packages);
- the transfer's effective date (or its scheduled date when not yet done);
- the **sender** block (printed as *Feladó:*) — the address of the warehouse the goods leave from,
  falling back to the company address;
- the **recipient** block (printed as *Címzett:*) — the customer's delivery address.

.. note::
   The sender and recipient captions on the printed label are in Hungarian (*Feladó* / *Címzett*),
   matching the domestic own-fleet use case the label was designed for.

.. important::
   Generate the label from the :guilabel:`Print Custom Label` button or by validating the delivery
   order — **not** from the generic :guilabel:`Picking Custom Label` entry in the transfer's print
   menu, which does not receive the label data.

Multi-warehouse transfers
=========================

Companies that move stock between their own warehouses with the eYssen internal-transfer flow can
use the Custom carrier on those transfers too. The bridge module
``eyssen_stock_multi_warehouse_delivery_custom`` adjusts only the addresses printed on the label:
when the delivery order belongs to an internal transfer, the sender block shows the **source
warehouse's** address and the recipient block the **destination warehouse's** address, instead of
the company and a customer. Everything else — packing, generation, storage in the
:guilabel:`Custom label` field — works as described above. Automatic generation at validation
additionally requires the transfer's operation type to have :guilabel:`Generate Shipping Labels`
enabled (on by default only for delivery-type operations); the :guilabel:`Print Custom Label`
button works in any case.

The bridge has no configuration of its own; install it when both the multi-warehouse
internal-transfer module and ``eyssen_delivery_custom`` are in use.

Usage
=====

#. On a quotation, add shipping and pick the :guilabel:`Custom` method (or let the customer select
   it at webshop checkout, where it appears once published). The delivery line is priced from the
   order's pricelist.
#. Confirm the order; the delivery order is created with the Custom carrier set.
#. In the warehouse, pick the goods and use :guilabel:`Put in Pack` for every physical box, using a
   package type tagged with the :guilabel:`Custom` carrier.
#. Validate the delivery order — the label PDF is generated, stored on the transfer and attached to
   the chatter — or press :guilabel:`Print Custom Label` first to print before validating.
#. Print the PDF, cut the A4 sheet into its four labels, affix one to each box, and hand the
   parcels to the driver.
#. The sales order's delivery status updates from the validated transfer as usual (see
   :doc:`../delivery_status_and_dates`).

Scope and modules
=================

- ``eyssen_delivery_custom`` — the :guilabel:`Custom` delivery provider: the seeded shipping
  method, shipping product, package type and paper format, pricelist-based rating, and the in-house
  A4 label report with its :guilabel:`Print Custom Label` button.
- ``eyssen_stock_multi_warehouse_delivery_custom`` — prints source- and destination-warehouse
  addresses on Custom labels generated for multi-warehouse internal transfers.

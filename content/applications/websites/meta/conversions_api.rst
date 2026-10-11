===============
Conversions API
===============

The **Conversions API** sends events to Meta **from the server**, in addition to (or instead of) the
:doc:`pixel <pixel>`. It is not affected by ad blockers or by the browsers that limit scripts, and
it can report events that happen when nobody is on the website: a payment confirmed later, a lead
qualified by a salesperson, or a sale at the store counter.

Like every outgoing event, the events are put in a queue, sent in batches every few minutes, and
retried when Meta is not reachable. See :doc:`/applications/websites/website/tracking/server_events`.

.. important::
   The server events respect the choice of the visitor: an event of a website visit is only sent if
   the visitor accepted the **marketing** cookies. The exceptions are the store sales (see
   :ref:`meta/capi/store-sales`) and the CRM events of leads that come from a Meta lead form.

Set up the Conversions API
==========================

#. In Meta Events Manager, open your dataset (pixel), then *Settings > Conversions API*, and
   generate an **access token** for a system user, or use a :doc:`Meta connection <connection>`.
#. In Odoo, go to :menuselection:`Meta --> Configuration --> Settings`. In the :guilabel:`Conversions
   API` block, enable :guilabel:`Conversions API` and fill in:

   .. list-table::
      :header-rows: 1
      :widths: 30 70

      * - Field
        - Description
      * - :guilabel:`Dataset ID`
        - The dataset (pixel) that receives the events. Leave it empty to use the main pixel ID.
      * - :guilabel:`Conversions API Access Token`
        - The system user token generated in Events Manager (administrators only). Leave it empty to
          use the :guilabel:`Meta Connection` of the website.

.. screenshot:: meta-settings-capi
   :menu: Meta ‣ Configuration ‣ Settings
   :shows: The Conversions API block of the Meta settings with the Conversions API setting enabled:
      the Dataset ID and access token fields (hidden), the Server Events link, then the Conversions
      API Only, Browser Events (with Page Views), Test Events, Limited Data Use, Store Sales, and
      CRM Lead Events settings.
   :highlight: The Conversions API setting (red frame).
   :data: Dataset "1234567890123456", token hidden (throw-away).
   :notes: English UI, light theme, 1440px width, crop to the block.

Which events are sent
=====================

By default, the server sends the events that only the server can know reliably: *Purchase*, *Lead*,
and *CompleteRegistration*. The following settings change this:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Setting
     - Description
   * - :guilabel:`Conversions API Only`
     - Does not load the pixel in the browser: every event is sent by the server. The visitor still
       needs to accept the marketing cookies.
   * - :guilabel:`Browser Events`
     - Enabled by default. Also sends from the server the events of the browser: *ViewContent*,
       *Search*, *AddToCart*, *AddToWishlist*, *InitiateCheckout*, *AddPaymentInfo*, *Contact*, and
       *Subscribe* (and the custom events, if enabled). When the pixel is active too, Meta
       deduplicates them with the same event ID.
   * - :guilabel:`Page Views`
     - Also sends every *PageView* from the server. It produces many events: enable it only with
       :guilabel:`Conversions API Only`.
   * - :guilabel:`Store Sales`
     - See :ref:`meta/capi/store-sales`.
   * - :guilabel:`CRM Lead Events`
     - Sends the stage events of the :doc:`lead tracking rules
       </applications/sales/crm/optimize/lead_tracking>`: the default Meta events are *WorkingLead*,
       *QualifiedLead*, *DisqualifiedLead*, *ConvertedLead*, and *LostLead*. With the :doc:`Lead
       Ads <lead_ads>` feature, each rule chooses its own event name.

What the events contain
=======================

Each event contains the event name, the time, the event ID, the page address, the products (IDs,
quantities, prices) and the value, plus information that helps Meta to recognize the person:

- the **hashed** (SHA-256) email, phone number, first name, last name, city, state, ZIP code, and
  country of the customer, and an external ID (the hashed customer ID in Odoo);
- the IP address and the browser of the visitor, and the Meta click and browser identifiers
  (`fbc` and `fbp` cookies).

Meta does not accept events older than **seven days**: the events that could not be sent before are
discarded.

.. _meta/capi/store-sales:

Store sales
-----------

With :guilabel:`Store Sales`, the paid point of sale orders of customers whose contact details are
known are sent as purchases that happened in a physical store. See :doc:`/applications/sales/point_of_sale/store_sales_tracking`.

.. warning::
   No cookie consent can be collected at the counter. Enable this setting only if your legal basis
   allows it, and inform your customers in your privacy policy.

Limited Data Use
----------------

:guilabel:`Limited Data Use` marks the server events so that Meta applies its restricted processing,
which is intended for the US state privacy laws. Meta applies it according to the location of the
visitor.

.. _meta/capi/test:

Test the Conversions API
========================

#. In Events Manager, open the dataset, go to the *Test events* tab, and copy the **test event
   code**.
#. In Odoo, enable :guilabel:`Test Events` and paste the code in the :guilabel:`Test Event Code`
   field.
#. Click :guilabel:`Send Test Event`. A *PageView* event is queued and sent in a few seconds. It
   appears in the *Test events* tab and in the :menuselection:`Meta --> Server Events` list.

While :guilabel:`Test Events` is enabled, every server event carries the code: it appears in the
*Test events* tab and is **not used** for ads. Disable the setting when the test is done.

.. screenshot:: meta-events-manager-test
   :shows: The Test events tab of Meta Events Manager receiving a PageView server event with the
      "Server" source tag, next to the same event from the browser.
   :highlight: The server event and its deduplication badge (red frame).
   :data: Throw-away dataset.
   :notes: Screenshot of Meta Events Manager, not of Odoo. Hide the account name.

The :menuselection:`Meta --> Server Events` list shows the sent, pending, and failed events with
the answer of Meta. See :doc:`/applications/websites/website/tracking/troubleshooting`.

.. seealso::
   - :doc:`pixel`
   - :doc:`connection`
   - :doc:`/applications/websites/website/tracking/privacy`

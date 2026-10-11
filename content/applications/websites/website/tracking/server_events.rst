=============
Server events
=============

Many events are sent from the **server** and not from the visitor's browser: purchases confirmed
later, refunds, lead stages, store sales, Meta Conversions API events, offline conversions, and
catalog updates. Server events are not lost if the visitor closes the page, are not blocked by ad
blockers, and can carry data that the browser does not have. They are queued, then sent by a
scheduled action that runs every 5 minutes.

Go to :menuselection:`Website --> Configuration --> Tracking & Consent --> Server Events` (also
available as :menuselection:`Google --> Reporting --> Server Events` and :menuselection:`Meta -->
Server Events`) to follow them.

.. screenshot:: tracking-server-events-list
   :menu: Website ‣ Configuration ‣ Tracking & Consent ‣ Server Events
   :shows: The Server Events list with a few lines of different providers and statuses (Sent,
      Pending, Error), the Send Again button above the list, and the filters Pending, Errors, Sent,
      and Test Events.
   :highlight: The Status column (red frame).
   :data: Events "purchase", "refund", "QualifiedLead" for providers Google and Meta.
   :notes: English UI, light theme, 1440px width.

Each line shows the :guilabel:`Date`, the :guilabel:`Provider` (for example the GA4 Measurement
Protocol, the Meta Conversions API, the Data Manager API, or the Merchant API), the
:guilabel:`Event`, the number of :guilabel:`Attempts`, the :guilabel:`Sent Date`, and the status:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Status
     - Meaning
   * - :guilabel:`Pending`
     - Waiting to be sent, or waiting for the next attempt.
   * - :guilabel:`Sent`
     - Accepted by the provider.
   * - :guilabel:`Error`
     - Refused or not sent after the last attempt. Read the error in the :guilabel:`Response` tab.
   * - :guilabel:`Discarded`
     - Expired before it could be sent (the providers refuse events that are too old).

If an attempt fails because of a temporary problem, Odoo tries again after 1 minute, 5 minutes,
30 minutes, 2 hours, 6 hours, and 24 hours. Then the event stays in :guilabel:`Error`, unless it
expired, in which case it is :guilabel:`Discarded`.

Open a line to see the :guilabel:`Payload` (the data sent: personal data is hashed), the
:guilabel:`Response` of the provider, the :guilabel:`Event ID` shared with the browser event (used
to avoid counting the event twice), the date of the next attempt, and, with the :guilabel:`Document`
button, the order, the lead, or the invoice that caused the event.

To send events again, select them in the list and click :guilabel:`Send Again`, or click the
button on a single event.

Use the filters :guilabel:`Pending`, :guilabel:`Errors`, :guilabel:`Sent`, and :guilabel:`Test
Events`, and group by :guilabel:`Provider`, :guilabel:`Event`, or :guilabel:`Status`. The events
sent in a test or validation mode are marked as test events: see :doc:`troubleshooting`.

.. note::
   The lines are removed after the delay set in :guilabel:`Keep Sent Events (days)` (see
   :ref:`tracking/consent/retention`). Only designers can read the list; administrators can also
   delete lines.

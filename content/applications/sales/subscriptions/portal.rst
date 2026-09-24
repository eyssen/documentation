===========================
Subscriptions on the portal
===========================

Customers follow their own subscriptions from the customer portal, without access to the backend.

What the customer sees
======================

A :guilabel:`Subscriptions` entry appears on the portal home page with the number of contracts the
customer has. It opens the list of their contracts with the reference, the dates and a state badge;
clicking one opens its detail page with the subscription lines, their periods and their prices.

Portal users only ever see the contracts and lines of their own partner.

.. screenshot:: sales-subscriptions-portal-list
   :menu: (customer portal) ‣ Subscriptions
   :shows: The customer portal list of subscriptions with the contract reference, the start date and the state badge on each row.
   :highlight: The Subscriptions entry and the state badges (red frames).
   :data: A demo portal user with two contracts, one Active and one Suspended.
   :module: subscription
   :notes: English UI, light theme, 1440px width, crop to the portal table.

Cancelling from the portal
==========================

The detail page offers the customer a way to request the cancellation of the contract. The contract
is then closed, and the reason is stored in its :guilabel:`Close Reason` field, so the backend shows
that the customer ended it themselves.

.. screenshot:: sales-subscriptions-portal-detail
   :menu: (customer portal) ‣ Subscriptions ‣ (a contract)
   :shows: The portal detail page of one subscription: the contract reference and state badge, the subscription lines with their periods and prices, and the cancellation action.
   :highlight: The cancellation action (red frame).
   :data: Contract SUB/2026/0012 with two lines.
   :module: subscription
   :notes: English UI, light theme, 1440px width, crop to the page.

.. seealso::
   :doc:`contracts`

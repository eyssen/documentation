:show-content:
:hide-page-toc:
:show-toc:

=============
Subscriptions
=============

The **Subscriptions** application bills customers repeatedly, on its own, from *subscription
contracts*. A contract groups everything that belongs to one customer agreement; each
*subscription line* inside it describes one recurring service: what is billed, how often, at what
price, and until when. A scheduled action then generates the recurring invoices.

The application is built for recurring billing only. It does not go through quotations or sales
orders: a contract is created directly, and the invoices it produces are ordinary customer invoices
in **Accounting**.

Installation and access rights
==============================

Install the **Subscription Management** module from the :menuselection:`Apps` application. It adds
a :menuselection:`Subscriptions` menu with the :guilabel:`Contracts`, :guilabel:`Subscription
Lines`, :guilabel:`Reporting` and :guilabel:`Configuration` entries.

Access follows the **Sales** access rights:

- :guilabel:`Sales / User`: can read and edit contracts, lines, pricing tiers, coupons, billing
  periods and quantity formulas.
- :guilabel:`Sales / Administrator`: can additionally delete them and maintain the configuration.
- Accounting users can see the dunning attempts.
- Portal users see their own contracts and lines only, through the customer portal.

In a multi-company database every record belongs to one company, and users only see the contracts
of the companies they are allowed to access.

.. screenshot:: sales-subscriptions-menu
   :menu: Subscriptions
   :shows: The Subscriptions application menu bar with the Contracts, Subscription Lines, Reporting and Configuration entries.
   :highlight: The menu bar (red frame).
   :data: Demo database with the Subscription Management module installed.
   :module: subscription
   :notes: English UI, light theme, 1440px width, crop to the menu bar.

.. toctree::
   :titlesonly:

   subscriptions/products
   subscriptions/contracts
   subscriptions/lines
   subscriptions/billing
   subscriptions/automatic_payments
   subscriptions/portal
   subscriptions/reports
   subscriptions/configuration

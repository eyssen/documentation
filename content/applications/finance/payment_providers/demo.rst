====
Demo
====

Odoo's **Demo Payment Provider** allows you to test business flows involving online transactions
without requiring real banking credentials.

Configuration
=============

.. seealso::
   :ref:`payment_providers/add_new`

.. important::
   Switch the state to :guilabel:`Test Mode`.

Payment outcome
===============

Upon checkout or when paying a bill online, you can choose the payment outcome when using the demo
payment provider. To do so, click on the :guilabel:`Payment Status` drop-down menu and select the
desired outcome.

.. screenshot:: finance-payment-providers-demo-demo-payment-outcome
   :menu: (eCommerce checkout or customer portal) ‣ Payment ‣ Demo
   :shows: The checkout payment step with the "Demo" payment method selected and its "Payment Status" drop-down open, listing the possible outcomes (Success, Pending, Cancelled, Error).
   :highlight: The "Payment Status" drop-down.
   :data: Demo provider in Test Mode.
   :module: payment_demo
   :notes: English UI, light theme, 1440px width.

Transaction state
=================

If you selected :guilabel:`Pending` as **payment outcome**, you can change the state of the
transaction straight from its form view. To access a transaction's form view, activate the
:ref:`developer mode <developer-mode>`, and go to :menuselection:`Accounting / Website -->
Configuration --> Payment Transactions`. Then, change the status of a transaction by clicking on the
state bar (:guilabel:`Draft, Pending, Authorized, Confirmed, Cancelled, Error`).

.. screenshot:: finance-payment-providers-demo-demo-view-form
   :menu: Accounting ‣ Configuration ‣ Payment Transactions ‣ (a demo transaction)
   :shows: A payment transaction form (developer mode) of the Demo provider in "Pending" state with the clickable status bar Draft / Pending / Authorized / Confirmed / Cancelled / Error.
   :highlight: The status bar.
   :data: Transaction reference S00042-1, provider Demo.
   :module: payment_demo
   :notes: English UI, light theme, 1440px width.

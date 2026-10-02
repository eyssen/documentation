======
Redsys
======

`Redsys <https://www.redsys.es/>`_ is the payment processor behind the virtual POS (:abbr:`TPV
(Terminal Punto de Venta)` virtual) that most Spanish banks offer to their business customers. The
**Redsys** payment provider lets your customers pay by card, or with `Bizum <https://bizum.es/>`_,
on your eCommerce website and customer portal.

With the **redirection** integration, customers are sent to the secure Redsys payment page to
complete the payment and are then brought back to your database. No card data is entered in, or
stored by, your database.

.. note::
   The Redsys provider is provided by the eYssen ``payment_redsys`` module. It is activated
   automatically with the module: no additional module needs to be installed.

Prerequisites
=============

- A Redsys virtual POS contract with your bank, which provides you with a **merchant code** (also
  called :abbr:`FUC (Fábrica Unificada de Comercios)`), a **terminal** number, and a **secret key**
  (:dfn:`clave secreta de firma`) for each environment (test and production).
- For :ref:`Bizum <payment_providers/redsys/bizum>`, Bizum must be enabled on your virtual POS by
  your bank.
- The currency of the payment must have an :abbr:`ISO 4217 (International Organization for
  Standardization currency code standard)` numeric code (all common currencies do).

.. _payment_providers/redsys/configure_redsys:

Redsys configuration
====================

Your bank gives you access to the Redsys administration portal (*Canales*), with one portal for the
test environment and one for production. In each of them, collect the following values:

- the **merchant code** (FUC);
- the **terminal** number (usually ``1``);
- the **secret key** of the terminal (:dfn:`clave secreta de firma`).

.. important::
   Odoo only accepts messages signed with the **HMAC_SHA512_V2** signature version. Make sure your
   terminal is configured to use it in the Redsys administration portal; if you do not know how,
   ask your bank. Messages signed with another version, such as ``HMAC_SHA256_V1``, are rejected
   (see :ref:`payment_providers/redsys/troubleshooting`).

.. note::
   The URLs Redsys uses to report the payment result to Odoo (the online notification and the
   customer return URLs) are sent to Redsys with each payment request, so you do not need to enter
   them in the Redsys administration portal.

.. _payment_providers/redsys/configure_odoo:

Odoo configuration
==================

#. :ref:`Navigate to the payment provider Redsys <payment_providers/add_new>`.
#. In the :guilabel:`Credentials` tab, fill in the fields with the values collected in the
   :ref:`payment_providers/redsys/configure_redsys` step:

   - :guilabel:`Merchant Code (FUC)`: the merchant code. It must only contain digits.
   - :guilabel:`Terminal`: the terminal number, 1 to 3 digits. It is set to ``1`` by default.
   - :guilabel:`Secret Key`: the secret key of the terminal.

#. Configure the remaining options as needed.
#. Set the :guilabel:`State` field to :guilabel:`Enabled` (or :guilabel:`Test Mode` if you want to
   :ref:`test the integration <payment_providers/redsys/test_mode>`).

.. screenshot:: finance-payment-providers-redsys-redsys-credentials
   :menu: Accounting ‣ Configuration ‣ Payment Providers ‣ Redsys ‣ Credentials
   :shows: The Redsys provider form, Credentials tab: Merchant Code (FUC), Terminal, Secret Key.
   :highlight: The Merchant Code (FUC), Terminal and Secret Key fields.
   :data: Fictitious merchant code and terminal 1; the secret key is masked (never use a real key).
   :module: payment_redsys
   :notes: English UI, light theme, 1440px width; developer mode off.

.. important::
   The :guilabel:`Secret Key` is only visible to and editable by users who belong to the
   Settings administrator access group (technical group ``base.group_system``). It is masked on
   screen. The three fields are required as soon as the provider is not disabled. The merchant code
   and the secret key are erased when the database is neutralized (for example, when a production
   database is duplicated for testing), so enter them again on the copy.

Payment methods
---------------

When the module is installed, the :guilabel:`Card`, :guilabel:`Bizum`, :guilabel:`Visa` and
:guilabel:`Mastercard` payment methods are activated for the provider. To
change this, click :guilabel:`Enable Payment Methods` in the :guilabel:`Configuration` tab of the
provider. See :ref:`payment_providers/payment_methods` for more information.

Only the currencies that have an ISO 4217 numeric code are available with Redsys. Amounts are sent
to Redsys in the smallest unit of the currency (for example, cents for the euro).

.. _payment_providers/redsys/test_mode:

Test mode and production
========================

The environment Odoo talks to follows the :guilabel:`State` of the payment provider:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - :guilabel:`State`
     - Redsys environment
   * - :guilabel:`Test Mode`
     - Redsys test environment (``sis-t.redsys.es``).
   * - :guilabel:`Enabled`
     - Redsys production environment (``sis.redsys.es``).

To try the integration without processing real payments:

#. Set the :guilabel:`State` to :guilabel:`Test Mode`.
#. Enter the merchant code, terminal and secret key of your **test** virtual POS in the
   :guilabel:`Credentials` tab.
#. Pay an invoice or an eCommerce order using one of the test cards provided by Redsys in its
   developer documentation.

When you are ready to accept real payments, replace the three credentials with the ones of your
**production** virtual POS, then set the :guilabel:`State` to :guilabel:`Enabled`.

.. warning::
   The test and production environments have different secret keys. Switching the :guilabel:`State`
   without replacing the credentials makes every payment fail with a signature error.

.. tip::
   Every payment gets its own random order number, so a duplicated test database and your
   production database can safely share a terminal. Still, use the test mode on a duplicate or test
   database, as recommended in :ref:`payment_providers/test-mode`.

How payments are processed
==========================

#. The customer selects Redsys (or Bizum) on the payment form and clicks :guilabel:`Pay`.
#. Odoo generates a unique **order number** of 12 characters for the transaction: 4 digits followed
   by 8 digits or capital letters. It identifies the payment in the Redsys administration portal
   and is stored in the :guilabel:`Redsys Order Number` field of the transaction. It is also used
   as the provider reference.
#. The customer is redirected to the Redsys payment page, where they pay and, if required by their
   bank, authenticate.
#. Redsys sends a signed notification to Odoo, and brings the customer back to the payment status
   page of your database. The notification is the reference for the payment result; the customer
   return is only used if it carries the signed data.
#. The state of the transaction is derived from the Redsys response code (``Ds_Response``):

   .. list-table::
      :header-rows: 1
      :widths: 30 70

      * - Response code
        - Transaction state
      * - 0000 to 0099
        - Done (payment authorized)
      * - 9915
        - Canceled (payment canceled by the customer)
      * - 8210, 8220, 9997, 9998, 9999
        - Pending (operation still in progress, e.g. authentication)
      * - Any other code
        - Error, with the reason shown when known, followed by the Redsys code

Odoo also checks that the amount and the currency reported by Redsys match those of the
transaction; if they do not, the transaction is set to error.

.. _payment_providers/redsys/bizum:

Bizum
=====

`Bizum <https://bizum.es/>`_ lets customers in Spain pay from their bank's mobile app, using their
phone number. It is processed by the same Redsys virtual POS.

To offer it, make sure Bizum is enabled on your Redsys virtual POS, and that the :guilabel:`Bizum`
payment method is activated on the Redsys provider (see :ref:`payment_providers/payment_methods`).

.. note::
   - :guilabel:`Bizum` is only offered for payments in :guilabel:`EUR` from :guilabel:`Spain`, as
     configured on the payment method.
   - When the customer selects Bizum, the Redsys payment page is restricted to Bizum. When a payment
     is reported by Redsys as made with Bizum, the payment method of the transaction is set to
     :guilabel:`Bizum`.
   - Bizum does not support saving payment methods or express checkout.

.. _payment_providers/redsys/refunds:

Refunds
=======

Full and partial :ref:`refunds <payment_providers/refunds>` can be made directly from Odoo, for card
and Bizum payments. To refund a payment, navigate to it and click the :guilabel:`Refund` button, as
explained in :ref:`payment_providers/refunds`.

Odoo sends the refund request to Redsys immediately and the refund transaction is set to done when
Redsys approves it (response code 900). If Redsys declines it (for example, *Refund not allowed*)
or cannot be reached, the refund transaction is set to error with the reason.

.. note::
   Refunds are always based on the Redsys order number of the original payment, and use the same
   currency. Redsys applies its own limits on refunds (for example, the refunded total cannot exceed
   the original amount).

.. _payment_providers/redsys/troubleshooting:

Troubleshooting
===============

The technical details of every payment and notification are written in the server logs. The
following situations are the most common.

The message is signed with an unsupported version
-------------------------------------------------

Odoo rejects the notification or the response with the message *The message is signed with version
HMAC_SHA256_V1, but only HMAC_SHA512_V2 is supported. Configure the terminal to use
HMAC_SHA512_V2.* Change the signature type of your terminal to HMAC_SHA512_V2 in the Redsys
administration portal, or ask your bank to do it.

Invalid signature
---------------------------------------------------

- Check that the :guilabel:`Secret Key` matches the environment set in the :guilabel:`State`
  (test or production) and the terminal entered in the :guilabel:`Terminal` field.
- Check that there are no leading or trailing spaces in the credentials.
- Make sure the notifications can reach your database: it must be publicly reachable on its base
  URL and not behind a firewall or proxy that blocks requests coming from Redsys.

Notifications with a missing or invalid signature are ignored, and the transaction is not updated.

Redsys rejects the payment page
-------------------------------

- The merchant code must match the environment and the terminal must exist on your virtual POS
  (*Merchant not registered in FUC*).
- *Duplicated order* means Redsys already knows the order number. Order numbers are generated
  randomly; try the payment again.
- Redsys may refuse a currency that your bank has not enabled on your terminal. Ask your bank if
  you use anything other than the euro.

Currency and amount errors
--------------------------

- *The currency ... has no ISO 4217 numeric code*: the currency is not supported by Redsys. Use
  another currency, such as the euro.
- *The amount received ... does not match the transaction amount* or *The currency received ... does
  not match*: the transaction is set to error because the data returned by Redsys differ from the
  request. Check the payment in the Redsys administration portal before doing anything else.

The customer paid but the transaction is not confirmed
------------------------------------------------------

The transaction is updated by the server-to-server notification. If it is missing, check the
Redsys administration portal for the order number stored in the :guilabel:`Redsys Order Number`
field of the transaction, and the server logs for the notification. The order number is reported
in the logs when no matching transaction is found.

A transaction is set to error
-----------------------------

The reason is shown on the transaction and in the chatter of the related document. It contains the
Redsys response code, for example *Insufficient funds. (Redsys code 0116)*.

.. seealso::
   - :doc:`../payment_providers`
   - :doc:`../fiscal_localizations/spain`

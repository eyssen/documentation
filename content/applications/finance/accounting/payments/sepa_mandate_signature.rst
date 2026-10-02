===============================
Sign SEPA direct debit mandates
===============================

A SEPA direct debit can only be collected with a :ref:`mandate <accounting/payment-orders/mandates>`
signed by the customer. Instead of printing the form, waiting for the scan and typing the mandate,
you can let the customer sign it online with eYssen Sign: the customer enters the account to debit,
confirms with a one-time code and signs on screen. The mandate is then created as **valid**, ready
for the next :ref:`debit order <accounting/payment-orders/debit>`, with the signed document and the
evidence of the signature attached.

.. note::
   The feature is provided by the *SEPA Mandate Online Signature* module, which needs the
   *eYssen Sign* and *Account Banking SEPA Direct Debit* modules. :ref:`Install
   <general/install>` it from the :guilabel:`Apps` menu.

.. _accounting/payment-orders/mandate-signature-prerequisites:

Prerequisites
=============

- The :guilabel:`SEPA Creditor Identifier` of the *company* is set in :menuselection:`Accounting
  --> Configuration --> Settings` (see :ref:`SEPA identifiers
  <accounting/payment-orders/configuration>`). It is printed on the mandate. Even if you use one
  identifier per payment mode, the company needs one to send a mandate; otherwise sending stops
  with *Set the SEPA creditor identifier of ... first*.
- The customer has an email address (or a contact with an email address, which is used when the
  customer has none). The one-time code and the link are sent there.
- To send the code by text message, the mobile number of the customer must be set and your database
  needs SMS credits (see :ref:`two-factor authentication <sign/2fa>`).
- The address of your company is printed on the mandate as the address of the creditor: check that
  it is filled in.

Send a mandate to a customer
============================

#. Open the contact of the customer, click the :guilabel:`Actions` (gear) menu, and select
   :guilabel:`Send SEPA Mandate for Signature`. The action is available to users who can create
   invoices.
#. Check the :guilabel:`Customer` and, in a multi-company database, the :guilabel:`Company` that
   will collect the debits.
#. Select the :guilabel:`Scheme`: :guilabel:`Basic (CORE)` or :guilabel:`Enterprise (B2B)`, and
   the :guilabel:`Type`: :guilabel:`Recurrent` or :guilabel:`One-Off`, as for a
   :ref:`manual mandate <accounting/payment-orders/mandates>`. A note reminds you that a B2B mandate
   must also be confirmed by the customer to their own bank before the first debit.
#. In :guilabel:`One-time Code`, select how the customer receives the code that confirms their
   identity: :guilabel:`Email`, :guilabel:`SMS` or :guilabel:`Email & SMS`.
#. Click :guilabel:`Send`.

.. screenshot:: accounting-sepa-mandate-sign-wizard
   :menu: Contacts ‣ (a customer) ‣ Actions ‣ Send SEPA Mandate for Signature
   :shows: The "Send SEPA Mandate for Signature" dialog with the customer, the company, the Scheme "Basic (CORE)", the Type "Recurrent" and the One-time Code "Email", with the Send button.
   :highlight: The Scheme, Type and One-time Code fields.
   :data: Demo customer with an email address, company with a SEPA creditor identifier.
   :module: sign_sepa_mandate
   :notes: English UI, light theme, crop to the dialog.

Odoo reserves the mandate reference, generates a one-page mandate form in the language of the
customer (creditor, creditor identifier, mandate reference, scheme text, type of payment) and sends
the signature request. The signature request opens on screen; it is also listed under
:menuselection:`eYssen Sign --> Sign Requests`, with the reference *SEPA mandate* followed by the
mandate reference.

What the customer does
======================

The customer receives an email with a link to the mandate and:

#. fills in their name, address, postal code, city, country, the :guilabel:`Account number (IBAN)`,
   the BIC (optional), the place and the date. The IBAN is checked before the signature: an invalid
   number is refused with the message *The IBAN ... is not valid. Please check it.*;
#. enters the six-digit code received by email and/or SMS. The code is valid for 10 minutes and the
   signer has three attempts;
#. signs on screen.

Customers with a portal account can also sign without waiting for an email: on their portal home
page, the :guilabel:`Direct debit` tile (*Sign a SEPA direct debit mandate to pay by bank debit*)
opens the signing page, at the address ``/my/sepa_mandate``. Add ``?scheme=B2B`` to the address to
offer a business (B2B) mandate. The portal mandate is recurrent, for the current company,
and the customer has to sign in first. A request that is still open is reused instead of creating
a new one.

Result and evidence
===================

When the customer has signed, the following is done automatically:

- the customer's bank account is found by IBAN, or created (with the bank of the BIC when given);
- a mandate is created and validated, in the state :guilabel:`Valid`, with the reference, scheme
  and type of the request. The :guilabel:`Date of Signature of the Mandate` is the date of the
  signature in the time zone of the customer (or of your company when the customer has none), and
  the :guilabel:`Sequence Type for Next Debit` of a recurrent mandate is :guilabel:`First`;
- the signed PDF is stored as the :guilabel:`Scan of the Mandate` and attached to the mandate;
- an evidence file named *<mandate reference>_evidence.json* is attached to the mandate;
- a message in the chatter of the mandate confirms the online signature.

The mandate form has an :guilabel:`Online Signature` field that opens the signature request. On the
request, the :guilabel:`SEPA Mandate` tab shows the debtor, creditor, reference, scheme, type and
the mandate created, and :guilabel:`Verify Document` checks the audit log and the document hash
again (see :ref:`Audit & verification <sign/audit>`).

The evidence file (JSON) contains:

- the request, the mandate reference, the creditor and its creditor identifier, the debtor, the
  scheme and the type;
- how the signer was identified (one-time code by email, SMS or both);
- for each signer: name, email, signature time in UTC, IP address and whether the code was
  verified;
- the SHA-256 hash of the signed document;
- the complete audit log with the hash of each entry, and whether the hash chain is valid.

.. warning::
   Whether a simple electronic signature confirmed by a one-time code is enough for your bank, and
   as evidence if a customer claims a refund of a debit they did not authorise (possible for 13
   months), has to be confirmed with your bank and your advisers. Keep the signed PDF and the
   evidence file for as long as you collect with the mandate.

Then use the mandate
====================

The mandate is proposed on the customer's invoices whose payment mode is :guilabel:`SEPA Direct
Debit for customers`, so the customer is collected with the next debit order. With the
*Subscriptions - SEPA Direct Debit* module, it is also proposed on the customer's new
:doc:`subscription contracts <../../../sales/subscriptions/automatic_payments>`.

.. seealso::
   - :doc:`payment_orders`
   - :ref:`Two-factor authentication of Sign <sign/2fa>`

=======
Romania
=======

Configuration
=============

:ref:`Install <general/install>` the following modules to get all the features of the Romanian
localization.

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Romania - Accounting`
     - `l10n_ro`
     - Default :ref:`fiscal localization package <fiscal_localizations/packages>`: chart of
       accounts, taxes and the :guilabel:`NRC` (trade register number) field on contacts.
   * - :guilabel:`Romania - E-invoicing`
     - `l10n_ro_edi`
     - Sends customer invoices in the CIUS-RO (UBL) format to the ANAF *SPV* platform (E-Factura).
       Installed automatically for Romanian companies.
   * - :guilabel:`Romania - Synchronize E-Factura`
     - `l10n_ro_efactura_synchronize`
     - Imports the vendor bills received in the SPV into a purchase journal.
   * - :guilabel:`Romania - E-Transport`
     - `l10n_ro_edi_stock`
     - Declares transports of goods to the ANAF e-Transport system from delivery orders and
       receipts (UIT code).
   * - :guilabel:`Romania - CPV Code`
     - `l10n_ro_cpv_code`
     - Adds the CPV (Common Procurement Vocabulary) code to products, required on some E-Factura
       lines.

.. note::
   The Romanian SAF-T export (**D.406 declaration**) is **not** available in this edition.

.. seealso::
   :doc:`Documentation on e-invoicing’s legality and compliance in Romania
   <../accounting/customer_invoices/electronic_invoicing/romania>`

Company
-------

In :menuselection:`Settings --> General Settings --> Companies --> Update Info`, fill in the
company's :guilabel:`Tax ID` (CUI, with the `RO` prefix for VAT-registered companies) and, in the
company's contact form, the :guilabel:`NRC` (*Număr de ordine în Registrul Comerțului*).

E-Factura
=========

Connection to the SPV
---------------------

Odoo sends the invoices to the ANAF *Spațiul Privat Virtual* (SPV) with the company's own OAuth
credentials. In :menuselection:`Accounting --> Configuration --> Settings --> Romanian E-Factura`:

#. Register an application on the ANAF developer portal with the :guilabel:`Callback URL` shown in
   the settings block, and copy the resulting :guilabel:`Client ID` and :guilabel:`Client Secret`
   into the corresponding fields.
#. Keep :guilabel:`Use Test Environment` enabled while testing; disable it for production.
#. Click :guilabel:`Generate Token` and log in with the company's ANAF certificate. The
   :guilabel:`Access Token` and :guilabel:`Refresh Token` and their expiry dates are then filled in
   automatically; the token is refreshed by a scheduled action before it expires.

.. screenshot:: finance-fl-romania-efactura-settings
   :menu: Accounting ‣ Configuration ‣ Settings ‣ Romanian E-Factura
   :shows: The "Romanian E-Factura" settings block with the Callback URL, "Client ID", "Client Secret", the "Generate Token" button, the access/refresh token expiry dates and the "Use Test Environment" checkbox.
   :highlight: The "Generate Token" button.
   :data: Demo company "YourCompany RO", Romanian localization installed; test environment, throw-away credentials.
   :module: l10n_ro_edi
   :notes: English UI, light theme, 1440px width; use a throw-away secret.

Sending invoices
----------------

Once an invoice is posted, open :guilabel:`Send & Print` and keep the :guilabel:`Send E-Factura to
SPV` option enabled: the CIUS-RO XML is generated, attached to the invoice and uploaded to the SPV. The
:guilabel:`E-Factura Status` field of the invoice then shows :guilabel:`Sent`; click
:guilabel:`Fetch status` (or wait for the scheduled action) to retrieve the ANAF answer, which
sets the status to :guilabel:`Validated` or :guilabel:`Error`. The validated document (signed XML
and ZIP) can be downloaded from the :guilabel:`E-Factura` tab of the invoice, and errors are
logged in the chatter.

.. screenshot:: finance-fl-romania-efactura-invoice
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (a sent invoice) ‣ E-Factura tab
   :shows: A posted customer invoice with the "E-Factura Status" field showing "Validated", the "Fetch status" button and the E-Factura tab listing the sent document with its index and the "Download" button.
   :highlight: The "E-Factura Status" field.
   :data: Demo company "YourCompany RO", invoice INV/2025/00003 validated in the test SPV.
   :module: l10n_ro_edi
   :notes: English UI, light theme, 1440px width.

Receiving vendor bills
----------------------

With the *Romania - Synchronize E-Factura* module, select the purchase journal in
:guilabel:`Import Vendor Bills in` in the same settings block. The scheduled action
:guilabel:`E-Factura: Synchronize with ANAF` then downloads the invoices addressed to the company in
the SPV and creates draft vendor bills from them in that journal.

E-Transport
===========

The *Romania - E-Transport* module declares the transport of goods to the ANAF e-Transport system
directly from the transfer. On a delivery order or receipt, the :guilabel:`Transport` tab holds the
required data: operation type and scope, :guilabel:`Vehicle Number` (and trailers), the start and
end location types, border crossing point or customs office where applicable, and the carrier's
partner set on the delivery method. Click :guilabel:`Send eTransport` to obtain the :guilabel:`UIT`
code, :guilabel:`Fetch Status` to update the :guilabel:`eTransport Status`, and :guilabel:`Amend
eTransport` to send a correction. The UIT is printed on the delivery slip.

.. screenshot:: finance-fl-romania-etransport-picking
   :menu: Inventory ‣ Operations ‣ Deliveries ‣ (a delivery order) ‣ Transport tab
   :shows: A validated delivery order with the "Send eTransport" and "Fetch Status" buttons in the header and the Transport tab: operation type, vehicle number, start/end location types and the returned "UIT" code with the "eTransport Status" = Validated.
   :highlight: The "UIT" field.
   :data: Demo company "YourCompany RO", delivery WH/OUT/00012, vehicle B123ABC.
   :module: l10n_ro_edi_stock
   :notes: English UI, light theme, 1440px width.

CPV codes
=========

The *Romania - CPV Code* module adds a :guilabel:`CPV Code` field to the product form (General
Information tab). Set it on the products sold to public institutions, so that the code is included
in the E-Factura lines when required.

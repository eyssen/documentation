=====
Spain
=====

Configuration
=============

Install the 🇪🇸 **Spanish** :doc:`fiscal localization package <../fiscal_localizations>` to get all
the default accounting features of the Spanish localization.

Three **Spanish** localizations exist, each with its own pre-configured **PGCE** charts of accounts:

- Spain - SMEs (2008);
- Spain - Complete (2008);
- Spain - Non-profit entities (2008).

To select the one to use, go to :menuselection:`Accounting --> Configuration --> Settings` and
select a package in the :guilabel:`Fiscal Localization` section.

.. warning::
   You can only change the accounting package as long as you have not created any accounting entry.

.. seealso::
   - :doc:`Documentation on e-invoicing’s legality and compliance in Spain
     <../accounting/customer_invoices/electronic_invoicing/spain>`
   - :doc:`Documentation on e-invoicing’s legality and compliance in the Basque Country
     <../accounting/customer_invoices/electronic_invoicing/basque_country>`

Chart of accounts
=================

You can reach the **Chart of Accounts** by going to :menuselection:`Accounting --> Configuration -->
Accounting: Chart of Accounts`.

.. tip::
    When a new database is created for a Spanish company, **Spain - SMEs (2008)** is installed by
    default.

Taxes
=====

Default Spain-specific taxes are created automatically when the
:guilabel:`Spanish - Accounting (PGCE 2008) (l10n_es)` module is installed. Each tax is mapped to
the boxes of the Spanish **Modelo 303** VAT return, which can be reviewed in the :doc:`tax report
<../accounting/reporting/dynamic_reports>`.

.. note::
   The Spain-specific statement reports (Balance Sheet (ES), Profit & Loss (ES), EC Sales List,
   and the Modelo 111 / 115 / 130 / 303 / 347 / 349 / 390 tax reports with their AEAT export) are
   **not** available in this edition; use the generic :doc:`financial reports
   <../accounting/reporting>` and the tax grids instead.


.. _localizations/spain/sii:

SII (Suministro Inmediato de Información)
=========================================

The *Spain - SII EDI Suministro de Libros* (`l10n_es_edi_sii`) module sends the VAT information of
customer invoices and vendor bills to the SII (*Llevanza de libros registro*) of the AEAT or of the
regional tax agencies. It is mandatory for companies with a turnover above 6 M€ and optional for
the others.

Configuration
-------------

#. :ref:`Install <general/install>` the :guilabel:`Spain - SII EDI Suministro de Libros
   (l10n_es_edi_sii)` module.
#. Go to :menuselection:`Accounting --> Configuration --> Settings`, scroll to the
   :guilabel:`Registro de Libros connection SII` setting and select the :guilabel:`Tax Agency for
   SII` (:guilabel:`Agencia Tributaria española`, :guilabel:`Hacienda Foral de Gipuzkoa`,
   :guilabel:`Hacienda Foral de Bizkaia`, or :guilabel:`Hacienda Foral de Navarra`).
#. Click the :guilabel:`Certificate (SII)` link to upload the company's digital certificate (file
   and password) used to sign the requests.
#. Keep :guilabel:`SII Test Mode` enabled while testing; disable it to send the data to the
   production web service.
#. On each sales and purchase journal that must report to the SII, enable the :guilabel:`SII IVA
   Llevanza de libros registro (ES)` format in the :guilabel:`Electronic invoicing` field of the
   :guilabel:`Advanced Settings` tab.

.. screenshot:: finance-fl-spain-sii-settings
   :menu: Accounting ‣ Configuration ‣ Settings ‣ Registro de Libros connection SII
   :shows: The "Registro de Libros connection SII" setting with the "Certificate (SII)" link, the "Tax Agency for SII" drop-down set to "Agencia Tributaria española" and the "SII Test Mode" checkbox enabled.
   :highlight: The "Tax Agency for SII" field.
   :data: Demo company "YourCompany ES", Spanish localization installed; test certificate.
   :module: l10n_es_edi_sii
   :notes: English UI, light theme, 1440px width; use a throw-away certificate.

Taxes
-----

The Spanish taxes carry a :guilabel:`Tax Type (Spain)` (:guilabel:`Sujeto`, :guilabel:`Exento`,
:guilabel:`Sujeto ISP`, :guilabel:`No Sujeto`, :guilabel:`Retencion`, :guilabel:`Recargo de
Equivalencia`, :guilabel:`DUA`, …), an :guilabel:`Exempt Reason (Spain)` for exempt taxes (E1 … E6) and
the :guilabel:`Bien de Inversion` flag, which determine how the amounts are reported to the SII.
The default taxes are configured; check these fields when creating new taxes.

Sending documents
-----------------

Once a customer invoice or vendor bill is posted in a journal with the SII format enabled, it is
sent to the SII by the scheduled action of the electronic invoicing (or immediately with the
:guilabel:`Process now` link of the blue banner). The status is shown in the
:guilabel:`Electronic invoicing` field; the CSV return code and the acceptance message (or the
errors reported by the agency) are logged in the chatter. The :guilabel:`Registration Date` field
of the document (Other Info tab) is the date reported as *fecha de registro contable* for vendor
bills.

.. _localizations/spain/veri-factu:

Veri*Factu
==========

.. note::
   Producers of Veri*Factu billing systems must self-certify their compliance with the regulations
   (*declaración responsable*). Ask your support provider for the declaration that applies to your
   installation.

**Veri*Factu** is an e-Invoicing system used by the Spanish Tax Agency. It is mandatory for most
taxpayers in Spain, except for those who use the SII system or are under a regional tax regime
(i.e., TicketBai).

Odoo allows :ref:`invoices <localizations/spain/veri-factu-invoices>` and Point of Sale :ref:`orders
<localizations/spain/veri-factu-orders>` to be automatically sent to the tax authorities.

.. _localizations/spain/veri-factu-configuration:

Configuration
-------------

To enable **Veri\*Factu**, follow these steps:

#. Open the Settings app to make sure your company's :guilabel:`Country` and :guilabel:`Tax ID` are
   correctly set in the :ref:`Companies <general/companies/company>` section.
#. :ref:`Install <general/install>` the :guilabel:`Spain - Veri*Factu (l10n_es_edi_verifactu)`
   module.
#. Go to :menuselection:`Accounting --> Configuration --> Settings`, scroll to the
   :guilabel:`Veri\*Factu` section, check the :guilabel:`Enable Veri*Factu` option, and click
   :icon:`oi-arrow-right` :guilabel:`Manage certificates` to add a certificate.
#. In the :guilabel:`Certificates for Veri\*Factu` list view, click :guilabel:`New`.
#. Click :guilabel:`Upload your file`, then select a certificate file and enter the
   :guilabel:`Password` needed to open the certificate (if there is one).

.. note::
   - At least one certificate has to be uploaded.
   - By default Veri*Factu is in testing mode. The data is sent to test servers
     and is not considered official. When official data can be sent to the production servers, go to
     the :guilabel:`Veri\*Factu` section in the :guilabel:`Settings` and disable :guilabel:`Test
     Environment`.

.. _localizations/spain/veri-factu-invoices:

Invoices
--------

Once an :doc:`invoice <../../finance/accounting/customer_invoices>` is confirmed, it can be
:ref:`sent <accounting/invoice/sending>`. In the :guilabel:`Send` window, the Veri*Factu option is
available if Veri*Factu has been enabled.

Click :guilabel:`Send` to generate a JSON file containing the invoice details. This file is stored
as a Veri*Factu document. In the :guilabel:`Veri*Factu` tab, all corresponding documents are
listed by their creation date and current status.

.. tip::
   To download a JSON file, click on its document in the :guilabel:`Veri*Factu` tab. Then, in
   the :guilabel:`Open: Veri*Factu Documents` window, click the link in the :guilabel:`JSON` field.

.. note::
   - The document should be sent to the :abbr:`AEAT (Agencia Estatal de Administración Tributaria)`
     immediately. However, it may be delayed due to mandatory waiting periods between submissions
     required by the :abbr:`AEAT (Agencia Estatal de Administración Tributaria)`. In such cases,
     the document is automatically sent the next time a scheduled action runs.
   - A Veri\*Factu **QR code** appears on the invoice PDF. Scan this code to verify that the invoice
     has been received and recognized by the :abbr:`AEAT (Agencia Estatal de Administración
     Tributaria)`.

.. _localizations/spain/veri-factu-orders:

Point of sale orders
--------------------

Once an order has been :ref:`paid <pos/sell>`, a JSON file containing the order details is
generated. This file is stored as a Veri*Factu document.

Go to :menuselection:`Point of Sale --> Orders --> Orders`. In the :guilabel:`Orders` list view,
select the relevant order. In the :guilabel:`Veri*Factu` tab, all the corresponding documents are
listed by their creation date and current status.

.. tip::
   To download a JSON file, click on its document in the :guilabel:`Veri*Factu` tab. Then, in
   the :guilabel:`Open: Veri*Factu Documents` window, click the link in the :guilabel:`JSON` field.

.. note::
   - The document should be sent to the :abbr:`AEAT (Agencia Estatal de Administración Tributaria)`
     immediately. However, it may be delayed due to mandatory waiting periods between submissions
     required by the :abbr:`AEAT (Agencia Estatal de Administración Tributaria)`. In such cases,
     the document is automatically sent the next time a scheduled action runs.

If an invoice is generated for an order during the payment process, the Veri*Factu document is
:ref:`created and sent for the invoice <localizations/spain/veri-factu-invoices>` instead.

.. note::
   A Veri\*Factu **QR code** appears on the order receipt, even if an invoice is created for the
   order. Scan this code to verify that the invoice has been received and recognized by the
   :abbr:`AEAT (Agencia Estatal de Administración Tributaria)`

TicketBAI
=========

`Ticket BAI <https://www.gipuzkoa.eus/es/web/ogasuna/ticketbai>`_ or **TBAI** is an e-Invoicing
system used by the Basque government and its three provincial councils (Álava, Biscay, and
Gipuzkoa).

Odoo supports the **TicketBAI (TBAI)** electronic invoicing format for all three regions of the
**Basque Country**. To enable **TicketBAI**, set your company's :guilabel:`Country` and
:guilabel:`Tax ID` under :menuselection:`Settings --> General Settings` in the :guilabel:`Companies`
section.

Then, :ref:`install <general/install>` the module :guilabel:`Spain -TicketBAI (l10n_es_edi_TBAI)`,
go to :menuselection:`Accounting --> Configuration --> Settings`, and select a **region** in the
:guilabel:`Spain Localization` section's :guilabel:`Tax Agency for TBAI` field.

Once a region is selected, click :guilabel:`Manage certificates (SII/TicketBAI)`, then click
:guilabel:`New`, upload the certificate, and enter the password provided by the tax agency.

.. warning::
   If you are testing certificates, enable :guilabel:`Test Mode` in the
   :guilabel:`Spain Localization` section, which can be found under :guilabel:`Accounting` in
   the **Settings** app.

Use case
--------

Once an invoice has been :doc:`created <../../finance/accounting/customer_invoices>` and confirmed,
a TicketBAI **banner** appears at the top.

.. screenshot:: finance-fl-spain-ticketbai-invoice
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (a sent invoice)
   :shows: A posted invoice of a Basque company with the blue TicketBAI banner at the top stating that the invoice was sent to the tax agency, and the TicketBAI status.
   :highlight: The TicketBAI banner.
   :data: Demo company "YourCompany ES" (Bizkaia), TicketBAI test mode.
   :module: l10n_es_edi_tbai
   :notes: English UI, light theme, 1440px width.

Odoo sends invoices through TicketBAI automatically every **24 hours**. However, you can click
:guilabel:`Process now` to send the invoice immediately.

When the invoice is **sent**, the status of the field :guilabel:`Electronic Invoice` changes to
:guilabel:`Sent`, and the XML file can be found in the **chatter**. Under the
:guilabel:`EDI Documents` tab, you can see the traceability of other generated documents related to
the invoice (e.g., if the invoice should also be sent through the **SII**, it will appear here).

.. note::
   The TBAI **QR code** is displayed on the invoice PDF.

   .. screenshot:: finance-fl-spain-qr-code
      :menu: Accounting ‣ Customers ‣ Invoices ‣ (a sent invoice) ‣ Print
      :shows: The printed invoice PDF with the TicketBAI QR code and TBAI identifier in the footer.
      :highlight: The QR code.
      :data: Demo company "YourCompany ES" (Bizkaia).
      :module: l10n_es_edi_tbai
      :notes: English UI, light theme, 1440px width.

FACe
====

`FACe <https://face.gob.es/en>`_ is the e-Invoicing platform used by the public administrations in
Spain to send electronic invoices.

Before configuring the :abbr:`FACe (General Entrance for Electronic Invoices)` system,
:ref:`install <general/install>` the :guilabel:`Spain - Facturae EDI (l10n_es_edi_facturae)` module
and other **Facturae EDI**-related modules.

To configure FACe, follow these steps:

#. Go to :menuselection:`Accounting --> Configuration --> Certificates`.
#. Click :guilabel:`New` to create a new certificate.
#. Complete the fields, including uploading the file of the :guilabel:`Certificate` provided by the
   tax agency and the provided :guilabel:`Certificate Password`.

.. note::
   If using the Invoicing app instead of Accounting, go to :menuselection:`Invoicing -->
   Configuration --> Certificates`.

Use case
--------

Once you have :doc:`created <../../finance/accounting/customer_invoices>` an invoice and confirmed
it, click :guilabel:`Send & Print`. Make sure :guilabel:`Generate Facturae edi file` is enabled, and
click :guilabel:`Send & Print` again. Once the invoice is sent, the generated XML file is available
in the **chatter**.

.. warning::
   The file is **NOT** automatically sent. You have to send it yourself manually.

.. tip::
   You can send **FACe** XML files in batch through `the governmental portal <https://www.facturae.gob.es/formato/Paginas/descarga-aplicacion-escritorio.aspx>`_.

Administrative centers
----------------------

In order for **FACe** to work with **administrative centers**, the invoice *must* include specific
data about the centers.

.. note::
   Make sure to have the :guilabel:`Spain - Facturae EDI - Administrative Centers Patch
   (l10n_es_edi_facturae_adm_centers)` module :ref:`installed <general/install>`.

To add **administrative centers**, create a new **contact** to add to the **partner** company.
Select :guilabel:`FACe Center` as the **type**, assign one or more **role(s)** to that contact, and
:guilabel:`Save`. The **three** roles usually required are:

- Órgano gestor: :guilabel:`Receptor` (Receiver);
- Unidad tramitadora: :guilabel:`Pagador` (Payer);
- Oficina contable: :guilabel:`Fiscal` (Fiscal).

.. screenshot:: finance-fl-spain-administrative-center
   :menu: Contacts ‣ (a public entity) ‣ Administrative Centers
   :shows: The contact form of a public administration with the "Administrative Centers" section: a center with its "Center Code" (DIR3), role (Órgano gestor / Unidad tramitadora / Oficina contable) and address.
   :highlight: The administrative center lines.
   :data: Public entity "Ayuntamiento de Ejemplo", 3 DIR3 codes.
   :module: l10n_es_edi_facturae
   :notes: English UI, light theme, 1440px width.

.. tip::
   - If administrative centers need different :guilabel:`Codes` per role, you *must* create
     different centers for each role.
   - When an electronic invoice is created using a partner with **administrative centers**, *all*
     administrative centers are included in the invoice.
   - You can add one contact with multiple roles or multiple contacts with a different role each.

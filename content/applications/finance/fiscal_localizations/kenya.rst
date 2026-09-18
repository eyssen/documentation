=====
Kenya
=====

.. _localization/kenya/configuration:

Configuration
=============

Install the 🇰🇪 **Kenyan** :ref:`fiscal localization package <fiscal_localizations/packages>` to get
all the features of the Kenyan localization.

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Kenya - Accounting`
     - `l10n_ke`
     - Default :ref:`fiscal localization package <fiscal_localizations/packages>`: chart of
       accounts, taxes with their KRA item codes, tax grids, and withholding certificate fields on
       vendor bills.
   * - :guilabel:`Kenya Tremol Device EDI Integration`
     - `l10n_ke_edi_tremol`
     - Sends customer invoices and credit notes to a **Tremol G03** control unit device, which
       signs them and transmits them to the :abbr:`KRA (Kenya Revenue Authority)` through TIMS.

.. note::
   The eTIMS integration with an :abbr:`OSCU (Online Sales Control Unit)` (device initialization,
   eTIMS product and stock registration, purchases and imports synchronization, KRA sequences) and
   the Kenyan payroll are **not** available in this edition. Fiscalization is done through a
   Tremol G03 control unit as described below.

Taxes
=====

The Kenyan taxes carry a :guilabel:`KRA Item Code` (:menuselection:`Accounting --> Configuration
--> Taxes`, next to the :guilabel:`Country` field), which identifies the tax type towards the KRA
(exempted, zero rated, or taxable at the reduced rate). For 0 % and exempt taxes, an item code is
mandatory when the invoice is sent to the fiscal device; the drop-down only proposes the codes
matching the tax rate.

On vendor bills, the :guilabel:`Withholding Certificate Number` and :guilabel:`Date of Certificate`
fields (Other Info tab) record the withholding tax certificate received from the customer.

Tremol G03 fiscal device
========================

The `Kenya Revenue Authority (KRA) <https://www.kra.go.ke/>`_ requires invoices to be signed by a
certified control unit. Odoo integrates with the **Tremol G03** control unit device: the invoice
data is sent to the device, which signs it, stores it, transmits it to the KRA (TIMS) and returns
the control unit invoice number and a QR code that are printed on the invoice.

Proxy server
------------

The Tremol device is connected (by USB or network) to a computer on the same network as the device,
on which a *proxy server* must run. The proxy is a small Odoo server started on that computer (for
example with the Odoo Community Windows installer, *Odoo IoT* type of install, or an Odoo instance
started with the `l10n_ke_edi_tremol` module available) that exposes the device on a local address.

In :menuselection:`Accounting --> Configuration --> Settings --> Tremol Device Settings`, enter the
:guilabel:`Fiscal Device Proxy Address` (by default `http://localhost:8069`) of that proxy server.

.. screenshot:: finance-fl-kenya-tremol-settings
   :menu: Accounting ‣ Configuration ‣ Settings ‣ Tremol Device Settings
   :shows: The "Tremol Device Settings" block of the Accounting settings of a Kenyan company with the "Fiscal Device Proxy Address" field set to http://192.168.1.50:8069.
   :highlight: The "Fiscal Device Proxy Address" field.
   :data: Demo company "YourCompany KE", Kenyan localization installed.
   :module: l10n_ke_edi_tremol
   :notes: English UI, light theme, 1440px width.

Sending invoices to the device
------------------------------

Once a customer invoice or credit note is posted, click :guilabel:`Send To Fiscal Device` in the
header of the invoice. Before sending, Odoo checks that:

- the company is Kenyan and its currency is the Kenyan shilling (KES);
- the document is a posted invoice or credit note that has not been sent yet;
- a credit note references the original invoice, which must already have been sent;
- every line has exactly one VAT tax, and a 0 % or exempt tax has a KRA item code.

After the device has signed the document, the :guilabel:`Kenya CU Invoice Number` is filled in
and the :guilabel:`Tremol GO3 Fiscal Device` tab of the invoice shows the :guilabel:`CU QR Code`,
:guilabel:`CU Serial Number` and :guilabel:`CU Signing Date and Time`. These details and the QR
code are printed on the invoice PDF.

.. screenshot:: finance-fl-kenya-invoice-cu-tab
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (a signed invoice) ‣ Tremol GO3 Fiscal Device tab
   :shows: A posted Kenyan customer invoice with the "Kenya CU Invoice Number" filled in and the "Tremol GO3 Fiscal Device" tab showing the CU QR Code link, CU Serial Number and CU Signing Date and Time.
   :highlight: The "Kenya CU Invoice Number" field.
   :data: Demo company "YourCompany KE", invoice INV/2025/00007 signed by the device.
   :module: l10n_ke_edi_tremol
   :notes: English UI, light theme, 1440px width.

Customers
---------

For tax-exempt customers, enter their :guilabel:`Exemption Number` in the :guilabel:`Kenya
Accounting Details` section of the contact form (Sales & Purchase tab); it is transmitted to the
device with the invoice.

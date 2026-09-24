=====
India
=====

.. _india/installation:

Installation
============

:ref:`Install <general/install>` the following modules to get all the features of the Indian
localization:

.. list-table::
   :header-rows: 1

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Indian - Accounting`
     - `l10n_in`
     - Default :ref:`fiscal localization package <fiscal_localizations/packages>`
   * - :guilabel:`Indian E-invoicing`
     - `l10n_in_edi`
     - :ref:`Indian e-invoicing integration <india/e-invoicing>`
   * - :guilabel:`Indian E-waybill`
     - `l10n_in_edi_ewaybill`
     - :ref:`Indian E-way bill integration <india/e-waybill>`
   * - :guilabel:`Indian E-waybill Stock`
     - `l10n_in_ewaybill_stock`
     - :ref:`E-waybill creation from the Inventory app <india/e-waybill-stock>`
   * - :guilabel:`Indian - Check GST Number Status`
     - `l10n_in_gstin_status`
     - :ref:`Indian Check GST Number Status <india/gstin_status>`
   * - :guilabel:`Indian TDS and TCS`
     - `l10n_in_withholding`
     - :ref:`TDS/TCS threshold alerts and TDS entries <india/tds-tcs>`

.. note::
   The GST return filing (GSTR-1 / GSTR-2B / GSTR-3 exchange with the GST portal) and the Indian
   tax reports (GSTR-1, GSTR-3, Profit and Loss (IN)) are **not** available in this edition. The GST
   grids of the Indian taxes can be reviewed in the :doc:`tax report
   <../accounting/reporting/dynamic_reports>`.

.. screenshot:: finance-fl-india-modules
   :menu: Apps
   :shows: The Apps list filtered on "India", showing the installed Indian localization modules (Indian - Accounting, Indian E-invoicing, Indian E-waybill, Indian E-waybill Stock, Indian - Check GST Number Status, Indian TDS and TCS).
   :data: Demo company "YourCompany IN".
   :module: l10n_in
   :notes: English UI, light theme, 1440px width.

.. _india/e-invoicing:

Indian Configuration
====================

In :menuselection:`Settings --> Users & Companies --> Companies`, add your :guilabel:`PAN` and
:guilabel:`GSTIN`. The PAN is essential for determining the type of taxpayer,
while GSTIN is required for generating e-Invoices and E-waybills.

e-Invoice system
================

Odoo is compliant with the **Indian Goods and Services Tax (GST) e-Invoice system** requirements.

Setup
-----

.. _india/e-invoicing-api:

NIC e-Invoice registration
~~~~~~~~~~~~~~~~~~~~~~~~~~

You must register on the :abbr:`NIC (National Informatics Centre)` e-Invoice portal to get your
**API credentials**. You need these credentials to :ref:`configure your Odoo Accounting app
<india/e-invoicing-configuration>`.

#. Log in to the `NIC e-Invoice portal <https://einvoice1.gst.gov.in/>`_ by clicking
   :guilabel:`Login` and entering your :guilabel:`Username` and :guilabel:`Password`;

   .. note::
      If you are already registered on the NIC portal, you can use the same login credentials.

   .. screenshot:: finance-fl-india-e-invoice-system-login
      :menu: (NIC e-Invoice portal einvoice1.gst.gov.in) ‣ Login
      :shows: The login page of the NIC e-Invoice portal with the Username and Password fields.
      :highlight: The "Login" button.
      :data: Sandbox portal.
      :module: l10n_in_edi
      :notes: English UI, light theme, 1440px width; use throw-away test credentials.

#. From the dashboard, go to :menuselection:`API Registration --> User Credentials --> Create API
   User`;
#. After that, you should receive an :abbr:`OTP (one-time password)` code on your registered mobile
   number. Enter the OTP code and click :guilabel:`Verify OTP`;
#. Select :guilabel:`Through GSP` for the API interface, set :guilabel:`Tera Software Limited` as
   GSP, and type in a :guilabel:`Username` and :guilabel:`Password` for your API. Once it is done,
   click :guilabel:`Submit`.

   .. screenshot:: finance-fl-india-submit-api-registration-details
      :menu: (NIC e-Invoice portal) ‣ API Registration ‣ User Credentials ‣ Create API User
      :shows: The "Create API User" form with "Through GSP" selected, GSP "Tera Software Limited", and the API Username / Password fields, with the "Submit" button.
      :highlight: The GSP selection and the credentials fields.
      :data: Sandbox portal.
      :module: l10n_in_edi
      :notes: English UI, light theme, 1440px width; use throw-away test credentials.

.. _india/e-invoicing-configuration:

Configuration in Odoo
~~~~~~~~~~~~~~~~~~~~~

To enable the e-Invoice service in Odoo, go to :menuselection:`Accounting --> Configuration -->
Settings --> Indian Electronic Invoicing`, and enter the :guilabel:`Username` and
:guilabel:`Password` previously set for the API.

.. screenshot:: finance-fl-india-e-invoice-setup
   :menu: Accounting ‣ Configuration ‣ Settings ‣ Indian Electronic Invoicing
   :shows: The "Indian Electronic Invoicing" settings block with the "Username" and "Password" fields for the NIC API and the "Test environment" checkbox.
   :highlight: The credential fields.
   :data: Demo company "YourCompany IN" (GSTIN 24AAGCC7144L6ZE), Indian localization installed; NIC sandbox credentials.
   :module: l10n_in_edi
   :notes: English UI, light theme, 1440px width; use throw-away test credentials.

.. _india/e-invoicing-journals:

Journals
********

To automatically send e-Invoices to the NIC e-Invoice portal, you must first configure your *sales*
journal by going to :menuselection:`Accounting --> Configuration --> Journals`, opening your *sales*
journal, and in the :guilabel:`Advanced Settings` tab, under :guilabel:`Electronic Data
Interchange`, enable :guilabel:`E-Invoice (IN)` and save.

.. _india/e-invoicing-workflow:

Workflow
--------

.. _india/invoice-validation:

Invoice validation
~~~~~~~~~~~~~~~~~~

Once an invoice is validated, a confirmation message is displayed at the top. Odoo automatically
uploads the JSON-signed file of validated invoices to the NIC e-Invoice portal after some time. If
you want to process the invoice immediately, click :guilabel:`Process now`.

.. screenshot:: finance-fl-india-e-invoice-process
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (a posted invoice)
   :shows: A posted customer invoice with the blue banner at the top "The invoice will be processed asynchronously by the following E-invoicing service : Indian Electronic Invoicing" and the "Process now" link.
   :highlight: The banner and the "Process now" link.
   :data: Demo company "YourCompany IN" (GSTIN 24AAGCC7144L6ZE), Indian localization installed; NIC sandbox credentials.
   :module: l10n_in_edi
   :notes: English UI, light theme, 1440px width.

.. note::
   - You can find the JSON-signed file in the attached files in the chatter.
   - You can check the document's :abbr:`EDI (electronic data interchange)` status under the
     :guilabel:`EDI Document` tab or the :guilabel:`Electronic invoicing` field of the invoice.

.. _india/invoice-pdf-report:

Invoice PDF report
~~~~~~~~~~~~~~~~~~

Once an invoice is validated and submitted, the invoice PDF report can be printed. The report
includes the :abbr:`IRN (Invoice Reference Number)`, :guilabel:`Ack. No` (acknowledgment number) and
:guilabel:`Ack. Date` (acknowledgment date), and QR code. These certify that the invoice is a valid
fiscal document.

.. screenshot:: finance-fl-india-invoice-report
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (an e-invoiced invoice) ‣ Print
   :shows: The printed invoice PDF header showing the IRN, "Ack. No", "Ack. Date" and the e-invoice QR code.
   :highlight: The IRN/QR block.
   :data: Demo company "YourCompany IN" (GSTIN 24AAGCC7144L6ZE), Indian localization installed; NIC sandbox credentials.
   :module: l10n_in_edi
   :notes: English UI, light theme, 1440px width.

.. _india/edi-cancellation:

e-Invoice cancellation
~~~~~~~~~~~~~~~~~~~~~~

If you want to cancel an e-Invoice, go to the :guilabel:`Other info` tab of the invoice and fill out
the :guilabel:`Cancel reason` and :guilabel:`Cancel remarks` fields. Then, click :guilabel:`Request
EDI cancellation`. The status of the :guilabel:`Electronic invoicing` field changes to :guilabel:`To
Cancel`.

.. important::
   Doing so cancels both the :ref:`e-Invoice <india/e-invoicing>` and the :ref:`E-Way bill
   <india/e-waybill>`.

.. screenshot:: finance-fl-india-e-invoice-cancellation
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (an e-invoiced invoice) ‣ Other Info tab
   :shows: The Other Info tab with the "Cancel reason" drop-down and "Cancel remarks" field filled in, and the "Request EDI cancellation" button in the header.
   :highlight: The "Cancel reason" and "Cancel remarks" fields.
   :data: Demo company "YourCompany IN" (GSTIN 24AAGCC7144L6ZE), Indian localization installed; NIC sandbox credentials.
   :module: l10n_in_edi
   :notes: English UI, light theme, 1440px width.

.. note::
   - If you want to abort the cancellation before processing the invoice, then click :guilabel:`Call
     Off EDI Cancellation`.
   - Once you request to cancel the e-Invoice, Odoo automatically submits the JSON-signed file to
     the NIC e-Invoice portal. You can click :guilabel:`Process now` if you want to process the
     invoice immediately.

.. _india/e-invoice-negative-lines:

Management of negative lines in e-Invoices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Negative lines are typically used to represent discounts or adjustments associated with specific
products or global discounts. The government portal prohibits the submission of data with negative
lines, which means they need to be converted based on the HSN code and GST rate. This is done
automatically by Odoo.

.. example::

   Consider the following example:

   +---------------------------------------------------------------------------------------------------+
   |                                     **Product Details**                                           |
   +=======================+==============+==================+==============+==============+===========+
   | **Product Name**      | **HSN Code** | **Tax Excluded** | **Quantity** | **GST Rate** | **Total** |
   +-----------------------+--------------+------------------+--------------+--------------+-----------+
   | Product A             |  123456      |  1,000           |  1           |  18%         |  1,180    |
   +-----------------------+--------------+------------------+--------------+--------------+-----------+
   | Product B             |  239345      |  1,500           |  2           |  5%          |  3,150    |
   +-----------------------+--------------+------------------+--------------+--------------+-----------+
   | Discount on Product A |  123456      |  -100            |  1           |  18%         |  -118     |
   +-----------------------+--------------+------------------+--------------+--------------+-----------+

   Here's the transformed representation:

   +-------------------------------------------------------------------------------------------------------------+
   |                                         **Product Details**                                                 |
   +==================+==============+==================+==============+==============+==============+===========+
   | **Product Name** | **HSN Code** | **Tax Excluded** | **Quantity** | **Discount** | **GST Rate** | **Total** |
   +------------------+--------------+------------------+--------------+--------------+--------------+-----------+
   | Product A        |  123456      |  1,000           |  1           |  100         |  18%         |  1,062    |
   +------------------+--------------+------------------+--------------+--------------+--------------+-----------+
   | Product B        |  239345      |  1,500           |  2           |  0           |  5%          |  3,150    |
   +------------------+--------------+------------------+--------------+--------------+--------------+-----------+

   In this conversion, negative lines have been transformed into positive discounts, maintaining
   accurate calculations based on the HSN Code and GST rate. This ensures a more straightforward and
   standardized representation in the E-invoice records.

.. _india/verify-e-invoice:

GST e-Invoice verification
~~~~~~~~~~~~~~~~~~~~~~~~~~

After submitting an e-Invoice, you can verify if the invoice is signed from the GST e-Invoice system
website itself.

#. Download the JSON file from the attached files. It can be found in the chatter of the related
   invoice;
#. Open the `NIC e-Invoice portal <https://einvoice1.gst.gov.in/>`_ and go to
   :menuselection:`Search --> Verify Signed Invoice`;
#. Select the JSON file and submit it;

   .. screenshot:: finance-fl-india-verify-invoice
      :menu: (NIC e-Invoice portal) ‣ Search ‣ Verify Signed Invoice
      :shows: The "Verify Signed Invoice" page of the NIC portal with the file selector for the JSON file and the "Verify" button.
      :highlight: The file selector.
      :data: Sandbox portal.
      :module: l10n_in_edi
      :notes: English UI, light theme, 1440px width.

   If the file is signed, a confirmation message is displayed.

   .. screenshot:: finance-fl-india-signed-invoice
      :menu: (NIC e-Invoice portal) ‣ Search ‣ Verify Signed Invoice
      :shows: The confirmation message of the NIC portal stating that the uploaded JSON is a valid signed invoice, with the IRN details.
      :highlight: The confirmation message.
      :data: Sandbox portal.
      :module: l10n_in_edi
      :notes: English UI, light theme, 1440px width.

.. _india/e-waybill:

E-Way bill
==========

.. _india/e-waybill-setup:

Setup
-----

Odoo is compliant with the **Indian Goods and Services Tax (GST) E-waybill system** requirements.

.. _india/e-waybill-api:

API registration on NIC E-Way bill
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You must register on the :abbr:`NIC (National Informatics Centre)` E-Way bill portal to create your
**API credentials**. You need these credentials to :ref:`configure your Odoo Accounting app
<india/e-waybill-configuration>`.

#. Log in to the `NIC E-Way bill portal <https://ewaybillgst.gov.in/>`_ by clicking
   :guilabel:`Login` and entering your :guilabel:`Username` and :guilabel:`Password`;
#. From your dashboard, go to :menuselection:`Registration --> For GSP`;
#. Click :guilabel:`Send OTP`. Once you have received the code on your registered mobile number,
   enter it and click :guilabel:`Verify OTP`;
#. Check if :guilabel:`Tera Software Limited` is already on the registered GSP/ERP list. If so, use
   the username and password used to log in to the NIC portal. Otherwise, follow the next steps;

   .. screenshot:: finance-fl-india-e-waybill-gsp-list
      :menu: (NIC E-Way bill portal ewaybillgst.gov.in) ‣ Registration ‣ For GSP
      :shows: The "For GSP" registration page listing the registered GSP/ERP entries with the "Add/New" button.
      :highlight: The "Add/New" button.
      :data: Sandbox portal.
      :module: l10n_in_edi_ewaybill
      :notes: English UI, light theme, 1440px width; use throw-away test credentials.

#. Select :guilabel:`Add/New`, select :guilabel:`Tera Software Limited` as your GSP Name, create a
   :guilabel:`Username` and a :guilabel:`Password` for your API, and click :guilabel:`Add`.

   .. screenshot:: finance-fl-india-e-waybill-registration-details
      :menu: (NIC E-Way bill portal) ‣ Registration ‣ For GSP ‣ Add/New
      :shows: The GSP registration form with "Tera Software Limited" selected as GSP and the API Username / Password fields, with the "Add" button.
      :highlight: The GSP name and credentials fields.
      :data: Sandbox portal.
      :module: l10n_in_edi_ewaybill
      :notes: English UI, light theme, 1440px width; use throw-away test credentials.

.. _india/e-waybill-configuration:

Configuration in Odoo
~~~~~~~~~~~~~~~~~~~~~

To set up the E-Way bill service, go to :menuselection:`Accounting --> Configuration --> Settings
--> Indian Electronic WayBill --> Setup E-Way bill`, and enter your :guilabel:`Username` and
:guilabel:`Password`.

.. screenshot:: finance-fl-india-e-waybill-configuration
   :menu: Accounting ‣ Configuration ‣ Settings ‣ Indian Electronic WayBill
   :shows: The "Indian Electronic WayBill" settings block with "Setup E-Way bill" enabled and the "Username" / "Password" fields.
   :highlight: The credential fields.
   :data: Demo company "YourCompany IN" (GSTIN 24AAGCC7144L6ZE), Indian localization installed; NIC sandbox credentials.
   :module: l10n_in_edi_ewaybill
   :notes: English UI, light theme, 1440px width; use throw-away test credentials.

.. _india/e-waybill-workflow:

Workflow
--------

.. _india/e-waybill-send:

Send an E-Way bill
~~~~~~~~~~~~~~~~~~

To send an E-Way bill, confirm the customer invoice/vendor bill and click :guilabel:`Send E-Way
bill`.

.. screenshot:: finance-fl-india-e-waybill-send-button
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (a posted invoice)
   :shows: A posted customer invoice with the "Send E-Way bill" button in the header.
   :highlight: The "Send E-Way bill" button.
   :data: Demo company "YourCompany IN" (GSTIN 24AAGCC7144L6ZE), Indian localization installed; NIC sandbox credentials.
   :module: l10n_in_edi_ewaybill
   :notes: English UI, light theme, 1440px width.

.. _india/invoice-validation-e-way:

Invoice validation
~~~~~~~~~~~~~~~~~~

Once an invoice/bill has been issued and sent via :guilabel:`Send E-Way bill`, a confirmation
message is displayed.

.. screenshot:: finance-fl-india-e-waybill-process
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (a posted invoice) after "Send E-Way bill"
   :shows: The invoice with the banner "The invoice will be processed asynchronously by the following E-invoicing service : Indian Electronic Way Bill" and the "Process now" link.
   :highlight: The banner.
   :data: Demo company "YourCompany IN" (GSTIN 24AAGCC7144L6ZE), Indian localization installed; NIC sandbox credentials.
   :module: l10n_in_edi_ewaybill
   :notes: English UI, light theme, 1440px width.

.. note::
   - You can find the JSON-signed file in the attached files in the chatter.
   - Odoo automatically uploads the JSON-signed file to the government portal after some time. Click
     :guilabel:`Process now` if you want to process the invoice/bill immediately.

Invoice PDF report
~~~~~~~~~~~~~~~~~~

You can print the invoice PDF report once you have submitted the E-Way bill. The report includes the
**E-Way bill number** and the **E-Way bill validity date**.

.. screenshot:: finance-fl-india-e-waybill-invoice-report
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (an invoice with E-Way bill) ‣ Print
   :shows: The printed invoice PDF showing the E-Way bill number ("Ewaybill No") and date in the header.
   :highlight: The E-Way bill number.
   :data: Demo company "YourCompany IN" (GSTIN 24AAGCC7144L6ZE), Indian localization installed; NIC sandbox credentials.
   :module: l10n_in_edi_ewaybill
   :notes: English UI, light theme, 1440px width.

.. _india/e-waybill-cancellation:

E-Way bill cancellation
~~~~~~~~~~~~~~~~~~~~~~~

If you want to cancel an E-Way bill, go to the :guilabel:`E-Way bill` tab of the related
invoice/bill and fill out the :guilabel:`Cancel reason` and :guilabel:`Cancel remarks` fields. Then,
click :guilabel:`Request EDI Cancellation`.

.. important::
   Doing so cancels both the :ref:`e-Invoice <india/e-invoicing>` (if applicable) and the
   :ref:`E-Way bill <india/e-waybill>`.

.. screenshot:: finance-fl-india-e-waybill-cancellation
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (an invoice with E-Way bill) ‣ Other Info tab
   :shows: The Other Info tab with the E-Way bill "Cancel reason" and "Cancel remarks" fields and the "Request EDI cancellation" button.
   :highlight: The "Cancel reason" and "Cancel remarks" fields.
   :data: Demo company "YourCompany IN" (GSTIN 24AAGCC7144L6ZE), Indian localization installed; NIC sandbox credentials.
   :module: l10n_in_edi_ewaybill
   :notes: English UI, light theme, 1440px width.

.. note::
   - If you want to abort the cancellation before processing the invoice, click :guilabel:`Call Off
     EDI Cancellation`.
   - Once you request to cancel the E-Way bill, Odoo automatically submits the JSON-signed file to
     the government portal. You can click :guilabel:`Process Now` if you want to process the invoice
     immediately.

.. _india/e-waybill-stock:

E-waybill creation from receipts and delivery orders
----------------------------------------------------

.. note::
   Make sure the **E-Way bill Stock** module is :ref:`installed <general/install>` and
   the :ref:`E-Way bill setup <india/e-waybill-setup>` is complete.

To create E-Way bills from :doc:`receipts and deliveries
</applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations>` in the Inventory
app, follow these steps:

#. Go to :menuselection:`Inventory --> Operations --> Deliveries` or :menuselection:`Inventory -->
   Operations --> Receipts` and select an existing delivery order/receipt or create a new one.

#. Click :guilabel:`Create E-waybill/Challan`.

   .. note::
      To create an E-way bill:

      - A delivery order must be in the :guilabel:`Done` state (i.e., validated)
      - A receipt must have the :guilabel:`Ready` or :guilabel:`Done` state.

#. Click :guilabel:`Generate e-Waybill` to validate the E-Way bill and send it to the NIC E-Way
   bill portal.

   .. tip::
      To use the E-Way bill as a challan for goods deliveries without sending it to the NIC
      E-Waybill portal, click :guilabel:`Use as Challan`.

To print the E-waybill or the challan, click the :icon:`fa-cog` :guilabel:`(gear)` icon and select
:icon:`fa-print` :guilabel:`Ewaybill / Delivery Challan`.

.. _india/gstin_status:

Indian Check GSTIN Status
=========================

The :guilabel:`Indian - Check GST Number Status` module allows you to verify the status of a
:abbr:`GSTIN (Goods and Services Tax Identification Number)` directly from Odoo.

To verify the status of a contact's GST number, access the customer's/vendor's form and click
:guilabel:`Check GSTIN Status` next to the :guilabel:`GSTIN` field.

To verify the status of a GST number entered on an invoice/bill, access the invoice/bill and click
the :icon:`fa-refresh` (:guilabel:`refresh`) button next to the :guilabel:`GST Status` field.

.. screenshot:: finance-fl-india-gstin-status-invoice
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (an invoice)
   :shows: A customer invoice form with the "GST Status" field next to the customer, showing the verified status (e.g. "Active") and the refresh button.
   :highlight: The "GST Status" field and its refresh button.
   :data: Demo company "YourCompany IN" (GSTIN 24AAGCC7144L6ZE), Indian localization installed; NIC sandbox credentials.
   :module: l10n_in_gstin_status
   :notes: English UI, light theme, 1440px width.

A notification is displayed to confirm the status update and the GSTIN status and verification date
are logged in the contact's chatter.

.. _india/tds-tcs-threshold:

.. _india/tds-tcs:

TDS/TCS threshold alert
=======================

:abbr:`TDS (tax deducted at source)` and :abbr:`TCS (tax collected at source)` are tax provisions
under Indian law, triggered when transaction amounts exceed specified thresholds. This alert
notifies users when the value of invoices or bills surpasses these limits, prompting the application
of the appropriate TDS/TCS.

To configure Odoo to advise you on when to apply TDS/TCS, set the :guilabel:`TDS/TCS section`
field on the corresponding account in the chart of accounts. Odoo will display a banner suggesting
the TDS/TCS section under which tax might be applicable when recording an invoice or bill.

Configuration
-------------

#. Navigate to :menuselection:`Accounting --> Configuration --> Settings`.
#. In the :guilabel:`Indian Integration` section, enable the :guilabel:`TDS and TCS` feature.
#. Navigate to :menuselection:`Accounting --> Configuration --> Chart of Accounts`.
#. Click :guilabel:`View` on the desired account, and set the :guilabel:`TDS/TCS Section` field.

.. note::
   The TDS/TCS sections are pre-configured with threshold limits. If you need to modify these
   limits, go to :menuselection:`Accounting --> Configuration --> Taxes`. In the :guilabel:`Advanced
   Options` tab, click on the  :icon:`fa-arrow-right` :guilabel:`(internal link)` icon of the
   :guilabel:`Section` field.

   .. screenshot:: finance-fl-india-tds-tcs-section-modify
      :menu: Accounting ‣ Configuration ‣ Taxes ‣ (a TDS tax) ‣ Advanced Options tab
      :shows: A TDS tax form, Advanced Options tab, with the "Section" field and its internal-link arrow; the opened "Section Alert" form shows the section code and the threshold amounts.
      :highlight: The "Section" field and the internal link icon.
      :data: Demo company "YourCompany IN" (GSTIN 24AAGCC7144L6ZE), Indian localization installed; NIC sandbox credentials.
      :module: l10n_in_withholding
      :notes: English UI, light theme, 1440px width.

Applying TCS/TDS on invoices and bills
--------------------------------------

Based on the account used on the customer invoice or vendor bill, Odoo checks the TCS/TDS threshold
limit. If the limit specified in the :guilabel:`TCS/TDS Section` of the account is exceeded, Odoo
displays an alert that suggests applying the appropriate TCS/TDS. The alert will disappear once the
TCS/TDS is applied.

.. screenshot:: finance-fl-india-tcs-warning
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (an invoice above the threshold)
   :shows: A customer invoice with the yellow alert banner suggesting to apply TCS under the section configured on the account, because the partner's aggregate amount exceeds the threshold.
   :highlight: The alert banner.
   :data: Demo company "YourCompany IN" (GSTIN 24AAGCC7144L6ZE), Indian localization installed; NIC sandbox credentials. Customer with PAN ABCPX1234E.
   :module: l10n_in_withholding
   :notes: English UI, light theme, 1440px width.

**TCS** is directly applicable in the tax on the invoice lines. To apply **TDS**, click the
:guilabel:`TDS Entry` smart button on the vendor bill/payment. The popup window allows specifying
the TDS details. Confirm the entry to apply the TDS.

.. screenshot:: finance-fl-india-tds-apply
   :menu: Accounting ‣ Vendors ‣ Bills ‣ (a bill) ‣ TDS Entry
   :shows: The "TDS Entry" pop-up opened from the vendor bill smart button: the TDS section, base amount, TDS tax and amount fields, with the "Create" button.
   :highlight: The TDS tax and amount fields.
   :data: Demo company "YourCompany IN" (GSTIN 24AAGCC7144L6ZE), Indian localization installed; NIC sandbox credentials.
   :module: l10n_in_withholding
   :notes: English UI, light theme, 1440px width.

In Odoo, the aggregate total is calculated for partners sharing the same PAN number, across all
company branches.

.. example::

   .. list-table::
      :header-rows: 1
      :widths: 10 20 10 20 15

      * - **Branch**
        - **Customer**
        - **Invoice**
        - **Transaction Amount (₹)**
        - **PAN Number**
      * - IN - MH
        - XYZ Enterprise - GJ
        - Invoice 1
        - ₹50,000
        - ABCPX1234E
      * - IN - MH
        - XYZ Enterprise - GJ
        - Invoice 2
        - ₹30,000
        - ABCPX1234E
      * - IN - MH
        - XYZ Enterprise - MH
        - Invoice 3
        - ₹40,000
        - ABCPX1234E
      * - IN - DL
        - XYZ Enterprise - GJ
        - Invoice 4
        - ₹20,000
        - ABCPX1234E
      * - IN - GJ
        - XYZ Enterprise - MH
        - Invoice 5
        - ₹60,000
        - ABCPX1234E

   -  **Aggregate total** = 50,000 + 30,000 + 40,000 + 20,000 + 60,000 = ₹200,000
   -  The aggregate total for all customers (XYZ Enterprise - GJ, MH, DL) sharing the PAN number
      ABCPX1234E across all branches is ₹200,000.

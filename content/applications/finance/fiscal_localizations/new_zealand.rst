===========
New Zealand
===========

.. _localizations/new_zealand/modules:

Modules
=======

The following modules related to the New Zealand localization are available:

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Technical name
     - Description
   * - :guilabel:`New Zealand - Accounting`
     - `l10n_nz`
     - Installed by default when the accounting fiscal localization package is set to New Zealand.
       This module also installs the remittance advice report module.
   * - :guilabel:`Australia & New Zealand - UBL PINT`
     - `l10n_anz_ubl_pint`
     - Adds the PINT A-NZ (Peppol) electronic invoice format.

.. note::
   The Employment Hero payroll connector and the EFT batch payment files are **not** available in
   this edition.

.. note::
   The localization’s core modules are installed automatically with the localization. The rest can
   be manually :doc:`installed </applications/general/apps_modules>`.

.. _localizations/new_zealand/loc-specifics:

Localization overview
=====================

- :doc:`../accounting/get_started/chart_of_accounts`: a predefined structure tailored to New
  Zealand accounting standards
- :doc:`../accounting/taxes/fiscal_positions`: automated tax adjustments based on customer or
  supplier registration status
- :ref:`localizations/new_zealand/taxes-gst`
- :ref:`localizations/new_zealand/reporting`

.. _localizations/new_zealand/taxes-gst:

Taxes and GST
-------------

The default taxes impact the :ref:`GST report <localizations/new_zealand/gst-report>` (the
:doc:`tax report <../accounting/reporting/dynamic_reports>` with the GST return boxes).

The standard **Goods and Service Tax** (GST) rate is 15%, but different rates and exemptions exist
for specific categories of goods and services.

.. seealso::
   :doc:`Taxes <../accounting/taxes>`

.. _localizations/new_zealand/tax-mapping:

Tax mapping
~~~~~~~~~~~

Within the New Zealand localization package, tax names encompass the tax rate as an integral part
of their naming convention.

.. seealso::
   :doc:`Taxes documentation <../../../applications/finance/accounting/taxes>`

These are the taxes in Odoo.

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - GST name
     - Description
     - Label on invoices
     - GST Type
   * - 15%
     - Sale (15%)
     - GST Sales (15%)
     - Sales
   * - 15%
     - Purch (15%)
     - GST Purchases (15%)
     - Purchases
   * - 0% EX
     - Zero/Export (0%) Sale
     - Zero Rated (Export) Sales
     - Sales
   * - 0% F
     - Zero/Import (0%) Purch
     - GST Free Purchases
     - Purchases
   * - 0% TPS
     - Purch (Imports Taxable)
     - Purchase (Taxable Imports) - Tax Paid Separately
     - Purchases
   * - 100% ONLY
     - GST Only - Imports
     - GST Only on Imports
     - Purchases

.. _localizations/new_zealand/reporting:

Reporting
---------

.. _localizations/new_zealand/gst-report:

GST report
~~~~~~~~~~

The **Goods and Services Tax (GST) report** is a critical tax reporting requirement for businesses
registered for GST. The GST return is used to report and remit GST to the **Inland Revenue
Department (IRD)**.

The base and tax amounts are collected from the **GST** taxes, which are pre-configured in Odoo to
align with GST Return requirements (Boxes 1-15) through their tax grids. The **GST** taxes can also
be manually configured for special use cases, such as specific GST treatments (e.g., zero-rating
for exported agricultural goods). Once the **GST** setup for each tax is complete, Odoo
automatically categorizes journal items into the appropriate boxes, which are shown in the
:doc:`tax report <../accounting/reporting/dynamic_reports>`.

.. screenshot:: finance-fl-new-zealand-gst-report
   :menu: Accounting ‣ Reporting ‣ Dynamic Reports ‣ Tax Report
   :shows: The tax report of a New Zealand company listing the GST return boxes (Box 5 Total sales and income, Box 6 Zero-rated supplies, … Box 15 GST to pay/refund) with their base and tax amounts.
   :data: Demo company "YourCompany NZ", New Zealand localization installed.
   :module: l10n_nz, account_dynamic_reports
   :notes: English UI, light theme, 1440px width.

.. important::
   The **GST** report is not submitted directly to the **IRD**. Instead, Odoo
   automatically calculates the required values for each section, providing options to audit
   and review the data. Businesses can then submit these values to the `IRD portal
   <https://myir.ird.govt.nz/_/>`_.

.. seealso::
   :doc:`Taxes documentation <../../../applications/finance/accounting/taxes>`

.. _localizations/new_zealand/remittance-advice:

Remittance advice
~~~~~~~~~~~~~~~~~

A remittance advice is a document used as proof of payment to a business. To access it, go to
:menuselection:`Accounting --> Vendors --> Payments` and select the payment(s). Then click
:icon:`fa-print` :guilabel:`Print` and select :guilabel:`Payment Receipt`.

.. screenshot:: finance-fl-new-zealand-remitance-advice-new
   :menu: Accounting ‣ Vendors ‣ Payments ‣ (a payment) ‣ Print ‣ Payment Receipt
   :shows: The printed "Payment Receipt" PDF of a vendor payment used as remittance advice: company header, vendor, payment date, amount and the list of paid bills.
   :data: Vendor payment of 1,500.00 NZD to "Azure Interior".
   :module: account
   :notes: English UI, light theme, 1440px width.

.. _localizations/new_zealand/accounting:

Accounting
==========

.. _localizations/new_zealand/e-invoicing:

E-invoicing
-----------

Odoo allows :ref:`electronic invoicing <accounting/e-invoicing/configuration>` settings to be
configured per contact.

.. screenshot:: finance-fl-new-zealand-peppol-contact-new
   :menu: Accounting ‣ Customers ‣ Customers ‣ (a customer) ‣ Accounting tab
   :shows: The Accounting tab of a partner with the "Electronic Invoicing" section: "eInvoice Format" set to "PINT A-NZ (Peppol)" and the Peppol endpoint fields (Peppol e-address (EAS) = NZBN, Peppol Endpoint).
   :highlight: The "Electronic Invoicing" section.
   :data: Customer "Kiwi Customer Ltd", NZBN 9429041234567.
   :module: account_peppol, l10n_anz_ubl_pint
   :notes: English UI, light theme, 1440px width.

.. important::
   Validating an invoice or credit note for a contact on the PEPPOL network will download a
   compliant XML file that can be manually uploaded to the PEPPOL network. Odoo is currently in the
   process of becoming an access point for the ANZ region.

.. seealso::
   `PEPPOL requirements <https://peppol.org/learn-more/country-profiles/new-zealand/>`_

.. _localizations/new_zealand/XXXXXX:

Industry-specific features
==========================

.. _localizations/new_zealand/starshipit:

.. _localizations/new_zealand/buynow-paylater:

Buy Now, Pay Later solutions
----------------------------

**Buy Now, Pay Later** solutions are popular payment methods for e-shops. Some of these solutions
are available via the `Stripe <https://stripe.com/au/payments/payment-methods>`_ and
`AsiaPay payment <https://www.asiapay.com.au/payment.html#option>`_ providers.

.. seealso::
   - :doc:`AsiaPay Payment Provider documentation <../../../applications/finance/payment_providers/asiapay>`
   - :doc:`Stripe Payment Provider documentation <../../../applications/finance/payment_providers/stripe>`

.. _localizations/new_zealand/pos-terminals:

Point of Sale terminals
-----------------------

To have a direct connection between Odoo and a PoS terminal, a :doc:`Stripe terminal
<../../../applications/sales/point_of_sale/payment_methods/terminals/stripe>` is needed. Odoo
supports the **EFTPOS** payment solution.

.. note::
   A Stripe payment terminal is not needed to use Odoo as the main POS system. The only drawback
   of not using Stripe is that cashiers must manually enter the final payment amount on the
   terminal.

.. seealso::
   - :doc:`Stripe Payment Provider documentation <../../../applications/finance/payment_providers/stripe>`
   - `Stripe.com Dashboard <https://dashboard.stripe.com/login?redirect=%2Fdashboard>`_
   - `Stripe.com Docs: Terminal <https://docs.stripe.com/terminal>`_

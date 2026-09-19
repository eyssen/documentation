=====================
Bill control policies
=====================

.. _purchase/manage_deals/control-bills:

.. |PO| replace:: :abbr:`PO (Purchase Order)`
.. |POs| replace:: :abbr:`POs (Purchase Orders)`

In Odoo's *Purchase* app, the *bill control* policy determines the quantities billed by vendors on
every purchase order (PO), for either ordered or received quantities.

The policy selected in the *Purchase* app settings acts as the default value, and is applied to any
new product created.

Configuration
=============

To configure the *bill control* policy, navigate to :menuselection:`Purchase app --> Configuration
--> Settings`, and scroll down to the :guilabel:`Invoicing` section. Under :guilabel:`Bill Control`,
select either :guilabel:`Ordered quantities` or :guilabel:`Received quantities`. Then, click
:guilabel:`Save`.

.. screenshot:: purchase-control-bills-selected-policy
   :menu: Purchase ‣ Configuration ‣ Settings
   :shows: Settings page scrolled to the "Invoicing" section, with the "Bill Control" field set to
           "Received quantities".
   :highlight: The "Bill Control" setting (red frame).
   :data: Demo company "YourCompany".
   :module: purchase
   :notes: English UI, light theme, 1440px width, crop to the setting block.

- :guilabel:`Ordered quantities`: creates a vendor bill as soon as a |PO| is confirmed. The products
  and quantities in the |PO| are used to generate a draft bill.
- :guilabel:`Received quantities`: a bill is created only *after* part of the total order has been
  received. The products and quantities received are used to generate a draft bill. An error message
  appears if creation of a vendor bill is attempted without receiving anything.

  .. screenshot:: purchase-control-bills-error-popup
     :menu: Purchase ‣ Orders ‣ Purchase Orders ‣ (open a PO) ‣ Create Bill
     :shows: The "Invalid Operation" error pop-up that appears when clicking Create Bill on a PO
             with the "Received quantities" policy before any product has been received.
     :highlight: The error message text.
     :data: Demo company "YourCompany"; a PO with 0 received quantities.
     :module: purchase
     :notes: English UI, light theme, 1440px width.

.. note::
   If a specific product should use a different control policy than selected in the *Purchase* app
   settings, the :guilabel:`Bill Control` policy for that product can be changed from its product
   form.

   To do that, navigate to :menuselection:`Purchase app --> Products --> Products`, and select a
   product. From the product form, click the :guilabel:`Purchase` tab. Under the :guilabel:`Vendor
   Bills` section, modify the selection in the :guilabel:`Control Policy` field.

View a purchase order's billing status
======================================

Once a |PO| is confirmed, its :guilabel:`Billing Status` can be viewed under the :guilabel:`Other
Information` tab on the |PO| form.

To view the :guilabel:`Billing Status` of a |PO|, navigate to :menuselection:`Purchase app -->
Orders --> Purchase Orders`, and select a |PO| to view.

Click the :guilabel:`Other Information` tab, and locate the :guilabel:`Billing Status` field.

.. screenshot:: purchase-control-bills-billing-status
   :menu: Purchase ‣ Orders ‣ Purchase Orders ‣ (open a PO) ‣ Other Information
   :shows: The "Other Information" tab of a confirmed PO, with the "Billing Status" field visible.
   :highlight: The "Billing Status" field (red frame).
   :data: Demo company "YourCompany"; a confirmed PO with the status "Waiting Bills".
   :module: purchase
   :notes: English UI, light theme, 1440px width.

The table below details the different values the :guilabel:`Billing Status` field could read, and
when they are displayed, depending on the *Bill Control* policy used.

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Billing Status
     - On received quantities
     - On ordered quantities
   * - Nothing to Bill
     - PO confirmed; no products received
     - *Not applicable*
   * - Waiting Bills
     - All/some products received; bill not created
     - PO confirmed
   * - Fully Billed
     - All/some products received; draft bill created
     - Draft bill created

.. seealso::
   :doc:`manage`

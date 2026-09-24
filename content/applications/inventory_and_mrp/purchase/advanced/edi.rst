==================================
EDI purchase-to-sales order import
==================================

.. |EDI| replace:: :abbr:`EDI (Electronic Data Exchange)`
.. |PO| replace:: :abbr:`PO (purchase order)`
.. |SO| replace:: :abbr:`SO (sales order)`

Electronic data interchange (EDI) enables companies using different software systems to exchange
information in a standardized, structured format.

In Odoo, a *purchase order* (PO) can be exported as an XML file and imported as a *sales order* (SO)
into another Odoo database, removing the need for manual entry of products, quantities, prices, and
other key information.

The workflow in this document describes how buyers and sellers exchange data directly between their
Odoo databases. As an alternative, sellers can receive a PDF version of the request for quotation
(RFQ) by email and :ref:`upload it directly in their Sales dashboard
<purchase/advanced/rfq-upload>`. **This method is simpler** but does not use the XML-based exchange
described in the document.

.. note::
   Exported XMLs follow the `UBL schema
   <https://docs.peppol.eu/poacc/upgrade-3/syntax/Order/tree/>`_. When exchanging data between two
   Odoo databases, this schema remains compatible.

   However, implementing custom developments for software that does not support the UBL schema may
   introduce additional complexity.

Roles and configuration
=======================

To facilitate the |EDI| workflow, two companies are involved: the buyer (the company placing the
order) and the seller (the company fulfilling the order). Each company has specific roles and
configurations.

Buyer database
--------------

The buyer database is responsible for creating and confirming purchase orders. Prerequisites
include:

#. (required) :ref:`installing <general/install>` the **Purchase** app
#. (optional) adding vendors (the sellers in this workflow) as :doc:`portal users
   <../../../general/users/portal>`.

Seller database
---------------

The seller database is responsible for receiving and processing sales orders. The only prerequisite
is :ref:`installing <general/install>` the **Sales** app.

Workflow
========

Buyer's process
---------------

To begin, the buyer (in their database) navigates to the :menuselection:`Purchase` app to create a
:abbr:`RFQ (request for quotation)`.

Set the :guilabel:`Vendor` to the portal user representing the seller, and :guilabel:`Confirm` the
:abbr:`RFQ (request for quotation)`. Doing so converts it into a :doc:`purchase order
<../manage_deals/rfq>`.

.. example::
   |PO| from the buyer's database. The :guilabel:`Vendor` is the seller's portal user account, Joel.

   .. screenshot:: purchase-edi-po-database-view
      :menu: Purchase ‣ Orders ‣ Purchase Orders ‣ (open a PO)
      :shows: A confirmed PO in the buyer's database, with the Vendor field set to the seller's
              portal user, "Joel".
      :highlight: The Vendor field (red frame).
      :data: Demo company "YourCompany"; vendor/portal user "Joel".
      :module: purchase_edi_ubl_bis3
      :notes: English UI, light theme, 1440px width.

Seller's process
----------------

Once the |PO| is confirmed, it appears on the seller's portal dashboard. The seller downloads the
XML file and uploads it to their database.

Download file
~~~~~~~~~~~~~

As the seller, log in to the buyer's database as the portal user. On the dashboard, scroll down and
click the :guilabel:`Our Orders` button. Doing so reveals a list of purchase orders the buyer's
database has addressed to the portal user.

Select the desired purchase order, and the click :guilabel:`Connect with your software!` button.

In the pop-up window, copy the provided URL, and paste it into a new browser tab to download the XML
file.

.. example::
   Joel's portal view of the PO. The first image displays the :guilabel:`Connect with your
   software!` button, and the second image displays a pop-up window with the :guilabel:`Copy`
   button.

.. screenshot:: purchase-edi-po-portal-view
   :menu: (customer portal) ‣ Our Orders ‣ (open a PO)
   :shows: The portal view of a confirmed PO, with the "Connect with your software!" button.
   :highlight: The "Connect with your software!" button (red frame).
   :data: Demo company "YourCompany"; portal user "Joel"; PO PO00017.
   :module: purchase_edi_ubl_bis3
   :notes: English UI, light theme, 1440px width.

.. screenshot:: purchase-edi-pop-up
   :menu: (customer portal) ‣ Our Orders ‣ (open a PO) ‣ Connect with your software!
   :shows: The pop-up window with the download URL and the "Copy" button.
   :highlight: The Copy button (red frame).
   :data: Demo company "YourCompany"; PO PO00017.
   :module: purchase_edi_ubl_bis3
   :notes: English UI, light theme, 1440px width, use a throw-away/sample URL.

.. example::
   :download:`XML file <edi/P00017.xml>` for PO00017

.. _purchase/advanced/rfq-upload:

Upload file
~~~~~~~~~~~

Next, the seller logs in to their own Odoo database and opens :menuselection:`Sales` app. Click
:guilabel:`Upload` and select the downloaded XML file. Alternatively, users can drag and drop the
file into the :guilabel:`Quotations` dashboard.

Doing so automatically generates a sales order with the customer populated as the buyer and all
product lines, quantities, and prices pre-filled. This process ensures efficient and accurate data
exchange between the two databases.

.. screenshot:: purchase-edi-so
   :menu: Sales ‣ Orders ‣ Quotations ‣ (uploaded SO)
   :shows: The sales order automatically generated in the seller's database from the uploaded XML
           file, with the customer and product lines pre-filled.
   :highlight: The Order Lines tab (red frame).
   :data: Demo company "YourCompany"; SO generated from PO00017's XML.
   :module: purchase_edi_ubl_bis3
   :notes: English UI, light theme, 1440px width.

.. seealso::
   :doc:`../../../sales/sales/sales_quotations/create_quotations`

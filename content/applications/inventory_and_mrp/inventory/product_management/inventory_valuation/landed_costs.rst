============
Landed costs
============

.. |RfQ| replace:: :abbr:`RfQ (Request for Quotation)`
.. |PO| replace:: :abbr:`PO (Purchase Order)`
.. |FIFO| replace:: :abbr:`FIFO (First In First Out)`
.. |AVCO| replace:: :abbr:`AVCO (Average Costing)`

When shipping products to customers, the landed cost is the total price of a product or shipment,
including all expenses associated with shipping the product.

In Odoo, the *Landed Costs* feature is used to take additional costs into account when calculating
the valuation of a product. This includes the cost of shipment, insurance, customs duties, taxes,
and other fees.

Configuration
=============

To add landed costs to products, the *Landed Costs* feature must first be enabled. To enable this
feature, navigate to :menuselection:`Inventory app --> Configuration --> Settings`, and scroll to
the :guilabel:`Valuation` section.

Tick the checkbox next to the :guilabel:`Landed Costs` option, and click :guilabel:`Save` to save
changes.

Once the page refreshes, a new :guilabel:`Default Journal` field appears below the :guilabel:`Landed
Costs` feature in the :guilabel:`Valuation` section.

Click the :guilabel:`Default Journal` drop-down menu to reveal a list of accounting journals. Select
a journal for which all accounting entries related to landed costs should be recorded.

.. screenshot:: inventory-landed-costs-enable
   :menu: Inventory ‣ Configuration ‣ Settings
   :shows: The Inventory settings page scrolled to the "Valuation" section, with the "Landed Costs" checkbox
      enabled and the "Default Journal" field that appears below it filled in.
   :highlight: The "Landed Costs" checkbox and the "Default Journal" field (red frames).
   :data: Demo company "YourCompany HU"; default journal "Miscellaneous Operations".
   :module: stock_landed_costs
   :notes: English UI, light theme, 1440px width, crop to the "Valuation" settings block.

Create landed cost product
==========================

For charges that are consistently added as landed costs, a landed cost product can be created in
Odoo. This way, a landed cost product can be quickly added to a vendor bill as an invoice line,
instead of having to be manually entered every time a new vendor bill is created.

To do this, create a new product by going to :menuselection:`Inventory app --> Products -->
Products`, and clicking :guilabel:`New`.

Assign a name to the landed cost product in the :guilabel:`Product Name` field (i.e. `International
Shipping`). In the :guilabel:`Product Type` field, click the drop-down menu, and select
:guilabel:`Service` as the :guilabel:`Product Type`.

.. important::
   Landed cost products **must** have their :guilabel:`Product Type` set to :guilabel:`Service`.

Click the :guilabel:`Purchase` tab, and tick the checkbox next to :guilabel:`Is a Landed Cost` in
the :guilabel:`Vendor Bills` section. Once ticked, a new :guilabel:`Default Split Method` field
appears below it, prompting a selection. Clicking that drop-down menu reveals the following options:

- :guilabel:`Equal`: splits the cost equally across each product included in the receipt, regardless
  of the quantity of each.
- :guilabel:`By Quantity`: splits the cost across each unit of all products in the receipt.
- :guilabel:`By Current Cost`: splits the cost according to the cost of each product unit, so a
  product with a higher cost receives a greater share of the landed cost.
- :guilabel:`By Weight`: splits the cost, according to the weight of the products in the receipt.
- :guilabel:`By Volume`: splits the cost, according to the volume of the products in the receipt.

.. screenshot:: inventory-landed-costs-product
   :menu: Inventory ‣ Products ‣ Products ‣ (a service product) ‣ Purchase tab
   :shows: A service product form, "Purchase" tab, "Vendor Bills" section, with "Is a Landed Cost" ticked
      and the "Default Split Method" field showing its options.
   :highlight: The "Is a Landed Cost" checkbox and the "Default Split Method" field (red frame).
   :data: Service product "International Shipping", split method "By Weight".
   :module: stock_landed_costs
   :notes: English UI, light theme, 1440px width, crop to the "Vendor Bills" section.

When creating new vendor bills, this product can be added as an invoice line as a landed cost.

.. important::
   To apply a landed cost on a vendor bill, products in the original |PO| **must** belong to a
   *Product Category* with a *Costing Method* of either |AVCO| or |FIFO|, and the valuation method
   can be :doc:`manual <using_inventory_valuation>` or :doc:`automatic
   <inventory_valuation_config>`.

Create purchase order
=====================

Navigate to :menuselection:`Purchase app --> New` to create a new request for quotation (RfQ). In
the :guilabel:`Vendor` field, add a vendor to order products from. Then, click :guilabel:`Add a
product`, under the :guilabel:`Products` tab, to add products to the |RfQ|.

Once ready, click :guilabel:`Confirm Order` to confirm the order. Then, click :guilabel:`Receive
Products` once the products have been received, followed by :guilabel:`Validate`.

Create vendor bill
------------------

Once the vendor fulfills the |PO| and sends a bill, a vendor bill can be created from the |PO| in
Odoo.

Navigate to the :menuselection:`Purchase app`, and click into the |PO| for which a vendor bill
should be created. Then, click :guilabel:`Create Bill`. This opens a new :guilabel:`Vendor Bill` in
the :guilabel:`Draft` stage.

In the :guilabel:`Bill Date` field, click the line to open a calendar popover menu, and select the
date on which this draft bill should be billed.

Then, under the :guilabel:`Invoice Lines` tab, click :guilabel:`Add a line`, and click the drop-down
menu in the :guilabel:`Product` column to select the previously-created landed cost product. Click
the :icon:`fa-cloud-upload` :guilabel:`(cloud with arrow)` icon to manually save and update the
draft bill.

.. screenshot:: inventory-landed-costs-bill-lines
   :menu: Purchase ‣ Orders ‣ Purchase Orders ‣ (an order) ‣ Create Bill
   :shows: The "Invoice Lines" tab of a draft vendor bill with two lines: the ordered product with an
      unticked "Landed Costs" checkbox, and the landed cost service product with a ticked one.
   :highlight: The "Landed Costs" column (red frame).
   :data: One storable product line and the "International Shipping" line.
   :module: stock_landed_costs
   :notes: English UI, light theme, 1440px width, crop to the invoice lines.

In the :guilabel:`Landed Costs` column, the product ordered from the vendor does **not** have its
checkbox ticked, while the landed cost product's checkbox **is** ticked. This differentiates landed
costs from all other costs displayed on the bill.

Additionally, at the top of the form, a :guilabel:`Create Landed Costs` button appears.

.. screenshot:: inventory-landed-costs-create-button
   :menu: Accounting ‣ Vendors ‣ Bills ‣ (a draft bill with a landed cost line)
   :shows: The top of a draft vendor bill where the "Create Landed Costs" button has appeared.
   :highlight: The "Create Landed Costs" button (red frame).
   :data: The same bill as the previous screenshot.
   :module: stock_landed_costs
   :notes: English UI, light theme, 1440px width, crop to the button bar.

Add landed cost
===============

Once a landed cost is added to the vendor bill, click :guilabel:`Create Landed Costs` at the top of
the vendor bill.

Doing so automatically creates a landed cost record, with a set landed cost pre-filled in the
product line in the :guilabel:`Additional Costs` tab.

From the :guilabel:`Landed Cost` form, click the :guilabel:`Transfers` drop-down menu, and select
which transfer the landed cost belongs to.

.. screenshot:: inventory-landed-costs-form
   :menu: Inventory ‣ Operations ‣ Landed Costs ‣ (a landed cost)
   :shows: A landed cost form with the "Transfers" field set to the receipt the cost belongs to, the
      "Additional Costs" tab holding the landed cost product line, and the "Compute" button below the total.
   :highlight: The "Transfers" field (red frame).
   :data: Landed cost from the vendor bill above, linked to receipt WH/IN/00014.
   :module: stock_landed_costs
   :notes: English UI, light theme, 1440px width, full form.

.. tip::
   In addition to creating landed costs directly from a vendor bill, landed cost records can *also*
   be created by navigating to :menuselection:`Inventory app --> Operations --> Landed Costs`, and
   clicking :guilabel:`New`.

After setting the picking from the :guilabel:`Transfers` drop-down menu, click :guilabel:`Compute`
(at the bottom of the form, under the :guilabel:`Total:` cost).

Click the :guilabel:`Valuation Adjustments` tab to see the impact of the landed costs. The
:guilabel:`Original Value` column lists the original price of the |PO|, the :guilabel:`Additional
Landed Cost` column displays the landed cost, and the :guilabel:`New Value` displays the sum of the
two, for the total cost of the |PO|.

Once ready, click :guilabel:`Validate` to post the landed cost entry to the accounting journal.

This causes a :guilabel:`Valuation` smart button to appear at the top of the form. Click the
:guilabel:`Valuation` smart button to open a :guilabel:`Stock Valuation` page, with the product's
updated valuation listed.

.. note::
   For a :guilabel:`Valuation` smart button to appear upon validation, the products in the receipt
   **must** have their :guilabel:`Product Type` set to :guilabel:`Goods` with :guilabel:`Track
   Inventory` enabled.

To view the valuation of *every* product, including landed costs, navigate to
:menuselection:`Inventory app --> Reporting --> Valuation`.

.. note::
   Each journal entry created for a landed cost on a vendor bill can be viewed in the *Accounting*
   app.

   To locate these journal entries, navigate to :menuselection:`Accounting app --> Accounting -->
   Journal Entries`, and locate the correct entry by its number. The journal used is the one set in
   the :guilabel:`Default Journal` field of the :guilabel:`Landed Costs` setting.

   Click into the journal entry to view the :guilabel:`Journal Items`, and other information about
   the entry.

   .. screenshot:: inventory-landed-costs-journal-entry
      :menu: Accounting ‣ Accounting ‣ Journal Entries ‣ (the landed cost entry)
      :shows: The journal entry created when the landed cost was validated, with its journal items debiting
         the stock valuation account and crediting the landed cost account.
      :highlight: The journal items (red frame).
      :data: The entry generated by the validated landed cost.
      :module: stock_landed_costs, account
      :notes: English UI, light theme, 1440px width, crop to the journal items table.

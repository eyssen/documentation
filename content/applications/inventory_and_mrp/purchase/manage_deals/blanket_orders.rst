==============
Blanket orders
==============

.. _purchase/manage_deals/blanket-orders:

.. |SO| replace:: :abbr:`SO (Sales Order)`
.. |PO| replace:: :abbr:`PO (Purchase Order)`
.. |UoM| replace:: :abbr:`UoM (Unit of Measure)`
.. |RfQ| replace:: :abbr:`RfQ (Request for Quotation)`
.. |RfQs| replace:: :abbr:`RfQs (Requests for Quotation)`

Blanket orders are long-term purchase agreements between a company and a vendor to deliver products
on a recurring basis with predetermined pricing.

Blanket orders are helpful when products are consistently purchased from the same vendor, but in
different quantities, and at different times.

By simplifying the ordering process, blanket orders not only save time, they also save money, since
they can be advantageous when negotiating bulk pricing with vendors.

.. important::
   Two different blanket order implementations may be present in this database:

   - The one described on this page, part of the standard *Purchase Agreements* feature
     (`purchase_requisition`), reachable at :menuselection:`Purchase app --> Orders --> Purchase
     Agreements`, with the :guilabel:`Agreement Type` set to :guilabel:`Blanket Order`.
   - The *Purchase Blanket Orders* module (`purchase_blanket_order`), an independent feature with
     its own :guilabel:`Blanket Orders` and :guilabel:`Blanket Order Lines` menus, further down in
     :menuselection:`Purchase app --> Orders`. See :ref:`purchase/manage_deals/oca-blanket-orders`
     below for how it differs.

   Check which menus are visible in this database's :menuselection:`Purchase app --> Orders` to
   know which one applies.

Create a new blanket order
==========================

To create blanket orders, enable the *Purchase Agreements* feature from the *Purchase* app settings.
Navigate to :menuselection:`Purchase app --> Configuration --> Settings`, and under the
:guilabel:`Orders` section, click the checkbox for :guilabel:`Purchase Agreements`. Then click
:guilabel:`Save` to implement the changes.

.. note::
   In addition to creating blanket orders, the *Purchase Agreements* setting also allows users to
   create alternative requests for quotation (RfQs).

.. screenshot:: purchase-blanket-orders-enabled-setting
   :menu: Purchase ‣ Configuration ‣ Settings
   :shows: Settings page scrolled to the "Orders" section, with the "Purchase Agreements" checkbox
           enabled.
   :highlight: The "Purchase Agreements" setting (red frame).
   :data: Demo company "YourCompany".
   :module: purchase_requisition
   :notes: English UI, light theme, 1440px width, crop to the setting block.

To create a blanket order, go to :menuselection:`Purchase app --> Orders --> Purchase Agreements`,
and click :guilabel:`New`. This opens a new purchase agreement form.

Configure the following fields in the new purchase agreement form to establish predetermined rules
for the recurring long-term agreement:

- :guilabel:`Vendor`: the supplier to whom this agreement is tied, either once or on a recurring
  basis. The vendor can be selected directly from the drop-down menu next to this field.
- :guilabel:`Buyer`: the user assigned to this specific blanket order. By default, this is the user
  who created the agreement; the user can be changed directly from the drop-down menu next to this
  field.
- :guilabel:`Agreement Type`: the type of purchase agreement this blanket order is classified as.
  Use the drop-down menu to choose :guilabel:`Blanket Order` if not already selected.
- :guilabel:`Currency`: the agreed-upon currency to be used for this exchange. If multiple
  currencies have been activated in the database, the currency can be changed from the drop-down
  menu next to this field.
- :guilabel:`Agreement Validity`: the date range this agreement should be valid for. If this blanket
  order should not expire, leave this field blank.
- :guilabel:`Reference`: the source purchase order (PO) that this blanket order is tied to. If this
  blanket order should not be tied to any existing |PO|, leave this field blank.
- :guilabel:`Operation Type`: the operation type that should be applied to this order once it is
  delivered.
- :guilabel:`Company`: the company assigned to this specific blanket order. By default, this is the
  company that the user creating the blanket order is listed under. If the database is not a
  multi-company database, this field **cannot** be changed, and defaults to the only company listed
  in the database.

.. screenshot:: purchase-blanket-orders-new-agreement
   :menu: Purchase ‣ Orders ‣ Purchase Agreements ‣ New
   :shows: A new purchase agreement form with the Agreement Type set to "Blanket Order", a vendor
           selected, and two product lines added.
   :highlight: The Agreement Type field (red frame).
   :data: Demo company "YourCompany"; vendor "Azure Interior"; two products with quantities and
          unit prices set.
   :module: purchase_requisition
   :notes: English UI, light theme, 1440px width.

Once all relevant fields have been filled out, click :guilabel:`Add a line` to add products under
the :guilabel:`Product` column. Then, in the :guilabel:`Quantity` column, change the quantity of
each product, and set a price in the :guilabel:`Unit Price` column.

.. important::
   When adding products to a new blanket order, the pre-existing prices of products are not
   automatically added to the product lines. Instead, the prices **must** be manually assigned, by
   changing the value in the :guilabel:`Unit Price` column to an agreed-upon price with the listed
   vendor. Otherwise, the price will remain `0`.

Click :guilabel:`Confirm` to save this new purchase agreement.

Once confirmed, the blanket order's stage changes from :guilabel:`Draft` to :guilabel:`Confirmed`,
meaning this agreement can be selected and used when creating new |RfQs|.

.. tip::
   After creating and confirming a blanket order, products, quantities, and prices can still be
   edited, added, and removed from the purchase agreement.

Create a new |RfQ| from the blanket order
=========================================

After confirming a blanket order, new quotations can be created directly from the blanket order
form. |RfQs| using this form are pre-populated with information based on the rules set in the form.
The total quantities of products ordered through linked |RfQs| are automatically updated in the
:guilabel:`Ordered` field on the agreement.

Additionally, new quotations are automatically linked to this blanket order form, via the
:guilabel:`RFQs/Orders` smart button at the top-right of the form.

To create a new quotation from the blanket order form, click the :guilabel:`New Quotation` button.
This opens a new |RfQ|, that is pre-populated with the correct information, depending on the
settings configured on the blanket order form.

From the new |RfQ| form, click :guilabel:`Send by Email` to compose and send an email to the listed
vendor. Click :guilabel:`Print RFQ` to generate a printable PDF of the quotation; or, once ready,
click :guilabel:`Confirm Order` to confirm the |PO|.

.. screenshot:: purchase-blanket-orders-new-quotation
   :menu: Purchase ‣ Orders ‣ Purchase Agreements ‣ (open a blanket order) ‣ New Quotation
   :shows: A new RfQ pre-populated with the vendor and product lines copied from the blanket order.
   :highlight: The Products tab, pre-filled from the blanket order.
   :data: Demo company "YourCompany"; RfQ for vendor "Azure Interior".
   :module: purchase_requisition
   :notes: English UI, light theme, 1440px width.

Once the |PO| has been confirmed, click back to the blanket order form (via the breadcrumbs, at the
top of the page). From the blanket order form, there is now one |RfQ| listed in the
:guilabel:`RFQs/Orders` smart button at the top-right of the form. Click the :guilabel:`RFQs/Orders`
smart button to see the |PO| that was just created.

.. screenshot:: purchase-blanket-orders-rfq-smart-button
   :menu: Purchase ‣ Orders ‣ Purchase Agreements ‣ (open a blanket order)
   :shows: A confirmed blanket order form with the "RFQs/Orders" smart button showing a count of 1.
   :highlight: The "RFQs/Orders" smart button (red frame).
   :data: Demo company "YourCompany"; blanket order with one confirmed PO.
   :module: purchase_requisition
   :notes: English UI, light theme, 1440px width.

Replenishment
=============

Once a blanket order is confirmed, a new vendor line is added under the :guilabel:`Purchase` tab of
the products included in the order.

This makes blanket orders useful with :doc:`automated replenishment
<../../purchase/products/reordering>`, because information about the :guilabel:`Vendor`,
:guilabel:`Price`, and the :guilabel:`Agreement` are referenced on the vendor line. This information
dictates when, where, and at what price the product should be replenished.

.. screenshot:: purchase-blanket-orders-product-form
   :menu: Purchase ‣ Products ‣ Products ‣ (open a product) ‣ Purchase
   :shows: The Purchase tab of a product form, with a vendor line referencing the blanket order in
           the "Agreement" column.
   :highlight: The "Agreement" column (red frame).
   :data: Demo company "YourCompany"; product with a vendor line linked to a confirmed blanket
          order.
   :module: purchase_requisition
   :notes: English UI, light theme, 1440px width.

.. _purchase/manage_deals/oca-blanket-orders:

Alternative implementation: the Purchase Blanket Orders module
================================================================

Some databases instead use the *Purchase Blanket Orders* module (`purchase_blanket_order`, an OCA
community module), which is **not** built on the *Purchase Agreements* feature described above, and
works differently:

- Blanket orders live on their own model, with dedicated :guilabel:`Blanket Orders` and
  :guilabel:`Blanket Order Lines` menus under :menuselection:`Purchase app --> Orders`, separate
  from :guilabel:`Purchase Agreements`.
- A blanket order line has an :guilabel:`Original quantity`, and Odoo tracks its
  :guilabel:`Ordered`, :guilabel:`Invoiced`, :guilabel:`Received`, and :guilabel:`Remaining`
  quantities automatically.
- Its status is computed automatically: :guilabel:`Draft`, :guilabel:`Open`, :guilabel:`Done` (all
  quantities ordered), or :guilabel:`Expired` (past the :guilabel:`Validity Date`).
- **Regular purchase order lines are automatically matched** to an open blanket order line for the
  same product, vendor, and currency with enough remaining quantity — there is no need to create the
  |RfQ| from the blanket order form. Confirming a |PO| whose line is linked to a blanket order line
  with no remaining quantity is blocked.
- A :guilabel:`Create Purchase Order` button, on the blanket order form (or a selection of blanket
  order lines), generates a |PO| for the remaining quantities instead.
- The :guilabel:`Disable adding more lines to POs` setting, under :menuselection:`Purchase app -->
  Configuration --> Settings --> Blanket Orders`, can restrict purchase orders generated from a
  blanket order to only the products already on that blanket order.

.. screenshot:: purchase-blanket-orders-oca-form
   :menu: Purchase ‣ Orders ‣ Blanket Orders ‣ (open a blanket order)
   :shows: An open Purchase Blanket Order form (purchase_blanket_order module) with its order lines,
           the Original/Ordered/Received/Remaining quantity columns, and the "Create Purchase Order"
           button.
   :highlight: The "Create Purchase Order" button and the quantity columns (red frame).
   :data: Demo company "YourCompany"; open blanket order with two lines.
   :module: purchase_blanket_order
   :notes: English UI, light theme, 1440px width.

.. seealso::
   :doc:`calls_for_tenders`

======================
Sales order extensions
======================

Several eYssen modules add fields and buttons to quotations and sales orders. Each section below
says which module provides the feature; install only the ones you need.

.. _sales/order_extensions/eyssen_sale:

Order information
=================

The *eYssen Sale* module (``eyssen_sale``) adds four things to the quotation and sales order form.

Contact person
--------------

The :guilabel:`Contact Person` field, next to :guilabel:`Customer`, records who at the customer this
order is handled with. Only child contacts of the customer are offered, and the value is carried
over to the customer invoice created from the order.

Company-creation warning
------------------------

When the invoice address carries company data (a company name or a VAT number) but no company
contact has been created for it, an orange banner appears at the top of the order:

   *Warning: The invoice address has company data (name/VAT) but the company has not been created
   yet. Open the contact and click "+Create Company".*

Settlement periods
------------------

Service lines that cover a period — support, hosting, a maintenance fee — can carry the period they
settle. The order holds a :guilabel:`Default Settlement Start` and :guilabel:`Default Settlement
End`, which new lines inherit, and every order line has its own :guilabel:`Settlement Period Start`,
:guilabel:`Settlement Period End` and the computed :guilabel:`Settlement Days` (the inclusive number
of days in the period). The three line fields are optional columns of the :guilabel:`Order Lines`
tab — switch them on with the column-options toggle at the right of the header.

Locking line data
-----------------

The padlock toggle above the order lines, :guilabel:`Line Data Locked`, protects the manually agreed
prices and discounts from being recomputed. It is switched on automatically when the order is
confirmed. While it is on, :guilabel:`Update Prices` refuses to run and shows which orders must be
unlocked first.

Payment method
--------------

A :guilabel:`Payment Method` field is shown under :guilabel:`Payment Terms`. Only the methods
compatible with the order's company, customer and currency are offered.

.. screenshot:: sales-order-extensions-eyssen-sale
   :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation)
   :shows: A quotation form showing the Contact Person field under Customer, the Default Settlement Start/End fields, the Payment Method field under Payment Terms, and the padlock "Line Data Locked" toggle above the order lines.
   :highlight: The Contact Person field and the padlock toggle (red frames).
   :data: Quotation for "Deco Addict", contact person "Jane Doe", settlement period for the current month.
   :module: eyssen_sale
   :notes: English UI, light theme, 1440px width, crop to the order header and the top of the order lines.

Add items from a previous sale
==============================

*Add Items from Previous Sale* (``eyssen_add_item_from_previous_sale``) copies the lines of an
earlier order into the current one — useful for customers who reorder the same basket.

On a quotation, click :guilabel:`Add Previous Items`. In the pop-up, pick the
:guilabel:`Previous Sale` and choose what to do with products that are already on the current order
in the :guilabel:`If Product Duplication` field:

- :guilabel:`Stop`: refuse the copy and report the conflict.
- :guilabel:`Skip`: leave the existing line untouched.
- :guilabel:`Replace`: overwrite the existing line with the one from the previous order.
- :guilabel:`Increase`: add the quantities together.

Click :guilabel:`Add` to copy the lines.

.. screenshot:: sales-order-extensions-previous-items
   :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation) ‣ Add Previous Items
   :shows: The "Add Previous Items" pop-up with the Previous Sale field and the "If Product Duplication" options.
   :highlight: The "If Product Duplication" field (red frame).
   :data: Previous order S00031; duplication set to "Increase".
   :module: eyssen_add_item_from_previous_sale
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

Order versions
==============

*Sale Versioning* (``eyssen_sale_version``) keeps the successive offers made to a customer instead of
overwriting one quotation.

Click :guilabel:`Create Version` on a quotation to produce a copy with the
:guilabel:`Version Number` increased by one; the new order keeps a :guilabel:`Parent Version` link
to the one it came from. The :guilabel:`Versions` smart button opens the whole family of versions.

.. important::
   Only one version of a family can be confirmed. Confirming a version cancels the sibling versions,
   so the pipeline never contains two confirmed variants of the same offer.

.. screenshot:: sales-order-extensions-versions
   :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation)
   :shows: A quotation with the "Create Version" button in the header, the Version Number field and the "Versions" smart button in the button box.
   :highlight: The "Create Version" button and the Versions smart button (red frames).
   :data: Quotation S00042, version 2, 3 versions in the family.
   :module: eyssen_sale_version
   :notes: English UI, light theme, 1440px width, crop to the header and button box.

Quantity totals on the order
============================

*Add Quantity Total for Sale* (``eyssen_quantity_total_sale``) totals the ordered quantities next to
the amount totals at the bottom of the order.

Because quantities of different units cannot simply be added up, the total is shown per unit of
measure: a compact :guilabel:`Sum Qty` next to the amounts, and a detailed
:guilabel:`Sum Qty (detailed)` breakdown listing each unit separately.

Copying ordered quantity to delivered
=====================================

*Sale Copy Qty to Delivered* (``sale_copy_qty_delivered``) speeds up service lines that are
delivered manually.

On a confirmed order, a right-arrow button appears between the ordered and the delivered quantity of
a **service** line whenever the two differ. Clicking it copies the ordered quantity into
:guilabel:`Delivered`.

.. note::
   The button only appears on service lines whose delivery is set manually. Lines delivered through
   a stock operation or a timesheet keep their computed quantity.

Price calculator
================

*Sale Price Calculator* (``eyssen_sale_price_calculator``) helps the salesperson set a line price
from every price that is known for the product.

Open it from an order line; the :guilabel:`Sale Price Calculator` pop-up shows four reference
groups:

- :guilabel:`Base Prices`: the product's sales price.
- :guilabel:`Pricelist Prices`: the price each pricelist would give.
- :guilabel:`Vendor Prices`: the supplier prices recorded on the product, with the supplier quantity
  and its unit.
- :guilabel:`Purchase Prices`: the prices actually paid on past purchase orders, with their dates.

Select a reference line, then adjust it with the :guilabel:`Percent Plus` / :guilabel:`Percent
Minus`, :guilabel:`Net Plus` / :guilabel:`Net Minus` and :guilabel:`Gross Plus` / :guilabel:`Gross
Minus` fields. The calculator shows the resulting :guilabel:`Calculated Net Price` and
:guilabel:`Calculated Gross Price`; prices in another currency are converted to the order currency.
The :guilabel:`Method` field decides whether :guilabel:`Set Price` writes the result as a
:guilabel:`Price` or as a :guilabel:`Discount` on the order line.

.. screenshot:: sales-order-extensions-price-calculator
   :menu: Sales ‣ Orders ‣ Quotations ‣ (a quotation) ‣ Order Lines ‣ (a line) ‣ price calculator
   :shows: The "Sale Price Calculator" pop-up with the Base, Pricelist, Vendor and Purchase price groups, the plus/minus adjustment fields and the calculated net and gross prices.
   :highlight: The adjustment fields and the "Set Price" button (red frames).
   :data: Product "Conference Chair"; one vendor price and two past purchase prices.
   :module: eyssen_sale_price_calculator
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

.. note::
   The vendor and purchase references require the *Purchase* application and the supplier product
   data (``supplier_product_management``).

Overdue-payment warning
=======================

*Sale Payment Warning* (``sale_payment_warning``) shows a banner on the quotation or sales order when
the customer has overdue invoices, so the salesperson sees the payment risk before confirming.

The banner has three levels — informational, warning and danger — depending on how much is overdue
and for how long.

.. note::
   The thresholds come from the *Payment Warning* configuration of the accounting module
   ``account_payment_warning``.

Process numbers
===============

*Process Number - Sale* (``process_number_sale``) links sales orders to the company's process (case)
numbers.

A :guilabel:`Process Number` field is added to the sales order, and the process number record gets a
:guilabel:`Sale Orders` smart button listing the orders attached to it. When the
:guilabel:`Create Automatically` option is enabled in :menuselection:`Sales app --> Configuration
--> Settings`, confirming an order without a process number creates one for it.

.. note::
   Requires the base *Process Number* module (``process_number``).

Warehouse per order line
========================

*Sale Multiple Warehouse* (``eyssen_sale_multiple_warehouse``) makes the :guilabel:`Warehouse` field
editable **per order line** instead of only once for the whole order, so one order can be shipped
from several warehouses.

Set the warehouse on each line in the :guilabel:`Order Lines` tab; the delivery orders generated on
confirmation are split accordingly.

.. seealso::
   :doc:`../../inventory_and_mrp/inventory/warehouses_storage/multi_warehouse`

Comment templates
=================

*Sale Comments* (``sale_comment_template``) lets you keep reusable comment texts and drop them on
quotations and sales orders instead of retyping the same conditions.

Maintain the texts in :menuselection:`Sales app --> Configuration --> Document Comments`. Each
template has a position (before or after the document lines) and can be set to apply automatically
to a partner or a document type.

.. note::
   Requires the base comment-template modules (``base_comment_template``,
   ``account_comment_template``).

Order quantity limits
=====================

*Sale Quantity Limitation* (``eyssen_sale_quantity_limit``) enforces per-product ordering rules.

Open a product and fill in the :guilabel:`Quantity Limitation` group of the :guilabel:`Sales` tab:

- :guilabel:`Minimum Quantity`: the smallest quantity that may be ordered.
- :guilabel:`Maximum Quantity`: the largest quantity that may be ordered.
- :guilabel:`Quantity Multiplier`: the quantity must be a multiple of this number — for example `6`
  for a product sold by the half-dozen.

A sales order line that breaks one of these rules is refused with an explanatory message.

.. screenshot:: sales-order-extensions-quantity-limits
   :menu: Sales ‣ Products ‣ Products ‣ (a product) ‣ Sales
   :shows: The "Quantity Limitation" group of a product's Sales tab with the Minimum Quantity, Maximum Quantity and Quantity Multiplier fields.
   :highlight: The Quantity Limitation group (red frame).
   :data: Product "Conference Chair"; minimum 2, maximum 100, multiplier 2.
   :module: eyssen_sale_quantity_limit
   :notes: English UI, light theme, 1440px width, crop to the field group.

.. note::
   The companion module *Sale Quantity Limitation - Website Sale*
   (``eyssen_sale_quantity_limit_ws``) applies the same rules to the online store: the quantity
   selector on the product page and in the cart respects the minimum, the maximum and the
   multiplier.

.. _sales/order-extensions/team-logo:

Report logo per sales team
==========================

*Conditional Report Logo* (``report_conditional_logo``) prints the logo of the **sales team**
instead of the company logo in the header of the PDF documents, which is useful when several brands
or business units sell under the same company.

Go to :menuselection:`Sales --> Configuration --> Sales Teams`, open a team, and upload its image in
the :guilabel:`Report Logo` group at the bottom of the form.

From then on, every document that has a :guilabel:`Sales Team` field (quotations, sales orders, and
customer invoices) is printed with the logo of its team, in all the document layouts. Documents whose team has no logo, and documents without a sales team (e.g.,
purchase orders or delivery slips), keep the company logo.

The feature can be switched off without removing the logos: go to :menuselection:`Sales -->
Configuration --> Conditional Report Logos`, and turn off the :guilabel:`Active` toggle of the
:guilabel:`Sales Team` source. A source can also be limited to one :guilabel:`Company`. The menu is
reserved for the users with the :guilabel:`Sales: Administrator` access right.

.. screenshot:: sales-order-extensions-team-logo
   :menu: Sales ‣ Configuration ‣ Sales Teams ‣ (a team)
   :shows: The bottom of a sales team form with the "Report Logo" group and an uploaded logo image.
   :highlight: The "Report Logo" group (red frame).
   :data: Sales team "Website" with a brand logo different from the company logo.
   :module: report_conditional_logo
   :notes: English UI, light theme, 1440px width, crop to the lower part of the form.

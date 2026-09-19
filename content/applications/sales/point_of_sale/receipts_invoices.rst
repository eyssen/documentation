=====================
Receipts and invoices
=====================

Receipts
========

Set up receipts by going to :menuselection:`Point of Sale --> Configuration --> Point of Sale`,
selecting a POS, and scrolling down to the :guilabel:`Bills & Receipts` section.

To **customize** the **header** and **footer**, activate :guilabel:`Header & Footer` and fill in
both fields with the information to be printed on the receipts.

To **print receipts** automatically once the payment is registered, enable the :guilabel:`Automatic
Receipt Printing` setting.

.. screenshot:: pos-receipts-receipt-preview
   :menu: (POS interface) ‣ Receipt screen
   :shows: A POS receipt preview with the company header, the order lines, the taxes, the total and the payment method.
   :module: point_of_sale
   :notes: English UI, light theme; scale down to about 75 % of the page width.

.. note::
   With the *PoS Hungarian* module (`eyssen_l10n_hu_pos`), the line *Nem adóügyi bizonylat!* (“Not a
   fiscal receipt!”) is printed in the header of every receipt, in Hungarian, whatever the language
   of the point of sale. See :doc:`../../finance/fiscal_localizations/hungary`.

.. seealso::
   - :ref:`pos/restaurant/bills`
   - :doc:`configuration/epos_printers`

Reprint a receipt
-----------------

From the POS interface, click :guilabel:`Orders`, open the dropdown selection menu next to the
search bar, and change the default :guilabel:`All active orders` filter to :guilabel:`Paid`. Then,
select the corresponding order and click :guilabel:`Print Receipt`.

.. screenshot:: pos-receipts-reprint
   :menu: (POS interface) ‣ Orders
   :shows: The order list inside the POS filtered on "Paid", with a paid order selected and the
      "Print Receipt" button visible.
   :highlight: The "Print Receipt" button (red frame).
   :module: point_of_sale
   :notes: English UI, light theme, 1440px width.

.. note::
   You can filter the list of orders using the search bar. Type in your reference and click
   :guilabel:`Receipt Number`, :guilabel:`Date`, or :guilabel:`Customer`.

.. _receipts-invoices/receipt-designs:

Receipt designs
---------------

The *POS Receipt Design* module (`custom_receipts_for_pos`) replaces the standard receipt layout
with a custom one, so the receipt can be adapted to the shop's branding or to local requirements
without touching the source code.

To manage the available layouts, go to :menuselection:`Point of Sale --> Configuration --> Receipt
Designs`. Each record holds a :guilabel:`Name` and the :guilabel:`Receipt XML` field containing the
QWeb template of the receipt. Two ready-made designs are installed with the module and can be
duplicated as a starting point.

To apply a design to a point of sale, go to :menuselection:`Point of Sale --> Configuration -->
Point of Sale`, open the POS, enable :guilabel:`Custom Receipt` in the :guilabel:`Bills & Receipts`
section, and select the layout in the :guilabel:`Receipt Design` field.

.. screenshot:: pos-receipts-custom-design
   :menu: Point of Sale ‣ Configuration ‣ Receipt Designs ‣ (a design)
   :shows: A receipt design form with its name and the "Receipt XML" field showing the QWeb
      template in the code editor.
   :data: Design "Compact receipt".
   :module: custom_receipts_for_pos
   :notes: English UI, light theme, 1440px width.

.. important::
   The :guilabel:`Receipt XML` field expects a valid QWeb template. An invalid template prevents
   the receipt from being rendered, so test a new design on a test point of sale before using it in
   the shop.

.. _receipts-invoices/invoices:

Invoices
========

Point of Sale allows you to issue and print invoices for :ref:`registered customers <pos/customers>`
upon payment and retrieve all past invoiced orders.

.. note::
   An invoice created in a POS creates an entry into the corresponding :ref:`accounting journal
   <cheat_sheet/journals>`, previously :ref:`set up <receipts_invoices/invoice_configuration>`.

.. _receipts_invoices/invoice_configuration:

Configuration
-------------

To define what journals will be used for a specific POS, go to the :ref:`POS' settings
<configuration/settings>` and scroll down to the accounting section. Then, you can determine the
accounting journals used by default for orders and invoices in the :guilabel:`Default Journals`
section.

.. screenshot:: pos-receipts-invoicing-setting
   :menu: Point of Sale ‣ Configuration ‣ Settings
   :shows: The "Accounting" section of the POS settings with the "Invoicing" option enabled and an invoice journal selected.
   :highlight: The "Invoicing" setting block (red frame).
   :module: point_of_sale
   :notes: English UI, light theme, 1440px width, crop to the settings block.

Invoice a customer
------------------

Upon processing a payment, click :guilabel:`Invoice` underneath the customer's name to issue an
invoice for that order.

Select the payment method and click :guilabel:`Validate`. The **invoice** is automatically issued
and ready to be downloaded and/or printed.

.. note::
   To be able to issue an invoice, a :ref:`customer <pos/customers>` must be selected.

Retrieve invoices
-----------------

To retrieve invoices from the **POS dashboard**,

#. access all orders made through your POS by going to :menuselection:`Point of Sale --> Orders -->
   Orders`;
#. to access an order's invoice, open the **order form** by selecting the order, then click
   :guilabel:`Invoice`.

.. screenshot:: pos-receipts-invoice-smart-button
   :menu: Point of Sale ‣ Orders ‣ Orders ‣ (an invoiced order)
   :shows: A POS order form with the "Invoice" smart button in the upper right corner of the form.
   :highlight: The "Invoice" smart button (red frame).
   :module: point_of_sale
   :notes: English UI, light theme, 1440px width, crop to the top of the order form.

.. note::
   - **Invoiced orders** can be identified by the :guilabel:`Invoiced` status in the
     :guilabel:`Status` column.
   - You can filter the list of orders to invoiced orders by clicking :guilabel:`Filters` and
     :guilabel:`Invoiced`.

QR codes to generate invoices
-----------------------------

Customers can also request an invoice by scanning the **QR code** printed on their receipt. Upon
scanning, they must fill in a form with their billing information and click :guilabel:`Get my
invoice`. On the one hand, doing so generates an invoice available for download. On the other hand,
the order status goes from :guilabel:`Paid` or :guilabel:`Posted` to :guilabel:`Invoiced` in the
Odoo backend.

.. screenshot:: pos-receipts-portal-order-status
   :menu: (Customer portal) ‣ POS order
   :shows: The customer portal view of a POS order reached from the receipt QR code, showing the order status and the download links.
   :module: point_of_sale
   :notes: English UI, light theme, 1440px width, crop to the portal page.

To use this feature, you have to enable QR codes on receipts by going to :menuselection:`Point of
Sale --> Configuration --> Settings`. Then, select the POS in the :guilabel:`Point of Sale` field,
scroll down to the :guilabel:`Bills & Receipts` section and enable :guilabel:`Use QR code on
ticket`.

.. _receipts-invoices/payment-terms:

Payment terms on POS invoices
-----------------------------

By default, an invoice issued from the POS carries no payment term, which is inconvenient when the
POS is also used for deferred-payment sales. The *PoS Invoice* module (`eyssen_pos_invoice`) links a
payment term to each :doc:`payment method <payment_methods>`.

To set it, go to :menuselection:`Point of Sale --> Configuration --> Payment Methods`, open a
payment method, and fill in the :guilabel:`Payment Term` field. The field is required; it defaults to
a payment term due immediately. When an order paid with that payment method is invoiced, the invoice
is created with the payment term of the method.

The module also checks the customer's invoicing address while the order is being registered: if the
street, city, ZIP code or country is missing — or, for a Hungarian company, a valid VAT number — the
missing fields are listed next to the customer in the POS customer list, so the cashier can complete
them before issuing the invoice.

.. screenshot:: pos-invoice-payment-term
   :menu: Point of Sale ‣ Configuration ‣ Payment Methods ‣ (a payment method)
   :shows: A payment method form with the "Payment Term" field filled in.
   :highlight: The "Payment Term" field (red frame).
   :data: Payment method "Bank transfer" with payment term "30 Days".
   :module: eyssen_pos_invoice
   :notes: English UI, light theme, 1440px width, crop to the form.

.. note::
   This module requires the *eYssen Hungarian localization* module (`eyssen_l10n_hu`), which
   provides the Hungarian VAT number validation used by the address check.

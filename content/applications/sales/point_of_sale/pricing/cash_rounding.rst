=============
Cash rounding
=============

**Cash rounding** is required when the lowest physical denomination
of currency, or the smallest coin, is higher than the minimum unit
of account.

For example, some countries require their companies to round up or
down the total amount of an invoice to the nearest five cents, when
the payment is made in cash.

Each point of sale in Odoo can be configured to apply cash rounding
to the totals of its bills or receipts.

Configuration
=============

Go to :menuselection:`Point of Sale --> Configuration --> Settings`
and enable *Cash Rounding*, then click on *Save*.

.. screenshot:: pos-cash-rounding-accounting-setting
   :menu: Accounting ‣ Configuration ‣ Settings
   :shows: The Accounting settings with the "Cash Rounding" option enabled.
   :highlight: The "Cash Rounding" setting (red frame).
   :module: account
   :notes: English UI, light theme, 1440px width, centered, crop to the settings block.

Go to :menuselection:`Point of Sale --> Configuration --> Point of
Sale`, open the point of sale you want to configure, and enable the
*Cash Rounding* option.

To define the **Rounding Method**, open the drop-down list and click
on *Create and Edit...*.

Define here your *Rounding Precision*, *Profit Account*, and
*Loss Account*, then save both the Rounding Method and your Point
of Sale settings.

.. screenshot:: pos-cash-rounding-pos-setting
   :menu: Point of Sale ‣ Configuration ‣ Settings
   :shows: The POS settings with "Cash Rounding" enabled and a rounding method selected below it.
   :highlight: The "Cash Rounding" setting block (red frame).
   :data: Rounding method "Rounding 0.05" with rounding precision 0.05.
   :module: point_of_sale, account
   :notes: English UI, light theme, 1440px width, centered, crop to the settings block.

All total amounts of this point of sale now add a line to apply the
rounding according to your settings.

.. screenshot:: pos-cash-rounding-payment-screen
   :menu: (POS interface) ‣ Payment screen
   :shows: The POS payment screen with a separate rounding line added to the order total.
   :highlight: The rounding line (red frame).
   :module: point_of_sale, account
   :notes: English UI, light theme, 1440px width, centered, crop to the totals block.

.. note::
   Odoo Point of Sale only supports the :guilabel:`Add a rounding line` rounding strategy.

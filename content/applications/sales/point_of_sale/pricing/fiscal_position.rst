=================================
Flexible taxes (fiscal positions)
=================================

When running a business, you may need to apply different taxes and record transactions on various
accounts based on the location and type of business of your customers and providers.

The **fiscal positions** feature enables you to establish rules that automatically select the right
taxes and accounts used for each transaction.

.. seealso::
   - :doc:`../../../finance/accounting/taxes/fiscal_positions`
   - :doc:`../../../finance/accounting/taxes`

Configuration
=============

To enable the feature, go to :menuselection:`Point of Sale --> Configuration --> Settings`, scroll
down to the :guilabel:`Accounting` section, and enable :guilabel:`Flexible Taxes`.

Then, set a default fiscal position that should be applied to all sales in the selected POS in the
:guilabel:`Default` field. You can also add more fiscal positions to choose from in the
:guilabel:`Allowed` field.

.. screenshot:: pos-fiscal-position-setting
   :menu: Point of Sale ‣ Configuration ‣ Settings
   :shows: The "Accounting" section of the POS settings with "Flexible Taxes" enabled, a default fiscal position selected and two positions listed in the "Allowed" field.
   :highlight: The "Flexible Taxes" setting block (red frame).
   :module: point_of_sale, account
   :notes: English UI, light theme, 1440px width, centered, crop to the settings block.

According to the :doc:`fiscal localization package <../../../finance/fiscal_localizations>`
activated, several fiscal positions are preconfigured and can be set and used in POS. However, you
can also :ref:`create new fiscal positions <fiscal_positions/mapping>`.

.. note::
   If you do not set a fiscal position, the tax remains as defined in the **customer taxes** field
   on the product form.

Use fiscal positions
====================

Open a :ref:`POS session <pos/session-start>` to use one of the allowed fiscal positions. Then,
click the :guilabel:`Tax` button next to the **book-shaped** icon and select a fiscal position from
the list. Doing so applies the defined rules automatically to all the products subject to the chosen
fiscal position's regulations.

.. screenshot:: pos-fiscal-position-frontend
   :menu: (POS interface) ‣ Register screen ‣ Tax
   :shows: The POS register screen with the fiscal position button open, listing the allowed fiscal positions to apply to the order.
   :highlight: The fiscal position button (red frame).
   :module: point_of_sale, account
   :notes: English UI, light theme, 1440px width, centered.

.. note::
   If a default fiscal position is set, the tax button displays the name of the fiscal position.

.. seealso::
   :doc:`../../../finance/accounting/taxes/fiscal_positions`

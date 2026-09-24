:show-content:
:show-toc:

=============
Configuration
=============

.. _configuration/settings:

Access the POS settings
=======================

To access the general POS settings, go to :menuselection:`Point of Sale --> Configuration -->
Settings`. Then, open the dropdown menu in the :guilabel:`Point of Sale` field and select the POS to
configure.

.. screenshot:: pos-configuration-select-pos
   :menu: Point of Sale ‣ Configuration ‣ Settings
   :shows: The top of the POS settings page with the "Point of Sale" dropdown open, listing the available points of sale.
   :highlight: The "Point of Sale" dropdown (red frame).
   :data: Two POS configurations: "Shop" and "Restaurant".
   :module: point_of_sale
   :notes: English UI, light theme, 1440px width, crop to the top of the settings page.

.. note::
   These settings are available to users with the :doc:`access rights </applications/general/users>`
   :guilabel:`Administration` set as :guilabel:`Settings`.

You can also configure some settings from the dashboard by clicking the vertical ellipsis button
(:guilabel:`⋮`) on a POS card. Doing so opens a popup window, from which you can:

- :doc:`Enable multiple employees to log in. <employee_login>`
- :doc:`Connect and set up an ePOS printer. <configuration/epos_ssc>`

.. screenshot:: pos-configuration-quick-settings
   :menu: Point of Sale ‣ Dashboard ‣ (POS card) ‣ ⋮
   :shows: The quick settings popup opened from the vertical ellipsis button on a POS card, with the toggles for multi-employee login and the ePOS printer.
   :module: point_of_sale
   :notes: English UI, light theme, crop to the popup window.

.. note::
   These settings are available to users with the :doc:`access rights </applications/general/users>`
   :guilabel:`Point of Sale` set as :guilabel:`Administrator`.

Make products available
=======================

To make products available for sale,

#. Go to :menuselection:`Point of Sale --> Products --> Products`.
#. Select a product to open the product form.
#. Tick the :guilabel:`Point of Sale` checkbox at the top of the form.

.. screenshot:: pos-configuration-product-available
   :menu: Point of Sale ‣ Products ‣ Products ‣ (a product)
   :shows: A product form with the "Point of Sale" checkbox at the top of the form ticked.
   :highlight: The "Point of Sale" checkbox (red frame).
   :module: point_of_sale
   :notes: English UI, light theme, 1440px width, crop to the top of the product form.

PoS product categories
======================

Configuration
-------------

POS product categories allow users to categorize products and get a more structured and clean
POS interface.

To manage PoS categories, go to :menuselection:`Point of Sale --> Configuration --> PoS Product
Categories`. To add a new category, click :guilabel:`Create`. Then, name it in the
:guilabel:`Category Name` field.

To associate a category with a parent category, fill in the :guilabel:`Parent Category` field. A
parent category groups one or more child categories.

.. example::
   .. screenshot:: pos-configuration-parent-categories
      :menu: Point of Sale ‣ Configuration ‣ PoS Product Categories
      :shows: The list of PoS product categories, showing child categories grouped under their parent categories.
      :data: Parent category "Drinks" with child categories "Soft drinks" and "Hot drinks".
      :module: point_of_sale
      :notes: English UI, light theme, 1440px width, crop to the list.

Assign PoS product categories
-----------------------------

Go to :menuselection:`Point of Sale --> Products --> Products` and open a product form. Then, go to
the :guilabel:`Point of Sale` tab and fill in the :guilabel:`Category` field under the
:guilabel:`Point of Sale` section with one or multiple PoS categories.

.. screenshot:: pos-configuration-product-category
   :menu: Point of Sale ‣ Products ‣ Products ‣ (a product) ‣ Point of Sale
   :shows: The "Point of Sale" tab of a product form with two PoS categories selected in the "Category" field.
   :highlight: The "Category" field (red frame).
   :module: point_of_sale
   :notes: English UI, light theme, 1440px width, crop to the tab.

Restrict categories
-------------------

You can limit the categories displayed on your POS interface. To achieve this, go to your :ref:`POS
settings <configuration/settings>` and choose the specific categories to display in the
:guilabel:`Restrict Categories` field within the :guilabel:`Product & PoS categories` section.

.. screenshot:: pos-configuration-restrict-categories
   :menu: Point of Sale ‣ Configuration ‣ Settings
   :shows: The "Product & PoS categories" section of the POS settings with two categories selected in the "Restrict Categories" field.
   :highlight: The "Restrict Categories" setting block (red frame).
   :module: point_of_sale
   :notes: English UI, light theme, 1440px width, crop to the settings block.


.. _pos/configuration/restrict-products:

Restrict products
=================

Beside the :guilabel:`Restrict Categories` setting above, which filters the POS product categories
shown in the interface, the *PoS Product Restriction* module (`eyssen_pos_product_restriction`)
limits which **products** are loaded into a point of sale at all. In the :ref:`POS settings
<configuration/settings>`, scroll to the :guilabel:`Product & PoS categories` section:

- :guilabel:`Restrict Product Categories`: only products belonging to one of the
  :guilabel:`Available Product Categories` are loaded. Keep :guilabel:`Include Product Category
  Descendants` enabled to also load the products of the child categories.
- :guilabel:`Restrict Product Tags`: only products carrying one of the :guilabel:`Available Product
  Tags` are loaded.

Leaving a list empty disables the corresponding restriction. Both settings are locked while a POS
session is open.

.. screenshot:: pos-configuration-product-restriction
   :menu: Point of Sale ‣ Configuration ‣ Settings
   :shows: The "Product & PoS categories" section with "Restrict Product Categories" enabled, two
      product categories selected, "Include Product Category Descendants" ticked, and "Restrict
      Product Tags" enabled with one tag selected.
   :highlight: The two restriction settings (red frame).
   :module: eyssen_pos_product_restriction
   :notes: English UI, light theme, 1440px width, crop to the settings block.

.. _pos/configuration/interface:

Interface settings
==================

The :guilabel:`PoS Interface` section of the :ref:`POS settings <configuration/settings>` controls
how the register screen behaves:

- :guilabel:`Log in with Employees`: see :doc:`employee_login`.
- :guilabel:`Large Scrollbars`: enlarges the scrollbars for imprecise industrial touchscreens.
- :guilabel:`Share Open Orders`: lets the selected :guilabel:`Trusted POS` see and take over each
  other's active orders. The trusted points of sale must use the same currency. This setting is not
  available in :doc:`restaurant mode <restaurant>` or on a kiosk.
- :guilabel:`Hide pictures in POS`: untick :guilabel:`Show product images` or :guilabel:`Show
  category images` to display text-only buttons, which speeds up the interface on slow devices.
  The :doc:`self-ordering interfaces <self_order>` are not affected.
- :guilabel:`Show margins & costs`: makes the product's cost and margin visible to every POS user in
  the product information popup, not only to managers.
- :guilabel:`Sort cart by category`: groups the cart lines according to the sequence of their PoS
  product category instead of the order in which they were added.

.. _pos/configuration/logo:

POS logo and screen saver
-------------------------

The *POS Logo & Screen Saver* module (`eyssen_pos_logo`) replaces the logo shown in the POS
navigation bar. In the :guilabel:`PoS Interface` section, set :guilabel:`Logo Option` to:

- :guilabel:`System Logo`: the default Odoo logo;
- :guilabel:`Company Logo`: the logo of the company the POS belongs to;
- :guilabel:`Custom Logo`: an image uploaded in the :guilabel:`Custom Logo` field.

Upload an image in the :guilabel:`Screen Saver Background` field to enable the screen saver: the
image is displayed full screen when the register stays idle. Leave the field empty to disable the
feature.

.. screenshot:: pos-configuration-logo-screensaver
   :menu: Point of Sale ‣ Configuration ‣ Settings
   :shows: The "POS Logo & Screen Saver" setting with "Logo Option" set to "Custom Logo", the
      uploaded logo displayed, and a screen saver background image below it.
   :highlight: The "POS Logo & Screen Saver" setting block (red frame).
   :module: eyssen_pos_logo
   :notes: English UI, light theme, 1440px width, crop to the setting block.

.. _pos/configuration/access-rules:

Access rules
------------

The *Access Management - PoS* module (`eyssen_access_management_pos`) restricts which users may open
a given point of sale. In the :guilabel:`PoS Interface` section, list the authorized users in the
:guilabel:`Access Rules` field. Leaving the field empty makes the POS available to everyone.

As soon as at least one point of sale has authorized users, the listed users only see the points of
sale they are authorized for; the record rules are regenerated automatically whenever the field
changes.

.. note::
   This feature requires the *Access Management* module (`eyssen_access_management`).

.. _pos/configuration/performance:

Performance
-----------

To keep the interface responsive, a POS session does not load the whole catalog: it loads a limited
number of products and customers and fetches the rest on demand when the cashier uses
:guilabel:`Search more`.

The *PoS Performance Optimization* module (`eyssen_pos_performance`) makes these limits
configurable per point of sale. In the :guilabel:`PoS Interface` section, set:

- :guilabel:`Limited Product Count`;
- :guilabel:`Limited Customer Count`.

Leave a field at `0` to fall back to the database-wide value (the `point_of_sale.limited_product_count`
and `point_of_sale.limited_customer_count` system parameters, or 50 when they are not set).

.. tip::
   Raise these values only as far as the register hardware allows: every additional record is loaded
   when the session opens and slows the session start down.

.. _pos/configuration/pricing-settings:

Pricing settings
================

The :guilabel:`Pricing` section of the :ref:`POS settings <configuration/settings>` gathers:

- :guilabel:`Flexible Pricelists`: see :doc:`pricing/pricelists`.
- :guilabel:`Restrict Price Modifications to Managers`: only users with the :guilabel:`Point of
  Sale` access right set to :guilabel:`Administrator` may change a price on an order.
- :guilabel:`Tax Display`: choose whether product prices are shown as :guilabel:`Tax-Excluded Price`
  or :guilabel:`Tax-Included Price` in the interface and on receipts.
- :guilabel:`Discounts` settings: see :doc:`pricing/discounts`.
- :guilabel:`Promotions, Coupons, Gift Card & Loyalty Program`: see :doc:`pricing/loyalty`.

.. _pos/configuration/accounting:

Accounting settings
===================

The :guilabel:`Accounting` section gathers the settings that drive the accounting entries generated
by the POS:

- :guilabel:`Default Sales Tax`: the tax applied to any new product created in the catalog. This
  setting is common to all points of sale.
- :guilabel:`Default Temporary Account`: the intermediary receivable account used for unidentified
  customers. This setting is common to all points of sale.
- :guilabel:`Track orders edits`: stores the successive versions of an edited order in the backend,
  so the changes made to an order after it was placed remain auditable.
- :guilabel:`Flexible Taxes`: see :doc:`pricing/fiscal_position`.
- :guilabel:`Default Journals`: the :guilabel:`Orders` journal receives the closing entry generated
  for all non-invoiced orders of a session; the :guilabel:`Invoices` journal is used for the
  :ref:`invoices issued from the POS <receipts-invoices/invoices>`.
- :guilabel:`Closing Entry by product`: breaks the automatically generated closing entry down by
  product instead of posting one line per account.

.. _pos/configuration/inventory:

Inventory settings
==================

The :guilabel:`Inventory` section determines how POS sales affect stock:

- :guilabel:`Operation Type`: the operation type used to record the pickings generated by the POS.
  Products are taken from its default source location.
- :guilabel:`Allow Ship Later`: see :doc:`shop/ship_later`.
- :guilabel:`Barcode Nomenclature`: the nomenclature used to interpret scanned barcodes. This
  setting is common to all points of sale. See :doc:`shop/barcode` and
  :doc:`pricing/discount_tags`.
- :guilabel:`Inventory Management` (visible in :doc:`developer mode
  </applications/general/developer_mode>`): choose whether stock quantities are updated at each
  order or at the closing of the session. This setting is company-specific.

.. toctree::
   :titlesonly:

   configuration/pos_groups
   configuration/epos_printers
   configuration/https
   configuration/epos_ssc

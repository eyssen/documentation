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

.. toctree::
   :titlesonly:

   configuration/epos_printers
   configuration/https
   configuration/epos_ssc

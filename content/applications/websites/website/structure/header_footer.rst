===================
Headers and footers
===================

The website header is the top section of a web page and usually contains elements such as the logo,
the :ref:`menu <website/header_footer/header-content>`, the search bar, the sign-in/customer account
button, etc. The footer is displayed at the bottom of a web page and usually contains information
such as contact details, links, legal notices, and other options.

.. _website/header_footer/header-design:

Header design
=============

To modify the header's design, click on :guilabel:`Edit`, then click on the header. The following
options are available in the :guilabel:`Header` section of the :guilabel:`Customize` tab in the
website editor:

- Choose a :guilabel:`Template` from the drop-down menu.
- Select :guilabel:`Background` settings to change the color palette through different
  :ref:`Theme styles <website/themes/theme-colors>`, :guilabel:`Custom` color options, and
  :guilabel:`Gradient` ones.
- When adding a :guilabel:`Border` to the header, its size, style, and color can be defined.
- Adapt :guilabel:`Round corners` to fit the design.
- Add a :guilabel:`Shadow` and define its :guilabel:`Color`, :guilabel:`Offset`, :guilabel:`Blur`,
  and :guilabel:`Spread`.
- Add a :guilabel:`Scroll Effect`. Hover on an effect to preview it.
- Choose the :guilabel:`Header Position` between :guilabel:`Regular`, :guilabel:`Hidden`, and
  :guilabel:`Over The Content`. When :guilabel:`Over The Content` is selected, you can customize
  the :guilabel:`Background` and :guilabel:`Text Color`.
- Show or hide :guilabel:`Elements` such as text, the search bar, :guilabel:`Sign in` button, social
  media links, :guilabel:`Contact us` button, and logo.

To finalize changes, click on :guilabel:`Save`.

.. tip::
   To hide the header, click on :guilabel:`Edit`, click on the header, and go to the
   :guilabel:`Theme` tab of the website editor. Scroll down to the :guilabel:`Advanced` section and
   toggle the :guilabel:`Show Header` switch to hide/show the header.

.. _website/header_footer/header-content:

Header content
==============

Menus organize the header’s content and help users navigate through web pages effectively.
User-friendly and well-structured menus also play a crucial role in improving
:doc:`search engine rankings <seo>`.

.. _website/header_footer/menu-editor:

Menu editor
-----------

The menu editor allows to edit the website's header and add
:ref:`menu items <website/header_footer/menu-items>` and
:ref:`mega menus <website/header_footer/mega-menus>`.

To edit the header's content, go to :menuselection:`Website --> Site --> Menu Editor`. From there,
you can:

- **rename** a menu item or change its URL using the :guilabel:`Edit Menu Item` icon;
- **delete** a menu item using the :guilabel:`Delete Menu Item` icon;
- **move** a menu item by dragging and dropping it to the desired place in the menu;
- **create a regular drop-down menu** by dragging and dropping the sub-menu items to the right,
  underneath their parent menu.

.. screenshot:: website-header_footer-menu-editor
   :menu: Website ‣ Site ‣ Menu Editor
   :shows: The Menu Editor pop-up window with the menu entries and their indented sub-menus, plus the Add Menu Item button.
   :highlight: The sub-menu entries (red frame).
   :data: Menu with the entries Home, Shop, Services (with two sub-items) and Contact us.
   :module: website
   :notes: English UI, light theme, 1440px width.

.. note::
   You can also access the menu editor by clicking :guilabel:`Edit`, selecting any menu item, and
   clicking the :guilabel:`Edit Menu` icon.

  .. screenshot:: website-header_footer-edit-menu-icon
     :menu: Website ‣ Edit ‣ (header)
     :shows: The website header in edit mode with the Edit Menu (pencil) icon that opens the Menu Editor.
     :highlight: The Edit Menu icon (red frame).
     :data: Demo website 'My Website'.
     :module: website
     :notes: English UI, light theme, 1440px width.

.. _website/header_footer/menu-items:

Add menu items
--------------

By default, pages are added to the menu as drop-down menu items when
:doc:`they are created <../structure/pages>`. To add a new menu item, follow these steps:

#. Go to :menuselection:`Website --> Site --> Menu Editor`.
#. In the menu editor, click :guilabel:`Add Menu Item`.
#. In the pop-up window, enter the :guilabel:`Name` to be displayed in the menu.
#. Type `/` in the :guilabel:`URL or Email` field to search for a page on your website or `#` to
   search for an existing custom anchor.
#. Click :guilabel:`OK`.
#. Edit the :ref:`menu structure <website/header_footer/menu-editor>` if needed, then
   :guilabel:`Save`.

Menu item design
~~~~~~~~~~~~~~~~

To modify the menu items, click on :guilabel:`Edit`, click on a menu item, then go to the
:guilabel:`Navbar` section of the website editor. The following options are available:

- Adapt the :guilabel:`Mobile Alignment`.
- Choose the :guilabel:`Font` for the menu items.
- Change the font size, color, and alignment in the :guilabel:`Format` field.
- Select a :guilabel:`Links Style` to highlight the current page in the menu.
- Change the :ref:`style of the header buttons <website/themes/button-styles>`.
- Choose to display the :guilabel:`Sub Menus` :guilabel:`On Hover` or :guilabel:`On Click`.

.. note::
   The fields available in the :guilabel:`Navbar` section can vary depending on the chosen template.

To finalize changes, click on :guilabel:`Save`.

.. _website/header_footer/mega-menus:

Mega menus
----------

Mega menus are similar to drop-down menus, but instead of a simple list of sub-menus, they display a
panel divided into groups of navigation options. This makes them suitable for websites with large
amounts of content or :doc:`e-commerce websites <../../ecommerce>`, as they can help include all of
your web pages or :doc:`e-commerce categories <../../ecommerce/products/catalog>` in the menu while
still making all menu items visible at once.

.. screenshot:: website-header_footer-mega-menu
   :menu: (website)
   :shows: The website navigation bar with a mega menu dropped down over the page, showing its columns of links and images.
   :highlight: The opened mega menu (red frame).
   :data: Mega menu 'Services' with three columns.
   :module: website
   :notes: English UI, light theme, 1440px width.

To create a mega menu, go to :menuselection:`Website --> Site --> Menu Editor` and click
:guilabel:`Add Mega Menu Item`. Enter the :guilabel:`Name` of the mega menu in the pop-up, click
:guilabel:`OK`, then :guilabel:`Save`.

To adapt the options and content of the mega menu, click on a mega menu item in the header, then
click :guilabel:`Edit`. Mega menus are composed of building blocks, which means you can customize
each component individually. For example:

- Edit the text directly in the building block.
- Edit a menu item's URL by selecting the menu item and clicking the :guilabel:`Edit link` button
  in the small preview pop-up. Type `/` to search for a page on your website, or `#` to search for
  an existing custom anchor.

  .. screenshot:: website-header_footer-mega-menu-option
     :menu: Website ‣ Edit ‣ (mega menu)
     :shows: The editor's right sidebar for a selected mega menu with the Template and Size options.
     :highlight: The Template option (red frame).
     :data: Demo website 'My Website'.
     :module: website
     :notes: English UI, light theme, 1440px width.

- Move a menu item by dragging and dropping the related block to the desired position in the mega
  menu.
- Delete a menu item by deleting the related block.

To adapt the general layout of the mega menu, go to the :guilabel:`Customize` tab of the website
editor, then, in the :guilabel:`Mega Menu` section:

- Choose a :guilabel:`Template`.
- Pick the :guilabel:`Size`: either :guilabel:`Full-Width` or :guilabel:`Narrow`.

To finalize changes, click on :guilabel:`Save`.

.. _website/header_footer/auto-mega-menus:

Automatic category mega menus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Keeping a mega menu in sync with a large eCommerce category tree by hand is tedious. The *Auto
Category Mega Menu* module (`website_sale_megamenu_category`) generates the content of a mega menu
from the :doc:`eCommerce categories <../../ecommerce/products/catalog>`.

On a mega menu item in the :guilabel:`Menu Editor`, enable :guilabel:`Auto-generate mega menu` and
set:

- :guilabel:`Starting category`: the category whose children are listed. Leave it empty to start
  from the top of the tree.
- :guilabel:`Depth`: how many levels of sub-categories are included, two by default.
- :guilabel:`Mega-menu template`: the layout used to render the generated menu.

The menu is regenerated when the category tree changes. Three buttons control it:

- :guilabel:`Regenerate`: rebuilds the menu content from the categories;
- :guilabel:`Force regenerate (discard edits)`: rebuilds it even if the menu was edited by hand,
  discarding those edits;
- :guilabel:`Detach / make manual`: stops the automatic generation and keeps the current content as
  an ordinary, hand-edited mega menu.

.. screenshot:: website-header_footer-auto-mega-menu
   :menu: Website ‣ Site ‣ Menu Editor ‣ (mega menu item)
   :shows: A mega menu item with Auto-generate mega menu enabled, the Starting category, Depth and Mega-menu template fields, and the Regenerate / Force regenerate / Detach buttons.
   :highlight: The Auto-generate mega menu checkbox and the Starting category field (red frame).
   :data: Starting category "Shop", depth 2, template "Columns".
   :module: website_sale_megamenu_category
   :notes: English UI, light theme, 1440px width.

Which categories appear in the menu is controlled on the category itself. Each eCommerce category
has a :guilabel:`Show in mega menu` state and an :guilabel:`Auto-manage menu visibility` option:
while the latter is enabled, a scheduled job hides categories that currently have no available
product and shows them again when they do, so that the menu never leads to an empty page. Turn the
option off on a category to set its visibility by hand.

The layouts themselves are managed under :menuselection:`Website --> Configuration --> Mega Menu
Templates`, where each template holds its own :guilabel:`XML`, :guilabel:`CSS` and :guilabel:`JS`,
together with a revision :guilabel:`History` that can be compared and restored.

.. screenshot:: website-header_footer-mega-menu-templates
   :menu: Website ‣ Configuration ‣ Mega Menu Templates ‣ (template)
   :shows: A mega menu template with its XML, CSS and JS tabs and the History section listing previous revisions with the Compare and Restore buttons.
   :highlight: The History section (red frame).
   :data: Template "Columns" with three revisions.
   :module: website_sale_megamenu_category
   :notes: English UI, light theme, 1440px width.

.. note::
   The generated menus are listed under :menuselection:`Website --> Configuration --> Auto Mega
   Menus`, which gives an overview of every automatically managed mega menu and of the ones whose
   content no longer matches the category tree.

Hide a dynamic menu item for non-logged in users
------------------------------------------------

To hide a dynamic menu item (i.e., a menu item generated automatically by Odoo, for example, when
you install an app or module, such as `Events`, `Courses`, etc.) for non-logged in users, follow
these steps:

#. :ref:`Enable developer mode <developer-mode>`.
#. Go to :menuselection:`Website --> Configuration --> Menus`.
#. Expand the list of menus for the relevant website if needed, then click the menu item you wish to
   hide.
#. In the :guilabel:`Visible Groups` section, click :guilabel:`Add a line` under
   :guilabel:`Group Name`.
#. Search for the group :guilabel:`User types / Portal`, select it, then click :guilabel:`Select`.
#. Save.

.. tip::
   To hide the `Shop` menu item, :doc:`restrict ecommerce access to logged-in users
   <../../ecommerce/customer_accounts>`.

.. _website/header_footer/footer-design:

Footer design
=============

To modify the footer, click on :guilabel:`Edit`, click on the footer, and in the :guilabel:`Footer`
section of the :guilabel:`Customize` tab in the website editor:

- Select a :guilabel:`Template`.
- Choose its :guilabel:`Colors`.
- Choose a :guilabel:`Slideout Effect`: :guilabel:`Regular` (i.e., no effect),
  :guilabel:`Slide Hover`, or :guilabel:`Shadow`.
- Toggle the :guilabel:`Copyright` switch to hide or show the copyright.
- Choose the :guilabel:`Border` size.
- Add a :guilabel:`Shadow`.
- Add a :guilabel:`Scroll Top Button` and choose its position.
- Hide or show the footer by toggling the :guilabel:`Page visibility` switch.

To finalize changes, click on :guilabel:`Save`.

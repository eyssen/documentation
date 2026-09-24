=================
Backend interface
=================

Several eYssen and community modules change the look and the ergonomics of the back end (the
interface used by internal users). This page describes what they add for the users, and how an
administrator can adapt the appearance to the company.

.. _backend-interface/theme:

eYssen backend theme
====================

The *eYssen Backend Theme* module (`eyssen_backend_theme`) replaces the standard navigation of the
back end and lets each company use its own colors.

.. note::
   To install the theme, go to :menuselection:`Settings --> eYssen ERP`, and, in the
   :guilabel:`General Modules` section, enable :guilabel:`eYssen ERP Backend Theme`. The theme
   installs along with it the :ref:`dialog size <backend-interface/dialog-size>` and :ref:`column
   width <backend-interface/column-width>` modules described below, the :doc:`chatter position
   <../productivity/discuss/chatter>` preference (`muk_web_chatter`), and the calculator
   (`odoo_calculator_tool`).

Home menu
---------

Click the :icon:`oi-apps` (:guilabel:`Home Menu`) icon, in the top-left corner, to open the home
menu: a full-screen panel showing the icon and the name of every application the user has access
to. Click an application to open it, or click outside the icons to close the panel.

While the home menu is open, start typing to search: the command palette opens in menu search mode
(`/`), and lists the matching menu items of all applications.

Apps bar
--------

The apps bar is a permanent shortcut bar listing the applications, so that the user can switch
from one application to another with a single click, without opening the home menu. The current
application is highlighted.

Each user chooses where the apps bar is displayed: click the profile avatar in the top-right
corner, select :guilabel:`Preferences`, and set the :guilabel:`Appsbar Position` field to one of
the following values:

- :guilabel:`Bottom Dock` (default): a floating dock centered at the bottom of the screen. Hover
  over an icon to enlarge it and display the name of the application. The dock hides itself while
  the home menu is open;
- :guilabel:`Left Small`: a narrow vertical bar on the left, with icons only;
- :guilabel:`Left Large`: a wide vertical bar on the left, with the icon and the name of each
  application, and the company's apps bar image at the bottom. On tablets, the bar shrinks to the
  icons; on mobile phones, it is hidden;
- :guilabel:`Invisible`: no apps bar.

Reload the page to apply the change.

.. screenshot:: general-backend-interface-appsbar-positions
   :menu: Avatar ‣ Preferences
   :shows: The Preferences dialog with the "Appsbar Position" selection open (Invisible, Bottom Dock, Left Small, Left Large) and, underneath, the "Dialog Size" and "Chatter Position" fields.
   :highlight: The "Appsbar Position" field (red frame).
   :module: eyssen_backend_theme, muk_web_dialog, muk_web_chatter
   :notes: English UI, light theme, crop to the dialog.

.. screenshot:: general-backend-interface-left-large
   :menu: Sales ‣ Orders ‣ Quotations
   :shows: The quotations list with the apps bar in "Left Large" position: application icons and names on the left, the current application highlighted, and the company image at the bottom of the bar.
   :highlight: The apps bar (red frame).
   :data: Demo company "YourCompany HU" with a company logo used as apps bar image.
   :module: eyssen_backend_theme
   :notes: English UI, light theme, 1440px width, full window.

Company appearance
------------------

To adapt the theme to the company, go to :menuselection:`Settings --> General Settings`, and scroll
down to the :guilabel:`Companies` section:

- :guilabel:`Backend Theme Appearance`: upload the :guilabel:`Appsbar Image`, displayed at the
  bottom of the apps bar in the :guilabel:`Left Large` position. The setting is company-specific;
  when the module is installed, the image of each company is initialized with a default image.
- :guilabel:`Backend ThemeColors`: pick the :guilabel:`Brand`, :guilabel:`Primary`,
  :guilabel:`Success`, :guilabel:`Info`, :guilabel:`Warning`, and :guilabel:`Danger` colors. The
  brand color replaces the standard Odoo brand color (e.g., in the navigation bar), the primary
  color is used for the main buttons and the links, and the four others for the corresponding
  badges, alerts, and buttons.

Click :guilabel:`Save`. The style sheets of the back end are regenerated with the new colors, and
the page reloads.

.. note::
   - The colors are stored on the company, but they are applied to the whole database: the colors
     saved last are the ones in use for all companies.
   - The :guilabel:`Favicon` field is not used yet.

.. screenshot:: general-backend-interface-theme-settings
   :menu: Settings ‣ General Settings ‣ Companies section
   :shows: The "Backend Theme Appearance" setting with the Appsbar Image and Favicon image fields, and the "Backend ThemeColors" setting with the six color pickers.
   :highlight: The two setting blocks (red frame).
   :module: eyssen_backend_theme
   :notes: English UI, light theme, 1440px width, crop to the two blocks.

Recipients of a message
-----------------------

In the chatter, clicking the :icon:`fa-envelope-o` (:guilabel:`envelope`) icon of a message lists
the recipients who were notified by email. With the theme installed, the email address of each
recipient is displayed next to their name.

.. _backend-interface/dialog-size:

Dialog size
===========

With the *MuK Dialog* module (`muk_web_dialog`), pop-up windows (dialogs) can be displayed in
full-screen mode:

- click the :icon:`fa-expand` (:guilabel:`expand`) icon in the header of a dialog to enlarge it to
  the whole window, and the :icon:`fa-compress` (:guilabel:`compress`) icon to restore it;
- to choose the initial state of all dialogs, click the profile avatar, select
  :guilabel:`Preferences`, and set :guilabel:`Dialog Size` to :guilabel:`Minimize` (default) or
  :guilabel:`Maximize`.

.. _backend-interface/column-width:

Column widths in list views
===========================

With the *List View Column width Adjustment* module (`web_listview_column_width_cr`), the width
given to a column of a list view is remembered: drag the right border of a column header to resize
the column, and the same width is applied the next time a list of the same model is displayed.

.. note::
   The widths are stored in the browser, per model and per field. They are therefore specific to
   the computer and the browser in use, and are lost when the browsing data of the site is cleared.

.. _backend-interface/no-quick-create:

Quick creation disabled in many2one fields
==========================================

When typing a new value in a many2one field (e.g., a customer on a quotation), Odoo normally offers
:guilabel:`Create "value"`, which creates the record at once with just a name. With the *No
quick_create* module (`deltatech_no_quick_create`), this option is removed from many2one fields, to
avoid incomplete contacts, products, etc. Only :guilabel:`Create and edit...` remains, which opens
the full creation form.

.. _backend-interface/clickable-tags:

Clickable tags
==============

The *Clickable Many2many Tags Widget* module (`widget_many2many_clickable`) provides a variant of
the tags field in which clicking a tag opens the form of the corresponding record. It is used, for
example, by the eYssen return merchandise (RMA) forms to jump from a tag to the linked document.
In other tags fields, clicking a tag keeps its standard behavior.

.. seealso::
   - :doc:`eyssen_erp_settings`
   - :doc:`../productivity/discuss/chatter`
   - :doc:`../essentials/keyboard_shortcuts`

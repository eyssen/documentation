=========
Knowledge
=========

The **Knowledge** app is the knowledge base of the database: internal users write, organize, and
share *pages* — rich-text documents that can be nested under each other and grouped into *spaces*.

.. note::
   The app is provided by the *Knowledge* (``knowledge``) module and uses its own rich-text editor.
   It is independent of the database's other content, so pages are edited only in the Knowledge app.

Access rights
=============

The :guilabel:`Knowledge` category of the :ref:`access rights <access-rights/users>` offers two
levels:

- :guilabel:`User`: can read the pages they have access to, write the pages they are allowed to
  edit, and manage their own pages.
- :guilabel:`Manager`: can additionally manage spaces, all pages, and the app's configuration.

Spaces
======

A **space** is a top-level container that groups related pages, e.g., one space per department or
per product. Managers create spaces in :menuselection:`Knowledge --> Configuration --> Spaces`:

- :guilabel:`Name` and :guilabel:`Icon`: how the space appears in the sidebar;
- :guilabel:`Slug`: the technical identifier, generated from the name;
- :guilabel:`Description`: a short explanation of what belongs in the space;
- :guilabel:`Sequence`: the order of the spaces in the sidebar.

Every page belongs to exactly one space, and a page can only be nested under a parent page of the
same space.

Pages
=====

Go to :menuselection:`Knowledge --> Content` to open the editor. The left sidebar shows the spaces
and, inside each of them, the page tree; the selected page is displayed on the right.

Create and organize pages
-------------------------

- Click :icon:`fa-plus` :guilabel:`New page` to add a page to a space, or :guilabel:`Add child page`
  on a page to nest a new page under it.
- Drag pages in the sidebar to reorder them.
- Give the page a :guilabel:`Title`, and click :guilabel:`Add icon` to pick an emoji shown next to
  the title in the tree. A **cover image** can be added at the top of the page and repositioned
  vertically.
- Enable :guilabel:`Wide layout` in the page settings to use the full width of the screen.

.. screenshot:: productivity-knowledge-editor
   :menu: Knowledge ‣ Content
   :shows: The Knowledge editor with the sidebar (spaces and nested page tree) on the left, a page with its icon, title and formatted body on the right, and the top bar with the favorite, lock and settings buttons.
   :data: Space "Handbook" with pages "Onboarding", "Onboarding / First week", "Processes".
   :module: knowledge
   :notes: English UI, light theme, 1440px width.

Write content
-------------

The editor toolbar offers the usual rich-text formatting:

- text styles: :guilabel:`Bold` (:command:`Ctrl` + :command:`B`), :guilabel:`Italic`
  (:command:`Ctrl` + :command:`I`), :guilabel:`Underline` (:command:`Ctrl` + :command:`U`),
  :guilabel:`Strikethrough`, and inline :guilabel:`Code`;
- structure: :guilabel:`Heading 1` to :guilabel:`Heading 3`, :guilabel:`Bullet List`,
  :guilabel:`Numbered List`, :guilabel:`Checklist`, :guilabel:`Blockquote`, :guilabel:`Callout`,
  :guilabel:`Code Block`, :guilabel:`Table`, :guilabel:`Horizontal Rule`, :guilabel:`Toggle /
  Expand` sections, and a :guilabel:`Table of Contents` generated from the headings;
- media and links: :guilabel:`Insert Link` (:command:`Ctrl` + :command:`K`), :guilabel:`Insert
  Image`, :guilabel:`Insert Video`, and :guilabel:`Insert File`.

Each time the body is saved, the page version is increased, and the page records who edited it and
when. The top bar shows the current version and the last editor.

.. screenshot:: productivity-knowledge-toolbar
   :menu: Knowledge ‣ Content
   :shows: The editor toolbar expanded above a page body that contains a heading, a checklist, a callout and a table.
   :highlight: The formatting toolbar (red frame).
   :module: knowledge
   :notes: English UI, light theme, crop to the toolbar and the first part of the body.

Favorites, locking, and trash
-----------------------------

- Click the :icon:`fa-star-o` :guilabel:`(star)` icon to :guilabel:`Add to favorites`; favorite
  pages are listed at the top of the sidebar for quick access.
- Click :guilabel:`Lock page` to prevent the title and the body from being modified;
  :guilabel:`Unlock page` restores editing.
- Click :guilabel:`Send to trash` to remove a page from the tree without deleting it. Trashed pages
  keep a :guilabel:`Deletion Date` 30 days later, and can be restored until then.

Comments
--------

Select text in the body and click :guilabel:`Add Comment` to discuss a passage with colleagues. Each
page also has a chatter, where followers are notified of the changes they are subscribed to.

Access rights of a page
=======================

By default, a page is visible to all internal users. Open the :guilabel:`Page settings` and use the
:guilabel:`Access Rights` section to change this:

- :guilabel:`Base Access` sets the level applied to every internal user: :guilabel:`Full edit`
  (write), :guilabel:`Read only`, or :guilabel:`No access`.
- :guilabel:`Custom Access` makes the page define its own access level. Without it, a page inherits
  the access of its parent page, and the settings dialog shows which page the access is inherited
  from.
- In the access list, grant a specific :guilabel:`User` or :guilabel:`Group` the
  :guilabel:`Read`  or :guilabel:`Write` permission. These entries take precedence over the base
  access.

Depending on these settings, a page is listed in one of three sidebar sections:

- :guilabel:`Team`: readable or editable by all internal users;
- :guilabel:`Personal`: base access set to :guilabel:`No access`, so only its author and the users
  explicitly granted access see it;
- :guilabel:`Collaborative`: shared with specific users or groups.

.. screenshot:: productivity-knowledge-access
   :menu: Knowledge ‣ Content
   :shows: The Page settings dialog open on the Access Rights tab, with the Base Access selection, the "Custom Access" toggle and one user line with the Write permission.
   :highlight: The "Base Access" field and the access list (red frame).
   :data: Page "Salary policy" with Base Access "No access" and one group granted "Read".
   :module: knowledge
   :notes: English UI, light theme, 1440px width.

Import articles from another database
=====================================

The *Knowledge Importer* (``knowledge_importer``) module copies articles from another Odoo database
into the Knowledge app. Go to :menuselection:`Knowledge --> Configuration --> Import` and follow the
steps:

#. :guilabel:`Select Source`: choose the import source.
#. :guilabel:`Connection Settings`: enter the :guilabel:`Odoo URL`, the :guilabel:`Database`, the
   :guilabel:`Login`, and the :guilabel:`API Key / Password` of the source database. Choose a
   :guilabel:`Target Space` to import everything into one space, or enable :guilabel:`Create spaces
   from root articles` to turn each top-level article into a space. :guilabel:`Skip "Welcome"
   articles` leaves out the personal onboarding articles.
#. :guilabel:`User Mapping`: the wizard lists the authors found in the source database and matches
   them with local users where possible; complete the :guilabel:`Local User` column for the
   remaining ones.
#. :guilabel:`Importing` and :guilabel:`Done`: the wizard reports the number of
   :guilabel:`Articles Found`, :guilabel:`Articles Imported`, and :guilabel:`Errors`, together with
   an :guilabel:`Import Log`.

.. note::
   The import requires the *Knowledge Importer* (``knowledge_importer``) module and a user with API
   access on the source database.

.. screenshot:: productivity-knowledge-import
   :menu: Knowledge ‣ Configuration ‣ Import
   :shows: The Import Knowledge wizard on the Connection Settings step, with the Odoo URL, Database, Login and API key fields, the Target Space field and the two option checkboxes.
   :data: Source database "mycompany", target space empty.
   :module: knowledge_importer
   :notes: English UI, light theme, 1440px width, use a throw-away API key.

=========
Documents
=========

The **Documents** app organizes every file stored in the database — the attachments of records, the
files uploaded from the chatter, and the documents uploaded directly — in one place, where they can
be sorted into folders, tagged, shared with a link, and used to create or complete records.

.. note::
   The app is provided by the *Document Management* (``eyssen_document_management``) module. It
   works on the standard attachments of the database, so a file uploaded on a record is immediately
   visible in Documents as well.

Access rights
=============

The module adds a :guilabel:`Document Management` category to the :ref:`access rights
<access-rights/users>` of a user:

- :guilabel:`User`: can open the Documents app, and work with the files they have access to.
- :guilabel:`Manager`: can additionally configure folders, tags, and operations.

Browse documents
================

Go to :menuselection:`Documents --> Documents` to list the files of the database. The list, kanban,
and form views show, for each document, its :guilabel:`Folder`, :guilabel:`Tags`, the related
:guilabel:`Partner` and :guilabel:`Model`, and the file :guilabel:`Type`.

The search panel and the search view help narrow the list down:

- group the documents by :guilabel:`Folder`, :guilabel:`Model`, :guilabel:`Partner`,
  :guilabel:`Tag`, or :guilabel:`Type`;
- use the :guilabel:`Hide JS/CSS`, :guilabel:`Hide View Model`, and :guilabel:`Hide Without Model`
  filters to leave out the technical attachments that Odoo stores together with the business files.

Each document has a chatter, so notes and activities can be logged on a file itself.

.. screenshot:: productivity-documents-overview
   :menu: Documents ‣ Documents
   :shows: The Documents kanban view with the search panel on the left (folders), several document cards with their tags, and the group-by menu open.
   :data: Demo company "YourCompany HU"; folders "Contracts", "Invoices"; tags "Signed", "Draft".
   :module: eyssen_document_management
   :notes: English UI, light theme, 1440px width.

Download several documents
--------------------------

To download several documents at once, select them in the list view, click the :icon:`fa-cog`
:guilabel:`Actions` button, and select :guilabel:`Download Files`. Odoo proposes a file name for the
archive (`files_<date>.zip`); confirm with :guilabel:`Download Files` to get all selected documents
in a single ZIP file.

.. note::
   The file name must end with `.zip`.

Folders
=======

Folders classify documents and can be nested. To create one, go to :menuselection:`Documents -->
Configuration --> Folders` and click :guilabel:`New`:

- :guilabel:`Folder Name` and :guilabel:`Parent Folder`: the position of the folder in the tree. The
  :guilabel:`Complete Name` of a folder shows its full path, e.g. `Contracts / 2026`.
- :guilabel:`Company`: leave empty to make the folder available to all companies.
- :guilabel:`Sequence`: the order of the folders.

The :guilabel:`Documents` smart button opens the documents filed in the folder, and the
:guilabel:`Child Folders` tab lists its subfolders.

Automatic folders
-----------------

In the :guilabel:`Automatic Folder` section, an :guilabel:`Auto Model` can be selected. Documents
attached to a record of that model are then filed automatically in the folder, without the user
having to select it. Subfolders of an automatic folder inherit this behavior.

.. screenshot:: productivity-documents-folder-form
   :menu: Documents ‣ Configuration ‣ Folders
   :shows: A folder form with the folder name, the parent folder, the Settings group, the Automatic Folder group with the Auto Model field, and the Documents smart button.
   :highlight: The "Automatic Folder" group (red frame).
   :data: Folder "Project files" with Auto Model "Task".
   :module: eyssen_document_management
   :notes: English UI, light theme, 1440px width.

Tags
====

Tags describe the content of a document. They are grouped into **tag categories**, and both the
categories and the tags can be attached to a folder, so that only the relevant tags are proposed on
a document of that folder.

To manage them, go to :menuselection:`Documents --> Configuration --> Tags`. Create a category, give
it a :guilabel:`Folder` if it should only apply there, and add the :guilabel:`Tags` with their
:guilabel:`Color`. A tag name must be unique within its category, and a category name must be unique
within its folder.

Share a document
================

Open a document and, in the :guilabel:`Share` section of the form, click :guilabel:`Share File`.
Odoo generates a share :guilabel:`URL` that can be copied with the :icon:`fa-clipboard`
:guilabel:`(copy)` icon and sent to anyone: the link gives access to the file without logging in.
Click :guilabel:`Unshare File` to invalidate the link.

Both actions are logged in the document's chatter, with the user and the date.

.. screenshot:: productivity-documents-share
   :menu: Documents ‣ Documents
   :shows: A document form with the Organize group (folder, tags) and the Share group showing the generated share URL with its copy icon and the "Unshare File" button.
   :highlight: The "Share" group (red frame).
   :data: Document "Contract - Deco Addict.pdf" in folder "Contracts", shared.
   :module: eyssen_document_management
   :notes: English UI, light theme, 1440px width, use a throw-away token.

Operations
==========

An **operation** turns a document into a record, or links it to an existing one — for example, to
register a vendor bill from a received PDF, or to attach a signed contract to a project task.

To define an operation, go to :menuselection:`Documents --> Configuration --> Operations` and click
:guilabel:`New`:

- :guilabel:`Operation Name`: the name proposed to the user.
- :guilabel:`Folders` and :guilabel:`Models`: restrict the operation to documents in specific
  folders or attached to specific models. Leave empty to apply it everywhere.
- :guilabel:`Operation`: :guilabel:`Creating a New Record` or :guilabel:`Link to an Existing
  Record`.
- :guilabel:`Model for the Operation`: the model of the record to create or to link to, and,
  optionally, a :guilabel:`Filter for the Operation Model` restricting the records proposed.

To run an operation, open a document and click :guilabel:`Operations` in the :guilabel:`Organize`
section. Select the :guilabel:`Operation` and the target :guilabel:`Record`, then save: the document
is attached to that record.

.. screenshot:: productivity-documents-operation
   :menu: Documents ‣ Documents
   :shows: The Operation Wizard dialog open from a document, with the Operation field and the Record reference field filled in.
   :data: Operation "Attach to task", record "Website redesign" (project task).
   :module: eyssen_document_management
   :notes: English UI, light theme, 1440px width.

Documents of a contact
======================

A :guilabel:`Documents` smart button on the contact form opens the documents linked to that contact.
Odoo determines the contact of a document from the record the document is attached to.

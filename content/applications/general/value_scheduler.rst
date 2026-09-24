===============
Value scheduler
===============

The *eYssen Value Scheduler* application (`value_scheduler`) changes the value of one field on many
records at once, from a two-column CSV or Excel file, either immediately or at a date and time
chosen in advance. Typical examples are price list tags that must be switched at the start of a
promotion, or product attributes to be updated for a whole supplier catalog during the night.

Every operation relies on a **preset**, prepared once by an administrator, which defines the model
and the field to update and how the records are found. The users then only have to upload a file.

.. note::
   The application requires the *Price List Validation by Tags* module
   (`eyssen_product_pricelist_tag`), which is installed along with it.

.. _value-scheduler/access:

Access rights
=============

In the :doc:`access rights <users/access_rights>` of a user, the :guilabel:`Value Scheduler`
category has two levels:

- :guilabel:`Scheduler`: can open the application, and create, process, schedule, and cancel
  imports with the existing presets;
- :guilabel:`Administrator`: in addition, has access to the :guilabel:`Developer` menu: the
  :guilabel:`Preset Editor` and the list of :guilabel:`All Scheduled Changes`.

.. _value-scheduler/import:

Import a file
=============

#. Open the :guilabel:`Value Scheduler` app, and, in the :guilabel:`Operations` menu, click the
   operation to perform (e.g., :guilabel:`Pricelist Tag Update`). The list of the previous imports of
   that operation is displayed.
#. Click :guilabel:`New`, and upload the file in the :guilabel:`File` field.
#. Select the :guilabel:`Run Mode`:

   - :guilabel:`Timed`: the changes are applied at the :guilabel:`Scheduled Date`, which becomes
     mandatory;
   - :guilabel:`Instant`: the changes are applied as soon as the file is processed. This mode is
     limited to 25 changes per import.

#. Select the :guilabel:`Write Mode`:

   - :guilabel:`Overwrite`: the value of the file replaces the current value of the field. For a
     tags field, an empty second column empties the field;
   - :guilabel:`Extend`: for a tags field, the values of the file are added to the existing ones;
   - :guilabel:`Remove`: for a tags field, the values of the file are removed from the existing
     ones. Tick :guilabel:`Clear All` to empty the field instead, whatever the second column
     contains. For any other field, the field is emptied.

#. Click :guilabel:`Process`. The file is read, one *scheduled change* is created per row, and the
   file is attached to the chatter of the import. If a row cannot be interpreted (e.g., an unknown
   tag name), the whole file is refused, and the message lists the rows to correct.

In :guilabel:`Timed` mode, the import and its changes move to the :guilabel:`Scheduled` status. In
:guilabel:`Instant` mode, the changes are executed right away, and the import moves to
:guilabel:`Done`.

.. screenshot:: general-value-scheduler-import-form
   :menu: Value Scheduler ‣ Operations ‣ Pricelist Tag Update ‣ New
   :shows: A draft import form with the Process button, the uploaded file, Run Mode "Timed" with a scheduled date, and Write Mode "Extend".
   :highlight: The "Run Mode" and "Write Mode" radio buttons (red frame).
   :data: File "promo_tags_week40.csv"; scheduled date next Monday 00:00.
   :module: value_scheduler
   :notes: English UI, light theme, 1440px width.

File format
-----------

The file is either a CSV file (`;` separator, UTF-8 or Latin-1 encoding) or an Excel workbook
(`.xlsx`), of which only the first sheet is read. The first row is a header and is ignored. Each
following row has two columns:

#. the **lookup value**, used to find the record(s) to update. The field it is compared with is
   defined by the preset (e.g., the internal reference of the product). Rows with an empty first
   column are skipped;
#. the **new value**. How it is interpreted depends on the preset; for the *Pricelist Tag Update*
   preset, it is a comma-separated list of price list tag names (not case-sensitive).

.. code-block:: text

   reference;tags
   FURN_0096;Promo week 40, Wholesale
   FURN_1118;Promo week 40

.. warning::
   Do not use apostrophes (`'`) in the lookup values: such rows cannot be matched.

.. _value-scheduler/follow-up:

Follow up and cancel an import
==============================

Scheduled changes are applied by the *Value Scheduler: Process Timed Changes* scheduled action,
which runs every five minutes and processes the due changes in batches of 25, until none is left.
A change is therefore applied within a few minutes after its :guilabel:`Scheduled Date`.

On the import, the :guilabel:`Changes` smart button and the :guilabel:`Scheduled Changes` tab show
the changes with their :guilabel:`Lookup` value, the :guilabel:`Modifier` (the value of the file),
and, once executed, the :guilabel:`Old Value` and the :guilabel:`Result`. Click the
:icon:`fa-search` icon of a line to open the matching records. The status of a change is one of the
following:

- :guilabel:`Draft`: created, not queued yet;
- :guilabel:`Scheduled`: waiting for its date;
- :guilabel:`Done`: the value was changed;
- :guilabel:`Unchanged`: the records already had the requested value;
- :guilabel:`Failed`: the change could not be applied; the reason is given in the
  :guilabel:`Notes` tab of the change (e.g., no record found for the lookup value).

An import is :guilabel:`Done` when all its changes have been processed without failure, and
:guilabel:`Failed` if at least one of them failed.

The following buttons are available on the import:

- :guilabel:`Cancel`: on a :guilabel:`Scheduled` import of which no change has been executed yet,
  moves the import to :guilabel:`Cancelled`; its changes go back to :guilabel:`Draft` and are not
  applied;
- :guilabel:`Reset to Draft`: brings the import back to :guilabel:`Draft`, together with its
  scheduled and failed changes, e.g., to modify the scheduled date;
- :guilabel:`Schedule`: on a draft import that already has changes, queues them again without
  reading the file a second time.

Only draft imports can be deleted.

.. note::
   In :guilabel:`Instant` mode, a *Value Scheduler* note is posted in the chatter of each updated
   record, with the old value, the value of the file, and the resulting value. Changes applied by
   the scheduled action do not post such a note, and the usual field tracking is disabled in both
   modes: use the :guilabel:`Old Value` and :guilabel:`Result` columns of the import as the audit
   trail.

.. _value-scheduler/presets:

Presets
=======

Presets are managed by the administrators of the application in :menuselection:`Value Scheduler
--> Developer --> Preset Editor`. A preset is defined by:

- :guilabel:`Name` and :guilabel:`Menu Name`, the label of its entry in the :guilabel:`Operations`
  menu;
- :guilabel:`Target Model` and :guilabel:`Target Field`: the model and the field to update;
- :guilabel:`Domain Lookup Field`: the technical name of the field of the target model that is
  compared with the first column of the file;
- :guilabel:`Code`: optionally, Python code that converts the rows of the file into changes, e.g.,
  to turn tag names into records and to report unknown names. Without code, the second column is
  written as is, which suits text and number fields.

Click :guilabel:`Install` to create the entry of the preset in the :guilabel:`Operations` menu, and
:guilabel:`Uninstall` to remove it. The :guilabel:`Imports` smart button lists the imports made with
the preset.

The application is delivered with one preset, *Pricelist Tag Update*, which updates the
:guilabel:`Pricelist Tags` of the products.

.. important::
   - The *Pricelist Tag Update* preset is delivered with `master_article_number` as
     :guilabel:`Domain Lookup Field`. This field is not part of the standard product form: before
     installing the preset, replace it with the field that identifies your products in the file,
     e.g., `default_code` (internal reference) or `barcode`.
   - The code of a preset is executed on the server. Only trusted administrators should be
     granted the :guilabel:`Administrator` level.

:menuselection:`Value Scheduler --> Developer --> All Scheduled Changes` lists the changes of all
imports, with filters by status and grouping by import, model, and scheduled date.

.. screenshot:: general-value-scheduler-preset
   :menu: Value Scheduler ‣ Developer ‣ Preset Editor ‣ Pricelist Tag Update
   :shows: The preset form with the Install button, the Configuration group (name, menu name, sequence), the Target group (Target Model "Product", Target Field "Pricelist Tags", Domain Lookup Field) and the Row Processing Code editor.
   :highlight: The "Domain Lookup Field" (red frame).
   :data: Domain Lookup Field set to "default_code".
   :module: value_scheduler
   :notes: English UI, light theme, 1440px width.

.. seealso::
   - :doc:`../inventory_and_mrp/inventory/product_management/pricing_extensions`
   - :doc:`../essentials/export_import_data`

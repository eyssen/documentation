==============================
Background printing and export
==============================

Printing hundreds of invoices in one go, or exporting tens of thousands of lines, can take longer
than a web page is allowed to wait: the browser then shows an error although the server is still
working. To avoid this, large print and export requests are executed **in the background**: the
user keeps working, and is notified when the file is ready to download.

Two modules provide this behavior:

- *Asynchronous Report Printing* (`report_async_print`), for PDF reports;
- *Asynchronous List Export* (`export_async`), for the exports of list views.

Both rely on the *Job Queue* module (`queue_job`) to execute the jobs.

.. _background-jobs/print:

Background printing
===================

Select the records in a list view, and print a report from the :icon:`fa-print` :guilabel:`Print`
menu, as usual. When the number of selected records reaches the :ref:`threshold
<background-jobs/print-settings>` (20 by default), the report is not downloaded directly. Instead:

#. a notification confirms that the documents are being prepared in the background;
#. once the PDF is ready, a sticky notification with a :guilabel:`Download` button is displayed,
   and a *Report ready* message with a link to the file is sent to the user's :doc:`inbox
   <../productivity/discuss>`. If the generation failed, the notification and the message contain
   the error instead.

The file can also be downloaded later from :menuselection:`Print Jobs --> My Print Jobs`, where each
job shows the report, the model, the number of records, and its :guilabel:`Status`
(:guilabel:`Queued`, :guilabel:`Processing`, :guilabel:`Done`, or :guilabel:`Failed`). Click
:guilabel:`Download` on a done job to get the file.

.. note::
   - Only PDF reports are concerned. Smaller selections, and other report types, are downloaded
     directly as before.
   - The report is generated with the access rights of the user who requested it.
   - Users only see their own jobs; administrators (:guilabel:`Administration: Settings`) see the
     jobs of all users.
   - Jobs and their files are deleted automatically after seven days. Download the file again, or
     print again, if needed later.

.. screenshot:: essentials-background-jobs-print-notification
   :menu: Accounting ‣ Customers ‣ Invoices (30 invoices selected, Print ‣ Invoices)
   :shows: The invoice list with the green sticky notification "Your document … is ready." and its Download button in the top-right corner.
   :highlight: The notification (red frame).
   :data: 30 posted customer invoices selected.
   :module: report_async_print
   :notes: English UI, light theme, 1440px width.

.. _background-jobs/print-settings:

Configuration
-------------

Go to :menuselection:`Settings --> General Settings`, and scroll down to the :guilabel:`Background
Printing` section. In :guilabel:`Bulk print threshold`, enter the number of records from which
printing runs in the background. Enter `0` to disable background printing.

The threshold can be overridden report by report: in :ref:`developer mode <developer-mode>`, go to
:menuselection:`Settings --> Technical --> Actions --> Reports`, open the report, and set the
:guilabel:`Async Print Threshold` field:

- `0`: use the global threshold;
- a positive number: use this threshold for this report, e.g., a lower one for a report that is
  slow to generate;
- `-1`: never print this report in the background.

.. note::
   The global threshold is read by the browser when the page is loaded. After changing it, the users
   have to reload the page for the new value to be taken into account.

.. _background-jobs/export:

Background export
=================

:ref:`Export <essentials/export_import_data/export-data>` the records of a list view as usual: select the records (or all the
records of the search), click :menuselection:`Action --> Export`, choose the fields and the format,
and click :guilabel:`Export`. When the number of records reaches the :ref:`threshold
<background-jobs/export-settings>` (2,000 by default), the export runs in the background:

#. a notification confirms that the export is being prepared;
#. the records are exported in successive batches. When the file is complete, a sticky notification
   with a :guilabel:`Download` button is displayed, and an *Export ready* message with a link to the
   file is sent to the user's inbox.

The progress of an export can be followed in :menuselection:`Export Jobs --> My Export Jobs`: the
:guilabel:`Progress Offset` column shows how many of the :guilabel:`Records` have been exported so
far. Click :guilabel:`Download` on a done job to get the file.

.. note::
   - Both the XLSX and the CSV formats are supported, as well as the :guilabel:`I want to update
     data (import-compatible export)` option.
   - The export of a **grouped** list always runs directly, whatever the number of records, unless
     the import-compatible option is ticked.
   - The visibility of the jobs and their automatic deletion after seven days follow the same rules
     as for the print jobs.

.. _background-jobs/export-settings:

Configuration
-------------

Go to :menuselection:`Settings --> General Settings`, and scroll down to the :guilabel:`Background
Export` section:

- :guilabel:`Bulk export threshold`: the number of records from which an export runs in the
  background (2,000 by default). Enter `0` to disable background export;
- :guilabel:`Chunk batch size`: the number of records processed per batch (200 by default). Lower
  it if exports containing heavy computed columns, such as price list prices, fail or take too long.

As for printing, the users have to reload the page after a change of the threshold.

.. _background-jobs/queue:

Job queue
=========

Background jobs are executed by the *Job Queue* module (`queue_job`), a technical module that is
also used by other features to defer long operations.

Users who belong to the :guilabel:`Job Queue Manager` group have access to the
:menuselection:`Job Queue --> Queue --> Jobs` menu, which lists all the jobs of the database with
their state, their execution time, and, for a failed job, the error. From a job, the
:guilabel:`Requeue Job`, :guilabel:`Set to 'Done'`, and :guilabel:`Cancel job` buttons allow to run
a failed job again, or to discard it.

.. important::
   The jobs are only executed if the job runner is enabled in the configuration of the server. If
   the print or export jobs stay in the :guilabel:`Queued` status, contact your system
   administrator or your hosting provider.

.. seealso::
   - :doc:`export_import_data`
   - :doc:`reporting`

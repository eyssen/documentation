=========
Documents
=========

Each equipment can have multiple documents attached — manuals, certificates, calibration records,
warranty documents, service books, and more.

.. image:: equipment-documents-tab.png
   :alt: Documents tab on equipment form

Document types
==============

Each document has a **type** that categorizes it:

- **Manual**: User manuals, operating instructions.
- **Certificate**: Compliance certificates, safety certifications.
- **Calibration**: Calibration certificates and records.
- **Warranty**: Warranty documentation.
- **Service Book**: Service history and maintenance logs.
- **Other**: Any other document type.

Adding documents
================

Documents can be added directly on the equipment form in the :guilabel:`Documents` tab:

#. Click :guilabel:`Add a line` in the documents table.
#. Enter a **Name** for the document.
#. Select the **Type**.
#. Set the **Expiry Date** if applicable (especially important for certificates, calibrations, and
   warranties).
#. Upload the **File**.
#. Optionally add **Notes**.

Documents can also be accessed from the :guilabel:`Documents` stat button, which opens the full
document list view with advanced filtering and grouping.

Expiry tracking
===============

Documents with an **Expiry Date** are automatically monitored by a daily scheduled job. When a
document's expiry date is within the configured warning period (default: 30 days), the system
creates an **activity** on the equipment record to alert the assigned user.

**How it works:**

- The cron runs daily and checks all documents where the expiry date falls within the warning
  period.
- Only equipment in *Active* state is checked.
- A warning activity is created for each expiring document, assigned to the equipment's first
  assignee (or the company admin as fallback).
- Duplicate activities are prevented — if a warning activity already exists for the same document,
  no new one is created.

**Configuring the warning period:**

Navigate to :menuselection:`Equipment Management --> Settings --> Configuration --> Automation -->
Document Expiry Warning` and set the number of days. The default is 30 days.

.. note::
   The expiry tracking applies to all document types, not just calibration documents. If you have
   a warranty expiring in 30 days, you'll receive a notification too.

Searching and filtering documents
==================================

The standalone document list view (accessible via the Documents stat button) includes:

- **Filter: Expiring (30 days)**: Shows documents expiring within the next 30 days.
- **Filter: Expired**: Shows documents past their expiry date.
- **Group By: Type**: Groups documents by their type.
- **Group By: Equipment**: Groups documents by their parent equipment.

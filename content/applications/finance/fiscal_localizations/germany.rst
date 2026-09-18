=======
Germany
=======

Accounting
==========

Chart of accounts
-----------------

Both SKR03 and SKR04 charts of accounts are supported in Odoo. When a new database is created for
a German company, SKR03 is installed by default.

Verify which is installed by going to :menuselection:`Accounting --> Configuration --> Settings`
and checking the :guilabel:`Package` field under the :guilabel:`Fiscal Localization` section.

.. warning::
   Selecting another package is only possible if you have not created an accounting entry. If one
   was posted, a new company or database must be set up to select another package. In
   addition, all journal entries will need to be created again.

.. note::
   The German versions of the financial reports (balance sheet, profit & loss, Umsatzsteuervoranmeldung,
   EC sales list, Intrastat), the DATEV exports, the GoBD XML export, and the certified Point of
   Sale with a technical security system (TSS / DSFinV-K) are **not** available in this edition.
   The generic :doc:`financial reports <../accounting/reporting>`, the :doc:`tax report
   <../accounting/reporting/dynamic_reports>` (with the German UStVA grids) and the
   :doc:`Intrastat declaration <../accounting/reporting/intrastat>` can be used instead.

.. _germany/gobd:

GoBD compliance
---------------

**GoBD** stands for *Grundsätze zur ordnungsmäßigen Führung und Aufbewahrung von Büchern,
Aufzeichnungen und Unterlagen in elektronischer Form sowie zum Datenzugriff*. In short, it is a
guideline for the proper management and storage of books, records, and documents in electronic form,
as well as for data access, that is relevant for the German tax authority, tax declaration, and
balance sheet.

These principles have been written and published by the Federal Ministry of Finance (BMF) in
November 2014. Since January 2015, **they have become the norm** and have replaced previously
accepted practices linked to computer-based accounting. Several changes have been made by the BMF in
2019 and January 2020 to specify some of the content due to the development of digital solutions
(cloud hosting, paperless companies, etc.).

.. important::
   Odoo is certified **GoBD-compliant**.

Understanding GoBD in relation to accounting software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **GoBD is binding for companies that have to present accounts**, which includes SMEs,
freelancers, and entrepreneurs, to the financial authorities. As such, **the taxpayer himself is the
sole responsible** for the complete and exhaustive keeping of fiscal-relevant data (above-mentioned
financial and related data).

Apart from software requirements, the user is required to ensure internal control systems (*in
accordance with sec. 146 of the Fiscal Code*):

- access rights control;
- segregation of duties, functional separating;
- entry controls (error notifications, plausibility checks);
- reconciliation checks at data entry;
- processing controls; and
- measures to prevent intentional or unintentional manipulation of software, data, or documents.

The user must distribute tasks within their organization to the relevant positions (*control*) and
verify that the tasks are properly and completely performed (*supervision*). The result of these
controls must be recorded (*documentation*), and should errors be found during these controls,
appropriate measures to correct the situation should be put into place (*prevention*).

Data security
~~~~~~~~~~~~~

The taxpayer must **secure the system against any data loss** due to deletion, removal, or theft of
any data. If the entries are not sufficiently secured, the bookkeeping will be regarded as not in
accordance with the GoBD guidelines.

Once bookings have been finally posted, they can no longer be changed or deleted via the
application.

- If the database is hosted by a hosting provider, check which backup guarantees are part of the
  service. In addition, regular backups can be downloaded and backed up on external systems.
- If the server is operated locally, the user is responsible for creating the necessary backup
  infrastructure.

.. important::
   In some cases, data has to be kept for ten years or more, so always have backups saved. It is
   even more important if you decide to change software provider.

Responsibility of the software editor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Considering GoBD applies only to the taxpayer, **the software editor can by no means be held
responsible for the accurate and compliant documentation of their users' financial transactional
data**. It can merely provide the necessary tools for the user to respect the software-related
guidelines described in the GoBD.

Ensuring compliance through Odoo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The keywords, when it comes to GoBD are: **traceable, verifiable, true, clear, and continuous**.
In short, you need to have audit-proof archiving in place, and Odoo provides you with the means to
achieve all of these objectives:

#. | **Traceability and verifiability**
   | Each record in Odoo is stamped with the creator of the document, the creation date, the
     modification date, and who modified it. In addition, relevant fields are tracked. Thus, it can
     be seen which value was changed by whom in the chatter of the relevant object.
#. | **Completeness**
   | All financial data must be recorded in the system, and there can be no gaps. Odoo ensures that
     there is no gap in the numbering of the financial transactions. It is the responsibility of the
     user to encode all financial data in the system. As most financial data in Odoo is generated
     automatically, it remains the responsibility of the user to encode all vendor bills and
     miscellaneous operations completely.
#. | **Accuracy**
   | Odoo ensures that, with the correct configuration, the correct accounts are used. In addition,
     the control mechanisms between purchase orders and sales orders and their respective invoices
     reflect the reality of the business. It is the responsibility of the user to scan and attach
     the paper-based vendor bill to the respective record in Odoo.
#. | **Timely booking and record-keeping**
   | As most financial data in Odoo is generated by the transactional objects (for example, the
     invoice is booked at confirmation), Odoo ensures out-of-the-box timely record-keeping. It is
     the responsibility of the user to encode all incoming vendor bills in a timely manner, as well
     as the miscellaneous operations.
#. | **Order**
   | Financial data stored in Odoo is, per definition, ordered and can be reordered according to
     most fields present in the model. A specific ordering is not enforced by the GoBD, but the
     system must ensure that a given financial transaction can be quickly found by a third-party
     expert. Odoo ensures this out-of-the-box.
#. | **Inalterability**
   | With the German Odoo localization, Odoo is in standard configured in such a way that the
     inalterability clause can be adhered to without any further customization.

GoBD export
~~~~~~~~~~~

In the case of fiscal control, the fiscal authority can request three levels of access to the
accounting system (Z1, Z2, Z3). These levels vary from direct access to the interface to the
handover of the financial data on a storage device.

In the case of a handover of financial data to a storage device, the GoBD does **not** enforce the
format. It can be, for example, in XLS, CSV, XML, Lotus 123, SAP-format, AS/400-format, or else.
Odoo supports the CSV and XLSX export of financial data out of the box (list views and the
:doc:`dynamic reports <../accounting/reporting/dynamic_reports>`). The GoBD **recommends** the
export in a specific XML-based GoBD format (see "Ergänzende Informationen zur
Datenträgerüberlassung" §3), but it is not binding; this XML export is not available in this
edition.

Non-compliance
~~~~~~~~~~~~~~

In the event of an infringement, you can expect a fine and a court order demanding the
implementation of specific measures.

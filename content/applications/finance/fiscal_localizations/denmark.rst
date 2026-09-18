=======
Denmark
=======

Modules
=======

The following modules are installed automatically for Danish companies:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Denmark - Accounting`
     - `l10n_dk`
     - Default :ref:`fiscal localization package <fiscal_localizations/packages>`: Danish chart of
       accounts, taxes and tax grids.
   * - :guilabel:`Denmark - FIK Number`
     - `l10n_dk_fik`
     - Uses a FIK payment reference (+71 or +75) as the payment communication on customer invoices.
   * - :guilabel:`Denmark - E-invoicing`
     - `l10n_dk_oioubl`
     - Adds the OIOUBL 2.1 electronic invoice format.
   * - :guilabel:`Denmark EDI - Nemhandel`
     - `l10n_dk_nemhandel`
     - Sends and receives OIOUBL documents through the Nemhandel network (with the *Nemhandel
       Business Response* module for the business-level responses).

FIK payment reference
=====================

The Danish FIK (*Fælles Indbetalingskort*) reference lets the customer's bank match a payment to
the invoice automatically. To use it, open the sales journal (:menuselection:`Accounting -->
Configuration --> Journals`), go to the :guilabel:`Advanced Settings` tab and set the
:guilabel:`Communication Standard` to :guilabel:`Denmark FIK Number (+71)` or :guilabel:`Denmark
FIK Number (+75)`. The :guilabel:`FIK Creditor Number` is filled in automatically from the
company's first bank account number and can be edited.

Every invoice posted in that journal gets a *Payment Reference* of the form
`+71<invoice number with check digit>+<creditor number>`, printed on the invoice.

.. note::
   The FIK +71 reference supports invoice numbers of up to 14 digits, and +75 up to 15 digits;
   longer invoice numbers raise an error when the reference is generated.

.. screenshot:: finance-fl-denmark-fik-journal
   :menu: Accounting ‣ Configuration ‣ Journals ‣ Customer Invoices ‣ Advanced Settings tab
   :shows: The Advanced Settings tab of the Customer Invoices journal with "Communication Standard" set to "Denmark FIK Number (+71)" and the computed "FIK Creditor Number" field below it.
   :highlight: The "Communication Standard" and "FIK Creditor Number" fields.
   :data: Demo company "YourCompany DK", bank account DK50 0040 0440 1162 43.
   :module: l10n_dk_fik
   :notes: English UI, light theme, 1440px width.

Nemhandel e-invoicing
=====================

Danish companies exchange electronic invoices in the OIOUBL format over the Nemhandel network. In
:menuselection:`Accounting --> Configuration --> Settings`, the :guilabel:`Nemhandel E-Delivery`
block lets you register the company on the network: click :guilabel:`Start sending via Nemhandel`,
choose the :guilabel:`EDI mode` (:guilabel:`Demo`, :guilabel:`Test`, or :guilabel:`Live`), enter
the :guilabel:`Identifier Type` / :guilabel:`Identifier Value` (e.g., the CVR number), the contact
:guilabel:`Email` and :guilabel:`Phone`, and confirm the code received by SMS. Once the
:guilabel:`Nemhandel status` is *active*, invoices sent to partners whose :guilabel:`Nemhandel
Endpoint` is verified are delivered electronically from the :guilabel:`Send & Print` window, and
incoming documents are created in the :guilabel:`Incoming Invoices Journal` set in the same block.

.. note::
   The Nemhandel connection goes through an access-point service operated by Odoo S.A.; the
   registration requires a public URL for the database. Use the :guilabel:`Demo` mode to test the
   flow without sending anything to the network.

.. screenshot:: finance-fl-denmark-nemhandel-settings
   :menu: Accounting ‣ Configuration ‣ Settings ‣ Nemhandel E-Delivery
   :shows: The "Nemhandel E-Delivery" settings block of a Danish company: Nemhandel status "Active", the Nemhandel Address (CVR), Contact Email, Incoming Invoices Journal, and the "Update contact details" / "Deregister" buttons.
   :highlight: The "Nemhandel status" line.
   :data: Demo company "YourCompany DK" registered in Demo mode.
   :module: l10n_dk_nemhandel
   :notes: English UI, light theme, 1440px width; use a test/demo registration.

Bookkeeping Act compliance
==========================

The Danish Bookkeeping Act requires a digital bookkeeping system to retain transactions and
receipts for five years, to prevent the deletion or backdating of recorded transactions, to keep
the data accessible in a machine-readable format, and to be able to deliver it in decrypted form.
Odoo's accounting supports these requirements through immutable posted entries (posted documents
cannot be deleted, all changes are logged in the chatter), receipts stored as attachments in the
database, and standard database backups (SQL dump + ZIP archive of the attachments). The
registration of the system with the Danish Business Authority and the backup retention guarantees
are, however, the responsibility of your hosting provider; check with them which guarantees apply to
your database.

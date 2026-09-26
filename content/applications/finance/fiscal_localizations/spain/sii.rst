============================================
SII (Suministro Inmediato de Información)
============================================

With the :ref:`Spain - Base Layer <localizations/spain/base-layer>`, the SII (*Llevanza de libros
registro del IVA a través de la Sede electrónica de la AEAT*) is handled by the *Suministro
Inmediato de Información en el IVA* module. It sends the VAT data of customer invoices and vendor
bills to the web service of the AEAT, or of the regional tax agency of the company. The SII is
mandatory for companies with a turnover above 6 M€, for the taxpayers registered in the REDEME, and
optional for the others.

.. note::
   The standard *Spain - SII EDI Suministro de Libros* module described in :ref:`the SII section of
   the Spain page <localizations/spain/sii>` cannot be installed together with the base layer.

Configuration
=============

Certificate
-----------

The requests are signed with the electronic certificate of the company (a :file:`.p12` or
:file:`.pfx` file).

#. Go to :menuselection:`Accounting --> Configuration --> AEAT --> Certificates AEAT` and click
   :guilabel:`New`.
#. Enter a name, upload the certificate :guilabel:`File`, and enter a :guilabel:`Folder Name`.
#. Click :guilabel:`Obtain Keys`, enter the password of the certificate, and confirm with
   :guilabel:`Obtain Keys`.
#. Click :guilabel:`To Active` to use this certificate.

.. tip::
   The certificate is also used by the other AEAT web services, such as the check of contact data
   against the AEAT census.

Company
-------

Open the company form (:ref:`Settings app <general/companies/company>`) and:

#. In the :guilabel:`AEAT` tab, check the :guilabel:`Tax Agency` (the AEAT or a regional tax
   agency).
#. In the :guilabel:`SII` tab, tick :guilabel:`Enable SII`, then set:

   - :guilabel:`Sii Start Date`: invoices dated before this date are not sent;
   - :guilabel:`Is it the SII test environment?`: keep it ticked while testing; untick it to send the
     data to the production web service;
   - :guilabel:`Method`: :guilabel:`Automatic` queues the invoices for sending when they are
     confirmed; with :guilabel:`Manual`, the invoices are sent only when you request it;
   - :guilabel:`Sii Period`: :guilabel:`Monthly` or :guilabel:`Quarterly`;
   - :guilabel:`SII Description Method`: how the description of the operation sent to the SII is
     built (:guilabel:`Automatic` from the invoice lines, :guilabel:`Fixed` text, or
     :guilabel:`Manual` on each invoice), optionally preceded by the :guilabel:`SII Customer
     header` or :guilabel:`SII Supplier header`;
   - :guilabel:`Send Mode`: :guilabel:`On validate`, :guilabel:`At fixed time`, or :guilabel:`With
     delay` (the default, which leaves time to correct a mistake before the invoice is sent).

.. screenshot:: finance-fl-spain-sii-oca-company
   :menu: Settings ‣ Companies ‣ (the Spanish company) ‣ SII tab
   :shows: The SII tab of the company form with "Enable SII" ticked, the SII start date, the test environment checkbox, Method "Automatic", period "Monthly", the description configuration and the "Send Mode" set to "With delay".
   :highlight: The "Enable SII" and "Is it the SII test environment?" fields.
   :data: Spanish demo company.
   :module: l10n_es_aeat_sii_oca
   :notes: English UI, light theme, 1440px width.

Journals, fiscal positions, and taxes
-------------------------------------

- On the sales and purchase journals, the :guilabel:`Enable SII` option (:guilabel:`Localization
  Settings` tab) is ticked by default. Untick it for a journal whose documents must not be sent.
- The fiscal positions of the Spanish chart of accounts carry the SII data (registration keys,
  exemption and non-subject causes). Check them when you create a new fiscal position.
- The taxes are sent according to the SII tax map, which covers the default Spanish taxes.

Send invoices
=============

With the automatic method, a customer invoice or vendor bill is queued for sending when it is
confirmed, and sent according to the :guilabel:`Send Mode`. The :guilabel:`SII` tab of the invoice
shows:

- the :guilabel:`Description` and the :guilabel:`Registration key` of the operation, proposed from
  the company settings and the fiscal position;
- in the result section, the :guilabel:`Send state`, the :guilabel:`CSV` code returned by the tax
  agency, and the :guilabel:`Send error` if the invoice was rejected.

To send an invoice immediately, click :guilabel:`Send now` in the :guilabel:`SII` tab. To send
several invoices, select them in the list view, and click :menuselection:`Actions --> Send
Invoices to SII`.

If the sending failed, correct the invoice and click :guilabel:`Send to SII`. If a sent invoice is
modified (for example, after resetting it to draft and confirming it again), the modification is
sent again. To cancel a sent invoice in the SII, cancel the invoice, then click :guilabel:`Send
cancellation to SII`.

.. tip::
   In the invoice and bill lists, use the :guilabel:`SII not sent`, :guilabel:`SII sent`, and
   :guilabel:`SII failed` filters to follow up the sending, and correct and resend the rejected
   documents.

.. screenshot:: finance-fl-spain-sii-oca-invoice
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (a sent invoice) ‣ SII tab
   :shows: The SII tab of a confirmed customer invoice: description, registration key "01", send state "Sent", the CSV code and the send date.
   :highlight: The "Send state" and "CSV" fields.
   :data: Spanish demo company, SII test environment.
   :module: l10n_es_aeat_sii_oca
   :notes: English UI, light theme, 1440px width.

.. seealso::
   - :doc:`aeat_declarations`
   - :doc:`../spain`

=======================================
Pro-forma invoices and advance invoices
=======================================

A pro-forma invoice (*díjbekérő*) is a request for payment. It is not an accounting document: it has
no journal entry, it is not reported to NAV and no VAT becomes due on it. When the customer pays, an
**advance invoice** (*előlegszámla*) is issued for the received amount; the advance is then deducted
on the final invoice of the sales order.

The `eyssen_l10n_hu_proforma` module provides a separate document for pro-forma invoices with its
own numbering (`D/<year>/00001`, restarting every year) and creates the advance invoice and the
payment in one step.

.. note::
   The module replaces the standard :guilabel:`Pro-Forma Invoice` feature of the Sales app, which
   is switched off and removed from the settings in Hungarian databases.

Configuration
=============

Payment terms
-------------

Pro-forma invoices can be created from sales orders whose payment terms allow it. Open
:menuselection:`Accounting --> Configuration --> Payment Terms`, select a payment term and tick
:guilabel:`Enable Pro Forma`. At installation, the option is enabled on all payment terms whose
:ref:`NAV payment method <localizations/hungary/payment-terms>` is *Banki átutalás* (transfer).

Settings
--------

In :menuselection:`Accounting --> Configuration --> Settings`, section :guilabel:`Other Settings`:

- :guilabel:`Előlegszámla-fizetés e-mail előtöltése` (enabled by default): the payment dialog is
  opened with the invoice e-mail template pre-selected, so the paid advance invoice is e-mailed to
  the customer automatically. Disable it to decide case by case.
- :guilabel:`Ajánlat megjegyzésének átvétele`: copy the terms and conditions of the sales order to
  the pro-forma invoice.
- :guilabel:`Rendelés tételeinek felsorolása a díjbekérőn`: default value of the
  :guilabel:`Tételek hozzáadása` option when a pro-forma invoice is created.

.. note::
   The :guilabel:`Proforma prefix` setting has no effect in the current module version; the prefix
   of the numbers is always `D`.

Create a pro-forma invoice
==========================

From a sales order
------------------

The :guilabel:`Create Proforma` button is displayed on a confirmed sales order if the payment terms
have :guilabel:`Enable Pro Forma` ticked and the order still has quantities to invoice. Click it and
fill in the dialog:

- :guilabel:`Összeg típusa` (amount type): :guilabel:`Százalék` (percentage of the order total) or
  :guilabel:`Összeg` (fixed amount, the default);
- :guilabel:`Érték` (value): defaults to the gross total of the order; it cannot exceed 100% or the
  order total;
- :guilabel:`Fizetési határidő (nap)` (payment deadline in days, 2 by default): the due date is
  today plus this number of days;
- :guilabel:`Tételek hozzáadása` (add items): lists the products of the order as notes under the
  advance line; the notes are copied to the advance invoice as well.

Click :guilabel:`Kiállítás`. A draft pro-forma invoice opens with the customer, currency, payment
terms, customer reference and bank account of the order, and a single line *Down payment*
(translated to the language of the customer) for the requested gross amount with the taxes of the
order lines. :ref:`Cash rounding <localizations/hungary/payment-terms>` is applied automatically.

.. screenshot:: finance-fl-hungary-proforma-wizard
   :menu: Sales ‣ Orders ‣ Orders ‣ (sales order) ‣ Create Proforma
   :shows: The "Create Pro Forma" dialog with "Összeg típusa" set to "Százalék", "Érték" 50, "Fizetési határidő (nap)" 2, the "Tételek hozzáadása" checkbox, and the "Kiállítás" and "Mégse" buttons.
   :highlight: The amount type and value fields (red frame).
   :data: Sales order "S00042" for "Minta Kft.", total 254,000 HUF, payment terms "Advance payment".
   :module: eyssen_l10n_hu_proforma
   :notes: English UI, light theme, 1440px width, crop to the dialog. The dialog labels are Hungarian.

Only one open pro-forma invoice can exist for an order: while a confirmed, unpaid pro-forma invoice
exists, a new one can only be created after the previous one is cancelled. The
:guilabel:`Díjbekérők` smart button of the sales order opens the related pro-forma invoices.

Manually
--------

Go to :menuselection:`Accounting --> Customers --> Pro Forma Invoices` and click :guilabel:`New` to
create a pro-forma invoice that is not linked to a sales order. Fill in the customer, the payment
terms or due date, the :guilabel:`Bankszámla` (company bank account, mandatory) and the lines.

.. note::
   Most field labels of the pro-forma invoice form are displayed in Hungarian in the current module
   version: :guilabel:`Ügyfél` (customer), :guilabel:`Díjbekérő dátuma` (date),
   :guilabel:`Fizetési hivatkozás` (payment reference), :guilabel:`Fizetési feltétel` (payment
   terms), :guilabel:`Díjbekérő tételek` (lines), :guilabel:`Előlegszámlák` (advance invoices),
   :guilabel:`Egyéb` (other information).

Confirm and send
================

#. Click :guilabel:`Confirm`. The pro-forma invoice gets its number and the status *Posted*; no
   journal entry is created.
#. Click :guilabel:`Send & Print` to e-mail the PDF to the customer with the *Díjbekérő küldése*
   template (the text of the template is Hungarian), or to download it. :guilabel:`Preview` shows
   the document as the customer sees it in the portal.

The list opens with the :guilabel:`Nincs fizetve` (not paid) filter. The
:guilabel:`Fizetés állapota` (payment status) of a pro-forma invoice is *Nincs fizetve* (not paid),
*Részben fizetve* (partially paid), *Fizetés folyamatban* (in payment) or *Fizetve* (paid),
depending on its advance invoices.

A draft or confirmed pro-forma invoice without advance invoice can be withdrawn with
:guilabel:`Cancel`; it is then marked with a red :guilabel:`Revoked` ribbon. It cannot be reset to
draft.

.. screenshot:: finance-fl-hungary-proforma-form
   :menu: Accounting ‣ Customers ‣ Pro Forma Invoices ‣ (posted pro-forma invoice)
   :shows: Posted pro-forma invoice "D/2026/00003" with the buttons "Send & Print", "Register Payment", "Preview" and "Cancel", the sales order smart button, the "Díjbekérő tételek" tab with the "Down payment" line and the list of ordered items as notes, and the totals.
   :highlight: The "Register Payment" button (red frame).
   :data: Customer "Minta Kft.", amount 127,000 HUF, due in 2 days, origin "S00042".
   :module: eyssen_l10n_hu_proforma
   :notes: English UI, light theme, 1440px width, crop to the form sheet.

Register the payment and issue the advance invoice
==================================================

When the money arrives, open the pro-forma invoice and click :guilabel:`Register Payment`. In the
dialog (*Előlegszámla kiállítása és fizetés rögzítése*):

- adjust the :guilabel:`Bruttó összeg` (gross amount) of the lines if the customer paid only a part
  of the requested amount. The field is pre-filled with the amount not yet invoiced, so a pro-forma
  invoice can be paid in several installments;
- select the :guilabel:`Bank napló` (bank or cash journal of the payment) and the
  :guilabel:`Számla napló` (sales journal of the advance invoice);
- set the :guilabel:`Teljesítés időpontja` (fulfillment date): the day the payment was received;
- check the payment terms and the payment method;
- keep or clear the :guilabel:`E-mail sablon` (e-mail template) to send or not to send the advance
  invoice to the customer (:guilabel:`Számla küldése`).

Click :guilabel:`Kifizetés rögzítése`. In a single step, Odoo

#. creates the advance invoice with today's invoice date and the given fulfillment and accounting
   date, with lines named after the pro-forma lines and the pro-forma number;
#. links the advance to the sales order, so that it is deducted on the final invoice;
#. confirms the invoice, which is :doc:`reported to NAV <nav_online_invoice>`;
#. registers the payment and reconciles it with the invoice;
#. e-mails the paid advance invoice to the customer, if an e-mail template was selected.

The advance invoices are listed in the :guilabel:`Előlegszámlák` tab of the pro-forma invoice, and
the pro-forma invoice is shown in the :guilabel:`Díjbekérő` field of the :guilabel:`Related Invoices`
tab of the advance invoice.

.. screenshot:: finance-fl-hungary-proforma-payment
   :menu: Accounting ‣ Customers ‣ Pro Forma Invoices ‣ (posted pro-forma invoice) ‣ Register Payment
   :shows: The payment dialog with the pro-forma line and its editable gross amount, the bank journal, the invoice journal, the fulfillment date, the payment terms, the e-mail template and the "Kifizetés rögzítése" button.
   :highlight: The gross amount column and the fulfillment date (red frames).
   :data: Pro-forma invoice "D/2026/00003", 127,000 HUF; bank journal "Bank"; invoice journal "Customer Invoices".
   :module: eyssen_l10n_hu_proforma
   :notes: English UI, light theme, 1440px width, crop to the dialog. The dialog labels are Hungarian.

Final invoice
=============

Invoice the sales order as usual with :guilabel:`Create Invoice` once the goods are delivered or the
service is performed. The advance invoices are deducted automatically; see :ref:`advance and final
invoices <localizations/hungary/corrective>` for the option limiting the deduction.

Reports and customer portal
===========================

Two PDF reports are available in the :guilabel:`Print` menu: :guilabel:`Proformas` and
:guilabel:`Proformas without Payment`. The document is titled *Pro Forma Invoice* (*Draft* or
*Cancelled Pro Forma Invoice*) and shows the tax numbers of the customer, the dates, the payment
method, the bank account and payment reference, the lines with net, VAT and gross amounts, and the
exchange rate for foreign-currency documents.

Customers receive a secure link to the pro-forma invoice in the e-mail and can view and print it in
the portal. Online payment of pro-forma invoices is not available.

:show-content:
:show-toc:

=============
Cash register
=============

The **Cash register** (*Házipénztár*) turns an Odoo cash journal into a Hungarian
strict-accountability (*szigorú számadás*) cash book. Every cash movement becomes a numbered cash
voucher (*pénztárbizonylat*), the vouchers are collected on cash-book pages that are closed with a
serial number and locked, and each page prints as a cash report (*pénztárjelentés*) together with
the cash count of the drawer.

The module builds on standard Odoo :ref:`cash journals <accounting/journals/cash>`, the
:guilabel:`Accounting Dashboard` and the reconciliation view of the statement lines; it does not
replace them, it extends them with the controls a strict-accountability cash book requires.

How it works
============

In a cash journal, every cash movement is a statement line, and the journal entry of that line is
the cash voucher: its number is the voucher number. A voucher can be recorded from three places (the
cash journal card, the reconciliation view, or a payment), and in each case it is numbered, put on
the open cash-book page and printed the same way.

Key features
============

- **Two numbering modes per cash journal**: one common series for receipts and disbursements, or two
  separate series (``BEF/`` for receipts, ``KIF/`` for disbursements). See
  :ref:`cash_register/numbering`.
- **Gap-free, audit-proof vouchers**: an issued voucher can never be deleted. A wrong voucher is
  voided; it keeps its number and appears as voided on the cash report.
- **Recording from anywhere**: a cash receipt or payment can be recorded from the cash journal card,
  from the reconciliation view, or by paying an invoice or bill in cash. See
  :ref:`cash_register/record`.
- **Cash-book pages**: every cash voucher lands on the open page of its journal. Closing a page gives
  it a serial ``STAT`` number and locks it; only an accounting administrator can reopen it, and no
  voucher may be dated before a closed period.
- **Cash report**: the printed page lists the opening balance, the vouchers with a running balance,
  daily totals, the voided vouchers, the closing balance, the last cash count and the signature
  lines.
- **Cash count with an optional controller**: the drawer is counted by denomination and compared
  with the book balance. A discrepancy needs a reason and the approval of an accounting
  administrator, and a cash journal can require a second user to check every count.

.. screenshot:: accounting-cash-register-dashboard-card
   :menu: Accounting ‣ Dashboard
   :shows: A cash journal card on the Accounting Dashboard with the :guilabel:`Close Cash Register`,
      :guilabel:`New Cash-in` and :guilabel:`New Cash-out` buttons next to the standard
      :guilabel:`Transactions` button.
   :highlight: The three cash-register buttons (red frame).
   :data: Demo company "YourCompany HU"; cash journal "Cash (HUF)" with a non-zero balance.
   :module: eyssen_cashregister, eyssen_accountant
   :notes: English UI, light theme, 1440px width, crop to the card.

.. note::
   The Cash register is an *eYssen* extension for Hungarian localization. Once the cash journals are
   configured, day-to-day work (vouchers, pages, cash counts) is done from the
   :guilabel:`Accounting Dashboard`.

.. toctree::
   :titlesonly:

   cash_register/configuration
   cash_register/operations

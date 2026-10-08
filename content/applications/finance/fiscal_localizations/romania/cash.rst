==============
Cash documents
==============

The :guilabel:`Romania - Cash Documents (eYssen)` (`l10n_ro_cash`) module adapts the :doc:`cash
register <../../accounting/bank/cash_register>` to the Romanian rules. For the cash journals of
Romanian companies, the cash vouchers are printed as the official documents of OMFP 2634/2015:

- the **receipt** (*chitanță*, form 14-4-1), given to the customers who pay in cash;
- the **cash collection order** (*dispoziție de încasare*) and the **cash payment order**
  (*dispoziție de plată*), both on form 14-4-4;
- the **cash register book** (*registru de casă*, form 14-4-7), printed from the cash-book pages.

The module also checks the cash operations against the limits of Law 70/2015 on cash payments.

It requires the *eYssen Accountant* and *Cash register* modules, which are installed with it, and
only changes the cash journals of companies whose **fiscal country** is Romania.

.. _localizations/romania/cash-installation:

Installation in a multi-company database
========================================

The cash register manages **every** cash journal of the database: vouchers, cash-book pages,
numbering and locks. When `l10n_ro_cash` installs the cash register as a dependency in a database
that already contains companies of other countries, the cash register is **disabled** for the
non-Romanian companies that already have journal entries: their cash journals keep working as
before, as in standard Odoo. The companies without entries, the new companies and the Romanian
companies get the cash register.

The setting is the :guilabel:`Cash Register Disabled` field, displayed on the cash journals
(:menuselection:`Accounting --> Configuration --> Journals`, :guilabel:`Journal Entries` tab, for
users with the *Adviser* access right on the Accounting app). It belongs to the company: it applies
to all the cash journals of the company. If the cash register was already installed, or if you
install it yourself, it is enabled for all the companies, as before.

.. note::
   While the cash register is disabled for a company, its cash journals have no cash vouchers, no
   cash-book pages and no separate receipt/disbursement numbering, and the
   :guilabel:`Separate Receipt/Disbursement Numbering` field is hidden.

.. _localizations/romania/cash-numbering:

Numbering of the documents
==========================

Cash orders
-----------

With the :guilabel:`Separate Receipt/Disbursement Numbering` option of the cash journal (see
:ref:`cash_register/numbering`), the cash vouchers of a Romanian journal are numbered in the two
series of the cash orders instead of `BEF/` and `KIF/`:

- `DI/` for the cash receipts (*dispoziții de încasare*), for example `DI/CASH/2026/00001`;
- `DP/` for the cash payments (*dispoziții de plată*), for example `DP/CASH/2026/00001`.

A journal that already numbered vouchers in the `BEF/` and `KIF/` series (before the module was
installed) keeps them, because the prefix is part of the numbers already issued.

Receipts
--------

A receipt is issued for the cash collected from a **customer**: a customer payment, or a cash line
reconciled with a receivable account. It has its own gap-free series for each cash journal,
`CH/<journal code>/<year>/00001`. The series is created automatically with the first receipt. It
is displayed in the :guilabel:`Receipt (Chitanță) Sequence` field of the cash journal
(:guilabel:`Journal Entries` tab, for users with the *Adviser* access right).

The receipt number is given when the payment is posted or, at the latest, when the receipt is first
printed. It is never changed afterwards. The number of the cash voucher itself (`DI/…` or the plain
number of the journal) is also printed on the receipt.

Any other cash collection (for example, the refund of a vendor) is documented by a cash collection
order, and any cash payment by a cash payment order.

Printing the documents
======================

The documents are printed in Romanian when the Romanian language is installed in the database,
whatever the language of the partner. The amount is written in words (for example *o mie două sute
lei și cincizeci bani*).

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Document
     - How to print it
   * - Receipt, cash collection order, cash payment order
     - Click :guilabel:`Print Cash Document` on the payment (displayed once the payment is posted),
       or :guilabel:`Print Cash Voucher` on the cash voucher (see :ref:`cash_register/record`).
       The payment receipt of a cash payment prints the same document.
   * - Cash register book
     - Open a cash-book page and choose :menuselection:`Print --> Cash Report` (see
       :ref:`cash_register/pages`).

Receipt
-------

The :guilabel:`RECEIPT` shows the company (unit, tax ID, trade register number, registered
office), the receipt number and date, and the payer (:guilabel:`Received from`, tax ID, trade
register number, address), the :guilabel:`The sum of` in figures and :guilabel:`In words`, and the
reason (:guilabel:`Representing`), for example *Payment of invoice INV/2026/00012 of 2026-09-25*.
It is signed by the cashier.

Cash collection and payment orders
----------------------------------

The :guilabel:`CASH COLLECTION ORDER` and the :guilabel:`CASH PAYMENT ORDER` show the name and the
position of the person, the amount in figures and in words, and the purpose of the collection or
of the payment. They have the signature blocks for the head of the unit, the preventive financial
control and the financial and accounting department, and the part for the cashier and for the
recipient of the money (the identity document of the recipient is to be filled in by hand).

Cash register book
------------------

The :guilabel:`CASH REGISTER BOOK` prints **one page for each day** of the cash-book page: the
company, the cash desk and its account, the :guilabel:`Balance carried over from the previous
day`, the documents of the day in the order of the vouchers (document number, number of annexes,
explanations, receipts and payments), the :guilabel:`Total`, the :guilabel:`Balance at the end of
the day`, and the signatures of the cashier and of the financial and accounting department. The
documents that are not posted or are cancelled are marked :guilabel:`NOT POSTED` or
:guilabel:`CANCELLED`. A page that is not closed is marked :guilabel:`NOT CLOSED - FOR INFORMATION
ONLY`.

.. _localizations/romania/cash-limits:

Cash limits (Law 70/2015)
=========================

Law 70/2015 limits the cash operations between businesses and with individuals, and the cash
that a business may keep. Go to :menuselection:`Accounting --> Configuration --> Settings` and
open the :guilabel:`Romanian Cash Limits (Law 70/2015)` section, displayed for Romanian companies
below the bank and cash settings.

.. list-table::
   :header-rows: 1
   :widths: 40 15 45

   * - Setting
     - Default
     - Limit
   * - :guilabel:`Cash Limit Policy`
     - :guilabel:`Warn`
     - :guilabel:`Warn` or :guilabel:`Block` the operations that exceed a limit.
   * - :guilabel:`Receipts from a Legal Entity (per Day)`
     - 5,000
     - Cash collected from one legal entity in one day.
   * - :guilabel:`Payments to a Legal Entity (per Day)`
     - 5,000
     - Cash paid to one legal entity in one day.
   * - :guilabel:`Payments to Legal Entities (Daily Total)`
     - 10,000
     - All the cash paid to legal entities in one day.
   * - :guilabel:`Operations with an Individual (per Day)`
     - 10,000
     - Cash collected from, and cash paid to, one individual in one day (each direction is
       counted separately).
   * - :guilabel:`Treasury Advance (per Person and Day)`
     - 5,000
     - Treasury advances (account `542`) paid to one person in one day.
   * - :guilabel:`Cash Ceiling (End of Day)`
     - 50,000
     - Cash on hand allowed at the end of each day (*plafon de casă*). Informational. Set it to
       zero to disable the check.

The amounts are in the currency of the company. Set a limit to zero to disable it. The defaults
are the limits set by GEO 115/2023, which Law 239/2025 (in force since 1 January 2026) did not
change. They are not updated automatically: check them with the accountant of the company and
adapt them if the law changes.

How the limits are checked
--------------------------

Each time a cash payment is posted or a cash line is recorded, Odoo adds up, for the partner and
the day of the operation, the operations of **all the cash journals of the company** on that
day (cancelled vouchers excluded), converted into the currency of the company. A contact that is
a company is a legal entity; any other contact is an individual. The partner is the commercial
entity of the contact.

- With the :guilabel:`Warn` policy, a :guilabel:`Cash limit` warning is displayed on the form while
  you enter the operation, and a note is posted in the chatter of the voucher and of the payment.
- With the :guilabel:`Block` policy, the operation is refused with an error message that gives
  the date, the partner, the total and the limit.
- The cash ceiling never blocks anything. When the cash on hand of the company (the balance of the
  cash accounts of its cash journals in the currency of the company) is above the ceiling at the
  end of a day, a note recommends depositing the excess in a bank account within two working days.
  The cash register book prints a warning for the days concerned.

.. seealso::
   - :doc:`../../accounting/bank/cash_register`
   - :doc:`../romania`
   - :doc:`multi_company`

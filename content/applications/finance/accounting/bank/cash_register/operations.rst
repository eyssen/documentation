==========
Operations
==========

Day-to-day cash handling starts from the cash journal card of the :guilabel:`Accounting Dashboard`.
Its main button and its name open the reconciliation view of the cash journal, and the
cash-register buttons sit next to the standard ones.

.. screenshot:: accounting-cash-register-actions
   :menu: Accounting ‣ Dashboard
   :shows: The cash journal card with the :guilabel:`New Cash-in`, :guilabel:`New Cash-out` and
      :guilabel:`Close Cash Register` buttons.
   :highlight: The :guilabel:`New Cash-in` and :guilabel:`New Cash-out` buttons (red frame).
   :data: Cash journal "Cash (HUF)".
   :module: eyssen_cashregister
   :notes: English UI, light theme, crop to the card.

.. _cash_register/record:

Record a cash receipt or payment
================================

A cash voucher can be recorded from three places. Wherever it starts, the voucher is numbered,
placed on the open cash-book page and printed the same way.

.. list-table::
   :header-rows: 1
   :widths: 26 37 37

   * - Where
     - Use it for
     - What happens
   * - 1. Cash journal card: :guilabel:`New Cash-in` or :guilabel:`New Cash-out`
     - Everyday cash movements, whether or not an invoice belongs to them.
     - The voucher is recorded; you then match it with an invoice or book it to an account in the
       reconciliation view, where it opens.
   * - 2. Reconciliation view: :guilabel:`New`
     - The same, when you are already working in the reconciliation view.
     - The voucher is recorded and appears in the list, ready to be matched or booked.
   * - 3. Paying an invoice or a bill: :guilabel:`Pay` with the cash journal
     - Settling a known invoice or bill in cash.
     - A payment is created, and its voucher is issued and matched automatically. Nothing else is
       needed.

A payment created by hand in :menuselection:`Accounting --> Customers --> Payments` or
:menuselection:`Accounting --> Vendors --> Payments` with the cash journal works like the third
case.

From the cash journal card
--------------------------

#. On the cash journal card, click :guilabel:`New Cash-in` for money received, or
   :guilabel:`New Cash-out` for money paid out.
#. Enter the :guilabel:`Date`, the :guilabel:`Label` (the title of the cash movement, *jogcím*), the
   :guilabel:`Partner` and the :guilabel:`Amount`. Enter the amount without a sign: the button gives
   the direction.
#. Click :guilabel:`Save`. The voucher receives its number, lands on the open cash-book page, and the
   reconciliation view of the cash journal opens with the new voucher selected.
#. Match the voucher with an open invoice or bill on the :guilabel:`Reconcile` tab, or book it to an
   account on the :guilabel:`Manual operation` tab, then click :guilabel:`Validate`. The voucher
   stays in the list after it is matched.
#. Click :guilabel:`Print Cash Voucher` to print the voucher. It can be printed as soon as it is
   recorded, before or after matching.

.. screenshot:: accounting-cash-register-voucher
   :menu: Accounting ‣ Dashboard ‣ (cash journal) ‣ New Cash-out ‣ Save
   :shows: The reconciliation view with the new cash voucher selected, its number on the cash line,
      the open invoices on the Reconcile tab and the Print Cash Voucher button.
   :highlight: The voucher number and the :guilabel:`Print Cash Voucher` button (red frame).
   :data: Cash journal "Cash (HUF)", short code PENZ, separate numbering; disbursement of 12,500 HUF,
      voucher KIF/PENZ/2026/00001.
   :module: eyssen_cashregister, eyssen_accountant
   :notes: English UI, light theme, 1440px width.

From the reconciliation view
----------------------------

Open the reconciliation view with the main button of the cash journal card, then click
:guilabel:`New`. The form is the same as above, but here the sign of the :guilabel:`Amount` gives the
direction: a positive amount is a receipt, a negative amount a disbursement. After saving, select the
new voucher in the list to match, book and print it.

By paying an invoice or a bill
------------------------------

#. On a posted invoice or bill, click :guilabel:`Pay`.
#. Select the cash journal as :guilabel:`Journal`, check the amount and the date, and click
   :guilabel:`Create Payment`.

The payment is booked against an outstanding account, its cash voucher is issued in the cash journal
and the two are matched at once, so the invoice is paid. The voucher can be printed from the
reconciliation view of the cash journal with :guilabel:`Print Cash Voucher`.

.. important::
   While its cash voucher stands, the payment cannot be reset to draft, cancelled or deleted. To
   correct it, void the voucher first (see below), then change the payment; posting the payment
   again issues a new voucher.

Void a cash voucher
-------------------

An issued voucher can never be deleted, because its number must stay accountable. To void a wrong
voucher (*rontás*), open its journal entry with :guilabel:`View move` in the reconciliation view
and click :guilabel:`Cancel Entry`. The voucher keeps its number, no longer counts in the cash
balance, and appears as **VOIDED** on the cash report. Record the correct movement as a new voucher.

A voucher on a closed cash-book page cannot be voided: reopen the page first, or record a correcting
voucher dated today.

.. _cash_register/pages:

Cash-book pages
===============

A cash-book page (*pénztárjelentés-lap*) collects the vouchers of a period. Every new voucher lands
automatically on the open page of its cash journal; when the journal has no open page, the first
voucher opens a new one. A page is either :guilabel:`Open` or :guilabel:`Confirmed` (closed).

The pages of a cash journal are listed with :menuselection:`(cash journal card) ⋮ --> Cash
Registers`.

.. screenshot:: accounting-cash-register-cashbook-list
   :menu: Accounting ‣ Dashboard ‣ (cash journal ⋮) ‣ Cash Registers
   :shows: The cash-book page list with the :guilabel:`STAT Number` and :guilabel:`Cash-book State`
      columns, one row selected and the :guilabel:`Action` menu open showing
      :guilabel:`Confirm cash-book` and :guilabel:`Reopen cash-book`.
   :highlight: The open :guilabel:`Action` menu (red frame).
   :data: Two pages, one Open and one Confirmed (STAT/2026/00013).
   :module: eyssen_cashregister
   :notes: English UI, light theme, 1440px width.

Close a cash-book page
----------------------

Close the page at the end of the period set in the cash-handling policy (for example every day or
every month): select it in the list and choose :menuselection:`Action --> Confirm cash-book`. On
closing:

- The page receives the next gap-free :guilabel:`STAT Number` (for example ``STAT/2026/00013``). An
  open page never uses up a number.
- The page is locked. No voucher can be added to it, its vouchers can no longer be changed (amount,
  date, partner, label, order) or voided, and its balances are fixed.
- The next voucher opens a new page, whose opening balance is the closing balance of this one.
- No new voucher may be dated before the last day of the closed pages. A voucher dated on that same
  day is allowed, so a page closed at midday can be followed by vouchers of the afternoon.

The bookkeeping of a voucher on a closed page can still be completed: for example, a voucher booked
to a suspense or outstanding account can be matched with an invoice later. This does not change the
cash report.

Reopen a cash-book page
-----------------------

A closed page can be reopened with :menuselection:`Action --> Reopen cash-book`. Only users with the
:guilabel:`Administrator` access right of :guilabel:`Accounting` can reopen a page. Reopening keeps
the existing ``STAT`` number — a page is never renumbered — and is recorded in the chatter.

Print the cash report
=====================

Open a cash-book page and choose :menuselection:`Print --> Cash Report`. The cash report
(*pénztárjelentés*) shows:

- the company, the cash desk and its currency, the ``STAT`` number and the period of the page;
- the opening balance;
- every voucher in order, with its date, number, title, partner, receipt or disbursement and the
  running balance, and the voided vouchers marked **VOIDED** without an amount;
- the daily totals and the closing balance;
- the last approved cash count of the page with its denominations, or a note that no cash count was
  taken;
- signature lines for the cashier and the checker.

An open page can be printed too, for information: the report is then marked **NOT CLOSED - FOR
INFORMATION ONLY** and has no ``STAT`` number.

.. _cash_register/cash-count:

Count the cash drawer
=====================

To compare the physical cash with the books, click :guilabel:`Close Cash Register` on the cash
journal card. Enter the number of coins and bills per denomination; the :guilabel:`Counted Balance`
and the :guilabel:`Discrepancy` against the :guilabel:`Cash Balance in Journal` are computed as you
type. The book balance is computed again from the journal at the moment the count is closed.

.. screenshot:: accounting-cash-register-closure
   :menu: Accounting ‣ Dashboard ‣ (cash journal) ‣ Close Cash Register
   :shows: The cash register closure form with the denomination lines (value, number of
      coins/bills, subtotal), the :guilabel:`Cash Balance in Journal`, the :guilabel:`Counted
      Balance`, the :guilabel:`Discrepancy` and the :guilabel:`Reason for Discrepancy` field.
   :highlight: The :guilabel:`Discrepancy` block (red frame).
   :data: HUF denominations, counted balance 1,000 HUF short of the journal balance.
   :module: eyssen_cashregister
   :notes: English UI, light theme, 1440px width.

The next steps depend on the :guilabel:`Controller Required for Cash Count` setting of the cash
journal (see :ref:`cash_register/controller`).

Without a controller (default)
------------------------------

- **No discrepancy**: click :guilabel:`Close`. The count is closed.
- **Discrepancy**: enter the :guilabel:`Reason for Discrepancy` and click :guilabel:`Forward to the
  Manager`. The count waits for approval (:guilabel:`Waiting for Approval`) until an accounting
  administrator clicks :guilabel:`Close with Discrepancy`. When only one user handles the cash, that
  user may approve the own count, provided they have the :guilabel:`Administrator` access right.

With a controller
-----------------

#. Select the :guilabel:`Controller`: an active internal user of the company with accounting rights,
   other than yourself. If there is a discrepancy, enter the :guilabel:`Reason for Discrepancy` too.
#. Click :guilabel:`Send for Check`. The count is fixed as counted and waits for the controller
   (:guilabel:`Waiting for Check`).
#. The controller opens the count and clicks :guilabel:`Approve Count`. Only the selected controller
   can do this. Without a discrepancy the count is closed.
#. If there is a discrepancy, the count then waits for approval (:guilabel:`Waiting for Approval`),
   and an accounting administrator clicks :guilabel:`Close with Discrepancy`. The approver cannot be
   the user who counted the cash; the controller may be the same administrator, so two people are
   enough.

After the count
---------------

- The count belongs to the open cash-book page of the journal (to the last page, if the page was
  already closed), and the cash report of that page prints it once it is closed.
- Once sent or closed, a count can no longer be changed; only a draft count can be deleted.
- :guilabel:`Print` produces the cash count sheet.

Past counts are listed under :menuselection:`Accounting --> Reporting --> Cash Register Closures`,
where they can be filtered by state (:guilabel:`Draft`, :guilabel:`Waiting for Check`,
:guilabel:`Waiting for Approval`, :guilabel:`Closed`) and grouped by cash register, user or
controller.

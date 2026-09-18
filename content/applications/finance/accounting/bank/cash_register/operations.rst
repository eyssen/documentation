==========
Operations
==========

Day-to-day cash handling is done from the :guilabel:`Accounting Dashboard`. On a cash journal card,
the cash-register actions are available next to the standard buttons.

.. screenshot:: accounting-cash-register-actions
   :menu: Accounting ‣ Dashboard
   :shows: The cash journal card with the :guilabel:`New Cash-in`, :guilabel:`New Cash-out` and
      :guilabel:`Close Cash Register` buttons.
   :highlight: The :guilabel:`New Cash-in` and :guilabel:`New Cash-out` buttons (red frame).
   :data: Cash journal "Cash (HUF)".
   :module: eyssen_cashregister
   :notes: English UI, light theme, crop to the card.

Record a cash-in or cash-out voucher
====================================

#. On the cash journal card, click :guilabel:`New Cash-in` for money received, or
   :guilabel:`New Cash-out` for money paid out. A cash voucher form opens with the journal and the
   direction already filled in.
#. Select the :guilabel:`Customer` or :guilabel:`Vendor` and enter the :guilabel:`Amount`.
#. Fill in the cash-specific fields:

   - :guilabel:`Pretense` (*Jogcím*): the reason for the cash movement. It is editable only while
     the voucher is a draft.
   - :guilabel:`Date`: the voucher date. It may not be earlier than the last numbered voucher (see
     :ref:`cash_register/back-dating`).

#. Confirm the voucher. On posting:

   - It receives the next gap-free number from the journal's :guilabel:`Cash-in Sequence` or
     :guilabel:`Cash-out Sequence` (for example ``BEF/2026/00012`` or ``KIF/2026/00007``), shown in
     :guilabel:`Voucher Number`.
   - The :guilabel:`Amount in Words` (*betűs összeg*) is filled in automatically for the printed
     voucher.

.. screenshot:: accounting-cash-register-voucher
   :menu: Accounting ‣ Dashboard ‣ (cash journal) ‣ New Cash-in
   :shows: A posted cash-in voucher with the customer, the amount, the :guilabel:`Pretense` field,
      the assigned :guilabel:`Voucher Number` and the :guilabel:`Amount in Words`.
   :highlight: The :guilabel:`Voucher Number` and :guilabel:`Amount in Words` fields (red frame).
   :data: Customer "Deco Addict", amount 25,000 HUF, voucher BEF/2026/00012.
   :module: eyssen_cashregister
   :notes: English UI, light theme, 1440px width.

.. note::
   A draft voucher that is cancelled never consumes a number, so the numbering stays gap-free. Once
   a voucher carries a number it can no longer be deleted, which preserves the audit trail.

Cash-book statements
====================

A cash-book statement (*pénztárkönyv / kivonat*) is a numbered page that groups a period's cash
movements. A statement is **Open** while it accepts entries and **Confirmed** once it is closed and
locked.

.. screenshot:: accounting-cash-register-cashbook-list
   :menu: Accounting ‣ Dashboard ‣ (cash journal ellipsis) ‣ Cash Registers
   :shows: The cash-book statement list with the :guilabel:`STAT Number` and
      :guilabel:`Cash-book State` columns, one row selected and the :guilabel:`Action` menu open
      showing :guilabel:`Confirm cash-book` and :guilabel:`Reopen cash-book`.
   :highlight: The open :guilabel:`Action` menu (red frame).
   :data: Two statements, one Open and one Confirmed (STAT/2026/00013).
   :module: eyssen_cashregister
   :notes: English UI, light theme, 1440px width.

Confirm a cash book
-------------------

When a cash-book page is complete, select it in the statement list and choose
:menuselection:`Action --> Confirm cash-book`. On confirmation:

- The statement receives the next gap-free :guilabel:`STAT Number` from the journal's
  :guilabel:`Statement Sequence` (for example ``STAT/2026/00013``). Because the number is assigned
  only on confirmation, an open page never burns a ``STAT`` number.
- The :guilabel:`Cash-book State` changes to :guilabel:`Confirmed`, and the page and its number can
  no longer be altered.

Reopen a cash book
------------------

A confirmed cash book can be reopened with :menuselection:`Action --> Reopen cash-book`. This action
is restricted to the :guilabel:`Billing Administrator` (*Főkönyvelő*) group. Reopening keeps the
existing ``STAT`` number — a cash book is never re-numbered — and is recorded in the chatter.

Close and count the cash drawer
===============================

To reconcile the physical cash on hand, click :guilabel:`Close Cash Register` on the cash journal
card. Count the drawer by denomination; the system compares the counted amount with the journal
balance and reports any discrepancy. A controller can review and approve a discrepancy before the
count is closed.

.. screenshot:: accounting-cash-register-closure
   :menu: Accounting ‣ Dashboard ‣ (cash journal) ‣ Close Cash Register
   :shows: The cash register closure form with the denomination lines (value, number of
      coins/bills, subtotal), the :guilabel:`Cash Balance in Journal`, the :guilabel:`Counted
      Balance`, the :guilabel:`Discrepancy` and the :guilabel:`Controller` field.
   :highlight: The :guilabel:`Discrepancy` block (red frame).
   :data: HUF denominations, counted balance 1,000 HUF short of the journal balance.
   :module: eyssen_cashregister
   :notes: English UI, light theme, 1440px width.

Fill in the number of coins and bills per :guilabel:`Denomination`; the :guilabel:`Counted Balance`
and the :guilabel:`Discrepancy` against the :guilabel:`Cash Balance in Journal` are computed as you
type. If there is no difference, click :guilabel:`Close`. If there is one, enter the
:guilabel:`Reason for Discrepancy`, appoint a :guilabel:`Controller` (it cannot be yourself) and
click :guilabel:`Close with Discrepancy`; the closure then waits for that controller's approval.
:guilabel:`Print` produces the cash count sheet.

Past closures are listed under :menuselection:`Accounting --> Reporting --> Cash Register Closures`,
where they can be filtered by state (:guilabel:`Draft`, :guilabel:`Waiting for Approval`,
:guilabel:`Closed`) and grouped by cash register, user or controller.

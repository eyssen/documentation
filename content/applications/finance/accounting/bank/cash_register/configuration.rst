=============
Configuration
=============

Installation
============

Navigate to :menuselection:`Apps`, search for **Cash Register**, and click :guilabel:`Install`. The
module depends on :guilabel:`Accounting`; on a Hungarian localization database it is usually
installed together with the localization.

.. important::
   The cash-book settings of a journal are visible to users with the :guilabel:`Administrator`
   access right of :guilabel:`Accounting`. Cashiers do not need this right to record vouchers.

Set up a cash journal
=====================

Each physical cash desk is a separate cash journal, one per currency (for example *Cash HUF*,
*Cash EUR*). To create one, go to :menuselection:`Accounting --> Configuration --> Journals`, click
:guilabel:`New`, set the :guilabel:`Type` to :guilabel:`Cash` and select the :guilabel:`Currency`.

On a cash journal, the :guilabel:`Journal Entries` tab shows three cash-book settings:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Field
     - Purpose
   * - :guilabel:`Separate Receipt/Disbursement Numbering`
     - Chooses the numbering mode of the cash vouchers (see :ref:`cash_register/numbering`).
   * - :guilabel:`Controller Required for Cash Count`
     - Requires a second user to check every cash count of the journal (see
       :ref:`cash_register/controller`).
   * - :guilabel:`Statement Sequence`
     - The numbering of the closed cash-book pages (see :ref:`cash_register/stat`).

.. screenshot:: accounting-cash-register-journal-config
   :menu: Accounting ‣ Configuration ‣ Journals ‣ (a cash journal) ‣ Journal Entries
   :shows: The cash journal form with the Separate Receipt/Disbursement Numbering, Controller
      Required for Cash Count and Statement Sequence fields.
   :highlight: The three cash-book settings (red frame).
   :data: Cash journal "Cash (HUF)", short code PENZ, with the STAT/ sequence assigned.
   :module: eyssen_cashregister
   :notes: English UI, light theme, crop to the group.

.. _cash_register/numbering:

Voucher numbering modes
=======================

The number of a cash voucher is the number of its journal entry. It is assigned when the voucher is
recorded, continues without gaps, and restarts every fiscal year. Each cash journal uses one of two
numbering modes:

.. list-table::
   :header-rows: 1
   :widths: 22 39 39

   * -
     - Common numbering (default)
     - Separate numbering
   * - Setting
     - :guilabel:`Separate Receipt/Disbursement Numbering` cleared
     - :guilabel:`Separate Receipt/Disbursement Numbering` ticked
   * - Receipts
     - ``PENZ/2026/00001``, ``PENZ/2026/00003``, …
     - ``BEF/PENZ/2026/00001``, ``BEF/PENZ/2026/00002``, …
   * - Disbursements
     - ``PENZ/2026/00002``, ``PENZ/2026/00004``, …
     - ``KIF/PENZ/2026/00001``, ``KIF/PENZ/2026/00002``, …
   * - Result
     - One running number for all vouchers of the cash desk, in the order they are recorded.
     - Two independent running numbers, one for receipts (*bevételi bizonylat*) and one for
       disbursements (*kiadási bizonylat*).

In the examples, ``PENZ`` is the short code of the cash journal and ``2026`` is the fiscal year.

Hungarian law does not prescribe either mode: the cash-handling policy (*pénzkezelési szabályzat*) of
the company decides. Separate numbering follows the traditional pre-printed receipt and disbursement
voucher pads; common numbering gives a single sequence that is easy to check for gaps.

.. important::
   - The numbering mode can only be changed at the start of a fiscal year. Once a voucher has been
     numbered in the current fiscal year, the setting can no longer be changed for that year.
   - With separate numbering, a voucher keeps its direction: an issued receipt cannot be turned into
     a disbursement (or the other way round) by changing its amount. Void it and record a new one
     instead.
   - A line with a zero amount moves no cash and gets no ``BEF/`` or ``KIF/`` number.
   - Other entries of the cash journal that are not vouchers (for example a manual journal entry)
     keep the plain ``PENZ/`` numbering in both modes.

.. note::
   When a cash voucher is issued for a payment (see :ref:`cash_register/record`), the payment keeps
   its own journal entry with a separate number (for example ``PPENZ/2026/00001``). The voucher
   number shown on the printed voucher and on the cash report is always the number of the cash
   voucher, not that of the payment.

.. _cash_register/stat:

Cash-book page numbering
========================

A closed cash-book page receives a gap-free ``STAT`` number. The module ships the
:guilabel:`Cash Book - Statement` sequence (prefix ``STAT/``, restarting every year); select it, or
your own copy of it, in the :guilabel:`Statement Sequence` field of each cash journal. A page cannot
be closed until the journal has a :guilabel:`Statement Sequence`.

To create your own sequence, duplicate the supplied one in :menuselection:`Settings --> Technical
--> Sequences & Identifiers --> Sequences` and keep its :guilabel:`Implementation` set to
:guilabel:`No gap`.

Payment methods
===============

When an invoice or a bill is paid with a cash journal, the payment is first booked against an
outstanding account, and its cash voucher books the cash. On the :guilabel:`Incoming Payments` and
:guilabel:`Outgoing Payments` tabs of the cash journal, the payment methods may therefore not use the
cash account itself in the :guilabel:`Outstanding Receipts accounts` and :guilabel:`Outstanding
Payments accounts` columns. Leave these columns empty to use the default outstanding accounts of the
company.

A cash payment must also be in the currency of its cash journal.

.. _cash_register/controller:

Controller for the cash count
=============================

By default, the user who counts the drawer also closes the count. Tick :guilabel:`Controller
Required for Cash Count` on a cash journal to apply the four-eyes principle: every count of that
journal must then be checked and approved by a second user, the controller, before it closes. See
:ref:`cash_register/cash-count` for the procedure.

The controller must be an active internal user of the company with accounting rights, and cannot be
the user who counts the cash. Leave the option cleared on databases where only one user handles the
cash.

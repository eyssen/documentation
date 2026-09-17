=================
Recurring billing
=================

Recurring invoices are produced by a scheduled action, not by hand. It walks the active subscription
lines, works out which periods are due, and creates one customer invoice per contract.

The billing scheduled action
============================

The :guilabel:`Subscription: Generate Recurring Invoices` scheduled action runs once a day. It is
delivered **inactive**: activate it in :menuselection:`Settings --> Technical --> Automation -->
Scheduled Actions` once the configuration has been checked on the database.

For each active line it:

#. skips the line if its contract is not :guilabel:`Active`, or if the contract is still
   :guilabel:`In Trial`;
#. computes the next period from the line's :guilabel:`Period`, :guilabel:`Invoice Method` and
   :guilabel:`Invoice Basis`;
#. stops when :guilabel:`Contract End` is reached, or when :guilabel:`Auto-renew` is off and the
   first period has been billed;
#. skips periods that ended before :guilabel:`Billing Resumes On`, so a paused subscription is not
   billed retroactively;
#. adds an invoice line carrying the billed period, and applies the contract's :guilabel:`Coupon`,
   if any.

Lines of the same contract are billed onto **one** invoice.

.. important::
   One run catches up at most 24 missed periods per line. This is a guard: a mis-set
   :guilabel:`Start Date` would otherwise generate years of history in a single run.

Draft or posted
===============

The contract's :guilabel:`Invoice Posting` policy decides what happens to the generated invoice:

- :guilabel:`Leave as draft for review` (default): the invoice stays in draft, for an accountant to
  check and post.
- :guilabel:`Post automatically`: the invoice is posted immediately, and — if the contract has a
  :guilabel:`Payment Token` — an :doc:`automatic charge <automatic_payments>` is attempted.

:guilabel:`Paid Until` only moves forward on **posted** invoices, so a draft invoice never makes the
line look billed.

The generated invoice
=====================

The invoice is an ordinary customer invoice in the contract's :guilabel:`Billing Journal`. It is
flagged as a subscription invoice and links back to the subscription lines it bills; each invoice
line stores the :guilabel:`Period Start` and :guilabel:`Period End` it covers. The line label comes
from the line's :guilabel:`Invoice Note` when one is set, with `#START#`, `#END#` and `#PERIOD#`
replaced by the billed period.

.. screenshot:: sales-subscriptions-generated-invoice
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (a subscription invoice)
   :shows: A generated recurring invoice with two invoice lines, each showing the billed period in its label, and the link back to the subscription contract.
   :highlight: The billed period in the line labels (red frame).
   :data: Invoice of contract SUB/2026/0012 covering March 2026.
   :module: subscription
   :notes: English UI, light theme, 1440px width, crop to the invoice lines.

Changing a running subscription
===============================

Changes to a running line are recorded in its :guilabel:`Change History` tab with the old and the
new value, so the reason for a changed invoice amount can always be traced. Changes take effect from
the next period that is billed; already posted invoices are not modified.

.. seealso::
   - :doc:`lines`
   - :doc:`automatic_payments`

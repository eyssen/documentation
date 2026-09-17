=========================
Invoice and bill approval
=========================

The *eYssen Account Approval* (`account_approval`) module requires an approval before customer
invoices, vendor bills, and their credit notes can be confirmed. The approvers are defined by
**approval rules**, based on the document's amount.

.. _accounting/invoice-approval/rules:

Approval rules
==============

To create an approval rule, go to :menuselection:`Accounting --> Configuration --> Approval -->
Rules` and click :guilabel:`New`. Fill in the following fields:

- :guilabel:`Rule Name` and :guilabel:`Description`.
- :guilabel:`Enabled`: only enabled rules are applied.
- :guilabel:`Company`: the company the rule applies to.
- :guilabel:`Direction`: the documents the rule applies to: :guilabel:`Inbound` (vendor bills and
  refunds), :guilabel:`Outbound` (customer invoices and credit notes), or :guilabel:`Both`.
- :guilabel:`Currency` and :guilabel:`Min Amount`: the rule applies to documents whose amount
  reaches the minimum amount (converted into the document's currency).
- :guilabel:`Based On`: whether the :guilabel:`Untaxed Amount` or the :guilabel:`Taxed Amount` of the
  document is compared with the amounts of the rule.

In the :guilabel:`Lines` tab, add one line per approval level:

- :guilabel:`User` and/or :guilabel:`Group`: the users who can approve the document (the users of
  the selected groups are also approvers).
- :guilabel:`Max Amount`: the maximum document amount the line's approvers can approve. `0` means
  unlimited.
- :guilabel:`Enabled`: only enabled lines are taken into account.

.. important::
   - Each line must have at least one user or group.
   - At least one enabled line must have a :guilabel:`Max Amount` of `0` (unlimited).

.. screenshot:: accounting-invoice-approval-rule
   :menu: Accounting ‣ Configuration ‣ Approval ‣ Rules ‣ New
   :shows: Approval rule form: Rule Name "Vendor bills over 500,000 HUF", Enabled, Company, Direction "Inbound", Currency HUF, Min Amount 500,000, Based On "Untaxed Amount"; "Lines" tab with two lines: a user with Max Amount 2,000,000 and the "Accounting / Advisor" group with Max Amount 0.
   :highlight: The "Lines" tab (red frame).
   :data: Demo company "YourCompany HU"; demo users "Marc Demo" and "Mitchell Admin".
   :module: account_approval
   :notes: English UI, light theme, 1440px width.

.. _accounting/invoice-approval/request:

Requesting an approval
======================

When a user who is not an approver of the document clicks :guilabel:`Confirm` on a draft invoice
or bill, the :guilabel:`Request for Approval` window opens instead of confirming the document.
Select the :guilabel:`Approving User` among the possible approvers, then click :guilabel:`Send
Request`. A *To-Do* activity is scheduled for the approver.

.. note::
   - Users who are approvers of the document can confirm it directly.
   - Only one approval request can be pending on a document at a time.
   - Documents that require an approval must be confirmed one by one, not from the list view.

.. screenshot:: accounting-invoice-approval-request
   :menu: Accounting ‣ Vendors ‣ Bills ‣ (open a draft bill) ‣ Confirm
   :shows: "Request for Approval" dialog with the "Approving User" field and the "Send Request" and "Cancel" buttons.
   :highlight: The "Approving User" field (red frame).
   :data: Draft vendor bill of 800,000 HUF created by a user who is not an approver.
   :module: account_approval
   :notes: English UI, light theme, crop to the dialog.

.. _accounting/invoice-approval/answer:

Approving or rejecting
======================

The status of the last request is displayed above the draft document, with buttons to answer it:

- :icon:`fa-thumbs-o-up` (approve): the request is approved, and a *To-Do* activity asks the
  requesting user to confirm the document. The document can then be confirmed.
- :icon:`fa-thumbs-o-down` (reject): enter the :guilabel:`Reason for Rejection` and click
  :guilabel:`Send Reject`. The requesting user is notified with an activity.
- :icon:`fa-trash-o` (withdraw): the requesting user can withdraw the request; enter the
  :guilabel:`Reason for Withdrawal` and click :guilabel:`Send Withdraw`.

Only the approvers of the document can approve or reject a request. The history of the requests
(:guilabel:`Requesting User`, :guilabel:`Approving User`, :guilabel:`User of Answer`,
:guilabel:`Date of Answer`, :guilabel:`Message of Answer`, and status) is available in the
:guilabel:`Approvals` tab of the document.

.. important::
   If an approved document is modified (e.g., its partner, lines, delivery date, journal, or
   currency), the approval is automatically withdrawn, and a new approval must be requested.

.. screenshot:: accounting-invoice-approval-banner
   :menu: Accounting ‣ Vendors ‣ Bills ‣ (open a draft bill with a pending request)
   :shows: Draft vendor bill with the approval status banner above the form ("… requested approval of the invoice from …") and the approve, reject and withdraw icon buttons; the "Approvals" tab is open with the request history.
   :highlight: The status banner and its buttons (red frame).
   :data: Draft vendor bill of 800,000 HUF with a pending request.
   :module: account_approval
   :notes: English UI, light theme, 1440px width.

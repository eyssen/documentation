===========
Commissions
===========

Commissions reward salespeople for the business they bring in. The **Commissions** module records a
commission for every customer invoice line that matches a rule, so the amount paid out is derived
from actual invoicing — not from a manual estimate.

A commission is always the result of three records:

- a **commission plan**, which defines the period the commissions belong to;
- one or more **commission rules** inside that plan, which decide *which* invoice lines earn a
  commission and *how much*;
- the **commissions** themselves, one per invoice line and rule.

Configuration
=============

Install the **Commissions** module from the :menuselection:`Apps` application. Installing it also
installs :guilabel:`Margins` (``sale_margin``), because margin-based rules read the deal margin from
the sales order.

The module adds two access rights, under the :guilabel:`Commissions` category of the user form:

- :guilabel:`User`: sees their own commissions only. Every salesperson gets this level
  automatically.
- :guilabel:`Administrator`: sees every commission, and is the only level that can create plans and
  rules, collect and recompute commissions, and change a frozen deal salesperson. Sales
  administrators get this level automatically.

Accounting users also see every commission.

.. screenshot:: sales-commissions-access-rights
   :menu: Settings ‣ Users & Companies ‣ Users ‣ (a salesperson) ‣ Access Rights
   :shows: The Access Rights tab of a user form, scrolled to the "Commissions" category with the
      "User" level selected.
   :highlight: The "Commissions" access-right row (red frame).
   :data: Demo user "Mitchell Admin"; Sales = Administrator, Commissions = Administrator.
   :module: commission
   :notes: English UI, light theme, 1440px width, crop to the access-rights group.

Commission plans
================

To create a plan, go to :menuselection:`Sales app --> Configuration --> Commissions --> Plans` and
click :guilabel:`New`.

- :guilabel:`Name`: a label for the period or the scheme, for example `Sales 2026`.
- :guilabel:`Date From` / :guilabel:`Date To`: the invoice dates the plan covers. Both are optional;
  leaving one empty makes that side unbounded.
- :guilabel:`Company`: the company the plan belongs to (only shown in a multi-company database).
  A plan never collects commissions from another company's invoices.

Rules are added in the :guilabel:`Rules` tab. The plan's dates, company and rules can only be
changed while the plan is in the :guilabel:`Draft` stage.

.. screenshot:: sales-commissions-plan-form
   :menu: Sales ‣ Configuration ‣ Commissions ‣ Plans ‣ (a plan)
   :shows: A commission plan form in the "Running" stage, showing Date From/Date To and the Rules tab
      with three rules listed (name, trigger, rate type, rate, product type).
   :highlight: The status bar (Draft ‣ Running ‣ Closed) and the Start/Collect/Recompute/Close buttons
      (red frame).
   :data: Plan "Sales 2026", 01/01/2026 – 12/31/2026; rules "Goods 1.5%", "Services 3%",
      "Margin bands".
   :module: commission
   :notes: English UI, light theme, 1440px width, crop to the header and the Rules tab.

Plan stages
-----------

A plan moves through three stages, using the buttons in the header:

#. :guilabel:`Draft`: the plan is being prepared. Click :guilabel:`Start` to activate it. At least
   one active rule is required.
#. :guilabel:`Running`: the plan collects commissions. Posted customer invoices whose invoice date
   falls inside the plan's period are matched against the plan's rules automatically.
#. :guilabel:`Closed`: the plan no longer collects anything. Click :guilabel:`Reset to Draft` to
   reopen it.

Two more buttons are available while a plan is :guilabel:`Running`:

- :guilabel:`Collect`: scans every posted customer invoice, credit note and receipt in the plan's
  period and creates the commissions that are still missing. Use it after adding a rule to an
  already running plan, or after posting invoices while the plan was still in draft.
- :guilabel:`Recompute`: rebuilds the rate and amount of the commissions already collected, from the
  current rules and the current sales order margin. Collected commissions are otherwise frozen, so
  later cost changes cannot move them; use :guilabel:`Recompute` after changing a rule's bands.

The :guilabel:`Commissions` smart button on the plan opens the commissions collected by it.

Commission rules
================

A rule answers two questions: which invoice lines it applies to, and how much they earn. Rules are
added from the :guilabel:`Rules` tab of a plan, or from :menuselection:`Sales app --> Configuration
--> Commissions --> Rules`.

Within one plan the rules are evaluated in the order of the list (drag the handle to reorder), and
**the first matching rule wins** — an invoice line never earns twice from the same plan. Put the
most specific rules at the top.

When to pay
-----------

The :guilabel:`Trigger` field decides when a collected commission becomes payable:

- :guilabel:`Invoice Posted`: as soon as the invoice is posted.
- :guilabel:`Invoice Paid` (default): only once the invoice is fully paid. Invoices that are only
  *in payment* do not count.

The :guilabel:`Base` of the calculation is always the :guilabel:`Untaxed Amount` of the invoice
line, converted to the company currency at the invoice date.

How much
--------

The :guilabel:`Rate Type` field offers four calculation methods:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Rate type
     - Calculation
   * - :guilabel:`Fixed Percentage`
     - :guilabel:`Rate (%)` of the untaxed line amount. `1.5` means 1.5%.
   * - :guilabel:`Fixed Amount`
     - The :guilabel:`Amount Fixed` per matching invoice line, regardless of its value.
   * - :guilabel:`Amount Bands`
     - The rate depends on the untaxed line amount, looked up in the :guilabel:`Bands` tab.
   * - :guilabel:`Margin % Bands`
     - The rate depends on the margin of the *sales order* the line comes from, in percent points.

.. note::
   On a credit note the base amount — and therefore the commission — is negative, so refunds reduce
   the salesperson's total.

Bands
~~~~~

The :guilabel:`Bands` tab appears for both banded rate types. Each band has a :guilabel:`From`
value, a :guilabel:`To` value and a :guilabel:`Rate (%)`. :guilabel:`From` is inclusive,
:guilabel:`To` is exclusive, and `0` in :guilabel:`To` means *no upper bound*. If no band matches,
the rate is `0`.

.. example::
   A margin-band rule paying more on profitable deals:

   - :guilabel:`From` `10`, :guilabel:`To` `20`, :guilabel:`Rate (%)` `1.0`
   - :guilabel:`From` `20`, :guilabel:`To` `30`, :guilabel:`Rate (%)` `1.5`
   - :guilabel:`From` `30`, :guilabel:`To` `0`, :guilabel:`Rate (%)` `2.5`

   A deal with a 24% margin is paid 1.5% of the untaxed invoice amount.

.. screenshot:: sales-commissions-rule-bands
   :menu: Sales ‣ Configuration ‣ Commissions ‣ Rules ‣ (a rule) ‣ Bands
   :shows: A commission rule form with Rate Type = "Margin % Bands" and the Bands tab open, listing
      three bands (From, To, Rate) and the explanatory text above the list.
   :highlight: The Bands list (red frame).
   :data: Rule "Margin bands"; bands 10–20 = 1.0%, 20–30 = 1.5%, 30–0 = 2.5%.
   :module: commission
   :notes: English UI, light theme, 1440px width, crop to the notebook.

Deals without a cost
~~~~~~~~~~~~~~~~~~~~

If a sales order has no cost at all, the margin is reported as 100%, which would put every line in
the top band. The :guilabel:`Zero Cost Policy` field, shown for :guilabel:`Margin % Bands` rules,
decides what happens then:

- :guilabel:`No commission` (default): the rate is `0`.
- :guilabel:`Use fallback rate`: the :guilabel:`Fallback Rate (%)` field is used instead of the
  bands.
- :guilabel:`Use computed margin`: the 100% margin is kept, and the bands are applied to it.

Commissions collected from such an order are flagged :guilabel:`Cost Missing`, and can be listed
with the :guilabel:`Cost Missing` filter.

Which lines
-----------

The :guilabel:`Products` tab restricts the rule. A rule with an empty tab matches every invoice line
that has a product.

- :guilabel:`Product Type`: limit the rule to :guilabel:`Goods` or to :guilabel:`Service` lines.
- :guilabel:`Products` and :guilabel:`Categories`: the allowed list. A line matches if its product is
  listed, or if its product category is listed.
- :guilabel:`Include Child Categories` (on by default): also match the sub-categories of the listed
  categories.
- :guilabel:`Exclude Products`: products that never earn a commission from this rule, even if their
  category is listed.

.. tip::
   Because the first matching rule wins, an "everything else" rule with an empty
   :guilabel:`Products` tab placed **last** in the plan works as a default rate.

.. _sales/commissions/deal-salesperson:

Deal salesperson
================

The commission is credited to the :guilabel:`Deal Salesperson` of the invoice, not to whoever
happens to be the salesperson at payout time.

On a quotation, :guilabel:`Deal Salesperson` follows the :guilabel:`Salesperson` field as long as
the order is a quotation and the two were identical. When the order is confirmed, the field is
**frozen**: only a commission administrator can change it afterwards. The same applies to the
:guilabel:`Deal Salesperson` field on the customer invoice once the invoice is posted.

Invoices created from a sales order inherit the order's deal salesperson; invoices created directly
inherit their own :guilabel:`Salesperson`.

.. screenshot:: sales-commissions-deal-salesperson
   :menu: Sales ‣ Orders ‣ Orders ‣ (a confirmed order) ‣ Other Info
   :shows: The sales person group of a confirmed sales order, with the "Salesperson" and
      "Deal Salesperson" fields filled with two different users, and the "Commissions" smart button
      in the button box.
   :highlight: The "Deal Salesperson" field and the "Commissions" smart button (red frames).
   :data: Order S00042 for "Deco Addict"; Salesperson "Mitchell Admin", Deal Salesperson
      "Marc Demo"; 3 commissions.
   :module: commission
   :notes: English UI, light theme, 1440px width, crop to the button box and the Other Info group.

Reviewing commissions
=====================

Go to :menuselection:`Sales app --> Commissions` to see the collected commissions. Salespeople see
their own; commission and accounting administrators see all of them. The list opens filtered on the
current month.

Each commission shows the :guilabel:`Invoice` and :guilabel:`Invoice Line` it comes from, the
:guilabel:`Sales Order`, the :guilabel:`Plan` and :guilabel:`Rule` applied, the :guilabel:`Base
Amount`, the :guilabel:`Rate (%)`, the resulting :guilabel:`Amount`, and the invoice's
:guilabel:`Payment State`. The :guilabel:`Is Payable` field tells whether the commission has met its
rule's trigger, and :guilabel:`Payment Date` holds the date of the latest payment matched to the
invoice.

Useful filters and groupings:

- :guilabel:`My Commissions`, :guilabel:`Payable`, :guilabel:`Paid`, :guilabel:`This Month`,
  :guilabel:`Paid This Month`, :guilabel:`Cost Missing`, :guilabel:`Cancelled`.
- Group by :guilabel:`Salesperson`, :guilabel:`Invoice Date`, :guilabel:`Payment State`,
  :guilabel:`Product` or :guilabel:`Plan`.

The :guilabel:`Base` and :guilabel:`Commission` columns are totalled in the list, and the pivot view
(salespeople in rows, invoice month in columns) gives the payout per person and per month.

.. screenshot:: sales-commissions-list
   :menu: Sales ‣ Commissions
   :shows: The commissions list grouped by salesperson, with the Base and Commission column totals
      visible, and the Payment State and Status badges.
   :highlight: The "Payable" filter and the Commission column total (red frames).
   :data: Demo company; two salespeople, six commissions, mixed Paid / Not Paid payment states.
   :module: commission
   :notes: English UI, light theme, 1440px width, crop to the list and the search bar.

Cancelling a commission
-----------------------

A commission administrator can set a commission to :guilabel:`Cancelled` with the
:guilabel:`Cancel` button, and bring it back with :guilabel:`Restore`. Cancelled commissions are
never payable.

Odoo cancels commissions automatically when their invoice is reset to draft or cancelled. If that
invoice is posted again, the commissions are restored and refreshed.

.. note::
   Commissions are also reachable from the documents they come from: both the sales order and the
   customer invoice have a :guilabel:`Commissions` smart button.

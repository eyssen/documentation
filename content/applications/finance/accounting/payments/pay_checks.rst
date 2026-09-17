=============
Pay by checks
=============

Once you decide to pay a supplier bill, you can select to pay by check. You can then print all the
payments registered by check. Finally, the bank reconciliation process will match the checks you
sent to suppliers with actual bank statements.

Configuration
=============

Activate checks payment methods
-------------------------------

To activate the checks payment method, go to :menuselection:`Accounting --> Configuration -->
Settings`, and scroll down to the :guilabel:`Vendor Payments` section. There, you can activate the
:guilabel:`Checks` setting (which installs the *Check Printing Base* module) and set up the
:guilabel:`Check Layout`.

.. note::
   - Once the :guilabel:`Checks` setting is activated, the **Checks** payment method is
     automatically set up in the :guilabel:`Outgoing Payments` tabs of **bank** journals.
   - The available check layouts are provided by country-specific modules. If no layout is
     available (:guilabel:`None`), check numbers can still be tracked, but checks cannot be printed
     from Odoo.

Pay a supplier bill with a check
================================

Paying a supplier with a check is done in three steps:

1. registering a payment
2. printing checks in batch for all registered payments
3. reconciling bank statements

Register a payment by check
---------------------------

To register a payment, open any supplier bill from the menu :menuselection:`Accounting --> Vendors
--> Bills`. Once the supplier bill is confirmed, click :guilabel:`Pay`, set the :guilabel:`Payment
Method` to :guilabel:`Checks`, and click :guilabel:`Create Payment`.

Print checks
------------

On the accounting dashboard (:menuselection:`Accounting --> Dashboard`), the :guilabel:`Bank`
journal card shows the number of checks registered. Click :guilabel:`Checks to print` to list the
checks waiting to be printed (:guilabel:`Checks to Print` filter).

To print all checks in batch, select all payments from the list view and click on :guilabel:`Print`.

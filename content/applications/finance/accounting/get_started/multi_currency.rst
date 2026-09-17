=====================
Multi-currency system
=====================

Odoo allows you to issue invoices, receive bills, and record transactions in currencies other than
the main currency configured for your company. You can also set up bank accounts in other currencies
and run reports on your foreign currency activities.

.. seealso::
   - :doc:`../bank/foreign_currency`

.. _multi-currency/config:

Configuration
=============

.. _multi-currency/config-main-currency:

Main currency
-------------

The **main currency** is defined by default according to the company's country. You can change it by
going to :menuselection:`Accounting --> Configuration --> Settings`, and changing the currency in the
:guilabel:`Main Currency` setting of the :guilabel:`Currencies` section.

.. _multi-currency/config-enable:

Enable foreign currencies
-------------------------

Go to :menuselection:`Accounting --> Configuration --> Currencies`, and enable the currencies you
wish to use by toggling the :guilabel:`Active` button.

.. screenshot:: accounting-multi-currency-enable
   :menu: Accounting ‣ Configuration ‣ Currencies
   :shows: Currencies list with the "Active" toggle column; HUF, EUR and USD active.
   :highlight: The "Active" toggles (red frame).
   :data: Demo company "YourCompany HU".
   :module: base, account
   :notes: English UI, light theme, 1440px width.

.. _multi-currency/config-rates:

Currency rates
--------------

Manual update
~~~~~~~~~~~~~

To manually create and set a currency rate, go to :menuselection:`Accounting --> Configuration -->
Currencies`, click on the currency you wish to change the rate of, and under the :guilabel:`Rates`
tab, click :guilabel:`Add a line` to create a new rate.

.. screenshot:: accounting-multi-currency-manual-rate
   :menu: Accounting ‣ Configuration ‣ Currencies ‣ EUR ‣ Rates tab
   :shows: Currency form of EUR, "Rates" tab with the rate lines (Date, Unit per HUF, HUF per Unit) and the "Add a line" link.
   :highlight: "Add a line" (red frame).
   :data: Demo company "YourCompany HU" (HUF).
   :module: base, account
   :notes: English UI, light theme, 1440px width.

.. _multi-currency/config-rates-auto:

Automatic update
~~~~~~~~~~~~~~~~

The *eYssen currency rate updater* (`eyssen_currency_rate_live_community`) module retrieves the
currency rates automatically from a web service. When at least two currencies are active, the
:guilabel:`Update currency exchange rates` setting appears in the :guilabel:`Currencies` section of
:menuselection:`Accounting --> Configuration --> Settings`:

- :guilabel:`Provider`: the web service from which the rates are retrieved (e.g., the European
  Central Bank). The default provider depends on the company's country.
- :guilabel:`Interval Unit`: :guilabel:`Manually`, :guilabel:`Daily`, :guilabel:`Weekly`, or
  :guilabel:`Monthly`.
- :guilabel:`Next running time`: the date of the next automatic update.

Click the :icon:`fa-refresh` (:guilabel:`Update now`) button to update the rates immediately. The
provider of each rate is displayed in the :guilabel:`Exchange Provider` column of the currency's
:guilabel:`Rates` tab.

.. screenshot:: accounting-multi-currency-automatic-rates
   :menu: Accounting ‣ Configuration ‣ Settings
   :shows: "Currencies" section with the "Main Currency" setting and the "Update currency exchange rates" setting (provider, interval, next running time and the refresh button).
   :highlight: The "Update currency exchange rates" setting (red frame).
   :data: Demo company "YourCompany HU" with EUR and USD active; provider "European Central Bank", interval "Daily".
   :module: account, eyssen_currency_rate_live_community
   :notes: English UI, light theme, 1440px width, crop to the section. The setting labels may appear in Hungarian in the current module version.

.. note::
   The *MNB* rate provider for Hungarian companies is described in the Hungarian
   :doc:`fiscal localization <../../fiscal_localizations>` documentation.

.. _multi-currency/config-exch-diff:

Exchange difference entries
---------------------------

Odoo automatically records exchange differences entries on dedicated accounts, in a dedicated
journal.

You can define which journal and accounts to use to **post exchange difference entries** by
going to :menuselection:`Accounting --> Configuration --> Settings`, and editing the
:guilabel:`Journal`, :guilabel:`Gain`, and :guilabel:`Loss` fields of the :guilabel:`Exchange
difference entries` setting in the :guilabel:`Default Accounts` section.

.. example::
   If you receive a payment for a customer invoice one month after it was issued, the exchange rate
   has likely changed since. Therefore, this fluctuation implies some profit or loss due to the
   exchange difference, which Odoo automatically records in the default **Exchange Difference**
   journal.

.. _multi-currency/config-coa:

Chart of accounts
-----------------

Each account can have a set currency. By doing so, all moves relevant to the account are forced to
have that account's currency.

To do so, go to :menuselection:`Accounting --> Configuration --> Chart of Accounts` and select a
currency in the field :guilabel:`Account Currency`. If left empty, all active currencies are handled
instead of just one.

.. _multi-currency/config-journals:

Journals
--------

If a currency is set on a **journal**, that journal only handles transactions in that currency.

To do so, go to :menuselection:`Accounting --> Configuration --> Journals`, open the journal you
want to edit, and select a currency in the field :guilabel:`Currency`.

.. screenshot:: accounting-multi-currency-journal-currency
   :menu: Accounting ‣ Configuration ‣ Journals ‣ (open a bank journal)
   :shows: Bank journal form with the "Currency" field set to EUR.
   :highlight: The "Currency" field (red frame).
   :data: Demo bank journal "Bank EUR".
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the upper part of the form.

.. _multi-currency/mca:

Multi-currency accounting
=========================

.. _multi-currency/mca-documents:

Invoices, bills, and other documents
------------------------------------

For all documents, you can select the currency and journal to use for the transaction on the
document itself.

.. _multi-currency/fixed-rate:

Fixed currency rate
~~~~~~~~~~~~~~~~~~~

With the *eYssen currency rate updater* module, the invoice form displays the currency rate used
for the document and the date and provider of the applied rate below the journal. The rate
information is colored green if a rate of the relevant day is available, orange if the rate of the
previous day is used, and red if an older rate is used.

On vendor bills, refunds and receipts, the :guilabel:`Fixed Currency Rate` field allows you to
record the document at a given rate instead of the daily rate (e.g., the rate indicated on the
vendor's bill). A credit note created from a document with a fixed rate uses the same rate.

.. screenshot:: accounting-multi-currency-fixed-rate
   :menu: Accounting ‣ Vendors ‣ Bills ‣ (open a draft EUR bill)
   :shows: Draft vendor bill in EUR; below the Journal field, the currency rate information line and the "Fixed Currency Rate" field filled in.
   :highlight: The rate information and the "Fixed Currency Rate" field (red frame).
   :data: Demo company "YourCompany HU" (HUF); vendor bill in EUR with a fixed rate of 395.50.
   :module: account, eyssen_currency_rate_live_community
   :notes: English UI, light theme, 1440px width, crop to the upper part of the form.

.. screenshot:: accounting-multi-currency-invoice-currency
   :menu: Accounting ‣ Customers ‣ Invoices ‣ New
   :shows: Draft invoice with the "Journal" and "Currency" fields (currency EUR).
   :highlight: The "Journal" and "Currency" fields (red frame).
   :data: Demo company "YourCompany HU"; invoice in EUR.
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the upper part of the form.

.. _multi-currency/mca-payment:

Payment registration
--------------------

To register a payment in a currency other than your company's main currency, click on the
:guilabel:`Pay` button of your document and, in the pop-up window, select a **currency** next to the
:guilabel:`Amount` field.

.. screenshot:: accounting-multi-currency-register-payment
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (open a posted EUR invoice) ‣ Pay
   :shows: "Pay" dialog with the Journal, Payment Method, Amount (with currency selector) and Payment Date fields.
   :highlight: The currency next to the Amount field (red frame).
   :data: Posted customer invoice in EUR.
   :module: account
   :notes: English UI, light theme, crop to the dialog.

.. _multi-currency/mca-statements:

Bank transactions
-----------------

When creating or importing bank transactions, the amount is in the journal's currency. To input
a **foreign currency**, select a currency in the :guilabel:`Foreign Currency` field. Once selected,
enter the :guilabel:`Amount` in the journal's currency and the amount in the foreign currency in the
:guilabel:`Amount in Currency` field.

.. screenshot:: accounting-multi-currency-transaction-foreign
   :menu: Accounting ‣ Accounting ‣ Bank and Cash ‣ Bank Statements ‣ (open a statement line)
   :shows: Bank transaction with the "Foreign Currency" (USD) and "Amount in Currency" fields filled in.
   :highlight: The "Foreign Currency" and "Amount in Currency" fields (red frame).
   :data: Demo bank journal in HUF; transaction of 100 USD.
   :module: account, om_account_accountant
   :notes: English UI, light theme, 1440px width.

When reconciling, Odoo displays both the foreign currency amount and the equivalent amount in your
company's main currency.

.. _multi-currency/mca-exch-entries:

Exchange rate journal entries
-----------------------------

To see **exchange difference journal entries**, go to :menuselection:`Accounting --> Accounting -->
Journals --> Miscellaneous`, or open the :guilabel:`Exchange Difference` journal from
:menuselection:`Accounting --> Configuration --> Journals`.

.. screenshot:: accounting-multi-currency-exchange-entry
   :menu: Accounting ‣ Accounting ‣ Journals ‣ Miscellaneous ‣ (open an exchange difference entry)
   :shows: Journal entry of the "Exchange Difference" journal with the receivable line and the exchange gain/loss line.
   :highlight: The journal items (red frame).
   :data: Exchange difference entry created by the payment of a EUR invoice.
   :module: account
   :notes: English UI, light theme, 1440px width.

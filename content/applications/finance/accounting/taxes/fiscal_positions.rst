==========================================
Fiscal positions (tax and account mapping)
==========================================

Default taxes and accounts are set on products and customers to create new transactions on the fly.
However, depending on the customers' and providers' localization and business type, using different
taxes and accounts for a transaction might be necessary.

**Fiscal positions** allow the creation of rules to adapt the taxes and accounts used for a
transaction automatically.

They can be applied :ref:`automatically <fiscal_positions/automatic>`, :ref:`manually
<fiscal_positions/manual>`, or :ref:`assigned to a partner <fiscal_positions/partner>`.

.. note::
   Several default fiscal positions are available as part of your :ref:`fiscal localization
   package <fiscal_localizations/packages>`.

Configuration
=============

 .. _fiscal_positions/mapping:

Tax and account mapping
-----------------------

To edit or create a fiscal position, go to :menuselection:`Accounting --> Configuration --> Fiscal
Positions`, and open the entry to modify or click on :guilabel:`New`.

The mapping of taxes and accounts is based on the default taxes and accounts defined in the
product form.

- To map to another tax or account, fill out the right column (:guilabel:`Tax to Apply`/
  :guilabel:`Account to Use Instead`).

.. screenshot:: accounting-fiscal-positions-tax-mapping
   :menu: Accounting ‣ Configuration ‣ Fiscal Positions ‣ (open a fiscal position) ‣ Tax Mapping tab
   :shows: "Tax Mapping" tab with "Tax on Product" → "Tax to Apply" lines (e.g., "27%" → "0% EU G").
   :highlight: The mapping lines (red frame).
   :data: Demo company "YourCompany HU"; fiscal position "EU (intra-community)".
   :module: account
   :notes: English UI, light theme, 1440px width.

.. screenshot:: accounting-fiscal-positions-account-mapping
   :menu: Accounting ‣ Configuration ‣ Fiscal Positions ‣ (open a fiscal position) ‣ Account Mapping tab
   :shows: "Account Mapping" tab with "Account on Product" → "Account to Use Instead" lines.
   :highlight: The mapping lines (red frame).
   :data: Demo company "YourCompany HU"; fiscal position "EU (intra-community)".
   :module: account
   :notes: English UI, light theme, 1440px width.

- To remove a tax, leave the field :guilabel:`Tax to Apply` empty.
- To replace a tax with several other taxes, add multiple lines using the same :guilabel:`Tax on
  Product`.

.. note::
   The mapping only works with *active* taxes. Therefore, make sure they are active by going to
   :menuselection:`Accounting --> Configuration --> Taxes`.

Application
===========

.. _fiscal_positions/automatic:

Automatic application
---------------------

To automatically apply a fiscal position following a set of conditions, go to
:menuselection:`Accounting --> Configuration --> Fiscal Positions`, open the fiscal position to
modify, and tick :guilabel:`Detect Automatically`.

From there, several conditions can be activated:

- :guilabel:`VAT Required`: the customer's VAT number must be present on their contact form.
- :guilabel:`Country Group` and :guilabel:`Country`: the fiscal position is only applied to the
  selected country or country group.
- :guilabel:`Federal States` and :guilabel:`Zip Range`: when a country is selected, the fiscal
  position can be further restricted to some states or to a range of zip codes.

Other fields of the fiscal position form:

- :guilabel:`Foreign Tax ID`: your company's tax ID in the region mapped by the fiscal position
  (e.g., when you are registered for VAT in another country).
- :guilabel:`Notes`: legal mentions printed on the invoices that use the fiscal position.

.. screenshot:: accounting-fiscal-positions-automatic
   :menu: Accounting ‣ Configuration ‣ Fiscal Positions ‣ (open a fiscal position)
   :shows: Upper part of the fiscal position form: "Detect Automatically" enabled, "VAT required" enabled, "Country Group" set to "Europe".
   :highlight: The "Detect Automatically", "VAT required" and "Country Group" fields (red frame).
   :data: Demo company "YourCompany HU"; fiscal position "EU (intra-community)".
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the upper part of the form.

.. note::
   - If the :doc:`Verify VAT Numbers <vat_verification>` feature is enabled, any fiscal positions
     with :guilabel:`VAT required` enabled will require Intra-Community valid VAT numbers to apply
     automatically.
   - Taxes on **eCommerce orders** are automatically updated once the customer has logged in or
     filled out their billing details.

.. important::
   The fiscal positions' **sequence** defines which fiscal position is applied if all conditions
   set on multiple fiscal positions are met simultaneously.

   For example, suppose the first fiscal position in a sequence targets *country A* while the second
   fiscal position targets a *country group* that comprises *country A*. In that case, only the
   first fiscal position will be applied to customers from *country A*.

.. _fiscal_positions/manual:

Manual application
------------------

To manually select a fiscal position, open a sales order, invoice, or bill, go to the
:guilabel:`Other Info` tab and select the desired :guilabel:`Fiscal Position` before adding product
lines.

.. screenshot:: accounting-fiscal-positions-manual
   :menu: Accounting ‣ Customers ‣ Invoices ‣ (open a draft invoice) ‣ Other Info tab
   :shows: "Other Info" tab of a draft invoice with the "Fiscal Position" field selected.
   :highlight: The "Fiscal Position" field (red frame).
   :data: Demo customer invoice.
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the tab.

.. _fiscal_positions/partner:

Assign to a partner
-------------------

To define which fiscal position must be used by default for a specific partner, go to
:menuselection:`Accounting --> Customers --> Customers`, select the partner, open the
:guilabel:`Sales & Purchase` tab, and select the :guilabel:`Fiscal Position`.

.. screenshot:: accounting-fiscal-positions-customer
   :menu: Accounting ‣ Customers ‣ Customers ‣ (open a customer) ‣ Sales & Purchase tab
   :shows: "Sales & Purchase" tab of a company contact; "Fiscal Information" section with the "Fiscal Position" field.
   :highlight: The "Fiscal Position" field (red frame).
   :data: Demo customer company from another EU country.
   :module: account
   :notes: English UI, light theme, 1440px width, crop to the tab.

.. seealso::

  * :doc:`../taxes`
  * :doc:`B2B_B2C`

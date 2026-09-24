=======================
Import vendor pricelist
=======================

Set vendor prices to auto-populate requests for quotations (RFQs) or purchase orders (POs) with the
unit price, once the product is added, which reduces errors and saves time.

In Odoo, vendor pricelists can be :ref:`added individually <purchase/products/pricelist>` on the
product form, or :ref:`imported in bulk <purchase/products/import-pricelist>`, via an XLSX or CSV
file.

.. important::
   Please review this :doc:`import guide <../../../essentials/export_import_data>` before uploading
   vendor pricelists.

.. _purchase/products/pricelist:

On product form
===============

To manually add the vendor price on the product form, go to the :menuselection:`Purchase app -->
Products --> Products`, and click the desired product.

.. note::
   Product forms are accessible from multiple apps, such as **Sales**, **Inventory**, and
   **Manufacturing**.

In the :guilabel:`Purchase` tab of the product form, input the vendor and their price, to have this
information auto-populate on a request for quotation each time the product is listed.

.. seealso::
   :ref:`Vendor pricelist on product form <purchase/manage_deals/vendor-pricelist>`

.. screenshot:: purchase-pricelist-product-form
   :menu: Purchase ‣ Products ‣ Products ‣ (open a product) ‣ Purchase
   :shows: The Purchase tab of a product form with a vendor pricelist line: vendor, quantity, unit
           price, and delivery lead time.
   :highlight: The vendor pricelist line (red frame).
   :data: Demo company "YourCompany"; vendor "Azure Interior".
   :module: purchase
   :notes: English UI, light theme, 1440px width.

.. _purchase/products/import-pricelist:

Import vendor pricelist
=======================

To import vendor pricelists, ensure the XLSX or CSV file is accurately completed. The best way to
obtain a correctly formatted template, including product names, references, and vendor details, is
to first :ref:`export a pricelist <purchase/products/export-price>` from the database.

Modify the exported file, as needed, then import it back into the Odoo database.

.. _purchase/products/export-price:

Export pricelist
----------------

To export a pricelist, go to :menuselection:`Purchase app --> Configuration --> Vendor Pricelists`.

On the page, tick the checkbox(es) for the desired vendor pricelists.

Then, click the :icon:`fa-cog` :guilabel:`Actions` button that appears, and choose :icon:`fa-upload`
:guilabel:`Export` from the drop-down menu.

.. screenshot:: purchase-pricelist-export
   :menu: Purchase ‣ Configuration ‣ Vendor Pricelists
   :shows: The Vendor Pricelists list with several lines selected, and the "Export" option open in
           the Actions drop-down menu.
   :highlight: The Actions ‣ Export menu entry (red frame).
   :data: Demo company "YourCompany"; three selected vendor pricelist lines.
   :module: purchase
   :notes: English UI, light theme, 1440px width.

In the resulting pop-up window, fields listed under the :guilabel:`Fields to export` section are
included in the exported file. To add more fields, find the desired field in the
:guilabel:`Available fields` section, and click the :icon:`fa-plus` :guilabel:`(plus)` icon to the
right of the field.

.. note::
   To update to existing records, tick the :guilabel:`I want to update data (import-compatible
   export)` checkbox, and refer to the section on the :ref:`External ID
   <purchase/products/external-id>` field.

   For details on commonly-used fields for importing vendor pricelists, see the :ref:`Common fields
   <purchase/products/common-fields>` section.

Select the desired :guilabel:`Export Format`: :guilabel:`XLSX` or :guilabel:`CSV`.

To save the selected fields as a template, click the :guilabel:`Template` field, and select
:guilabel:`New template` from the drop-down menu. Type the name of the new template, and click the
:icon:`fa-floppy-o` :guilabel:`(save)` icon. After that, the template is a selectable option when
clicking the :guilabel:`Template` field.

Finally, click :guilabel:`Export`.

.. note::
   With :ref:`developer mode <developer-mode>` turned on, the column names of the exported file
   display the *field name* with the *technical name* in parenthesis.

.. example::
   .. screenshot:: purchase-pricelist-export-data
      :menu: Purchase ‣ Configuration ‣ Vendor Pricelists ‣ Actions ‣ Export
      :shows: The Export Data pop-up window, with the "Product Template" and other fields listed
              under "Fields to export", and "XLSX" selected as the export format.
      :highlight: The Fields to export list.
      :data: Demo company "YourCompany".
      :module: purchase
      :notes: English UI, light theme, 1440px width.

.. _purchase/products/external-id:

External ID
~~~~~~~~~~~

*External ID* is a unique identifier used to update existing vendor pricelists. Without it, imported
records create new entries, instead of updating existing ones. Including this field in the XLSX or
CSV, indicates the line replaces an existing vendor pricelist in the Odoo database.

.. example::
   .. screenshot:: purchase-pricelist-duplicate-values
      :menu: Purchase ‣ Configuration ‣ Vendor Pricelists
      :shows: The Vendor Pricelists list with "Ready Mat" appearing twice, at $790 and $780.
      :highlight: The two "Ready Mat" lines (red frame).
      :data: Demo company "YourCompany"; vendor "Ready Mat", prices $790 and $780.
      :module: purchase
      :notes: English UI, light theme, 1440px width. `Ready Mat` appears twice because the
              external ID was omitted during the price update from `$790` to `$780`.

To look-up the :guilabel:`External ID` for a vendor pricelist, tick the :guilabel:`I want to update
data (import-compatible export)` checkbox at the top of the :guilabel:`Export Data` pop-up window.

.. note::
   Selecting :guilabel:`External ID` from the :guilabel:`Available fields` section with the
   :guilabel:`I want to update data (import-compatible export)` checkbox ticked results in an export
   file with two columns containing the external ID.

.. _purchase/products/common-fields:

Common fields
~~~~~~~~~~~~~

Below is a list of commonly-used fields when importing vendor pricelists:

.. list-table:: Field name definitions
   :header-rows: 1

   * - Field name
     - Used for
     - Field in Odoo database
     - Technical name of field
   * - Vendor
     - The only required field for creating a vendor pricelist record. This field specifies the
       vendor associated with the product.
     - :guilabel:`Vendor` field in the :ref:`vendor pricelist of the product form
       <purchase/products/pricelist>`.
     - `partner_id`
   * - Product Template
     - The Odoo product the vendor pricelist entry is related to.
     - :guilabel:`Product` field in the vendor pricelist.
     - `product_tmpl_id`
   * - Product Variant
     - Restricts the price to a single variant of the product. Leave empty to apply the price to
       every variant.
     - :guilabel:`Variant` field in the vendor pricelist (enable it via the
       :icon:`oi-settings-adjust` :guilabel:`(adjust)` icon).
     - `product_id`
   * - Quantity
     - The minimum quantity required to receive the product at the specified price.
     - :guilabel:`Quantity` field in the vendor pricelist. (If not visible, enable it by clicking
       the :icon:`oi-settings-adjust` :guilabel:`(adjust)` icon, and tick the :guilabel:`Quantity`
       checkbox)
     - `min_qty`
   * - Unit Price
     - The purchase price for the product from the vendor.
     - :guilabel:`Price` field in the vendor pricelist.
     - `price`
   * - Delivery Lead Time
     - :ref:`Number of days <inventory/warehouses_storage/purchase-lt>` before receiving the product
       after confirming a purchase order.
     - :guilabel:`Delivery Lead Time` field on the vendor pricelist.
     - `delay`
   * - Start Date / End Date
     - The date range during which this vendor price is used. Leave both empty for a price that
       never expires.
     - :guilabel:`Validity` field in the vendor pricelist (enable it via the
       :icon:`oi-settings-adjust` :guilabel:`(adjust)` icon).
     - `date_start` / `date_end`
   * - Sequence
     - Defines the order of vendors in the pricelist when multiple vendors are available. For
       example, if `Azure Interior` is listed first and Wood Corner second, their sequences would be
       `1` and `2`.
     - N/A
     - `sequence`
   * - Company
     - Name of company the product belongs to.
     - :guilabel:`Company` field in the vendor pricelist.
     - `company_id`
   * - :ref:`External ID <purchase/products/external-id>`
     - Unique ID of a record used to update existing vendor pricelists.
     - N/A
     - `id`

Import records
--------------

With a template downloaded, fill out the XLSX or CSV file with the necessary information. After
inputting everything, import the file back into the Odoo database, by going to
:menuselection:`Purchase app --> Configuration --> Vendor Pricelists`.

On the page, click the :icon:`fa-cog` :guilabel:`(gear)` icon in the top-left corner. In the
drop-down menu that appears, click :guilabel:`Import records`.

Then, click :guilabel:`Upload File` in the upper-left corner, and after selecting the XLSX or CSV
file, confirm the correct fields, and click :guilabel:`Import`.

.. seealso::
   - :doc:`../../../essentials/export_import_data`
   - :ref:`Common fields <purchase/products/common-fields>`

.. screenshot:: purchase-pricelist-supplier-example
   :menu: Purchase ‣ Configuration ‣ Vendor Pricelists ‣ Import records ‣ Upload File
   :shows: The import "Upload File" screen with an XLSX file selected and its columns mapped to
           Odoo fields.
   :highlight: The Upload File button (red frame).
   :data: Demo company "YourCompany"; sample vendor pricelist import file.
   :module: purchase
   :notes: English UI, light theme, 1440px width.

Formatting import file
~~~~~~~~~~~~~~~~~~~~~~

To understand how to format import files for vendor pricelists, consider the following example.

- `Storage Box` (:guilabel:`Reference`: `E-COM08`) is sold by `Wood Corner` for `$10`.
- `Large Desk` (:guilabel:`Reference`: `E-COM09`) has no records in the vendor pricelist.

An import file is created to do the following:

- Update the price for `Wood Corner` from `$10` to `$13`.
- Add pricelist for `Storage Box`: the vendor, `Ready Mat` intends to sell the product for `$14`.
- Add pricelist for `Large Desk`: vendor is `Wood Corner`, price is `$1299`.
- Add pricelist for `Large Desk`: vendor is `Azure Interior`, price is `$1399`.

.. list-table:: Vendor pricelist data
   :header-rows: 1

   * - id
     - company_id
     - delay
     - price
     - product_tmpl_id
     - sequence
     - partner_id
   * - product.product_supplierinfo_3
     - My Company (San Francisco)
     - 3
     - 13.00
     - [E-COM08] Storage Box
     - 4
     - Wood Corner
   * -
     - My Company (San Francisco)
     - 3
     - 14.00
     - [E-COM08] Storage Box
     - 5
     - Ready Mat
   * -
     - My Company (San Francisco)
     - 2
     - 1299.00
     - [E-COM09] Large Desk
     - 6
     - Wood Corner
   * -
     - My Company (San Francisco)
     - 4
     - 1399.00
     - [E-COM09] Large Desk
     - 7
     - Azure Interior

.. note::
   The *technical field name* was used to create this information.

.. note::
   Download the sample files for reference:

   - :download:`Sample XLSX import file <pricelist/pricelist-example.xlsx>`
   - :download:`Sample CSV import file <pricelist/pricelist-example.csv>`

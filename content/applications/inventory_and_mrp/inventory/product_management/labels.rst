=======================
Product and lot labels
=======================

Labels are printed from Odoo for two different things: a **product** (its name, internal reference,
barcode and optionally a price) and a **lot or serial number**. Both are produced from the record
lists themselves, so no separate label application is needed.

Print product labels
====================

Select one or more products in :menuselection:`Inventory app --> Products --> Products` (or open a
single product) and click :guilabel:`Print Labels`. The pop-up that appears offers:

- :guilabel:`Format`: the label sheet layout — :guilabel:`Dymo`,
  :guilabel:`2 x 7 with price`, :guilabel:`4 x 7 with price`, :guilabel:`4 x 12` or
  :guilabel:`4 x 12 with price`.
- :guilabel:`Quantity`: how many labels to print per product.
- :guilabel:`Pricelist`: the pricelist whose price is shown on the formats that include a price.
- :guilabel:`Extra Content`: free text added to every label.

.. screenshot:: inventory-labels-print-product-labels
   :menu: Inventory ‣ Products ‣ Products ‣ (select products) ‣ Print Labels
   :shows: The product label pop-up with the Format, Quantity, Pricelist and Extra Content fields, the
      Format drop-down open showing all layout choices.
   :highlight: The "Format" and "Pricelist" fields (red frame).
   :data: Three selected products; format "4 x 12 with price"; pricelist "Public (HUF)".
   :module: product
   :notes: English UI, light theme, 1440px width, crop to the pop-up.

.. seealso::
   :ref:`Print lot labels <inventory/product_management/lot-labels>`

.. _inventory/product_management/custom-labels:

Custom label designs
====================

The eYssen *Custom Product Label* module (``eyssen_product_custom_label``) adds label layouts of
your own next to the built-in ones, so a company can print labels that match its own shelf edges,
label rolls or legal requirements.

Label designs are maintained under :menuselection:`Inventory app --> Configuration --> Label
Designs` (the menu is also available in **Sales**). Each design has:

- :guilabel:`Name` — what the design is called in the :guilabel:`Format` drop-down of the product
  label pop-up.
- :guilabel:`Paper Format` — the paper format used when the label sheet is rendered.
- :guilabel:`Barcode Size`, :guilabel:`Table Style` and :guilabel:`Padding Page` — CSS style values
  applied to the barcode image, the label table and the page margins.
- :guilabel:`Label XML` — the label body itself, written as a QWeb template. The design has access
  to the product, its barcode and the selected pricelist.

.. screenshot:: inventory-labels-design-form
   :menu: Inventory ‣ Configuration ‣ Label Designs ‣ (a design)
   :shows: A label design form with the Name, Paper Format, Barcode Size, Table Style and Padding Page
      fields, and the "Label XML" editor below them holding a label template.
   :highlight: The "Name" and "Label XML" fields (red frames).
   :data: Design "Shelf label 40x20" with a small barcode and the product name, reference and price.
   :module: eyssen_product_custom_label
   :notes: English UI, light theme, 1440px width, full form.

Once a design is saved, it appears as an extra entry in the :guilabel:`Format` field of the
:guilabel:`Print Labels` pop-up, and printing works exactly as with the standard layouts.

.. screenshot:: inventory-labels-custom-format
   :menu: Inventory ‣ Products ‣ Products ‣ (select products) ‣ Print Labels
   :shows: The product label pop-up with the "Format" drop-down open, showing the custom label designs listed
      after the built-in layouts.
   :highlight: The custom entries in the drop-down (red frame).
   :data: Two custom designs, "Shelf label 40x20" and "Warehouse bin label".
   :module: eyssen_product_custom_label
   :notes: English UI, light theme, 1440px width, crop to the field and the open drop-down.

.. important::
   Saving a label design triggers an in-place module upgrade so the new format becomes selectable
   immediately. Create and rename designs outside of busy hours.

.. note::
   If a design's :guilabel:`Paper Format` is left empty, the default label paper format is used.

Barcode format check
====================

The eYssen *Product Barcode* module (``eyssen_product_barcode``) validates barcodes against the
company's own barcode standard and renders the barcode as an image on the product.

Configure the standard once per company in :menuselection:`Settings --> eYssen ERP`:

- :guilabel:`Barcode Type` — the symbology the company uses (for example EAN-13).
- :guilabel:`Barcode Length` — the number of characters a barcode must have.

.. screenshot:: inventory-labels-barcode-settings
   :menu: Settings ‣ eYssen ERP
   :shows: The eYssen ERP settings with the "Barcode Type" and "Barcode Length" fields.
   :highlight: The two fields (red frame).
   :data: Barcode type "EAN-13", length 12.
   :module: eyssen_product_barcode
   :notes: English UI, light theme, 1440px width, crop to the setting rows.

On the product form, the module shows the barcode as a rendered :guilabel:`Barcode` image next to
the :guilabel:`Barcode` field, so a wrong or missing code is spotted at a glance. The same image is
used by the :guilabel:`Product Information` screen of the eYssen *Barcode* app.

.. screenshot:: inventory-labels-barcode-image
   :menu: Inventory ‣ Products ‣ Products ‣ (a product) ‣ General Information tab
   :shows: A product form showing the "Barcode" field with the rendered barcode image generated next to it.
   :highlight: The barcode image (red frame).
   :data: A product with a valid EAN-13 barcode.
   :module: eyssen_product_barcode
   :notes: English UI, light theme, 1440px width, crop to the field.

.. seealso::
   :doc:`../../barcode`

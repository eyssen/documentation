================================
Environmental product fee (KVTD)
================================

The :guilabel:`KVTD` (`eyssen_l10n_hu_kvtd`) module records the environmental product fee
(*környezetvédelmi termékdíj*) content of products, calculates the fee-liable weight and the fee on
invoice lines, prints it on customer invoices, and provides the list needed to prepare the product
fee return. It can be installed from the Apps menu or by ticking :guilabel:`Hungarian KVTD` in the
general settings.

.. note::
   - The fee is **informative**: it does not change the price, the taxes or the journal entry of the
     invoice, and no return file is generated.
   - The menus and fields of this module are displayed in Hungarian in the current module version.

Configuration
=============

Fee types
---------

Go to :menuselection:`Accounting --> Configuration --> Környezetvédelmi termékdíj --> Termékdíj
típusok` and create a row for every fee item used by the company:

- :guilabel:`Megnevezés`: unique name;
- :guilabel:`KT/CSK kód`: the KT or CsK code of the fee item;
- :guilabel:`Termékdíj kategória`: battery, packaging, other petroleum products, tyres,
  refrigerants, advertising paper, or electrical and electronic equipment;
- :guilabel:`VTSZ`: customs tariff number (optional);
- :guilabel:`Díjtétel (Ft/kg)`: the fee rate in HUF per kilogram;
- :guilabel:`Mode`: :guilabel:`Bejövő számla alapján` (the fee is recorded on vendor bills) or
  :guilabel:`Kiemnő számla alapján` (on customer invoices).

Products
--------

On the :guilabel:`KVTD` tab of the product form, add a line for every fee type contained in the
product with the :guilabel:`Mennyiség (kg)`: the weight of the fee-liable material in **one unit** of
the product. The same assignments can be edited in bulk in :menuselection:`Accounting -->
Configuration --> Környezetvédelmi termékdíj --> Termékdíj termékenként`.

On the :guilabel:`Inventory` tab, :guilabel:`Nettó súly` (net weight) can be recorded next to the
:guilabel:`Weight`. A red ✕ warns if the weight minus the packaging fee quantities differs from the
net weight.

.. note::
   Fee types and product assignments can be modified by users with the :guilabel:`Settings`
   administration right; other users can only read them.

.. screenshot:: finance-fl-hungary-kvtd-product
   :menu: Inventory ‣ Products ‣ Products ‣ (product) ‣ KVTD tab
   :shows: Product form with the "KVTD" tab open, listing two fee types ("Termékdíj fajtája") with their quantity in kg per unit ("Mennyiség (kg)").
   :highlight: The KVTD lines (red frame).
   :data: Product "Office Chair"; fee types "Műanyag csomagolás" 0.35 kg and "Karton csomagolás" 1.20 kg.
   :module: eyssen_l10n_hu_kvtd
   :notes: Hungarian field labels (hardcoded), light theme, 1440px width, crop to the tab.

Invoices
========

When a product with fee assignments is added to a customer invoice (types recorded on customer
invoices) or to a vendor bill (types recorded on vendor bills), a KVTD record is created for each fee
type: weight = quantity per unit × invoiced quantity, fee = weight × rate.

- The optional :guilabel:`KVTD` column of the invoice lines shows the weight and the fee type.
- The pencil icon at the end of the line opens the journal item, where the :guilabel:`KVTD` tab
  allows changing the fee type and the :guilabel:`Súly (kg)`; the fee is recalculated.
- On the printed customer invoice, the fee content is shown under the line: code, name, weight, and
  the sentence stating the amount of the product fee included in the gross price.

.. important::
   In the current module version, no KVTD records are created on credit notes, the quantity is not
   converted between units of measure, and the existing records are not updated when the quantity of
   the line is changed later: check the weight with the pencil icon in these cases.

Reporting
=========

:menuselection:`Accounting --> Reporting --> Környezetvédelmi termékdíj` lists the KVTD records of
**posted** invoices with the invoice date, invoice line, fee type, KT/CSK code, category, VTSZ, mode,
:guilabel:`Súly (kg)`, :guilabel:`Díjtétel (Ft)` and :guilabel:`Termékdíj (Ft)`. Filter by mode and
by :guilabel:`Számla kelte` (invoice date), group by fee type or category, and export the list to a spreadsheet to total the weights and fees
for the quarterly product fee return.

===========================================
Quotation, bill of materials and purchasing
===========================================

Create the quotation
====================

When the import is :guilabel:`Reviewed`, click :guilabel:`Create quotation`. A window opens with the
weights and prices of the import:

- :guilabel:`Manufacturing weight`: choose :guilabel:`Option 1: without purlins` or :guilabel:`Option
  2: with purlins`. The :guilabel:`Manufacturing quantity (kg)` below shows the weight that will be
  quoted. Option 2 is proposed.
- :guilabel:`Manufacturing price per kg`: the default comes from the import, which takes it from the
  settings.
- :guilabel:`Add assembly` and :guilabel:`Assembly price per kg`: assembly is optional and is always
  quoted on the weight of **option 2**, purlins included.
- :guilabel:`Pricelist`: a pricelist in euro is proposed when one exists. Otherwise the customer's
  pricelist is used, and a note in the chatter of the import and of the order says that the
  quotation is not in euro.
- :guilabel:`Untaxed amount`: the total, for your information.

Click :guilabel:`Create quotation`. The sales order gets two lines in kilograms, *Steel structure
manufacturing* (the weight of the chosen option) and *Steel structure assembly* (the weight of option
2). The prices you typed are kept, so the price stays purely kg-based; taxes come from the products and
the fiscal position. The prices are also written back to the import. You can create another quotation
with :guilabel:`New quotation`; all of them are listed behind the :guilabel:`Quotations` button.

.. screenshot:: manufacturing-cad-quote-wizard
   :menu: Manufacturing app --> CAD imports --> (an import) --> Create quotation
   :shows: The quotation window with the two options, the manufacturing and assembly prices per kg and
      the untaxed amount.
   :highlight: The Manufacturing weight option and the two price fields (red frames).
   :data: Option 2 selected, 2.50 and 0.80 euro per kg.
   :module: mrp_cad_bom_import
   :notes: English UI, light theme, 1440px width, crop to the window.

Accept the quotation
====================

When the customer confirms the sales order, the import becomes :guilabel:`Accepted`. If the quotation
was accepted outside Odoo, click :guilabel:`Mark as accepted`.

With the setting :guilabel:`Create the BoM when the quotation is confirmed` (on by default) the bill of
materials is created at once. A failure does not block the order: the error is posted in the
chatter of the import and you create the bill of materials by hand with :guilabel:`Create BoM`.
That button, and :guilabel:`New BoM version` after an import is :guilabel:`Done`, needs the
*Manufacturing / Administrator* right. The automatic creation runs with elevated rights when the
person confirming the order is not an administrator.

.. _manufacturing/cad_bom_import/products:

Products and the bill of materials
==================================

The importer gives every distinct material a **product key** of the form
``FAMILY|DESIGNATION|GRADE``, for example ``SHS|100X100X4|S235JR``. Plates bought in kilograms have one
key per thickness (``PLATE|T10|S235JR``); plates bought in pieces have one per size
(``PLATE|300X300X10|S235JR``). The key is stored on the product in the field :guilabel:`CAD material key`.

For each line the product is found in this order:

1. the product you chose on the line;
2. a product with the same CAD key;
3. a product remembered in :menuselection:`Manufacturing app --> Configuration --> CAD product
   aliases`;
4. a product whose internal reference equals the key written with dashes (for products coded that
   way by hand);
5. a product with the same name, ignoring case, accents, spaces and separators; and
6. otherwise a new product is created. **Only missing products are created.**

A product you choose by hand on a line is remembered as an alias when the bill of materials is
created, so the next import finds it. On the line, :guilabel:`Product action` shows whether the
product is an existing one or will be created.

Created products are storable goods in a category per kind (*Steel materials*, with *Profiles*, *Hollow
sections*, *Purlins*, *Bars*, *Plates*, *Bolts* and *Other materials*). Profiles, tubes, bars and purlins
are measured in metres (the bill of materials quantity is the total length, the product weight is kg
per metre), plates in kilograms or pieces according to the setting, bolts in units. They carry:

- their **main material**, the grade of the line, with its density;
- their **shape and dimensions** in millimetres: I, H and U sections and angles as open profiles
  (height, width, web and flange thickness), Z, C and Σ purlins as open profiles, square and
  rectangular hollow sections as hollow sections, round hollow sections as tubes, flat bars and plates
  as cuboids, and round bars as cylinders; and
- the **cross-section area** the import weighed with, with :guilabel:`Weight from Dimensions` switched
  on. The weight of the product therefore equals area x density and follows later changes of the
  material density.

The importer never writes the internal reference itself. When the rules of the *default code* module
are installed, they code the new product; otherwise the reference stays empty.

The **bill of materials** is made for a finished product named after the project or the import. It has
one line per product (quantities of equal products are added up) and the reference ``CAD v1``,
``CAD v2``, and so on. A new bill of materials archives the previous ones of the import, so the history
is kept; all versions are behind the :guilabel:`BoMs` button.

.. _manufacturing/cad_bom_import/procurement:

Procurement list
================

Click :guilabel:`Procurement list` (or :guilabel:`Compute` on the tab :guilabel:`Procurement list`) to
work out what to buy. The lines are grouped by product key.

- **Linear members** (profiles, tubes, bars, purlins): the *stock length* is the quantity of the
  product's first packaging (for example "Bar 6 m" with a quantity of 6 on a product in metres), and
  otherwise the stock length of the kind in the settings. The number of :guilabel:`Bars` is the larger
  of two figures: a first-fit-decreasing packing of the pieces into bars, and the total length plus the
  :guilabel:`Waste (%)` divided by the stock length. The :guilabel:`Purchase quantity` is bars x stock
  length. A piece longer than a stock bar is noted ("joints needed").
- **Plates**: the area in m² and the weight with waste, or pieces if plates are bought per piece.
- **Bolts and others**: pieces.

The columns show the :guilabel:`Net quantity`, :guilabel:`Stock length (m)`, the :guilabel:`Stock
packaging` it came from, :guilabel:`Bars`, :guilabel:`Waste (%)`, :guilabel:`Purchase quantity` and the
first :guilabel:`Vendor` of the product. Use :guilabel:`PDF` and :guilabel:`XLSX` for the report
*Procurement list*.

Create requests for quotation
-----------------------------

Click :guilabel:`Create RFQs`, choose a :guilabel:`Default vendor` for the products that have no
vendor, review the materials and confirm. The module creates the missing products, then one **draft**
purchase order per vendor (the first vendor of each product, with its price and the packaging as the
line packaging), converting the quantities to the purchase unit of measure. Lines without any vendor are
reported to you. Nothing is confirmed: you confirm the requests for quotation yourself. They are listed
behind the :guilabel:`RFQs` button.

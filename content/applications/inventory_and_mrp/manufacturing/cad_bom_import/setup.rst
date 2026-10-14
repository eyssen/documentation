=====================
Set up the CAD import
=====================

This page lists what the server needs, the settings of the import and the master data it relies on.

.. _manufacturing/cad_bom_import/requirements:

Requirements
============

Install the module **CAD Bill of Materials Import** (``mrp_cad_bom_import``). It depends on
*Manufacturing*, *Sales*, *Purchase*, *Project* and the eYssen modules for the :ref:`material master
and product dimensions <inventory/product_data/material>`, which are installed with it.

The server needs the following software.

- **ezdxf**, a Python library (MIT license) that reads DXF files. It is installed with
  ``pip install ezdxf`` and listed in ``requirements-eyssen.txt``.
- **LibreDWG** and its ``dwgread`` program, but *only* if you import DWG files. **DXF files need no
  converter.** If ``dwgread`` is missing, the import stops with a message that explains how to
  install it, or asks you to upload the drawing as DXF.

.. important::
   LibreDWG is distributed under the GPL. The module never links to it and never ships it: it only
   runs ``dwgread`` as a separate program in a temporary folder. Install it yourself on the Odoo
   server.

Install LibreDWG for DWG files
------------------------------

**Docker** (Debian or Ubuntu based image): add the following to the Dockerfile of your Odoo image.

.. code-block:: dockerfile

   RUN apt-get update && apt-get install -y --no-install-recommends build-essential curl xz-utils \
       && curl -L https://ftp.gnu.org/gnu/libredwg/libredwg-0.13.3.tar.xz | tar xJ -C /tmp \
       && cd /tmp/libredwg-0.13.3 && ./configure --prefix=/opt/libredwg --disable-bindings \
       && make -j"$(nproc)" && make install && rm -rf /tmp/libredwg-0.13.3

``dwgread`` is then found at ``/opt/libredwg/bin/dwgread``. When the module runs it, it sets
``LD_LIBRARY_PATH`` to ``/opt/libredwg/lib``.

**macOS**: run ``brew install libredwg``. ``dwgread`` is then on the ``PATH``. If you installed it
elsewhere, enter the path in the settings.

The module looks for the converter in this order: the path in the setting :guilabel:`DWG converter`,
``dwgread`` on the ``PATH``, and ``/opt/libredwg/bin/dwgread``. The setting :guilabel:`Converter in
use` shows which program was found. A DWG is converted once per parse (time limit 180 seconds).

Settings
========

Open :menuselection:`Manufacturing app --> Configuration --> Settings` and scroll to the block
:guilabel:`CAD BoM import`.

.. list-table::
   :header-rows: 1
   :widths: 30 15 55

   * - Setting
     - Default
     - What it does
   * - :guilabel:`DWG converter`
     - empty
     - Path of the ``dwgread`` program. Empty: it is searched on the ``PATH`` and in
       ``/opt/libredwg/bin``. :guilabel:`Converter in use` shows the result.
   * - :guilabel:`Manufacturing price per kg`
     - 2.5
     - Default manufacturing price of the quotation, in euro per kg. It can be changed on every
       quotation.
   * - :guilabel:`Assembly price per kg`
     - 0.8
     - Default assembly price of the quotation, in euro per kg.
   * - :guilabel:`Manufacturing product` and :guilabel:`Assembly product`
     - *Steel structure manufacturing* and *Steel structure assembly*
     - The service products (unit of measure kg) used on the quotation lines. You can replace them.
   * - :guilabel:`Default material grade`
     - empty (S235JR)
     - Grade of the lines when neither the line nor the drawing notes name one.
   * - :guilabel:`Default bolt property class`
     - 8.8
     - Property class of the bolts when the drawing does not say.
   * - :guilabel:`Plates in`
     - Kilograms
     - Plates are bought in :guilabel:`Kilograms (one product per thickness)` or in
       :guilabel:`Pieces (one product per plate size)`.
   * - :guilabel:`Stock length of profiles (m)`, :guilabel:`Stock length of tubes (m)`,
       :guilabel:`Stock length of purlins (m)` and :guilabel:`Stock length of bars (m)`
     - 12, 6, 12 and 6
     - Length of the bars you buy. It is used when the product has no packaging such as "Bar 6 m"
       (see :ref:`the procurement list <manufacturing/cad_bom_import/procurement>`).
   * - :guilabel:`Cutting waste (%)`
     - 5
     - Waste added when the number of bars is calculated.
   * - :guilabel:`Create the BoM when the quotation is confirmed`
     - on
     - Creates the bill of materials as soon as the customer's quotation is confirmed.
   * - :guilabel:`Block attribute tags`
     - empty
     - Extra tag mapping for drawings whose blocks use their own attribute names, for example
       ``POSNR=mark, ANZ=quantity, PROF=profile, LG=length``. The roles are mark, quantity,
       profile, material, length, width, thickness, weight and description.
   * - :guilabel:`Plate mark prefixes`
     - PM, PL, P, PB, PC, PI, PS, T, TB, TP, LEMEZ, PLACA, TABLA, BL, CH, GUS
     - A mark that starts with one of these letters is a plate when its size has no family, for
       example "PM 2 / 300x300x10".

The same block has a shortcut to the steel section catalogue (see :doc:`drawings`).

Master data the import relies on
================================

- **Materials.** Every line has a material grade. Grades are records of the material master
  (:menuselection:`Products --> Configuration --> Materials`), looked up by code, name and
  aliases, and their density drives the weights. The standard data contains the EN 10025-2
  qualities S235JR, S235J0, S235J2, S275JR, S275J0, S275J2, S355JR, S355J0, S355J2 and S355K2, and
  also S460, 1.4301, 1.4404, EN AW-6060 and EN AW-6082. A grade written on a drawing matches its exact
  quality, and old designations such as OL37, St37-2 or Fe360 are aliases of S235JR. See
  :ref:`inventory/product_data/material`.
- **Product dimensions.** Products created by the import carry their shape, dimensions and
  cross-section area, so that their weight follows the material density. See
  :ref:`inventory/product_data/dimensions`.
- **Packaging.** If you buy a product in fixed bar lengths, add a packaging such as "Bar 6 m" with
  a quantity of 6 to the product. The procurement list and the request for quotation then use it.

Access rights
=============

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Group
     - Can
   * - *Manufacturing / User*
     - Create and edit imports, lines, summaries and procurement lists, use the wizards, read the
       steel section catalogue and read and write the product aliases. Imports cannot be deleted.
   * - *Manufacturing / Administrator*
     - Everything, including deleting imports, creating bills of materials, and editing the steel
       section catalogue and the CAD product aliases.
   * - *Sales* users
     - Read the import linked on a quotation.

The imports are separated by company.

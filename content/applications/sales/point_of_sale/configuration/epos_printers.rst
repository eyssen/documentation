=============
ePOS printers
=============

ePOS printers are designed to work seamlessly with Point of Sale systems. Once connected, these
devices automatically share information, allowing for direct printing of tickets from the POS system
to the ePOS printer.

Configuration
=============

To use an ePos printer in Point of Sale:

#. :ref:`Access the POS settings <configuration/settings>`.
#. Activate the :guilabel:`ePos Printer` feature.
#. Fill in the field with your ePos IP address.

.. screenshot:: pos-epos-printers-setting
   :menu: Point of Sale ‣ Configuration ‣ Settings
   :shows: The "Connected Devices" section of the POS settings with the "ePos Printer" option enabled and the printer's IP address entered below it.
   :highlight: The "ePos Printer" setting block (red frame).
   :data: IP address 192.168.1.25.
   :module: point_of_sale, pos_epson_printer
   :notes: English UI, light theme, 1440px width, crop to the settings block.

.. note::
   When the printer connects to a network, it automatically prints a ticket with its IP address.

Directly supported ePOS printers
================================

The following ePOS printers connect directly to Odoo over the network:

- Epson TM-m30 i/ii/iii (Wi-Fi/Ethernet models only; Recommended)
- Epson TM-H6000IV-DT (Receipt printer only)
- Epson TM-T70II-DT
- Epson TM-T88V-DT
- Epson TM-L90-i
- Epson TM-T70-i
- Epson TM-T82II-i
- Epson TM-T83II-i
- Epson TM-U220-i
- Epson TM-m10
- Epson TM-P20 (Wi-Fi® model)
- Epson TM-P60II (Receipt: Wi-Fi® model)
- Epson TM-P60II (Peeler: Wi-Fi® model)
- Epson TM-P80 (Wi-Fi® model)

.. important::
   - Epson printers using Wi-Fi/Ethernet connections and following the `EPOS SDK Javascript protocol
     <https://download4.epson.biz/sec_pubs/pos/reference_en/technology/epson_epos_sdk.html>`_ are
     compatible with Odoo.
   - Epson printers that connect only over USB or Bluetooth, and thermal printers that use the
     ESC/POS protocol, are **not compatible**.
   - The Epson TM-T20, TM-T88, and TM-U220 families ship with ePOS software that is not compatible
     with Odoo.

.. seealso::
   - :doc:`https`
   - :doc:`epos_ssc`

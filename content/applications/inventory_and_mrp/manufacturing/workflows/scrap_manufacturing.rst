==========================
Scrap during manufacturing
==========================

.. |MO| replace:: :abbr:`MO (Manufacturing Order)`

During the manufacturing process, scrapping components or finished products may be necessary when
items are damaged, defective, or no longer usable.

Tracking scrapped materials helps manufacturers monitor waste, identify process issues, and account
for production costs.

In Odoo, scrapped items are removed from physical inventory and moved to a virtual location called
*Virtual Locations/Scrap*. This location is not a physical space—it is a way to log and track losses
without affecting real stock levels.

.. seealso::
   :doc:`Location types <../../inventory/warehouses_storage/inventory_management>`

.. tip::
   Scrap orders can be viewed by navigating to :menuselection:`Inventory --> Operations --> Scrap`.
   Each scrap order shows the date and time the order was created, along with the product and
   quantity that was scrapped.

   To view the total quantity of each item scrapped, navigate to :menuselection:`Inventory -->
   Configuration --> Locations`, then remove the :guilabel:`Internal` filter from the
   :guilabel:`Search...` bar to display all virtual locations. From the list, select the
   :guilabel:`Virtual Locations/Scrap` location.

.. _manufacturing/management/scrap-window:

Navigate to the scrap window
============================

Scrapping can be done directly from a manufacturing order in the **Manufacturing** app:

- Components can be scrapped as long as the |MO| has not been fully produced (:guilabel:`Draft`,
  :guilabel:`Confirmed`, or :guilabel:`In Progress` stage).
- Finished products can be scrapped once the |MO| is in the *Done* stage.

To scrap a product from the **Manufacturing** app, go to :menuselection:`Manufacturing -->
Operations --> Manufacturing Orders` and select the desired |MO|.

On the |MO|, click the :icon:`fa-cog` :guilabel:`(Actions)` icon, then choose :guilabel:`Scrap` from
the drop-down menu.

.. screenshot:: manufacturing-scrap-cog-menu
   :menu: Manufacturing app --> Operations --> Manufacturing Orders (open an MO)
   :shows: The MO form, cog/"Actions" drop-down menu open, "Scrap" option visible in the list.
   :highlight: The "Scrap" menu option.
   :data: Demo company "YourCompany"; confirmed MO.
   :module: mrp
   :notes: English UI, light theme, 1440px width.

Scrap pop-up window
===================

After opening the :guilabel:`Scrap Products` pop-up window as :ref:`detailed above
<manufacturing/management/scrap-window>`, select the component or finished product being scrapped,
from the :guilabel:`Product` drop-down menu.

In the :guilabel:`Quantity` field, enter the quantity being scrapped.

By default, the :guilabel:`Source Location` field is set to the warehouse's pre-production location,
while the :guilabel:`Scrap Location` field is set to the :guilabel:`Virtual Locations/Scrap`
location. If either the source or scrap location should be changed, select a different location from
their respective drop-down menus.

Enable the :guilabel:`Replenish Scrapped Quantities` checkbox if a picking order should be created
to replace the scrapped component upon confirmation of the scrap order. This option should only be
enabled for warehouses with :doc:`two-step <../basic_setup/two_step_manufacturing>` or
:doc:`three-step <../basic_setup/three_step_manufacturing>` manufacturing enabled, since components
are not picked as part of the :doc:`one-step <../basic_setup/one_step_manufacturing>` manufacturing
process.

.. screenshot:: manufacturing-scrap-window
   :menu: Manufacturing app --> Operations --> Manufacturing Orders (open an MO) --> Actions -->
      Scrap
   :shows: The "Scrap Products" pop-up window with "Product", "Quantity", "Source Location",
      "Scrap Location" fields filled in, and the "Replenish Scrapped Quantities" checkbox visible.
   :highlight: The "Replenish Scrapped Quantities" checkbox.
   :data: Demo company "YourCompany"; component scrapped from a two-step manufacturing MO.
   :module: mrp, stock
   :notes: English UI, light theme, 1440px width.

After filling out the :guilabel:`Scrap Products` pop-up window, click the :guilabel:`Scrap Products`
button. After one or more scrap orders have been created, a :guilabel:`Scraps` smart button appears
at the top of the screen. Click it to view a list of all scrap orders for the |MO|.

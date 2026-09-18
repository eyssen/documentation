==========
PoS groups
==========

When several points of sale share the same look and the same product range — a chain of shops, or
several registers in one store — the *PoS Grouping* module (`eyssen_pos_group`) lets you maintain
those settings once, on a **PoS group**, and apply them to every point of sale of the group.

Configuration
=============

Create a group
--------------

#. Go to :menuselection:`Point of Sale --> Configuration --> Groups` and click :guilabel:`New`.
#. Enter a :guilabel:`PoS Group Name`.
#. Fill in the :guilabel:`Base Settings`:

   - :guilabel:`PoSes`: the points of sale that belong to the group. Only points of sale that are
     not yet assigned to another group can be selected.
   - :guilabel:`Managers`: the users responsible for the group.
   - :guilabel:`Description`: a free description of the group.
#. Fill in the :guilabel:`Appearances` settings, which mirror the
   :ref:`POS logo and screen saver <pos/configuration/logo>` settings: :guilabel:`Logo Option`,
   :guilabel:`Screen Saver Background`, and the :guilabel:`Receipt Design` (see
   :ref:`receipts-invoices/receipt-designs`).
#. On the :guilabel:`Product Restriction` tab, define what the points of sale of the group may sell:

   - :guilabel:`PoS Product Categories`: enable :guilabel:`Restrict Categories` and list the
     :guilabel:`Available PoS Product Categories`.
   - :guilabel:`Product Categories`: enable :guilabel:`Restrict Product Categories` and list the
     :guilabel:`Available Product Categories`. Keep :guilabel:`Include Product Category
     Descendants` enabled to also allow the child categories.
   - :guilabel:`Product Tags`: enable :guilabel:`Restrict Product Tags` and list the
     :guilabel:`Available Product Tags`.

   These fields work exactly like the per-POS settings described in
   :ref:`pos/configuration/restrict-products`.
#. A :guilabel:`Sales Team` can be linked to the group, so the orders of its points of sale are
   attributed to that team.

.. screenshot:: pos-groups-form
   :menu: Point of Sale ‣ Configuration ‣ Groups ‣ New
   :shows: A PoS group form with the group name, the "Base Settings" and "Appearances" groups filled
      in, and the "Product Restriction" tab visible below.
   :data: Group "Premium Stores" with two points of sale and a custom logo.
   :module: eyssen_pos_group
   :notes: English UI, light theme, 1440px width.

Assign a point of sale to a group
---------------------------------

A point of sale is added to a group either from the group's :guilabel:`PoSes` field or from the
:ref:`POS settings <configuration/settings>`, in the :guilabel:`PoS Group` section, using the
:guilabel:`PoS Group` field. The field is locked while a POS session is open.

The group is also shown on the POS list, kanban, and search views, where the points of sale can be
grouped by :guilabel:`PoS Group`.

Group operation mode
====================

Every setting managed by the group can either follow the group or be overridden for one point of
sale. Once a POS belongs to a group, a :guilabel:`Group Operation Mode` selector appears next to
each of those settings in the POS settings:

- :guilabel:`Based on Group`: the value is copied from the group and is refreshed whenever the group
  changes. This is the default.
- :guilabel:`Forced set Values`: the point of sale keeps its own value, and the group no longer
  overwrites it.

The selector is available for the sales team, the logo and screen saver, the PoS product category
restriction, the product category restriction, and the product tag restriction.

.. screenshot:: pos-groups-operation-mode
   :menu: Point of Sale ‣ Configuration ‣ Settings
   :shows: A POS setting managed by a group, with the warning box below it showing the "Group
      Operation Mode" selector set to "Based on Group".
   :highlight: The "Group Operation Mode" selector (red frame).
   :module: eyssen_pos_group
   :notes: English UI, light theme, 1440px width, crop to the setting block.

.. important::
   Changing a value on the group immediately updates every point of sale of the group whose
   operation mode is :guilabel:`Based on Group`. Set the mode to :guilabel:`Forced set Values`
   *before* changing the group if one of the points of sale must keep a different value.

.. note::
   The :guilabel:`Receipt Design` of the group is not yet propagated to the points of sale; set it
   on each point of sale as described in :ref:`receipts-invoices/receipt-designs`.

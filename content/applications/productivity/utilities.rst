=========
Utilities
=========

Small tools that are available across the database.

Calculator
==========

A calculator is available from the systray, at the top right of any backend screen. Click the
:icon:`fa-calculator` :guilabel:`(calculator)` icon to open it, perform the calculation with the
number and operator buttons, and drag the calculator by its body to move it out of the way. It stays
open while working in another screen.

.. note::
   Requires the *Odoo Calculator* (``odoo_calculator_tool``) module.

.. screenshot:: productivity-utilities-calculator
   :menu: (any backend view)
   :shows: The calculator opened from the systray icon, floating over a backend view, with a calculation in its display.
   :highlight: The systray calculator icon (red frame).
   :module: odoo_calculator_tool
   :notes: English UI, light theme, crop to the systray and the calculator.

Gantt view
==========

The *Web Gantt* (``web_gantt``) module adds a Gantt view type: on models that have a start and a
stop date, records are displayed as bars on a timeline, which can be zoomed and scrolled. Where the
view is available, it appears in the view switcher of the model, next to the list and kanban views,
and it can also be added to :doc:`My Dashboard <dashboards/my_dashboard>`.

.. note::
   The Gantt view has to be declared on a model; it is not automatically available everywhere.

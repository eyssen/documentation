===================
eYssen ERP settings
===================

The *eYssen ERP Base* module (`eyssen_base`) is the foundation of all eYssen modules. It adds the
:guilabel:`eYssen ERP` page to the general settings, from which the eYssen features are switched on
and off, application by application.

Go to :menuselection:`Settings --> eYssen ERP`. Each option of the page corresponds to a module:

- ticking an option and clicking :guilabel:`Save` **installs** the module, together with the modules
  it depends on;
- unticking an option and clicking :guilabel:`Save` **uninstalls** the module, after a confirmation.

.. warning::
   Uninstalling a module deletes the data stored in the fields and the records that the module
   added. Untick an option only after checking with your system administrator that the data is no
   longer needed.

Some options have sub-options, displayed under the main option (e.g., :guilabel:`Account` and
:guilabel:`PoS` under :guilabel:`Access Management`). They install a bridge between the feature and
another application, and require that application to be installed.

Once a module is installed, its own settings, if any, appear directly under its option on the same
page (e.g., :guilabel:`Create Automatically` under the :guilabel:`Process Number` options), or in
the settings of the related application.

.. note::
   - Only users with the :guilabel:`Administration: Settings` access right can open the page.
   - The labels of this page are only available in English.
   - Do not enable in a production database the options whose description reads *Under
     development. Don't use it yet!*
   - The same modules can also be installed from the :doc:`Apps <apps_modules>` dashboard.

.. screenshot:: general-eyssen-erp-settings-page
   :menu: Settings ‣ eYssen ERP
   :shows: The eYssen ERP settings page with the "eYssen ERP" entry selected in the left-hand application list, and the "General Modules" and "Process Number" sections with several options ticked.
   :highlight: The "eYssen ERP" entry of the left-hand list (red frame).
   :module: eyssen_base
   :notes: English UI, light theme, 1440px width.

.. _eyssen-erp-settings/options:

Available options
=================

The tables below list the options of each section of the page, the technical name of the module
they install, and the documentation page describing the feature.

General Modules
---------------

Features that are not tied to one application: interface, access control, documents, signature, and chatter.

.. list-table::
   :header-rows: 1
   :widths: 45 30 25

   * - Option
     - Module
     - Documentation
   * - :guilabel:`eYssen ERP Backend Theme`
     - `eyssen_backend_theme`
     - :doc:`backend_interface`
   * - :guilabel:`eYssen Cloud Token Login`
     - `eyssen_cloud_token_login`
     - :ref:`Below <eyssen-erp-settings/token-login>`
   * - :guilabel:`Document Management`
     - `eyssen_document_management`
     - :doc:`../productivity/documents`
   * - :guilabel:`Access Management`
     - `eyssen_access_management`
     - :doc:`users/access_management`
   * - :guilabel:`Access Management` ‣ :guilabel:`Account`
     - `eyssen_access_management_account`
     - :doc:`users/access_management`
   * - :guilabel:`Access Management` ‣ :guilabel:`PoS`
     - `eyssen_access_management_pos`
     - :doc:`../sales/point_of_sale/configuration`
   * - :guilabel:`Dashboard`
     - `dashboard`
     - :doc:`../productivity/dashboards/custom_dashboards`
   * - :guilabel:`eYssen Electronic Signature`
     - `eyssen_esign`
     - :doc:`../productivity/sign`
   * - :guilabel:`Mail Follower Notification`
     - `eyssen_mail_follower_notification`
     - :doc:`../productivity/discuss/chatter`
   * - :guilabel:`Mail Follower Notification` ‣ :guilabel:`Invoicing`
     - `eyssen_mail_follower_notification_account`
     - :doc:`../productivity/discuss/chatter`
   * - :guilabel:`Chatter: Log Archive/Restore (no duplicate with tracking)`
     - `eyssen_chatter_log_all_state_chnage`
     - :doc:`../productivity/discuss/chatter`
   * - :guilabel:`Data Audit`
     - `eyssen_data_audit`
     - :doc:`data_audit`

Process Number
--------------

Case identifiers shared by the documents of several applications.

.. list-table::
   :header-rows: 1
   :widths: 45 30 25

   * - Option
     - Module
     - Documentation
   * - :guilabel:`Process Number`
     - `process_number`
     - :doc:`process_numbers`
   * - :guilabel:`Process Number` ‣ :guilabel:`CRM`
     - `process_number_crm`
     - :doc:`process_numbers`
   * - :guilabel:`Process Number` ‣ :guilabel:`Sale`
     - `process_number_sale`
     - :doc:`../sales/sales/order_extensions`
   * - :guilabel:`Process Number` ‣ :guilabel:`Purchase`
     - `process_number_purchase`
     - :doc:`../inventory_and_mrp/purchase/manage_deals/rfq`
   * - :guilabel:`Process Number` ‣ :guilabel:`Stock`
     - `process_number_stock`
     - :doc:`../inventory_and_mrp/inventory/product_management/stock_helpers`
   * - :guilabel:`Process Number` ‣ :guilabel:`Invoicing`
     - `process_number_account`
     - :doc:`process_numbers`
   * - :guilabel:`Process Number` ‣ :guilabel:`Project`
     - `process_number_project`
     - :doc:`../services/project/process_numbers`

Partner
-------

Extensions of the contacts.

.. list-table::
   :header-rows: 1
   :widths: 45 30 25

   * - Option
     - Module
     - Documentation
   * - :guilabel:`Partner Extension`
     - `eyssen_partner`
     - :doc:`../sales/crm/optimize/contact_data`

Product
-------

Extensions of the products, price lists, attributes, and barcodes.

.. list-table::
   :header-rows: 1
   :widths: 45 30 25

   * - Option
     - Module
     - Documentation
   * - :guilabel:`Product Management`
     - `eyssen_product`
     - :doc:`../inventory_and_mrp/inventory/product_management/product_data`
   * - :guilabel:`Product Stages`
     - `eyssen_product_stage`
     - :doc:`../inventory_and_mrp/inventory/product_management/product_data`
   * - :guilabel:`Show Pricelist Price on Product`
     - `eyssen_product_show_pricelist_price`
     - :doc:`../inventory_and_mrp/inventory/product_management/pricing_extensions`
   * - :guilabel:`Price List Validation by Tags`
     - `eyssen_product_pricelist_tag`
     - :doc:`../inventory_and_mrp/inventory/product_management/pricing_extensions`
   * - :guilabel:`Price List Validation by Tags` ‣ :guilabel:`Price List Validation by Tags - WS Ribbon`
     - `eyssen_product_pricelist_tag_ribbon`
     - :doc:`../inventory_and_mrp/inventory/product_management/pricing_extensions`
   * - :guilabel:`Price List Rule Sequence`
     - `eyssen_product_pricelist_sequence`
     - :doc:`../inventory_and_mrp/inventory/product_management/pricing_extensions`
   * - :guilabel:`Product Reference Functions`
     - `eyssen_product_default_code`
     - :doc:`../inventory_and_mrp/inventory/product_management/product_data`
   * - :guilabel:`Barcode Generator`
     - `eyssen_product_barcode`
     - :doc:`../inventory_and_mrp/inventory/product_management/labels`
   * - :guilabel:`Barcode App Base`
     - `eyssen_barcode_app`
     - :doc:`../inventory_and_mrp/barcode/operations/product_lookup`
   * - :guilabel:`Bulk Update`
     - `eyssen_product_bulk_update`
     - :doc:`../inventory_and_mrp/inventory/product_management/bulk_editing`
   * - :guilabel:`Bulk Update` ‣ :guilabel:`Bulk Update - Website Sale`
     - `eyssen_product_bulk_update_ws`
     - :doc:`../inventory_and_mrp/inventory/product_management/bulk_editing`
   * - :guilabel:`Advnaced UoM`
     - `eyssen_uom`
     - :doc:`../inventory_and_mrp/inventory/product_management/configure/uom`
   * - :guilabel:`Dimensions`
     - `eyssen_product_dimension`
     - :doc:`../inventory_and_mrp/inventory/product_management/product_data`
   * - :guilabel:`Pricelist Import`
     - `eyssen_pricelist_import`
     - :doc:`../inventory_and_mrp/inventory/product_management/pricing_extensions`
   * - :guilabel:`Pricelist Price Pair`
     - `eyssen_pricelist_price_pair`
     - :doc:`../inventory_and_mrp/inventory/product_management/pricing_extensions`
   * - :guilabel:`Custom Product Label`
     - `eyssen_product_custom_label`
     - :doc:`../inventory_and_mrp/inventory/product_management/labels`
   * - :guilabel:`Attribute Management`
     - `eyssen_product_attribute`
     - :doc:`../inventory_and_mrp/inventory/product_management/product_attributes`
   * - :guilabel:`Attribute Management` ‣ :guilabel:`Attribute Management - Website Sale`
     - `eyssen_product_attribute_ws`
     - :doc:`../inventory_and_mrp/inventory/product_management/product_attributes`
   * - :guilabel:`Attribute Collection`
     - `eyssen_product_attribute_collection`
     - :doc:`../inventory_and_mrp/inventory/product_management/product_attributes`
   * - :guilabel:`Product Material`
     - `eyssen_product_material`
     - :doc:`../inventory_and_mrp/inventory/product_management/product_data`
   * - :guilabel:`Season Management`
     - `eyssen_product_season`
     - :doc:`../inventory_and_mrp/inventory/product_management/product_data`
   * - :guilabel:`Product Image In List View`
     - `eyssen_product_list_view_image`
     - :doc:`../inventory_and_mrp/inventory/product_management/product_data`
   * - :guilabel:`Product Catalog`
     - `eyssen_product_catalog`
     - :doc:`../inventory_and_mrp/inventory/warehouses_storage/inventory_management/product_catalog`

Sale
----

Extensions of the Sales application.

.. list-table::
   :header-rows: 1
   :widths: 45 30 25

   * - Option
     - Module
     - Documentation
   * - :guilabel:`Sale Price Calculator`
     - `eyssen_sale_price_calculator`
     - :doc:`../sales/sales/order_extensions`
   * - :guilabel:`Sale Multiple Warehouse`
     - `eyssen_sale_multiple_warehouse`
     - :doc:`../sales/sales/order_extensions`
   * - :guilabel:`Versioning`
     - `eyssen_sale_version`
     - :doc:`../sales/sales/order_extensions`
   * - :guilabel:`Sale Quantity Limitation`
     - `eyssen_sale_quantity_limit`
     - :doc:`../sales/sales/order_extensions`
   * - :guilabel:`Sale Quantity Limitation` ‣ :guilabel:`Sale Quantity Limitation - Website Sale`
     - `eyssen_sale_quantity_limit_ws`
     - :doc:`../sales/sales/order_extensions`
   * - :guilabel:`Add Bulk Products for Sale`
     - `eyssen_product_bulk_add_sale`
     - :doc:`../inventory_and_mrp/inventory/product_management/bulk_editing`
   * - :guilabel:`Add Products to Sale Order with Barcode Scanner`
     - `eyssen_barcode_sale`
     - :doc:`../inventory_and_mrp/barcode/operations/scan_on_orders`
   * - :guilabel:`Add item from previous sale`
     - `eyssen_add_item_from_previous_sale`
     - :doc:`../sales/sales/order_extensions`
   * - :guilabel:`Delivery Status`
     - `eyssen_sale_delivery_status`
     - :doc:`../inventory_and_mrp/inventory/shipping_receiving/delivery_status_and_dates`
   * - :guilabel:`Delivery Status` ‣ :guilabel:`Website Portal`
     - `sale_delivery_status_ws`
     - :doc:`../inventory_and_mrp/inventory/shipping_receiving/delivery_status_and_dates`
   * - :guilabel:`Sale Out of Stock Ordering (Preorder, Backorder)`
     - `eyssen_sale_out_of_stock`
     - :doc:`../inventory_and_mrp/inventory/product_management/out_of_stock_ordering`

CRM
---

Extensions of the CRM application.

.. list-table::
   :header-rows: 1
   :widths: 45 30 25

   * - Option
     - Module
     - Documentation
   * - :guilabel:`Multi Currency`
     - `eyssen_crm_multi_currency`
     - :doc:`../sales/crm/pipeline/multi_currency`

Subscription
------------

Recurring sales and automatic invoicing.

.. list-table::
   :header-rows: 1
   :widths: 45 30 25

   * - Option
     - Module
     - Documentation
   * - :guilabel:`Subscription Management`
     - `subscription`
     - :doc:`../sales/subscriptions`

Purchase
--------

Extensions of the Purchase application.

.. list-table::
   :header-rows: 1
   :widths: 45 30 25

   * - Option
     - Module
     - Documentation
   * - :guilabel:`Supplier Product Management`
     - `eyssen_supplier_product_management`
     - :doc:`../inventory_and_mrp/inventory/product_management/supplier_products`
   * - :guilabel:`Supplier Product Management` ‣ :guilabel:`Vision Software API`
     - `eyssen_vision_software_api`
     - —
   * - :guilabel:`Supplier Color Code`
     - `supplier_color_code`
     - :doc:`../inventory_and_mrp/inventory/product_management/product_attributes`
   * - :guilabel:`Add Bulk Products for Purchase`
     - `eyssen_product_bulk_add_purchase`
     - :doc:`../inventory_and_mrp/inventory/product_management/bulk_editing`
   * - :guilabel:`Add Products to Purchase with Barcode Scanner`
     - `eyssen_barcode_purchase`
     - :doc:`../inventory_and_mrp/barcode/operations/scan_on_orders`
   * - :guilabel:`Add item from previous purchase`
     - `eyssen_add_item_from_previous_purchase`
     - :doc:`../inventory_and_mrp/purchase/manage_deals/rfq`

Stock
-----

Extensions of the Inventory application, including the shipping connectors.

.. list-table::
   :header-rows: 1
   :widths: 45 30 25

   * - Option
     - Module
     - Documentation
   * - :guilabel:`Warehouse More Features`
     - `eyssen_stock`
     - :doc:`../inventory_and_mrp/inventory/warehouses_storage/stock_control`
   * - :guilabel:`Deliveryslip More Features`
     - `eyssen_stock_deliveryslip`
     - :doc:`../inventory_and_mrp/inventory/shipping_receiving/delivery_slips`
   * - :guilabel:`Deliveryslip SO Info`
     - `eyssen_stock_deliveryslip_so_info`
     - :doc:`../inventory_and_mrp/inventory/shipping_receiving/delivery_slips`
   * - :guilabel:`Priced Delivery Note`
     - `eyssen_stock_priced_delivery_note`
     - :doc:`../inventory_and_mrp/inventory/shipping_receiving/delivery_slips`
   * - :guilabel:`Invoiceing from Picking`
     - `eyssen_stock_picking_invoice`
     - :doc:`../finance/accounting/customer_invoices/invoice_from_delivery_notes`
   * - :guilabel:`Disallow Negative Stock`
     - `eyssen_stock_disallow_negative_stock`
     - :doc:`../inventory_and_mrp/inventory/warehouses_storage/stock_control`
   * - :guilabel:`Calculate Warehouse Stock`
     - `eyssen_stock_calculate_wh_stock`
     - —
   * - :guilabel:`Advanced Stock`
     - `eyssen_stock_advanced_stock`
     - :doc:`../inventory_and_mrp/inventory/warehouses_storage/stock_control`
   * - :guilabel:`Size & Load Management`
     - `eyssen_stock_load`
     - :doc:`../inventory_and_mrp/inventory/warehouses_storage/stock_control`
   * - :guilabel:`Location Searchpanel`
     - `eyssen_stock_location_searchpanel`
     - :doc:`../inventory_and_mrp/inventory/warehouses_storage/locations_and_picking`
   * - :guilabel:`Disable Remaining quantities not yet delivered section on Delivery Slip`
     - `eyssen_stock_disable_remaining_quantities_on_ds`
     - :doc:`../inventory_and_mrp/inventory/shipping_receiving/delivery_slips`
   * - :guilabel:`Add Bulk Products for Stock`
     - `eyssen_product_bulk_add_stock`
     - :doc:`../inventory_and_mrp/inventory/product_management/stock_helpers`
   * - :guilabel:`Add Products to Stock with Barcode Scanner`
     - `eyssen_barcode_stock`
     - :doc:`../inventory_and_mrp/inventory/product_management/stock_helpers`
   * - :guilabel:`Delivery Payment`
     - `eyssen_delivery_payment`
     - :doc:`../inventory_and_mrp/inventory/shipping_receiving/delivery_payment`
   * - :guilabel:`Delivery Payment` ‣ :guilabel:`GLS Shipping Provider`
     - `eyssen_delivery_gls`
     - :doc:`../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/gls`
   * - :guilabel:`Delivery Payment` ‣ :guilabel:`Foxpost Shipping Provider`
     - `eyssen_delivery_foxpost`
     - :doc:`../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/foxpost`
   * - :guilabel:`Delivery Payment` ‣ :guilabel:`MPL (Magyar Posta) Shipping Provider`
     - `eyssen_delivery_mpl`
     - :doc:`../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/mpl`
   * - :guilabel:`Multiple Warehouse`
     - `eyssen_stock_multi_warehouse`
     - :doc:`../inventory_and_mrp/inventory/warehouses_storage/multi_warehouse`
   * - :guilabel:`Add item from previous picking`
     - `eyssen_add_item_from_previous_stock`
     - :doc:`../inventory_and_mrp/inventory/product_management/stock_helpers`
   * - :guilabel:`Stock Removal Priority`
     - `eyssen_stock_removal_priority`
     - :doc:`../inventory_and_mrp/inventory/warehouses_storage/locations_and_picking`

Invoicing
---------

Extensions of customer invoices and vendor bills, including the Hungarian invoicing features.

.. list-table::
   :header-rows: 1
   :widths: 45 30 25

   * - Option
     - Module
     - Documentation
   * - :guilabel:`Hungarian Invoicing`
     - `eyssen_l10n_hu`
     - :doc:`../finance/fiscal_localizations/hungary`
   * - :guilabel:`Hungarian Pro-Forma Invoicing`
     - `eyssen_l10n_hu_proforma`
     - :doc:`../finance/fiscal_localizations/hungary/proforma`
   * - :guilabel:`Hungarian KVTD`
     - `eyssen_l10n_hu_kvtd`
     - :doc:`../finance/fiscal_localizations/hungary/kvtd`
   * - :guilabel:`Copying Invoice rows values`
     - `eyssen_copy_invoice_row_value`
     - :doc:`../finance/accounting/customer_invoices`
   * - :guilabel:`Add Bulk Products for Invoice`
     - `eyssen_product_bulk_add_invoice`
     - :doc:`../finance/accounting/customer_invoices`
   * - :guilabel:`Add Products to Invoice with Barcode Scanner`
     - `eyssen_barcode_invoice`
     - :doc:`../finance/accounting/customer_invoices`
   * - :guilabel:`Add item from previous invoice`
     - `eyssen_add_item_from_previous_invoice`
     - :doc:`../finance/accounting/customer_invoices`

Accounting
----------

Full accounting, Hungarian accounting and tax returns, bank statement imports, and exchange rates.

.. list-table::
   :header-rows: 1
   :widths: 45 30 25

   * - Option
     - Module
     - Documentation
   * - :guilabel:`Full Accounting`
     - `eyssen_accountant`
     - :doc:`../finance/accounting/bank/reconciliation`
   * - :guilabel:`Stock Accounting`
     - `eyssen_stock_accountant`
     - :doc:`../inventory_and_mrp/inventory/warehouses_storage/reporting/aging`
   * - :guilabel:`Hungarian Accounting`
     - `eyssen_l10n_hu_accountant`
     - :doc:`../finance/fiscal_localizations/hungary/vat_return`
   * - :guilabel:`Hungarian Accounting` ‣ :guilabel:`ABEV 2024`
     - `eyssen_l10n_hu_abev_24`
     - :doc:`../finance/fiscal_localizations/hungary/vat_return`
   * - :guilabel:`Hungarian Accounting` ‣ :guilabel:`ABEV 2025`
     - `eyssen_l10n_hu_abev_25`
     - :doc:`../finance/fiscal_localizations/hungary/vat_return`
   * - :guilabel:`Hungarian Accounting` ‣ :guilabel:`ABEV 2026`
     - `eyssen_l10n_hu_abev_26`
     - :doc:`../finance/fiscal_localizations/hungary/vat_return`
   * - :guilabel:`Cash Register`
     - `eyssen_cashregister`
     - :doc:`../finance/accounting/bank/cash_register`
   * - :guilabel:`Currency Rate Live`
     - `eyssen_currency_rate_live_community`
     - :doc:`../finance/accounting/get_started/multi_currency`
   * - :guilabel:`Currency Rate Live` ‣ :guilabel:`MNB (Magyar Nemzeti Bank)`
     - `eyssen_currency_rate_live_mnb_community`
     - :doc:`../finance/fiscal_localizations/hungary`
   * - :guilabel:`CIB Bank Statement Import`
     - `eyssen_account_bank_statement_import_cib`
     - :doc:`../finance/accounting/bank/statement_import`
   * - :guilabel:`CIB Bank Statement Import` ‣ :guilabel:`K&H Bank Statement Import`
     - `eyssen_account_bank_statement_import_kh`
     - :doc:`../finance/accounting/bank/statement_import`
   * - :guilabel:`CIB Bank Statement Import` ‣ :guilabel:`OTP Bank Statement Import`
     - `eyssen_account_bank_statement_import_otp`
     - :doc:`../finance/accounting/bank/statement_import`
   * - :guilabel:`CIB Bank Statement Import` ‣ :guilabel:`Raiffeisen Bank Statement Import`
     - `eyssen_account_bank_statement_import_raiffeisen`
     - :doc:`../finance/accounting/bank/statement_import`
   * - :guilabel:`CIB Bank Statement Import` ‣ :guilabel:`Wise Bank Statement Import`
     - `eyssen_account_bank_statement_import_wise`
     - :doc:`../finance/accounting/bank/statement_import`
   * - :guilabel:`Intrastat`
     - `eyssen_intrastat`
     - :doc:`../finance/accounting/reporting/intrastat`
   * - :guilabel:`Cashbook`
     - `eyssen_l10n_hu_cashbook`
     - :doc:`../finance/fiscal_localizations/hungary/cashbook`
   * - :guilabel:`Approval`
     - `account_approval`
     - :doc:`../finance/accounting/customer_invoices/invoice_approval`

Project
-------

Extensions of the Project application.

.. list-table::
   :header-rows: 1
   :widths: 45 30 25

   * - Option
     - Module
     - Documentation
   * - :guilabel:`Project Template`
     - `eyssen_project_template`
     - :doc:`../services/project/templates`
   * - :guilabel:`Project Category`
     - `eyssen_project_category`
     - :doc:`../services/project/categories`
   * - :guilabel:`Project SLA`
     - `eyssen_project_sla`
     - :doc:`../services/project/sla`
   * - :guilabel:`Project Product`
     - `eyssen_project_product`
     - :doc:`../services/field_service/product_management`
   * - :guilabel:`Project Worksheet`
     - `eyssen_project_worksheet`
     - :doc:`../services/field_service/worksheets`
   * - :guilabel:`Project Field Service`
     - `eyssen_project_fsm`
     - :doc:`../services/field_service/configuration`
   * - :guilabel:`Task Priority`
     - `eyssen_project_task_priority`
     - :doc:`../services/project/tasks/task_stages_statuses`
   * - :guilabel:`Invoice from Timesheet`
     - `eyssen_invoice_from_timesheet`
     - :doc:`../services/timesheets/services`

MRP
---

Extensions of the Manufacturing application.

.. list-table::
   :header-rows: 1
   :widths: 45 30 25

   * - Option
     - Module
     - Documentation
   * - :guilabel:`BoM on Product`
     - `eyssen_mrp_bom_on_product`
     - :doc:`../inventory_and_mrp/inventory/product_management/product_data`

Fleet
-----

Extensions of the Fleet application.

.. list-table::
   :header-rows: 1
   :widths: 45 30 25

   * - Option
     - Module
     - Documentation
   * - :guilabel:`Fleet More Features`
     - `fleet_extra`
     - :doc:`../hr/fleet/extensions`
   * - :guilabel:`Stock Management`
     - `fleet_stock`
     - :doc:`../hr/fleet/extensions`
   * - :guilabel:`Parts Management`
     - `fleet_parts`
     - :doc:`../hr/fleet/extensions`

Website Sale
------------

Extensions of the eCommerce application.

.. list-table::
   :header-rows: 1
   :widths: 45 30 25

   * - Option
     - Module
     - Documentation
   * - :guilabel:`Product Multi Website`
     - `eyssen_website_sale_product_multi_website`
     - :doc:`../websites/ecommerce/products`
   * - :guilabel:`Order Sign`
     - `website_sale_order_sign`
     - :doc:`../websites/ecommerce/checkout`
   * - :guilabel:`Payment Management`
     - `eyssen_website_sale_payment`
     - :doc:`../websites/ecommerce/payments`
   * - :guilabel:`Disable Auto Confirmation`
     - `eyssen_website_sale_disable_auto_confirm`
     - :doc:`../websites/ecommerce/order_handling`
   * - :guilabel:`Company Checkout`
     - `website_sale_company`
     - :doc:`../websites/ecommerce/checkout`
   * - :guilabel:`Árgép`
     - `eyssen_website_sale_argep`
     - :doc:`../websites/ecommerce/products`

Point of Sale
-------------

Extensions of the Point of Sale application.

.. list-table::
   :header-rows: 1
   :widths: 45 30 25

   * - Option
     - Module
     - Documentation
   * - :guilabel:`Performance Optimization`
     - `eyssen_pos_performance`
     - :doc:`../sales/point_of_sale/configuration`
   * - :guilabel:`Logo & Screen Saver`
     - `eyssen_pos_logo`
     - :doc:`../sales/point_of_sale/configuration`
   * - :guilabel:`Product Restriction`
     - `eyssen_pos_product_restriction`
     - :doc:`../sales/point_of_sale/configuration`
   * - :guilabel:`Grouping`
     - `eyssen_pos_group`
     - :doc:`../sales/point_of_sale/configuration/pos_groups`
   * - :guilabel:`Invoice`
     - `eyssen_pos_invoice`
     - :doc:`../sales/point_of_sale/receipts_invoices`
   * - :guilabel:`PoS Hungarian`
     - `eyssen_l10n_hu_pos`
     - :doc:`../finance/fiscal_localizations/hungary`

Appointment
-----------

The eYssen appointment booking application and its bridges.

.. note::
   On the settings page, this section is also titled :guilabel:`Process Number`. It is the last
   section of the page, below :guilabel:`Point of Sale`.

.. list-table::
   :header-rows: 1
   :widths: 45 30 25

   * - Option
     - Module
     - Documentation
   * - :guilabel:`Appointment`
     - `appointment`
     - :doc:`../productivity/appointments`
   * - :guilabel:`Appointment` ‣ :guilabel:`CRM`
     - `appointment_crm`
     - :doc:`../productivity/appointments/create-opps`
   * - :guilabel:`Appointment` ‣ :guilabel:`eLearning`
     - `appointment_elearning`
     - :doc:`../productivity/appointments`
   * - :guilabel:`Appointment` ‣ :guilabel:`HelpDesk`
     - `appointment_helpdesk`
     - —
   * - :guilabel:`Appointment` ‣ :guilabel:`HR`
     - `appointment_hr`
     - :doc:`../productivity/appointments`
   * - :guilabel:`Appointment` ‣ :guilabel:`Pass`
     - `appointment_pass`
     - :doc:`../productivity/appointments`
   * - :guilabel:`Appointment` ‣ :guilabel:`Payment`
     - `appointment_payment`
     - :doc:`../productivity/appointments`
   * - :guilabel:`Appointment` ‣ :guilabel:`Reports`
     - `appointment_reports`
     - :doc:`../productivity/appointments`
   * - :guilabel:`Appointment` ‣ :guilabel:`Website`
     - `appointment_website`
     - :doc:`../websites/website/appointments`

.. note::
   The options :guilabel:`Supplier Product Management` ‣ :guilabel:`Vision Software API`
   (`eyssen_vision_software_api`) and :guilabel:`Calculate Warehouse Stock`
   (`eyssen_stock_calculate_wh_stock`) refer to modules that are no longer part of eYssen ERP;
   ticking them has no effect. The Vision Software connector is now provided by the
   `spm_vision_software_api` module; see
   :doc:`../inventory_and_mrp/inventory/product_management/supplier_connectors`.

.. _eyssen-erp-settings/token-login:

eYssen Cloud token login
========================

The :guilabel:`eYssen Cloud Token Login` option of the :guilabel:`General Modules` section installs
the `eyssen_cloud_token_login` module. It lets the operator of the hosting platform open a session
in the database **as any user, without knowing the user's password**, for testing, development,
and support purposes.

The module requires the *Website* application, and has no menu and no setting in the database. The hosting platform registers a one-time
token for the chosen user, and immediately opens the dedicated login address of the database with
that token. A token can only be used once, and only during the 10 seconds following its creation.

.. important::
   Enable this option only if you agree that your hosting provider or support provider can log in on
   behalf of your users. To withdraw the permission, untick the option and click :guilabel:`Save`.

About
=====

The :guilabel:`About` section, at the bottom of the page, displays the version and the publisher of
eYssen ERP.

.. seealso::
   - :doc:`apps_modules`
   - :doc:`users/access_rights`

---
name: stock_account
summary: Inventory, Logistic, Valuation, Accounting
description: WMS Accounting module - This module makes the link between the 'stock' and 'account' modules and allows you to create accounting entries to value your stock movements. Key Features: Stock Valuation (periodical or automatic), Invoice from Picking. Dashboard / Reports for Warehouse Management includes: Stock Inventory Value at given date.
author: Odoo S.A.
version: '1.1'
depends: stock, account
external_dependencies: []
data_entities:
  - stock.quant: Stock quantity tracking
    fields: [product_id, location_id, quantity, value]
  - stock.move: Stock movement with valuation
    fields: [product_id, location_id, location_dest_id, quantity, value]
  - account.move: Accounting entries for stock valuation
    fields: [date, line_ids, state]
views:
  - xml: account_account_views.xml - Account Views
  - xml: stock_account_views.xml - Stock Account Views
  - xml: res_config_settings_views.xml - Settings Views
  - xml: report_invoice.xml - Invoice Report
  - xml: stock_quant_views.xml - Stock Quant Views
  - xml: product_views.xml - Product Views
  - xml: product_value_views.xml - Product Value Views
  - xml: stock_location_views.xml - Location Views
  - xml: stock_lot_views.xml - Lot Views
  - xml: stock_picking_views.xml - Picking Views
  - xml: stock_move_views.xml - Move Views
  - xml: wizard/stock_inventory_adjustment_name_views.xml - Inventory Adjustment Wizard
  - xml: report/account_invoice_report_view.xml - Invoice Report
  - xml: report/stock_avco_audit_report_views.xml - AVCO Audit Report
  - xml: report/stock_valuation_report.xml - Stock Valuation Report
access_rights:
  - stock.user: read,write
  - account.user: read,write
business_logic:
  - _post_init_hook: Post-init hook for valuation setup
  - compute_valuation: Compute stock valuation
  - action_stock_valued: Mark stock as valued
  - _create_valuation_entry: Create accounting entry for valuation
external_integrations:
  - account: Create journal entries for stock valuation
---
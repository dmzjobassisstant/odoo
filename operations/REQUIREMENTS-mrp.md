# Requirements: mrp

**Module:** Manufacturing
**Version:** 2.0
**Category:** Supply Chain/Manufacturing
**Author:** Odoo S.A.
**License:** LGPL-3
**Website:** https://www.odoo.com/app/manufacturing

## Dependencies
- `product`
- `stock`
- `resource`

## Hooks
- `pre_init_hook` → `_pre_init_mrp`
- `post_init_hook` → `_create_warehouse_data`
- `uninstall_hook` → `uninstall_hook`

## Models
- `ir_attachment`
- `mrp_bom`
- `mrp_production`
- `mrp_routing`
- `mrp_unbuild`
- `mrp_workcenter`
- `mrp_workorder`
- `product`
- `product_document`
- `res_company`
- `res_config_settings`
- `stock_lot`
- `stock_move`
- `stock_move_line`
- `stock_orderpoint`
- `stock_picking`
- `stock_quant`
- `stock_reference`
- `stock_replenish_mixin`
- `stock_rule`
- `stock_scrap`
- `stock_traceability`
- `stock_warehouse`

## Data Files
- `security/mrp_security.xml`
- `security/ir.model.access.csv`
- `data/digest_data.xml`
- `data/mail_templates.xml`
- `data/mrp_data.xml`
- `data/mail_message_subtype_data.xml`
- `wizard/change_production_qty_views.xml`
- `wizard/mrp_workcenter_block_view.xml`
- `wizard/stock_warn_insufficient_qty_views.xml`
- `wizard/mrp_production_backorder.xml`
- `wizard/mrp_consumption_warning_views.xml`
- `wizard/mrp_production_split.xml`
- `wizard/mrp_production_serial_numbers.xml`
- `views/mrp_views_menus.xml`
- `views/stock_move_views.xml`
- `views/mrp_workorder_views.xml`
- `views/mrp_workcenter_views.xml`
- `views/mrp_bom_views.xml`
- `views/mrp_production_views.xml`
- `views/mrp_routing_views.xml`
- `views/product_document_views.xml`
- `views/product_views.xml`
- `views/stock_orderpoint_views.xml`
- `views/stock_warehouse_views.xml`
- `views/stock_picking_views.xml`
- `views/stock_rule_views.xml`
- `views/mrp_unbuild_views.xml`
- `views/res_config_settings_views.xml`
- `views/stock_scrap_views.xml`
- `wizard/stock_replenishment_info.xml`
- `report/report_deliveryslip.xml`
- `report/mrp_report_views_main.xml`
- `report/mrp_report_bom_structure.xml`
- `report/mrp_report_mo_overview.xml`
- `report/mrp_production_templates.xml`
- `report/report_stock_reception.xml`
- `report/report_stock_rule.xml`
- `report/mrp_zebra_production_templates.xml`
- `report/mrp_workorder_templates.xml`

## Demo Files
- `data/mrp_demo.xml`

## Security
- `ir.model.access.csv`
- `mrp_security.xml`

## Views
- `mrp_bom_views.xml`
- `mrp_production_views.xml`
- `mrp_routing_views.xml`
- `mrp_unbuild_views.xml`
- `mrp_views_menus.xml`
- `mrp_workcenter_views.xml`
- `mrp_workorder_views.xml`
- `product_document_views.xml`
- `product_views.xml`
- `res_config_settings_views.xml`
- `stock_move_views.xml`
- `stock_orderpoint_views.xml`
- `stock_picking_views.xml`
- `stock_rule_views.xml`
- `stock_scrap_views.xml`
- `stock_warehouse_views.xml`

## Wizards
- `__init__.py`
- `change_production_qty.py`
- `change_production_qty_views.xml`
- `mrp_consumption_warning.py`
- `mrp_consumption_warning_views.xml`
- `mrp_production_backorder.py`
- `mrp_production_backorder.xml`
- `mrp_production_serial_numbers.py`
- `mrp_production_serial_numbers.xml`
- `mrp_production_split.py`
- `mrp_production_split.xml`
- `mrp_workcenter_block_view.xml`
- `product_replenish.py`
- `stock_label_type.py`
- `stock_replenishment_info.py`
- `stock_replenishment_info.xml`
- `stock_warn_insufficient_qty.py`
- `stock_warn_insufficient_qty_views.xml`

## Reports
- `__init__.py`
- `mrp_production_templates.xml`
- `mrp_report_bom_structure.py`
- `mrp_report_bom_structure.xml`
- `mrp_report_mo_overview.py`
- `mrp_report_mo_overview.xml`
- `mrp_report_views_main.xml`
- `mrp_workorder_templates.xml`
- `mrp_zebra_production_templates.xml`
- `report_deliveryslip.xml`
- `report_stock_reception.py`
- `report_stock_reception.xml`
- `report_stock_rule.py`
- `report_stock_rule.xml`
- `stock_forecasted.py`

## Asset Bundles
- `web.assets_backend` (1 entries)
- `web.assets_tests` (1 entries)
- `web.assets_unit_tests` (1 entries)

## Install Settings
- **Installable:** `True`
- **Auto-install:** `False`
- **Application:** `True`

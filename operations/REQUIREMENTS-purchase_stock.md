# Requirements: purchase_stock

**Module:** Purchase Stock
**Version:** 1.2
**Category:** Supply Chain/Purchase
**Author:** Odoo S.A.
**License:** LGPL-3
**Website:** N/A

## Dependencies
- `stock_account`
- `purchase`

## Hooks
- `post_init_hook` → `_create_buy_rules`

## Models
- `account_invoice`
- `account_move_line`
- `product`
- `purchase_order`
- `purchase_order_line`
- `res_company`
- `res_config_settings`
- `res_partner`
- `stock`
- `stock_move`
- `stock_reference`
- `stock_replenish_mixin`
- `stock_rule`

## Data Files
- `security/ir.model.access.csv`
- `data/purchase_stock_data.xml`
- `data/mail_templates.xml`
- `report/vendor_delay_report.xml`
- `views/purchase_views.xml`
- `views/stock_views.xml`
- `views/stock_picking_views.xml`
- `views/stock_rule_views.xml`
- `views/res_config_settings_views.xml`
- `views/res_partner_views.xml`
- `views/stock_lot_views.xml`
- `views/stock_orderpoint_views.xml`
- `views/stock_reference_views.xml`
- `views/product_views.xml`
- `report/purchase_report_views.xml`
- `report/purchase_report_templates.xml`
- `report/report_stock_rule.xml`
- `wizard/stock_replenishment_info.xml`
- `wizard/product_replenish_views.xml`

## Demo Files
- `data/purchase_stock_demo.xml`

## Security
- `ir.model.access.csv`

## Views
- `product_views.xml`
- `purchase_views.xml`
- `res_config_settings_views.xml`
- `res_partner_views.xml`
- `stock_lot_views.xml`
- `stock_orderpoint_views.xml`
- `stock_picking_views.xml`
- `stock_reference_views.xml`
- `stock_rule_views.xml`
- `stock_views.xml`

## Wizards
- `__init__.py`
- `product_replenish.py`
- `product_replenish_views.xml`
- `stock_replenishment_info.py`
- `stock_replenishment_info.xml`

## Reports
- `__init__.py`
- `purchase_report.py`
- `purchase_report_templates.xml`
- `purchase_report_views.xml`
- `report_stock_rule.py`
- `report_stock_rule.xml`
- `stock_forecasted.py`
- `stock_valuation_report.py`
- `vendor_delay_report.py`
- `vendor_delay_report.xml`

## Asset Bundles
- `web.assets_backend` (1 entries)
- `web.assets_tests` (1 entries)
- `web.assets_unit_tests` (1 entries)

## Install Settings
- **Installable:** `True`
- **Auto-install:** `True`
- **Application:** `False`

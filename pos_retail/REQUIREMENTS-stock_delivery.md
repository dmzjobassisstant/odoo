# Requirements: stock_delivery

## Module Details
- **Name:** Delivery - Stock
- **Category:** Shipping Connectors
- **Version:** 1.0
- **Author:** Odoo S.A.
- **License:** LGPL-3

## Description
Allows you to add delivery methods in pickings. When creating invoices from picking, the system is able to add and compute the shipping line.

## Dependencies
- `sale_stock`
- `delivery`

## Auto Install
- Yes

## Data Files
- `security/ir.model.access.csv`
- `views/product_template_view.xml`
- `views/delivery_view.xml`
- `views/delivery_portal_template.xml`
- `views/report_shipping.xml`
- `views/report_deliveryslip.xml`
- `views/report_package_barcode.xml`
- `wizard/choose_delivery_carrier_views.xml`
- `wizard/stock_put_in_pack_views.xml`
- `views/stock_package_type_views.xml`
- `views/stock_picking_type_views.xml`
- `views/stock_rule_views.xml`
- `views/stock_move_line_views.xml`
- `report/product_templates.xml`

## Demo Files
- `data/delivery_demo.xml`

## Hooks
- `post_init_hook`: `_auto_install_sale_app`

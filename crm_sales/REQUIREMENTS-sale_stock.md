# sale_stock Requirements

## Module Overview
- **Name**: Sales and Warehouse Management
- **Category**: Sales/Sales
- **Summary**: Quotation, Sales Orders, Delivery & Invoicing Control
- **Description**: Manage sales quotations and orders. Makes the link between sales and warehouses management applications.
- **Features**: Shipping (partial/whole delivery), Invoicing control, Incoterms
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.0

## Technical Details

### Dependencies
- `sale`
- `stock_account`
- Auto-installs: True

### Data Files
- `security/sale_stock_security.xml`
- `security/ir.model.access.csv`
- `views/sale_order_views.xml`
- `views/sale_order_line_views.xml`
- `views/stock_route_views.xml`
- `views/res_config_settings_views.xml`
- `views/sale_stock_portal_template.xml`
- `views/stock_lot_views.xml`
- `views/res_users_views.xml`
- `views/stock_picking_views.xml`
- `views/stock_reference_views.xml`
- `report/sale_order_report_templates.xml`
- `report/stock_report_deliveryslip.xml`
- `data/mail_templates.xml`
- `data/sale_stock_data.xml`
- `wizard/stock_rules_report_views.xml`

### Demo Data
- `data/sale_order_demo.xml`

### Assets
- `web.assets_backend`: All static src files
- `web.assets_tests`: Tour tests

### Installable
- True

### Models (implied by views/data)
- `sale.order` - Extended with warehouse/delivery handling
- `sale.order.line` - Extended with stock reservations
- `stock.picking` - Delivery orders linked to sales
- `stock.lot` - Lot/serial numbers for sales

# Sales and MRP Management (sale_mrp)

## Module Details

- **Name**: Sales and MRP Management
- **Version**: 1.0
- **Category**: Sales/Sales
- **Summary**: Integrates MRP with sales modules
- **Description**: This module provides facility to the user to install mrp and sales modules at a time. It is basically used when we want to keep track of production orders generated from sales order. It adds sales name and sales Reference on production order.
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Installable**: True
- **Auto Install**: True

## Dependencies

| Type | Module |
|------|--------|
| Core | mrp |
| Core | sale_stock |

## External Dependencies

None

## Security

- `security/ir.model.access.csv`

## Data Files

- `views/mrp_production_views.xml`
- `views/sale_order_views.xml`
- `views/sale_portal_templates.xml`

## Models

- `account_move.py`
- `mrp_bom.py`
- `mrp_production.py`
- `sale_order.py`
- `sale_order_line.py`
- `stock_move.py`
- `stock_move_line.py`
- `stock_rule.py`

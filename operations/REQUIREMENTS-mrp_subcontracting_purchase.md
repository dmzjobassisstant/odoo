# Requirements: mrp_subcontracting_purchase

**Module:** Purchase and Subcontracting Management
**Version:** 0.1
**Category:** Supply Chain/Purchase
**Author:** Odoo S.A.
**License:** LGPL-3
**Website:** N/A

## Description
This bridge module adds some smart buttons between Purchase and Subcontracting

## Dependencies
- `mrp_subcontracting`
- `purchase_mrp`

## Models
- `account_move_line`
- `product_product`
- `purchase_order`
- `stock_move`
- `stock_picking`
- `stock_rule`

## Data Files
- `views/purchase_order_views.xml`
- `views/stock_picking_views.xml`

## Demo Files
- `data/mrp_subcontracting_purchase_demo.xml`

## Views
- `purchase_order_views.xml`
- `stock_picking_views.xml`

## Reports
- `__init__.py`
- `mrp_report_bom_structure.py`

## Install Settings
- **Installable:** `True`
- **Auto-install:** `True`
- **Application:** `False`

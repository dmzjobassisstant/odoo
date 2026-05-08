# Requirements: stock_dropshipping

## Module Details
- **Name:** Drop Shipping
- **Category:** Supply Chain/Inventory
- **Version:** 1.0
- **Summary:** Drop Shipping
- **Author:** Odoo S.A.
- **License:** LGPL-3

## Description
Manage drop shipping orders. This module adds a pre-configured Drop Shipping operation type as well as a procurement route that allow configuring Drop Shipping products and orders. When drop shipping is used the goods are directly transferred from vendors to customers (direct delivery) without going through the retailer's warehouse.

## Dependencies
- `sale_purchase_stock`

## Data Files
- `data/stock_data.xml`
- `views/sale_order_views.xml`
- `views/stock_picking_views.xml`
- `views/purchase_order_views.xml`

## Demo Files
- `data/stock_dropshipping_demo.xml`

## Hooks
- `uninstall_hook`

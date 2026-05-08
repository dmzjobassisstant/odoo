# Requirements: mrp_subcontracting_dropshipping

**Module:** Dropship and Subcontracting Management
**Version:** 0.1
**Category:** Supply Chain/Purchase
**Author:** Odoo S.A.
**License:** LGPL-3
**Website:** N/A

## Description
This bridge module allows to manage subcontracting with the dropshipping module.

## Dependencies
- `mrp_subcontracting`
- `stock_dropshipping`

## Models
- `purchase`
- `res_company`
- `stock_move`
- `stock_orderpoint`
- `stock_picking`
- `stock_replenish_mixin`
- `stock_rule`
- `stock_warehouse`

## Data Files
- `data/mrp_subcontracting_dropshipping_data.xml`
- `views/purchase_order_views.xml`

## Views
- `purchase_order_views.xml`

## Install Settings
- **Installable:** `True`
- **Auto-install:** `True`
- **Application:** `False`

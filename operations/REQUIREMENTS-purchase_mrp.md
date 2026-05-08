# Requirements: purchase_mrp

**Module:** Purchase and MRP Management
**Version:** 1.0
**Category:** Supply Chain/Purchase
**Author:** Odoo S.A.
**License:** LGPL-3
**Website:** N/A

## Description
This module provides facility to the user to install mrp and purchase modules at a time.
========================================================================================

It is basically used when we want to keep track of production orders generated
from purchase order.

## Dependencies
- `mrp`
- `purchase_stock`

## Models
- `mrp_bom`
- `mrp_production`
- `purchase`
- `stock_move`
- `stock_rule`

## Data Files
- `views/mrp_bom_views.xml`
- `views/purchase_order_views.xml`
- `views/mrp_production_views.xml`
- `views/stock_orderpoint_views.xml`
- `security/ir.model.access.csv`

## Demo Files
- `data/purchase_mrp_demo.xml`

## Security
- `ir.model.access.csv`

## Views
- `mrp_bom_views.xml`
- `mrp_production_views.xml`
- `purchase_order_views.xml`
- `stock_orderpoint_views.xml`

## Reports
- `__init__.py`
- `mrp_report_bom_structure.py`
- `mrp_report_mo_overview.py`

## Asset Bundles
- `web.assets_backend` (1 entries)

## Install Settings
- **Installable:** `True`
- **Auto-install:** `True`
- **Application:** `False`

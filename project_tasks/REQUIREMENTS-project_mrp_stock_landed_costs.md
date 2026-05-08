# Project MRP Stock Landed Costs Module Requirements

## Module Overview
- **Name**: Project MRP Landed Costs
- **Version**: 1.0
- **Category**: Supply Chain/Manufacturing
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto-install**: True

## Dependencies
- `project_mrp_account`
- `mrp_landed_costs`

## Description
Technical bridge module connecting project_mrp_account with mrp_landed_costs.

## Models
- `stock.landed.cost` - Extended to link with project via analytic account

## Structure
- `models/`
  - `__init__.py`
  - `stock_landed_costs.py` - Links landed costs to project profitability
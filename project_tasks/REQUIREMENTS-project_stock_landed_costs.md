# Project Stock Landed Costs Module Requirements

## Module Overview
- **Name**: Project Stock Landed Costs
- **Version**: 1.0
- **Category**: Supply Chain/Inventory
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto-install**: True

## Dependencies
- `project_stock_account`
- `stock_landed_costs`

## Description
Technical bridge module connecting project_stock_account with stock_landed_costs.

## Models
- Extends `stock.landed.cost` with project profitability integration

## Structure
- `models/`
  - `__init__.py`
  - `stock_landed_costs.py`
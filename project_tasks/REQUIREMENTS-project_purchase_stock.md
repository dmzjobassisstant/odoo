# Project Purchase Stock Module Requirements

## Module Overview
- **Name**: Project - Purchase - Stock
- **Version**: 1.0
- **Category**: Services/Project
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto-install**: True

## Dependencies
- `project_purchase`
- `project_stock`

## Description
Add a project link between POs (Purchase Orders) and their generated stock pickings.

## Models
- Extends `purchase.order` with project link
- Extends `stock.rule` with project_id field

## Structure
- `models/`
  - `__init__.py`
  - `purchase_order.py`
  - `stock_rule.py`
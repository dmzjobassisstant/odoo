# Project Stock Account Module Requirements

## Module Overview
- **Name**: Project Stock Account
- **Version**: 1.0
- **Category**: Services/Project
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto-install**: True

## Dependencies
- `stock_account`
- `project_stock`

## Description
Handle analytics in Stock pickings with Project. Adds "Materials" section to project profitability.

## Models
- Extends `project.project` with stock-related profitability
- Extends `account.analytic.line` with picking applicability
- Extends `analytic.applicability` with picking rules
- Extends `stock.move` (from stock_account) with analytic account
- Extends `stock.picking.type` with analytic distribution

## Key Methods
- `_get_profitability_labels()` - Adds 'Materials' label (other_costs)
- `_get_profitability_sequence_per_invoice_type()` - Sequence (12)
- `_get_profitability_items()` - Adds picking costs to profitability
- `_get_items_from_aal_picking()` - Gets picking analytic lines

## Views
- `stock_picking_type_views.xml`
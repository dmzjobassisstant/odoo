# Project MRP Account Module Requirements

## Module Overview
- **Name**: MRP Account Project
- **Version**: 1.0
- **Category**: Services/Project
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto-install**: True

## Dependencies
- `mrp_account`
- `project_mrp`

## Description
Monitor MRP account using project. Adds Manufacturing Orders section to project profitability.

## Models
- Extends `project.project` with MRP profitability
- Extends `mrp.production` with analytic account fields
- Extends `mrp.workorder` with analytic account fields
- Extends `stock.move` (from mrp_account) with analytic account
- Extends `stock.rule` with project_link field

## Key Methods
- `_get_profitability_labels()` - Adds 'Manufacturing Orders' label
- `_get_profitability_sequence_per_invoice_type()` - Sequence for MRP (12)
- `_get_profitability_aal_domain()` - Excludes manufacturing_order category
- `_get_profitability_items()` - Adds MRP costs to profitability

## Demo Data
- `project_mrp_account_demo.xml`
# Project Account Module Requirements

## Module Overview
- **Name**: Project - Account
- **Category**: Accounting/Accounting
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto-install**: True (depends on `account` and `project`)

## Dependencies
- `account`
- `project`

## Description
Allows the computation of some section for the project profitability:
- Vendor Bills
- Other Costs
- Other Revenues

These sections are displayed in the project update view.

## Models
- Extends `project.project` with profitability computation methods

## Key Methods
- `_add_purchase_items()` - Adds vendor bills to profitability
- `_get_costs_items_from_purchase()` - Calculates costs from vendor bills
- `_get_items_from_aal()` - Gets items from analytic lines (Other Costs/Revenues)
- `_get_domain_aal_with_no_move_line()` - Domain for AAL without move lines
- `_get_profitability_labels()` - Returns profitability section labels
- `_get_profitability_sequence_per_invoice_type()` - Returns ordering sequence
- `action_profitability_items()` - Action to open profitability items
- `action_open_analytic_items()` - Action to open analytic items

## Views
- `account_analytic_line_views.xml`
- `project_project_views.xml`
- `project_task_views.xml`
- `project_sharing_project_task_views.xml`
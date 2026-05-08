# Project HR Expense Module Requirements

## Module Overview
- **Name**: Project Expenses
- **Version**: 1.0
- **Category**: Services/expenses
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto-install**: True

## Dependencies
- `project_account`
- `hr_expense`

## Description
Bridge module to add the number of expenses linked to an analytic account to a project form.

## Models
- Extends `project.project` with expense-related profitability
- Extends `hr.expense` with project reference

## Key Methods
- `_get_expense_action()` - Returns action for expense list
- `_get_add_purchase_items_domain()` - Excludes expense lines from purchase items
- `action_profitability_items()` - Handles 'expenses' section
- `action_open_project_expenses()` - Opens project expenses
- `_get_profitability_labels()` - Adds 'expenses' label
- `_get_profitability_sequence_per_invoice_type()` - Sequence for expenses (13)
- `_get_already_included_profitability_invoice_line_ids()` - Excludes expense-related move lines
- `_get_expenses_profitability_items()` - Gets expense profitability items
- `_get_profitability_aal_domain()` - Domain for analytic lines excluding expenses
- `_get_profitability_items()` - Combines expense data with profitability

## Demo Data
- `project_hr_expense_demo.xml`

## Views
- `project_project_views.xml`
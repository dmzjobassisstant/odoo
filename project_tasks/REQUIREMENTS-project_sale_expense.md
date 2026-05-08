# Project Sale Expense Module Requirements

## Module Overview
- **Name**: Project - Sale - Expense
- **Version**: 1.0
- **Category**: Services/Project
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto-install**: True

## Dependencies
- `sale_project`
- `sale_expense`
- `project_hr_expense`

## Description
Adds a full traceability of reinvoice expenses on the profitability report.

## Models
- Extends `account.move.line` with expense and project links
- Extends `hr.expense` with project profitability methods
- Extends `project.project` with expense reinvoice traceability

## Key Methods
- Extends `_get_expenses_profitability_items()` to handle reinvoiced expenses
- Adds expense reinvoice tracking to project profitability

## Structure
- `models/`
  - `__init__.py`
  - `account_move_line.py`
  - `hr_expense.py`
  - `project_project.py`
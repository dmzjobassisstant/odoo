# Sales Expense (sale_expense)

## Module Details

- **Name**: Sales Expense
- **Version**: 1.0
- **Category**: Sales/Sales
- **Summary**: Quotation, Sales Orders, Delivery & Invoicing Control
- **Description**: Reinvoice Employee Expense - Create some products for which you can re-invoice the costs. This module allows to reinvoice employee expense, by setting the SO directly on the expense.
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Installable**: True
- **Auto Install**: True

## Dependencies

| Type | Module |
|------|--------|
| Core | sale_management |
| Core | hr_expense |

## External Dependencies

None

## Security

None

## Data Files

- `data/sale_expense_data.xml`
- `views/product_view.xml`
- `views/hr_expense_views.xml`
- `views/sale_order_views.xml`

## Models

- `account_move.py`
- `account_move_line.py`
- `hr_expense.py`
- `hr_expense_split.py`
- `product_template.py`
- `sale_order.py`
- `sale_order_line.py`

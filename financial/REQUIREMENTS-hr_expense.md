# REQUIREMENTS — hr_expense (Expenses)

## Module Details
- **Name:** Expenses
- **Category:** Human Resources/Expenses
- **Version:** 2.1
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Application:** Yes

## Depends
- `account`
- `web_tour`
- `hr`

## Description
Submit, validate and reinvoice employee expenses. Manages the full expense workflow: Draft → Submitted → Approved → Validation → Accounting entries creation. Uses analytic accounting and is compatible with invoice on timesheet module.

## Data Files
- `security/hr_expense_security.xml`
- `security/ir.model.access.csv`
- `data/digest_data.xml`
- `data/mail_activity_type_data.xml`
- `data/mail_alias_data.xml`
- `data/mail_message_subtype_data.xml`
- `data/mail_templates.xml`
- `data/hr_expense_sequence.xml`
- `data/hr_expense_data.xml`
- `data/hr_expense_tour.xml`
- `data/hr_expense_cron.xml`
- `wizard/hr_expense_refuse_reason_views.xml`
- `wizard/hr_expense_approve_duplicate_views.xml`
- `wizard/hr_expense_split_wizard_views.xml`
- `wizard/hr_expense_post_wizard_views.xml`
- `views/product_product_views.xml`
- `views/hr_expense_views.xml`
- `views/mail_activity_views.xml`
- `security/ir_rule.xml`
- `report/hr_expense_report.xml`
- `views/account_move_views.xml`
- `views/account_payment_views.xml`
- `views/hr_department_views.xml`
- `views/res_config_settings_views.xml`
- `views/hr_employee_views.xml`

## Demo
- `data/hr_expense_demo.xml`

## Models
- `hr.expense`
- `hr.expense.split`
- `account.move`
- `account.payment`
- `product.product`
- `mail.activity`

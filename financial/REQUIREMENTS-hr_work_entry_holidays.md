# REQUIREMENTS — hr_work_entry_holidays (Time Off in Payslips)

## Module Details
- **Name:** Time Off in Payslips
- **Category:** Human Resources/Payroll
- **Version:** 1.0
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Auto-install:** True

## Depends
- `hr_holidays`
- `hr_work_entry`

## Description
Manage Time Off in Payslips. Integrates time off in payslips.

## Data Files
- `data/hr_leave_type_data.xml`
- `views/hr_leave_views.xml`
- `views/hr_leave_type_views.xml`

## Demo
- `data/hr_payroll_holidays_demo.xml`

## Models
- `hr.leave`
- `hr.leave.type`

## Hooks
- `_validate_existing_work_entry` (post_init)

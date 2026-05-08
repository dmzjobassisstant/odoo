# Requirements: pos_hr

## Module Details
- **Name:** POS - HR
- **Category:** Sales/Point of Sale
- **Summary:** Link module between Point of Sale and HR
- **Author:** Odoo S.A.
- **License:** LGPL-3

## Description
This module allows Employees (and not users) to log in to the Point of Sale application using a barcode, a PIN number or both. The actual till still requires one user but an unlimited number of employees can log on to that till and process sales.

## Dependencies
- `point_of_sale`
- `hr`

## Auto Install
- Yes

## Data Files
- `views/pos_config.xml`
- `views/pos_order_view.xml`
- `views/pos_payment_view.xml`
- `views/pos_order_report_view.xml`
- `views/single_employee_sales_report.xml`
- `views/res_config_settings_views.xml`
- `wizard/pos_daily_sales_reports.xml`

## Assets
- `point_of_sale._assets_pos`: `pos_hr/static/src/**/*`
- `web.assets_tests`: `pos_hr/static/tests/tours/**/*`
- `web.assets_unit_tests`: `pos_hr/static/tests/unit/**/*`

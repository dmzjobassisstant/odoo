# pos_hr Requirements

## Module Overview
- **Name**: POS - HR
- **Category**: Sales/Point of Sale
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.0
- **Installable**: True
- **Auto-install**: True

## Dependencies
- `point_of_sale`
- `hr`

## Description
Links Point of Sale with HR module, allowing employees (not users) to log in to PoS using barcode, PIN, or both.

## Models
- `hr.employee` - Extended with POS functionality
  - `_load_pos_data_domain()` - Domain for POS data loading
  - `_load_pos_data_fields()` - Fields to load: name, user_id, work_contact_id
  - `_load_pos_data_read()` - Read employee data with role assignment
  - `get_barcodes_and_pin_hashed()` - Get hashed barcode/PIN for POS
  - `_unlink_except_active_pos_session()` - Prevent deletion during active sessions

- `pos.config` - Extended with employee access control
  - `minimal_employee_ids` - Employees with minimal access
  - `basic_employee_ids` - Employees with basic access
  - `advanced_employee_ids` - Employees with manager access
  - `_employee_domain()` - Build employee filtering domain
  - `_onchange_*_employee_ids()` - Onchange handlers to maintain exclusivity

- `pos.session` - Extended for HR

- `pos.order` - Extended for employee tracking

- `pos.payment` - Extended for employee tracking

- `product.product` - Extended

- `account.bank.statement` - Extended

- `single.employee.sales.report` - Report model

## Employee Roles in POS
- `admin` - PoS Manager users
- `manager` - Users in advanced_employee_ids
- `minimal` - Users in minimal_employee_ids
- `cashier` - Default role

## Security
- `get_barcodes_and_pin_hashed()` requires `point_of_sale.group_pos_user` group
- Record rules applied for visibility filtering
- Barcode and PIN are SHA-1 hashed

## Views
- `views/pos_config.xml`
- `views/pos_order_view.xml`
- `views/pos_payment_view.xml`
- `views/pos_order_report_view.xml`
- `views/single_employee_sales_report.xml`
- `views/res_config_settings_views.xml`
- `wizard/pos_daily_sales_reports.xml`

## Assets
### POS Assets (point_of_sale._assets_pos)
- `pos_hr/static/src/**/*`

### Tests
- `web.assets_tests`: Tours
- `web.assets_unit_tests`: Unit tests

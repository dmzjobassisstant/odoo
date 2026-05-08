# sale_timesheet Requirements

## Module Overview
- **Name**: Sales Timesheet
- **Category**: Sales/Sales
- **Summary**: Sell based on timesheets
- **Description**: Allows to sell timesheets in your sales order. Sets the right product on all timesheet lines according to the order/contract you work on for real delivered quantities in sales orders.
- **Author**: Odoo S.A.
- **License**: LGPL-3

## Technical Details

### Dependencies
- `sale_project`
- `hr_timesheet`
- Auto-installs: True

### Data Files
- `data/sale_service_data.xml`
- `security/ir.model.access.csv`
- `security/sale_timesheet_security.xml`
- `views/account_invoice_views.xml`
- `views/sale_order_views.xml`
- `views/product_views.xml`
- `views/project_task_views.xml`
- `views/hr_timesheet_views.xml`
- `views/res_config_settings_views.xml`
- `views/sale_timesheet_portal_templates.xml`
- `views/project_sharing_views.xml`
- `views/project_portal_templates.xml`
- `report/timesheets_analysis_views.xml`
- `report/report_timesheet_templates.xml`
- `report/project_report_view.xml`
- `wizard/sale_make_invoice_advance_views.xml`

### Demo Data
- `data/sale_service_demo.xml`

### Assets
- `web.assets_frontend`: SCSS files
- `web.assets_backend`: Components
- `web.assets_tests`: Tour tests
- `web.assets_unit_tests`: Unit tests
- `project.webclient`: SO line field components

### Hooks
- **post_init_hook**: `_sale_timesheet_post_init`
- **uninstall_hook**: `uninstall_hook`

### Models
- `account.move` - Extended with timesheet billing
- `hr.timesheet` - Timesheet lines linked to sale orders
- `project.project` - Project with timesheet billing
- `sale.order` - Extended with timesheet services
- `sale.order.line` - Service lines with timesheet tracking
- `product.template` - Products with timesheet billing

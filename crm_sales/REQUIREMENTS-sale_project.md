# sale_project Requirements

## Module Overview
- **Name**: Sales - Project
- **Category**: Sales/Sales
- **Summary**: Task Generation from Sales Orders
- **Description**: Allows to create task from sales order. Generates a project/task from sales orders.
- **Author**: Odoo S.A.
- **License**: LGPL-3

## Technical Details

### Dependencies
- `sale_management`
- `sale_service`
- `project_account`
- Auto-installs: `sale_management`, `project_account`

### Data Files
- `security/ir.model.access.csv`
- `security/sale_project_security.xml`
- `views/product_views.xml`
- `views/project_task_views.xml`
- `views/sale_order_line_views.xml`
- `views/sale_order_views.xml`
- `views/sale_project_portal_templates.xml`
- `views/project_update_template.xml`
- `views/project_sharing_views.xml`
- `views/project_views.xml`
- `views/project_task_type_views.xml`
- `data/sale_project_data.xml`
- `wizard/project_template_create_wizard.xml`

### Demo Data
- `data/sale_project_demo.xml`

### Assets
- `web.assets_backend`: Components, core, views
- `web.assets_tests`: Tour tests
- `web.assets_unit_tests`: Unit tests

### Hooks
- **post_init_hook**: `_set_allow_billable_in_project`
- **uninstall_hook**: `uninstall_hook`

### Models
- `project.project` - Project model with sale order integration
- `project.task` - Task model linked to sale order lines
- `sale.order` - Extended with project/task generation
- `sale.order.line` - Extended with service product handling
- `product.template` - Product with service tracking
- `project.milestone` - Project milestones for sales

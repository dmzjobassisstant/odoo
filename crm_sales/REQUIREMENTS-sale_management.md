# Sales Management (sale_management)

## Module Details

- **Name**: Sales
- **Version**: 1.0
- **Category**: Sales/Sales
- **Summary**: From quotations to invoices
- **Description**: Manage sales quotations and orders. This application allows you to manage your sales goals in an effective and efficient manner by keeping track of all sales orders and history. It handles the full sales workflow: Quotation -> Sales order -> Invoice.
- **Website**: https://www.odoo.com/app/sales
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Application**: Yes

## Dependencies

| Type | Module |
|------|--------|
| Core | sale |
| Core | digest |

## External Dependencies

None

## Security

- `security/ir.model.access.csv`
- `security/sale_management_security.xml`

## Data Files

- `data/digest_data.xml`
- `views/sale_order_template_views.xml`
- `views/digest_views.xml`
- `views/res_config_settings_views.xml`
- `views/sale_order_views.xml`
- `views/sale_portal_templates.xml`
- `views/sale_management_menus.xml`

## Demo Data

- `data/sale_order_template_demo.xml`

## Models

- `digest.py`
- `res_company.py`
- `res_config_settings.py`
- `sale_order.py`
- `sale_order_line.py`
- `sale_order_template.py`
- `sale_order_template_line.py`

## Assets

- `web.assets_backend`: `sale_management/static/src/fields/**/*`
- `web.assets_frontend`: `sale_management/static/src/interactions/**/*`
- `web.assets_unit_tests`: `sale_management/static/tests/**/*.test.js`

## Hooks

- Pre init hook: `pre_init_hook`
- Post init hook: `post_init_hook`
- Uninstall hook: `uninstall_hook`

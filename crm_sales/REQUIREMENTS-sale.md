# Sales (sale)

## Module Details

- **Name**: Sales
- **Version**: 1.2
- **Category**: Sales/Sales
- **Summary**: Sales internal machinery
- **Description**: This module contains all the common features of Sales Management and eCommerce.
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Installable**: True
- **Auto Install**: No

## Dependencies

| Type | Module |
|------|--------|
| Core | sales_team |
| Core | account_payment (implies: account, payment, portal) |
| Core | utm |

## External Dependencies

None

## Security

- `security/ir.model.access.csv`
- `security/res_groups.xml`
- `security/ir_rules.xml`

## Data Files

- `report/account_invoice_report_views.xml`
- `report/ir_actions_report_templates.xml`
- `report/ir_actions_report.xml`
- `report/sale_report_views.xml`
- `data/ir_cron.xml`
- `data/ir_sequence_data.xml`
- `data/mail_message_subtype_data.xml`
- `data/mail_template_data.xml`
- `data/sale_tour.xml`
- `data/ir_config_parameter.xml`
- `wizard/account_accrued_orders_wizard_views.xml`
- `wizard/mass_cancel_orders_views.xml`
- `wizard/payment_link_wizard_views.xml`
- `wizard/res_config_settings_views.xml`
- `wizard/sale_make_invoice_advance_views.xml`
- `wizard/sale_order_discount_views.xml`
- `views/sale_order_views.xml`
- `views/account_views.xml`
- `views/crm_team_views.xml`
- `views/mail_activity_views.xml`
- `views/mail_activity_plan_views.xml`
- `views/payment_views.xml`
- `views/product_document_views.xml`
- `views/product_pricelist_item_views.xml`
- `views/product_template_views.xml`
- `views/product_views.xml`
- `views/res_partner_views.xml`
- `views/sale_order_line_views.xml`
- `views/sale_portal_templates.xml`
- `views/utm_campaign_views.xml`
- `views/sale_menus.xml`

## Demo Data

- `data/product_demo.xml`
- `data/sale_demo.xml`

## Models

- `account_move.py`
- `account_move_line.py`
- `analytic.py`
- `chart_template.py`
- `crm_team.py`
- `ir_actions_report.py`
- `ir_config_parameter.py`
- `payment_provider.py`
- `payment_transaction.py`
- `product_document.py`
- `product_pricelist_item.py`
- `product_product.py`
- `product_template.py`
- `res_company.py`
- `res_partner.py`
- `sale_order.py`
- `sale_order_line.py`
- `utm_campaign.py`

## Assets

- `web.assets_backend`: SCSS, JS models, product, combo configurator, sale action helper, etc.
- `web.assets_frontend`: interactions, portal SCSS
- `web.assets_tests`: tours and tour utils
- `web.assets_unit_tests`: mock server, test helpers, test files
- `web.report_assets_common`: sale report SCSS

## Hooks

- Post init hook: `_post_init_hook`

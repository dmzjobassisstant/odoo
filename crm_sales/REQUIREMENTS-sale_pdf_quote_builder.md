# Sales PDF Quotation Builder (sale_pdf_quote_builder)

## Module Details

- **Name**: Sales PDF Quotation Builder
- **Version**: Not specified
- **Category**: Sales/Sales
- **Summary**: Build nice quotations
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto Install**: True

## Dependencies

| Type | Module |
|------|--------|
| Core | sale_management |

## External Dependencies

None

## Security

- `security/ir.model.access.csv`
- `security/ir_rules.xml`

## Data Files

- `data/ir_cron.xml`
- `data/sale_pdf_form_field.xml`
- `report/ir_actions_report.xml`
- `views/product_document_views.xml`
- `views/quotation_document_views.xml`
- `views/sale_order_template_views.xml`
- `views/sale_order_views.xml`
- `views/sale_pdf_form_field_views.xml`
- `views/sale_pdf_quote_builder_menus.xml`
- `wizards/res_config_settings_views.xml`

## Demo Data

- `data/sale_pdf_quote_builder_demo.xml`

## Models

- `ir_actions_report.py`
- `product_document.py`
- `quotation_document.py`
- `sale_order.py`
- `sale_order_line.py`
- `sale_order_template.py`
- `sale_pdf_form_field.py`

## Assets

- `web.assets_backend`: `sale_pdf_quote_builder/static/src/js/**/*`
- `web.assets_tests`: `sale_pdf_quote_builder/static/tests/tours/**/*`

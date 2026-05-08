# Gelato (sale_gelato)

## Module Details

- **Name**: Gelato
- **Version**: Not specified
- **Category**: Sales/Sales
- **Summary**: Place orders through Gelato's print-on-demand service
- **Author**: Odoo S.A.
- **License**: LGPL-3

## Dependencies

| Type | Module |
|------|--------|
| Core | sale |
| Core | delivery |

## External Dependencies

None

## Security

None

## Data Files

- `data/product_data.xml`
- `data/delivery_carrier_data.xml`
- `data/mail_template_data.xml`
- `views/delivery_carrier_views.xml`
- `views/product_document_views.xml`
- `views/product_product_views.xml`
- `views/product_template_views.xml`
- `wizards/res_config_settings_views.xml`

## Models

- `delivery_carrier.py`
- `product_document.py`
- `product_product.py`
- `product_template.py`
- `res_company.py`
- `res_partner.py`
- `sale_order.py`
- `sale_order_line.py`

# l10n_tw_edi_ecpay_website_sale — Taiwan - E-invoicing Ecommerce

## Metadata
- **Name**: Taiwan - E-invoicing Ecommerce
- **Version**: 1.0
- **Author**: Odoo S.A.
- **Category**: Website Sale/Localizations/EDI
- **License**: LGPL-3

## Description
This bridge module allows the user to input Ecpay information in ecommerce for sending their invoices to the Ecpay system

## Dependencies
- `website_sale`
- `l10n_tw_edi_ecpay`

## Auto-install
- `True`

## Hooks
- **post_init_hook**: `_post_init_hook`

## Data Files
- `data/data.xml`
- `views/sale_order_views.xml`
- `views/templates.xml`

## Assets
- `web.assets_frontend`: `l10n_tw_edi_ecpay_website_sale/static/src/**/*`
- `web.assets_tests`: `l10n_tw_edi_ecpay_website_sale/static/tests/**/*`

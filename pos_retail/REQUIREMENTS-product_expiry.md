# Requirements: product_expiry

## Module Details
- **Name:** Products Expiration Date
- **Category:** Supply Chain/Inventory
- **Author:** Odoo S.A.
- **License:** LGPL-3

## Description
Track different dates on products and production lots.

**Following dates can be tracked:**
- end of life
- best before date
- removal date
- alert date

Also implements the removal strategy First Expiry First Out (FEFO) widely used, for example, in food industries.

## Dependencies
- `stock`

## Data Files
- `security/ir.model.access.csv`
- `security/stock_security.xml`
- `views/production_lot_views.xml`
- `views/product_template_views.xml`
- `views/res_config_settings_views.xml`
- `views/stock_move_views.xml`
- `views/stock_quant_views.xml`
- `wizard/confirm_expiry_view.xml`
- `report/report_deliveryslip.xml`
- `report/report_lot_barcode.xml`
- `data/product_expiry_data.xml`

## Hooks
- `post_init_hook`: `_enable_tracking_numbers`

## Assets
- `web.assets_tests`: `product_expiry/static/tests/tours/*.js`
- `web.assets_backend`: `product_expiry/static/src/**/*`

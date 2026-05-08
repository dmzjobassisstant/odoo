# Requirements: pos_event

## Module Details
- **Name:** POS - Event
- **Category:** Technical
- **Version:** 1.0
- **Summary:** Link module between Point of Sale and Event
- **Author:** Odoo S.A.
- **License:** LGPL-3

## Dependencies
- `point_of_sale`
- `event_product`

## Auto Install
- Yes

## Data Files
- `security/ir.model.access.csv`
- `data/point_of_sale_data.xml`
- `data/event_product_data.xml`
- `views/event_registration_views.xml`
- `views/event_event_views.xml`
- `views/pos_order_views.xml`

## Demo Files
- `data/event_product_demo.xml`
- `data/point_of_sale_demo.xml`

## Assets
- `point_of_sale._assets_pos`: `pos_event/static/src/**/*`
- `web.assets_tests`: `pos_event/static/tests/tours/**/*`
- `web.assets_unit_tests`: `pos_event/static/tests/unit/**/*`

# Requirements: delivery_mondialrelay

## Module Details
- **Name:** delivery_mondialrelay
- **Category:** Shipping Connectors
- **Version:** 0.1
- **Summary:** Let's choose a Point Relais® as shipping address
- **Author:** Odoo S.A.
- **License:** LGPL-3

## Description
This module allow your customer to choose a Point Relais® and use it as shipping address. This module doesn't implement the WebService. It is only the integration of the widget. Delivery price pre-configured is an example, you need to adapt the pricing's rules.

## Dependencies
- `stock_delivery`

## Data Files
- `data/data.xml`
- `views/portal_address_templates.xml`
- `views/views.xml`
- `wizard/choose_delivery_carrier_views.xml`

## Assets
- `web.assets_backend`:
  - `delivery_mondialrelay/static/src/components/**/*.js`
  - `delivery_mondialrelay/static/src/scss/mondialrelay.scss`

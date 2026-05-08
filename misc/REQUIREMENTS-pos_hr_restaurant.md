# pos_hr_restaurant Requirements

## Module Overview
- **Name**: POS HR Restaurant
- **Category**: Sales/Point of Sale
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.0
- **Auto-install**: True

## Dependencies
- `pos_hr`
- `pos_restaurant`

## Description
Adapts POS behavior when both pos_hr and pos_restaurant modules are installed.

## Module Relationship
This is a link module that combines pos_hr (employee management) with pos_restaurant (restaurant-specific POS features).

## Assets
### POS Assets (point_of_sale._assets_pos)
- `pos_hr_restaurant/static/src/**/*`

### Tests
- `web.assets_tests`: Test files

## Notes
- No models defined (all logic is in static JS)
- Adapts behavior through asset bundles and potentially overriding pos_hr static resources

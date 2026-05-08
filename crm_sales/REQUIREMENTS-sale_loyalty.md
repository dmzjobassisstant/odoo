# Sale Loyalty (sale_loyalty)

## Module Details

- **Name**: Sale Loyalty
- **Version**: 1.0
- **Category**: Sales/Sales
- **Summary**: Use discounts and loyalty programs in sales orders
- **Description**: Integrate discount and loyalty programs mechanisms in sales orders.
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto Install**: True

## Dependencies

| Type | Module |
|------|--------|
| Core | sale |
| Core | loyalty |

## External Dependencies

None

## Security

- `security/ir.model.access.csv`

## Data Files

- `data/sale_loyalty_data.xml`
- `wizard/sale_loyalty_coupon_wizard_views.xml`
- `wizard/sale_loyalty_reward_wizard_views.xml`
- `views/loyalty_card_views.xml`
- `views/loyalty_program_views.xml`
- `views/sale_order_views.xml`
- `views/sale_portal_templates.xml`
- `views/res_partner_views.xml`
- `views/sale_loyalty_menus.xml`

## Models

- `loyalty_card.py`
- `loyalty_history.py`
- `loyalty_program.py`
- `loyalty_reward.py`
- `sale_order.py`
- `sale_order_coupon_points.py`
- `sale_order_line.py`

## Assets

- `web.assets_backend`: `sale_loyalty/static/src/**/*`

## Hooks

- Uninstall hook: `uninstall_hook`

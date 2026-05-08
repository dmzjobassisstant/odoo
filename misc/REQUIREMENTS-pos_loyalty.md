---
name: pos_loyalty
summary: Use Coupons, Gift Cards and Loyalty programs in Point of Sale
description: Use Coupons, Gift Cards and Loyalty programs in Point of Sale
author: Odoo S.A.
version: '2.0'
depends: loyalty, point_of_sale
external_dependencies: []
data_entities:
  - loyalty.card: Loyalty card for rewards
    fields: [program_id, partner_id, points]
  - loyalty.program: Loyalty program definition
    fields: [name, trigger, rule_ids]
  - loyalty.rule: Program rules
    fields: [program_id, type, operator, minimum_amount]
views:
  - xml: loyalty_card_views.xml - Loyalty Card Views
  - xml: loyalty_mail_views.xml - Loyalty Mail Views
  - xml: pos_loyalty_menu_views.xml - POS Loyalty Menu Views
  - xml: res_config_settings_view.xml - Settings View
  - xml: loyalty_program_views.xml - Loyalty Program Views
  - xml: res_partner_views.xml - Partner Views
access_rights:
  - base.user: read,write
business_logic:
  - compute_points: Compute loyalty points
  - _check_coupon_code: Validate coupon code
  - action_apply_loyalty: Apply loyalty discount
external_integrations:
  - mail: Send loyalty notification emails
---
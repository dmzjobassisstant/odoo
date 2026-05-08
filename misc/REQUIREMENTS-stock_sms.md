---
name: stock_sms
summary: Send text messages when final stock move
description: Send text messages when final stock move
author: Odoo S.A.
version: '1.0'
depends: stock, sms
external_dependencies: []
data_entities:
  - sms.template: SMS template for stock moves
    fields: [name, body, model_id]
  - stock.picking: Stock picking with SMS notification
    fields: [name, move_ids, state, sms_template_id]
views:
  - xml: res_config_settings_views.xml - Settings Views
  - xml: wizard/confirm_stock_sms_views.xml - Confirm SMS Wizard
access_rights:
  - stock.user: read,write
business_logic:
  - _assign_default_sms_template_picking_id: Assign default SMS template
  - _reset_sms_text_confirmation: Reset SMS on uninstall
  - action_send_sms_confirmation: Send SMS on stock move completion
  - _check_sms_enabled: Check if SMS is enabled
external_integrations:
  - sms: Send SMS notifications on stock moves
---
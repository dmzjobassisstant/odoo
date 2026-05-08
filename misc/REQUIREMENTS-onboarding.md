---
name: onboarding
summary: Manage onboardings and their progress
description: This module allows to manage onboardings and their progress
author: Odoo S.A.
version: '1.2'
depends: web
external_dependencies: []
data_entities: []
views:
  - xml: onboarding_templates.xml - Onboarding templates
  - xml: onboarding_views.xml - Onboarding views
  - xml: onboarding_menus.xml - Onboarding menus
access_rights:
  - base.user: read,write
business_logic:
  - _compute_onboarding_state: Compute onboarding step state
  - action_close_onboarding_box: Close onboarding box
external_integrations: []
---
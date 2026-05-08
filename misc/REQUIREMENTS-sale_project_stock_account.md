---
name: sale_project_stock_account
summary: Technical Bridge
description: Technical Bridge module connecting sale_project and project_stock_account
author: Odoo S.A.
version: '1.0'
depends: sale_project, project_stock_account
external_dependencies: []
data_entities: []
views: []
access_rights:
  - base.user: read,write
business_logic:
  - _post_init_hook: Post-init hook for stock account linking
external_integrations: []
---
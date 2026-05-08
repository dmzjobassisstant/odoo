---
name: stock_maintenance
summary: See lots used in maintenance
description: Stock in Maintenance - Open the record of the serial number from an equipment form
author: Odoo S.A.
version: '1.0'
depends: stock, maintenance
external_dependencies: []
data_entities:
  - maintenance.equipment: Maintenance equipment tracking
    fields: [name, serial_no, product_id, location_id]
  - stock.production.lot: Lot/serial number tracking
    fields: [name, product_id, reference]
views:
  - xml: maintenance_views.xml - Maintenance Views
  - xml: stock_location.xml - Stock Location Views
access_rights:
  - maintenance.user: read,write
  - stock.user: read,write
business_logic:
  - _link_lot_to_maintenance: Link lot to maintenance equipment
  - action_view_lot: View lot from maintenance
external_integrations: []
---
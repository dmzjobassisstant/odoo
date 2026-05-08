---
name: stock_fleet
summary: Stock Transport - Dispatch Management System
description: Transport Management: organize packs in your fleet, or carriers.
author: Odoo S.A.
version: '1.0'
depends: stock_picking_batch, fleet
external_dependencies: []
data_entities:
  - fleet.vehicle: Fleet vehicle for transport
    fields: [model_id, license_plate, driver_id]
  - stock.picking.batch: Batch picking for dispatch
    fields: [name, picking_ids, state]
views:
  - xml: fleet_vehicle_model.xml - Fleet Vehicle Model Views
  - xml: stock_picking_batch.xml - Picking Batch Views
  - xml: stock_picking_type.xml - Picking Type Views
  - xml: stock_picking_view.xml - Picking Views
  - xml: report/report_picking_batch.xml - Batch Picking Report
  - xml: stock_location.xml - Stock Location Views
access_rights:
  - stock.user: read,write
  - fleet.user: read,write
business_logic:
  - _enable_dispatch_management: Enable dispatch management feature
  - _assign_vehicle_to_picking: Assign vehicle to picking
  - action_dispatch: Create dispatch from batch
external_integrations:
  - fleet: Integrate with fleet management
---
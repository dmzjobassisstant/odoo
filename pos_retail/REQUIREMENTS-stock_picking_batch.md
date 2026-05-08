# Requirements: stock_picking_batch

## Module Details
- **Name:** Warehouse Management: Batch Transfer
- **Category:** Supply Chain/Inventory
- **Version:** 1.0
- **Author:** Odoo S.A.
- **License:** LGPL-3

## Description
This module adds the batch transfer option in warehouse management.

## Dependencies
- `stock`

## Data Files
- `security/ir.model.access.csv`
- `views/stock_picking_batch_views.xml`
- `views/stock_picking_type_views.xml`
- `views/stock_move_line_views.xml`
- `views/stock_picking_wave_views.xml`
- `views/stock_picking_views.xml`
- `data/stock_picking_batch_data.xml`
- `wizard/stock_picking_to_batch_views.xml`
- `wizard/stock_add_to_wave_views.xml`
- `report/stock_picking_batch_report_views.xml`
- `report/report_picking_batch.xml`
- `security/stock_picking_batch_security.xml`

## Demo Files
- `data/stock_picking_batch_demo.xml`

## Assets
- `web.assets_backend`:
  - `stock_picking_batch/static/src/js/stock_picking_many2many_field.js`
  - `stock_picking_batch/static/src/scss/*.scss`
- `web.assets_tests`: `stock_picking_batch/static/tests/tours/**/*`

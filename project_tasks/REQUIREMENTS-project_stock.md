# Project Stock Module Requirements

## Module Overview
- **Name**: Project Stock
- **Version**: 1.0
- **Category**: Services/Project
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto-install**: True

## Dependencies
- `stock`
- `project`

## Description
Link Stock pickings to Project. Track deliveries and receipts related to a project.

## Models
- Extends `project.project` with stock picking actions
- Extends `stock.picking` with project link

## Key Methods
- `action_open_deliveries()` - Open outgoing pickings
- `action_open_receipts()` - Open incoming pickings
- `action_open_all_pickings()` - Open all project pickings
- `_get_picking_action()` - Generic picking action builder

## Views
- `stock_picking_views.xml`
- `project_project_views.xml`
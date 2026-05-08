# Requirements: repair

## Module Overview
- **Name**: Repairs
- **Version**: 1.0
- **Category**: Supply Chain/Inventory
- **Depends**: `sale_stock`, `sale_management`
- **Application**: Yes
- **License**: LGPL-3

## Description
Manage product repairs - track damaged products, parts usage, warranties, and repair quotations.

## Dependencies

### Internal Dependencies
- `sale_stock` - Sale stock integration
- `sale_management` - Sale management

## Models

### Core Models
| Model | Description |
|-------|-------------|
| `repair.order` | Repair Order - main repair entity |
| `repair.tags` | Repair Tags |
| `stock.move` | Extended with repair linking |
| `stock.move.line` | Extended with repair linking |
| `stock.lot` | Extended with repair history |
| `stock.picking` | Extended with repair linking |
| `stock.warehouse` | Extended with repair operations |
| `product.product` | Extended with repair configuration |
| `sale.order` | Extended with repair orders |

## Repair Order States
- `draft` - New, unconfirmed
- `confirmed` - Confirmed repair
- `under_repair` - Repair in progress
- `done` - Repaired
- `cancel` - Cancelled

## Views & Security

### Data Files
- `security/ir.model.access.csv` - Access control
- `security/repair_security.xml` - Repair security rules
- `data/repair_data.xml` - Demo and default data

### View Files
- `wizard/stock_warn_insufficient_qty_views.xml`
- `views/product_views.xml`
- `views/stock_move_views.xml`
- `views/repair_views.xml`
- `views/sale_order_views.xml`
- `views/stock_lot_views.xml`
- `views/stock_picking_views.xml`
- `views/stock_warehouse_views.xml`

### Report Files
- `report/repair_reports.xml`
- `report/repair_templates_repair_order.xml`

## Key Features
- Repair order creation and tracking
- Product to repair selection (consumable type)
- Lot/serial number tracking
- Component parts (stock moves)
- Parts source and destination locations
- Removed parts tracking
- Warranty handling (under warranty flag)
- Sale order linking
- Transfer/return picking linking
- Repair request from sale order line
- Priority scheduling
- Internal and external notes
- Repair quotation reports
- Stock operations for repair flow
- Multi-company support

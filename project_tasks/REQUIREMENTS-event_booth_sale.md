# Requirements: event_booth_sale

## Module Overview
- **Name**: Events Booths Sales
- **Version**: 1.2
- **Category**: Marketing/Events
- **Depends**: `event_booth`, `event_sale`
- **Auto-install**: Yes
- **License**: LGPL-3

## Description
Sell event booths and track payments on sale orders.

## Dependencies

### Internal Dependencies
- `event_booth` - Event booth module
- `event_sale` - Event sales module

## Models

### Core Models
| Model | Description |
|-------|-------------|
| `event.booth` | Extended with sale order linking |
| `event.booth.category` | Extended with product/pricing |
| `event.booth.registration` | Booth registration/payment tracking |
| `event.type.booth` | Extended with sale configuration |
| `sale.order` | Extended with booth references |
| `sale.order.line` | Extended with booth configuration |
| `product.product` | Extended for booth products |
| `product.template` | Extended for booth product templates |
| `account.move` | Invoice linked to booth sale |

## Views & Security

### Data Files
- `security/ir.model.access.csv` - Access control
- `data/product_data.xml` - Booth sale products
- `data/event_booth_category_data.xml` - Booth category data

### View Files
- `views/sale_order_views.xml`
- `views/event_type_booth_views.xml`
- `views/event_booth_category_views.xml`
- `views/event_booth_registration_views.xml`
- `views/event_booth_views.xml`
- `wizard/event_booth_configurator_views.xml`

## Key Features
- Booth selling via sale orders
- Booth product configuration
- Booth registration confirmation
- Sale order line linking to booth reservations
- Invoice generation for booth sales
- Booth configurator wizard

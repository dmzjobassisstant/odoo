# Requirements: event_product

## Module Overview
- **Name**: Events Product
- **Version**: 1.0
- **Category**: Marketing/Events
- **Depends**: `event`, `product`, `account`
- **Auto-install**: Yes
- **License**: LGPL-3

## Description
Integrates products with event tickets for invoicing.

## Dependencies

### Internal Dependencies
- `event` - Event module
- `product` - Product module
- `account` - Accounting module

## Models

### Core Models
| Model | Description |
|-------|-------------|
| `event.event` | Extended with ticket/product linking |
| `event.event.ticket` | Extended with product linking |
| `event.type.ticket` | Extended with product linking |
| `event.registration` | Extended with ticket/product info |
| `product.product` | Extended for event tickets |
| `product.template` | Extended for event ticket templates |

## Views & Security

### Data Files
- `data/event_product_data.xml` - Product data for events

### View Files
- `views/event_ticket_views.xml`
- `views/event_registration_views.xml`

## Key Features
- Link products to event tickets
- Ticket pricing through product pricing
- Registration with product/ticket selection
- Event product invoicing capability

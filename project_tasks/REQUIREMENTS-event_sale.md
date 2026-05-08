# Requirements: event_sale

## Module Overview
- **Name**: Events Sales
- **Version**: 1.3
- **Category**: Marketing/Events
- **Website**: https://www.odoo.com/app/events
- **Depends**: `event_product`, `sale_management`
- **Auto-install**: Yes
- **License**: LGPL-3

## Description
Creating registration with sales orders - connect sale flow with event registration and invoicing.

## Dependencies

### Internal Dependencies
- `event_product` - Event product module
- `sale_management` - Sale management module

## Models

### Core Models
| Model | Description |
|-------|-------------|
| `event.event` | Extended with sale configuration |
| `event.ticket` | Extended with sale order linking |
| `event.registration` | Extended with sale order line reference |
| `sale.order` | Extended with event registrations |
| `sale.order.line` | Extended with event/ticket selection |
| `product.template` | Extended with event category linking |

## Views & Security

### Data Files
- `data/event_sale_data.xml` - Demo/event sale data
- `data/mail_templates.xml` - Mail templates
- `data/event_sale_demo.xml` - Demo sale data
- `data/event_registration_demo.xml` - Registration demo

### View Files
- `views/event_registration_views.xml`
- `views/event_views.xml`
- `views/product_template_views.xml`
- `views/sale_order_views.xml`
- `wizard/event_edit_registration.xml`
- `wizard/event_configurator_views.xml`

### Report Files
- `report/event_sale_report_views.xml`

### Security Files
- `security/ir.model.access.csv`
- `security/ir_rule.xml`
- `security/event_security.xml`

## Key Features
- Event-based service products
- Automatic registration creation from sale order confirmation
- Event category selection on sale order line
- Ticket selection on sale order
- Registration confirmation via sale order
- Event configurator wizard
- Edit registration from sale order
- Sale order reporting for events

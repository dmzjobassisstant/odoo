# Requirements: event_crm_sale

## Module Overview
- **Name**: Event CRM Sale
- **Version**: 1.0
- **Category**: Marketing/Events
- **Website**: https://www.odoo.com/app/events
- **Depends**: `event_crm`, `event_sale`
- **Auto-install**: Yes
- **License**: LGPL-3

## Description
Add information of sale order linked to the registration for the creation of the lead.

## Dependencies

### Internal Dependencies
- `event_crm` - Event CRM module
- `event_sale` - Event Sales module

## Models

### Extended Models
| Model | Original Module | Description |
|-------|----------------|-------------|
| `event.registration` | event_crm | Extended with sale order info for leads |

## Views & Security

### View Files
- `views/event_lead_rule_views.xml` - Lead rule views with sale order fields

## Key Features
- Sale order information added to lead creation from registration
- Links sale order line to registration for lead
- Supports both attendee-based and order-based lead generation

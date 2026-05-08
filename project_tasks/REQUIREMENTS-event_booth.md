# Requirements: event_booth

## Module Overview
- **Name**: Events Booths
- **Version**: 1.1
- **Category**: Marketing/Events
- **Depends**: `event`
- **License**: LGPL-3

## Description
Create and manage booths for events.

## Dependencies

### Internal Dependencies
- `event` - Base event module

## Models

### Core Models
| Model | Description |
|-------|-------------|
| `event.booth` | Event Booth - bookable booth at event |
| `event.booth.category` | Booth Category - type/size grouping |
| `event.type.booth` | Event Type Booth configuration |
| `event.type` | Extended with booth configuration |

## Views & Security

### Data Files
- `security/ir.model.access.csv` - Access control
- `data/event_booth_category_data.xml` - Booth category demo data
- `data/mail_message_subtype_data.xml` - Message subtypes
- `data/mail_templates.xml` - Mail templates for booth booking

### View Files
- `views/event_booth_category_views.xml`
- `views/event_type_booth_views.xml`
- `views/event_booth_views.xml`
- `views/event_type_views.xml`
- `views/event_event_views.xml`
- `views/event_menus.xml`

## Key Features
- Booth management per event
- Booth availability tracking
- Booth booking with customer info (partner, contact name/email/phone)
- Booth states: available/unavailable
- Mail notifications on booth confirmation
- Booth categories for grouping

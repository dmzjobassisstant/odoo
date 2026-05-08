# Requirements: event_sms

## Module Overview
- **Name**: SMS on Events
- **Version**: 1.0
- **Category**: Marketing/Events
- **Depends**: `event`, `sms`
- **Auto-install**: Yes
- **License**: LGPL-3

## Description
Schedule SMS in event management.

## Dependencies

### Internal Dependencies
- `event` - Event module
- `sms` - SMS gateway module

## Models

### Core Models
| Model | Description |
|-------|-------------|
| `event.mail` | Extended with SMS notification support |
| `event.type.mail` | Extended with SMS defaults |
| `event.mail.registration` | Extended with SMS on registration |
| `sms.template` | SMS templates for events |

## Views & Security

### Data Files
- `data/sms_data.xml` - SMS templates for events

### Security Files
- `security/ir.model.access.csv` - Access control
- `security/sms_security.xml` - SMS security rules

## Key Features
- SMS notifications for events
- SMS scheduling on registration
- SMS templates for event communications
- SMS on event type configuration

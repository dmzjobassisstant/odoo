# Requirements: event

## Module Overview
- **Name**: Events Organization
- **Version**: 1.9
- **Category**: Marketing/Events
- **Website**: https://www.odoo.com/app/events
- **Depends**: `barcodes`, `base_setup`, `mail`, `phone_validation`, `portal`, `utm`
- **Application**: Yes
- **License**: LGPL-3

## Description
Organization and management of Events - trainings, conferences, meetings, exhibitions, registrations.

## Dependencies

### Internal Dependencies
- `barcodes` - Barcode scanning for registration
- `base_setup` - Base setup module
- `mail` - Mail/messaging
- `phone_validation` - Phone number validation
- `portal` - Portal access
- `utm` - UTM tracking

## Models

### Core Models
| Model | Description |
|-------|-------------|
| `event.event` | Event - main event entity with date, seats, location |
| `event.type` | Event Type - template for events |
| `event.stage` | Event Stage - Kanban pipeline stages |
| `event.tag` | Event Tags |
| `event.ticket` | Event Ticket - with pricing |
| `event.event.ticket` | Event-specific ticket pricing |
| `event.type.ticket` | Type-level ticket definition |
| `event.registration` | Event Registration - attendee |
| `event.registration.answer` | Registration answer to questions |
| `event.question` | Event Question for registration |
| `event.question.answer` | Predefined question answers |
| `event.mail` | Event mail scheduling |
| `event.type.mail` | Event type mail defaults |
| `event.mail.registration` | Registration-triggered mail |
| `event.mail.slot` | Slot-triggered mail |
| `event.slot` | Event time slot for multi-slot events |

## Views & Security

### Data Files
- `security/event_security.xml` - Event security rules
- `security/ir.model.access.csv` - Access control
- `data/ir_cron_data.xml` - Scheduled actions
- `data/mail_template_data.xml` - Mail templates
- `data/event_data.xml` - Demo data
- `data/event_tour.xml` - Tour data
- `data/event_question_data.xml` - Question data
- `data/res_users_demo.xml` - Demo users
- `data/res_partner_demo.xml` - Demo partners
- `data/event_demo_misc.xml`, `event_demo.xml` - Event demo data
- `data/event_registration_demo.xml` - Registration demo data

### View Files
- `views/event_menu_views.xml`
- `views/event_ticket_views.xml`
- `views/event_mail_views.xml`
- `views/event_registration_views.xml`
- `views/event_slot_views.xml`
- `views/event_type_views.xml`
- `views/event_event_views.xml`
- `views/event_stage_views.xml`
- `views/event_tag_views.xml`
- `views/event_question_views.xml`
- `views/event_registration_answer_views.xml`
- `views/res_config_settings_views.xml`
- `views/event_templates.xml`
- `views/res_partner_views.xml`

### Report Files
- `report/event_event_templates.xml`
- `report/event_event_reports.xml`
- `report/event_registration_report.xml`

## Key Features
- Event creation and management
- Registration tracking with states
- Event tickets with pricing
- Mail/SMS communications on registration
- Barcode scanning for check-in
- Multi-slot events
- Event tags and categories
- Seat capacity management
- Event questions for registrants
- UTM source tracking
- Phone validation for registrations

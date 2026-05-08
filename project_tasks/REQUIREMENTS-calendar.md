# Requirements: calendar

## Module Overview
- **Name**: Calendar
- **Version**: 1.1
- **Category**: Productivity/Calendar
- **Depends**: `base`, `mail`
- **Application**: Yes
- **License**: LGPL-3

## Description
Full-featured calendar system supporting calendar of events and recurring events.

## Dependencies

### External Dependencies
- `vobject` (Python module) - for iCal file generation (optional)

### Internal Dependencies
- `base` - Base module
- `mail` - Mail/messaging module

## Models

### Core Models
| Model | Description |
|-------|-------------|
| `calendar.event` | Calendar Event - supports recurring events, attendees, alarms |
| `calendar.event.type` | Event Type/Category |
| `calendar.recurrence` | Recurrence Rules (RRULE) |
| `calendar.attendee` | Event Attendee with state tracking |
| `calendar.alarm` | Event Alarm/Reminder |
| `calendar.filter` | Calendar Filter |

### Supporting Models
| Model | Description |
|-------|-------------|
| `res.partner` | Partner extended with calendar fields |
| `res.users` | User extended with settings |
| `res.users.settings` | User calendar settings |
| `mail.activity` | Mail activity linked to calendar |
| `mail.activity.type` | Activity type |
| `discuss.channel` | Discuss channel for video calls |

## Views & Security

### Data Files
- `security/ir.model.access.csv` - Access control
- `security/calendar_security.xml` - Calendar security rules
- `data/calendar_cron.xml` - Scheduled actions
- `data/mail_template_data.xml` - Mail templates
- `data/calendar_data.xml` - Demo data
- `data/mail_activity_type_data.xml` - Activity types
- `data/mail_message_subtype_data.xml` - Message subtypes

### View Files
- `views/mail_activity_views.xml`
- `views/calendar_templates.xml`
- `views/calendar_views.xml`
- `views/res_config_settings_views.xml`
- `views/res_partner_views.xml`
- `views/res_users_views.xml`
- `wizard/calendar_provider_config.xml`
- `wizard/calendar_popover_delete_wizard.xml`
- `wizard/mail_activity_schedule_views.xml`

## Key Features
- Calendar event management with start/stop dates
- Recurring events (daily, weekly, monthly, yearly, custom)
- Attendee management with state tracking (accepted, declined, tentative)
- Event alarms/reminders
- Videocall integration via Discuss
- Mail activity integration
- Privacy controls (public, private, confidential)
- Partner calendar views

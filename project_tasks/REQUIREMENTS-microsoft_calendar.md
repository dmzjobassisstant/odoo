# microsoft_calendar — Requirements

## Module Overview
- **Name**: Outlook Calendar
- **Version**: 1.0
- **Category**: Productivity
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Status**: Installable

## Dependencies
- `microsoft_account`
- `calendar`

## Core Functionality
Synchronizes Odoo calendar events with Microsoft Outlook Calendar. Supports two-way sync of calendar events, attendees,recurrence rules, and alarms.

## Key Models
- `calendar.event` — Inherits `calendar.event` + `microsoft.calendar.sync`; stores Microsoft recurrence master ID
- `microsoft.sync.mixin` — Mixin for synchronized models
- `calendar.attendee` — Handles attendee synchronization
- `calendar.recurrence.rule` — Handles recurrence rules
- `calendar.alarm.manager` — Manages calendar alarms
- `res.users` — Extended with Microsoft calendar token fields
- `res.users.settings` — User settings for Microsoft sync

## Key Features
- Two-way sync with Microsoft Outlook Calendar
- OAuth token management via `microsoft_account`
- Support for recurrent events
- Attendee status synchronization
- Alarm/notification management
- Videocall URL patterns (Microsoft Teams)

## Data Files
- `data/microsoft_calendar_data.xml`
- `security/ir.model.access.csv`
- `wizard/reset_account_views.xml`
- `views/res_config_settings_views.xml`
- `views/res_users_views.xml`
- `views/microsoft_calendar_views.xml`

## Assets
- `web.assets_backend`: SCSS and Views from `microsoft_calendar/static/src/views/**/*`
- `web.assets_unit_tests`: Tests from `microsoft_calendar/static/tests/**/*`

## Hooks
- `init_initiating_microsoft_uuid` — Post-init hook

## External Dependencies
- `pytz` — Timezone handling
- `python-dateutil` — Date parsing and relativedelta

## Security
- Access control via `ir.model.access.csv`

# google_calendar Requirements

## Module Overview
- **Name**: Google Calendar
- **Category**: Productivity
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.0
- **Installable**: True

## Dependencies
- `google_account`
- `calendar`

## Description
Synchronizes Odoo calendar events with Google Calendar.

## External Services / API
- Google Calendar API (via google_account service)
- Requires OAuth tokens from Google

## Configuration Parameters (ir.config_parameter)
- `google_calendar_client_id` - Google Calendar OAuth Client ID
- `google_calendar_client_secret` - Google Calendar OAuth Client Secret
- `google_calendar_sync_paused` - Boolean to pause synchronization

## Data Files
- `data/google_calendar_data.xml`
- `security/ir.model.access.csv`

## Models
- `res.users` - Extended with Google Calendar fields:
  - `google_calendar_rtoken` - Refresh token (groups: base.group_system)
  - `google_calendar_token` - Access token (groups: base.group_system)
  - `google_calendar_token_validity` - Token expiry (groups: base.group_system)
  - `google_calendar_sync_token` - Google sync token (groups: base.group_system)
  - `google_calendar_cal_id` - Calendar ID (groups: base.group_system)
  - `google_synchronization_stopped` - Stop sync flag (groups: base.group_system)

- `res.users.settings` - Stores user Google calendar settings

## Security
- Token fields restricted to `base.group_system`
- Access control via `ir.model.access.csv`

## Cron Jobs
- `_sync_all_google_calendar` - Synchronizes all users' calendars

## Views
- `views/res_config_settings_views.xml`
- `views/res_users_views.xml`
- `views/google_calendar_views.xml`
- `wizard/reset_account_views.xml`

## Assets
- `web.assets_backend`: SCSS and views
- `web.assets_unit_tests`: Unit tests

# Requirements: calendar_sms

## Module Overview
- **Name**: Calendar - SMS
- **Version**: 1.1
- **Category**: Productivity/Calendar
- **Depends**: `calendar`, `sms`
- **Auto-install**: Yes
- **License**: LGPL-3

## Description
Send text messages as event reminders.

## Dependencies

### Internal Dependencies
- `calendar` - Base calendar module
- `sms` - SMS gateway module

## Models

### Extended Models
| Model | Original Module | Description |
|-------|----------------|-------------|
| `calendar.event` | calendar | Extended with SMS reminder support |
| `calendar.alarm` | calendar | Extended with SMS notification |
| `calendar.alarm.manager` | calendar | Manages SMS alarm notifications |

## Views & Security

### Data Files
- `data/sms_data.xml` - SMS templates for event reminders

### View Files
- `views/calendar_views.xml` - Calendar view extensions for SMS

## Key Features
- SMS reminders for calendar events
- Integration with calendar alarm system
- Automatic SMS sending based on event reminders

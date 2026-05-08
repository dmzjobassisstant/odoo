# Requirements: sms_twilio

## Module Overview
- **Name**: Twilio SMS
- **Version**: 1.0
- **Category**: Hidden/Tools
- **Depends**: `sms`
- **License**: LGPL-3

## Description
Send SMS messages using Twilio as the SMS provider.

## Dependencies

### Internal Dependencies
- `sms` - Base SMS module

## Models

### Core Models
| Model | Description |
|-------|-------------|
| `sms.sms` | Extended with Twilio delivery webhook |
| `sms.tracker` | Extended with Twilio tracking |
| `sms.twilio.number` | Twilio phone number management |
| `res.company` | Extended with Twilio credentials |
| `res.config.settings` | Extended with Twilio configuration |
| `sms.composer` | Extended with Twilio sending |
| `mail.notification` | Extended with Twilio status |

## Views & Security

### Data Files
None specific

### View Files
- `views/res_config_settings_views.xml` - Twilio configuration
- `views/sms_sms_views.xml` - SMS views with Twilio info
- `wizard/sms_twilio_account_manage_views.xml` - Twilio account management

### Security Files
- `security/ir.model.access.csv` - Access control

## Key Features
- Twilio as SMS provider
- Twilio account configuration
- Twilio phone number management
- Delivery status webhook from Twilio
- SMS sending via Twilio API
- Twilio-specific tracking

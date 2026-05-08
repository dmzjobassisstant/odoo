# Requirements: sms

## Module Overview
- **Name**: SMS gateway
- **Version**: 3.0
- **Category**: Sales/Sales
- **Depends**: `base`, `iap_mail`, `mail`, `phone_validation`
- **Auto-install**: True
- **License**: LGPL-3

## Description
SMS text messaging framework using In App Purchase Odoo platform.

## Dependencies

### Internal Dependencies
- `base` - Base module
- `iap_mail` - IAP mail integration
- `mail` - Mail/messaging framework
- `phone_validation` - Phone number validation

## Models

### Core Models
| Model | Description |
|-------|-------------|
| `sms.sms` | Outgoing SMS - main SMS entity |
| `sms.template` | SMS Template for reusable messages |
| `sms.tracker` | SMS delivery tracking |
| `iap.account` | IAP account for SMS service |
| `mail.thread` | Extended with SMS sending capability |
| `mail.message` | Extended with SMS notification |
| `mail.notification` | Extended for SMS delivery status |
| `mail.followers` | Extended for SMS following |
| `res.partner` | Extended with SMS fields |
| `res.company` | Extended with SMS configuration |
| `ir.actions.server` | Extended with SMS action |
| `ir.model` | Extended for SMS API access |

## SMS States
- `outgoing` - In Queue
- `process` - Processing
- `pending` - Sent/Waiting
- `sent` - Delivered
- `error` - Error
- `canceled` - Cancelled

## Failure Types
- `sms_number_missing` - Missing Number
- `sms_number_format` - Wrong Number Format
- `sms_country_not_supported` - Country Not Supported
- `sms_registration_needed` - Country-specific Registration
- `sms_credit` - Insufficient Credit
- `sms_server` - Server Error
- `sms_acc` - Unregistered Account
- `sms_blacklist` - Blacklisted
- `sms_duplicate` - Duplicate
- `sms_optout` - Opted Out

## Views & Security

### Data Files
- `data/iap_service_data.xml` - IAP service configuration
- `data/ir_cron_data.xml` - Scheduled SMS sending

### View Files
- `wizard/sms_account_code_views.xml`
- `wizard/sms_account_phone_views.xml`
- `wizard/sms_account_sender_views.xml`
- `wizard/sms_composer_views.xml`
- `wizard/sms_template_preview_views.xml`
- `wizard/sms_template_reset_views.xml`
- `views/ir_actions_server_views.xml`
- `views/mail_notification_views.xml`
- `views/res_config_settings_views.xml`
- `views/res_partner_views.xml`
- `views/iap_account_views.xml`
- `views/sms_sms_views.xml`
- `views/sms_template_views.xml`

### Security Files
- `security/ir.model.access.csv` - Access control
- `security/sms_security.xml` - SMS security rules

## Key Features
- SMS sending via IAP (In App Purchase)
- SMS templates with personalization
- Phone number validation and formatting
- Delivery status tracking
- SMS tracking via UUID
- Blacklist management
- Resend failed SMS
- Batch SMS sending
- Composer for ad-hoc SMS
- Scheduled SMS sending via cron
- Mail thread SMS integration
- Partner SMS notification preferences

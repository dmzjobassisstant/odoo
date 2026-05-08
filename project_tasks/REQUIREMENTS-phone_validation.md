# phone_validation — Requirements

## Module Overview
- **Name**: Phone Numbers Validation
- **Version**: 2.1
- **Category**: Hidden
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Status**: Auto-install

## Dependencies
- `base`
- `mail`

## Core Functionality
Validates and formats phone numbers according to destination country. Manages phone blacklist for excluding numbers from messaging.

## Key Models
- `phone.blacklist` — Stores blacklisted phone numbers; inherits `mail.thread` for tracking
- `res.partner` — Extended with phone validation
- `mail.thread.phone` — Mixin for phone handling and blacklist

## Key Features
- Phone number formatting/sanitation per country
- Phone blacklist management (add/remove numbers)
- Blacklist tracking with `mail.thread` mixin
- E164 format support
- Search by sanitized phone number

## Data Files
- `security/ir.model.access.csv`
- `views/phone_blacklist_views.xml`
- `views/res_partner_views.xml`
- `wizard/phone_blacklist_remove_view.xml`

## Constraints
- Unique constraint on `number` field in `phone.blacklist`
- Numbers must be E164 formatted

## Security
- Access control via `ir.model.access.csv`

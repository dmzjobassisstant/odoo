# Requirements: auth_totp_mail

## Module Overview

- **Name**: 2FA Invite mail
- **Category**: Extra Tools
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Auto-install**: True

## Depends

- `auth_totp`
- `mail`

## External Dependencies

None specified in manifest.

## Data Files

- `data/ir_action_data.xml`
- `data/mail_template_data.xml`
- `data/security_notifications_template.xml`
- `views/res_config_settings_views.xml`
- `views/res_users_views.xml`
- `views/templates.xml`

## Assets

- `web.assets_tests`: `auth_totp_mail/static/tests/**/*`

## Notes

- Allows users to invite another user to enable Two-Factor Authentication by sending an email
- Email redirects the target user to security settings (internal users go to user security settings, portal users go to portal security settings)
- Depends on `mail` module for email delivery
- Auto-installs alongside `auth_totp` to provide the invitation flow

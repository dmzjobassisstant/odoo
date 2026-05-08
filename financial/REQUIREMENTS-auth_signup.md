# Requirements: auth_signup

## Module Overview

- **Name**: Signup
- **Version**: 1.0
- **Category**: Hidden/Tools
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Auto-install**: True
- **Bootstrap**: True

## Depends

- `base_setup`
- `mail`
- `web`

## External Dependencies

None specified in manifest.

## Data Files

- `data/ir_config_parameter_data.xml`
- `data/ir_cron_data.xml`
- `data/mail_template_data.xml`
- `views/res_config_settings_views.xml`
- `views/res_users_views.xml`
- `views/auth_signup_login_templates.xml`
- `views/auth_signup_templates_email.xml`
- `views/webclient_templates.xml`

## Assets

- `web.assets_frontend`: `auth_signup/static/**/*`

## Models

### `res.users` (inherited)

**Fields**:
- `state` — computed field: `'new'` (Invited) if no `login_date`, else `'active'` (Confirmed); searchable by selection

**Key Methods**:

- `signup(values, token=None)` — handles three scenarios:
  1. **Signup with token** — invited user (with or without existing user record): invalidates token, writes values, sends invite notification for internal users
  2. **Signup with token + existing user** — password reset flow
  3. **Signup without token** — external (b2c) signup: creates user from template; requires `auth_signup.invitation_scope` = `b2c`

- `_get_signup_invitation_scope()` — returns `auth_signup.invitation_scope` config param (`b2b` or `b2c`)

- `_signup_create_user(values)` — checks uninvited users can only signup if scope is `b2c`; creates user via `_create_user_from_template`

- `_create_user_from_template(values)` — copies `base.template_portal_user_id` as template with provided values; raises `SignupError` on failure

- `reset_password(login)` — finds user by login or email domain, calls `action_reset_password`

- `action_reset_password()` — wraps `_action_reset_password`; handles `MailDeliveryException` for connection errors

- `_action_reset_password(signup_type)` — prepares signup tokens on partner records, sends password reset/signup email (internal users get `auth_signup.set_password_email` template; portal users get `auth_signup.portal_set_password_email` template; fallback renders `auth_signup.reset_password_email` via qweb); returns notification action

- `send_unregistered_user_reminder(after_days=5, batch_size=100)` — cron-actionable method; finds users created in last N days with no login, groups by inviter, sends `mail_template_data_unregistered_users` email

- `web_create_users(emails)` — creates new internal users from email list; reactivates inactive users and sends signup invitation

- `create(vals_list)` — overridden: after creating users, automatically sends signup invitation email unless `no_reset_password` context is set; catches `MailDeliveryException` to cancel partner signup on failure

- `write(vals)` — if `active` set to False, cancels pending partner signup

- `_ondelete_signup_cancel()` — ondelete hook: cancels pending partner signup when user is deleted

## Configuration Parameters

- `auth_signup.invitation_scope` — `b2b` (default, invitation-only) or `b2c` (anyone can sign up)
- `base.template_portal_user_id` — ID of template user for portal signup

## Notes

- Uses `mail` module for sending signup/reset password emails
- Cron job `ir_cron_data.xml` handles unregistered user reminders
- `bootstrap=True` means it can pre-configure data during module installation

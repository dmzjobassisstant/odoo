# Requirements: auth_timeout

## Module Overview

- **Name**: Auth Timeout
- **Category**: Hidden/Tools
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Auto-install**: No

## Depends

- `auth_totp`
- `auth_totp_mail`
- `auth_passkey`
- `bus`

## External Dependencies

None specified in manifest.

## Data Files

- `views/login_templates.xml`
- `views/res_groups_views.xml`

## Assets

- `web.assets_backend`: `auth_timeout/static/src/services/check_identity/*`
- `web.assets_frontend`: `auth_timeout/static/src/services/check_identity/*`, `auth_timeout/static/src/scss/auth_timeout.scss`
- `web.assets_tests`: `auth_timeout/static/tests/tours/**/*`

## Models

### `auth_totp.device` (inherited in `auth_totp` module)

**Key Methods**:

- `_get_trusted_device_age()` — overridden to respect `auth_timeout` lock timeouts for MFA; returns the minimum of the default trusted device age and any user-specific MFA lock timeout values from `_get_lock_timeouts().get("lock_timeout")`

### `res.users` (inherited)

- `_get_lock_timeouts()` — provides lock timeout thresholds by MFA type (called by `auth_totp.device._get_trusted_device_age()`)

### `ir_http` (inherited)

- Handles timeout-related HTTP behavior

### `ir_websocket` (inherited)

- Handles timeout via websocket mechanism

### `res_groups` (inherited)

- Group configuration for timeout policies

## Notes

- Enforces re-authentication after user inactivity
- Works with `auth_totp`, `auth_totp_mail`, and `auth_passkey` — users authenticated via TOTP or passkey are subject to session timeout
- Uses `bus` module for real-time timeout notifications
- Trusted device age for TOTP is capped by the user's lock timeout when MFA is active

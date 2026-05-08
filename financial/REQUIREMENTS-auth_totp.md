# Requirements: auth_totp

## Module Overview

- **Name**: Two-Factor Authentication (TOTP)
- **Category**: Extra Tools
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Auto-install**: True

## Depends

- `web`

## External Dependencies

None specified in manifest.

## Data Files

- `security/security.xml`
- `security/ir.model.access.csv`
- `data/ir_action_data.xml`
- `views/res_users_views.xml`
- `views/templates.xml`
- `wizard/auth_totp_wizard_views.xml`

## Assets

- `web.assets_tests`: `auth_totp/static/tests/**/*`
- `web.assets_backend`: `auth_totp/static/src/**/*`

## Models

### `auth_totp.device` (inherited from `res.users.apikeys`)

Abstract-like model for trusted TOTP devices. Uses `_name` = `auth_totp.device` but inherits functionality from `res.users.apikeys`.

**Key Methods**:

- `_check_credentials_for_uid(*, scope, key, uid)` — checks device key matches scope for a given user ID; returns True if valid
- `_get_trusted_device_age()` — returns trusted device cookie lifetime in seconds; reads `auth_totp.trusted_device_age` ir.config_parameter (default: `TRUSTED_DEVICE_AGE_DAYS` = 30 days); converts days to seconds; handles invalid/zero values

**Configuration**:

- `auth_totp.trusted_device_age` — number of days a trusted device remains valid (integer; <= 0 means no trust)

## Notes

- TOTP code entry is required at login via authenticator apps (Google Authenticator, etc.)
- When TOTP is enabled, password-based RPC access is blocked; users must use API keys instead
- `auth_totp.device` inherits from `res.users.apikeys` and uses its `_check_credentials` mechanism but with a separate table/model to distinguish trusted devices from API keys

# Requirements: auth_password_policy

## Module Overview

- **Name**: Password Policy
- **Category**: Hidden/Tools
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Auto-install**: No

## Depends

- `base_setup`
- `web`

## External Dependencies

None specified in manifest.

## Data Files

- `data/defaults.xml`
- `views/res_users.xml`
- `views/res_config_settings_views.xml`

## Assets

- `web.assets_backend`: `auth_password_policy/static/src/**/*`
- `web.assets_frontend`: `auth_password_policy/static/src/css/password_field.css`, `auth_password_policy/static/src/password_policy.js`

## Models

### `res.users` (inherited)

**Methods**:

- `get_password_policy()` — returns `{'minlength': int}` from `auth_password_policy.minlength` ir.config_parameter (default 0)

- `_set_password()` — validates password via `_check_password_policy` before calling super

- `_check_password_policy(passwords)` — validates all passwords against `auth_password_policy.minlength`; raises `UserError` if any password is shorter than minimum length

## Configuration

- `auth_password_policy.minlength` — minimum password character length (integer, default 0 = no policy)

## Notes

- Only enforces minimum length constraint
- No complexity requirements (character classes, special chars, etc.)

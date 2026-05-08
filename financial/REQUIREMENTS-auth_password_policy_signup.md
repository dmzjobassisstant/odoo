# Requirements: auth_password_policy_signup

## Module Overview

- **Name**: Password Policy support for Signup
- **Category**: Hidden/Tools
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Auto-install**: True

## Depends

- `auth_password_policy`
- `auth_signup`

## External Dependencies

None specified in manifest.

## Data Files

- `views/signup_templates.xml`

## Assets

- `web.assets_frontend`:
  - `auth_password_policy_signup/static/src/public/**/*`
  - `auth_password_policy/static/src/password_meter.js`
  - `auth_password_policy/static/src/password_policy.js`

## Notes

Auto-installs to add signup-specific password policy frontend assets and templates. Integrates the password meter and policy UI into the `auth_signup` signup flow. Requires `auth_signup` for the signup flow.

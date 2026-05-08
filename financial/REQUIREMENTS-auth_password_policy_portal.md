# Requirements: auth_password_policy_portal

## Module Overview

- **Name**: Password Policy support for Signup (Portal)
- **Category**: Tools
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Auto-install**: True

## Depends

- `auth_password_policy`
- `portal`

## External Dependencies

None specified in manifest.

## Data Files

- `views/templates.xml`

## Notes

Auto-installs to add portal-specific password policy templates when `portal` is installed alongside `auth_password_policy`. Provides frontend templates for password policy enforcement on portal signup pages.

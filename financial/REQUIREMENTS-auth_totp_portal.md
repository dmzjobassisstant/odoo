# Requirements: auth_totp_portal

## Module Overview

- **Name**: TOTPortal (TOTP Portal)
- **Category**: Hidden
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Auto-install**: True

## Depends

- `portal`
- `auth_totp`

## External Dependencies

None specified in manifest.

## Data Files

- `security/security.xml`
- `views/templates.xml`

## Assets

- `web.assets_frontend`: `auth_totp_portal/static/src/**/*`
- `web.assets_tests`: `auth_totp_portal/static/tests/**/*`

## Notes

- Extends `auth_totp` with portal-specific TOTP frontend assets and templates
- Allows portal users to configure and use Two-Factor Authentication via their portal interface
- Templates provide the portal-facing TOTP setup and validation UI
- Security records in `security/security.xml` manage portal-specific access rights for TOTP

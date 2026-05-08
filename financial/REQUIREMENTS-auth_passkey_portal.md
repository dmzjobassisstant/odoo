# Requirements: auth_passkey_portal

## Module Overview

- **Name**: Passkeys Portal
- **Version**: 1.0
- **Category**: Hidden/Tools
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Auto-install**: True

## Depends

- `auth_passkey`
- `portal`

## External Dependencies

None specified in manifest.

## Data Files

- `views/templates.xml`

## Assets

- `web.assets_frontend`: `auth_passkey_portal/static/src/**`
- `web.assets_tests`: `auth_passkey_portal/static/tests/tours/*.js`

## Notes

This module extends `auth_passkey` with portal-specific passkey support (frontend assets and templates for portal users).

# resource_mail — Requirements

## Module Overview
- **Name**: Resource Mail
- **Version**: 1.0
- **Category**: Hidden
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Status**: Auto-install

## Dependencies
- `resource`
- `mail`

## Core Functionality
Integrates mail features developed in the `mail` module for use cases involving resources instead of users. Extends `resource.resource` model with mail-related capabilities.

## Key Models
- `resource.resource` — Inherited; extended with `color` and `im_status` (related to user_id)

## Key Features
- Color field for resources
- IM status integration (via related user_id)
- Avatar card data support for resources

## Assets
- `web.assets_backend`: All files from `resource_mail/static/src/**/*`
- `web.assets_unit_tests`: Tests from `resource_mail/static/tests/**/*`

## Security
- Standard Odoo access control (inherited from resource and mail)

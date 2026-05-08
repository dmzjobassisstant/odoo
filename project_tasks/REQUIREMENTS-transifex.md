# transifex — Requirements

## Module Overview
- **Name**: Transifex integration
- **Version**: 1.0
- **Category**: Hidden/Tools
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Status**: Installable

## Dependencies
- `base`
- `web`

## Core Functionality
Adds a link to edit translations in Transifex directly from Odoo's translation view. Reads `.tx/config` files to detect Transifex project configuration.

## Key Models
- `transifex.translation` — Abstract model for Transifex integration
- `transifex.code.translation` — Code translations via Transifex
- `ir.http` — Routing

## Key Features
- Transifex URL generation for translations
- Reads `.tx/config` files from addon paths
- Language code to ISO code mapping
- Project/module name resolution from Transifex config
- Translation dialog with Transifex link

## Data Files
- `data/transifex_data.xml`
- `views/code_translation_views.xml`
- `security/ir.model.access.csv`

## Assets
- `web.assets_backend`: Translation dialog XML, views JS and XML

## External Dependencies
- `configparser` — For parsing `.tx/config` files
- Transifex project_url config parameter

## Security
- Access control via `ir.model.access.csv`

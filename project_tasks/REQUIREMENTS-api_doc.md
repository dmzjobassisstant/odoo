# api_doc — Requirements

## Module Overview
- **Name**: API Documentation
- **Version**: 1.0
- **Category**: Hidden
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Status**: Auto-install

## Dependencies
- `web`

## Core Functionality
Provides a dynamic API documentation page at `/doc` URL. Generates documentation from the database listing models, fields, and methods. Includes a playground to run methods over HTTP with examples in various languages.

## Key Features
- Dynamic documentation generation from database models
- Model/field/method listing
- HTTP method playground
- Code examples in multiple programming languages
- Bootstrap-based UI

## Data Files
- `security/res_groups.xml`
- `views/docclient.xml`

## Assets (Custom Bundle `api_doc.assets`)
- FontAwesome CSS
- OWL framework (odoo_module.js, owl.js)
- Utils: functions, reactive, browser, timing, template_inheritance, registry, assets
- Bootstrap SCSS (variables, maps)
- API doc static files (XML, JS, CSS)

## Bootstrap
- `bootstrap: True` — Loads at earliest stage

## Security
- Group-based access control via `res_groups.xml`

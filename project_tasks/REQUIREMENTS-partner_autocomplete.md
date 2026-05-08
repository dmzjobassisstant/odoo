# partner_autocomplete — Requirements

## Module Overview
- **Name**: Partner Autocomplete
- **Version**: 1.1
- **Category**: Hidden/Tools
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Status**: Auto-install

## Dependencies
- `iap_mail`

## Core Functionality
Auto-completes partner company data (name, address, industry, VAT, etc.) by querying the IAP partner autocomplete service.

## Key Models
- `res.partner` — Extended with autocomplete methods
- `res.company` — Extended for autocomplete
- `iap.autocomplete.api` — IAP service for autocomplete requests
- `ir.http` — Routing/endpoint handling

## Key Features
- Search partner companies by name via IAP
- Auto-fill: country, state, industry, language, VAT
- Formatting of returned data to match Odoo records
- Integration with `iap_mail` for email-based autocomplete

## Data Files
- `views/res_company_views.xml`
- `views/res_config_settings_views.xml`
- `data/iap_service_data.xml`

## Assets
- `web.assets_backend`: SCSS, JS, XML from `partner_autocomplete/static/src/**/*`
- `web.jsvat_lib`: External lib from `partner_autocomplete/static/lib/**/*`
- `web.assets_unit_tests`: Tests from `partner_autocomplete/static/tests/**/*`

## External Dependencies
- `stdnum.eu.vat` — VAT number validation (via VIES)
- `iap` service endpoint for partner autocomplete

## Security
- Access control via `ir.model.access.csv`

# google_address_autocomplete Requirements

## Module Overview
- **Name**: Google Address Autocomplete
- **Category**: Hidden/Tools
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.0

## Dependencies
- `web`

## Description
Assists with automatic completion and suggestions when filling address fields using Google Places API.

## External Services / API
- Google Places API
  - Requires `google_places_api_key` configuration parameter

## Configuration Parameters (ir.config_parameter)
- `google_address_autocomplete.google_places_api_key` - Google Places API Key

## Assets
### Backend (web.assets_backend)
- `google_address_autocomplete/static/src/**/*`

### Frontend Dark (web.assets_web_dark)
- `google_address_autocomplete/static/src/address_autocomplete/google_address_autocomplete_dark.scss`

### Core Assets (web._assets_core)
- `google_address_autocomplete/static/src/address_autocomplete/google_address_autocomplete.scss`

### Tests (web.assets_tests)
- `google_address_autocomplete/static/tests/tours/*.js`

### Unit Tests (web.assets_unit_tests)
- `google_address_autocomplete/static/tests/**/*.test.js`

## Views
- `views/res_config_settings_views.xml`
- `views/res_partner_views.xml`
- `views/res_company_views.xml`

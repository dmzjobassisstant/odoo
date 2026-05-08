# Requirements: google_address_autocomplete

## Module Details
- **Name:** Google Address Autocomplete
- **Category:** Hidden/Tools
- **Version:** 1.0
- **Summary:** Assist with automatic completion & suggestions when filling address
- **Author:** Odoo S.A.
- **License:** LGPL-3

## Description
This module Auto complete the address data.

## Dependencies
- `web`

## Data Files
- `views/res_config_settings_views.xml`
- `views/res_partner_views.xml`
- `views/res_company_views.xml`

## Assets
- `web.assets_backend`: `google_address_autocomplete/static/src/**/*` (with dark mode variant removed)
- `web.assets_web_dark`: `google_address_autocomplete/static/src/address_autocomplete/google_address_autocomplete_dark.scss`
- `web._assets_core`: `google_address_autocomplete/static/src/address_autocomplete/google_address_autocomplete.scss`
- `web.assets_tests`: `google_address_autocomplete/static/tests/tours/*.js`
- `web.assets_unit_tests`: `google_address_autocomplete/static/tests/**/*.test.js`

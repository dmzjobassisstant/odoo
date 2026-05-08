# l10n_latam_base — LATAM Localization Base

## Module Details
- **Name:** LATAM Localization Base
- **Version:** 1.0
- **Category:** Accounting/Localizations
- **Author:** Odoo S.A., ADHOC SA
- **License:** LGPL-3

## Description
Adds "Identification Type" model extending VAT field functionality. Enables partners to be identified with fiscal tax ID (VAT), national documents, passports, foreign IDs, etc.

Generic Identification Types:
- VAT
- Passport
- Foreign ID

## Dependencies
### Odoo Modules
- `contacts`
- `base_vat`

## Data Files
- `data/res_country_group.xml`
- `data/l10n_latam.identification.type.csv`
- `views/res_partner_view.xml`
- `views/l10n_latam_identification_type_view.xml`
- `views/portal_address_templates.xml`
- `security/ir.model.access.csv`

## Assets
- `web.assets_frontend`: `l10n_latam_base/static/src/components/select_menu_wrapper/**.*`

## Hooks
- `post_init`: _set_default_identification_type

## Requirements Summary
- Base module for LATAM localizations
- Requires contacts and base_vat
- Identification types for Latin American countries

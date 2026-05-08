# Requirements: l10n_pe (Peru - Accounting)

## Module Details
- **Name**: Peru - Accounting
- **Version**: 3.1
- **Category**: Accounting/Localizations/Account Charts
- **Author**: Vauxoo, Odoo S.A.
- **License**: LGPL-3
- **Countries**: ['pe']
- **Website**: https://www.odoo.com/documentation/latest/applications/finance/fiscal_localizations/peru.html

## Dependencies
- `base_vat`
- `base_address_extended`
- `l10n_latam_base`
- `l10n_latam_invoice_document`
- `account_debit_note`
- `account`

## Auto-install
- `account`

## Data Files
- `security/ir.model.access.csv`
- `views/account_tax_view.xml`
- `views/portal_address_templates.xml`
- `views/res_bank_view.xml`
- `data/l10n_latam_document_type_data.xml`
- `data/res.city.csv`
- `data/l10n_pe.res.city.district.csv`
- `data/res_country_data.xml`
- `data/l10n_latam_identification_type_data.xml`
- `data/res.bank.csv`

## Assets
- `web.assets_frontend`: `l10n_pe/static/src/interactions/**/*`

## Demo
- `demo/demo_company.xml`
- `demo/demo_partner.xml`

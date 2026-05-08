# l10n_uy — Uruguay - Accounting

## Metadata
- **Name**: Uruguay - Accounting
- **Version**: 0.1
- **Author**: Uruguay l10n Team, Guillem Barba, ADHOC
- **Category**: Accounting/Localizations/Account Charts
- **Website**: https://www.odoo.com/documentation/latest/applications/finance/fiscal_localizations/uruguay.html
- **License**: LGPL-3

## Description
General Chart of Accounts for Uruguay.

This module adds accounting functionalities for the Uruguayan localization, representing the minimum required configuration for a company to operate in Uruguay under the regulations and guidelines provided by the DGI (Dirección General Impositiva).

Among the functionalities are:
- Uruguayan Generic Chart of Account
- Pre-configured VAT Taxes and Tax Groups
- Legal document types in Uruguay
- Valid contact identification types in Uruguay
- Configuration and activation of Uruguayan Currencies (UYU, UYI - Unidad Indexada Uruguaya)
- Frequently used default contacts already configured: DGI, Consumidor Final Uruguayo

## Dependencies
- `account`
- `l10n_latam_invoice_document`
- `l10n_latam_base`

## Auto-install
- `account`

## Data Files
- `data/account_tax_report_data.xml`
- `data/l10n_latam.document.type.csv`
- `data/l10n_latam_identification_type_data.xml`
- `data/res_partner_data.xml`
- `data/res_currency_data.xml`
- `views/account_tax_views.xml`

## Demo
- `demo/demo_company.xml`
- `demo/res_currency_rate_demo.xml`

# l10n_th — Thailand - Accounting

## Metadata
- **Name**: Thailand - Accounting
- **Version**: 2.0
- **Author**: Almacom (http://almacom.co.th/)
- **Category**: Accounting/Localizations/Account Charts
- **Website**: https://www.odoo.com/documentation/latest/applications/finance/fiscal_localizations/thailand.html
- **License**: LGPL-3

## Description
Chart of Accounts for Thailand.

Thai accounting chart and localization.

## Dependencies
- `account_qr_code_emv`
- `account`

## Auto-install
- `account`

## Data Files
- `data/account_tax_report_data.xml`
- `views/report_invoice.xml`

## Demo
- `demo/demo_company.xml`

## Hooks
- **post_init_hook**: `_preserve_tag_on_taxes`

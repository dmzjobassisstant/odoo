# l10n_sa — Saudi Arabia - Accounting

## Metadata
- **Name**: Saudi Arabia - Accounting
- **Version**: 2.2
- **Author**: Odoo S.A.
- **Category**: Accounting/Localizations/Account Charts
- **Website**: https://www.odoo.com/documentation/latest/applications/finance/fiscal_localizations/saudi_arabia.html
- **License**: LGPL-3

## Description
Saudi Arabia Accounting Basic Charts and Localization

Activates:
- Chart of Accounts
- Taxes
- VAT Return
- Withholding Return
- Fiscal Positions

## Dependencies
- `l10n_gcc_invoice`
- `account`
- `account_debit_note`

## Auto-install
- `account`

## Data Files
- `data/account_data.xml`
- `data/account_tax_report_data.xml`
- `data/account_tax_report_withholding_data.xml`
- `data/report_paperformat_data.xml`
- `views/account_move_views.xml`
- `views/report_invoice.xml`
- `wizard/account_debit_note.xml`
- `wizard/account_move_reversal_views.xml`
- `views/report_templates_views.xml`

## Demo
- `demo/demo_company.xml`

## Assets
- `web.report_assets_common`: `l10n_sa/static/src/scss/styles.scss`

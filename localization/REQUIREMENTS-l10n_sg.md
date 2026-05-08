# l10n_sg — Singapore - Accounting

## Metadata
- **Name**: Singapore - Accounting
- **Version**: 2.2
- **Author**: Tech Receptives
- **Category**: Accounting/Localizations/Account Charts
- **Website**: https://www.odoo.com/documentation/latest/applications/finance/fiscal_localizations/singapore.html
- **License**: LGPL-3

## Description
Singapore accounting chart and localization.

This module add, for accounting:
- The Chart of Accounts of Singapore
- Field UEN (Unique Entity Number) on company and partner
- Field PermitNo and PermitNoDate on invoice

## Dependencies
- `account_qr_code_emv`
- `account`

## Auto-install
- `account`

## Data Files
- `data/l10n_sg_chart_data.xml`
- `data/account_tax_report_data.xml`
- `views/account_invoice_view.xml`
- `views/res_bank_views.xml`
- `views/res_company_view.xml`
- `views/res_partner_view.xml`

## Demo
- `demo/demo_company.xml`

## Hooks
- **post_init_hook**: `_preserve_tag_on_taxes`

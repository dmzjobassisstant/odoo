# l10n_lu — Luxembourg - Accounting

## Module Details
- **Name:** Luxembourg - Accounting
- **Country:** Luxembourg (lu)
- **Version:** 2.2
- **Author:** Odoo S.A., ADN, ACSONE SA/NV
- **License:** LGPL-3
- **Category:** Accounting/Localizations/Account Charts

## Dependencies
- `account`
- `base_iban`
- `base_vat`
- `account_edi_ubl_cii`

## Auto-Install
- `account`

## Features
- Luxembourg Official Chart of Accounts (law of June 2009 + 2015 chart and Taxes)
- Tax Code Chart for Luxembourg
- Main taxes used in Luxembourg
- Default fiscal position for local, intracom, extracom
- Post-init hook: `_post_init_hook`

## Data Files
- `data/account.account.tag.csv`
- `data/l10n_lu_chart_data.xml`
- `data/tax_report/section_1.xml`
- `data/tax_report/section_2.xml`
- `data/tax_report/sections_34.xml`
- `data/tax_report/tax_report.xml`

## Demo
- `demo/demo_company.xml`

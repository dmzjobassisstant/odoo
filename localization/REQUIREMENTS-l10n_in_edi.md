# l10n_in_edi — Indian - E-invoicing

## Module Details
- **Name:** Indian - E-invoicing
- **Version:** 1.03.00
- **Category:** Accounting/Localizations/EDI
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Country:** IN

## Description
E-invoicing for India via API to the government. Uses "Tera Software Limited" as GSP.

## Dependencies
### Odoo Modules
- `account_edi`
- `l10n_in`

## Data Files
- `security/ir.model.access.csv`
- `views/account_move_views.xml`
- `views/edi_pdf_report.xml`
- `views/res_config_settings_views.xml`
- `wizard/l10n_in_edi_cancel_views.xml`

## Demo Data
- `demo/demo_company.xml`

## Requirements Summary
- Requires l10n_in (Indian base accounting)
- Requires account_edi
- GSP: Tera Software Limited

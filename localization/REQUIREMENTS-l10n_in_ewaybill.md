# l10n_in_ewaybill — Indian - E-waybill

## Module Details
- **Name:** Indian - E-waybill
- **Version:** 2.0
- **Category:** Accounting/Localizations
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Country:** IN

## Description
E-waybill submission through API to the government. Uses "Tera Software Limited" as GSP.

## Dependencies
### Odoo Modules
- `l10n_in`

## Data Files
- `security/ir.model.access.csv`
- `security/ir_rules.xml`
- `data/ewaybill_type_data.xml`
- `views/l10n_in_ewaybill_views.xml`
- `views/account_move_views.xml`
- `views/edi_pdf_report.xml`
- `views/res_config_settings_views.xml`
- `wizard/l10n_in_ewaybill_cancel_views.xml`
- `report/ewaybill_report_views.xml`
- `report/ewaybill_report.xml`

## Demo Data
- `demo/demo_company.xml`

## Requirements Summary
- Requires l10n_in (Indian base accounting)
- GSP: Tera Software Limited
- Not auto_install (company can be service industry)

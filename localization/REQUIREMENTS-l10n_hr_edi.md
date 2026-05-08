# l10n_hr_edi — Croatia - e-invoicing

## Module Details
- **Name:** Croatia - e-invoicing
- **Version:** 1.0
- **Category:** Accounting/Localizations/Reporting
- **Author:** Odoo S.A.
- **License:** OEEL-1

## Description
e-invoicing for Croatia

## Dependencies
### Odoo Modules
- `l10n_hr`
- `account_edi_ubl_cii`
- `account_peppol`

## Hooks
- `post_init`: post_init

## Data Files
- `data/cron.xml`
- `data/l10n_hr.kpd.category.csv`
- `security/ir.model.access.csv`
- `data/l10n_hr_tax_category.xml`
- `views/account_journal_views.xml`
- `views/account_move_views.xml`
- `views/account_tax_views.xml`
- `views/l10n_hr_kpd_category_views.xml`
- `views/product_views.xml`
- `views/report_invoice_views.xml`
- `views/res_config_settings_views.xml`
- `views/res_partner_views.xml`
- `wizard/l10n_hr_edi_mojeracun_reject_wizard_views.xml`

## Demo Data
- `demo/demo_company.xml`

## Requirements Summary
- Requires l10n_hr (Croatia base accounting)
- EDI/UBL support via account_edi_ubl_cii
- Peppol support via account_peppol

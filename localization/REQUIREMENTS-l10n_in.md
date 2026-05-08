# l10n_in — Indian - Accounting

## Module Details
- **Name:** Indian - Accounting
- **Version:** 2.0
- **Category:** Accounting/Localizations/Account Charts
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Country:** IN

## Description
Indian Accounting: Chart of Account with support for:
- Indian Chart Of Accounts - Standard
- Indian Chart Of Accounts - Schedule VI (MCA revised format)

## Dependencies
### Odoo Modules
- `account_tax_python`
- `base_vat`
- `account_debit_note`
- `account`
- `iap`

### Auto-Install
- `account`

## Data Files
- `security/l10n_in_security.xml`
- `security/ir.model.access.csv`
- `data/iap_service_data.xml`
- `data/account.account.tag.csv`
- `data/l10n_in_chart_data.xml`
- `data/l10n_in.port.code.csv`
- `data/res_country_state_data.xml`
- `data/res_country_group.xml`
- `data/uom_data.xml`
- `data/res_partner_industry.xml`
- `data/account_cash_rounding.xml`
- `data/account_tax_report_tcs_data.xml`
- `data/account_tax_report_tds_data.xml`
- `data/l10n_in.section.alert.csv`
- `wizard/l10n_in_withhold_wizard.xml`
- `views/l10n_in_pan_entity_views.xml`
- `views/l10n_in_section_alert_views.xml`
- `views/account_account_views.xml`
- `views/account_invoice_views.xml`
- `views/account_move_line_views.xml`
- `views/account_payment_views.xml`
- `views/account_journal_views.xml`
- `views/res_config_settings_views.xml`
- `views/product_template_view.xml`
- `views/port_code_views.xml`
- `views/res_company_views.xml`
- `views/report_invoice.xml`
- `views/res_country_state_view.xml`
- `views/res_partner_views.xml`
- `views/account_tax_views.xml`
- `views/uom_uom_views.xml`

## Demo Data
- `demo/product_demo.xml`
- `demo/demo_company.xml`

## Hooks
- `post_init`: post_init

## Assets
- `web.assets_backend`: `l10n_in/static/src/components/**/*`, `l10n_in/static/src/helpers/*.js`
- `web.assets_frontend`: `l10n_in/static/src/components/tests_shared_js_python/*`, `l10n_in/static/src/helpers/*.js`

## Requirements Summary
- Indian localization with GST support
- Requires account_tax_python, base_vat, account_debit_note, iap
- Complex chart with Schedule VI support

# l10n_it_edi — Italy - E-invoicing

## Module Details
- **Name:** Italy - E-invoicing
- **Version:** 0.4
- **Category:** Accounting/Localizations/EDI
- **Author:** Odoo S.A.
- **License:** LGPL-3

## Description
Italian E-invoice implementation (FatturaPA)

## Dependencies
### Odoo Modules
- `l10n_it`
- `account_edi_proxy_client`
- `account_debit_note`

### Auto-Install
- `l10n_it`

## Data Files
- `security/ir.model.access.csv`
- `data/account.account.tag.csv`
- `data/invoice_it_simplified_template.xml`
- `data/invoice_it_template.xml`
- `data/ir_cron.xml`
- `data/l10n_it.document.type.csv`
- `views/account_payment_method.xml`
- `views/account_tax_view.xml`
- `views/l10n_it_document_type.xml`
- `views/l10n_it_view.xml`
- `views/portal_address_templates.xml`
- `views/report_invoice.xml`
- `views/res_config_settings_views.xml`

## Demo Data
- `data/account_invoice_demo.xml`

## Hooks
- `post_init`: _l10n_it_edi_post_init
- `uninstall`: uninstall_hook

## Assets
- `web.assets_frontend`: `l10n_it_edi/static/src/interactions/**/*`
- `web.assets_tests`: `l10n_it_edi/static/tests/tours/*.js`

## Requirements Summary
- Requires l10n_it (Italy base accounting)
- Requires account_edi_proxy_client for EDI proxy
- FatturaPA format

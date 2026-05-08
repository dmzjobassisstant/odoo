# Requirements: l10n_pl_edi (Polish E-Invoicing FA(3))

## Module Details
- **Name**: Polish E-Invoicing FA(3)
- **Category**: Accounting/Localizations
- **Author**: Odoo S.A.
- **License**: LGPL-3

## Summary
Support for FA(3) electronic invoices in Poland via KSeF

## Dependencies
- `l10n_pl`
- `certificate`

## Auto-install
- `l10n_pl`

## Description
Export FA(3) compliant XML invoices and prepare for integration with KSeF.

## Data Files
- `views/account_move_views.xml`
- `views/res_config_settings_views.xml`
- `data/ir_cron_data.xml`
- `data/fa3_template.xml`

## Demo
- `demo/account_invoice_demo.xml`

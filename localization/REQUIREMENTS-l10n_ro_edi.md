# Requirements: l10n_ro_edi (Romania - E-invoicing)

## Module Details
- **Name**: Romania - E-invoicing
- **Version**: 1.0
- **Category**: Accounting/Localizations/EDI
- **Author**: Odoo
- **License**: LGPL-3

## Summary
E-Invoice implementation for Romania

## Dependencies
- `account_edi_ubl_cii`
- `l10n_ro`

## Auto-install
- True

## Description
E-invoice implementation for Romania

## Uninstall Hook
- `uninstall_hook`

## Data Files
- `data/ir_cron.xml`
- `security/ir.model.access.csv`
- `views/account_move_views.xml`
- `views/res_config_settings_views.xml`

## Assets
- `web.assets_backend`: `l10n_ro_edi/static/src/components/*`
- `web.tests_assets`: `l10n_ro_edi/static/tests/legacy/helpers/mock_server.js`

# Requirements: l10n_account_withholding_tax

**Module:** Withholding Tax on Payment  
**Version:** 1.0  
**License:** LGPL-3  
**Author:** Odoo S.A.  
**Category:** Accounting/Localizations  

## Description

Allows to register withholding taxes during the payment of an invoice or bill.

## Dependencies

- `account`

## Data Files

- `security/ir.model.access.csv`
- `views/account_payment_views.xml`
- `views/account_tax_views.xml`
- `views/report_payment_receipt_templates.xml`
- `views/res_config_settings.xml`
- `wizards/account_payment_register_views.xml`

## Assets

- `web.assets_backend`: `l10n_account_withholding_tax/static/src/helpers/*.js`
- `web.assets_frontend`: `l10n_account_withholding_tax/static/src/helpers/*.js`

## Installability

- `installable`: True

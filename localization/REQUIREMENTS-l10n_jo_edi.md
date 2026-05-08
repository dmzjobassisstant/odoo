# l10n_jo_edi — Jordan E-Invoicing

## Module Details
- **Name:** Jordan E-Invoicing
- **Version:** 1.0
- **Category:** Accounting/Localizations/EDI
- **Author:** Odoo S.A., Smart Way Business Solutions
- **License:** LGPL-3
- **Country:** JO

## Description
Electronic Invoicing for Jordan UBL 2.1 - integrates with JoFotara

## Dependencies
### Odoo Modules
- `account_edi_ubl_cii`
- `l10n_jo`

### Auto-Install
- `l10n_jo`

## Data Files
- `views/account_move_views.xml`
- `views/report_invoice.xml`
- `views/res_config_settings_views.xml`

## Demo Data
- `demo/demo_company.xml`

## Hooks
- `post_init`: _post_init_hook

## Requirements Summary
- Requires account_edi_ubl_cii and l10n_jo
- JoFotara integration

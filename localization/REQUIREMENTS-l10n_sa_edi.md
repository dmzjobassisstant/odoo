# l10n_sa_edi — Saudi Arabia - E-invoicing

## Metadata
- **Name**: Saudi Arabia - E-invoicing
- **Version**: 0.3
- **Author**: Odoo S.A.
- **Category**: Accounting/Localizations/EDI
- **License**: LGPL-3

## Description
E-invoice implementation for Saudi Arabia; Integration with ZATCA

## Dependencies
- `account_edi`
- `account_edi_ubl_cii`
- `l10n_sa`
- `base_vat`
- `certificate`

## Hooks
- **post_init_hook**: `_l10n_sa_edi_post_init`

## Data Files
- `security/ir.model.access.csv`
- `data/account_edi_format.xml`
- `data/ubl_21_zatca.xml`
- `data/res_country_data.xml`
- `wizard/l10n_sa_edi_otp_wizard.xml`
- `views/account_tax_views.xml`
- `views/account_journal_views.xml`
- `views/res_partner_views.xml`
- `views/res_company_views.xml`
- `views/res_config_settings_view.xml`
- `views/report_invoice.xml`

## Demo
- `demo/demo_company.xml`

## Assets
- `web.assets_backend`: `l10n_sa_edi/static/src/scss/form_view.scss`

# Requirements: l10n_pl (Poland - Accounting)

## Module Details
- **Name**: Poland - Accounting
- **Version**: 2.0
- **Category**: Accounting/Localizations/Account Charts
- **Author**: Odoo S.A., Grzegorz Grzelak (OpenGLOBE) (http://www.openglobe.pl)
- **License**: LGPL-3
- **Countries**: ['pl']
- **Website**: https://www.odoo.com/documentation/latest/applications/finance/fiscal_localizations.html

## Dependencies
- `base_iban`
- `base_vat`
- `account`
- `account_edi_ubl_cii`

## Auto-install
- `account`

## Description
This is the module to manage the accounting chart and taxes for Poland in Odoo.

To jest moduł do tworzenia wzorcowego planu kont, podatków, obszarów podatkowych i rejestrów podatkowych. Moduł ustawia też konta do kupna i sprzedaży towarów zakładając, że wszystkie towary są w obrocie hurtowym.

Niniejszy moduł jest przeznaczony dla odoo 8.0. Wewnętrzny numer wersji OpenGLOBE 1.02

## Post-init Hook
- `_preserve_tag_on_taxes`

## Data Files
- `security/ir.model.access.csv`
- `data/l10n_pl.l10n_pl_tax_office.csv`
- `data/account.account.tag.csv`
- `data/account_tax_report_data.xml`
- `views/account_move_views.xml`
- `views/product_views.xml`
- `views/res_config_settings_views.xml`
- `views/res_partner_views.xml`

## Demo
- `demo/demo_company.xml`

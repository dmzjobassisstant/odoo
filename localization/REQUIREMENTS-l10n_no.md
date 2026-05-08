# Requirements: l10n_no (Norway - Accounting)

## Module Details
- **Name**: Norway - Accounting
- **Version**: 2.1
- **Category**: Accounting/Localizations/Account Charts
- **Author**: Rolv Råen
- **License**: LGPL-3
- **Countries**: ['no']
- **Website**: https://www.odoo.com/documentation/latest/applications/finance/fiscal_localizations.html

## Dependencies
- `base_iban`
- `base_vat`
- `account`
- `account_edi_ubl_cii`

## Auto-install
- `account`

## Description
This is the module to manage the accounting chart for Norway in Odoo.

Updated for Odoo 9 by Bringsvor Consulting AS

## Post-init Hook
- `_preserve_tag_on_taxes`

## Data Files
- `data/account_tax_report_data.xml`
- `views/account_tax.xml`
- `views/res_partner_views.xml`
- `views/res_company_views.xml`

## Demo
- `demo/demo_company.xml`

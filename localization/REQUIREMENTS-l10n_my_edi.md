# Requirements: l10n_my_edi (Malaysia - E-invoicing)

## Module Details
- **Name**: Malaysia - E-invoicing
- **Version**: 1.0
- **Category**: Accounting/Localizations/EDI
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Countries**: ['my']

## Summary
E-invoicing using MyInvois

## Dependencies
- `l10n_my`
- `l10n_my_ubl_pint`
- `account_edi_proxy_client`

## Description
This modules allows the user to send their invoices to the MyInvois system.

## Data Files
- `data/ir_cron.xml`
- `data/l10n_my_edi.industry_classification.csv`
- `security/ir.model.access.csv`
- `security/myinvois_security.xml`
- `views/account_move_view.xml`
- `views/account_tax_view.xml`
- `views/l10n_my_edi_industrial_classification_views.xml`
- `views/myinvois_document_views.xml`
- `views/product_template_view.xml`
- `views/report_invoice.xml`
- `views/res_company_view.xml`
- `views/res_config_settings_view.xml`
- `views/res_partner_view.xml`
- `views/account_portal_templates.xml`
- `wizard/myinvois_consolidate_invoice_wizard.xml`
- `wizard/myinvois_document_status_update_wizard.xml`

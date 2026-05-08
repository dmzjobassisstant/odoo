# l10n_hu_edi — Hungary - E-invoicing

## Module Details
- **Name:** Hungary - E-invoicing
- **Version:** 1.0.0
- **Category:** Accounting/Localizations/EDI
- **Author:** DO Tech (OdooTech Zrt.), BDSC Business Consulting Kft. & Odoo S.A.
- **License:** LGPL-3

## Description
- Electronically report invoices to the NAV (Hungarian Tax Agency) when issuing physical (paper) invoices.
- Perform the Tax Audit Export (Adóhatósági Ellenőrzési Adatszolgáltatás) in NAV 3.0 format.

## Dependencies
### Odoo Modules
- `account_debit_note`
- `base_iban`
- `l10n_hu`

### Auto-Install
- `l10n_hu`

## Data Files
- `security/ir.model.access.csv`
- `data/uom.uom.csv`
- `data/account_cash_rounding.xml`
- `data/template_requests.xml`
- `data/template_invoice.xml`
- `data/ir_cron.xml`
- `views/report_templates.xml`
- `views/report_invoice.xml`
- `views/account_move_views.xml`
- `views/product_template_views.xml`
- `views/account_tax_views.xml`
- `views/uom_uom_views.xml`
- `views/res_partner_views.xml`
- `views/res_company_views.xml`
- `views/res_config_settings_views.xml`
- `wizard/l10n_hu_edi_cancellation.xml`
- `wizard/l10n_hu_edi_tax_audit_export.xml`

## Demo Data
- `demo/demo_partner.xml`

## Hooks
- `post_init`: post_init

## Requirements Summary
- Requires l10n_hu (Hungary base accounting)
- Requires base_iban for IBAN support
- NAV 3.0 format tax audit export

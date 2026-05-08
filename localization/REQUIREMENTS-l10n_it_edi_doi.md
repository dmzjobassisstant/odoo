# l10n_it_edi_doi — Italy - Declaration of Intent

## Module Details
- **Name:** Italy - Declaration of Intent
- **Version:** 0.1
- **Category:** Accounting/Localizations
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Country:** IT

## Description
Add support for Declaration of Intent (Dichiarazione di Intento) to Italian localization

## Dependencies
### Odoo Modules
- `l10n_it_edi`
- `sale`

## Data Files
- `security/ir.model.access.csv`
- `data/invoice_it_template.xml`
- `views/l10n_it_edi_doi_declaration_of_intent_views.xml`
- `views/account_move_views.xml`
- `views/report_invoice.xml`
- `views/res_partner_views.xml`
- `views/sale_ir_actions_report_templates.xml`
- `views/sale_order_views.xml`

## Hooks
- `post_init`: _l10n_it_edi_doi_post_init

## Requirements Summary
- Requires l10n_it_edi and sale
- Dichiarazione di Intento support

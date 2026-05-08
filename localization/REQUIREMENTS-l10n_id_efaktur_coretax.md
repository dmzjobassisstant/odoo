# l10n_id_efaktur_coretax — Indonesia E-faktur (Coretax)

## Module Details
- **Name:** Indonesia E-faktur (Coretax)
- **Version:** 1.0
- **Category:** Accounting/Localizations/EDI
- **Author:** Odoo S.A.
- **License:** LGPL-3

## Description
E-invoicing feature provided by DJP (Indonesian Tax Office). As of January 1st 2025, Indonesia is using CoreTax system, which changes the file format and content of E-Faktur from CSV to XML.

## Dependencies
### Odoo Modules
- `l10n_id`

### Auto-Install
- True

## Data Files
- `data/l10n_id_efaktur_coretax.product.code.csv`
- `data/l10n_id_efaktur_coretax.uom.code.csv`
- `data/uom.uom.csv`
- `data/efaktur_templates.xml`
- `data/ir_action.xml`
- `security/ir.model.access.csv`
- `security/ir_rule.xml`
- `views/product_template.xml`
- `views/product_code.xml`
- `views/uom_code.xml`
- `views/res_partner.xml`
- `views/account_move.xml`
- `views/efaktur_document.xml`
- `views/uom_uom.xml`

## Requirements Summary
- Requires l10n_id (Indonesian base accounting)
- E-faktur with CoreTax XML format (replaces CSV)
- TaxBase factor change to 11/12 for 11% effective rate

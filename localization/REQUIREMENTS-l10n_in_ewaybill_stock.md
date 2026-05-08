# l10n_in_ewaybill_stock — Indian - E-waybill Stock

## Module Details
- **Name:** Indian - E-waybill Stock
- **Version:** 1.1
- **Category:** Accounting/Localizations/EDI
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Country:** IN

## Description
Create E-waybill from Inventory App without generating an invoice

## Dependencies
### Odoo Modules
- `l10n_in_stock`
- `l10n_in_ewaybill`

### Auto-Install
- True

## Data Files
- `security/ir.model.access.csv`
- `data/ewaybill_type_data.xml`
- `views/l10n_in_ewaybill_views.xml`
- `views/stock_picking_views.xml`
- `report/ewaybill_report_inherit.xml`

## Requirements Summary
- Requires l10n_in_stock and l10n_in_ewaybill
- E-waybill generation from stock pickings

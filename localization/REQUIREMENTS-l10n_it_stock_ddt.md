# l10n_it_stock_ddt — Italy - Stock DDT

## Module Details
- **Name:** Italy - Stock DDT
- **Version:** 0.1
- **Category:** Accounting/Localizations/EDI
- **Author:** Odoo S.A.
- **License:** LGPL-3

## Description
Documento di Trasporto (DDT) - Italian delivery document for goods transfer. Prints DDT instead of delivery slip with value, transportation reason, carrier info. Links DDTs to invoices for FatturaPA XML export.

## Dependencies
### Odoo Modules
- `l10n_it_edi`
- `stock_delivery`
- `stock_account`

### Auto-Install
- True

## Data Files
- `report/l10n_it_ddt_report.xml`
- `views/stock_picking_views.xml`
- `views/account_invoice_views.xml`
- `data/l10n_it_ddt_template.xml`

## Hooks
- `post_init`: _create_picking_seq

## Requirements Summary
- Requires l10n_it_edi, stock_delivery, stock_account
- DDT (Documento di Trasporto) for Italian goods transport

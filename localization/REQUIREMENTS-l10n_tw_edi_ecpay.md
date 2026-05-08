# l10n_tw_edi_ecpay — Taiwan - E-invoicing

## Metadata
- **Name**: Taiwan - E-invoicing
- **Version**: 1.0
- **Author**: Odoo S.A.
- **Category**: Accounting/Localizations/EDI
- **License**: LGPL-3

## Description
Taiwan - E-invoicing

This module allows the user to send their invoices to the Ecpay system.

## Dependencies
- `l10n_tw`
- `base_vat`

## Installable
- `True`

## Hooks
- **uninstall_hook**: `uninstall_hook`

## Data Files
- `security/ir.model.access.csv`
- `views/res_config_setting_view.xml`
- `views/account_tax.xml`
- `views/account_move_view.xml`
- `views/account_move_reversal_view.xml`
- `views/l10n_tw_edi_invoice_cancel_view.xml`
- `views/l10n_tw_edi_invoice_print_view.xml`

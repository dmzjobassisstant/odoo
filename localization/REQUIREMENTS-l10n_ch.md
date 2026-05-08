# Requirements for l10n_ch

## Module Info
- **Name:** Switzerland - Accounting
- **Category:** Accounting/Localizations/Account Charts
- **Countries:** CH
- **Version:** 11.3
- **Author:** Odoo S.A.
- **License:** LGPL-3

## Dependencies (external)
- `account`
- `account_edi_ubl_cii`
- `base_iban`
- `l10n_din5008`

## Auto-installs
- `account`

## Features
- Swiss chart of account (Swiss PME/KMU 2015)
- Taxes
- QR-bill generation on invoices
- QR-bill attached when printing or sending by mail

## Hooks
- `post_init_hook`: `post_init`

# Requirements: l10n_test_pos_qr_payment

**Module:** POS QR Tests  
**Version:** 1.0  
**License:** LGPL-3  
**Author:** Odoo S.A.  
**Category:** Sales/Point of Sale  
**Sequence:** 9876  

## Description

This module contains tests related to point of sale QR code payment.  
It tests all the supported qr codes: SEPA, Swiss QR and EMV QR (using the hk and br implementation).

## Dependencies

- `point_of_sale`
- `account_qr_code_sepa`
- `l10n_be`
- `l10n_ch`
- `l10n_hk`
- `l10n_br`

## Assets

- `web.assets_tests`: `l10n_test_pos_qr_payment/static/tests/**/*`

## Installability

- `installable`: True

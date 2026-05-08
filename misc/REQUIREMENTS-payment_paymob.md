# Module: payment_paymob
**Name:** Payment Provider: Paymob
**Version:** 1.0
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'paymob'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `paymob_account_country_id` | Many2one | Yes | Account country (`res.country`) |
| `paymob_public_key` | Char | Yes | Paymob public key |
| `paymob_secret_key` | Char | Yes | Paymob secret key |
| `paymob_hmac_key` | Char | Yes | Paymob HMAC key |
| `paymob_api_key` | Char | Yes | Paymob API key |

## Supported Countries / API Prefixes
AE (uae), EG (accept), OM (oman), PK (pakistan), SA (ksa)

## Default Payment Method Codes
`card`

## Supported Payment Methods (via mapping)
VPC, MIGS, mobile_wallet_eg, kiosk, halan, sympl, valu, aman, souhoola, contact, premium_card, forsa, tabby, tamara, stcpay, omannet, easypaisa, jazzcash

## Security
No separate security file.

## Controllers
- `main.py`: Handles Paymob payment processing and webhooks

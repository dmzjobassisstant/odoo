# Module: payment_redsys
**Name:** Payment Provider: Redsys
**Version:** (inherited from payment)
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'redsys'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `redsys_merchant_code` | Char | Yes | Redsys merchant code |
| `redsys_merchant_terminal` | Char | Yes | Redsys merchant terminal |
| `redsys_secret_key` | Char | Yes | Redsys secret key |

## Default Payment Method Codes
`card`, `visa`, `mastercard`, `amex`, `diners`, `jcb`, `bizum`

## Supported Payment Methods (via mapping)
bizum, card, visa, mastercard, amex, diners, jcb

## Security
No separate security file.

## Controllers
- `main.py`: Handles Redsys payment processing and webhooks

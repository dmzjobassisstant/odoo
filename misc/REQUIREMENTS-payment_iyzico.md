# Module: payment_iyzico
**Name:** Payment Provider: Iyzico
**Version:** (inherited from payment)
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'iyzico'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `iyzico_key_id` | Char | Yes | Iyzico API Key |
| `iyzico_key_secret` | Char | Yes | Iyzico API secret |

## Supported Currencies
CHF, EUR, GBP, IRR, NOK, RUB, TRY, USD

## Default Payment Method Codes
`card`, `mastercard`, `visa`, `amex`, `troy`

## Security
No separate security file.

## Controllers
- `main.py`: Handles Iyzico payment processing and webhook (`/payment/iyzico/webhook`)

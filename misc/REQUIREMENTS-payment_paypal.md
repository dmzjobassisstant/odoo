# Module: payment_paypal
**Name:** Payment Provider: PayPal
**Version:** 2.0
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'paypal'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `paypal_email_account` | Char | Yes | PayPal email account |
| `paypal_client_id` | Char | Yes | PayPal client ID |
| `paypal_client_secret` | Char | No | PayPal client secret |
| `paypal_access_token` | Char | No | OAuth access token (internal) |
| `paypal_access_token_expiry` | Datetime | No | OAuth token expiry |
| `paypal_webhook_id` | Char | No | PayPal webhook ID |

## Supported Currencies
CAD, CZK, DKK, EUR, HKD, HUF, ILS, JPY, MYR, MXN, TWD, NZD, NOK, PHP, PLN, GBP, RUB, SGD, SEK, CHF, THB, USD

## Default Payment Method Codes
`paypal`

## Security
No separate security file.

## Controllers
- `main.py`: Handles PayPal payment processing and webhooks

# Module: payment_mollie
**Name:** Payment Provider: Mollie
**Version:** 1.0
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'mollie'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `mollie_api_key` | Char | Yes | Mollie API key |

## Supported Currencies
AED, AUD, BGN, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HRK, HUF, ILS, ISK, JPY, MXN, MYR, NOK, NZD, PHP, PLN, RON, RUB, SEK, SGD, THB, TWD, USD, ZAR

## Security
No separate security file.

## Controllers
- `main.py`: Handles Mollie payment processing and webhooks

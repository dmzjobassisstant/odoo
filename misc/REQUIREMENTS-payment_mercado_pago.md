# Module: payment_mercado_pago
**Name:** Payment Provider: Mercado Pago
**Version:** 1.0
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'mercado_pago'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `mercado_pago_account_country_id` | Many2one | Yes | Account country (`res.country`) |
| `mercado_pago_access_token` | Char | No | OAuth access token |
| `mercado_pago_access_token_expiry` | Datetime | No | OAuth token expiry |
| `mercado_pago_refresh_token` | Char | No | OAuth refresh token |
| `mercado_pago_public_key` | Char | No | Mercado Pago public key |

## Supported Countries
AR, BO, BR, CL, CO, CR, DO, EC, GT, HN, MX, NI, PA, PY, PE, SV, UY, VE

## Supported Currencies
Country-to-currency mapping: ARS, BOB, BRL, CLP, COP, CRC, DOP, USD, GTQ, HNL, MXN, NIO, PYG, PEN, SVC (see const.py for full mapping)

## OAuth Support
Yes — supports OAuth authentication (computed field `_compute_mercado_pago_is_oauth_supported`).

## Security
No separate security file.

## Controllers
- `payment.py`: Main payment processing
- `onboarding.py`: OAuth onboarding flow

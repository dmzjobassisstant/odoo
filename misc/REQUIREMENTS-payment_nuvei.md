# Module: payment_nuvei
**Name:** Payment Provider: Nuvei
**Version:** (inherited from payment)
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'nuvei'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `nuvei_merchant_identifier` | Char | Yes | Nuvei merchant identifier |
| `nuvei_site_identifier` | Char | Yes | Nuvei site identifier |
| `nuvei_secret_key` | Char | Yes | Nuvei secret key |

## Default Payment Method Codes
`card`, `visa`, `mastercard`, `amex`, `discover`, `tarjeta_mercadopago`, `naranja`

## Supported Payment Methods (via mapping)
astropay, boleto, card, nuvei_local, oxxopay, pix, pse, spei, webpay

## Special Methods
- **Integer methods** (no decimals): `webpay`
- **Full name required**: `boleto`

## Supported Currencies
PEN, USD, UYU (see const.py)

## Security
No separate security file.

## Controllers
- `main.py`: Handles Nuvei payment processing and webhooks
